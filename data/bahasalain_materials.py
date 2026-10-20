"""Kurikulum Bahasa Pemrograman Lain.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

BAHASALAIN_BAB = [
    {
        "judul": "Cara Membaca Bahasa Baru",
        "ket": "Paradigma, sistem tipe, model memori, dan cara cepat belajar bahasa ke-N.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Skrip dan Otomasi Sistem",
        "ket": "PowerShell, Perl, dan peta bahasa skrip untuk mengotomasi komputer.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Lua dan Bahasa Skrip Game",
        "ket": "Lua sebagai bahasa tertanam, GDScript di Godot, dan skrip game lain.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Swift dan Dart untuk Aplikasi",
        "ket": "Bahasa di balik aplikasi Apple dan Flutter, plus warisan Objective-C.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Bahasa Data dan Sains",
        "ket": "R, MATLAB/Octave, dan peta bahasa sains serta bahasa array.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "JVM dan .NET di Luar Java dan C#",
        "ket": "Scala, Groovy, dan F#: bahasa lain yang menumpang mesin yang sama.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "BEAM: Elixir, Erlang, dan Gleam",
        "ket": "Bahasa untuk sistem yang melayani banyak koneksi dan tahan gangguan.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Fungsional Murni",
        "ket": "Haskell dan peta bahasa fungsional serta bahasa yang dikompilasi ke JavaScript.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
    {
        "judul": "Lisp, Logika, dan Bukti",
        "ket": "Keluarga Lisp, Prolog, dan Lean: kode sebagai data, aturan, dan bukti.",
        "tingkat": "mahir",
        "jumlah": 2,
    },
    {
        "judul": "Bahasa Sistem dan Tingkat Rendah",
        "ket": "Assembly, Zig, dan generasi baru pengganti C dan C++.",
        "tingkat": "mahir",
        "jumlah": 4,
    },
    {
        "judul": "Enterprise dan Kode Warisan",
        "ket": "COBOL, VBA, ERP/CRM, dialek SQL prosedural, dan sistem lama yang masih hidup.",
        "tingkat": "mahir",
        "jumlah": 5,
    },
    {
        "judul": "Perangkat Keras dan Industri",
        "ket": "Verilog/VHDL, MicroPython, dan bahasa PLC di pabrik.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
    {
        "judul": "Smart Contract, Konfigurasi, dan Proyek Akhir",
        "ket": "Solidity dan kawan-kawan, bahasa konfigurasi, lalu interpreter buatanmu sendiri.",
        "tingkat": "mahir",
        "jumlah": 2,
    },
]

BAHASALAIN_MATERIALS = [
    {
        "title": "1. Peta Paradigma Pemrograman",
        "sections": [
            {
                "body": [
                    "Kurikulum ini memperkenalkan puluhan bahasa. Kalau tiap bahasa",
                    "dipelajari dari nol, kamu bakal capek duluan. Untungnya hampir semua",
                    "bahasa bisa dikelompokkan menurut paradigmanya.",
                    "",
                    "Paradigma itu cara berpikir yang dituntut sebuah bahasa waktu kamu",
                    "menyusun program. Gampangnya begini. Resep masakan menyuruh kamu",
                    "mengerjakan langkah satu per satu. Daftar belanja cuma bilang barang",
                    "apa yang dibutuhkan, urutan mengambilnya terserah kamu. Dua-duanya",
                    "bikin kamu sampai di hasil yang sama, tapi cara berpikirnya beda.",
                    "",
                    "Sekali kamu bisa menebak paradigma sebuah potongan kode, kamu juga",
                    "bisa menebak apa yang perlu dicari di dokumentasinya. Bahasa",
                    "fungsional, misalnya, hampir pasti punya map dan filter. Bahasa logika",
                    "pasti punya cara menulis fakta dan aturan.",
                    "",
                    "Kebanyakan bahasa populer sekarang multiparadigma. Python yang sudah",
                    "kamu kenal bisa ditulis imperatif, berorientasi objek, dan sedikit",
                    "fungsional. Jadi paradigma lebih tepat dibaca sebagai gaya yang",
                    "paling didorong sebuah bahasa, bukan pagar yang mengurung.",
                ],
            },
            {
                "heading": "Imperatif dan fungsional di Python",
                "code": """nilai = [70, 85, 60, 90]

# imperatif: ubah variabel langkah demi langkah
total = 0
for n in nilai:
    if n >= 70:
        total += n
print(total)

# fungsional: rangkai fungsi, tanpa mengubah variabel
print(sum(filter(lambda n: n >= 70, nilai)))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  245",
                    "  245",
                    "",
                    "Versi pertama itu gaya imperatif. Kamu menyuruh komputer mengerjakan",
                    "langkah demi langkah, dan variabel total berubah terus. Bahasa",
                    "prosedural seperti C dan Pascal adalah imperatif yang dikelompokkan",
                    "ke dalam prosedur atau fungsi.",
                    "",
                    "Versi kedua gaya fungsional. Nggak ada variabel yang diubah. Data",
                    "dialirkan lewat fungsi: saring dulu, lalu jumlahkan. Bahasa yang",
                    "dibangun penuh di atas gaya ini misalnya Haskell, F#, dan Elixir.",
                    "Di Haskell, program yang sama cuma satu baris:",
                    "",
                    "  main = print (sum (filter (>= 70) [70, 85, 60, 90]))",
                ],
            },
            {
                "heading": "Tiga rasa OOP: kelas, prototipe, kirim pesan",
                "bahasa": "smalltalk",
                "code": """| nilai lulus total |
nilai := #(70 85 60 90).
lulus := nilai select: [:n | n >= 70].
total := lulus inject: 0 into: [:a :b | a + b].
Transcript show: total printString; cr.""",
            },
            {
                "body": [
                    "OOP, singkatan dari object-oriented programming, menyatukan data dan",
                    "fungsi yang mengolahnya ke dalam objek. Tapi caranya ada tiga rasa.",
                    "",
                    "  - Berbasis kelas. Kamu menulis cetakan (class) dulu, lalu membuat",
                    "    objek dari cetakan itu. Java, C#, Kotlin, dan Python memakai cara",
                    "    ini.",
                    "  - Berbasis prototipe. Nggak ada cetakan. Objek baru dibuat dengan",
                    "    meminjam objek lain yang sudah ada. JavaScript dan Lua memakai",
                    "    cara ini, dan kamu bakal melihatnya lagi di materi Lua.",
                    "  - Kirim pesan. Semua hal adalah objek, dan semua kerja terjadi",
                    "    karena satu objek mengirim pesan ke objek lain. Smalltalk adalah",
                    "    bahasa yang paling murni memakai cara ini.",
                    "",
                    "Kode di atas ditulis dalam Smalltalk (dialek Pharo). Perhatikan baris",
                    "nilai select: [...]. Itu artinya kirim pesan select: ke objek nilai,",
                    "dengan blok kode sebagai argumennya. Bahkan 3 + 4 di Smalltalk dibaca",
                    "\"kirim pesan + dengan argumen 4 ke objek 3\". Smalltalk jarang dipakai",
                    "untuk kerja hari ini, tapi idenya menurun ke Objective-C dan Ruby.",
                ],
            },
            {
                "heading": "Logika: Prolog",
                "bahasa": "prolog",
                "code": """orangtua(budi, ani).
orangtua(ani, citra).
kakek(X, Z) :- orangtua(X, Y), orangtua(Y, Z).

% ?- kakek(budi, Siapa).
% Siapa = citra.""",
            },
            {
                "body": [
                    "Di paradigma logika kamu nggak menulis langkah sama sekali. Kamu",
                    "menulis fakta (budi orang tua ani) dan aturan (X kakek Z kalau X",
                    "orang tua Y dan Y orang tua Z). Lalu kamu bertanya, dan mesinnya",
                    "mencari sendiri jawaban yang cocok. Prolog adalah wakil paling",
                    "terkenal paradigma ini, dan dibahas lebih dalam di bab Lisp, Logika,",
                    "dan Bukti.",
                ],
            },
            {
                "heading": "Array dan stack: APL dan Forth",
                "bahasa": "apl",
                "code": """nilai ← 70 85 60 90
+/ (nilai ≥ 70) / nilai
245""",
            },
            {
                "body": [
                    "Bahasa array mengolah seluruh daftar sekaligus, tanpa loop. Di APL,",
                    "nilai ≥ 70 menghasilkan 1 1 0 1. Tanda / di tengah memakai deretan",
                    "itu untuk menyaring, lalu +/ menjumlahkan semuanya. Simbol-simbolnya",
                    "aneh, tapi ide yang sama hidup di NumPy, R, MATLAB, dan q.",
                    "",
                    "Bahasa stack, disebut juga konkatenatif, menyimpan semua nilai di",
                    "satu tumpukan. Di Forth, 2 3 + . artinya taruh 2, taruh 3, jumlahkan",
                    "dua yang teratas, lalu cetak. Hasilnya 5. Nggak ada nama variabel",
                    "sama sekali. Forth masih dipakai di firmware kecil dan dibahas di bab",
                    "Bahasa Sistem dan Tingkat Rendah.",
                ],
            },
            {
                "heading": "Deklaratif dan visual: SQL, HTML, Scratch",
                "bahasa": "teks",
                "code": """when green flag clicked
say [Halo, Dunia!] for (2) seconds
repeat (4)
  move (100) steps
  turn right (90) degrees
end""",
            },
            {
                "body": [
                    "Bahasa deklaratif menjelaskan hasil yang diinginkan, lalu mesinnya",
                    "memutuskan caranya. Kamu sudah memakainya di kurikulum SQL (SELECT",
                    "cuma bilang data apa yang mau diambil) dan HTML (cuma bilang bagian",
                    "ini judul, bagian itu paragraf).",
                    "",
                    "Bahasa visual menyusun program dengan menyambung blok, bukan mengetik.",
                    "Contoh di atas notasi teks untuk Scratch, bahasa visual dari MIT. Di",
                    "antarmuka berbahasa Indonesia, blok pertamanya berbunyi \"ketika",
                    "bendera hijau diklik\". Program itu menyuruh tokoh berkata Halo,",
                    "lalu berjalan membentuk persegi. Scratch dipakai untuk mengenalkan",
                    "logika ke anak-anak. Buat kamu, ia berguna kalau suatu hari kamu",
                    "mengajar orang lain.",
                ],
            },
            {
                "heading": "Jebakan saat menebak paradigma",
                "body": [
                    "Jebakan: kata class di sebuah bahasa belum tentu berarti OOP gaya",
                    "Java. Di Haskell, class artinya typeclass, yaitu kumpulan fungsi yang",
                    "harus dimiliki sebuah tipe. Sebelum menyimpulkan, cek dulu dokumentasi",
                    "bahasanya.",
                    "",
                    "Tanda lain yang bisa dipakai:",
                    "  - Banyak := atau = di dalam loop, variabel diubah terus: imperatif.",
                    "  - Ada class, new, atau self dan this: OOP.",
                    "  - Fungsi dirangkai dengan |>, map, filter, tanpa loop: fungsional.",
                    "  - Baris berakhir titik dan ada :- di tengah: logika (Prolog).",
                    "  - Satu baris pendek penuh simbol yang mengolah seluruh daftar:",
                    "    bahasa array.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Satu aplikasi web biasa sudah mencampur beberapa paradigma. Query ke",
                    "database ditulis deklaratif dengan SQL, logika bisnisnya OOP di Java",
                    "atau C#, dan pengolahan daftarnya memakai stream atau LINQ yang",
                    "bergaya fungsional. Saat PKL, kamu juga bakal ketemu berkas yang",
                    "bahasanya belum kamu kenal sama sekali di repositori kantor.",
                    "",
                    "Kasus kecil: kamu menemukan berkas aturan.pl di repo kantor dan",
                    "diminta menjelaskan isinya ke mentor.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat ekstensinya. .pl bisa Perl atau Prolog, jadi jangan",
                    "     langsung menyimpulkan.",
                    "  2. Lihat bentuk barisnya. Kalau isinya baris seperti",
                    "     boleh_cuti(X) :- karyawan(X), masa_kerja(X, N), N >= 1.",
                    "     itu aturan Prolog.",
                    "  3. Baca tiap aturan sebagai kalimat: X boleh cuti kalau X karyawan",
                    "     dan masa kerjanya minimal satu tahun.",
                    "  4. Cari bagian yang memanggil berkas itu (misalnya program Python",
                    "     yang memakai pustaka pyswip) supaya tahu siapa yang bertanya.",
                    "  5. Tulis ringkasan satu paragraf: berkas ini daftar fakta dan aturan",
                    "     cuti, dan jawabannya dicari mesin Prolog.",
                ],
            },
        ],
    },
    {
        "title": "2. Sistem Tipe: Statis, Dinamis, Kuat, dan Bertahap",
        "sections": [
            {
                "body": [
                    "Tipe itu jenis sebuah nilai: bilangan bulat, teks, daftar, dan",
                    "seterusnya. Setiap bahasa punya aturan soal tipe, dan aturan itu",
                    "menentukan kapan kesalahanmu ketahuan.",
                    "",
                    "Untuk membaca sistem tipe bahasa apa pun, cukup tanya dua hal:",
                    "  1. Kapan tipe diperiksa? Sebelum program jalan (statis) atau",
                    "     sambil program jalan (dinamis)?",
                    "  2. Seberapa ketat? Apakah bahasa menolak mencampur tipe (kuat) atau",
                    "     mengubah salah satunya tanpa bilang-bilang (lemah)?",
                    "",
                    "Dua pertanyaan ini terpisah. Python dinamis tapi kuat. C statis tapi",
                    "cukup lemah. JavaScript dinamis dan lemah.",
                ],
            },
            {
                "heading": "Dinamis: error baru muncul saat barisnya jalan",
                "code": """def gandakan(x):
    return x * 2

print(gandakan(21))
print(gandakan("ha"))
try:
    print(gandakan(None))
except TypeError as e:
    print("TypeError:", e)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  42",
                    "  haha",
                    "  TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'",
                    "",
                    "Python nggak protes waktu fungsi gandakan ditulis. Ia baru protes",
                    "waktu baris gandakan(None) benar dijalankan. Kalau baris itu ada di",
                    "cabang if yang jarang dilewati, error-nya bisa lolos sampai dipakai",
                    "orang lain.",
                    "",
                    "Di bahasa statis seperti Java, Kotlin, Rust, atau Swift, kompilator",
                    "memeriksa tipe sebelum program boleh jalan. Kesalahan yang sama",
                    "ditolak di laptopmu, bukan di tangan pengguna.",
                ],
            },
            {
                "heading": "Lemah: JavaScript mengubah tipe tanpa bilang",
                "bahasa": "javascript",
                "code": """console.log("5" * 2);
console.log("5" + 2);
console.log(true + 1);
console.log([] + {});""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  10",
                    "  52",
                    "  2",
                    "  [object Object]",
                    "",
                    "Teks \"5\" dikali 2 jadi bilangan 10, tapi teks \"5\" ditambah 2 jadi",
                    "teks \"52\". Ini yang disebut konversi tipe implisit, dan itulah ciri",
                    "bahasa bertipe lemah. Python menolak \"5\" + 2 dengan TypeError,",
                    "karena itu Python disebut bertipe kuat walaupun dinamis. Perl dan PHP",
                    "termasuk lemah seperti JavaScript.",
                ],
            },
            {
                "heading": "Inferensi tipe: statis tanpa cerewet",
                "bahasa": "typescript",
                "code": """function gandakan(x: number): number {
  return x * 2;
}

let umur = 17;            // tipenya number, ditebak dari nilainya
const nama: string = "Ani";
console.log(gandakan(umur));
console.log(nama.toUpperCase());
// gandakan("ha");       // ditolak tsc sebelum program jalan""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  34",
                    "  ANI",
                    "",
                    "Dulu bahasa statis identik dengan menulis tipe di mana-mana. Sekarang",
                    "hampir semua bahasa statis punya inferensi tipe: kompilator menebak",
                    "tipe dari nilainya. Di contoh TypeScript tadi, umur nggak diberi",
                    "anotasi, tapi tsc tahu tipenya number. Swift (let umur = 17), Kotlin",
                    "(val umur = 17), Rust, dan Dart bekerja sama.",
                    "",
                    "Haskell paling jauh soal ini. Fungsi tambah x y = x + y nggak ditulis",
                    "tipenya sama sekali, dan kompilatornya tetap menyimpulkan bahwa",
                    "tambah menerima dua bilangan dengan tipe yang sama.",
                ],
            },
            {
                "heading": "Null dan optional",
                "bahasa": "swift",
                "code": "var kota: String? = nil\nprint(kota ?? \"tidak diketahui\")\n\nkota = \"Bandung\"\nif let k = kota {\n    print(\"Tinggal di \\(k)\")\n}",
            },
            {
                "body": [
                    "Null, atau nil, atau None, artinya \"nggak ada nilai\". Tony Hoare,",
                    "orang yang memperkenalkannya di bahasa Algol W tahun 1965, pernah",
                    "menyebutnya kesalahan bernilai miliaran dolar. Alasannya, hampir",
                    "setiap variabel boleh kosong tanpa ketahuan, dan program crash waktu",
                    "nilai kosong itu dipakai.",
                    "",
                    "Bahasa baru memisahkan dua tipe: String yang pasti berisi, dan",
                    "String? yang boleh kosong. Kompilator menolak kalau kamu memakai",
                    "String? seolah pasti berisi. Kamu wajib membukanya dulu, misalnya",
                    "dengan if let atau operator ?? yang memberi nilai cadangan. Swift,",
                    "Kotlin, Dart, dan C# modern memakai pola ini. Haskell memakai tipe",
                    "Maybe, Rust memakai Option.",
                ],
            },
            {
                "heading": "Tipe bertahap",
                "code": """def luas(p: int, l: int) -> int:
    return p * l

print(luas(3, 4))
print(luas("ab", 2))   # tetap jalan; mypy akan protes""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  12",
                    "  abab",
                    "",
                    "Tipe bertahap (gradual typing) artinya anotasi tipe boleh ditambahkan",
                    "sedikit demi sedikit ke bahasa dinamis. Di Python, anotasi seperti",
                    "p: int nggak memengaruhi jalannya program sama sekali. Yang membacanya",
                    "pemeriksa terpisah seperti mypy atau pyright.",
                    "",
                    "Pola yang sama ada di beberapa tempat:",
                    "  - TypeScript menambah tipe ke JavaScript.",
                    "  - Luau, turunan Lua di Roblox, punya mode --!strict.",
                    "  - Elixir sedang menambah pemeriksaan tipe bertahap sejak versi 1.17",
                    "    (2024), sedikit demi sedikit tiap rilis.",
                ],
            },
            {
                "heading": "Contoh Luau",
                "bahasa": "luau",
                "code": """--!strict
local function luas(p: number, l: number): number
    return p * l
end

print(luas(3, 4))
print(luas("3", 4)) -- ditolak pemeriksa tipe di mode strict""",
            },
            {
                "heading": "Lebih jauh: tipe dependen",
                "body": [
                    "Ada sistem tipe yang jauh lebih kuat lagi, namanya tipe dependen.",
                    "Tipenya boleh bergantung pada nilai, misalnya \"daftar yang panjangnya",
                    "tepat 3\". Dengan itu kompilator bisa membuktikan sifat program,",
                    "lebih dari sekadar memeriksa tipenya. Lean 4 dan Idris memakai ide ini. Untuk",
                    "sekarang cukup tahu namanya; Lean dibahas di bab Lisp, Logika, dan",
                    "Bukti.",
                    "",
                    "Jebakan: dinamis bukan berarti tanpa tipe. Nilai di Python tetap",
                    "punya tipe, cuma diperiksanya belakangan. Jadi kalimat \"Python nggak",
                    "punya tipe\" itu keliru.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak proyek JavaScript besar pindah ke TypeScript, dan banyak tim",
                    "Python memasang mypy atau pyright di pipeline CI. Alasannya sama:",
                    "error tipe lebih murah ditemukan di laptop daripada di server",
                    "produksi.",
                    "",
                    "Kasus kecil: form pendaftaran mengirim umur sebagai teks \"17\", lalu",
                    "fungsi hitung_tahun_lulus(umur) di Python crash dengan TypeError",
                    "waktu menjalankan umur + 1.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambahkan anotasi di fungsinya:",
                    "       def hitung_tahun_lulus(umur: int) -> int:",
                    "  2. Jalankan mypy pada proyek. Pemanggilan yang mengoper teks ke",
                    "     fungsi itu akan ditandai sebelum program jalan.",
                    "  3. Ubah teks jadi bilangan di tempat data masuk, yaitu di kode yang",
                    "     membaca form, dengan int(umur_teks).",
                    "  4. Tangani teks yang bukan angka dengan try/except ValueError, lalu",
                    "     tampilkan pesan ke pengguna.",
                    "  5. Tambahkan mypy ke CI supaya kesalahan serupa ketahuan saat pull",
                    "     request, bukan setelah rilis.",
                ],
            },
        ],
    },
    {
        "title": "3. Model Memori dan Mesin yang Menjalankan Kode",
        "sections": [
            {
                "body": [
                    "Setiap bahasa harus menjawab dua pertanyaan di belakang layar.",
                    "Pertama, siapa yang membersihkan memori yang sudah nggak dipakai?",
                    "Kedua, bagaimana kode yang kamu ketik berubah jadi instruksi yang",
                    "dimengerti prosesor?",
                    "",
                    "Jawabannya menentukan banyak hal yang kelihatan dari luar. Program",
                    "jadi cepat atau lambat, bisa jalan di semua sistem atau harus",
                    "dikompilasi ulang, dan jenis bug apa yang paling sering muncul.",
                ],
            },
            {
                "heading": "Stack dan heap",
                "code": """def tambah_nilai(daftar, n):
    daftar.append(n)     # objek di heap diubah
    n = 0                # cuma variabel lokal yang berubah

nilai = [70, 80]
x = 90
tambah_nilai(nilai, x)
print(nilai)
print(x)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  [70, 80, 90]",
                    "  90",
                    "",
                    "Memori program dibagi dua daerah. Stack berisi variabel lokal setiap",
                    "fungsi yang sedang berjalan. Begitu fungsi selesai, bagiannya di",
                    "stack langsung dibuang. Heap berisi objek yang umurnya bisa lebih",
                    "panjang dari fungsi yang membuatnya, seperti daftar nilai tadi.",
                    "",
                    "Variabel nilai cuma menyimpan alamat daftar di heap. Waktu",
                    "tambah_nilai mengubah daftar itu, yang di luar ikut berubah karena",
                    "objeknya sama. Sebaliknya, n = 0 cuma mengubah variabel lokal di",
                    "stack, jadi x tetap 90. Stack gampang dibersihkan. Masalahnya ada di",
                    "heap: siapa yang tahu kapan sebuah objek boleh dibuang?",
                ],
            },
            {
                "heading": "Manual: C, Zig, Odin",
                "bahasa": "c",
                "code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main(void) {\n    int n = 3;\n    int *nilai = malloc(n * sizeof(int));\n    if (nilai == NULL) return 1;\n    for (int i = 0; i < n; i++) {\n        nilai[i] = (i + 1) * 10;\n    }\n    printf(\"%d %d %d\\n\", nilai[0], nilai[1], nilai[2]);\n    free(nilai);\n    return 0;\n}",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  10 20 30",
                    "",
                    "Jawaban pertama: programmer sendiri yang membersihkan. Di C, malloc",
                    "meminta sepotong heap dan free mengembalikannya. Cepat dan bisa",
                    "diatur sampai ke byte terakhir. Risikonya juga jelas. Lupa free",
                    "berarti memori bocor. Memakai pointer sesudah free (use after free)",
                    "berarti program membaca sampah, dan itu sumber banyak celah keamanan.",
                    "",
                    "Zig dan Odin juga manual, tapi lebih tertib. Zig mewajibkan kamu",
                    "menyebut alokator yang dipakai dan menyediakan defer supaya free",
                    "nggak lupa ditulis. Keduanya dibahas di bab Bahasa Sistem dan",
                    "Tingkat Rendah.",
                ],
            },
            {
                "heading": "Garbage collector",
                "body": [
                    "Jawaban kedua: sebuah program pembantu bernama garbage collector",
                    "(GC) mencari objek yang sudah nggak dirujuk siapa pun, lalu",
                    "membuangnya. Kamu cukup membuat objek; membersihkannya urusan GC.",
                    "",
                    "  - JVM (Java, Kotlin, Scala, Groovy), .NET (C#, F#), dan Go memakai",
                    "    GC yang sesekali berjalan di samping programmu.",
                    "  - Python menghitung jumlah rujukan tiap objek, ditambah GC untuk",
                    "    rujukan yang melingkar.",
                    "  - Mesin virtual BEAM (Erlang, Elixir) memberi tiap proses ringan",
                    "    heap sendiri. GC membersihkan satu proses kecil dalam satu waktu,",
                    "    jadi seluruh sistem nggak perlu berhenti bersamaan.",
                    "",
                    "Harga GC: program butuh memori lebih besar, dan kadang ada jeda",
                    "singkat waktu GC bekerja. Untuk aplikasi web dan bisnis, harga itu",
                    "biasanya pantas.",
                ],
            },
            {
                "heading": "ARC di Swift dan Objective-C",
                "bahasa": "swift",
                "code": "class Pemain {\n    let nama: String\n    init(nama: String) { self.nama = nama }\n    deinit { print(\"\\(nama) dibersihkan\") }\n}\n\nvar a: Pemain? = Pemain(nama: \"Ani\")\nvar b = a      // hitungan rujukan jadi 2\na = nil        // tinggal 1, belum dibersihkan\nb = nil        // 0: deinit jalan, tercetak \"Ani dibersihkan\"",
            },
            {
                "body": [
                    "Jawaban ketiga ada di tengah. Swift dan Objective-C memakai ARC,",
                    "automatic reference counting. Kompilator menyisipkan kode penambah",
                    "dan pengurang hitungan rujukan di tempat yang tepat. Begitu hitungan",
                    "jadi nol, objek dibuang saat itu juga, tanpa GC yang berjalan",
                    "terpisah.",
                    "",
                    "Kelemahannya rujukan melingkar. Kalau objek A merujuk B dan B merujuk",
                    "A, hitungannya nggak pernah nol. Di Swift kamu memutusnya dengan",
                    "kata weak pada salah satu rujukan.",
                ],
            },
            {
                "heading": "Kepemilikan di Rust",
                "bahasa": "rust",
                "code": """fn main() {
    let a = String::from("halo");
    let b = a;              // kepemilikan pindah ke b
    // println!("{}", a);   // galat kompilasi: a sudah dipindah
    println!("{}", b);
}   // b keluar lingkup, memorinya dibebaskan di sini""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  halo",
                    "",
                    "Jawaban keempat datang dari Rust: kepemilikan (ownership). Setiap",
                    "nilai di heap punya tepat satu pemilik. Waktu pemiliknya keluar dari",
                    "lingkup, memorinya dibebaskan. Kompilator memeriksa aturan ini",
                    "sebelum program jalan, jadi use after free ditolak sejak awal dan",
                    "nggak ada GC yang perlu berjalan. Harganya, aturannya harus dipelajari",
                    "dulu, dan kurikulum Rust membahasnya panjang.",
                ],
            },
            {
                "heading": "Dari kode ke mesin",
                "bahasa": "teks",
                "code": """C, Rust, Go, Swift   kode -> kompilator -> berkas mesin (per OS dan CPU)
Python, Ruby, Lua    kode -> interpreter (lewat bytecode internal)
Java, Kotlin, Scala  kode -> bytecode .class -> JVM + JIT
C#, F#, VB.NET       kode -> IL -> runtime .NET + JIT
Elixir, Erlang       kode -> bytecode .beam -> BEAM
TypeScript, Elm      kode -> JavaScript (transpiler)
Rust, C, Zig         kode -> WebAssembly -> browser atau runtime Wasm""",
            },
            {
                "body": [
                    "Kompilasi AOT (ahead of time) menerjemahkan seluruh kode jadi berkas",
                    "mesin sebelum dijalankan. Hasilnya cepat, tapi berkas untuk Linux",
                    "x86-64 nggak jalan di Mac ARM. Kamu harus kompilasi per sistem.",
                    "",
                    "Interpreter membaca kode lalu langsung menjalankannya. Python pun",
                    "menerjemahkan dulu ke bytecode, yaitu instruksi untuk mesin",
                    "khayalan, lalu menjalankan bytecode itu.",
                    "",
                    "Mesin virtual seperti JVM, runtime .NET, dan BEAM menjalankan bytecode",
                    "yang sama di sistem mana pun. Karena itu berkas .jar bisa",
                    "dibawa ke Windows dan Linux. JIT (just in time) adalah kompilator di",
                    "dalam mesin virtual yang mengubah bagian yang sering jalan jadi kode",
                    "mesin sambil program berjalan.",
                    "",
                    "Transpiler menerjemahkan satu bahasa ke bahasa lain, biasanya ke",
                    "JavaScript. WebAssembly (Wasm) adalah format bytecode yang bisa",
                    "dijalankan browser maupun runtime di server.",
                ],
            },
            {
                "heading": "Mengintip bytecode Python",
                "code": """import dis

def tambah(a, b):
    return a + b

dis.dis(tambah)""",
            },
            {
                "body": [
                    "Hasilnya daftar instruksi seperti LOAD_FAST, BINARY_OP (+), dan",
                    "RETURN_VALUE. Nama persisnya berubah sedikit antarversi Python, jadi",
                    "jangan dihafal. Yang penting kamu lihat sendiri bahwa \"bahasa yang",
                    "diinterpretasi\" pun punya tahap terjemahan.",
                    "",
                    "Jebakan: punya GC bukan jaminan memori nggak bocor. Objek yang masih",
                    "dirujuk, misalnya disimpan di daftar global yang terus bertambah,",
                    "nggak akan pernah dibuang GC.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Layanan web berbahasa Python, Java, atau Node yang berjalan",
                    "berminggu-minggu sering mati karena kehabisan memori. Penyebab",
                    "paling umum adalah cache di memori yang nggak pernah dibatasi:",
                    "tiap permintaan menambah isi, nggak ada yang menghapus, dan GC",
                    "nggak boleh membuangnya karena masih dirujuk.",
                    "",
                    "Kasus kecil: layanan Python yang menyimpan hasil hitungan di dict",
                    "global memakai memori makin besar setiap hari sampai server",
                    "mematikannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pantau pemakaian memori prosesnya, misalnya dengan top atau ps",
                    "     selama beberapa jam, dan pastikan memang naik terus.",
                    "  2. Nyalakan tracemalloc di Python untuk melihat baris kode mana",
                    "     yang paling banyak mengalokasikan memori:",
                    "       import tracemalloc",
                    "       tracemalloc.start()",
                    "  3. Kalau tersangkanya dict cache, ganti dengan cache berbatas:",
                    "       from functools import lru_cache",
                    "       @lru_cache(maxsize=1000)",
                    "  4. Ulangi pemantauan. Grafik memori yang mendatar artinya cache",
                    "     sudah membuang isi lama sendiri.",
                ],
            },
        ],
    },
    {
        "title": "4. Belajar Bahasa ke-N dengan Cepat",
        "sections": [
            {
                "body": [
                    "Bahasa kedua biasanya yang paling berat. Sesudah itu polanya mulai",
                    "kelihatan: tiap bahasa menjawab pertanyaan yang sama, cuma dengan",
                    "sintaks yang beda. Materi ini memberi kamu resep yang sama untuk",
                    "setiap bahasa baru, termasuk yang nggak ada di kurikulum ini.",
                ],
            },
            {
                "heading": "Sepuluh pertanyaan",
                "body": [
                    "Setiap kali bertemu bahasa baru, cari jawaban sepuluh pertanyaan ini,",
                    "kira-kira dengan urutan begini:",
                    "",
                    "  1. Halo dunia. Bagaimana memasang dan menjalankan program pertama?",
                    "  2. Tipe. Statis atau dinamis, kuat atau lemah, bagaimana null-nya?",
                    "  3. Koleksi. Apa padanan list, dict, dan set di bahasa ini?",
                    "  4. Fungsi. Bagaimana menulis fungsi, parameter bawaan, dan lambda?",
                    "  5. Error. Pakai exception, nilai kembalian, atau tipe Result?",
                    "  6. Modul dan paket. Bagaimana memecah berkas dan memasang pustaka?",
                    "  7. Konkurensi. Thread, async/await, proses ringan, atau coroutine?",
                    "  8. Tooling. Apa formatter, linter, alat tes, dan pengelola proyeknya?",
                    "  9. Idiom. Bagaimana programmer bahasa ini biasa menulis hal umum?",
                    "  10. Ekosistem dan status. Dipakai di bidang apa, aktif atau menurun?",
                    "",
                    "Pertanyaan 1 sampai 5 biasanya selesai dalam sehari dua hari. Nomor 6",
                    "sampai 10 butuh waktu lebih lama, karena jawabannya baru terasa",
                    "waktu kamu menulis program yang lebih besar dari satu berkas.",
                ],
            },
            {
                "heading": "Contoh: Ruby lewat sepuluh pertanyaan",
                "bahasa": "ruby",
                "code": """# 1. halo dunia
puts "Halo, Dunia!"

# 2-3. tipe dan koleksi
nilai = [70, 85, 60, 90]
siswa = { "ani" => 85, "budi" => 70 }

# 4. fungsi
def rata(daftar)
  daftar.sum.to_f / daftar.size
end

# 5. error
begin
  Integer("abc")
rescue ArgumentError => e
  puts "galat: #{e.message}"
end

puts rata(nilai)
puts siswa.select { |_, n| n >= 80 }.keys.inspect""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Halo, Dunia!",
                    "  galat: invalid value for Integer(): \"abc\"",
                    "  76.25",
                    "  [\"ani\"]",
                    "",
                    "Dari satu berkas pendek ini, lima pertanyaan pertama sudah terjawab.",
                    "Ruby dinamis dan kuat, punya array dan hash, fungsi ditulis dengan",
                    "def ... end, dan error memakai exception dengan begin dan rescue.",
                    "Idiomnya juga mulai kelihatan: blok { |_, n| ... } dipakai di",
                    "mana-mana.",
                ],
            },
            {
                "heading": "Terjemahkan program yang sudah kamu kuasai",
                "code": """nilai = [70, 80, 90]
for i, n in enumerate(nilai, start=1):
    print(f"{i}: {n}")
print(f"rata-rata: {sum(nilai) / len(nilai):.1f}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  1: 70",
                    "  2: 80",
                    "  3: 90",
                    "  rata-rata: 80.0",
                    "",
                    "Cara belajar paling cepat adalah menulis ulang program kecil yang",
                    "sudah kamu pahami. Logikanya sudah di kepala, jadi seluruh tenagamu",
                    "tercurah ke sintaks dan idiom. Program Python di atas, kalau ditulis",
                    "dalam Lua, jadi seperti ini:",
                ],
            },
            {
                "heading": "Versi Lua",
                "bahasa": "lua",
                "code": """local nilai = {70, 80, 90}
local total = 0
for i = 1, #nilai do
  print(i .. ": " .. nilai[i])
  total = total + nilai[i]
end
print(string.format("rata-rata: %.1f", total / #nilai))""",
            },
            {
                "body": [
                    "Dari terjemahan sekecil ini kamu langsung menemukan tiga perbedaan:",
                    "indeks Lua mulai dari 1, panjang daftar ditulis #nilai, dan teks",
                    "disambung dengan .. bukan +. Program kecil yang cocok untuk",
                    "diterjemahkan misalnya FizzBuzz, menghitung kata di sebuah teks, dan",
                    "rata-rata nilai dari input.",
                ],
            },
            {
                "heading": "Cek versi sebelum membaca tutorial",
                "bahasa": "terminal",
                "code": """lua -v
perl -v
dotnet --version
swift --version
pwsh --version""",
            },
            {
                "body": [
                    "Dokumentasi resmi hampir selalu lebih bisa dipercaya daripada artikel",
                    "acak. Cari tiga halaman di situs resmi bahasanya: tur singkat (biasanya",
                    "bernama tour, getting started, atau learn), referensi pustaka standar,",
                    "dan catatan rilis (release notes atau changelog).",
                    "",
                    "Catatan rilis menjawab pertanyaan yang sering bikin pemula bingung:",
                    "kenapa contoh di tutorial nggak jalan di komputerku. Penyebabnya",
                    "biasanya beda versi. Tutorial Godot 3 nggak cocok untuk Godot 4,",
                    "kode Swift 5 bisa ditolak mode Swift 6, dan Python 2 sudah lama mati.",
                    "Jadi cek versimu dulu dengan perintah di atas, lalu cek versi yang",
                    "dipakai tutorialnya.",
                ],
            },
            {
                "heading": "Halo Dunia di enam bahasa",
                "bahasa": "teks",
                "code": "Lua    print(\"Halo, Dunia!\")\nPerl   print \"Halo, Dunia!\\n\";\nRuby   puts \"Halo, Dunia!\"\nTcl    puts \"Halo, Dunia!\"\nSwift  print(\"Halo, Dunia!\")\nDart   void main() { print('Halo, Dunia!'); }",
            },
            {
                "heading": "Cara memakai kurikulum ini",
                "body": [
                    "Tiap bab sesudah ini memperkenalkan bahasa dengan urutan sepuluh",
                    "pertanyaan tadi. Ada dua jenis materi:",
                    "  - Materi bahasa (misalnya Lua: Table, Fungsi, dan Indeks dari",
                    "    Satu) membahas satu bahasa cukup dalam sampai kamu bisa menulis",
                    "    program kecil.",
                    "  - Materi peta (judulnya diawali Peta) membahas beberapa bahasa",
                    "    sekaligus: apa itu, dipakai di mana, Halo Dunia, dan statusnya.",
                    "    Tujuannya supaya kamu mengenali bahasa itu saat bertemu, bukan",
                    "    supaya langsung mahir.",
                    "",
                    "Latihan di kurikulum ini ditulis dalam Python, karena hampir semua",
                    "bahasa di sini belum terpasang di komputermu. Polanya selalu sama:",
                    "kamu membaca kode bahasa lain di soal, lalu meniru logikanya atau",
                    "membuat versi mini dari ide utamanya.",
                    "",
                    "Jebakan: menulis Python dengan sintaks bahasa lain. Program Lua yang",
                    "isinya terjemahan kata per kata dari Python memang jalan, tapi orang",
                    "Lua akan susah membacanya. Begitu sintaks dasar dikuasai, cari",
                    "panduan gaya resmi dan baca kode proyek sumber terbuka di bahasa itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Anak PKL sering ditempatkan di tim yang memakai bahasa di luar yang",
                    "diajarkan sekolah, misalnya skrip Perl di server lama atau",
                    "Jenkinsfile berbahasa Groovy. Yang dinilai mentor biasanya seberapa",
                    "cepat kamu bisa membaca kode itu dan membuat perubahan kecil dengan",
                    "aman. Hafalan sintaks jarang ditanyakan.",
                    "",
                    "Kasus kecil: hari pertama PKL, kamu diminta menambah satu kolom di",
                    "laporan yang dibuat skrip Lua, padahal kamu belum pernah menulis",
                    "Lua.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jawab pertanyaan nomor 1 dulu: cari tahu cara skrip itu",
                    "     dijalankan (lua laporan.lua) dan jalankan sekali tanpa diubah.",
                    "  2. Baca kodenya sambil mencari jawaban pertanyaan 2 sampai 4:",
                    "     tipe datanya apa, koleksinya apa, fungsinya di mana.",
                    "  3. Tulis program Lua sekecil mungkin di berkas terpisah yang meniru",
                    "     bagian yang mau diubah, sampai kamu yakin dengan sintaksnya.",
                    "  4. Ubah skrip aslinya sedikit, jalankan, dan bandingkan keluarannya",
                    "     dengan sebelum diubah.",
                    "  5. Catat jawaban sepuluh pertanyaan untuk Lua di catatanmu. Lain",
                    "     kali ketemu Lua, kamu tinggal membaca catatan itu.",
                ],
            },
        ],
    },
    {
        "title": "5. PowerShell dan Pipeline Objek",
        "sections": [
            {
                "body": [
                    "PowerShell itu shell sekaligus bahasa skrip buatan Microsoft. Dulu ia",
                    "cuma ada di Windows. Sejak versi 6 (2018) ia jalan juga di Linux dan",
                    "macOS, dan sekarang dikenal sebagai PowerShell 7. Versi stabil",
                    "terbaru saat materi ini ditulis (Oktober 2026) adalah 7.6.7, rilis 13",
                    "Oktober 2026, dan jalur 7.6 berstatus LTS (didukung jangka panjang).",
                    "Lisensinya MIT.",
                    "",
                    "Di Survei Stack Overflow 2026, PowerShell dipakai 24,6% responden.",
                    "Angka itu yang tertinggi di antara semua bahasa yang belum punya",
                    "kurikulum sendiri di aplikasi ini. Alasannya sederhana: hampir semua",
                    "admin Windows, Microsoft 365, dan Azure memakainya setiap hari.",
                    "",
                    "Kalau kamu sudah menyelesaikan kurikulum Bash, kamu sudah kenal",
                    "pipeline: keluaran satu perintah dialirkan ke perintah berikutnya",
                    "lewat tanda |. PowerShell memakai tanda yang sama, tapi yang mengalir",
                    "di dalamnya beda. Itu inti materi ini.",
                ],
            },
            {
                "heading": "Pipeline teks di Bash",
                "bahasa": "bash",
                "code": "printf '%s\\n' \"firefox 35 820\" \"code 12 640\" \"bash 0 5\" \"gnome-shell 18 410\" |\n  awk '$2 > 10' |\n  sort -k2 -nr |\n  awk '{ print $1, $2 }'",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  firefox 35",
                    "  gnome-shell 18",
                    "  code 12",
                    "",
                    "Di Bash, yang mengalir di pipeline adalah teks. Tiap baris cuma",
                    "deretan huruf. Supaya awk dan sort bisa bekerja, kamu harus tahu",
                    "bahwa CPU ada di kolom kedua, dan kolom dipisah spasi. Kalau suatu",
                    "hari ada nama proses yang mengandung spasi, kolomnya bergeser dan",
                    "hasilnya salah tanpa pesan apa pun.",
                ],
            },
            {
                "heading": "Pipeline objek di PowerShell",
                "bahasa": "powershell",
                "code": """Get-Process |
    Where-Object CPU -gt 10 |
    Sort-Object CPU -Descending |
    Select-Object -First 3 Name, CPU""",
            },
            {
                "body": [
                    "Di PowerShell, Get-Process nggak mengeluarkan teks. Ia mengeluarkan",
                    "objek .NET, satu objek per proses, lengkap dengan properti seperti",
                    "Name, Id, CPU, dan WorkingSet64. Properti CPU berisi total detik",
                    "prosesor yang sudah dipakai proses itu.",
                    "",
                    "Perintah sesudahnya memakai nama properti, bukan nomor kolom:",
                    "  - Where-Object CPU -gt 10 menyaring objek yang CPU-nya di atas 10.",
                    "  - Sort-Object CPU -Descending mengurutkan dari yang terbesar.",
                    "  - Select-Object -First 3 Name, CPU mengambil tiga objek pertama",
                    "    dan cuma menyisakan dua properti itu.",
                    "",
                    "Baru di ujung pipeline, PowerShell mengubah objek jadi tabel teks",
                    "untuk ditampilkan di layar. Hasilnya kira-kira seperti ini (angkanya",
                    "tentu beda di komputermu):",
                    "",
                    "  Name             CPU",
                    "  ----             ---",
                    "  firefox      2553.17",
                    "  gnome-shell   973.94",
                    "  code          859.82",
                ],
            },
            {
                "heading": "Cmdlet dan Get-Member",
                "bahasa": "powershell",
                "code": """Get-Process -Id $PID | Get-Member -MemberType Property

Get-Date -Year 2026 -Month 10 -Day 19 |
    Select-Object Year, Month, DayOfWeek""",
            },
            {
                "body": [
                    "Perintah bawaan PowerShell disebut cmdlet (dibaca command-let). Semua",
                    "namanya berpola Kata-kerja-Benda: Get-Process, Sort-Object,",
                    "Remove-Item. Kata kerjanya diambil dari daftar resmi, dan kamu bisa",
                    "melihat daftarnya dengan Get-Verb. Pola ini membantu menebak: kalau",
                    "ada Get-Service, hampir pasti ada Stop-Service dan Start-Service.",
                    "",
                    "Get-Member adalah teman terbaikmu. Ia menampilkan semua properti dan",
                    "metode objek yang lewat di pipeline, jadi kamu tahu nama apa yang",
                    "bisa dipakai di Where-Object dan Select-Object. Perintah kedua di",
                    "atas mencetak tabel kecil berisi tahun 2026, bulan 10, dan hari",
                    "Monday, karena 19 Oktober 2026 memang hari Senin.",
                ],
            },
            {
                "heading": "Perbandingan: -eq, -lt, -gt",
                "bahasa": "powershell",
                "code": """$umur = 17
if ($umur -ge 17) { "Boleh bikin KTP" }

"abc" -eq "ABC"     # True: teks dibandingkan tanpa peduli huruf besar
"abc" -ceq "ABC"    # False: awalan c berarti peka huruf besar
1 -eq "1"           # True: sisi kanan diubah jadi tipe sisi kiri
"10" -lt 9          # True: kiri teks, jadi dibandingkan sebagai teks
10 -lt "9"          # False: kiri angka, jadi dibandingkan sebagai angka""",
            },
            {
                "body": [
                    "PowerShell nggak memakai == dan < untuk membandingkan. Gantinya",
                    "-eq (sama), -ne (beda), -lt (kurang dari), -le, -gt, dan -ge.",
                    "Alasannya, tanda > dan < sudah dipakai untuk mengalihkan keluaran ke",
                    "berkas, sama seperti di Bash.",
                    "",
                    "Jebakan: menulis if ($a > 5) nggak membandingkan apa pun. Perintah",
                    "itu menulis nilai $a ke berkas bernama 5 di folder aktif, dan kondisi",
                    "if-nya selalu dianggap salah. Program tetap jalan tanpa pesan error.",
                    "",
                    "Perhatikan juga dua baris terakhir contoh tadi. Tipe sisi kiri yang",
                    "menentukan cara membandingkan. \"10\" -lt 9 dibandingkan sebagai teks,",
                    "dan teks \"10\" memang lebih kecil daripada \"9\" karena huruf pertamanya",
                    "1. Kalau datamu berasal dari berkas CSV, semua kolomnya teks, jadi",
                    "ubah dulu jadi angka dengan [int] atau [double].",
                ],
            },
            {
                "heading": "Meniru pipeline objek dengan Python",
                "code": """berkas = [
    {"nama": "video.mp4", "ukuran": 734003200},
    {"nama": "catatan.txt", "ukuran": 2048},
    {"nama": "foto.jpg", "ukuran": 3145728},
    {"nama": "arsip.zip", "ukuran": 52428800},
]
MB = 1024 * 1024

def where(data, syarat):
    return [x for x in data if syarat(x)]

def sort_desc(data, kunci):
    return sorted(data, key=lambda x: x[kunci], reverse=True)

besar = where(berkas, lambda x: x["ukuran"] > 1 * MB)
for x in sort_desc(besar, "ukuran"):
    print(x["nama"], round(x["ukuran"] / MB, 1), "MB")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  video.mp4 700.0 MB",
                    "  arsip.zip 50.0 MB",
                    "  foto.jpg 3.0 MB",
                    "",
                    "Daftar dict di Python mirip deretan objek di PowerShell. Fungsi",
                    "where dan sort_desc menerima daftar dan mengembalikan daftar, jadi",
                    "bisa dirangkai. Padanan PowerShell-nya untuk folder aktif:",
                    "",
                    "  Get-ChildItem -File |",
                    "      Where-Object Length -gt 1MB |",
                    "      Sort-Object Length -Descending",
                    "",
                    "Perhatikan 1MB. PowerShell paham akhiran KB, MB, GB, dan TB sebagai",
                    "kelipatan 1024, jadi 1MB sama dengan 1048576.",
                ],
            },
            {
                "heading": "Windows PowerShell 5.1 dan PowerShell 7",
                "body": [
                    "Ada dua PowerShell yang namanya mirip, dan ini sering membingungkan:",
                    "",
                    "  - Windows PowerShell 5.1, dijalankan dengan powershell.exe. Bawaan",
                    "    Windows, dibangun di atas .NET Framework lama, cuma ada di",
                    "    Windows, dan sudah nggak mendapat fitur baru.",
                    "  - PowerShell 7, dijalankan dengan pwsh. Dipasang terpisah, jalan di",
                    "    Windows, Linux, dan macOS. Versi 7.6 berjalan di atas .NET 10.",
                    "",
                    "Hampir semua skrip 5.1 jalan di pwsh, tapi ada modul lama khusus",
                    "Windows yang belum pindah. Kalau menulis skrip baru, pakai pwsh.",
                    "",
                    "Jebakan: di Linux, ls di dalam pwsh menjalankan program /usr/bin/ls",
                    "yang asli, jadi keluarannya teks biasa. Alias yang menghasilkan",
                    "objek adalah dir atau gci, yaitu singkatan dari Get-ChildItem. Di",
                    "Windows, ls justru alias untuk Get-ChildItem.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Admin TI di kantor yang memakai Windows dan Microsoft 365 biasanya",
                    "menulis PowerShell untuk pekerjaan berulang: membuat ratusan akun",
                    "pengguna dari berkas CSV, mengecek laptop mana yang belum diperbarui,",
                    "atau mengekspor daftar lisensi. Pipeline objek membuat datanya",
                    "gampang diekspor lagi ke CSV atau Excel.",
                    "",
                    "Kasus kecil: mentor PKL minta daftar lima proses yang paling banyak",
                    "memakai memori di sebuah laptop Windows, dalam satuan MB, disimpan",
                    "ke berkas CSV.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari dulu nama properti memorinya:",
                    "       Get-Process | Get-Member -Name *Memory*, WorkingSet*",
                    "  2. Urutkan menurut WorkingSet64 (byte) dan ambil lima:",
                    "       Get-Process | Sort-Object WorkingSet64 -Descending |",
                    "           Select-Object -First 5 Name, Id, WorkingSet64",
                    "  3. Ubah byte jadi MB dengan properti hitungan:",
                    "       Select-Object -First 5 Name, Id,",
                    "           @{Name='MB'; Expression={[math]::Round($_.WorkingSet64 / 1MB)}}",
                    "  4. Simpan hasilnya:",
                    "       ... | Export-Csv proses.csv -NoTypeInformation",
                    "  5. Buka proses.csv di Excel dan cek angkanya cocok dengan Task",
                    "     Manager.",
                ],
            },
        ],
    },
    {
        "title": "6. PowerShell untuk Skrip Otomasi Sehari-hari",
        "sections": [
            {
                "body": [
                    "Satu baris pipeline cukup untuk pekerjaan sekali jalan. Begitu",
                    "pekerjaannya diulang tiap hari, simpan sebagai skrip. Skrip",
                    "PowerShell adalah berkas teks berakhiran .ps1, dan isinya perintah",
                    "yang sama dengan yang kamu ketik di terminal.",
                    "",
                    "Materi ini membahas lima hal yang membuat skrip aman dijalankan",
                    "berulang kali: parameter, fungsi, penanganan error, modul, dan",
                    "execution policy.",
                ],
            },
            {
                "heading": "Skrip pertama dengan param()",
                "bahasa": "powershell",
                "code": """# bersihkan-log.ps1
param(
    [Parameter(Mandatory)]
    [string]$Folder,
    [int]$HariSimpan = 7
)

$ErrorActionPreference = 'Stop'
$batas = (Get-Date).AddDays(-$HariSimpan)

Get-ChildItem -Path $Folder -Filter *.log -File |
    Where-Object LastWriteTime -lt $batas |
    Remove-Item -WhatIf""",
            },
            {
                "body": [
                    "Blok param() di paling atas mendaftar parameter skrip. Folder wajib",
                    "diisi karena ditandai Mandatory; kalau lupa, PowerShell menanyakannya.",
                    "HariSimpan punya nilai bawaan 7. Skrip ini dijalankan seperti ini:",
                    "",
                    "  pwsh ./bersihkan-log.ps1 -Folder ./log -HariSimpan 14",
                    "",
                    "Perhatikan -WhatIf di ujung. Dengan itu Remove-Item cuma bilang apa",
                    "yang akan dihapus, misalnya:",
                    "",
                    "  What if: Performing the operation \"Remove File\" on target",
                    "  \"/home/ani/log/lama.log\".",
                    "",
                    "Jalankan dulu dengan -WhatIf, periksa daftarnya, baru hapus kata",
                    "itu. Hampir semua cmdlet yang mengubah sesuatu mendukung -WhatIf.",
                ],
            },
            {
                "heading": "Fungsi dan nilai kembalian",
                "bahasa": "powershell",
                "code": """function Get-UkuranFolder {
    param([string]$Path = ".")
    $total = (Get-ChildItem -Path $Path -Recurse -File |
              Measure-Object -Property Length -Sum).Sum
    [math]::Round($total / 1MB, 2)
}

Get-UkuranFolder -Path ./proyek""",
            },
            {
                "body": [
                    "Fungsi PowerShell nggak butuh return. Semua nilai yang nggak",
                    "ditampung variabel otomatis jadi keluaran fungsi. Di contoh tadi,",
                    "baris terakhir menghasilkan angka, jadi angka itu yang dikembalikan.",
                    "Nama fungsinya juga mengikuti pola Kata-kerja-Benda: kata kerjanya",
                    "dari daftar resmi (Get), bendanya bebas.",
                    "",
                    "Jebakan: karena semua nilai yang lepas ikut dikembalikan, fungsi",
                    "berikut nggak mengembalikan 5:",
                    "",
                    "  function Tambah { param($a, $b) \"menghitung...\"; $a + $b }",
                    "  $h = Tambah 2 3",
                    "",
                    "Isi $h adalah array berisi \"menghitung...\" dan 5. Untuk pesan ke",
                    "layar, pakai Write-Host atau Write-Verbose, yang nggak masuk ke",
                    "pipeline.",
                ],
            },
            {
                "heading": "Error: try, catch, dan -ErrorAction",
                "bahasa": "powershell",
                "code": """try {
    Get-Item ./tidak-ada.txt -ErrorAction Stop
    Write-Output "ketemu"
}
catch {
    Write-Warning "Gagal: $($_.Exception.Message)"
}
finally {
    Write-Output "selesai memeriksa"
}""",
            },
            {
                "body": [
                    "PowerShell punya dua jenis error. Error yang menghentikan",
                    "(terminating) bisa ditangkap catch. Error biasa (non-terminating)",
                    "cuma dicetak merah, lalu skrip jalan terus ke baris berikutnya.",
                    "Get-Item untuk berkas yang nggak ada termasuk jenis kedua.",
                    "",
                    "Akibatnya, tanpa -ErrorAction Stop, blok catch di atas nggak pernah",
                    "jalan dan \"ketemu\" tetap tercetak. Dengan -ErrorAction Stop,",
                    "errornya dinaikkan jadi terminating, dan yang tercetak adalah",
                    "peringatan Gagal lalu selesai memeriksa. Di dalam catch, $_ berisi",
                    "error yang sedang ditangani.",
                    "",
                    "Supaya nggak perlu menulis -ErrorAction di tiap baris, banyak skrip",
                    "memasang $ErrorActionPreference = 'Stop' di bagian atas, seperti",
                    "skrip bersihkan-log tadi.",
                ],
            },
            {
                "heading": "Modul dan PowerShell Gallery",
                "bahasa": "terminal",
                "code": """pwsh
Find-Module -Name Pester
Install-Module -Name Pester -Scope CurrentUser
Import-Module Pester
Get-Command -Module Pester | Select-Object -First 5""",
            },
            {
                "body": [
                    "Modul adalah paket berisi cmdlet tambahan. Tempat berbagi modul",
                    "resminya PowerShell Gallery (powershellgallery.com), mirip PyPI untuk",
                    "Python. Install-Module mengunduh dari sana; -Scope CurrentUser",
                    "memasang di folder pribadimu, jadi nggak butuh hak admin.",
                    "",
                    "PowerShell 7.4 ke atas juga membawa modul PSResourceGet dengan",
                    "perintah Install-PSResource, pengganti PowerShellGet yang lebih",
                    "baru. Dua-duanya mengambil dari Gallery yang sama.",
                    "",
                    "Pester adalah alat tes untuk PowerShell. Dengan Pester kamu menulis",
                    "blok Describe dan It, lalu menjalankan Invoke-Pester untuk mengecek",
                    "fungsi-fungsimu, mirip pytest di Python.",
                ],
            },
            {
                "heading": "Execution policy",
                "bahasa": "terminal",
                "code": """Get-ExecutionPolicy
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Unblock-File ./skrip-dari-internet.ps1""",
            },
            {
                "body": [
                    "Di Windows, skrip .ps1 pertamamu kemungkinan besar ditolak dengan",
                    "pesan running scripts is disabled on this system. Itu execution",
                    "policy: aturan Windows soal skrip mana yang boleh dijalankan. Bawaan",
                    "di Windows untuk laptop dan PC adalah Restricted, artinya skrip sama",
                    "sekali nggak boleh jalan. Di Windows Server bawaannya RemoteSigned.",
                    "",
                    "Pilihan yang umum dipakai adalah RemoteSigned untuk pengguna saat ini.",
                    "Skrip buatanmu sendiri boleh jalan, sedangkan skrip yang diunduh dari",
                    "internet harus ditandatangani atau dibuka blokirnya dengan",
                    "Unblock-File setelah kamu membacanya.",
                    "",
                    "Ingat: execution policy bukan pagar keamanan. Ia cuma mencegah skrip",
                    "terjalankan tanpa sengaja. Di Linux dan macOS, policy-nya selalu",
                    "Unrestricted dan nggak bisa diubah.",
                ],
            },
            {
                "heading": "Memasang pwsh di Fedora",
                "bahasa": "terminal",
                "code": """sudo dnf install https://github.com/PowerShell/PowerShell/releases/download/v7.6.7/powershell-7.6.7-1.rh.x86_64.rpm
pwsh --version
pwsh ./bersihkan-log.ps1 -Folder ./log""",
            },
            {
                "body": [
                    "PowerShell nggak ada di repositori Fedora. Microsoft menyediakan",
                    "berkas rpm di halaman rilis GitHub-nya, dan dnf bisa memasangnya",
                    "langsung dari URL. Ganti nomor versinya dengan rilis terbaru waktu",
                    "kamu membaca ini. Cara lain kalau dotnet sudah terpasang:",
                    "dotnet tool install --global PowerShell.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Server Windows yang menjalankan aplikasi web sering kehabisan ruang",
                    "disk karena berkas log menumpuk. Solusi yang biasa dipakai admin",
                    "adalah skrip PowerShell kecil yang dijadwalkan lewat Task Scheduler",
                    "setiap malam. Di Linux, skrip yang sama bisa dijadwalkan dengan cron",
                    "atau timer systemd, asal pwsh terpasang.",
                    "",
                    "Kasus kecil: folder C:\\Aplikasi\\log berisi ribuan berkas .log, dan",
                    "kamu diminta menghapus yang lebih tua dari 30 hari setiap malam",
                    "tanpa risiko salah hapus.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pakai skrip bersihkan-log.ps1 dari materi ini, lengkap dengan",
                    "     -WhatIf.",
                    "  2. Jalankan manual sekali dan periksa daftar yang akan dihapus:",
                    "       pwsh .\\bersihkan-log.ps1 -Folder C:\\Aplikasi\\log -HariSimpan 30",
                    "  3. Kalau daftarnya benar, ganti -WhatIf dengan -Verbose supaya",
                    "     tiap penghapusan tercatat.",
                    "  4. Arahkan catatannya ke berkas dengan Start-Transcript di awal",
                    "     skrip dan Stop-Transcript di akhir.",
                    "  5. Daftarkan di Task Scheduler untuk jalan setiap hari pukul 01.00,",
                    "     dengan perintah pwsh dan argumen jalur skripnya.",
                ],
            },
        ],
    },
    {
        "title": "7. Perl: Regex dan Olah Teks",
        "sections": [
            {
                "body": [
                    "Perl dibuat Larry Wall tahun 1987 untuk mengolah teks dan laporan.",
                    "Di tahun 1990-an ia jadi bahasa favorit admin sistem dan pembuat",
                    "situs web, sampai dijuluki lakban internet: dipakai menyambung apa",
                    "saja dengan apa saja.",
                    "",
                    "Sekarang Perl sudah lewat masa jayanya, tapi masih banyak ditemui.",
                    "Skrip cron di server lama, alat bawaan Linux seperti autotools, dan",
                    "perintah git send-email ditulis dengan Perl. Di Survei Stack Overflow",
                    "2026 pemakainya 3,8%. Rilis tahunannya tetap jalan: versi stabil",
                    "terbaru saat materi ini ditulis (Oktober 2026) adalah 5.44.0, rilis",
                    "Juli 2026. Fedora 44 membawa seri 5.42, dan biasanya sudah terpasang",
                    "karena banyak alat sistem memerlukannya. Cek dengan perl -v.",
                ],
            },
            {
                "heading": "Halo Dunia dan use strict",
                "bahasa": "perl",
                "code": "use strict;\nuse warnings;\n\nprint \"Halo, Dunia!\\n\";",
            },
            {
                "body": [
                    "Simpan sebagai halo.pl dan jalankan dengan perl halo.pl. Dua baris",
                    "use di atas wajib kamu biasakan. use strict menolak variabel yang",
                    "belum dideklarasikan dengan my, dan use warnings memperingatkan hal",
                    "mencurigakan seperti memakai nilai yang belum diisi. Tanpa keduanya,",
                    "salah ketik nama variabel diam saja: Perl membuat variabel baru yang",
                    "kosong.",
                ],
            },
            {
                "heading": "Sigil: $, @, dan %",
                "bahasa": "perl",
                "code": "use strict;\nuse warnings;\n\nmy $nama  = \"Ani\";                    # skalar: satu nilai\nmy @nilai = (70, 85, 90);              # array: daftar\nmy %umur  = (ani => 17, budi => 18);   # hash: kunci dan nilai\n\nprint \"$nama\\n\";\nprint \"$nilai[0]\\n\";      # satu elemen array memakai $\nprint \"$umur{budi}\\n\";    # satu nilai hash juga memakai $\nprint scalar(@nilai), \"\\n\";",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Ani",
                    "  70",
                    "  18",
                    "  3",
                    "",
                    "Ciri Perl yang paling kelihatan adalah sigil, tanda di depan nama",
                    "variabel. $ untuk skalar (satu angka atau teks), @ untuk array, dan %",
                    "untuk hash, padanan dict di Python.",
                    "",
                    "Yang bikin pemula bingung: sigil menunjukkan apa yang kamu ambil,",
                    "bukan jenis variabelnya. Satu elemen array itu satu nilai, jadi",
                    "ditulis $nilai[0], bukan @nilai[0]. Sama untuk hash: $umur{budi}.",
                ],
            },
            {
                "heading": "Konteks skalar dan konteks list",
                "bahasa": "perl",
                "code": "use strict;\nuse warnings;\n\nmy @nilai = (70, 85, 90);\nmy $banyak = @nilai;      # konteks skalar: jumlah elemen\nmy ($pertama) = @nilai;   # konteks list: elemen pertama\nprint \"$banyak $pertama\\n\";",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  3 70",
                    "",
                    "Ekspresi yang sama bisa menghasilkan nilai berbeda tergantung",
                    "tempatnya. Kalau hasilnya ditampung satu skalar, Perl memakai konteks",
                    "skalar, dan array di konteks skalar berarti jumlah elemennya. Kalau",
                    "ditampung daftar dalam kurung, konteksnya list, dan elemen pertama",
                    "masuk ke $pertama.",
                    "",
                    "Fungsi bawaan juga ikut aturan ini. localtime, misalnya, mengembalikan",
                    "teks tanggal lengkap di konteks skalar dan sembilan angka terpisah di",
                    "konteks list. Ini sumber banyak kebingungan saat membaca kode orang.",
                ],
            },
            {
                "heading": "Regex bawaan: m// dan s///",
                "bahasa": "perl",
                "code": "use strict;\nuse warnings;\n\nmy @log = (\n    \"2026-10-01 12:00:01 ERROR [10.0.0.5] disk penuh\",\n    \"2026-10-01 12:00:07 INFO [10.0.0.9] login berhasil\",\n    \"2026-10-01 12:01:12 ERROR [10.0.0.5] disk penuh\",\n);\n\nmy %hitung;\nfor my $baris (@log) {\n    if ($baris =~ m/ (ERROR|WARN|INFO) \\[([\\d.]+)\\]/) {\n        $hitung{\"$1 $2\"}++;\n    }\n}\nfor my $kunci (sort keys %hitung) {\n    print \"$kunci: $hitung{$kunci}\\n\";\n}\n\n(my $samar = $log[0]) =~ s/\\d+\\.\\d+\\.\\d+\\.\\d+/x.x.x.x/;\nprint \"$samar\\n\";",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ERROR 10.0.0.5: 2",
                    "  INFO 10.0.0.9: 1",
                    "  2026-10-01 12:00:01 ERROR [x.x.x.x] disk penuh",
                    "",
                    "Regex adalah bagian dari sintaks Perl, bukan pustaka tambahan.",
                    "Operator =~ mencocokkan teks dengan pola. m/.../ mencari, dan bagian",
                    "dalam kurung yang cocok otomatis masuk ke $1, $2, dan seterusnya.",
                    "s/pola/ganti/ mengganti teks yang cocok. Baris terakhir menyalin",
                    "$log[0] ke $samar dulu, lalu menyamarkan alamat IP di salinan itu.",
                    "",
                    "Gaya regex Perl ini menular ke banyak bahasa. Pustaka re di Python, regex",
                    "JavaScript, dan PCRE yang dipakai PHP semuanya meniru sintaksnya.",
                ],
            },
            {
                "heading": "One-liner di terminal",
                "bahasa": "terminal",
                "code": "perl -ne 'print if /ERROR/' app.log\nperl -ne '$n{$1}++ if / (ERROR|WARN|INFO) /; END { print \"$_ $n{$_}\\n\" for sort keys %n }' app.log\nperl -pi.bak -e 's/localhost/127.0.0.1/g' konfigurasi.ini",
            },
            {
                "body": [
                    "Perl paling sering dipakai lewat one-liner, satu baris perintah",
                    "langsung di terminal:",
                    "  - -e berarti kodenya ditulis di argumen, bukan di berkas.",
                    "  - -n membungkus kode dengan loop yang membaca baris demi baris; baris",
                    "    yang sedang dibaca ada di variabel $_.",
                    "  - -p sama dengan -n, ditambah mencetak $_ di akhir tiap putaran.",
                    "  - -i.bak menyunting berkas di tempat dan menyimpan salinan aslinya",
                    "    dengan akhiran .bak.",
                    "",
                    "Baris kedua menghitung jumlah tiap level log. Blok END dijalankan",
                    "sekali, setelah semua baris dibaca. Kamu bisa membandingkannya",
                    "dengan awk di kurikulum Bash; idenya mirip, dan memang Perl lahir",
                    "sebagian untuk menggantikan sed dan awk.",
                ],
            },
            {
                "heading": "Perbandingan teks: eq, bukan ==",
                "body": [
                    "Jebakan: Perl memakai operator berbeda untuk angka dan teks. == dan",
                    "< untuk angka, eq dan lt untuk teks. Kalau kamu menulis",
                    "",
                    "  if (\"abc\" == \"abd\") { print \"sama\\n\" }",
                    "",
                    "Perl mengubah kedua teks jadi angka. Teks yang nggak diawali angka",
                    "jadi 0, jadi 0 == 0 bernilai benar dan tercetak sama. Dengan use",
                    "warnings, Perl setidaknya memberi peringatan Argument \"abc\" isn't",
                    "numeric. Ini juga contoh nyata bahasa bertipe lemah.",
                ],
            },
            {
                "heading": "Membaca log yang sama dengan Python",
                "code": "import re\n\nlog = [\n    \"2026-10-01 12:00:01 ERROR [10.0.0.5] disk penuh\",\n    \"2026-10-01 12:00:07 INFO [10.0.0.9] login berhasil\",\n]\nfor baris in log:\n    m = re.search(r\" (ERROR|WARN|INFO) \\[([\\d.]+)\\]\", baris)\n    if m:\n        print(m.group(1), m.group(2))",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  ERROR 10.0.0.5",
                    "  INFO 10.0.0.9",
                    "",
                    "Polanya persis sama dengan versi Perl. Bedanya cuma cara memanggil:",
                    "Python memakai fungsi re.search dan objek hasil m.group(1), sedangkan",
                    "Perl memakai operator =~ dan variabel $1.",
                ],
            },
            {
                "heading": "CPAN dan kapan memilih Perl",
                "body": [
                    "Pustaka Perl dikumpulkan di CPAN (cpan.org) sejak 1995. Pemasang yang",
                    "nyaman dipakai adalah cpanm. Modul yang sering ditemui antara lain",
                    "DBI untuk database, Mojolicious dan Dancer2 untuk web, dan Moose",
                    "untuk OOP yang lebih rapi.",
                    "",
                    "Soal masa depannya: rencana Perl 7 yang diumumkan tahun 2020 sudah",
                    "dibatalkan, jadi Perl tetap di seri 5. Raku, yang dulu bernama Perl",
                    "6, adalah bahasa terpisah dan kode Perl 5 nggak jalan di sana.",
                    "",
                    "Saran praktisnya: pelajari Perl cukup untuk membaca dan memperbaiki",
                    "skrip yang sudah ada. Untuk skrip baru yang akan dirawat tim, Python",
                    "biasanya lebih mudah dibaca orang lain.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak server lama masih menjalankan skrip Perl dari cron untuk",
                    "merangkum log, mengirim laporan email, atau memindahkan berkas.",
                    "Panel hosting cPanel dan pelacak bug Bugzilla juga ditulis dengan",
                    "Perl. Saat PKL di bagian infrastruktur, kemungkinan besar kamu",
                    "bertemu salah satunya.",
                    "",
                    "Kasus kecil: alamat server database pindah dari db-lama.kantor.id ke",
                    "db-baru.kantor.id, dan nama lamanya tertulis di 40 berkas .conf.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari dulu berkas mana yang memuat nama lama:",
                    "       grep -l 'db-lama.kantor.id' *.conf",
                    "  2. Ganti di semua berkas sekaligus, sambil menyimpan cadangan:",
                    "       perl -pi.bak -e 's/db-lama\\.kantor\\.id/db-baru.kantor.id/g' *.conf",
                    "  3. Titik di pola ditulis \\. karena titik polos di regex berarti",
                    "     huruf apa saja.",
                    "  4. Bandingkan satu berkas dengan cadangannya:",
                    "       diff aplikasi.conf.bak aplikasi.conf",
                    "  5. Kalau semuanya benar, hapus berkas .bak.",
                ],
            },
        ],
    },
    {
        "title": "8. Peta Bahasa Skrip: Awk, Tcl, Raku, Batch, VBScript",
        "sections": [
            {
                "body": [
                    "Selain Bash, PowerShell, dan Perl, ada lima bahasa skrip lain yang",
                    "mungkin kamu temukan di komputer orang. Dua masih sehat, satu punya",
                    "komunitas kecil, dan dua sebaiknya nggak dipakai untuk skrip baru.",
                    "Materi ini cukup supaya kamu mengenalinya dan tahu harus bersikap",
                    "bagaimana.",
                ],
            },
            {
                "heading": "Awk",
                "bahasa": "awk",
                "code": "# jumlahkan kolom ke-3 untuk baris berstatus lunas\n$2 == \"lunas\" { total += $3; n++ }\nEND { printf \"%d transaksi, total %d\\n\", n, total }",
            },
            {
                "body": [
                    "Awk mengolah teks berkolom baris demi baris. Programnya berupa",
                    "pasangan pola dan aksi: kalau baris cocok dengan pola, aksinya",
                    "dijalankan. $1, $2, $3 adalah kolom, $0 baris utuh, dan blok END",
                    "jalan sekali di akhir. Untuk masukan",
                    "",
                    "  T01 lunas 50000",
                    "  T02 batal 20000",
                    "  T03 lunas 75000",
                    "",
                    "program di atas mencetak 2 transaksi, total 125000.",
                    "",
                    "Awk sudah dibahas di kurikulum Bash (materi grep, sed, dan awk) dan",
                    "kurikulum Fedora (sed & awk), jadi di sini cukup diingatkan. GNU awk",
                    "(gawk) terpasang bawaan di Fedora; versi terbarunya 5.4.1 (Juli",
                    "2026). Statusnya matang dan masih dipakai setiap hari di terminal.",
                ],
            },
            {
                "heading": "Tcl",
                "bahasa": "tcl",
                "code": "set nama \"Ani\"\nset nilai {70 85 90}\nset total 0\nforeach n $nilai {\n    set total [expr {$total + $n}]\n}\nputs \"$nama: total $total, rata-rata [expr {$total / [llength $nilai]}]\"",
            },
            {
                "body": [
                    "Tcl (dibaca tikel) adalah bahasa di mana setiap baris adalah perintah",
                    "dan semua nilai adalah teks. Ada tiga aturan yang harus dipahami",
                    "dulu:",
                    "  - $nama diganti isi variabelnya.",
                    "  - [perintah] dijalankan, lalu diganti hasilnya.",
                    "  - {...} dibiarkan apa adanya, tanpa penggantian apa pun.",
                    "",
                    "Program di atas mencetak Ani: total 245, rata-rata 81. Hasil bagi",
                    "245 / 3 jadi 81 karena dua bilangan bulat dibagi secara bulat.",
                    "",
                    "Tcl hidup di tempat yang mungkin nggak kamu sangka. Alat desain chip",
                    "seperti Vivado memakainya sebagai bahasa skrip, rangkaian tes SQLite",
                    "ditulis dengan Tcl, dan pasangannya Tk dipakai membuat GUI ringan.",
                    "Versi terbarunya 9.1.0 (September 2026); Fedora 44 membawa 9.0. Tcl 9",
                    "punya beberapa perubahan yang nggak cocok dengan 8.6, jadi cek versi",
                    "skrip lama sebelum menjalankannya.",
                    "",
                    "Expect, alat berbasis Tcl, mengotomasi program yang menunggu ketikan",
                    "pengguna:",
                    "",
                    "  spawn ./pasang.sh",
                    "  expect \"Lanjutkan? (y/n)\"",
                    "  send \"y\\r\"",
                    "  expect eof",
                ],
            },
            {
                "heading": "Raku",
                "bahasa": "raku",
                "code": "say 'Halo, Dunia!';\n\nmy @nilai = 70, 85, 90;\nsay @nilai.sum / @nilai.elems;   # 81.666667\n\ngrammar Tanggal {\n    token TOP   { <tahun> '-' <bulan> '-' <hari> }\n    token tahun { \\d ** 4 }\n    token bulan { \\d ** 2 }\n    token hari  { \\d ** 2 }\n}\nsay ~Tanggal.parse('2026-10-19')<bulan>;   # 10",
            },
            {
                "body": [
                    "Raku dulu bernama Perl 6, lalu diganti nama tahun 2019 karena isinya",
                    "dirancang ulang total. Kode Perl 5 nggak jalan di Raku. Ciri paling",
                    "menarik Raku adalah grammar bawaan: kamu bisa menulis aturan",
                    "pengurai teks seperti di contoh, lalu mengambil bagiannya dengan",
                    "nama.",
                    "",
                    "Implementasinya bernama Rakudo dan rilis tiap bulan; versi terbaru",
                    "saat materi ini ditulis 2026.09. Komunitasnya kecil dan Raku nggak",
                    "tercantum di Survei Stack Overflow 2026. Bagus untuk belajar parsing,",
                    "jarang diminta di lowongan.",
                ],
            },
            {
                "heading": "Batch (cmd.exe)",
                "bahasa": "batch",
                "code": """@echo off
setlocal enabledelayedexpansion
set total=0
for %%n in (70 85 90) do (
    set /a total=!total!+%%n
)
echo Total: %total%""",
            },
            {
                "body": [
                    "Batch adalah bahasa skrip Command Prompt Windows, warisan MS-DOS.",
                    "Berkasnya berakhiran .bat atau .cmd. Skrip di atas mencetak",
                    "Total: 245.",
                    "",
                    "Jebakan utamanya ada di variabel. %total% diganti nilainya sekali,",
                    "waktu seluruh blok dalam kurung dibaca, bukan tiap putaran. Jadi di",
                    "dalam loop, %total% selalu 0. Supaya nilainya dibaca ulang tiap",
                    "putaran, nyalakan delayed expansion lalu tulis !total!. Variabel loop",
                    "juga ditulis %%n di dalam berkas, tapi %n kalau diketik langsung di",
                    "prompt.",
                    "",
                    "Batch nggak punya nomor versi dan nggak dikembangkan lagi. Microsoft",
                    "menyarankan PowerShell untuk skrip baru. Batch nggak bisa dijalankan",
                    "di Fedora; Wine menyediakan cmd tiruan, tapi perilakunya nggak sama",
                    "persis.",
                ],
            },
            {
                "heading": "VBScript",
                "bahasa": "basic",
                "code": """' halo.vbs, jalankan dengan: cscript halo.vbs
Dim nilai, n, total
nilai = Array(70, 85, 90)
total = 0
For Each n In nilai
    total = total + n
Next
WScript.Echo "Total: " & total""",
            },
            {
                "body": [
                    "VBScript adalah turunan Visual Basic untuk skrip Windows dan halaman",
                    "ASP klasik. Skripnya dijalankan Windows Script Host lewat cscript",
                    "atau wscript. Banyak kantor masih punya skrip logon .vbs yang",
                    "memetakan drive jaringan setiap kali karyawan masuk.",
                    "",
                    "Statusnya usang. Microsoft menyatakannya deprecated pada Mei 2024. Di",
                    "Windows 11 24H2 ia jadi fitur opsional yang masih menyala, sekitar",
                    "2027 akan dimatikan secara bawaan, lalu dihapus. Kalau kamu menemukan",
                    "skrip .vbs, rencanakan pindah ke PowerShell. Untuk Visual Basic",
                    "modern, lihat kurikulum VB.NET di aplikasi ini.",
                ],
            },
            {
                "heading": "Memilih untuk skrip baru",
                "body": [
                    "Ringkasnya, untuk skrip baru:",
                    "  - Olah kolom teks satu baris di terminal: awk.",
                    "  - Otomasi Windows atau Microsoft 365: PowerShell.",
                    "  - Skrip yang lebih panjang dari satu layar: Python.",
                    "  - Skrip di dalam alat desain chip yang memang memakai Tcl: Tcl.",
                    "",
                    "Batch dan VBScript cukup dibaca, lalu dipindahkan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kantor yang sudah lama memakai Windows sering punya skrip logon",
                    "warisan berbahasa VBScript atau Batch yang dipasang lewat Group",
                    "Policy. Tugas memindahkannya ke PowerShell sering diberikan ke staf",
                    "TI junior, termasuk anak PKL.",
                    "",
                    "Kasus kecil: skrip logon.vbs memetakan folder bersama",
                    "\\\\server\\data ke drive S: dengan baris",
                    "  CreateObject(\"WScript.Network\").MapNetworkDrive \"S:\", \"\\\\server\\data\"",
                    "dan kamu diminta membuat penggantinya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca skrip lamanya sampai habis dan catat semua yang dilakukan,",
                    "     termasuk baris yang kelihatannya sepele.",
                    "  2. Tulis padanannya di PowerShell:",
                    "       New-PSDrive -Name S -PSProvider FileSystem `",
                    "           -Root \\\\server\\data -Persist",
                    "  3. Uji di satu laptop dengan akun biasa, bukan akun admin.",
                    "  4. Cek drive S: muncul di File Explorer dan bisa dibuka.",
                    "  5. Ganti skrip di Group Policy, lalu simpan logon.vbs lama di",
                    "     arsip sampai semua laptop terbukti memakai skrip baru.",
                ],
            },
        ],
    },
    {
        "title": "9. Lua: Table, Fungsi, dan Indeks dari Satu",
        "sections": [
            {
                "body": [
                    "Lua (bahasa Portugis untuk bulan) dibuat tahun 1993 di sebuah",
                    "universitas di Rio de Janeiro, Brasil. Ia sengaja dibuat kecil:",
                    "interpreternya cuma beberapa ratus kilobyte dan gampang ditanam di",
                    "dalam program lain. Program besar itu memakai Lua sebagai bahasa",
                    "skrip, jadi penggunanya bisa menambah fitur tanpa mengompilasi ulang",
                    "programnya.",
                    "",
                    "Karena itu Lua muncul di banyak tempat: addon World of Warcraft,",
                    "engine game Love2D dan Defold, berkas konfigurasi Neovim, skrip di",
                    "Redis, OpenResty di atas nginx, dan plugin Adobe Lightroom. Di Survei",
                    "Stack Overflow 2026 pemakainya 9,4%, terbanyak kedua di antara bahasa",
                    "yang dibahas kurikulum ini.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "5.5.1, rilis Agustus 2026, berlisensi MIT. Fedora 44 masih membawa",
                    "5.4.8. Semua contoh di materi ini jalan di kedua versi.",
                ],
            },
            {
                "heading": "Halo Dunia",
                "bahasa": "lua",
                "code": "print(\"Halo, Dunia!\")",
            },
            {
                "heading": "Memasang dan menjalankan",
                "bahasa": "terminal",
                "code": """sudo dnf install lua
lua -v
lua halo.lua
lua""",
            },
            {
                "body": [
                    "Perintah lua tanpa nama berkas membuka REPL, tempat kamu bisa",
                    "mengetik kode baris per baris dan langsung melihat hasilnya. Keluar",
                    "dengan Ctrl+D.",
                ],
            },
            {
                "heading": "Table: daftar dan kamus sekaligus",
                "bahasa": "lua",
                "code": """local nilai = {70, 80, 90}
print(nilai[1])      --> 70
print(#nilai)        --> 3

local siswa = {nama = "Ani", umur = 17}
print(siswa.nama)    --> Ani
print(siswa["umur"]) --> 17
siswa.kelas = "XI"   -- menambah kunci baru
print(siswa.kelas)   --> XI""",
            },
            {
                "body": [
                    "Lua cuma punya satu struktur data: table. Table yang sama bisa",
                    "dipakai sebagai daftar (seperti list Python) atau sebagai kamus",
                    "(seperti dict), bahkan dua-duanya sekaligus. Kelas, modul, dan",
                    "objek di Lua juga dibangun dari table.",
                    "",
                    "Tanda # memberi panjang bagian daftar sebuah table. Komentar di Lua",
                    "diawali --, dan banyak programmer Lua menulis --> untuk menunjukkan",
                    "hasil sebuah baris, seperti di contoh.",
                ],
            },
            {
                "heading": "Indeks mulai dari 1, dan nil",
                "bahasa": "lua",
                "code": """local t = {10, 20, 30}
print(t[0])       --> nil
print(t[1])       --> 10
t[#t + 1] = 40    -- menambah di ujung
print(#t)         --> 4
print(10 ~= 20)   --> true""",
            },
            {
                "body": [
                    "Indeks daftar di Lua mulai dari 1, bukan 0. t[0] nggak error, tapi",
                    "mengembalikan nil, nilai Lua untuk \"nggak ada\". Ini jebakan pertama",
                    "buat orang yang datang dari Python atau JavaScript: kode tetap jalan,",
                    "cuma hasilnya kosong.",
                    "",
                    "Menambah elemen di ujung ditulis t[#t + 1] = nilai, atau",
                    "table.insert(t, nilai). Operator tidak sama dengan ditulis ~=.",
                    "",
                    "Jebakan: mengisi elemen dengan nil sama dengan menghapusnya. Kalau",
                    "daftar punya lubang di tengah, misalnya {10, nil, 30}, hasil #t",
                    "nggak bisa diandalkan. Jangan menyimpan nil di tengah daftar.",
                ],
            },
            {
                "heading": "local dan global",
                "bahasa": "lua",
                "code": """local function hitung()
  hasil = 42          -- tanpa local: jadi variabel global
  local rahasia = 7   -- cuma hidup di dalam fungsi
end

hitung()
print(hasil)    --> 42
print(rahasia)  --> nil""",
            },
            {
                "body": [
                    "Di Lua, variabel yang nggak ditandai local otomatis global, bisa",
                    "dibaca dan ditimpa dari mana saja. Salah ketik nama variabel nggak",
                    "bikin error; Lua cuma membuat atau membaca variabel global baru yang",
                    "isinya nil. Biasakan menulis local di setiap variabel dan fungsi.",
                    "",
                    "Lua 5.5 menambah deklarasi global. Begitu sebuah blok memuat",
                    "deklarasi seperti global skor, nama yang nggak dideklarasikan di blok",
                    "itu langsung ditolak saat kompilasi. Ini membantu menangkap salah",
                    "ketik tadi, tapi baru tersedia di Lua 5.5.",
                ],
            },
            {
                "heading": "Loop: ipairs, pairs, dan for angka",
                "bahasa": "lua",
                "code": """local buah = {"apel", "jeruk", "mangga"}
for i, b in ipairs(buah) do
  print(i .. ". " .. b)
end

local stok = {apel = 5, jeruk = 0}
for nama, jumlah in pairs(stok) do
  print(nama, jumlah)   -- urutannya nggak dijamin
end

for i = 10, 1, -3 do
  io.write(i, " ")      --> 10 7 4 1
end
print()""",
            },
            {
                "body": [
                    "ipairs berjalan di bagian daftar, dari indeks 1 berurutan. pairs",
                    "berjalan di semua kunci, tapi urutannya bebas, mirip dict di Python",
                    "versi lama. Kalau urutan penting, kumpulkan kuncinya ke daftar lalu",
                    "urutkan dengan table.sort.",
                    "",
                    "for i = awal, akhir, langkah adalah loop angka. Batas akhirnya ikut",
                    "dihitung, beda dengan range di Python. Teks disambung dengan dua",
                    "titik: \"1. \" .. \"apel\" menghasilkan \"1. apel\".",
                ],
            },
            {
                "heading": "Fungsi adalah nilai",
                "bahasa": "lua",
                "code": """local function terapkan(daftar, f)
  local hasil = {}
  for i, v in ipairs(daftar) do
    hasil[i] = f(v)
  end
  return hasil
end

local kuadrat = terapkan({1, 2, 3}, function(x) return x * x end)
print(table.concat(kuadrat, ", "))   --> 1, 4, 9

local function bagi(a, b)
  return a // b, a % b
end
local hasil, sisa = bagi(17, 5)
print(hasil, sisa)                  --> 3   2""",
            },
            {
                "body": [
                    "Fungsi di Lua bisa disimpan di variabel, dioper ke fungsi lain, dan",
                    "dikembalikan, sama seperti di Python. Istilahnya fungsi kelas satu.",
                    "Fungsi juga boleh mengembalikan beberapa nilai sekaligus, seperti",
                    "bagi di atas. // adalah pembagian bulat, tersedia sejak Lua 5.3.",
                    "",
                    "Ringkasan padanan dengan Python:",
                ],
            },
            {
                "heading": "Python dan Lua berdampingan",
                "bahasa": "teks",
                "code": """Python                 Lua
None                   nil
x != y                 x ~= y
"a" + "b"              "a" .. "b"
len(t)                 #t
t[0] (pertama)         t[1] (pertama)
elif                   elseif
# komentar             -- komentar
def f(x): ...          local function f(x) ... end
for i in range(1, 4)   for i = 1, 3 do ... end""",
            },
            {
                "heading": "LuaRocks",
                "bahasa": "terminal",
                "code": """sudo dnf install luarocks
luarocks install --local luasocket
luarocks list""",
            },
            {
                "body": [
                    "Pustaka Lua dibagikan sebagai rock lewat LuaRocks, pengelola paket",
                    "Lua. Pilihan --local memasang di folder pribadimu, jadi nggak perlu",
                    "sudo. Tapi di banyak tempat kerja kamu jarang memasang rock: program",
                    "yang menanam Lua (Neovim, Redis, engine game) sudah menyediakan",
                    "fungsi-fungsinya sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Neovim, editor teks yang banyak dipakai programmer, membaca",
                    "konfigurasinya dari berkas init.lua. Plugin Neovim juga kebanyakan",
                    "ditulis dengan Lua. Jadi bagi banyak programmer, Lua pertama yang",
                    "mereka tulis adalah konfigurasi editornya sendiri.",
                    "",
                    "Kasus kecil: kamu ingin Neovim menampilkan nomor baris, memakai",
                    "empat spasi untuk satu tab, dan menyimpan berkas dengan Ctrl+S.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat berkas ~/.config/nvim/init.lua.",
                    "  2. Pilihan editor diatur lewat table vim.opt:",
                    "       vim.opt.number = true",
                    "       vim.opt.tabstop = 4",
                    "       vim.opt.shiftwidth = 4",
                    "       vim.opt.expandtab = true",
                    "  3. Pintasan papan ketik dibuat dengan vim.keymap.set:",
                    "       vim.keymap.set(\"n\", \"<C-s>\", \":w<CR>\")",
                    "  4. Simpan, tutup, lalu buka Neovim lagi. Nomor baris harus muncul.",
                    "  5. Kalau ada error, Neovim menampilkan nomor baris di init.lua yang",
                    "     salah. Periksa tanda kutip dan tanda = di baris itu.",
                ],
            },
        ],
    },
    {
        "title": "10. Lua Lanjut: Metatable, Closure, dan Coroutine",
        "sections": [
            {
                "body": [
                    "Lua sengaja nggak punya kelas, pewarisan, atau operator yang bisa",
                    "dibebani ulang. Gantinya, ia memberi satu mekanisme umum bernama",
                    "metatable. Dari mekanisme kecil itu, programmer Lua membangun OOP,",
                    "operator untuk tipe buatan sendiri, dan nilai bawaan. Materi ini",
                    "membahas metatable, closure, dan coroutine, tiga hal yang membuat",
                    "Lua cocok ditanam di program lain.",
                ],
            },
            {
                "heading": "Metatable dan __add",
                "bahasa": "lua",
                "code": """local Vektor = {}
Vektor.__index = Vektor

function Vektor.baru(x, y)
  return setmetatable({x = x, y = y}, Vektor)
end

Vektor.__add = function(a, b)
  return Vektor.baru(a.x + b.x, a.y + b.y)
end

Vektor.__tostring = function(v)
  return "(" .. v.x .. ", " .. v.y .. ")"
end

function Vektor:panjang2()
  return self.x * self.x + self.y * self.y
end

local a = Vektor.baru(1, 2)
local b = Vektor.baru(3, 4)
print(tostring(a + b))   --> (4, 6)
print(b:panjang2())      --> 25""",
            },
            {
                "body": [
                    "Metatable adalah table kedua yang ditempelkan ke sebuah table dengan",
                    "setmetatable. Isinya kunci khusus berawalan dua garis bawah, disebut",
                    "metamethod. Waktu Lua bertemu a + b dan a adalah table, ia mencari",
                    "__add di metatable a, lalu memanggilnya. __tostring dipakai tostring",
                    "dan print. Masih ada __eq, __lt, __len, __call, dan lainnya.",
                    "",
                    "Tanda titik dua di function Vektor:panjang2() adalah singkatan. Ia",
                    "menambah parameter tersembunyi bernama self. b:panjang2() sama dengan",
                    "Vektor.panjang2(b).",
                ],
            },
            {
                "heading": "__index dan OOP gaya prototipe",
                "bahasa": "lua",
                "code": """local Hewan = {suara = "...", kaki = 4}
Hewan.__index = Hewan

function Hewan:bersuara()
  return self.nama .. " bilang " .. self.suara
end

local Kucing = setmetatable({suara = "meong"}, Hewan)
Kucing.__index = Kucing

function Kucing.baru(nama)
  return setmetatable({nama = nama}, Kucing)
end

local k = Kucing.baru("Oyen")
print(k:bersuara())   --> Oyen bilang meong
print(k.kaki)         --> 4
print(k.sayap)        --> nil""",
            },
            {
                "body": [
                    "__index menjawab pertanyaan \"kalau kuncinya nggak ada di sini, cari",
                    "ke mana?\". Waktu kamu menulis k:bersuara(), Lua mencari bersuara di",
                    "table k dan nggak menemukannya. Lua lalu melihat metatable k, yaitu",
                    "Kucing, dan mengikuti __index-nya ke Kucing. Di sana juga nggak ada,",
                    "jadi Lua lanjut ke metatable Kucing, yaitu Hewan, dan menemukannya.",
                    "",
                    "k.kaki ditemukan dengan rantai yang sama, berakhir di Hewan. k.sayap",
                    "nggak ada di mana pun, jadi hasilnya nil.",
                    "",
                    "Itu yang disebut OOP berbasis prototipe: objek meminjam dari objek lain,",
                    "tanpa kelas. JavaScript bekerja dengan ide yang sama lewat rantai",
                    "prototype.",
                    "",
                    "Jebakan: memanggil dengan titik, k.bersuara(), bukan titik dua.",
                    "Parameter self jadi nil, dan Lua berhenti dengan pesan attempt to",
                    "index a nil value (local 'self').",
                ],
            },
            {
                "heading": "Closure",
                "bahasa": "lua",
                "code": """local function buatPenghitung()
  local n = 0
  return function()
    n = n + 1
    return n
  end
end

local hitung = buatPenghitung()
print(hitung())   --> 1
print(hitung())   --> 2
local lain = buatPenghitung()
print(lain())     --> 1""",
            },
            {
                "body": [
                    "Closure adalah fungsi yang membawa variabel dari tempat ia dibuat.",
                    "Fungsi yang dikembalikan buatPenghitung tetap bisa membaca dan",
                    "mengubah n, walaupun buatPenghitung sudah selesai. Tiap panggilan",
                    "buatPenghitung membuat n yang baru, jadi hitung dan lain punya",
                    "hitungan masing-masing. Python punya hal yang sama, dengan kata",
                    "nonlocal untuk mengubah variabelnya.",
                ],
            },
            {
                "heading": "Coroutine: resume dan yield",
                "bahasa": "lua",
                "code": """local produsen = coroutine.create(function()
  for i = 1, 3 do
    print("produsen kirim", i)
    coroutine.yield(i)
  end
  return "habis"
end)

for _ = 1, 4 do
  local ok, nilai = coroutine.resume(produsen)
  print("main terima", ok, nilai)
end
print(coroutine.status(produsen))""",
            },
            {
                "body": [
                    "Keluarannya (kolom dipisah tab):",
                    "",
                    "  produsen kirim   1",
                    "  main terima      true   1",
                    "  produsen kirim   2",
                    "  main terima      true   2",
                    "  produsen kirim   3",
                    "  main terima      true   3",
                    "  main terima      true   habis",
                    "  dead",
                    "",
                    "Coroutine adalah fungsi yang bisa berhenti di tengah jalan lalu",
                    "dilanjutkan. coroutine.resume menjalankannya sampai bertemu yield.",
                    "Nilai yang dioper ke yield dikembalikan ke pemanggil resume. Panggilan",
                    "resume berikutnya melanjutkan tepat sesudah yield tadi. Setelah",
                    "fungsinya selesai, statusnya dead.",
                    "",
                    "Coroutine beda dengan thread. Thread bisa jalan bersamaan dan",
                    "disela sistem operasi kapan saja. Coroutine bergantian: cuma satu yang",
                    "jalan, dan ia sendiri yang memutuskan kapan menyerahkan giliran.",
                    "Karena itu nggak ada data race. Engine game memakai coroutine untuk",
                    "urutan kejadian seperti dialog atau animasi yang berlangsung beberapa",
                    "frame.",
                ],
            },
            {
                "heading": "Padanannya di Python: generator",
                "code": """def produsen():
    for i in range(1, 4):
        print("produsen kirim", i)
        yield i

for nilai in produsen():
    print("main terima", nilai)""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  produsen kirim 1",
                    "  main terima 1",
                    "  produsen kirim 2",
                    "  main terima 2",
                    "  produsen kirim 3",
                    "  main terima 3",
                    "",
                    "Generator Python adalah coroutine yang lebih terbatas: yield hanya",
                    "boleh di fungsi generator itu sendiri. Coroutine Lua boleh yield dari",
                    "fungsi yang dipanggil di dalamnya, sedalam apa pun.",
                ],
            },
            {
                "heading": "Lua yang tertanam: Redis, Neovim, OpenResty",
                "bahasa": "lua",
                "code": """-- tambah-stok.lua: dijalankan Redis secara atomik
local stok = redis.call("GET", KEYS[1])
if not stok then
  return nil
end
return redis.call("INCRBY", KEYS[1], ARGV[1])""",
            },
            {
                "body": [
                    "Skrip di atas nggak bisa dijalankan dengan perintah lua biasa.",
                    "Variabel redis dan dua table masukannya baru tersedia waktu skrip",
                    "dikirim ke Redis lewat redis-cli:",
                    "",
                    "  redis-cli EVAL \"$(cat tambah-stok.lua)\" 1 stok:apel 5",
                    "",
                    "Begitulah pola bahasa tertanam: Lua menyediakan logika, programnya",
                    "menyediakan fungsi. Redis menjalankan skrip seutuhnya tanpa disela",
                    "perintah lain, jadi cek-lalu-ubah di atas aman walau banyak klien",
                    "mengakses bersamaan.",
                    "",
                    "Redis memakai Lua 5.1. Neovim dan OpenResty memakai LuaJIT, yaitu",
                    "implementasi Lua dengan kompilator JIT yang kompatibel dengan Lua",
                    "5.1. Jadi fitur baru seperti operator // dan deklarasi global",
                    "nggak selalu tersedia; cek dulu Lua versi berapa yang ditanam.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Layanan web sering membatasi jumlah permintaan per pengguna, misalnya",
                    "100 permintaan per menit, supaya server nggak kewalahan. Batas ini",
                    "banyak disimpan di Redis, dan cara aman menaikkan hitungannya adalah",
                    "skrip Lua kecil.",
                    "",
                    "Kasus kecil: login ke aplikasimu dicoba ribuan kali dari satu alamat",
                    "IP. Kamu ingin menolak lebih dari 5 percobaan per menit per IP.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Simpan hitungan dengan kunci yang memuat IP, misalnya",
                    "     login:10.0.0.5.",
                    "  2. Tulis skrip Lua yang menaikkan hitungan dan memasang umur kunci",
                    "     hanya pada percobaan pertama:",
                    "       local n = redis.call(\"INCR\", KEYS[1])",
                    "       if n == 1 then",
                    "         redis.call(\"EXPIRE\", KEYS[1], ARGV[1])",
                    "       end",
                    "       return n",
                    "  3. Jalankan skrip itu setiap ada percobaan login, dengan argumen",
                    "     pertama 60 (detik).",
                    "  4. Kalau hasilnya lebih dari 5, tolak login dan tampilkan pesan",
                    "     coba lagi nanti.",
                    "  5. Menaikkan hitungan dan memasang umur terjadi di satu skrip. Jadi",
                    "     nggak ada celah di mana kunci dibuat tapi lupa diberi umur.",
                ],
            },
        ],
    },
    {
        "title": "11. GDScript: Node, Signal, dan Game Loop di Godot",
        "sections": [
            {
                "body": [
                    "Godot adalah engine game sumber terbuka berlisensi MIT, jadi gratis",
                    "dipakai tanpa bagi hasil. GDScript adalah bahasa skrip bawaannya.",
                    "Sintaksnya mirip Python: indentasi bermakna, nggak ada kurung",
                    "kurawal, dan fungsi ditulis dengan func. Bedanya, GDScript menempel",
                    "erat ke editor Godot dan semua isi game-mu.",
                    "",
                    "Versi terbaru saat materi ini ditulis (Oktober 2026) adalah Godot",
                    "4.7.2, rilis Agustus 2026, dan Fedora 44 membawa versi yang sama di",
                    "dnf. Di Survei Stack Overflow 2026, GDScript dipakai 4,0% responden",
                    "dan termasuk yang paling disukai pemakainya (admired 53,8%). Game",
                    "indie seperti Brotato dibuat dengan Godot.",
                    "",
                    "Materi ini fokus ke bahasanya. Cara memakai editor, fisika, dan",
                    "ekspor game dibahas di kurikulum game.",
                ],
            },
            {
                "heading": "Scene tree dan node",
                "body": [
                    "Semua yang ada di game Godot adalah node: sprite, suara, kamera,",
                    "tombol, area tabrakan. Node disusun jadi pohon yang disebut scene",
                    "tree. Satu pohon yang disimpan ke berkas .tscn disebut scene, dan",
                    "scene bisa dipasang di dalam scene lain. Pemain bisa jadi satu",
                    "scene, koin satu scene, lalu dua-duanya dipasang di scene level.",
                    "",
                    "Skrip GDScript selalu ditempelkan ke satu node. Baris pertama skrip",
                    "menyebut jenis node itu dengan extends, dan dari sana skrip bisa",
                    "membaca properti node seperti position atau visible.",
                ],
            },
            {
                "heading": "Skrip pertama: _ready dan _process",
                "bahasa": "gdscript",
                "code": """extends Node2D

@export var kecepatan: float = 200.0

func _ready() -> void:
    print("Pemain siap di posisi ", position)

func _process(delta: float) -> void:
    var arah := Input.get_axis("ui_left", "ui_right")
    position.x += arah * kecepatan * delta""",
            },
            {
                "body": [
                    "Godot memanggil fungsi tertentu di saat tertentu. Fungsi seperti ini",
                    "disebut callback, dan namanya diawali garis bawah:",
                    "  - _ready() dipanggil sekali, waktu node dan anak-anaknya sudah",
                    "    masuk ke scene tree.",
                    "  - _process(delta) dipanggil setiap frame.",
                    "  - _physics_process(delta) dipanggil dengan selang tetap, dipakai",
                    "    untuk gerak berbasis fisika.",
                    "",
                    "@export membuat kecepatan muncul di panel Inspector editor, jadi",
                    "nilainya bisa diubah tanpa menyentuh kode. Input.get_axis memberi",
                    "angka dari -1 sampai 1 sesuai tombol panah yang ditekan.",
                ],
            },
            {
                "heading": "Game loop dan delta",
                "code": """DELTA = 0.5        # detik per frame, dibesarkan supaya gampang dihitung
kecepatan = 4.0    # satuan per detik
posisi = 0.0

for frame in range(1, 5):
    posisi += kecepatan * DELTA
    print(f"frame {frame}: posisi {posisi}")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  frame 1: posisi 2.0",
                    "  frame 2: posisi 4.0",
                    "  frame 3: posisi 6.0",
                    "  frame 4: posisi 8.0",
                    "",
                    "Setiap game berjalan dalam satu putaran besar yang disebut game loop:",
                    "baca input, perbarui keadaan, gambar layar, ulangi. Program Python di",
                    "atas meniru bagian perbarui keadaan.",
                    "",
                    "delta adalah lama frame sebelumnya dalam detik. Di 60 FPS nilainya",
                    "sekitar 0,0167. Mengalikan kecepatan dengan delta membuat gerakan",
                    "tetap sama cepat walau FPS turun naik. Tanpa delta, pemain di laptop",
                    "yang menampilkan 144 FPS bergerak lebih dari dua kali lipat lebih",
                    "cepat daripada di laptop 60 FPS.",
                ],
            },
            {
                "heading": "Signal: memberi kabar tanpa saling kenal",
                "bahasa": "gdscript",
                "code": """# koin.gd, ditempel ke node Area2D bernama Koin
extends Area2D

signal diambil(nilai: int)

func _ready() -> void:
    body_entered.connect(_on_body_entered)

func _on_body_entered(body: Node2D) -> void:
    diambil.emit(10)
    queue_free()""",
            },
            {
                "body": [
                    "Signal adalah pengumuman. Node koin nggak tahu siapa yang peduli",
                    "kalau ia diambil; ia cuma memancarkan signal diambil. Siapa pun yang",
                    "sudah menghubungkan diri ke signal itu akan dipanggil. Pola ini",
                    "disebut observer, dan membuat koin bisa dipakai ulang di level mana",
                    "pun.",
                    "",
                    "body_entered adalah signal bawaan Area2D, dipancarkan waktu benda",
                    "fisik masuk ke areanya. queue_free() menghapus koin dengan aman di",
                    "akhir frame. Di sisi lain, scene utama menghubungkan diri ke signal",
                    "buatan kita:",
                ],
            },
            {
                "heading": "Menghubungkan signal",
                "bahasa": "gdscript",
                "code": """# main.gd
extends Node2D

var skor := 0

func _ready() -> void:
    $Koin.diambil.connect(_on_koin_diambil)

func _on_koin_diambil(nilai: int) -> void:
    skor += nilai
    $HUD/Label.text = "Skor: %d" % skor""",
            },
            {
                "body": [
                    "$Koin adalah singkatan untuk mengambil node anak bernama Koin, dan",
                    "$HUD/Label menelusuri jalur di scene tree. connect menerima fungsi",
                    "sebagai nilai, jadi _on_koin_diambil ditulis tanpa tanda kurung.",
                    "",
                    "Soal tipe: GDScript memakai tipe opsional. var hp = 100 bertipe",
                    "dinamis, var hp: int = 100 bertipe statis, dan var hp := 100 ditebak",
                    "tipenya dari nilai. Kode bertipe membuat editor bisa menandai",
                    "kesalahan sebelum game dijalankan, dan dijalankan lebih cepat.",
                ],
            },
            {
                "heading": "Menjalankan skrip tanpa editor",
                "bahasa": "gdscript",
                "code": """# halo.gd
extends SceneTree

func _init() -> void:
    print("Halo, Dunia!")
    quit()""",
            },
            {
                "heading": "Perintahnya",
                "bahasa": "terminal",
                "code": """sudo dnf install godot
godot --headless --script halo.gd""",
            },
            {
                "body": [
                    "Skrip yang dijalankan langsung dengan --script harus mewarisi",
                    "SceneTree atau MainLoop. --headless membuat Godot jalan tanpa jendela,",
                    "berguna untuk mencoba GDScript di terminal atau menjalankan tes di",
                    "server CI.",
                    "",
                    "Jebakan: banyak tutorial di internet masih untuk Godot 3, dan",
                    "kodenya ditolak Godot 4. Beberapa perubahan yang paling sering",
                    "ditemui:",
                    "  - export var menjadi @export var.",
                    "  - yield menjadi await.",
                    "  - KinematicBody2D berganti nama jadi CharacterBody2D.",
                    "  - connect(\"diambil\", self, \"_on_diambil\") menjadi",
                    "    diambil.connect(_on_diambil).",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Game indie 2D yang dirilis di Steam dan itch.io makin banyak dibuat",
                    "dengan Godot, karena engine-nya gratis, ringan, dan nggak meminta bagi",
                    "hasil penjualan. Hampir semua logika game-nya ditulis dengan GDScript.",
                    "",
                    "Kasus kecil: di game buatanmu, koin bisa diambil, tapi angka skor di",
                    "layar nggak pernah berubah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan signal-nya dipancarkan. Tambahkan print(\"emit\") tepat",
                    "     sebelum diambil.emit(10) dan lihat panel Output.",
                    "  2. Kalau emit tercetak, cek apakah connect pernah jalan. Tambahkan",
                    "     print di _ready main.gd.",
                    "  3. Cek jalurnya. Kalau node koin bernama Koin2 atau dipindah ke",
                    "     dalam node lain, $Koin menghasilkan null dan connect gagal.",
                    "  4. Kalau ada banyak koin, kumpulkan dalam grup koin lalu",
                    "     hubungkan satu per satu:",
                    "       for k in get_tree().get_nodes_in_group(\"koin\"):",
                    "           k.diambil.connect(_on_koin_diambil)",
                    "  5. Jalankan lagi dan pastikan Label berubah tiap koin diambil.",
                ],
            },
        ],
    },
    {
        "title": "12. Peta Skrip Game: Luau, GML, dan Haxe",
        "sections": [
            {
                "body": [
                    "Banyak orang pertama kali menulis kode di dalam engine game, jauh",
                    "sebelum belajar di sekolah. Selain Lua dan GDScript, ada tiga bahasa yang",
                    "sering kamu temui di dunia game: Luau di Roblox, GML di GameMaker,",
                    "dan Haxe untuk game lintas platform. Materi ini memetakan ketiganya:",
                    "apa itu, dipakai di mana, dan kapan layak dipilih.",
                ],
            },
            {
                "heading": "Luau: bahasa Roblox",
                "bahasa": "luau",
                "code": """--!strict
local Players = game:GetService("Players")

local function sapa(pemain: Player)
    local nama = pemain.Name
    print(`Halo, {nama}!`)
end

Players.PlayerAdded:Connect(sapa)""",
            },
            {
                "body": [
                    "Luau adalah turunan Lua 5.1 buatan Roblox. Ia menambahkan pemeriksaan",
                    "tipe bertahap (baris --!strict di atas menyalakan mode ketat),",
                    "interpolasi teks dengan backtick, operator += dan continue, serta",
                    "mesin yang lebih cepat. Sejak 2021 Luau bersumber terbuka dengan",
                    "lisensi MIT, dan rilisnya mingguan; versi terbaru saat materi ini",
                    "ditulis 0.743.",
                    "",
                    "GitHub Octoverse 2025 mencatat Luau sebagai bahasa dengan pertumbuhan",
                    "tercepat di GitHub. Banyak remaja mulai ngoding dari Roblox Studio,",
                    "yang tersedia untuk Windows dan macOS. Sebagian besar kodenya",
                    "berurusan dengan API game seperti Players dan Workspace, bukan",
                    "bahasanya sendiri. Kalau kamu sudah menguasai materi Lua di bab ini,",
                    "Luau tinggal menambah anotasi tipe.",
                ],
            },
            {
                "heading": "GML: bahasa GameMaker",
                "bahasa": "gml",
                "code": """// Create Event objek pemain
kecepatan = 4;
skor = 0;

// Step Event: jalan tiap frame
if (keyboard_check(vk_right)) x += kecepatan;
if (keyboard_check(vk_left)) x -= kecepatan;

// Draw Event
draw_self();
draw_text(16, 16, "Skor: " + string(skor));""",
            },
            {
                "body": [
                    "GML (GameMaker Language) adalah bahasa di dalam GameMaker, engine",
                    "khusus game 2D yang ramah pemula. Sintaksnya mirip C dan JavaScript.",
                    "Undertale adalah contoh game terkenal yang dibuat dengan GameMaker.",
                    "",
                    "Kode GML ditempel ke event milik objek: Create jalan sekali waktu",
                    "objek dibuat, Step jalan tiap frame, Draw menggambar. Perhatikan",
                    "bahwa contoh di atas menambah x dengan angka tetap tanpa delta. Itu",
                    "gaya GameMaker yang umum, karena game berjalan dengan kecepatan",
                    "frame tetap (bawaannya 60 frame per detik). Bandingkan dengan",
                    "_process(delta) di Godot.",
                    "",
                    "Selain kode teks, ada GML Visual yang menyusun blok. GameMaker",
                    "berlisensi proprietary: gratis untuk karya non-komersial, dan lisensi",
                    "komersialnya 99,99 dolar AS sekali bayar. Versi terbarunya GameMaker",
                    "LTS 2026.0 (Mei 2026). IDE-nya resmi untuk Windows dan macOS; cek",
                    "situs gamemaker.io untuk status dukungan Linux.",
                ],
            },
            {
                "heading": "Haxe: satu kode, banyak target",
                "bahasa": "haxe",
                "code": """class Main {
    static function main() {
        var nilai = [70, 85, 90];
        var total = 0;
        for (n in nilai) total += n;
        trace('Total: $total');
    }
}""",
            },
            {
                "body": [
                    "Haxe adalah bahasa bertipe statis yang dikompilasi ke banyak target:",
                    "JavaScript, C++, bytecode HashLink, JVM, dan lainnya. Satu kode bisa",
                    "jadi game di browser, di PC, dan di konsol. Pustaka game yang dibangun",
                    "di atasnya antara lain Heaps (dipakai Dead Cells dan Northgard),",
                    "OpenFL, dan HaxeFlixel.",
                    "",
                    "Simpan contoh di atas sebagai Main.hx (nama berkas harus sama dengan",
                    "nama kelas), lalu jalankan dengan haxe -main Main --interp. trace",
                    "mencetak lokasi juga, jadi keluarannya Main.hx:6: Total: 245. Versi",
                    "stabil terbaru 4.3.7 (Mei 2025), tersedia di dnf Fedora 44, dan Haxe",
                    "5 masih dikembangkan. Kompilatornya berlisensi GPL-2.0, sedangkan",
                    "pustaka standarnya MIT, jadi game-mu bebas dijual.",
                ],
            },
            {
                "heading": "Memilih bahasa game",
                "body": [
                    "Buat pemula yang ingin membuat game sendiri, pilihan paling masuk",
                    "akal biasanya Godot dengan GDScript. Engine-nya gratis, sumber",
                    "terbuka, jalan di Fedora, dan bisa ekspor ke Android dan web.",
                    "",
                    "  - Mau membuat game yang langsung dimainkan jutaan pemain Roblox:",
                    "    Luau di Roblox Studio.",
                    "  - Fokus game 2D dan suka alur kerja visual: GameMaker dengan GML.",
                    "  - Butuh satu kode untuk banyak platform dan suka tipe statis: Haxe.",
                    "  - Ingin game 2D ringan dengan bahasa sekecil mungkin: Love2D atau",
                    "    Defold dengan Lua.",
                    "",
                    "Engine besar seperti Unity (C#) dan Unreal (C++ dan Blueprint)",
                    "dibahas di kurikulum game.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Friday Night Funkin', game ritme yang kodenya terbuka di GitHub,",
                    "ditulis dengan Haxe dan HaxeFlixel. Banyak mod buatan penggemar",
                    "lahir karena kodenya bisa dibaca siapa saja. Ini contoh bagus kenapa",
                    "mengenali bahasa game berguna: kamu bisa belajar langsung dari kode",
                    "game yang sudah jadi.",
                    "",
                    "Kasus kecil: temanmu ingin membuat game platformer 2D untuk PC dan",
                    "Android, tanpa biaya lisensi, dan meminta saran bahasa.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Catat syaratnya: 2D, PC dan Android, gratis.",
                    "  2. Coret yang nggak memenuhi. Roblox mengikat game ke platform",
                    "     Roblox, dan GameMaker butuh lisensi untuk dijual.",
                    "  3. Tersisa Godot (GDScript), Haxe (HaxeFlixel atau Heaps), dan",
                    "     Defold atau Love2D (Lua).",
                    "  4. Untuk pemula, sarankan Godot: editornya lengkap, tutorialnya",
                    "     paling banyak, dan GDScript mirip Python.",
                    "  5. Ingatkan untuk memakai tutorial Godot 4, bukan Godot 3.",
                ],
            },
        ],
    },
    {
        "title": "13. Swift: Optional, Struct, dan Protokol",
        "sections": [
            {
                "body": [
                    "Swift adalah bahasa buatan Apple yang diperkenalkan tahun 2014 untuk",
                    "menggantikan Objective-C. Hampir semua aplikasi baru di iPhone, iPad,",
                    "Mac, dan Apple Watch ditulis dengan Swift. Bahasanya bersumber",
                    "terbuka dengan lisensi Apache 2.0, jadi juga jalan di Linux dan",
                    "Windows untuk server dan alat baris perintah.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "6.4.1, rilis 15 Oktober 2026. Swift rilis besar setahun sekali. Di",
                    "Survei Stack Overflow 2026 pemakainya 5,9%.",
                    "",
                    "Perlu kamu tahu dari awal: membuat aplikasi iOS wajib",
                    "memakai Mac dengan Xcode. Di Fedora kamu bisa mempelajari bahasanya,",
                    "menulis program baris perintah, dan membuat server dengan Vapor.",
                    "Itu cukup untuk materi ini.",
                ],
            },
            {
                "heading": "let, var, dan inferensi",
                "bahasa": "swift",
                "code": "let nama = \"Ani\"        // konstanta, nggak bisa diubah\nvar umur = 17           // variabel, tipenya Int ditebak\numur += 1\nlet tinggi: Double = 160.5\nprint(\"\\(nama) umur \\(umur), tinggi \\(tinggi)\")",
            },
            {
                "body": [
                    "Program di atas mencetak Ani umur 18, tinggi 160.5.",
                    "",
                    "let untuk nilai yang nggak berubah, var untuk yang berubah. Programmer",
                    "Swift memakai let sebanyak mungkin; kompilator bahkan memberi",
                    "peringatan kalau var nggak pernah diubah. Teks disisipi nilai dengan",
                    "\\(...), mirip f-string di Python. Swift bertipe statis dengan",
                    "inferensi: tipe umur ditebak Int, dan kamu nggak bisa mengisinya",
                    "dengan teks nanti.",
                ],
            },
            {
                "heading": "Optional: ?, !, if let, guard, ??",
                "bahasa": "swift",
                "code": "let input = \"42a\"\nlet angka: Int? = Int(input)     // gagal diubah: nil\n\nif let n = angka {\n    print(\"angkanya \\(n)\")\n} else {\n    print(\"bukan angka\")\n}\nprint(angka ?? 0)\n\nfunc sapa(_ nama: String?) {\n    guard let nama else {\n        print(\"nama kosong\")\n        return\n    }\n    print(\"Halo, \\(nama)\")\n}\nsapa(nil)\nsapa(\"Budi\")",
            },
            {
                "body": [
                    "Keluarannya kalau dijalankan dengan swift:",
                    "",
                    "  bukan angka",
                    "  0",
                    "  nama kosong",
                    "  Halo, Budi",
                    "",
                    "Int? dibaca \"Int opsional\": kotak yang isinya bisa satu Int atau nil.",
                    "Int(\"42a\") gagal, jadi hasilnya nil. Swift nggak mengizinkan kamu",
                    "memakai Int? seolah Int biasa. Kamu wajib membuka kotaknya dulu:",
                    "",
                    "  - if let n = angka: kalau ada isinya, n berisi Int dan blok jalan.",
                    "  - guard let nama else { ... }: kebalikannya, keluar lebih awal",
                    "    kalau kosong, lalu sisa fungsi bisa memakai nama sebagai String.",
                    "  - angka ?? 0: pakai isinya, atau 0 kalau kosong.",
                    "  - angka!: buka paksa.",
                    "",
                    "Jebakan: tanda ! membuka optional tanpa memeriksa. Kalau isinya nil,",
                    "program langsung berhenti dengan Fatal error: Unexpectedly found nil",
                    "while unwrapping an Optional value. Di aplikasi iPhone, itu artinya",
                    "aplikasi tertutup sendiri di tangan pengguna. Pakai ! hanya kalau",
                    "kamu bisa menjelaskan kenapa nilainya pasti ada.",
                ],
            },
            {
                "heading": "Kotlin memakai ide yang sama",
                "bahasa": "kotlin",
                "code": """fun sapa(nama: String?) {
    val panjang = nama?.length ?: 0
    println("panjang nama: $panjang")
    if (nama != null) {
        println("Halo, $nama")   // di sini nama sudah dianggap String
    }
}

fun main() {
    sapa(null)
    sapa("Budi")
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  panjang nama: 0",
                    "  panjang nama: 4",
                    "  Halo, Budi",
                    "",
                    "Kalau kamu sudah mengikuti kurikulum Kotlin, polanya terasa akrab.",
                    "String? di Kotlin sama dengan String? di Swift. Operator ?: di Kotlin",
                    "sama dengan ?? di Swift. Kotlin membuka otomatis sesudah pengecekan",
                    "nama != null (smart cast), sedangkan Swift memakai if let. Dua bahasa",
                    "ini lahir di masa yang sama dan sama-sama memperlakukan null sebagai",
                    "tipe tersendiri.",
                ],
            },
            {
                "heading": "struct dan class: nilai dan referensi",
                "bahasa": "swift",
                "code": """struct Titik {
    var x: Int
    var y: Int
}

class Akun {
    var saldo: Int
    init(saldo: Int) { self.saldo = saldo }
}

var a = Titik(x: 1, y: 2)
var b = a          // disalin
b.x = 99
print(a.x)         // 1

let p = Akun(saldo: 100)
let q = p          // menunjuk objek yang sama
q.saldo = 0
print(p.saldo)     // 0""",
            },
            {
                "body": [
                    "Ini perbedaan paling penting di Swift. struct adalah tipe nilai:",
                    "b = a membuat salinan, jadi mengubah b nggak menyentuh a. class",
                    "adalah tipe referensi: q = p membuat dua nama untuk satu objek yang",
                    "sama.",
                    "",
                    "Di Swift, banyak tipe dasar seperti String, Array, dan Dictionary",
                    "adalah struct. Jadi menyalin array ke variabel lain lalu mengubahnya",
                    "nggak mengubah array aslinya, beda dengan list di Python. Swift",
                    "menyarankan struct sebagai pilihan pertama, dan class kalau kamu",
                    "butuh pewarisan atau satu objek yang dipakai bersama.",
                    "",
                    "Perilaku yang sama bisa ditiru di Python dengan menyalin dict:",
                ],
            },
            {
                "heading": "Padanannya di Python",
                "code": """a = {"x": 1, "y": 2}
b = dict(a)        # salinan, mirip struct Swift
b["x"] = 99
print(a["x"])

p = {"saldo": 100}
q = p              # objek yang sama, mirip class Swift
q["saldo"] = 0
print(p["saldo"])""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  1",
                    "  0",
                ],
            },
            {
                "heading": "enum dengan nilai terkait",
                "bahasa": "swift",
                "code": "enum Pembayaran {\n    case tunai\n    case transfer(bank: String)\n    case qris(kode: String)\n}\n\nfunc jelaskan(_ p: Pembayaran) -> String {\n    switch p {\n    case .tunai:\n        return \"bayar tunai\"\n    case .transfer(let bank):\n        return \"transfer lewat \\(bank)\"\n    case .qris(let kode):\n        return \"QRIS \\(kode)\"\n    }\n}\n\nprint(jelaskan(.transfer(bank: \"BRI\")))",
            },
            {
                "body": [
                    "enum di Swift jauh lebih kuat daripada daftar konstanta. Tiap kasus",
                    "boleh membawa data sendiri: transfer membawa nama bank, qris membawa",
                    "kode. switch wajib menangani semua kasus. Kalau suatu hari kamu",
                    "menambah case ewallet dan lupa menanganinya, kompilator menolak",
                    "sampai switch-nya diperbaiki. Program di atas mencetak kalimat",
                    "transfer lengkap dengan nama bank yang dioper.",
                ],
            },
            {
                "heading": "Protokol",
                "bahasa": "swift",
                "code": """protocol Bentuk {
    var nama: String { get }
    func luas() -> Double
}

struct Persegi: Bentuk {
    let sisi: Double
    var nama: String { "persegi" }
    func luas() -> Double { sisi * sisi }
}

struct Lingkaran: Bentuk {
    let r: Double
    var nama: String { "lingkaran" }
    func luas() -> Double { 3.14 * r * r }
}

let semua: [any Bentuk] = [Persegi(sisi: 2), Lingkaran(r: 1)]
for b in semua {
    print(b.nama, b.luas())
}""",
            },
            {
                "body": [
                    "Protokol adalah daftar kemampuan yang wajib dimiliki sebuah tipe,",
                    "mirip interface di Java dan Kotlin. Persegi dan Lingkaran sama-sama",
                    "berjanji punya nama dan luas(), jadi keduanya bisa dimasukkan ke satu",
                    "array bertipe any Bentuk. Program ini mencetak persegi 4.0 dan",
                    "lingkaran 3.14.",
                    "",
                    "Swift sering disebut bahasa berorientasi protokol. Banyak kemampuan",
                    "pustaka standar datang dari protokol seperti Equatable (bisa",
                    "dibandingkan dengan ==), Comparable, dan Codable (bisa diubah ke dan",
                    "dari JSON).",
                ],
            },
            {
                "heading": "Memasang Swift di Fedora",
                "bahasa": "terminal",
                "code": """sudo dnf install swift-lang
swift --version
swift halo.swift
mkdir kasir && cd kasir
swift package init --type executable
swift run""",
            },
            {
                "body": [
                    "Paket swift-lang di Fedora 44 berisi Swift 6.3. Untuk versi terbaru,",
                    "situs swift.org menyediakan pemasang bernama swiftly. swift halo.swift",
                    "menjalankan satu berkas langsung, sedangkan swift package init",
                    "membuat proyek lengkap dengan Package.swift.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan crash aplikasi iPhone sering berujung ke satu tanda !. Data",
                    "dari server biasanya dianggap selalu lengkap, sampai suatu hari ada",
                    "satu pengguna yang kolomnya kosong.",
                    "",
                    "Kasus kecil: aplikasi toko menampilkan nomor HP pengguna dari JSON",
                    "server dengan kode let hp = data[\"hp\"] as! String. Pengguna yang",
                    "belum mengisi nomor HP membuat aplikasi tertutup sendiri.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari semua as! dan ! di bagian yang membaca data dari luar.",
                    "  2. Jadikan propertinya optional di model:",
                    "       struct Pengguna: Codable {",
                    "           let nama: String",
                    "           let hp: String?",
                    "       }",
                    "  3. Biarkan JSONDecoder mengisi hp dengan nil kalau kolomnya",
                    "     kosong atau nggak ada.",
                    "  4. Tampilkan dengan nilai cadangan:",
                    "       labelHP.text = pengguna.hp ?? \"belum diisi\"",
                    "  5. Uji dengan contoh JSON tanpa kolom hp dan pastikan aplikasi",
                    "     tetap terbuka.",
                ],
            },
        ],
    },
    {
        "title": "14. Swift Lanjut: Konkurensi dan Warisan Objective-C",
        "sections": [
            {
                "body": [
                    "Aplikasi iPhone hampir selalu menunggu sesuatu: data dari internet,",
                    "berkas dari penyimpanan, atau gambar dari kamera. Kalau penantian itu",
                    "dilakukan di thread utama, layar membeku. Materi ini membahas cara",
                    "Swift modern menangani kerja bersamaan, lalu mengajak kamu membaca",
                    "Objective-C, bahasa yang masih memenuhi banyak proyek iOS lama.",
                ],
            },
            {
                "heading": "async dan await",
                "bahasa": "swift",
                "code": "func ambilSkor(id: Int) async -> Int {\n    try? await Task.sleep(for: .milliseconds(100))\n    return id * 10\n}\n\nfunc muat() async {\n    async let a = ambilSkor(id: 1)\n    async let b = ambilSkor(id: 2)\n    let total = await a + b\n    print(\"total \\(total)\")\n}\n\nawait muat()",
            },
            {
                "body": [
                    "Fungsi bertanda async boleh menunggu tanpa memblokir thread. Setiap",
                    "titik menunggu ditandai await, jadi kamu bisa melihat di mana fungsi",
                    "itu mungkin berhenti sejenak. async let memulai dua pekerjaan",
                    "sekaligus, lalu await a + b menunggu keduanya. Totalnya 30, dan",
                    "waktu tunggunya sekitar 100 milidetik, bukan 200.",
                    "",
                    "Kalau kamu sudah kenal async/await di JavaScript, Python, atau C#,",
                    "bentuknya mirip. Bedanya, di Swift pekerjaan async bisa jalan di",
                    "beberapa thread sekaligus, jadi muncul masalah baru: data",
                    "race.",
                ],
            },
            {
                "heading": "actor dan data race",
                "bahasa": "swift",
                "code": """actor Rekening {
    private(set) var saldo = 0

    func setor(_ jumlah: Int) {
        saldo += jumlah
    }
}

func uji() async -> Int {
    let rek = Rekening()
    await withTaskGroup(of: Void.self) { grup in
        for _ in 1...1000 {
            grup.addTask { await rek.setor(1) }
        }
    }
    return await rek.saldo
}

print(await uji())   // selalu 1000""",
            },
            {
                "body": [
                    "Data race terjadi kalau dua thread mengubah data yang sama pada saat",
                    "bersamaan. saldo += 1 terdiri dari tiga langkah: baca, tambah, tulis.",
                    "Kalau dua thread membaca 41 bersamaan, keduanya menulis 42, dan satu",
                    "setoran hilang. Bug seperti ini jarang muncul dan susah diulang.",
                    "",
                    "actor adalah tipe yang isinya cuma boleh disentuh satu tugas pada",
                    "satu waktu. Tugas lain harus antre, karena itu setiap panggilan dari",
                    "luar wajib memakai await. Hasilnya selalu 1000.",
                    "",
                    "Sejak Swift 6 (2024), mode bahasa Swift 6 memeriksa data race saat",
                    "kompilasi. Kalau kamu mengoper objek class biasa yang bisa diubah ke",
                    "tugas lain, kompilator menolak dengan pesan bahwa tipenya bukan",
                    "Sendable. Pesan ini sering membingungkan pemula. Artinya sederhana:",
                    "tipe itu belum terbukti aman dipakai bersama. Jalan keluarnya",
                    "biasanya mengubahnya jadi struct, jadi actor, atau membuat",
                    "propertinya let.",
                ],
            },
            {
                "heading": "Generik dan Swift Package Manager",
                "bahasa": "swift",
                "code": """func terbesar<T: Comparable>(_ daftar: [T]) -> T? {
    guard var hasil = daftar.first else { return nil }
    for x in daftar where x > hasil {
        hasil = x
    }
    return hasil
}

print(terbesar([3, 9, 4]) ?? 0)              // 9
print(terbesar(["apel", "jeruk"]) ?? "")    // jeruk""",
            },
            {
                "body": [
                    "Generik membuat satu fungsi bekerja untuk banyak tipe. T: Comparable",
                    "artinya T boleh tipe apa saja asal bisa dibandingkan. Fungsinya",
                    "mengembalikan T? karena daftar kosong nggak punya nilai terbesar.",
                    "",
                    "Pustaka dipasang lewat Swift Package Manager (SPM). Daftarnya ditulis",
                    "di berkas Package.swift, yang juga berupa kode Swift:",
                ],
            },
            {
                "heading": "Package.swift",
                "bahasa": "swift",
                "code": """// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "Kasir",
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser", from: "1.5.0")
    ],
    targets: [
        .executableTarget(
            name: "Kasir",
            dependencies: [
                .product(name: "ArgumentParser", package: "swift-argument-parser")
            ]
        )
    ]
)""",
            },
            {
                "heading": "Membaca Objective-C",
                "bahasa": "objectivec",
                "code": """// Pemain.h
#import <Foundation/Foundation.h>

@interface Pemain : NSObject
@property (nonatomic, copy) NSString *nama;
@property (nonatomic) NSInteger skor;
- (void)tambahSkor:(NSInteger)nilai;
@end

// Pemain.m
@implementation Pemain
- (void)tambahSkor:(NSInteger)nilai {
    self.skor += nilai;
    NSLog(@"%@ sekarang punya %ld poin", self.nama, (long)self.skor);
}
@end

// pemakaian
Pemain *p = [[Pemain alloc] init];
p.nama = @"Ani";
[p tambahSkor:10];""",
            },
            {
                "body": [
                    "Objective-C adalah bahasa C ditambah sistem objek bergaya Smalltalk.",
                    "Ia lahir di tahun 1980-an, dipakai NeXT, lalu jadi bahasa utama Apple",
                    "sampai Swift datang. Cara membacanya:",
                    "",
                    "  - [p tambahSkor:10] artinya kirim pesan tambahSkor: dengan",
                    "    argumen 10 ke objek p. Di Swift jadi p.tambahSkor(10).",
                    "  - [[Pemain alloc] init] adalah dua pesan bersarang: alokasikan",
                    "    memori, lalu inisialisasi.",
                    "  - @\"Ani\" adalah objek NSString. Teks C biasa tanpa @ beda tipe.",
                    "  - Satu kelas dibagi ke dua berkas: .h (deklarasi, @interface) dan",
                    "    .m (isi, @implementation).",
                    "  - - di depan metode berarti metode objek, + berarti metode kelas.",
                    "  - NSLog mencetak ke log sistem dengan cap waktu, bukan ke keluaran",
                    "    biasa.",
                    "",
                    "Memorinya diatur ARC sejak 2011, sama seperti Swift. Kode yang lebih",
                    "tua lagi memakai retain dan release manual.",
                    "",
                    "Jebakan: di Objective-C, mengirim pesan ke nil nggak crash. Hasilnya",
                    "cuma nil atau 0, dan program jalan terus. Bug karena objek yang",
                    "ternyata kosong bisa lolos jauh sebelum ketahuan.",
                ],
            },
            {
                "heading": "Swift dan Objective-C dalam satu aplikasi",
                "body": [
                    "Banyak aplikasi iOS yang mulai dibuat sebelum 2015 berisi campuran",
                    "dua bahasa. Apple sengaja membuat keduanya bisa saling memanggil:",
                    "",
                    "  - Swift memakai kelas Objective-C lewat bridging header, berkas",
                    "    berisi daftar #import. Sesudah itu Pemain terlihat seperti kelas",
                    "    Swift biasa: let p = Pemain(); p.tambahSkor(10).",
                    "  - Objective-C memakai kelas Swift lewat header yang dibuat Xcode",
                    "    otomatis, bernama NamaApp-Swift.h. Kelas dan metode Swift-nya",
                    "    harus ditandai @objc dan mewarisi NSObject.",
                    "  - Anotasi nullable dan nonnull di header Objective-C menentukan",
                    "    apakah Swift melihat sebuah properti sebagai String? atau String.",
                    "",
                    "Statusnya, Objective-C sedang menurun. Pemakainya di Survei Stack",
                    "Overflow 2026 tinggal 2,5%, dan RedMonk Januari 2026 mencatatnya",
                    "mulai turun. Dokumentasi Apple sekarang ditulis Swift lebih dulu.",
                    "Kamu cukup bisa membacanya untuk merawat proyek lama. Antarmuka",
                    "deklaratif SwiftUI yang dipakai aplikasi baru dibahas di kurikulum",
                    "mobile.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi bank, ojek daring, dan toko daring versi iOS dimulai",
                    "di era Objective-C, lalu fitur barunya ditulis dengan Swift. Anak",
                    "baru di tim iOS biasanya diminta menambah layar baru dalam Swift,",
                    "lalu memanggilnya dari kode Objective-C lama.",
                    "",
                    "Kasus kecil: kamu menulis kelas Swift PromoViewController, tapi kode",
                    "Objective-C di MenuUtama.m nggak bisa menemukannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan kelasnya mewarisi kelas Objective-C dan ditandai @objc:",
                    "       @objc class PromoViewController: UIViewController { ... }",
                    "  2. Tandai juga metode yang mau dipanggil dari Objective-C dengan",
                    "     @objc.",
                    "  3. Di MenuUtama.m, impor header buatan Xcode:",
                    "       #import \"TokoKu-Swift.h\"",
                    "  4. Build ulang proyek supaya header itu diperbarui.",
                    "  5. Panggil dengan sintaks Objective-C:",
                    "       PromoViewController *vc = [[PromoViewController alloc] init];",
                ],
            },
        ],
    },
    {
        "title": "15. Dart: Null Safety, Kelas, dan Async",
        "sections": [
            {
                "body": [
                    "Dart adalah bahasa buatan Google yang dirilis tahun 2011. Hampir",
                    "semua orang yang belajar Dart sekarang melakukannya karena Flutter,",
                    "framework untuk membuat aplikasi Android, iOS, web, dan desktop dari",
                    "satu kode. Lowongan kerja pun biasanya menyebut Flutter, bukan Dart",
                    "saja.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "3.13.5, rilis 29 September 2026; seri 3.13 sendiri dimulai Agustus",
                    "2026. Lisensinya BSD-3-Clause. Di Survei Stack Overflow 2026",
                    "pemakainya 4,9%, dan RedMonk Januari 2026 menaruhnya di peringkat 18,",
                    "naik melewati Rust.",
                    "",
                    "Kalau kamu sudah kenal Java atau Kotlin dan JavaScript, Dart terasa",
                    "seperti campuran keduanya: kelas dan tipe statis seperti Java, async",
                    "dan sintaks santai seperti JavaScript.",
                ],
            },
            {
                "heading": "Halo Dunia dan tipe",
                "bahasa": "dart",
                "code": """void main() {
  var nama = 'Ani';          // String, ditebak
  int umur = 17;
  final kota = 'Bandung';    // diisi sekali, lalu tetap
  const pi = 3.14;           // konstanta saat kompilasi
  print('$nama, $umur tahun, tinggal di $kota');
  print('Luas: ${pi * 2 * 2}');
}""",
            },
            {
                "body": [
                    "Program Dart selalu dimulai dari fungsi main. Program di atas",
                    "mencetak Ani, 17 tahun, tinggal di Bandung, lalu Luas: 12.56.",
                    "",
                    "var meminta Dart menebak tipe. final berarti variabel cuma boleh",
                    "diisi sekali. const lebih ketat lagi: nilainya harus sudah diketahui",
                    "saat kompilasi. Teks disisipi variabel dengan $nama, atau ${...} untuk",
                    "ekspresi.",
                ],
            },
            {
                "heading": "Null safety",
                "bahasa": "dart",
                "code": """String sapa(String? nama) {
  if (nama == null) {
    return 'Halo, tamu';
  }
  return 'Halo, $nama (${nama.length} huruf)';
}

void main() {
  print(sapa(null));
  print(sapa('Budi'));
  String? kota;
  print(kota?.toUpperCase() ?? 'kota belum diisi');
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  Halo, tamu",
                    "  Halo, Budi (4 huruf)",
                    "  kota belum diisi",
                    "",
                    "Sejak Dart 3 (Mei 2023), null safety wajib. String nggak boleh null.",
                    "String? boleh. Sesudah pengecekan nama == null, Dart tahu sisa fungsi",
                    "pasti punya nama, jadi nama.length boleh dipakai. Fitur ini disebut",
                    "type promotion, padanan smart cast di Kotlin.",
                    "",
                    "Operatornya sama dengan Swift dan Kotlin: ?. memanggil kalau nggak",
                    "null, ?? memberi nilai cadangan, dan ! membuka paksa. Ada juga late",
                    "untuk variabel yang pasti diisi nanti sebelum dipakai, dan required",
                    "untuk parameter bernama yang wajib diisi.",
                ],
            },
            {
                "heading": "Kelas dan parameter bernama",
                "bahasa": "dart",
                "code": """class Produk {
  final String nama;
  final int harga;
  final int stok;

  Produk({required this.nama, required this.harga, this.stok = 0});

  bool get habis => stok == 0;

  @override
  String toString() => '$nama Rp$harga (stok $stok)';
}

void main() {
  final kopi = Produk(nama: 'Kopi', harga: 15000, stok: 3);
  final teh = Produk(nama: 'Teh', harga: 8000);
  print(kopi);
  print('${teh.nama} habis? ${teh.habis}');
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  Kopi Rp15000 (stok 3)",
                    "  Teh habis? true",
                    "",
                    "Parameter di dalam kurung kurawal adalah parameter bernama. Saat",
                    "memanggil, kamu menulis nama: 'Kopi', jadi urutannya bebas dan",
                    "kodenya terbaca jelas. required membuatnya wajib, sedangkan stok",
                    "punya nilai bawaan 0. this.nama di konstruktor langsung mengisi",
                    "properti tanpa perlu ditulis ulang.",
                    "",
                    "Parameter opsional berurutan ditulis dengan kurung siku, misalnya",
                    "void cetak(String teks, [int ulang = 1]). Pola parameter bernama ini",
                    "yang paling sering kamu lihat di Flutter, karena setiap widget",
                    "menerima puluhan pengaturan bernama.",
                ],
            },
            {
                "heading": "Future dan async/await",
                "bahasa": "dart",
                "code": """Future<int> ambilStok(String nama) async {
  await Future.delayed(Duration(milliseconds: 300));
  return nama == 'kopi' ? 3 : 0;
}

Future<void> main() async {
  print('mulai');
  final stok = await ambilStok('kopi');
  print('stok kopi: $stok');
  ambilStok('teh').then((s) => print('stok teh: $s'));
  print('main selesai');
}""",
            },
            {
                "body": [
                    "Future adalah janji bahwa sebuah nilai akan tersedia nanti. Fungsi",
                    "async selalu mengembalikan Future. await menunggu Future selesai lalu",
                    "memberi nilainya. Keluarannya:",
                    "",
                    "  mulai",
                    "  stok kopi: 3",
                    "  main selesai",
                    "  stok teh: 0",
                    "",
                    "Baris stok teh muncul paling akhir karena pemanggilan keduanya nggak",
                    "ditunggu dengan await. main jalan terus, dan callback then baru",
                    "dipanggil 300 milidetik kemudian.",
                ],
            },
            {
                "heading": "Bandingkan dengan Promise di JavaScript",
                "bahasa": "javascript",
                "code": """function ambilStok(nama) {
  return new Promise((selesai) => {
    setTimeout(() => selesai(nama === "kopi" ? 3 : 0), 300);
  });
}

async function main() {
  console.log("mulai");
  const stok = await ambilStok("kopi");
  console.log(`stok kopi: ${stok}`);
  ambilStok("teh").then((s) => console.log(`stok teh: ${s}`));
  console.log("main selesai");
}

main();""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  mulai",
                    "  stok kopi: 3",
                    "  main selesai",
                    "  stok teh: 0",
                    "",
                    "Urutannya persis sama dengan versi Dart. Future di Dart adalah",
                    "Promise di JavaScript, async dan await bekerja sama, then juga sama,",
                    "dan Future.delayed setara dengan setTimeout. Bedanya, Dart memeriksa",
                    "tipe: Future<int> nggak bisa diperlakukan seperti Future<String>.",
                ],
            },
            {
                "heading": "Proyek Dart dan pub.dev",
                "bahasa": "terminal",
                "code": """dart create -t console halo_cli
cd halo_cli
dart pub add http
dart run""",
            },
            {
                "body": [
                    "dart create membuat kerangka proyek dengan berkas pubspec.yaml,",
                    "tempat daftar paket. Paket diambil dari pub.dev, gudang paket resmi",
                    "Dart dan Flutter, mirip npm untuk JavaScript. dart pub add http",
                    "menambah paket http ke pubspec.yaml dan mengunduhnya.",
                    "",
                    "Jebakan: lupa await. Kalau kamu menulis print(ambilStok('kopi')),",
                    "yang tercetak Instance of 'Future<int>', bukan angka 3. Linter Dart",
                    "bisa diatur untuk memperingatkan Future yang nggak ditunggu",
                    "(aturan unawaited_futures).",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi Flutter hampir selalu mengambil data dari API berbentuk",
                    "JSON, lalu mengubahnya jadi objek Dart. Data dari server sering punya",
                    "kolom yang kadang null, dan null safety memaksa kamu memikirkannya",
                    "sejak menulis model.",
                    "",
                    "Kasus kecil: API produk kadang mengirim \"diskon\": null, dan aplikasi",
                    "berhenti dengan galat type 'Null' is not a subtype of type 'int'.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat contoh JSON dari server dan tandai kolom mana yang bisa",
                    "     null atau hilang.",
                    "  2. Jadikan propertinya nullable di model:",
                    "       final int? diskon;",
                    "  3. Baca dari JSON tanpa memaksa tipe int:",
                    "       diskon: json['diskon'] as int?,",
                    "  4. Di tampilan, pakai nilai cadangan:",
                    "       Text('Diskon ${produk.diskon ?? 0}%')",
                    "  5. Tulis tes kecil dengan JSON yang diskonnya null dan JSON yang",
                    "     kolom diskonnya nggak ada sama sekali.",
                ],
            },
        ],
    },
    {
        "title": "16. Dart Lanjut: Event Loop, Stream, dan Isolate",
        "sections": [
            {
                "body": [
                    "Kode Dart berjalan di satu thread per isolate. Nggak ada dua baris",
                    "kode Dart yang jalan bersamaan di isolate yang sama. Lalu bagaimana",
                    "aplikasi Flutter bisa menunggu data dari internet sambil tetap",
                    "menggambar layar 60 kali per detik? Kuncinya ada di event loop.",
                    "",
                    "Event loop adalah putaran yang terus mengambil pekerjaan dari antrean",
                    "dan menjalankannya satu per satu. Memahami urutannya membantu kamu",
                    "menebak keluaran kode async, dan tahu kapan sebuah pekerjaan terlalu",
                    "berat untuk thread utama.",
                ],
            },
            {
                "heading": "Dua antrean: microtask dan event",
                "bahasa": "dart",
                "code": """import 'dart:async';

void main() {
  print('1. main mulai');
  Future(() => print('5. event dari Future()'));
  Future.delayed(Duration.zero, () => print('6. event dari Future.delayed'));
  scheduleMicrotask(() => print('3. microtask'));
  Future.value(7).then((v) => print('4. then dari Future.value($v)'));
  print('2. main selesai');
}""",
            },
            {
                "body": [
                    "Keluarannya, urut sesuai nomor di teksnya:",
                    "",
                    "  1. main mulai",
                    "  2. main selesai",
                    "  3. microtask",
                    "  4. then dari Future.value(7)",
                    "  5. event dari Future()",
                    "  6. event dari Future.delayed",
                    "",
                    "Dart punya dua antrean. Antrean microtask untuk pekerjaan kecil yang",
                    "harus segera dikerjakan. Antrean event untuk timer, masukan pengguna,",
                    "dan data dari jaringan. Aturannya:",
                    "",
                    "  1. Kode yang sedang berjalan (di sini main) selalu diselesaikan dulu.",
                    "  2. Sesudah itu, semua microtask dikerjakan sampai antreannya kosong,",
                    "     termasuk microtask yang ditambahkan oleh microtask lain.",
                    "  3. Baru satu event diambil dan dikerjakan.",
                    "  4. Kembali ke langkah 2.",
                    "",
                    "scheduleMicrotask dan callback then dari Future yang sudah selesai",
                    "masuk antrean microtask. Future(...) dan Future.delayed masuk antrean",
                    "event lewat timer. Di dalam satu antrean, yang masuk lebih dulu",
                    "dikerjakan lebih dulu.",
                ],
            },
            {
                "heading": "Event yang menjadwalkan microtask",
                "bahasa": "dart",
                "code": """import 'dart:async';

void main() {
  Future(() {
    print('A: event pertama');
    scheduleMicrotask(() => print('B: microtask dari A'));
  });
  Future(() => print('C: event kedua'));
}""",
            },
            {
                "body": [
                    "Keluarannya A, lalu B, lalu C. Microtask yang dijadwalkan di dalam",
                    "event A dikerjakan sesudah A selesai, sebelum event C. Aturan langkah",
                    "2 berlaku setiap kali satu event selesai.",
                    "",
                    "Jebakan: microtask yang terus menjadwalkan microtask baru membuat",
                    "antrean event nggak pernah disentuh. Di Flutter, itu artinya layar",
                    "berhenti digambar ulang. Pakai Future biasa untuk pekerjaan yang",
                    "nggak harus segera.",
                ],
            },
            {
                "heading": "Stream dan async*",
                "bahasa": "dart",
                "code": """Stream<int> hitungMundur(int dari) async* {
  for (var i = dari; i > 0; i--) {
    await Future.delayed(Duration(milliseconds: 100));
    yield i;
  }
}

Future<void> main() async {
  await for (final n in hitungMundur(3)) {
    print(n);
  }
  print('meluncur!');

  final genap = hitungMundur(6).where((n) => n.isEven).map((n) => n * 10);
  print(await genap.toList());
}""",
            },
            {
                "body": [
                    "Future memberi satu nilai di masa depan. Stream memberi banyak nilai",
                    "satu per satu, seperti pesan chat yang masuk atau posisi GPS yang",
                    "terus diperbarui. Fungsi bertanda async* menghasilkan Stream, dan",
                    "setiap yield mengirim satu nilai. await for membaca stream sampai",
                    "habis.",
                    "",
                    "Program di atas mencetak 3, 2, 1, meluncur!, lalu [60, 40, 20].",
                    "Stream punya metode yang mirip daftar, seperti where dan map. Untuk",
                    "mendengarkan stream tanpa menunggunya, pakai listen. Di Flutter,",
                    "widget StreamBuilder menggambar ulang layar setiap ada nilai baru.",
                ],
            },
            {
                "heading": "Isolate: kerja berat tanpa membekukan layar",
                "bahasa": "dart",
                "code": """import 'dart:isolate';

int jumlahPrima(int batas) {
  var n = 0;
  for (var i = 2; i <= batas; i++) {
    var prima = true;
    for (var j = 2; j * j <= i; j++) {
      if (i % j == 0) {
        prima = false;
        break;
      }
    }
    if (prima) n++;
  }
  return n;
}

Future<void> main() async {
  final hasil = await Isolate.run(() => jumlahPrima(2000000));
  print('ada $hasil bilangan prima');
}""",
            },
            {
                "body": [
                    "async nggak membuat kode jalan paralel. Kalau kamu menghitung bilangan",
                    "prima sampai dua juta di thread utama, event loop terhenti sampai",
                    "hitungannya selesai, dan aplikasi Flutter membeku.",
                    "",
                    "Isolate adalah pekerja terpisah dengan memori sendiri. Isolate nggak",
                    "berbagi variabel; mereka berkomunikasi dengan mengirim pesan.",
                    "Isolate.run menjalankan satu fungsi di isolate baru lalu",
                    "mengembalikan hasilnya sebagai Future. Program di atas mencetak ada",
                    "148933 bilangan prima. Di Flutter ada pembungkus serupa bernama",
                    "compute.",
                    "",
                    "Kapan perlu isolate? Kalau satu pekerjaan makan waktu lebih dari",
                    "beberapa milidetik: mengurai JSON berukuran megabyte, mengolah",
                    "gambar, atau menghitung sesuatu yang berat. Menunggu jaringan nggak",
                    "perlu isolate, karena selama menunggu, event loop tetap bebas.",
                ],
            },
            {
                "heading": "Sekilas widget Flutter",
                "bahasa": "dart",
                "code": """import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: Beranda()));

class Beranda extends StatelessWidget {
  const Beranda({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Toko Kopi')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text('Stok kopi: 3'),
            ElevatedButton(onPressed: () {}, child: const Text('Pesan')),
          ],
        ),
      ),
    );
  }
}""",
            },
            {
                "body": [
                    "Di Flutter, seluruh tampilan adalah pohon widget. Setiap widget",
                    "adalah objek Dart, dan pohonnya dibangun dari parameter bernama",
                    "seperti appBar, body, child, dan children. Karena itu materi",
                    "sebelumnya menekankan parameter bernama. Cara kerja Flutter, state,",
                    "dan navigasi dibahas di kurikulum mobile.",
                ],
            },
            {
                "heading": "Memasang Dart SDK",
                "bahasa": "terminal",
                "code": """# unduh dartsdk-linux-x64-release.zip dari https://dart.dev/get-dart/archive
unzip dartsdk-linux-x64-release.zip -d ~/sdk
echo 'export PATH="$HOME/sdk/dart-sdk/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
dart --version""",
            },
            {
                "body": [
                    "Dart nggak ada di repositori Fedora. Unduh berkas zip dari halaman",
                    "arsip resmi, ekstrak, lalu tambahkan folder bin ke PATH. Kalau kamu",
                    "memasang Flutter, Dart sudah ikut di dalamnya, jadi nggak perlu",
                    "dipasang terpisah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pengguna aplikasi Flutter paling cepat sadar kalau animasi patah-patah",
                    "atau layar membeku sesaat. Penyebab yang sering ditemukan adalah",
                    "pekerjaan berat yang dikerjakan di isolate utama, misalnya mengurai",
                    "berkas JSON besar saat aplikasi dibuka.",
                    "",
                    "Kasus kecil: aplikasi daftar produk membeku sekitar dua detik setiap kali",
                    "memuat daftar 50.000 produk dari berkas JSON.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka Flutter DevTools, tab Performance, dan cari frame yang",
                    "     merah saat daftar dimuat.",
                    "  2. Pastikan penyebabnya jsonDecode dan pembuatan objek Produk, bukan",
                    "     proses membaca berkas.",
                    "  3. Pindahkan penguraian ke isolate:",
                    "       final produk = await Isolate.run(() => uraiProduk(teks));",
                    "  4. Fungsi uraiProduk harus fungsi biasa yang cuma memakai",
                    "     parameternya, karena isolate nggak bisa membaca variabel milik",
                    "     isolate utama.",
                    "  5. Ukur ulang di DevTools. Frame merah saat memuat seharusnya",
                    "     hilang, dan indikator memuat tetap berputar mulus.",
                ],
            },
        ],
    },
    {
        "title": "17. R: Vektor, Data Frame, dan Statistik Dasar",
        "sections": [
            {
                "body": [
                    "R adalah bahasa yang dibuat khusus untuk statistik dan analisis data. Kamu",
                    "bakal ketemu R di kampus (skripsi, penelitian), di laboratorium biologi",
                    "dan kesehatan, dan di tim analis data yang bikin laporan rutin. Versi",
                    "stabil terbaru saat materi ini ditulis (Oktober 2026) adalah 4.6.1,",
                    "dirilis Juni 2026. R gratis dan berlisensi GPL.",
                    "",
                    "Popularitasnya agak unik. Di Survei Stack Overflow 2026 cuma 4,5%",
                    "responden yang memakai R, tapi di TIOBE Index Oktober 2026 R ada di",
                    "peringkat 8. Artinya R jarang dipakai programmer aplikasi, tapi banyak",
                    "dicari dan dibicarakan orang yang kerjanya mengolah data.",
                    "",
                    "Materi ini memakai urutan pertanyaan yang sama dengan bab pertama: halo",
                    "dunia, tipe, koleksi, fungsi, lalu hal-hal khas R. Pertanyaan terpenting",
                    "untuk R ada di nomor dua dan tiga, karena di R hampir semua nilai adalah",
                    "koleksi.",
                ],
            },
            {
                "heading": "Halo Dunia dan cara menjalankannya",
                "bahasa": "r",
                "code": "cat(\"Halo, Dunia!\\n\")\nprint(\"Halo, Dunia!\")",
            },
            {
                "body": [
                    "Simpan dua baris itu di halo.R, lalu jalankan dengan Rscript halo.R",
                    "(pasang dulu lewat sudo dnf install R di Fedora). Hasilnya:",
                    "",
                    "  Halo, Dunia!",
                    "  [1] \"Halo, Dunia!\"",
                    "",
                    "Baris kedua punya [1] di depannya. Itu nomor indeks elemen pertama yang",
                    "dicetak di baris itu. print() selalu memperlakukan nilainya sebagai",
                    "vektor, bahkan kalau isinya cuma satu teks. Untuk keluaran yang bersih",
                    "tanpa tanda kutip dan tanpa [1], pakai cat().",
                ],
            },
            {
                "heading": "Semua angka adalah vektor",
                "bahasa": "r",
                "code": """nilai <- c(85, 70, 92)     # c() = combine, bikin vektor
nilai + 5                  # [1] 90 75 97
nilai[1]                   # [1] 85   (indeks mulai dari 1)
nilai[-1]                  # [1] 70 92 (buang elemen pertama)
nilai[nilai > 80]          # [1] 85 92
mean(nilai)                # [1] 82.33333
median(nilai)              # [1] 85
sd(nilai)                  # [1] 11.23981
length(nilai)              # [1] 3""",
            },
            {
                "body": [
                    "Di Python, angka 5 dan daftar [5] itu dua hal berbeda. Di R nggak ada",
                    "beda: angka 5 adalah vektor yang panjangnya satu. Makanya nilai + 5",
                    "langsung menambah 5 ke setiap elemen tanpa perulangan. Cara berpikir ini",
                    "namanya vektorisasi, dan kode R yang bagus hampir nggak pernah memakai for",
                    "untuk hal sesederhana ini.",
                    "",
                    "Ada tiga hal yang bikin orang Python tersandung:",
                    "",
                    "  - Tanda <- dibaca \"diisi dengan\". Tanda = juga jalan untuk",
                    "    mengisi variabel, tapi panduan gaya komunitas R memakai <-.",
                    "  - Indeks mulai dari 1. nilai[0] nggak error, hasilnya vektor",
                    "    kosong numeric(0), jadi salahnya nggak langsung kelihatan.",
                    "  - Indeks negatif artinya buang. nilai[-1] di R membuang elemen",
                    "    pertama, sedangkan di Python justru mengambil elemen terakhir.",
                    "",
                    "Daur ulang (recycling) adalah aturan R saat dua vektor yang panjangnya",
                    "beda dijumlahkan. Vektor yang pendek diulang sampai sepanjang vektor yang",
                    "panjang:",
                    "",
                    "  c(1, 2, 3, 4) + c(10, 20)    hasilnya  11 22 13 24",
                    "  c(1, 2, 3) + c(10, 20)       hasilnya  11 22 13, plus peringatan",
                    "",
                    "Kasus kedua tetap dihitung, tapi R memberi peringatan \"longer object",
                    "length is not a multiple of shorter object length\", karena 3 nggak habis",
                    "dibagi 2. Peringatan bukan error. Skrip tetap jalan terus, jadi biasakan",
                    "membaca peringatan di akhir keluaran.",
                ],
            },
            {
                "heading": "Data frame dan factor",
                "bahasa": "r",
                "code": """siswa <- data.frame(
  nama  = c("Ani", "Budi", "Citra"),
  nilai = c(85, 70, 92),
  kelas = factor(c("A", "B", "A"))
)
print(siswa)
siswa[siswa$nilai > 80, ]      # baris yang nilainya > 80
mean(siswa$nilai)              # [1] 82.33333
levels(siswa$kelas)            # [1] "A" "B"
tapply(siswa$nilai, siswa$kelas, mean)   # rata-rata per kelas""",
            },
            {
                "body": [
                    "Data frame adalah tabel: setiap kolom sebuah vektor, dan semua kolom",
                    "panjangnya sama. Perintah print(siswa) mencetak:",
                    "",
                    "     nama nilai kelas",
                    "  1   Ani    85     A",
                    "  2  Budi    70     B",
                    "  3 Citra    92     A",
                    "",
                    "Tanda $ mengambil satu kolom sebagai vektor. Tanda kurung siku punya dua",
                    "slot, [baris, kolom]. Slot yang dikosongkan berarti \"semua\", jadi",
                    "siswa[siswa$nilai > 80, ] artinya baris yang nilainya di atas 80, dengan",
                    "semua kolom.",
                    "",
                    "Kolom kelas dibuat sebagai factor, yaitu tipe untuk data kategori seperti",
                    "kelas, jenis kelamin, atau kota. Factor menyimpan daftar kategori yang",
                    "mungkin (levels) dan memberi nomor ke tiap kategori. Fungsi statistik dan",
                    "grafik di R memakai informasi ini untuk mengelompokkan data.",
                    "",
                    "Jebakan: factor yang isinya angka menyimpan nomor kategorinya, bukan",
                    "angkanya. as.numeric(factor(c(\"10\", \"20\", \"10\"))) menghasilkan 1 2 1.",
                    "Untuk dapat 10 20 10, ubah ke teks dulu: as.numeric(as.character(x)). Ini",
                    "kejadian klasik waktu CSV dibaca dan sebuah kolom angka ternyata berisi",
                    "satu sel teks.",
                ],
            },
            {
                "heading": "Padanannya di Python, untuk perbandingan",
                "code": """nilai = [85, 70, 92]
print([n + 5 for n in nilai])
print(round(sum(nilai) / len(nilai), 5))
print([n for n in nilai if n > 80])
print(nilai[1:])""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  [90, 75, 97]",
                    "  82.33333",
                    "  [85, 92]",
                    "  [70, 92]",
                    "",
                    "Di Python semuanya butuh list comprehension, sedangkan di R operasinya",
                    "langsung kena seluruh vektor. Perhatikan juga baris terakhir: untuk",
                    "membuang elemen pertama, Python menulis nilai[1:], R menulis nilai[-1].",
                    "",
                    "Kapan pilih R, kapan Python? R unggul untuk statistik klasik (uji t,",
                    "regresi, ANOVA), grafik siap terbit, dan paket khusus riset seperti",
                    "Bioconductor untuk data genetika. Python unggul kalau analisisnya nanti",
                    "harus jadi bagian aplikasi, web, atau model machine learning. Banyak",
                    "analis memakai keduanya. Paket R didapat dari CRAN (Comprehensive R",
                    "Archive Network) lewat install.packages(\"nama\").",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "R banyak dipakai untuk laporan yang diulang tiap periode: rekap survei",
                    "kepuasan pelanggan, analisis hasil uji coba di laboratorium, atau",
                    "statistik nilai sekolah. Satu skrip R membaca CSV terbaru lalu",
                    "menghasilkan angka dan grafik yang sama formatnya setiap bulan.",
                    "",
                    "Kasus kecil: wali kelas mengirim nilai.csv berisi kolom nama, kelas, dan",
                    "nilai. Ia minta rata-rata tiap kelas dan daftar siswa yang nilainya di",
                    "bawah KKM 75.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Baca berkasnya jadi data frame, lalu cek tipe tiap kolom.",
                    "       d <- read.csv(\"nilai.csv\")",
                    "       str(d)",
                    "  2. Pastikan kolom nilai bertipe numeric. Kalau str() bilang chr",
                    "     atau Factor, ada sel yang bukan angka; cari dan betulkan dulu.",
                    "  3. Hitung rata-rata per kelas dengan tapply.",
                    "       tapply(d$nilai, d$kelas, mean)",
                    "  4. Saring siswa di bawah KKM dengan indeks logika.",
                    "       d[d$nilai < 75, c(\"nama\", \"kelas\", \"nilai\")]",
                    "  5. Jalankan dengan Rscript dan simpan skripnya, supaya bulan depan",
                    "     cukup ganti berkas CSV-nya.",
                ],
            },
        ],
    },
    {
        "title": "18. R Lanjut: Pipe, Tidyverse, dan ggplot2",
        "sections": [
            {
                "body": [
                    "Begitu analisis R makin panjang, kodenya cenderung jadi fungsi di dalam",
                    "fungsi di dalam fungsi. Kamu harus membacanya dari dalam ke luar, padahal",
                    "urutan kerjanya dari kiri ke kanan: ambil data, saring, hitung,",
                    "kelompokkan, ringkas.",
                    "",
                    "Tidyverse adalah kumpulan paket R yang dirancang supaya alur itu bisa",
                    "ditulis berurutan. Isinya antara lain dplyr (olah tabel), ggplot2",
                    "(grafik), tidyr (merapikan bentuk tabel), readr (baca CSV), stringr",
                    "(teks), dan purrr (fungsi untuk daftar). Semuanya dipasang sekaligus dari",
                    "CRAN dengan install.packages(\"tidyverse\"), lalu dimuat dengan",
                    "library(tidyverse).",
                ],
            },
            {
                "heading": "Dari bertingkat ke pipe",
                "bahasa": "r",
                "code": """# bertingkat: dibaca dari dalam ke luar
round(mean(sqrt(c(4, 9, 16))), 1)

# pipe bawaan R (sejak R 4.1): dibaca dari kiri ke kanan
c(4, 9, 16) |> sqrt() |> mean() |> round(1)

# pipe magrittr, banyak di kode lama dan contoh tidyverse
library(magrittr)
c(4, 9, 16) %>% sqrt() %>% mean() %>% round(1)""",
            },
            {
                "body": [
                    "Ketiga baris menghasilkan [1] 3, karena akar dari 4, 9, dan 16 adalah 2,",
                    "3, dan 4, dan rata-ratanya 3. Pipe artinya \"hasil sebelah kiri jadi",
                    "argumen pertama fungsi sebelah kanan\". Jadi x |> f(y) sama dengan f(x, y).",
                    "",
                    "Ada dua pipe, dan kamu bakal ketemu keduanya:",
                    "",
                    "  - |> adalah pipe bawaan, ada sejak R 4.1 (2021). Nggak perlu paket",
                    "    apa pun. Sisi kanannya wajib berupa pemanggilan fungsi lengkap",
                    "    dengan kurung, jadi x |> sqrt ditolak, sedangkan x |> sqrt()",
                    "    diterima.",
                    "  - %>% berasal dari paket magrittr dan ikut dimuat oleh dplyr. Ia",
                    "    lebih longgar dan punya tanda titik untuk menaruh hasil di",
                    "    posisi lain, misalnya data %>% lm(y ~ x, data = .).",
                    "",
                    "Untuk kode baru, panduan tidyverse sendiri sekarang memakai |>. Kode dan",
                    "jawaban forum sebelum 2021 hampir semuanya memakai %>%.",
                ],
            },
            {
                "heading": "Lima kata kerja dplyr",
                "bahasa": "r",
                "code": """library(dplyr)

nilai <- read.csv("nilai.csv")

nilai |>
  filter(hadir >= 10) |>
  mutate(akhir = 0.4 * tugas + 0.6 * ujian) |>
  group_by(kelas) |>
  summarise(rata = mean(akhir), n = n()) |>
  arrange(desc(rata))""",
            },
            {
                "body": [
                    "Bacanya seperti resep. Ambil tabel nilai, lalu saring siswa yang hadir",
                    "minimal 10 kali (filter). Tambah kolom akhir (mutate), lalu kelompokkan",
                    "per kelas (group_by). Ringkas tiap kelompok jadi rata-rata dan jumlah",
                    "siswa (summarise), lalu urutkan dari rata-rata terbesar (arrange). Di",
                    "dalam fungsi dplyr, nama kolom ditulis polos tanpa tanda kutip dan tanpa",
                    "nilai$.",
                    "",
                    "Hasilnya berupa tibble, versi data frame yang lebih rapi saat dicetak.",
                    "Untuk data contoh di bawah, bentuknya kira-kira begini (tibble menyingkat",
                    "angka jadi tiga digit penting):",
                    "",
                    "  # A tibble: 2 x 3",
                    "    kelas  rata     n",
                    "    <chr> <dbl> <int>",
                    "  1 B      82       1",
                    "  2 A      79.7     3",
                    "",
                    "Kalau kamu sudah pernah menulis SQL, polanya terasa akrab: filter mirip",
                    "WHERE, group_by dan summarise mirip GROUP BY dengan AVG dan COUNT, arrange",
                    "mirip ORDER BY.",
                ],
            },
            {
                "heading": "Resep yang sama di Python tanpa paket",
                "code": "import csv\nimport io\nfrom statistics import mean\n\ndata = \"\"\"nama,kelas,tugas,ujian,hadir\nAni,A,80,90,14\nBudi,B,70,60,9\nCitra,A,90,85,13\nDodi,B,85,80,12\nEka,A,60,70,11\n\"\"\"\nbaris = list(csv.DictReader(io.StringIO(data)))\nhadir = [b for b in baris if int(b[\"hadir\"]) >= 10]   # filter\nfor b in hadir:                                        # mutate\n    b[\"akhir\"] = 0.4 * int(b[\"tugas\"]) + 0.6 * int(b[\"ujian\"])\nkelompok = {}\nfor b in hadir:                                        # group_by\n    kelompok.setdefault(b[\"kelas\"], []).append(b[\"akhir\"])\nringkas = [(k, mean(v), len(v)) for k, v in kelompok.items()]\nfor kelas, rata, n in sorted(ringkas, key=lambda r: -r[1]):\n    print(f\"{kelas} {rata:.2f} {n}\")",
            },
            {
                "body": [
                    "Keluaran:",
                    "  B 82.00 1",
                    "  A 79.67 3",
                    "",
                    "Logikanya sama persis, tapi di Python tiap langkah butuh perulangan atau",
                    "dict sendiri. Pustaka pandas atau Polars di Python menyediakan gaya yang",
                    "mirip dplyr, dan keduanya paket pihak ketiga.",
                ],
            },
            {
                "heading": "ggplot2: grafik dari lapisan",
                "bahasa": "r",
                "code": """library(ggplot2)

ggplot(nilai, aes(x = tugas, y = ujian, colour = kelas)) +
  geom_point(size = 3) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Nilai tugas vs ujian", x = "Tugas", y = "Ujian")

ggsave("sebaran.png", width = 6, height = 4)""",
            },
            {
                "body": [
                    "ggplot2 memakai ide grammar of graphics: grafik disusun dari lapisan.",
                    "ggplot() menentukan data dan aes (aesthetic), yaitu kolom mana yang jadi",
                    "sumbu x, sumbu y, dan warna. Setiap geom_ menambah satu lapisan gambar:",
                    "titik, garis regresi, batang, dan seterusnya. labs() mengatur judul, dan",
                    "ggsave() menyimpan berkas gambar.",
                    "",
                    "Jebakan: lapisan ggplot disambung dengan +, bukan dengan pipe. Kalau kamu",
                    "terbiasa menulis |> di semua tempat lalu menulis geom_point() |>",
                    "labs(...), R memberi error yang membingungkan. Aturan gampangnya: |> untuk",
                    "mengolah data, + untuk menumpuk lapisan grafik.",
                ],
            },
            {
                "heading": "Alat di sekitar R",
                "body": [
                    "Beberapa nama yang sering muncul di lowongan dan tutorial:",
                    "",
                    "  - RStudio dan Positron adalah editor buatan Posit untuk R. RStudio",
                    "    sudah lama jadi pilihan utama; Positron editor yang lebih baru,",
                    "    dibangun di atas dasar VS Code dan juga melayani Python.",
                    "  - R Markdown dan penerusnya, Quarto, menggabungkan teks, kode, dan",
                    "    hasilnya dalam satu dokumen. Saat dokumen dirender, kodenya",
                    "    dijalankan dan tabel serta grafiknya ikut masuk ke laporan HTML,",
                    "    PDF, atau Word.",
                    "  - Shiny membuat aplikasi web interaktif cuma dengan R, misalnya",
                    "    dashboard dengan slider dan menu pilihan.",
                    "  - CRAN menyimpan puluhan ribu paket yang sudah lolos pemeriksaan;",
                    "    Bioconductor menyimpan paket khusus bioinformatika.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola pipe dan dplyr dipakai untuk membersihkan data sebelum dianalisis:",
                    "membuang baris kosong, menyeragamkan nama kategori, menghitung kolom",
                    "turunan, lalu meringkas per kelompok. Hasilnya sering langsung masuk ke",
                    "dokumen Quarto yang dikirim ke atasan atau dosen, lengkap dengan grafik",
                    "ggplot2.",
                    "",
                    "Kasus kecil: kamu menerima penjualan.csv berisi kolom tanggal, cabang,",
                    "produk, dan jumlah. Atasan minta total penjualan per cabang khusus bulan",
                    "September, diurutkan dari yang terbesar, ditambah grafik batangnya.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Muat dplyr dan ggplot2, lalu baca CSV dengan read.csv.",
                    "  2. Ubah kolom tanggal jadi tipe tanggal, lalu saring bulannya.",
                    "       d |> mutate(tanggal = as.Date(tanggal)) |>",
                    "         filter(format(tanggal, \"%m\") == \"09\")",
                    "  3. Kelompokkan per cabang dan jumlahkan.",
                    "       ... |> group_by(cabang) |>",
                    "         summarise(total = sum(jumlah)) |> arrange(desc(total))",
                    "  4. Simpan hasilnya ke variabel ringkas, lalu gambar:",
                    "       ggplot(ringkas, aes(x = cabang, y = total)) + geom_col()",
                    "  5. Taruh semua langkah di satu berkas Quarto, supaya bulan depan",
                    "     cukup mengganti angka bulannya lalu merender ulang.",
                ],
            },
        ],
    },
    {
        "title": "19. MATLAB dan GNU Octave: Berpikir dalam Matriks",
        "sections": [
            {
                "body": [
                    "MATLAB (singkatan dari matrix laboratory) adalah bahasa sekaligus",
                    "lingkungan kerja untuk hitungan numerik. Pemiliknya perusahaan MathWorks,",
                    "dan lisensinya berbayar. Kampus teknik biasanya punya lisensi untuk",
                    "mahasiswanya, jadi anak teknik elektro, mesin, atau fisika hampir pasti",
                    "ketemu MATLAB. Rilisnya dua kali setahun dengan nama tahun plus a atau b;",
                    "rilis terbaru saat materi ini ditulis (Oktober 2026) adalah R2026b.",
                    "",
                    "GNU Octave adalah pengganti bebasnya. Octave berlisensi GPL, ada di",
                    "repositori Fedora, dan sintaksnya sengaja dibuat hampir sama dengan",
                    "MATLAB, jadi sebagian besar kode MATLAB sederhana bisa langsung jalan.",
                    "Fedora 44 membawa Octave 10.3; rilis upstream terbarunya 11.3.0 (Juni",
                    "2026). Semua contoh di materi ini sudah dijalankan di Octave.",
                ],
            },
            {
                "heading": "Memasang Octave dan menjalankan berkas .m",
                "bahasa": "terminal",
                "code": """sudo dnf install octave
octave-cli halo.m          # jalankan satu berkas tanpa jendela
octave                     # buka REPL / GUI""",
            },
            {
                "heading": "Dua cara mengalikan matriks",
                "bahasa": "matlab",
                "code": """A = [1 2; 3 4];     % titik koma di dalam [] = ganti baris
B = [5 6; 7 8];     % titik koma di akhir = jangan cetak
A * B               % perkalian matriks
A .* B              % perkalian per elemen""",
            },
            {
                "body": [
                    "Octave mencetak:",
                    "",
                    "  ans =",
                    "",
                    "     19   22",
                    "     43   50",
                    "",
                    "  ans =",
                    "",
                    "      5   12",
                    "     21   32",
                    "",
                    "Bedanya cuma satu titik, dan di situlah cara berpikir MATLAB. Tanda *",
                    "berarti perkalian matriks seperti di pelajaran aljabar linear: baris kali",
                    "kolom lalu dijumlahkan, jadi 1*5 + 2*7 = 19. Tanda .* (pakai titik)",
                    "berarti kalikan elemen yang posisinya sama, jadi 1*5 = 5 dan 2*6 = 12. Hal",
                    "yang sama berlaku untuk ./ dan .^.",
                    "",
                    "Jebakan: kalau kamu mau mengkuadratkan setiap elemen vektor v, tulis v",
                    ".^ 2. Menulis v ^ 2 artinya v dikali v secara matriks. Untuk vektor",
                    "baris, itu error karena ukurannya nggak cocok; untuk matriks persegi,",
                    "hasilnya angka yang salah tanpa error sama sekali.",
                ],
            },
            {
                "heading": "Vektorisasi dan indeks",
                "bahasa": "matlab",
                "code": """v = [10 20 30 40];
v(1)                % 10, indeks mulai dari 1, pakai kurung biasa
v(end)              % 40, end = elemen terakhir
v .^ 2              % 100 400 900 1600
mean(v)             % 25

suhu = [31 33 29 35 30];
panas = suhu > 31   % 0 1 0 1 0
sum(panas)          % 2 hari yang panas

total = 0;          % versi perulangan...
for i = 1:5
  total = total + i^2;
end
disp(total)         % 55
disp(sum((1:5).^2)) % ...dan versi vektor: 55""",
            },
            {
                "body": [
                    "Sama seperti R, MATLAB lebih suka operasi yang langsung mengenai seluruh",
                    "vektor. Perbandingan suhu > 31 menghasilkan vektor 0 dan 1, dan sum()",
                    "menghitung berapa yang bernilai 1. Ekspresi 1:5 membuat vektor 1 2 3 4 5.",
                    "Versi perulangan dan versi vektor sama-sama memberi 55, tapi versi vektor",
                    "lebih pendek dan di MATLAB biasanya lebih cepat.",
                    "",
                    "Beberapa kebiasaan MATLAB yang sering bikin bingung saat membaca kodenya:",
                    "",
                    "  - Indeks memakai kurung biasa, v(1), sama seperti memanggil fungsi.",
                    "    Jadi f(2) bisa berarti fungsi f atau elemen kedua vektor f.",
                    "  - Baris tanpa titik koma di akhir langsung dicetak. Kalau keluaran",
                    "    skripmu banjir angka, cari baris yang lupa titik koma.",
                    "  - Komentar diawali %. Blok diakhiri end.",
                    "  - A' adalah transpose, dan A \\ b menyelesaikan sistem persamaan",
                    "    linear A*x = b tanpa menghitung invers.",
                ],
            },
            {
                "heading": "Skrip dan berkas fungsi",
                "bahasa": "matlab",
                "code": "% berkas rata_berbobot.m (nama berkas = nama fungsi)\nfunction hasil = rata_berbobot(nilai, bobot)\n  hasil = sum(nilai .* bobot) / sum(bobot);\nend\n\n% berkas utama.m, skrip biasa di folder yang sama\nnilai = [80 90 70];\nbobot = [0.3 0.5 0.2];\nfprintf('%.1f\\n', rata_berbobot(nilai, bobot))   % 83.0",
            },
            {
                "body": [
                    "MATLAB membedakan skrip dan fungsi. Skrip adalah berkas .m berisi perintah",
                    "yang dijalankan dari atas ke bawah. Fungsi ditulis di berkasnya sendiri,",
                    "dan nama berkasnya wajib sama dengan nama fungsinya. MATLAB mencari fungsi",
                    "lewat nama berkas di folder kerja dan di path-nya, jadi rata_berbobot.m",
                    "yang diganti nama jadi hitung.m bikin pemanggilan rata_berbobot() gagal.",
                    "",
                    "Fungsi fprintf mencetak dengan format seperti printf di C. Octave juga",
                    "mengenal printf, tapi itu khusus Octave; pakai fprintf supaya kodemu jalan",
                    "di keduanya.",
                ],
            },
            {
                "heading": "Padanannya di Python murni",
                "code": """A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
matriks = [[sum(A[i][k] * B[k][j] for k in range(2))
            for j in range(2)] for i in range(2)]
per_elemen = [[A[i][j] * B[i][j] for j in range(2)]
              for i in range(2)]
print(matriks)
print(per_elemen)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  [[19, 22], [43, 50]]",
                    "  [[5, 12], [21, 32]]",
                    "",
                    "Tanpa pustaka, Python harus menulis perulangan bersarang. Di dunia nyata",
                    "orang Python memakai NumPy, yang meniru banyak ide MATLAB: A @ B untuk",
                    "perkalian matriks dan A * B untuk per elemen. Perhatikan bahwa artinya",
                    "terbalik dari MATLAB. Di MATLAB tanda * adalah perkalian matriks, di NumPy",
                    "tanda * adalah per elemen.",
                    "",
                    "Octave juga punya beberapa tambahan yang nggak ada di MATLAB, seperti",
                    "komentar #, operator !=, dan printf. Kode yang memakainya jalan di Octave",
                    "tapi gagal di MATLAB. Kebalikannya, toolbox berbayar MATLAB dan Simulink",
                    "(alat simulasi berbasis blok diagram untuk sistem kendali, otomotif, dan",
                    "dirgantara) nggak punya padanan lengkap di Octave. Untuk belajar dasar",
                    "MATLAB secara resmi, MathWorks punya kursus gratis berbasis browser",
                    "bernama MATLAB Onramp.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "MATLAB dipakai di tugas besar dan laboratorium teknik: mengolah sinyal",
                    "dari sensor, merancang pengendali motor, atau menghitung data hasil",
                    "percobaan. Simulink dipakai industri otomotif dan dirgantara untuk",
                    "mensimulasikan sistem sebelum dipasang di perangkat sungguhan. Banyak kode",
                    "MATLAB peninggalan kakak tingkat atau dosen juga beredar dalam bentuk",
                    "berkas .m.",
                    "",
                    "Kasus kecil: temanmu dari teknik elektro mengirim filter.m yang",
                    "menghaluskan data sensor, tapi laptopmu nggak punya lisensi MATLAB.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pasang Octave dan jalankan berkasnya apa adanya.",
                    "       octave-cli filter.m",
                    "  2. Kalau muncul error fungsi nggak dikenal, cek apakah fungsi itu",
                    "     berasal dari toolbox MATLAB. Banyak fungsi toolbox punya padanan",
                    "     di paket Octave Forge, misalnya paket signal.",
                    "       pkg load signal",
                    "  3. Kalau error-nya soal ukuran matriks, cari operator * atau ^",
                    "     yang seharusnya .* atau .^.",
                    "  4. Pastikan setiap fungsi tambahan ada di berkas .m yang namanya",
                    "     sama dengan nama fungsinya, di folder yang sama.",
                    "  5. Bandingkan beberapa angka hasil dengan yang didapat temanmu di",
                    "     MATLAB sebelum kamu memakai hasilnya.",
                ],
            },
        ],
    },
    {
        "title": "20. Peta Bahasa Sains dan Bahasa Array",
        "sections": [
            {
                "body": [
                    "Selain R dan MATLAB, ada enam bahasa lain yang mungkin kamu temui di dunia",
                    "sains, teknik, dan keuangan: Julia, Fortran, SAS, Wolfram Language, APL,",
                    "dan q. Materi ini nggak mengajarkan semuanya sampai bisa. Tujuannya supaya",
                    "kamu mengenali kodenya, tahu bidangnya, dan tahu cara mencobanya gratis.",
                    "",
                    "Dua di antaranya, APL dan q, termasuk keluarga bahasa array. MATLAB dan R",
                    "meminjam sebagian idenya. Di bahasa array, operasi dasarnya bekerja pada",
                    "seluruh array sekaligus, jadi program yang di Python butuh perulangan bisa",
                    "ditulis dalam beberapa karakter.",
                ],
            },
            {
                "heading": "Julia: secepat C, semudah Python",
                "bahasa": "julia",
                "code": """println("Halo, Dunia!")

# multiple dispatch: fungsi dipilih dari tipe SEMUA argumennya
luas(r::Float64) = pi * r^2
luas(p::Int, l::Int) = p * l

println(luas(2.0))       # 12.566370614359172
println(luas(3, 4))      # 12
v = [1, 2, 3]
println(v .+ 10)         # [11, 12, 13], titik = per elemen""",
            },
            {
                "body": [
                    "Julia lahir tahun 2012 dari keluhan ilmuwan yang menulis prototipe di",
                    "Python atau MATLAB lalu menulis ulang bagian lambatnya di C. Julia",
                    "dikompilasi JIT (just-in-time) ke kode mesin saat fungsi pertama kali",
                    "dipanggil, jadi perulangan biasa pun bisa cepat. Ciri khasnya multiple",
                    "dispatch: satu nama fungsi bisa punya banyak versi, dan Julia memilih",
                    "versinya berdasarkan tipe semua argumen.",
                    "",
                    "Versi stabil saat materi ini ditulis (Oktober 2026) adalah 1.13.2, dengan",
                    "1.10 sebagai jalur dukungan panjang (LTS). Lisensinya MIT. Indeksnya mulai",
                    "dari 1. Pemanggilan pertama sering terasa lambat karena harus dikompilasi",
                    "dulu; orang Julia menyebutnya \"time to first plot\". Dipakai di pemodelan",
                    "iklim, farmasi, dan optimasi (paket JuMP). Pasang lewat juliaup dari",
                    "julialang.org, atau sudo dnf install julia di Fedora (versinya lebih",
                    "lama).",
                ],
            },
            {
                "heading": "Fortran: tertua yang masih bekerja",
                "bahasa": "fortran",
                "code": """program rata
  implicit none
  real :: nilai(3) = [85.0, 70.0, 92.0]
  print *, "Halo, Dunia!"
  print *, "Rata-rata:", sum(nilai) / size(nilai)
end program rata""",
            },
            {
                "body": [
                    "Fortran (formula translation) muncul tahun 1957 dan masih hidup.",
                    "Standarnya terus diperbarui, yang terbaru Fortran 2023, dan kompilator",
                    "gratisnya gfortran ikut GCC (sudo dnf install gcc-gfortran). Di TIOBE",
                    "Oktober 2026 Fortran ada di peringkat 13.",
                    "",
                    "Alasannya sederhana: kode hitungan angka yang sudah teruji puluhan tahun",
                    "nggak ada yang mau menulis ulang. Model cuaca seperti WRF ditulis dengan",
                    "Fortran, dan pustaka aljabar linear LAPACK yang dipakai SciPy aslinya",
                    "ditulis Fortran. Fortran modern (berkas .f90) punya operasi array bawaan",
                    "seperti sum() dan size(). Kode lama (.f, .for) memakai format kolom tetap",
                    "yang jauh lebih susah dibaca. Biasakan implicit none, supaya variabel yang",
                    "lupa dideklarasikan jadi error, bukan otomatis bertipe menurut huruf",
                    "awalnya.",
                ],
            },
            {
                "heading": "SAS: statistik di farmasi dan bank",
                "bahasa": "sas",
                "code": """data siswa;
  input nama $ nilai;
  datalines;
Ani 85
Budi 70
Citra 92
;
run;

proc means data=siswa mean;
  var nilai;
run;""",
            },
            {
                "body": [
                    "SAS adalah bahasa analitik komersial yang lama menguasai farmasi,",
                    "perbankan, dan lembaga statistik pemerintah. Programnya terdiri dari",
                    "langkah data (membaca dan mengolah data) dan langkah proc (prosedur",
                    "analisis siap pakai seperti proc means dan proc reg). Setiap pernyataan",
                    "diakhiri titik koma.",
                    "",
                    "Versi klasiknya SAS 9.4M9 (Juni 2025), sedangkan platform barunya, SAS",
                    "Viya, berjalan di cloud dengan rilis bulanan. SAS nggak bisa dipasang",
                    "gratis di laptop. Untuk belajar ada SAS OnDemand for Academics, gratis",
                    "lewat browser. Di pasar umum SAS menurun karena tergeser R dan Python,",
                    "tapi masih kuat di analisis uji klinis obat dan pemodelan risiko kredit.",
                ],
            },
            {
                "heading": "Wolfram Language: matematika simbolik",
                "bahasa": "wolfram",
                "code": """Print["Halo, Dunia!"]
Integrate[x^2, x]          (* x^3/3 *)
Solve[x^2 - 5 x + 6 == 0, x]   (* {{x -> 2}, {x -> 3}} *)
Total[{85, 70, 92}]/3      (* 247/3, pecahan persis *)""",
            },
            {
                "body": [
                    "Wolfram Language adalah bahasa di balik Mathematica dan Wolfram|Alpha.",
                    "Bedanya dengan bahasa lain di sini: ia bisa menghitung secara simbolik.",
                    "Integral x^2 dijawab x^3/3, bukan angka, dan pembagian bilangan bulat yang",
                    "nggak habis dibiarkan jadi pecahan persis. Fungsi dipanggil pakai kurung",
                    "siku, dan nama fungsi bawaannya diawali huruf besar.",
                    "",
                    "Versi 15.0 rilis Juni 2026 dan 15.0.1 menyusul Juli 2026. Lisensinya",
                    "proprietary, tapi Wolfram Engine gratis untuk pengembang (bukan untuk",
                    "produksi) dan bisa dijalankan dengan wolframscript. Dipakai di riset",
                    "matematika, fisika, dan pendidikan.",
                ],
            },
            {
                "heading": "APL dan q: bahasa array",
                "bahasa": "apl",
                "code": """⎕←'Halo, Dunia!'
+/ 70 80 90          ⍝ 240: sisipkan + di antara elemen
⍳5                   ⍝ 1 2 3 4 5
rata←{(+/⍵)÷≢⍵}      ⍝ jumlah dibagi banyaknya
rata 70 80 90        ⍝ 80
2×3+4                ⍝ 14, dihitung dari kanan""",
            },
            {
                "heading": "Contoh q (kdb+)",
                "bahasa": "q",
                "code": """-1 "Halo, Dunia!";
til 5                / 0 1 2 3 4
sum 70 80 90         / 240
avg 70 80 90         / 80f
2*3+4                / 14, juga dari kanan
select avg harga by sym from transaksi""",
            },
            {
                "body": [
                    "APL (A Programming Language) berasal dari notasi matematika Kenneth",
                    "Iverson di awal 1960-an. Ia memakai simbol khusus seperti ⍳, ⍴, dan ⌿",
                    "sebagai pengganti nama fungsi, jadi kamu butuh papan ketik atau cara input",
                    "khusus. Implementasi yang paling banyak dipakai adalah Dyalog APL (versi",
                    "20.0, November 2025, proprietary dengan lisensi gratis untuk keperluan",
                    "tertentu); ada juga GNU APL yang bebas. Cara tercepat mencobanya adalah",
                    "TryAPL di browser.",
                    "",
                    "q adalah bahasa untuk database deret waktu kdb+. Bahasanya sama",
                    "ringkasnya, tapi memakai kata (til, sum, avg) alih-alih simbol, dan punya",
                    "query mirip SQL. Bank dan perusahaan trading memakainya untuk mengolah",
                    "data harga saham per detik. Versi terbarunya KDB-X 5.0 (Oktober 2026),",
                    "dengan edisi komunitas yang gratis untuk pemakaian pribadi dan komersial",
                    "dengan batas sumber daya.",
                    "",
                    "Jebakan: APL dan q menghitung dari kanan ke kiri tanpa urutan prioritas",
                    "operator. 2×3+4 dibaca 2×(3+4), hasilnya 14, padahal pelajaran matematika",
                    "SD mengajarkan 10.",
                ],
            },
            {
                "heading": "Memilih di antara mereka",
                "body": [
                    "Pilihannya hampir selalu ditentukan bidang, bukan selera:",
                    "",
                    "  - Mau masuk riset numerik atau pemodelan baru dan suka kode",
                    "    terbuka? Julia layak dicoba.",
                    "  - Bergabung dengan kelompok riset cuaca, fisika, atau",
                    "    superkomputer? Siap-siap membaca dan merawat Fortran.",
                    "  - Melamar ke bagian statistik perusahaan farmasi atau bank? SAS",
                    "    sering tercantum di lowongan.",
                    "  - Banyak hitungan simbolik (aljabar, kalkulus)? Wolfram Language.",
                    "  - Bekerja di bagian data pasar keuangan? q dan kdb+, kadang juga",
                    "    bahasa array lain di sistem aktuaria yang lebih tua.",
                    "",
                    "Kalau belum ada bidang yang memaksa, Python plus R sudah menutup sebagian",
                    "besar kebutuhan analisis data.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kode Fortran dan bahasa array sering bersembunyi di balik alat yang",
                    "terlihat modern. Pustaka Python untuk sains memanggil rutin aljabar linear",
                    "yang asalnya Fortran, dan sistem trading memakai q di balik dashboard",
                    "berbasis web. Jadi kemungkinan kamu membaca bahasa ini lebih besar",
                    "daripada kemungkinan kamu menulisnya dari nol.",
                    "",
                    "Kasus kecil: dosen pembimbing memberimu program hitung.f90 dan bilang",
                    "\"jalankan, lalu ubah jumlah titik datanya dari 100 jadi 1000\".",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pasang kompilatornya, lalu kompilasi dan jalankan dulu tanpa",
                    "     mengubah apa pun, supaya kamu tahu keluaran aslinya.",
                    "       sudo dnf install gcc-gfortran",
                    "       gfortran hitung.f90 -o hitung && ./hitung",
                    "  2. Cari angka 100 di kode. Biasanya ada di deklarasi seperti",
                    "     integer, parameter :: n = 100, atau di ukuran array.",
                    "  3. Ganti nilainya, kompilasi ulang, dan bandingkan keluaran lama",
                    "     dengan yang baru.",
                    "  4. Kalau kodenya berformat kolom tetap (.f), jangan geser posisi",
                    "     baris; kolom 1 sampai 6 punya arti khusus di format lama.",
                ],
            },
        ],
    },
    {
        "title": "21. Scala: Fungsional dan OOP di JVM",
        "sections": [
            {
                "body": [
                    "Java dikompilasi jadi bytecode yang dijalankan JVM (Java Virtual Machine).",
                    "Ternyata JVM nggak peduli bytecode itu asalnya dari bahasa apa. Kotlin,",
                    "Scala, Groovy, dan Clojure semuanya menghasilkan bytecode untuk mesin yang",
                    "sama, jadi semuanya bisa memakai pustaka Java yang sudah ada. Hal yang",
                    "sama berlaku di dunia .NET: C#, F#, dan VB.NET berbagi runtime CLR.",
                    "",
                    "Scala dibuat Martin Odersky di EPFL, Swiss, dan dirilis tahun 2004.",
                    "Namanya dari scalable language. Scala memadukan OOP seperti Java dengan",
                    "gaya fungsional: data yang nggak diubah, fungsi sebagai nilai, dan pattern",
                    "matching. Bahasa ini terkenal lewat Apache Spark, mesin pengolah big data",
                    "yang ditulis dengan Scala.",
                    "",
                    "Saat materi ini ditulis (Oktober 2026), rilis terbarunya Scala 3.10.0 di",
                    "jalur Next, dan jalur dukungan panjang (LTS) ada di 3.9.0. Scala 2 masih",
                    "dirawat di 2.13.18 karena banyak kode lama, termasuk Spark, masih",
                    "memakainya. Lisensinya Apache 2.0.",
                ],
            },
            {
                "heading": "Dasar: val, var, dan koleksi",
                "bahasa": "scala",
                "code": """@main def halo(): Unit =
  val nama = "Ani"          // val: nggak bisa diisi ulang
  var skor = 0              // var: boleh diubah
  skor += 10
  val nilai = List(85, 70, 92)
  println(s"Halo, $nama! Skor $skor")
  println(nilai.map(_ + 5))           // List(90, 75, 97)
  println(nilai.filter(_ > 80).sum)   // 177

  val umur = Map("Ani" -> 17, "Budi" -> 18)
  println(umur.get("Ani"))            // Some(17)
  println(umur.get("Citra"))          // None
  println(umur.getOrElse("Citra", 0)) // 0""",
            },
            {
                "body": [
                    "Beberapa hal langsung terlihat beda dari Java:",
                    "",
                    "  - Tipe nggak perlu ditulis kalau bisa ditebak. val nama = \"Ani\"",
                    "    sudah cukup; Scala tahu itu String. Ini namanya inferensi tipe.",
                    "  - val dipakai untuk hampir semua variabel. var cuma kalau memang",
                    "    harus berubah. Kebiasaan ini mengurangi bug karena nilai yang",
                    "    diubah dari tempat lain.",
                    "  - List bawaan bersifat immutable. nilai.map(_ + 5) membuat list",
                    "    baru dan nilai tetap List(85, 70, 92). Tanda _ adalah singkatan",
                    "    parameter, jadi _ + 5 sama dengan x => x + 5.",
                    "  - Map.get mengembalikan Option: Some(nilai) kalau kuncinya ada,",
                    "    None kalau nggak ada. Scala jarang memakai null, dan Option",
                    "    memaksa kamu memikirkan kasus kosong.",
                    "  - Scala 3 boleh menulis blok dengan indentasi tanpa kurung kurawal,",
                    "    mirip Python. Scala 2 wajib memakai kurung kurawal.",
                    "",
                    "@main menandai fungsi yang jadi titik masuk program. Simpan di halo.scala",
                    "lalu jalankan dengan scala run halo.scala. Sejak Scala 3.5, perintah scala",
                    "adalah Scala CLI, alat yang sekaligus mengunduh kompilator dan pustaka",
                    "yang dibutuhkan.",
                ],
            },
            {
                "heading": "Case class, sealed trait, dan match",
                "bahasa": "scala",
                "code": """sealed trait Bentuk
case class Lingkaran(r: Double) extends Bentuk
case class Persegi(sisi: Double) extends Bentuk
case class Segitiga(a: Double, b: Double, c: Double) extends Bentuk

def luas(b: Bentuk): Double = b match
  case Lingkaran(r)      => math.Pi * r * r
  case Persegi(s)        => s * s
  case Segitiga(a, b, c) =>
    val s = (a + b + c) / 2
    math.sqrt(s * (s - a) * (s - b) * (s - c))

@main def jalan(): Unit =
  val daftar = List(Lingkaran(1), Persegi(2), Segitiga(3, 4, 5))
  for b <- daftar do
    println(f"$b%s -> ${luas(b)}%.2f")""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  Lingkaran(1.0) -> 3.14",
                    "  Persegi(2.0) -> 4.00",
                    "  Segitiga(3.0,4.0,5.0) -> 6.00",
                    "",
                    "Ini pola paling khas Scala untuk memodelkan data. trait mirip interface di",
                    "Java. sealed artinya semua turunannya wajib ada di berkas yang sama,",
                    "sehingga kompilator tahu daftar lengkapnya. Kalau kamu menambah case class",
                    "Trapesium lalu lupa menambah cabangnya di match, kompilator memberi",
                    "peringatan \"match may not be exhaustive\".",
                    "",
                    "case class adalah kelas data. Scala otomatis membuatkan konstruktor tanpa",
                    "new, equals yang membandingkan isi, toString yang rapi, copy untuk membuat",
                    "salinan dengan sebagian nilai diganti, dan kemampuan dibongkar di pattern",
                    "matching. Di cabang case Segitiga(a, b, c), ketiga isinya langsung diikat",
                    "ke variabel a, b, dan c.",
                ],
            },
            {
                "heading": "Pembanding: pola yang sama di Java 17",
                "bahasa": "java",
                "code": """public class Bentuk {
    sealed interface Bangun permits Lingkaran, Persegi {}
    record Lingkaran(double r) implements Bangun {}
    record Persegi(double sisi) implements Bangun {}

    static double luas(Bangun b) {
        if (b instanceof Lingkaran l) return Math.PI * l.r() * l.r();
        if (b instanceof Persegi p) return p.sisi() * p.sisi();
        throw new IllegalArgumentException("bentuk tak dikenal");
    }

    public static void main(String[] args) {
        Bangun[] daftar = { new Lingkaran(1), new Persegi(2) };
        for (Bangun b : daftar) {
            System.out.println(b + " -> " + Math.round(luas(b) * 100) / 100.0);
        }
    }
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Lingkaran[r=1.0] -> 3.14",
                    "  Persegi[sisi=2.0] -> 4.0",
                    "",
                    "Java mengejar Scala pelan-pelan. Record (Java 16) mirip case class, sealed",
                    "interface (Java 17) mirip sealed trait, dan switch dengan pola record baru",
                    "final di Java 21. Banyak ide yang dulu jadi alasan orang pindah ke Scala",
                    "sekarang ada di Java dan Kotlin. Yang masih jadi kekuatan Scala adalah",
                    "sistem tipenya yang jauh lebih ekspresif dan pustaka fungsionalnya seperti",
                    "Cats Effect dan ZIO.",
                ],
            },
            {
                "heading": "Scala 2, Scala 3, dan given",
                "bahasa": "scala",
                "code": """// Scala 2: implicit
// implicit val formatAngka: Format[Int] = ...
// def cetak[A](a: A)(implicit f: Format[A]) = ...

// Scala 3: given dan using
trait Format[A]:
  def tampil(a: A): String

given Format[Int] with
  def tampil(a: Int) = s"angka $a"

def cetak[A](a: A)(using f: Format[A]): Unit =
  println(f.tampil(a))

@main def coba(): Unit = cetak(42)   // angka 42""",
            },
            {
                "body": [
                    "Scala 3 (2021) merombak banyak bagian bahasa. Yang paling terasa: implicit",
                    "diganti given dan using. Fungsinya sama, yaitu menyediakan nilai yang",
                    "dicari kompilator secara otomatis menurut tipenya. Di contoh di atas,",
                    "cetak(42) butuh Format[Int], dan kompilator menemukan given yang cocok",
                    "tanpa kamu menuliskannya.",
                    "",
                    "Jebakan: tutorial dan jawaban forum sebelum 2021 hampir semuanya Scala 2.",
                    "Kode Scala 2 sebagian besar masih bisa dikompilasi Scala 3, tapi tidak",
                    "sebaliknya. Ditambah lagi, Apache Spark 4 dirilis untuk Scala 2.13, jadi",
                    "job Spark yang kamu temui di kantor besar kemungkinan memakai sintaks",
                    "Scala 2. Lihat versi di berkas build sebelum menyalin contoh dari",
                    "internet.",
                    "",
                    "Untuk proyek, alat build yang paling umum adalah sbt (berkas build.sbt).",
                    "sbt dikenal lambat saat pertama dijalankan dan butuh waktu untuk dipahami.",
                    "Alternatifnya Mill, dan untuk skrip kecil cukup Scala CLI. Di Fedora belum",
                    "ada paket kompilator Scala; pasang lewat Coursier (cs setup) atau SDKMAN",
                    "(sdk install scala).",
                ],
            },
            {
                "heading": "Kapan memilih Scala",
                "body": [
                    "Pilih Scala kalau timmu sudah memakai Spark untuk data besar. Scala juga",
                    "cocok untuk layanan backend yang memakai pustaka fungsional seperti ZIO,",
                    "Cats Effect, atau Apache Pekko (penerus terbuka Akka setelah Akka ganti",
                    "lisensi tahun 2022). Di Survei Stack Overflow 2026, 2,2% responden memakai",
                    "Scala, dan JetBrains mencatat pemakainya sering ada di kelompok gaji",
                    "tinggi.",
                    "",
                    "Kalau yang kamu cari cuma \"Java yang lebih ringkas\" untuk aplikasi Android",
                    "atau backend biasa, Kotlin lebih mudah dipelajari, lebih banyak",
                    "lowongannya, dan alatnya lebih ringan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Scala paling sering kamu temui sebagai job Apache Spark: program yang",
                    "membaca jutaan baris data dari penyimpanan, mengolahnya paralel di banyak",
                    "mesin, lalu menulis hasilnya ke tabel lain. Kodenya terlihat seperti",
                    "rantai map, filter, dan groupBy, persis gaya koleksi yang kamu lihat di",
                    "atas.",
                    "",
                    "Kasus kecil: kamu diminta membaca job Spark yang menghitung total",
                    "penjualan per cabang dan menambahkan syarat supaya transaksi dengan jumlah",
                    "nol atau negatif nggak ikut dihitung.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Cek build.sbt dulu untuk tahu versi Scala dan Spark-nya, supaya",
                    "     kamu memakai sintaks yang cocok.",
                    "  2. Cari rantai pemrosesan datanya. Bentuknya biasanya begini:",
                    "       df.groupBy(\"cabang\").agg(sum(\"jumlah\").as(\"total\"))",
                    "  3. Sisipkan saringan sebelum groupBy, supaya baris yang buruk",
                    "     dibuang lebih dulu.",
                    "       df.filter($\"jumlah\" > 0).groupBy(\"cabang\") ...",
                    "  4. Uji dengan data kecil di komputermu (Spark bisa jalan lokal)",
                    "     dan bandingkan total sebelum dan sesudah perubahan.",
                ],
            },
        ],
    },
    {
        "title": "22. Groovy: Bahasa di Balik Jenkinsfile dan Gradle",
        "sections": [
            {
                "body": [
                    "Banyak orang menulis Groovy tanpa sadar sedang menulis Groovy. Jenkinsfile",
                    "yang mengatur pipeline CI/CD di Jenkins ditulis dengan Groovy. Berkas",
                    "build.gradle di proyek Android dan Java lama juga Groovy. Jadi walaupun",
                    "jarang ada lowongan \"programmer Groovy\", kemungkinan besar kamu harus",
                    "membaca dan menyunting kode Groovy di tempat kerja.",
                    "",
                    "Groovy adalah bahasa dinamis di atas JVM, akrab untuk orang Java: hampir",
                    "semua kode Java juga kode Groovy yang sah. Versi terbarunya Groovy 6.0.0",
                    "(September 2026, butuh JDK 17 ke atas), dan jalur 5.1 masih dirawat.",
                    "Lisensinya Apache 2.0. Di Survei Stack Overflow 2026, 3,9% responden",
                    "memakainya, hampir semuanya lewat Jenkins dan Gradle.",
                ],
            },
            {
                "heading": "Groovy dalam lima menit",
                "bahasa": "groovy",
                "code": """def nama = 'Ani'
println "Halo, ${nama}!"                  // Halo, Ani!
def nilai = [85, 70, 92]
println nilai.collect { it + 5 }          // [90, 75, 97]
println nilai.findAll { n -> n > 80 }     // [85, 92]
def siswa = [nama: 'Budi', kelas: 'B']
println siswa.nama                        // Budi
def alamat = null
println alamat?.kota ?: 'tidak diketahui' // tidak diketahui""",
            },
            {
                "body": [
                    "Ciri-ciri yang perlu kamu kenali saat membaca kode Groovy:",
                    "",
                    "  - def membuat variabel tanpa menyebut tipe. Tipe tetap boleh",
                    "    ditulis seperti di Java (String nama = 'Ani').",
                    "  - Kurung saat memanggil fungsi boleh dibuang: println \"x\" sama",
                    "    dengan println(\"x\"). Titik koma di akhir baris juga opsional.",
                    "  - Teks berkutip ganda adalah GString, jadi ${nama} diganti isinya.",
                    "    Teks berkutip tunggal dicetak apa adanya.",
                    "  - Kurung kurawal { ... } adalah closure, yaitu fungsi tanpa nama",
                    "    yang bisa dioper. Kalau closure punya satu parameter dan kamu",
                    "    nggak memberinya nama, namanya otomatis it.",
                    "  - [a, b] membuat list dan [kunci: nilai] membuat map.",
                    "  - ?. berhenti dengan aman kalau nilainya null, dan ?: (Elvis)",
                    "    memberi nilai cadangan.",
                    "",
                    "Kode di atas sudah dijalankan dengan Groovy 6.0.0, dan komentar di tiap",
                    "baris adalah keluarannya. Pasang Groovy lewat SDKMAN (sdk install groovy)",
                    "lalu jalankan dengan groovy namaberkas.groovy.",
                ],
            },
            {
                "heading": "Rahasia DSL: closure sebagai argumen terakhir",
                "bahasa": "groovy",
                "code": """def stage(String judul, Closure isi) {
    println "== ${judul}"
    isi()
}
def sh(String perintah) { println "jalankan: ${perintah}" }

stage('Build') {
    sh './gradlew build'
}
stage('Test') {
    sh './gradlew test'
}""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  == Build",
                    "  jalankan: ./gradlew build",
                    "  == Test",
                    "  jalankan: ./gradlew test",
                    "",
                    "Pola ini yang bikin Groovy cocok untuk DSL (domain specific language,",
                    "bahasa kecil untuk satu keperluan). Di Groovy, kalau argumen terakhir",
                    "sebuah fungsi adalah closure, closure itu boleh ditulis di luar kurung.",
                    "Jadi stage('Build') { ... } adalah pemanggilan biasa stage('Build', { ...",
                    "}). Begitu kamu tahu ini, Jenkinsfile dan build.gradle berhenti terlihat",
                    "seperti bahasa aneh: semuanya cuma pemanggilan fungsi yang menerima",
                    "closure.",
                ],
            },
            {
                "heading": "Jenkinsfile deklaratif",
                "bahasa": "groovy",
                "code": """pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh './gradlew build -x test' }
        }
        stage('Test') {
            steps { sh './gradlew test' }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps { sh './deploy.sh' }
        }
    }
    post {
        failure { echo 'Pipeline gagal, cek log tahap terakhir' }
    }
}""",
            },
            {
                "body": [
                    "Jenkins mengenal dua gaya Jenkinsfile. Gaya deklaratif (di atas) diawali",
                    "pipeline { } dan strukturnya tetap: agent, stages, steps, post. Gaya skrip",
                    "diawali node { } dan isinya Groovy bebas dengan if dan perulangan. Untuk",
                    "pipeline baru, dokumentasi Jenkins menyarankan deklaratif karena lebih",
                    "mudah dibaca dan divalidasi.",
                    "",
                    "Jebakan: Groovy di Jenkinsfile bukan Groovy biasa. Jenkins menjalankan",
                    "pipeline dalam mode CPS (continuation passing style), supaya pipeline bisa",
                    "berhenti dan dilanjutkan, misalnya saat Jenkins di-restart. Akibatnya",
                    "sebagian fitur Groovy berperilaku lain di sana, dan fungsi yang butuh",
                    "Groovy murni harus diberi anotasi @NonCPS. Selain itu, pemanggilan banyak",
                    "method Java dan Groovy dicegat sandbox Script Security dan menunggu",
                    "persetujuan admin. Kalau kodenya mulai rumit, pindahkan logikanya ke skrip",
                    "terpisah dan panggil lewat sh.",
                ],
            },
            {
                "heading": "build.gradle: Groovy DSL dan Kotlin DSL",
                "bahasa": "groovy",
                "code": """// build.gradle (Groovy DSL)
plugins {
    id 'java'
}
repositories {
    mavenCentral()
}
dependencies {
    implementation 'com.google.code.gson:gson:2.11.0'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.11.0'
}""",
            },
            {
                "heading": "Isi yang sama dalam Kotlin DSL",
                "bahasa": "gradle",
                "code": """// build.gradle.kts (Kotlin DSL)
plugins {
    java
}
repositories {
    mavenCentral()
}
dependencies {
    implementation("com.google.code.gson:gson:2.11.0")
    testImplementation("org.junit.jupiter:junit-jupiter:5.11.0")
}""",
            },
            {
                "body": [
                    "Bedanya kelihatan kecil: Kotlin DSL wajib memakai kurung dan kutip ganda,",
                    "sedangkan Groovy DSL membolehkan kutip tunggal tanpa kurung. Bedanya yang",
                    "besar ada di editor. Kotlin bertipe statis, jadi IntelliJ dan Android",
                    "Studio bisa melengkapi kode dan menandai kesalahan sebelum build",
                    "dijalankan. Karena itu sejak Gradle 8.2, proyek Gradle baru memakai Kotlin",
                    "DSL sebagai bawaan. Proyek lama yang memakai build.gradle tetap jalan, dan",
                    "kamu bakal sering menyuntingnya.",
                    "",
                    "Groovy juga dipakai untuk menulis tes dengan Spock, framework yang membagi",
                    "tes jadi blok given, when, dan then yang mudah dibaca. Ada juga framework",
                    "web Grails, yang sekarang jauh lebih jarang dipakai.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di perusahaan yang memakai Jenkins, setiap repositori biasanya punya",
                    "Jenkinsfile di akarnya. Setiap push memicu Jenkins membaca berkas itu lalu",
                    "menjalankan tahap build, tes, dan deploy. Menambah satu tahap atau",
                    "memperbaiki tahap yang gagal adalah pekerjaan yang sering dilimpahkan ke",
                    "anak magang.",
                    "",
                    "Kasus kecil: pipeline perlu tahap baru yang menjalankan pemeriksa gaya",
                    "kode (lint) sebelum tes, dan tahap deploy hanya boleh jalan di cabang",
                    "main.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pastikan Jenkinsfile-nya deklaratif (diawali pipeline {).",
                    "  2. Sisipkan stage baru di antara Build dan Test, dengan bentuk yang",
                    "     sama seperti stage lain.",
                    "       stage('Lint') {",
                    "           steps { sh './gradlew check -x test' }",
                    "       }",
                    "  3. Cek apakah stage Deploy sudah punya when { branch 'main' }.",
                    "     Kalau belum, tambahkan.",
                    "  4. Push ke cabang percobaan dan buka tampilan pipeline di Jenkins.",
                    "     Tahap Lint harus muncul, dan Deploy harus dilewati.",
                ],
            },
        ],
    },
    {
        "title": "23. F#: Pemrograman Fungsional di .NET",
        "sections": [
            {
                "body": [
                    "F# adalah bahasa fungsional buatan Microsoft yang berjalan di .NET,",
                    "platform yang sama dengan C#. Artinya F# bisa memakai semua pustaka .NET",
                    "dan paket NuGet, dan proyek F# bisa dipanggil dari C#. F# lahir dari riset",
                    "Microsoft Research dan banyak meminjam dari OCaml (lihat peta bahasa",
                    "fungsional di bab berikutnya).",
                    "",
                    "Versi F# ikut rilis .NET tahunan. F# 10 dirilis bersama .NET 10 pada",
                    "November 2025. Lisensinya MIT. Di Survei Stack Overflow 2026, 1,2%",
                    "responden memakai F#. Komunitasnya kecil, tapi F# punya penggemar setia di",
                    "analitik keuangan dan skrip pengolahan data.",
                    "",
                    "Kabar baiknya untuk pemilik aplikasi ini: kalau .NET SDK sudah terpasang",
                    "untuk kurikulum C#, F# sudah ikut. Semua contoh di materi ini sudah",
                    "dijalankan dengan dotnet fsi.",
                ],
            },
            {
                "heading": "Menjalankan skrip F#",
                "bahasa": "terminal",
                "code": """dotnet fsi halo.fsx      # jalankan skrip
dotnet fsi               # REPL interaktif, akhiri ekspresi dengan ;;
dotnet new console -lang F# -o proyekku   # proyek lengkap""",
            },
            {
                "heading": "let, inferensi tipe, dan pipe",
                "bahasa": "fsharp",
                "code": """printfn "Halo, Dunia!"

let teks = "makan nasi makan sate minum teh manis"

let hasil =
    teks.Split(' ')
    |> Array.filter (fun k -> k.Length > 3)
    |> Array.countBy id
    |> Array.sortByDescending snd

for (kata, n) in hasil do
    printfn "%s %d" kata n""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  Halo, Dunia!",
                    "  makan 2",
                    "  nasi 1",
                    "  sate 1",
                    "  minum 1",
                    "  manis 1",
                    "",
                    "let mengikat nama ke nilai, dan nilainya nggak bisa diubah. Untuk variabel",
                    "yang memang harus berubah, F# meminta kamu menulis let mutable secara",
                    "eksplisit. Tipe hampir nggak pernah ditulis, karena F# menebaknya dari",
                    "pemakaian. Indentasi punya arti, mirip Python: badan let hasil ditandai",
                    "oleh baris yang menjorok.",
                    "",
                    "Operator |> (pipe) mengoper nilai di kirinya sebagai argumen terakhir",
                    "fungsi di kanannya. Jadi teks dipecah jadi kata, disaring yang lebih dari",
                    "tiga huruf, dihitung kemunculannya dengan Array.countBy, lalu diurutkan",
                    "dari yang paling sering. Kata \"teh\" hilang karena cuma tiga huruf.",
                    "Urutannya terbaca dari atas ke bawah, sama seperti pipe di R.",
                ],
            },
            {
                "heading": "Komposisi dengan >>",
                "bahasa": "fsharp",
                "code": """let tambahSatu x = x + 1
let kaliDua x = x * 2

let tambahLaluKali = tambahSatu >> kaliDua

printfn "%d" (tambahLaluKali 5)           // 12
printfn "%d" (5 |> tambahSatu |> kaliDua) // 12""",
            },
            {
                "body": [
                    "Kalau |> mengoper nilai, >> menyambung dua fungsi jadi fungsi baru.",
                    "tambahSatu >> kaliDua artinya \"tambah satu dulu, lalu kali dua\", jadi 5",
                    "jadi 6 lalu 12. Bedanya: dengan >> kamu mendapat fungsi yang bisa disimpan",
                    "dan dipakai ulang, tanpa menyebut nilainya sama sekali.",
                ],
            },
            {
                "heading": "Discriminated union, record, dan Option",
                "bahasa": "fsharp",
                "code": """type Bentuk =
    | Lingkaran of jari: float
    | Persegi of sisi: float
    | Segitiga of alas: float * tinggi: float

let luas bentuk =
    match bentuk with
    | Lingkaran r -> System.Math.PI * r * r
    | Persegi s -> s * s
    | Segitiga (a, t) -> 0.5 * a * t

[ Lingkaran 1.0; Persegi 2.0; Segitiga (3.0, 4.0) ]
|> List.iter (fun b -> printfn "%A -> %.2f" b (luas b))

type Siswa = { Nama: string; Nilai: int }
let ani = { Nama = "Ani"; Nilai = 85 }
let ani2 = { ani with Nilai = 90 }      // salinan, ani tetap 85

let cariNilai nama =
    [ ani; { Nama = "Budi"; Nilai = 70 } ]
    |> List.tryFind (fun s -> s.Nama = nama)
    |> Option.map (fun s -> s.Nilai)

printfn "%A" (cariNilai "Budi")          // Some 70
printfn "%A" (cariNilai "Citra")         // None
printfn "%d" (cariNilai "Citra" |> Option.defaultValue 0)  // 0""",
            },
            {
                "body": [
                    "Baris List.iter mencetak:",
                    "",
                    "  Lingkaran 1.0 -> 3.14",
                    "  Persegi 2.0 -> 4.00",
                    "  Segitiga (3.0, 4.0) -> 6.00",
                    "",
                    "Discriminated union (DU) adalah tipe yang nilainya salah satu dari",
                    "beberapa bentuk, masing-masing boleh membawa data. Ini padanan sealed",
                    "trait plus case class di Scala, tapi ditulis dalam empat baris. Kalau ada",
                    "bentuk yang lupa ditangani di match, kompilator F# memberi peringatan",
                    "\"Incomplete pattern matches\".",
                    "",
                    "Record adalah kelas data yang nggak bisa diubah. { ani with Nilai = 90 }",
                    "membuat salinan dengan satu nilai diganti. Option berisi Some nilai atau",
                    "None, dan F# memakainya sebagai pengganti null. List.tryFind memberi None",
                    "kalau nggak ada yang cocok, dan Option.map cuma menjalankan fungsinya",
                    "kalau isinya Some.",
                ],
            },
            {
                "heading": "F# dan C# di proyek yang sama",
                "body": [
                    "Karena keduanya menghasilkan kode untuk .NET, F# bisa langsung memakai",
                    "kelas .NET seperti System.IO.File atau System.Math, seperti terlihat di",
                    "contoh luas tadi. Pustaka F# juga bisa direferensikan dari proyek C#. Pola",
                    "yang cukup umum: logika perhitungan ditulis di F#, sedangkan antarmuka",
                    "atau API-nya ditulis di C#.",
                    "",
                    "Jebakan: di proyek F# (berkas .fsproj), urutan berkas menentukan siapa",
                    "boleh memakai siapa. Berkas hanya bisa memakai yang tertulis di atasnya.",
                    "Menambah berkas baru di urutan yang salah memberi error \"not defined\"",
                    "walaupun fungsinya jelas ada.",
                    "",
                    "Alat yang sering disebut bersama F#: Fable (mengompilasi F# ke JavaScript",
                    "untuk front-end), Giraffe dan Saturn (web backend), FAKE (skrip build),",
                    "dan Ionide (ekstensi VS Code).",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "F# banyak dipakai untuk perhitungan yang aturannya rumit dan harus tepat:",
                    "model harga, perhitungan risiko, atau aturan bisnis yang banyak cabangnya.",
                    "Discriminated union membuat semua kemungkinan kasus tertulis eksplisit,",
                    "dan kompilator mengingatkan kasus yang terlewat. Skrip .fsx juga dipakai",
                    "sebagai pengganti skrip Python di tim yang sudah memakai .NET.",
                    "",
                    "Kasus kecil: kamu diminta membuat skrip yang membaca log.txt dan",
                    "menghitung berapa baris yang memuat kata ERROR, tanpa memasang bahasa baru",
                    "karena di server cuma ada .NET SDK.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat hitung.fsx dan baca semua barisnya lewat pustaka .NET.",
                    "       let baris = System.IO.File.ReadAllLines \"log.txt\"",
                    "  2. Saring dan hitung dengan pipe.",
                    "       let n = baris |> Array.filter (fun b -> b.Contains \"ERROR\")",
                    "                     |> Array.length",
                    "  3. Cetak hasilnya dengan printfn \"%d baris error\" n.",
                    "  4. Jalankan dengan dotnet fsi hitung.fsx dan cocokkan hasilnya",
                    "     dengan grep -c ERROR log.txt.",
                ],
            },
        ],
    },
    {
        "title": "24. Elixir: Pattern Matching dan Operator Pipe",
        "sections": [
            {
                "body": [
                    "Bayangkan aplikasi chat yang harus menjaga ratusan ribu koneksi terbuka",
                    "sekaligus, dan nggak boleh ikut mati cuma karena satu pengguna mengirim",
                    "data aneh. Masalah semacam ini sudah dipecahkan perusahaan telekomunikasi",
                    "Ericsson sejak akhir 1980-an lewat bahasa Erlang dan mesin virtualnya,",
                    "BEAM. Bab ini membahas tiga bahasa yang berjalan di mesin itu: Elixir,",
                    "Erlang, dan Gleam.",
                    "",
                    "Elixir dibuat José Valim dan dirilis tahun 2012. Sintaksnya ramah, mirip",
                    "Ruby, tapi di baliknya ada seluruh kekuatan Erlang. Versi terbarunya saat",
                    "materi ini ditulis (Oktober 2026) adalah 1.20.4, berlisensi Apache 2.0. Di",
                    "Survei Stack Overflow 2026 cuma 2,6% responden yang memakai Elixir, tapi",
                    "62,1% pemakainya ingin terus memakainya. Artinya, orang yang sudah mencoba",
                    "cenderung betah.",
                    "",
                    "Semua contoh Elixir di bab ini sudah dijalankan dengan Elixir 1.20.4 di",
                    "atas Erlang/OTP 29.",
                ],
            },
            {
                "heading": "Memasang dan menjalankan",
                "bahasa": "terminal",
                "code": """sudo dnf install elixir    # Fedora 44: Elixir 1.19 + Erlang/OTP 26
elixir halo.exs            # jalankan skrip
iex                        # REPL interaktif""",
            },
            {
                "heading": "Tanda = adalah pencocokan",
                "bahasa": "elixir",
                "code": """{:ok, nilai} = {:ok, 42}
IO.puts(nilai)                 # 42

[pertama | sisa] = [1, 2, 3]
IO.inspect(pertama)            # 1
IO.inspect(sisa)               # [2, 3]

%{nama: nama} = %{nama: "Ani", kelas: "A"}
IO.puts(nama)                  # Ani

{:ok, _} = {:error, :enoent}   # ** (MatchError)

y = 5
case 5 do
  ^y -> IO.puts("sama dengan y")
  _ -> IO.puts("beda")
end""",
            },
            {
                "body": [
                    "Di kebanyakan bahasa, = artinya \"isi variabel di kiri dengan nilai di",
                    "kanan\". Di Elixir, = artinya \"cocokkan bentuk di kiri dengan nilai di",
                    "kanan\". Kalau cocok, variabel di kiri diikat ke bagian nilai yang",
                    "bersesuaian. Kalau nggak cocok, programnya berhenti dengan MatchError.",
                    "",
                    "Beberapa bentuk yang perlu kamu kenali:",
                    "",
                    "  - :ok dan :error adalah atom, yaitu nilai yang namanya adalah",
                    "    isinya sendiri. Mirip konstanta enum, tapi nggak perlu",
                    "    dideklarasikan.",
                    "  - {a, b} adalah tuple. Hampir semua fungsi Elixir yang bisa gagal",
                    "    mengembalikan {:ok, hasil} atau {:error, alasan}.",
                    "  - [kepala | ekor] membongkar list jadi elemen pertama dan sisanya.",
                    "  - %{kunci: nilai} adalah map. Pola map cukup menyebut kunci yang",
                    "    kamu perlukan; kunci lain diabaikan.",
                    "  - Tanda ^ (pin) artinya \"pakai nilai y yang sudah ada\", bukan",
                    "    \"ikat ulang y\". Tanpa ^, pola y cocok dengan apa pun.",
                    "",
                    "Data di Elixir nggak bisa diubah (immutable). Menulis x = 1 lalu x = 2",
                    "memang boleh, tapi itu mengikat nama x ke nilai baru, bukan mengubah nilai",
                    "lama. Siapa pun yang sudah memegang nilai lama tetap melihat 1.",
                ],
            },
            {
                "heading": "Fungsi berklausa banyak dan guard",
                "bahasa": "elixir",
                "code": """defmodule Hitung do
  def bagi(_, 0), do: {:error, :pembagi_nol}
  def bagi(a, b), do: {:ok, a / b}

  def kategori(n) when n < 0, do: :negatif
  def kategori(0), do: :nol
  def kategori(n) when n > 0, do: :positif

  def faktorial(0), do: 1
  def faktorial(n) when n > 0, do: n * faktorial(n - 1)
end

IO.inspect(Hitung.bagi(10, 4))       # {:ok, 2.5}
IO.inspect(Hitung.bagi(1, 0))        # {:error, :pembagi_nol}
IO.inspect(Enum.map([-3, 0, 7], &Hitung.kategori/1))
                                     # [:negatif, :nol, :positif]
IO.puts(Hitung.faktorial(5))         # 120

hasil =
  case Hitung.bagi(10, 0) do
    {:ok, v} -> "hasil #{v}"
    {:error, alasan} -> "gagal: #{alasan}"
  end
IO.puts(hasil)                       # gagal: pembagi_nol""",
            },
            {
                "body": [
                    "Satu fungsi Elixir boleh punya beberapa klausa (definisi). Saat",
                    "dipanggil, Elixir mencoba klausa dari atas ke bawah dan memakai yang",
                    "pertama cocok. Jadi bagi(1, 0) cocok dengan klausa pertama karena argumen",
                    "keduanya persis 0. Tanda _ artinya \"apa saja, nggak perlu dinamai\".",
                    "",
                    "Kata when menambahkan guard, yaitu syarat tambahan sesudah polanya cocok.",
                    "faktorial(n) when n > 0 cuma dipakai untuk n positif, dan faktorial(-1)",
                    "berakhir dengan FunctionClauseError karena nggak ada klausa yang cocok.",
                    "Ini disengaja: daripada menghitung nilai yang salah tanpa ketahuan,",
                    "programnya berhenti di tempat masalahnya muncul.",
                    "",
                    "case bekerja dengan cara yang sama untuk satu nilai. &Hitung.kategori/1",
                    "adalah cara Elixir menyebut fungsi sebagai nilai; angka /1 adalah arity,",
                    "yaitu jumlah argumennya. Di Elixir, kategori/1 dan kategori/2 dianggap dua",
                    "fungsi yang berbeda.",
                ],
            },
            {
                "heading": "with: rantai langkah yang bisa gagal",
                "bahasa": "elixir",
                "code": """defmodule Akun do
  def cari(1), do: {:ok, %{id: 1, saldo: 50_000}}
  def cari(_), do: {:error, :tidak_ada}

  def tarik(akun, jumlah) when jumlah <= akun.saldo,
    do: {:ok, %{akun | saldo: akun.saldo - jumlah}}
  def tarik(_akun, _jumlah), do: {:error, :saldo_kurang}

  def proses(id, jumlah) do
    with {:ok, akun} <- cari(id),
         {:ok, baru} <- tarik(akun, jumlah) do
      "sisa saldo #{baru.saldo}"
    else
      {:error, alasan} -> "gagal: #{alasan}"
    end
  end
end

IO.puts(Akun.proses(1, 20_000))   # sisa saldo 30000
IO.puts(Akun.proses(1, 90_000))   # gagal: saldo_kurang
IO.puts(Akun.proses(7, 1_000))    # gagal: tidak_ada""",
            },
            {
                "body": [
                    "with menjalankan langkah-langkah berurutan. Setiap baris berbentuk pola <-",
                    "ekspresi. Selama hasilnya cocok dengan pola, with lanjut ke baris",
                    "berikutnya. Begitu ada yang nggak cocok, misalnya cari(7) mengembalikan",
                    "{:error, :tidak_ada}, sisa langkah dilewati dan nilainya dikirim ke bagian",
                    "else. Tanpa with, kamu harus menulis case di dalam case di dalam case.",
                    "",
                    "Perhatikan juga %{akun | saldo: ...}. Itu membuat map baru dengan saldo",
                    "yang diganti, sedangkan akun yang lama tetap utuh.",
                ],
            },
            {
                "heading": "Operator pipe |>",
                "bahasa": "elixir",
                "code": "\"  Halo Dunia dari Elixir  \"\n|> String.trim()\n|> String.downcase()\n|> String.split()\n|> IO.inspect()\n# [\"halo\", \"dunia\", \"dari\", \"elixir\"]\n\nIO.inspect(Enum.map([1, 2, 3], fn n -> n * 10 end))   # [10, 20, 30]\nIO.inspect([90, 75, 97])                            # ~c\"ZKa\"",
            },
            {
                "body": [
                    "Pipe di Elixir mengoper hasil di kiri sebagai argumen pertama fungsi di",
                    "kanan. Ini sama dengan pipe |> di R, dan kebalikan dari F# yang menaruhnya",
                    "di argumen terakhir. Karena pustaka standar Elixir konsisten menaruh data",
                    "di argumen pertama (String.split(teks), Enum.map(list, fungsi)), rantai",
                    "pipe terasa alami.",
                    "",
                    "Jebakan: IO.inspect([90, 75, 97]) mencetak ~c\"ZKa\", bukan list angka.",
                    "Elixir mewarisi dari Erlang kebiasaan menganggap list bilangan bulat",
                    "sebagai daftar kode karakter (charlist), dan kalau semua angkanya huruf",
                    "yang bisa dicetak, IO.inspect menampilkannya sebagai teks. Angka 90, 75,",
                    "dan 97 kebetulan kode huruf Z, K, dan a. Datanya tetap list angka; cuma",
                    "tampilannya. Pakai IO.inspect(list, charlists: :as_lists) kalau ingin",
                    "melihat angkanya.",
                ],
            },
            {
                "heading": "Pembanding: match-case di Python",
                "code": """def bagi(a, b):
    match (a, b):
        case (_, 0):
            return ("error", "pembagi_nol")
        case _:
            return ("ok", a / b)


for hasil in [bagi(10, 4), bagi(1, 0)]:
    match hasil:
        case ("ok", nilai):
            print(f"hasil {nilai}")
        case ("error", alasan):
            print(f"gagal: {alasan}")""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  hasil 2.5",
                    "  gagal: pembagi_nol",
                    "",
                    "Python 3.10 menambahkan match-case yang idenya sama. Bedanya, di Python",
                    "pencocokan cuma ada di match, sedangkan di Elixir pencocokan ada di",
                    "mana-mana: di =, di kepala fungsi, di case, dan di with. Itu yang membuat",
                    "kode Elixir jarang memakai if.",
                ],
            },
            {
                "heading": "Mix dan Hex",
                "body": [
                    "Proyek Elixir dikelola dengan Mix, alat yang ikut terpasang bersama",
                    "Elixir. mix new toko membuat kerangka proyek, mix test menjalankan tes,",
                    "dan mix deps.get mengunduh dependensi. Paketnya diambil dari Hex (hex.pm),",
                    "gudang paket bersama untuk Elixir, Erlang, dan Gleam. Dokumentasi semua",
                    "paket ada di hexdocs.pm dengan format yang sama, jadi membaca dokumentasi",
                    "pustaka baru terasa akrab.",
                    "",
                    "Kalau kamu ingin mencoba pelan-pelan, iex adalah REPL Elixir. Ketik h",
                    "String.split di dalamnya untuk membaca dokumentasi fungsi langsung dari",
                    "terminal.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Elixir paling sering dipakai bersama Phoenix, framework web yang kuat",
                    "untuk fitur real-time: notifikasi langsung, chat, dashboard yang angkanya",
                    "bergerak sendiri. Pola {:ok, ...} dan {:error, ...} plus with muncul di",
                    "hampir setiap fungsi yang menyentuh database atau layanan luar.",
                    "",
                    "Kasus kecil: fungsi daftar_pengguna harus memeriksa email, memastikan",
                    "email belum dipakai, lalu menyimpan pengguna. Kode lamanya berupa tiga",
                    "case bertingkat yang susah dibaca.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pastikan setiap langkah jadi fungsi sendiri yang mengembalikan",
                    "     {:ok, nilai} atau {:error, alasan}.",
                    "  2. Rangkai dengan with, satu langkah per baris.",
                    "       with {:ok, email} <- cek_email(params),",
                    "            :ok <- belum_dipakai(email),",
                    "            {:ok, user} <- simpan(email) do",
                    "         {:ok, user}",
                    "       end",
                    "  3. Tangani semua kegagalan di satu tempat, di bagian else.",
                    "  4. Tulis satu tes untuk tiap jalur gagal dengan mix test, supaya",
                    "     tiap alasan error pernah dicoba.",
                ],
            },
        ],
    },
    {
        "title": "25. Elixir dan OTP: Proses, Pesan, dan Supervisor",
        "sections": [
            {
                "body": [
                    "Kekuatan utama Elixir datang dari mesin yang menjalankannya. Mesin itu",
                    "menjalankan kode di dalam proses-proses kecil. Proses BEAM bukan proses",
                    "sistem operasi dan bukan thread. Ia jauh lebih ringan: membuatnya cuma",
                    "butuh memori beberapa kilobyte, jadi satu server bisa menjalankan ratusan",
                    "ribu proses sekaligus. BEAM membagi proses-proses itu ke semua inti CPU",
                    "secara otomatis.",
                    "",
                    "Setiap proses punya memorinya sendiri dan nggak berbagi variabel dengan",
                    "proses lain. Satu-satunya cara berkomunikasi adalah mengirim pesan.",
                    "Akibatnya, kalau satu proses error dan mati, proses lain nggak ikut rusak,",
                    "karena memang nggak ada data bersama yang bisa rusak. Garbage collector",
                    "juga bekerja per proses, sehingga nggak ada jeda besar yang menghentikan",
                    "seluruh program.",
                ],
            },
            {
                "heading": "spawn, send, dan receive",
                "bahasa": "elixir",
                "code": """pid =
  spawn(fn ->
    receive do
      {:halo, dari} -> send(dari, {:balas, "halo juga"})
    end
  end)

send(pid, {:halo, self()})

receive do
  {:balas, teks} -> IO.puts("dapat balasan: " <> teks)
after
  1000 -> IO.puts("nggak ada balasan")
end""",
            },
            {
                "body": [
                    "Keluarannya dapat balasan: halo juga.",
                    "",
                    "spawn membuat proses baru yang menjalankan fungsi di dalamnya dan",
                    "mengembalikan PID, yaitu alamat proses itu. send(pid, pesan) menaruh pesan",
                    "di kotak surat proses tujuan; pengirim nggak menunggu. receive mengambil",
                    "pesan pertama di kotak surat yang cocok dengan salah satu pola, dan kalau",
                    "belum ada, prosesnya menunggu. Bagian after memberi batas waktu dalam",
                    "milidetik. self() adalah PID proses yang sedang berjalan, dikirim supaya",
                    "penerima tahu ke mana harus membalas.",
                    "",
                    "Menulis spawn dan receive mentah seperti ini jarang dilakukan di aplikasi",
                    "sungguhan. Polanya selalu sama (simpan keadaan, tunggu pesan, balas,",
                    "ulangi), jadi Erlang menyediakan kerangkanya di OTP.",
                ],
            },
            {
                "heading": "GenServer: proses yang menyimpan keadaan",
                "bahasa": "elixir",
                "code": """defmodule Penghitung do
  use GenServer

  # API untuk pemanggil
  def start_link(awal), do: GenServer.start_link(__MODULE__, awal, name: __MODULE__)
  def tambah(n), do: GenServer.cast(__MODULE__, {:tambah, n})
  def nilai, do: GenServer.call(__MODULE__, :nilai)

  # callback yang dijalankan di dalam proses GenServer
  @impl true
  def init(awal), do: {:ok, awal}

  @impl true
  def handle_cast({:tambah, n}, total), do: {:noreply, total + n}

  @impl true
  def handle_call(:nilai, _dari, total), do: {:reply, total, total}
end""",
            },
            {
                "body": [
                    "OTP (Open Telecom Platform) adalah kumpulan pustaka dan pola yang dibawa",
                    "Erlang. Namanya peninggalan zaman telekomunikasi, isinya dipakai untuk",
                    "aplikasi apa pun. GenServer (generic server) adalah pola paling dasarnya:",
                    "sebuah proses yang memegang satu keadaan, di sini angka total, dan",
                    "melayani permintaan satu per satu.",
                    "",
                    "Ada dua jenis permintaan:",
                    "",
                    "  - cast dikirim tanpa menunggu jawaban. handle_cast menerima pesan",
                    "    dan keadaan lama, lalu mengembalikan {:noreply, keadaan_baru}.",
                    "  - call menunggu jawaban. handle_call mengembalikan {:reply,",
                    "    jawaban, keadaan_baru}, dan pemanggil berhenti sampai jawaban",
                    "    itu datang (bawaannya paling lama 5 detik).",
                    "",
                    "Karena proses melayani pesan satu per satu, dua pemanggil yang menambah",
                    "bersamaan nggak akan saling menimpa. Kamu dapat keamanan itu tanpa kunci",
                    "(lock) sama sekali.",
                ],
            },
            {
                "heading": "Supervisor dan let it crash",
                "bahasa": "elixir",
                "code": """children = [{Penghitung, 0}]
{:ok, sup} = Supervisor.start_link(children, strategy: :one_for_one)

Penghitung.tambah(5)
Penghitung.tambah(10)
IO.puts("nilai: #{Penghitung.nilai()}")

lama = Process.whereis(Penghitung)
Process.exit(lama, :kill)          # paksa prosesnya mati
Process.sleep(100)
baru = Process.whereis(Penghitung)
IO.puts("pid berganti? #{lama != baru}")
IO.puts("nilai sesudah crash: #{Penghitung.nilai()}")
IO.inspect(Supervisor.count_children(sup))""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  nilai: 15",
                    "  pid berganti? true",
                    "  nilai sesudah crash: 0",
                    "  %{active: 1, workers: 1, supervisors: 0, specs: 1}",
                    "",
                    "Supervisor adalah proses yang tugasnya cuma mengawasi proses lain (anak).",
                    "Saat Penghitung dibunuh, supervisor menerima kabar kematiannya lalu",
                    "menjalankan Penghitung baru dengan keadaan awal 0. Program utama tetap",
                    "jalan, dan nama Penghitung sekarang menunjuk ke proses yang baru.",
                    "Perhatikan bahwa nilai 15 hilang: keadaan proses yang mati ikut hilang.",
                    "Data yang nggak boleh hilang disimpan di database atau di proses lain.",
                    "",
                    "Strategi menentukan siapa yang dihidupkan ulang:",
                    "",
                    "  - :one_for_one: cuma anak yang mati.",
                    "  - :one_for_all: semua anak, kalau mereka saling bergantung.",
                    "  - :rest_for_one: anak yang mati dan semua anak yang dijalankan",
                    "    sesudahnya.",
                    "",
                    "Supervisor juga punya batas. Bawaannya, kalau lebih dari 3 restart terjadi",
                    "dalam 5 detik, supervisor menyerah dan ikut mati, lalu supervisor di",
                    "atasnya yang mengambil keputusan. Susunan supervisor yang mengawasi",
                    "supervisor lain ini disebut supervision tree.",
                    "",
                    "Dari sini lahir filosofi let it crash. Daripada menulis penanganan error",
                    "untuk setiap kemungkinan aneh, biarkan proses yang kebingungan mati, lalu",
                    "biarkan supervisor memulainya lagi dari keadaan bersih. Error yang memang",
                    "diperkirakan (email salah, saldo kurang) tetap ditangani dengan {:error,",
                    "alasan}. Yang diserahkan ke supervisor adalah kejadian yang nggak masuk",
                    "akal.",
                ],
            },
            {
                "heading": "Konsep yang sama di Erlang",
                "bahasa": "erlang",
                "code": """-module(pesan).
-export([main/0, gema/0]).

gema() ->
    receive
        {halo, Dari} ->
            Dari ! {balas, "halo juga"},
            gema();
        berhenti ->
            ok
    end.

main() ->
    Pid = spawn(pesan, gema, []),
    Pid ! {halo, self()},
    receive
        {balas, Teks} -> io:format("dapat: ~s~n", [Teks])
    after 1000 ->
        io:format("nggak ada balasan~n")
    end,
    Pid ! berhenti.""",
            },
            {
                "body": [
                    "Semua istilah tadi (proses, pesan, GenServer yang di Erlang bernama",
                    "gen_server, supervisor) berasal dari Erlang. Elixir memakai OTP yang sama",
                    "persis, bukan tiruannya. Di Erlang, pengiriman pesan ditulis Pid ! Pesan.",
                    "Fungsi gema memanggil dirinya sendiri di akhir supaya terus menunggu pesan",
                    "berikutnya; BEAM mengoptimalkan pemanggilan terakhir seperti ini sehingga",
                    "stack-nya nggak tumbuh.",
                    "",
                    "Beberapa nama yang akan kamu temui di ekosistem Elixir:",
                    "",
                    "  - Phoenix: framework web. LiveView, bagian dari Phoenix, membuat",
                    "    halaman interaktif yang diperbarui server lewat WebSocket tanpa",
                    "    banyak JavaScript.",
                    "  - Nerves: membuat firmware perangkat embedded (misalnya Raspberry",
                    "    Pi) dengan Elixir. Rincian perangkat kerasnya ada di kurikulum",
                    "    iot.",
                    "  - Oban: antrean pekerjaan latar belakang yang disimpan di",
                    "    database, biasanya PostgreSQL.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola GenServer dan supervisor dipakai untuk apa pun yang harus jalan",
                    "terus: koneksi ke layanan pembayaran, pengambil data berkala, room chat,",
                    "atau sesi game. Setiap room atau sesi bisa jadi satu proses, sehingga room",
                    "yang error cuma membuat satu room diulang, sementara yang lain tetap",
                    "lancar.",
                    "",
                    "Kasus kecil: proses yang mengambil kurs mata uang dari API luar setiap",
                    "menit kadang crash karena API mengirim data rusak, dan setelah crash, kurs",
                    "nggak pernah diperbarui lagi.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Jadikan pengambil kurs sebuah GenServer yang menjadwalkan",
                    "     dirinya sendiri dengan Process.send_after(self(), :ambil,",
                    "     60_000).",
                    "  2. Daftarkan GenServer itu sebagai anak supervisor dengan strategi",
                    "     :one_for_one, supaya crash diikuti restart otomatis.",
                    "  3. Simpan kurs terakhir yang valid di luar proses itu (misalnya di",
                    "     tabel ETS atau database), supaya restart nggak menghapusnya.",
                    "  4. Uji dengan sengaja mengirim data rusak dan pastikan prosesnya",
                    "     hidup lagi dan mengambil kurs di menit berikutnya.",
                ],
            },
        ],
    },
    {
        "title": "26. Peta BEAM: Erlang dan Gleam",
        "sections": [
            {
                "body": [
                    "Elixir bukan satu-satunya penghuni BEAM. Erlang adalah bahasa asli mesin",
                    "itu, dan Gleam adalah pendatang baru yang menambahkan tipe statis.",
                    "Ketiganya dikompilasi ke bytecode yang sama, memakai OTP yang sama, dan",
                    "bisa saling memanggil fungsi. Paket Erlang bisa dipakai dari Elixir dan",
                    "Gleam, begitu juga sebaliknya.",
                ],
            },
            {
                "heading": "Erlang",
                "bahasa": "erlang",
                "code": """-module(hitung).
-export([main/0, faktorial/1, bagi/2]).

faktorial(0) -> 1;
faktorial(N) when N > 0 -> N * faktorial(N - 1).

bagi(_, 0) -> {error, pembagi_nol};
bagi(A, B) -> {ok, A / B}.

main() ->
    io:format("Halo, Dunia!~n"),
    io:format("~p~n", [faktorial(5)]),
    Naik = [N * 10 || N <- [1, 2, 3]],
    io:format("~p~n", [Naik]),
    case bagi(10, 0) of
        {ok, Hasil} -> io:format("hasil ~p~n", [Hasil]);
        {error, Alasan} -> io:format("gagal: ~p~n", [Alasan])
    end.""",
            },
            {
                "heading": "Menjalankan kode Erlang",
                "bahasa": "terminal",
                "code": """sudo dnf install erlang           # Fedora 44 masih OTP 26
erlc hitung.erl                   # menghasilkan hitung.beam
erl -noshell -s hitung main -s init stop""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  Halo, Dunia!",
                    "  120",
                    "  [10,20,30]",
                    "  gagal: pembagi_nol",
                    "",
                    "Erlang lahir di Ericsson tahun 1986 untuk switch telepon yang nggak boleh",
                    "mati. Versi terbarunya Erlang/OTP 29.1.2 (Oktober 2026), berlisensi Apache",
                    "2.0. Paket Fedora 44 tertinggal di OTP 26.2.5, jadi untuk versi terbaru",
                    "orang biasanya memakai pengelola versi seperti asdf atau mise.",
                    "",
                    "Sintaksnya diwarisi dari Prolog, jadi terlihat asing di awal:",
                    "",
                    "  - Variabel diawali huruf besar (N, Hasil) dan cuma bisa diikat",
                    "    sekali. Kata berhuruf kecil (ok, error, pembagi_nol) adalah atom.",
                    "  - Tanda baca punya arti. Koma memisahkan ekspresi dalam satu",
                    "    klausa, titik koma memisahkan klausa, dan titik mengakhiri",
                    "    fungsi.",
                    "  - Nama berkas wajib sama dengan nama modul: modul hitung ada di",
                    "    hitung.erl.",
                    "  - Teks berkutip ganda adalah list kode karakter. Karena itu",
                    "    list [90, 75, 97] dicetak \"ZKa\", jebakan yang sama dengan di",
                    "    Elixir.",
                    "",
                    "Proyek Erlang dibangun dengan rebar3. Software terkenal yang ditulis",
                    "dengan Erlang antara lain message broker RabbitMQ dan server pesan XMPP",
                    "ejabberd; keduanya terbuka, jadi kamu bisa membaca kodenya.",
                ],
            },
            {
                "heading": "Gleam",
                "bahasa": "gleam",
                "code": """import gleam/int
import gleam/io
import gleam/list

pub fn bagi(a: Int, b: Int) -> Result(Int, String) {
  case b {
    0 -> Error("pembagi nol")
    _ -> Ok(a / b)
  }
}

pub fn main() {
  io.println("Halo, Dunia!")
  case bagi(10, 2) {
    Ok(hasil) -> io.println("hasil: " <> int.to_string(hasil))
    Error(pesan) -> io.println("gagal: " <> pesan)
  }
  io.println(int.to_string(7 / 0))
  [85, 70, 92]
  |> list.map(fn(n) { n + 5 })
  |> list.filter(fn(n) { n > 80 })
  |> list.length
  |> int.to_string
  |> io.println
}""",
            },
            {
                "body": [
                    "Keluarannya Halo, Dunia!, lalu hasil: 5, lalu 0, lalu 2. Contoh ini sudah",
                    "dijalankan dengan Gleam 1.19.2, versi terbaru saat materi ini ditulis.",
                    "",
                    "Gleam mencapai versi 1.0 tahun 2024 dan merilis versi minor kira-kira dua",
                    "bulan sekali. Tujuannya membawa tipe statis ke BEAM tanpa mengorbankan",
                    "kesederhanaan. Bahasanya sengaja kecil:",
                    "",
                    "  - Tipe diperiksa saat kompilasi, dan sebagian besar bisa ditebak",
                    "    sendiri oleh kompilator.",
                    "  - Nggak ada null dan nggak ada exception. Fungsi yang bisa gagal",
                    "    mengembalikan Result, berisi Ok(nilai) atau Error(alasan), dan",
                    "    kompilator memaksa kamu menangani keduanya di case.",
                    "  - Nggak ada if. Semua percabangan memakai case.",
                    "  - Gleam bisa dikompilasi ke Erlang atau ke JavaScript. Contoh di",
                    "    atas memberi keluaran yang sama di kedua target.",
                    "",
                    "Jebakan: 7 / 0 di Gleam menghasilkan 0, bukan error. Karena nggak ada",
                    "exception, pembagian dengan nol diberi hasil yang pasti. Kalau pembagi nol",
                    "harus dianggap kesalahan, periksa sendiri seperti fungsi bagi di atas,",
                    "atau pakai int.divide yang mengembalikan Result.",
                ],
            },
            {
                "heading": "Memulai proyek Gleam",
                "bahasa": "terminal",
                "code": """gleam new halo                  # buat proyek baru
cd halo
gleam run                       # jalankan di BEAM (butuh Erlang)
gleam run --target javascript   # jalankan dengan Node.js
gleam test""",
            },
            {
                "heading": "Memilih di antara ketiganya",
                "body": [
                    "Ketiganya berbagi kekuatan yang sama (proses ringan, pesan, supervisor),",
                    "jadi pilihannya lebih soal tim dan ekosistem:",
                    "",
                    "  - Elixir punya ekosistem paling ramai untuk aplikasi web (Phoenix,",
                    "    LiveView, Ecto) dan dokumentasi yang rapi. Pilihan aman untuk",
                    "    proyek baru.",
                    "  - Erlang dipakai kalau kamu merawat sistem lama, bekerja dekat",
                    "    dengan telekomunikasi, atau menyumbang ke proyek seperti",
                    "    RabbitMQ. Memahami sedikit Erlang juga membantu membaca pesan",
                    "    error dan dokumentasi OTP dari Elixir.",
                    "  - Gleam cocok kalau kamu ingin pengecekan tipe yang ketat, atau",
                    "    ingin satu bahasa untuk BEAM dan front-end JavaScript (misalnya",
                    "    lewat framework Lustre). Ekosistemnya masih muda, jadi kadang",
                    "    kamu perlu memanggil pustaka Erlang atau Elixir.",
                    "",
                    "Gleam belum punya paket di repositori Fedora; biner resminya bisa diunduh",
                    "dari halaman rilis GitHub proyeknya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kamu mungkin memakai sistem buatan Erlang tanpa sadar. RabbitMQ, salah",
                    "satu message broker paling populer untuk mengantar pesan antar layanan",
                    "backend, berjalan di atas Erlang. Aplikasi Elixir dan Gleam sering",
                    "memanggil pustaka Erlang yang sudah teruji puluhan tahun, misalnya modul",
                    ":crypto atau :ets.",
                    "",
                    "Kasus kecil: log RabbitMQ di server kantor menampilkan pesan error bergaya",
                    "Erlang seperti {badmatch,{error,enoent}}, dan kamu diminta menebak",
                    "penyebabnya.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Bongkar bentuknya seperti pattern matching. badmatch berarti",
                    "     pencocokan = gagal, setara MatchError di Elixir.",
                    "  2. Lihat nilai yang gagal dicocokkan: {error,enoent}. enoent adalah",
                    "     kode sistem operasi untuk \"berkas atau folder nggak ada\".",
                    "  3. Cari di baris log sebelumnya berkas apa yang sedang dibuka,",
                    "     biasanya berkas konfigurasi atau sertifikat.",
                    "  4. Pastikan jalurnya benar dan dapat dibaca pengguna yang",
                    "     menjalankan RabbitMQ, lalu jalankan ulang layanannya.",
                ],
            },
        ],
    },
    {
        "title": "27. Haskell: Fungsi Murni, Tipe, dan Evaluasi Malas",
        "sections": [
            {
                "body": [
                    "Di bab sebelumnya kamu sudah ketemu ide fungsional di Scala, F#, dan",
                    "Elixir: data yang nggak diubah, fungsi sebagai nilai, dan pattern",
                    "matching. Semua bahasa itu tetap membolehkan efek samping kapan saja,",
                    "misalnya mencetak ke layar dari tengah fungsi apa pun. Haskell nggak",
                    "membolehkan itu. Haskell adalah bahasa fungsional murni.",
                    "",
                    "Fungsi murni artinya hasil fungsi cuma bergantung pada argumennya, dan",
                    "fungsi itu nggak mengubah apa pun di luar dirinya. Panggil kuadrat 4",
                    "seratus kali, hasilnya selalu 16, dan nggak ada berkas, variabel global,",
                    "atau layar yang tersentuh. Efek samping tetap bisa, tapi harus lewat tipe",
                    "khusus bernama IO, dan itu dibahas di materi berikutnya.",
                    "",
                    "Haskell lahir tahun 1990 dari komite peneliti yang ingin satu bahasa",
                    "bersama untuk riset fungsional; namanya diambil dari ahli logika Haskell",
                    "Curry. Banyak ide bahasa modern pertama kali matang di sini, termasuk",
                    "inferensi tipe yang kuat dan typeclass. Kompilator yang dipakai hampir",
                    "semua orang adalah GHC (Glasgow Haskell Compiler). Seri terbarunya saat",
                    "materi ini ditulis adalah GHC 9.14; Fedora 44 membawa GHC 9.10.3. Di",
                    "Survei Stack Overflow 2026, 2,3% responden memakai Haskell.",
                ],
            },
            {
                "heading": "Memasang dan menjalankan",
                "bahasa": "terminal",
                "code": """sudo dnf install ghc cabal-install   # versi Fedora
# atau versi terbaru lewat GHCup (www.haskell.org/ghcup)
runghc halo.hs                       # jalankan tanpa kompilasi terpisah
ghci                                 # REPL, ketik :q untuk keluar""",
            },
            {
                "heading": "Tanda tangan tipe dan fungsi",
                "bahasa": "haskell",
                "code": """kuadrat :: Int -> Int
kuadrat x = x * x

luasPersegiPanjang :: Int -> Int -> Int
luasPersegiPanjang p l = p * l

main :: IO ()
main = do
  putStrLn "Halo, Dunia!"
  print (kuadrat 4)                     -- 16
  print (luasPersegiPanjang 3 5)        -- 15
  print (map kuadrat [1, 2, 3, 4, 5])   -- [1,4,9,16,25]
  print (filter even [1 .. 10])         -- [2,4,6,8,10]
  print [x * x | x <- [1 .. 10], odd x] -- [1,9,25,49,81]""",
            },
            {
                "body": [
                    "Baris kuadrat :: Int -> Int adalah tanda tangan tipe, dibaca \"kuadrat",
                    "menerima Int dan menghasilkan Int\". Untuk dua argumen, tulisannya Int ->",
                    "Int -> Int. Tanda tangan ini boleh saja dihilangkan karena GHC bisa",
                    "menebaknya, tapi kebiasaan komunitas Haskell adalah menulisnya untuk",
                    "setiap fungsi tingkat atas, sebagai dokumentasi yang diperiksa kompilator.",
                    "",
                    "Memanggil fungsi nggak memakai kurung dan koma. kuadrat 4 sama dengan",
                    "kuadrat(4) di Python, dan luasPersegiPanjang 3 5 sama dengan luas(3, 5).",
                    "Kurung cuma dipakai untuk mengelompokkan: print (kuadrat 4) artinya cetak",
                    "hasil kuadrat 4. Tanpa kurung, print kuadrat 4 dibaca sebagai print yang",
                    "diberi dua argumen, dan GHC menolaknya.",
                    "",
                    "Baris terakhir adalah list comprehension, yang dipinjam Python dari",
                    "Haskell: [x * x | x <- [1 .. 10], odd x] berarti x kuadrat, untuk x dari 1",
                    "sampai 10, yang ganjil.",
                ],
            },
            {
                "heading": "Rekursi dan pattern matching",
                "bahasa": "haskell",
                "code": "jumlah :: [Int] -> Int\njumlah []       = 0\njumlah (x : xs) = x + jumlah xs\n\nnilaiHuruf :: Int -> Char\nnilaiHuruf n\n  | n >= 85   = 'A'\n  | n >= 70   = 'B'\n  | n >= 55   = 'C'\n  | otherwise = 'D'\n\nmain :: IO ()\nmain = do\n  print (jumlah [85, 70, 92])          -- 247\n  print (map nilaiHuruf [85, 70, 40])  -- \"ABD\"",
            },
            {
                "body": [
                    "Haskell nggak punya for atau while. Perulangan ditulis sebagai rekursi.",
                    "Fungsi jumlah punya dua persamaan: list kosong jumlahnya 0, dan list yang",
                    "diawali x dengan sisa xs jumlahnya x ditambah jumlah sisanya. Tanda :",
                    "memisahkan elemen pertama dari sisanya, sama seperti [kepala | ekor] di",
                    "Elixir.",
                    "",
                    "Tanda | di nilaiHuruf adalah guard, mirip when di Elixir. GHC mencoba dari",
                    "atas ke bawah, dan otherwise selalu benar. Hasilnya dicetak \"ABD\" karena",
                    "di Haskell, teks (String) adalah list Char.",
                    "",
                    "Dalam praktik, orang Haskell jarang menulis rekursi sendiri untuk hal",
                    "umum. sum, map, filter, dan foldr sudah tersedia. Tapi membaca kode",
                    "Haskell berarti membaca pola seperti ini di mana-mana.",
                ],
            },
            {
                "heading": "Evaluasi malas dan daftar tak hingga",
                "bahasa": "haskell",
                "code": """fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main :: IO ()
main = do
  print (take 5 [1 ..])                  -- [1,2,3,4,5]
  print (take 10 fibs)                   -- [0,1,1,2,3,5,8,13,21,34]
  print (takeWhile (< 40) (map (^ 2) [1 ..]))  -- [1,4,9,16,25,36]
  print (head (filter (> 1000) (map (* 7) [1 ..])))  -- 1001
  print (fst (42, undefined))            -- 42, undefined nggak disentuh""",
            },
            {
                "body": [
                    "Haskell menghitung sebuah nilai hanya kalau nilai itu benar diminta. Ini",
                    "namanya evaluasi malas (lazy evaluation). [1 ..] adalah list semua",
                    "bilangan bulat positif. Di bahasa lain, membuat list itu membuat program",
                    "macet. Di Haskell aman, karena take 5 cuma meminta lima elemen pertama,",
                    "dan sisanya nggak pernah dihitung.",
                    "",
                    "fibs adalah barisan Fibonacci yang didefinisikan memakai dirinya sendiri:",
                    "dua angka pertama 0 dan 1, sisanya adalah fibs dijumlahkan dengan fibs",
                    "yang digeser satu. Definisi ini cuma mungkin karena elemen-elemennya baru",
                    "dihitung saat diminta. Baris terakhir menunjukkan hal yang sama: undefined",
                    "akan menghentikan program kalau dievaluasi, tapi fst cuma mengambil elemen",
                    "pertama, jadi undefined nggak pernah disentuh.",
                ],
            },
            {
                "heading": "Pembanding: generator Python juga malas",
                "code": """from itertools import count, islice, takewhile


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(list(islice(count(1), 5)))
print(list(islice(fibonacci(), 10)))
print(list(takewhile(lambda x: x < 40, (n * n for n in count(1)))))
print(next(x for x in (n * 7 for n in count(1)) if x > 1000))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  [1, 2, 3, 4, 5]",
                    "  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]",
                    "  [1, 4, 9, 16, 25, 36]",
                    "  1001",
                    "",
                    "Generator Python memberi efek yang mirip, tapi kamu harus memintanya",
                    "secara eksplisit dengan yield, islice, atau ekspresi generator. Di Haskell",
                    "semuanya malas secara bawaan, termasuk argumen fungsi biasa.",
                    "",
                    "Jebakan: kemalasan membuat pemakaian memori susah ditebak. foldl (+) 0 [1",
                    ".. 10000000] menumpuk jutaan perhitungan yang belum dikerjakan (thunk)",
                    "sebelum akhirnya menjumlahkannya, dan bisa menghabiskan memori. Versi",
                    "ketatnya, foldl', menjumlah sambil jalan. Di GHC terbaru foldl' sudah ada",
                    "di Prelude; di versi lama impor dari Data.List. Kalau program Haskell",
                    "boros memori, kemalasan adalah tersangka pertama.",
                ],
            },
            {
                "heading": "Alat di sekitar Haskell",
                "body": [
                    "GHCup adalah cara resmi memasang dan berganti versi GHC, Cabal, Stack, dan",
                    "Haskell Language Server (HLS, yang memberi pelengkapan kode dan pesan",
                    "error langsung di VS Code). Cabal dan Stack sama-sama alat build dan",
                    "pengelola paket. Paket Haskell disimpan di Hackage (hackage.haskell.org),",
                    "dan dokumentasinya bisa dicari menurut tipe lewat Hoogle: ketik [a] -> Int",
                    "dan Hoogle menemukan length.",
                    "",
                    "Siapkan mental untuk pesan error tipe yang panjang. Biasanya bagian",
                    "terpenting ada di dua baris pertama: tipe yang diharapkan (Expected) dan",
                    "tipe yang ditemukan (Actual).",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dua alat yang mungkin sudah kamu pakai ditulis dengan Haskell. Pandoc",
                    "mengubah dokumen antar format (Markdown ke Word, HTML ke PDF, dan puluhan",
                    "lainnya). ShellCheck memeriksa skrip Bash dan menunjukkan kesalahan umum",
                    "seperti variabel tanpa tanda kutip. Keduanya terbuka, jadi kamu bisa",
                    "membaca kode Haskell sungguhan di repositorinya.",
                    "",
                    "Kasus kecil: kamu ingin memahami bagaimana ShellCheck memeriksa sebuah",
                    "aturan, tapi kodenya penuh tanda tangan tipe dan pattern matching.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pasang ShellCheck dulu (sudo dnf install ShellCheck) dan",
                    "     jalankan pada satu skrip, supaya kamu tahu kode aturannya,",
                    "     misalnya SC2086.",
                    "  2. Cari kode aturan itu di repositori ShellCheck. Kamu akan",
                    "     menemukan fungsi yang menerima pohon sintaks skrip.",
                    "  3. Baca tanda tangan tipenya dulu, baru badannya. Tipe memberi",
                    "     tahu apa yang masuk dan keluar sebelum kamu menyelami detail.",
                    "  4. Cocokkan tiap persamaan fungsi dengan bentuk kode Bash yang",
                    "     ditangkapnya, persis seperti membaca klausa jumlah [] dan",
                    "     jumlah (x : xs) di atas.",
                ],
            },
        ],
    },
    {
        "title": "28. Haskell Lanjut: Maybe, Typeclass, dan Monad IO",
        "sections": [
            {
                "body": [
                    "Kalau fungsi Haskell harus murni dan nggak punya null maupun exception",
                    "yang dilempar sembarangan, bagaimana cara menyatakan \"hasilnya mungkin",
                    "nggak ada\"? Dan bagaimana program bisa membaca masukan atau mencetak ke",
                    "layar? Dua-duanya diselesaikan lewat tipe. Materi ini membahas tiga tipe",
                    "yang paling sering kamu temui di kode Haskell, yaitu Maybe, Either, dan",
                    "IO, lalu baru menyebut kata yang sering bikin orang mundur: monad.",
                ],
            },
            {
                "heading": "Maybe: hasil yang mungkin kosong",
                "bahasa": "haskell",
                "code": """import Text.Read (readMaybe)

bacaUmur :: String -> Maybe Int
bacaUmur teks = readMaybe teks

cekUmur :: Int -> Maybe Int
cekUmur u = if u >= 0 && u <= 150 then Just u else Nothing

tahunLahir :: String -> Maybe Int
tahunLahir teks =
  case bacaUmur teks of
    Nothing -> Nothing
    Just u  -> case cekUmur u of
      Nothing -> Nothing
      Just v  -> Just (2026 - v)

main :: IO ()
main = do
  print (tahunLahir "18")    -- Just 2008
  print (tahunLahir "abc")   -- Nothing
  print (tahunLahir "200")   -- Nothing""",
            },
            {
                "body": [
                    "Maybe Int berarti \"mungkin ada Int, mungkin nggak\". Nilainya Just angka",
                    "atau Nothing. Ini sama dengan Option di Scala dan F#, dan mirip Optional",
                    "di Java, bedanya di Haskell nggak ada jalan pintas berupa null. Fungsi",
                    "yang menerima Maybe Int nggak bisa langsung menjumlahkannya dengan angka;",
                    "kompilator memaksa kamu membongkarnya dulu dan memutuskan apa yang terjadi",
                    "kalau isinya Nothing.",
                    "",
                    "readMaybe mencoba mengubah teks jadi angka. \"18\" jadi Just 18, dan \"abc\"",
                    "jadi Nothing, bukan program yang crash. Masalahnya terlihat di fungsi",
                    "tahunLahir: setiap langkah yang bisa gagal menambah satu case bertingkat.",
                    "Dengan tiga atau empat langkah, kodenya bergeser makin ke kanan.",
                ],
            },
            {
                "heading": "Rantai >>= dan do",
                "bahasa": "haskell",
                "code": "-- versi rantai: berhenti di Nothing pertama\ntahunLahir2 :: String -> Maybe Int\ntahunLahir2 teks = bacaUmur teks >>= cekUmur >>= \\v -> Just (2026 - v)\n\n-- versi do: artinya sama persis dengan versi rantai\ntahunLahir3 :: String -> Maybe Int\ntahunLahir3 teks = do\n  u <- bacaUmur teks\n  v <- cekUmur u\n  return (2026 - v)",
            },
            {
                "body": [
                    "Operator >>= (dibaca bind) mengambil nilai Maybe di kirinya. Kalau isinya",
                    "Just x, x diberikan ke fungsi di kanannya. Kalau Nothing, seluruh rantai",
                    "langsung jadi Nothing dan sisa fungsi nggak pernah dipanggil. Tanda \\v ->",
                    "... adalah fungsi tanpa nama (lambda).",
                    "",
                    "Notasi do adalah cara menulis rantai >>= supaya terbaca seperti langkah",
                    "berurutan. Baris u <- bacaUmur teks artinya \"bongkar Just, ikat isinya ke",
                    "u, dan kalau Nothing berhenti di sini\". return di Haskell bukan kata kunci",
                    "untuk keluar dari fungsi; ia cuma membungkus nilai, di sini jadi Just",
                    "(2026 - v). Kalau ini mengingatkanmu pada with di Elixir, kamu benar,",
                    "idenya sama.",
                ],
            },
            {
                "heading": "Either: gagal dengan alasan",
                "bahasa": "haskell",
                "code": """bagi :: Int -> Int -> Either String Int
bagi _ 0 = Left "pembagi nol"
bagi a b = Right (a `div` b)

main :: IO ()
main = do
  print (bagi 10 2)                   -- Right 5
  print (bagi 1 0)                    -- Left "pembagi nol"
  print (bagi 100 5 >>= bagi 60)      -- Right 3""",
            },
            {
                "body": [
                    "Maybe cuma bilang \"gagal\" tanpa alasan. Either membawa alasannya: Left",
                    "berisi kesalahan, Right berisi hasil yang benar (gampang diingat: right",
                    "juga berarti benar). Either String Int artinya kalau gagal, alasannya",
                    "berupa String. Ini padanan {:error, alasan} dan {:ok, nilai} di Elixir,",
                    "dan Result di Gleam. >>= bekerja dengan cara yang sama: Left pertama",
                    "menghentikan rantai.",
                    "",
                    "Di baris terakhir, bagi 100 5 menghasilkan Right 20, lalu angka 20",
                    "diberikan sebagai argumen kedua ke bagi 60, jadi 60 dibagi 20, hasilnya",
                    "Right 3.",
                ],
            },
            {
                "heading": "data, typeclass, dan instance",
                "bahasa": "haskell",
                "code": """data Bentuk = Lingkaran Double | Persegi Double
  deriving (Show, Eq)

class PunyaLuas a where
  luas :: a -> Double

instance PunyaLuas Bentuk where
  luas (Lingkaran r) = 3.14 * r * r
  luas (Persegi s)   = s * s

newtype Rupiah = Rupiah Int deriving Show

main :: IO ()
main = do
  print (Persegi 2)                    -- Persegi 2.0
  print (Persegi 2 == Persegi 2)       -- True
  print (map luas [Lingkaran 1, Persegi 3])   -- [3.14,9.0]
  print (fmap (+ 1) (Just 2))          -- Just 3
  print (fmap (+ 1) [1, 2, 3])         -- [2,3,4]
  print (Rupiah 5000)                  -- Rupiah 5000""",
            },
            {
                "body": [
                    "data membuat tipe baru dengan beberapa bentuk, padanan discriminated union",
                    "di F# dan sealed trait di Scala. deriving (Show, Eq) meminta GHC",
                    "membuatkan cara mencetak dan membandingkan secara otomatis.",
                    "",
                    "Typeclass adalah kumpulan fungsi yang bisa dimiliki banyak tipe, mirip",
                    "interface. class PunyaLuas mendeklarasikan fungsi luas, dan instance",
                    "PunyaLuas Bentuk mengisinya untuk tipe Bentuk. Show dan Eq adalah",
                    "typeclass bawaan, begitu juga Functor: tipe yang isinya bisa dipetakan",
                    "dengan fmap. Maybe dan list sama-sama Functor, jadi fmap (+ 1) bekerja",
                    "untuk keduanya.",
                    "",
                    "newtype membungkus satu nilai jadi tipe baru tanpa biaya saat program",
                    "jalan. Rupiah 5000 dan angka 5000 nggak bisa tertukar, karena kompilator",
                    "menganggapnya tipe yang berbeda.",
                ],
            },
            {
                "heading": "IO: efek samping di dalam tipe",
                "bahasa": "haskell",
                "code": """main :: IO ()
main = do
  nama <- getLine
  let sapa = "Halo, " ++ nama ++ "!"
  putStrLn sapa
  mapM_ print [1, 2, 3]""",
            },
            {
                "body": [
                    "getLine bertipe IO String: sebuah aksi yang, kalau dijalankan,",
                    "menghasilkan String. Menulis nama <- getLine di dalam do artinya \"jalankan",
                    "aksi itu dan ikat hasilnya ke nama\", polanya sama dengan u <- bacaUmur",
                    "teks tadi. let dipakai untuk nilai murni biasa, tanpa panah. Fungsi murni",
                    "nggak bisa memanggil getLine, karena tipenya nggak mengandung IO. Dengan",
                    "begitu, cukup dari tanda tangan tipe kamu tahu fungsi mana yang mungkin",
                    "menyentuh dunia luar.",
                    "",
                    "Sekarang istilahnya. Maybe, Either, IO, dan list sama-sama punya operasi",
                    ">>= dan return yang mematuhi beberapa aturan sederhana. Tipe seperti itu",
                    "disebut monad. Itu saja. Kamu sudah memakai tiga monad di materi ini",
                    "sebelum tahu namanya, dan do bekerja untuk semuanya.",
                ],
            },
            {
                "heading": "Pembanding: rantai None di Python",
                "code": """def baca_umur(teks):
    return int(teks) if teks.isdigit() else None


def cek_umur(u):
    return u if 0 <= u <= 150 else None


def bind(nilai, fungsi):
    return None if nilai is None else fungsi(nilai)


for teks in ["18", "abc", "200"]:
    hasil = bind(bind(baca_umur(teks), cek_umur), lambda v: 2026 - v)
    print(teks, "->", hasil)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  18 -> 2008",
                    "  abc -> None",
                    "  200 -> None",
                    "",
                    "Fungsi bind di atas adalah >>= versi Python untuk Maybe. Bedanya, Python",
                    "nggak memaksamu memakainya; kamu tetap bisa lupa memeriksa None dan",
                    "programnya baru error saat jalan. Di Haskell, lupa menangani Nothing",
                    "adalah kesalahan tipe.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola Maybe dan Either menyebar ke banyak bahasa: Optional di Java, Option",
                    "di Rust dan Scala, Result di Rust dan Gleam. Memahami versi Haskell-nya",
                    "membuat semua pola itu terasa satu keluarga. Pandoc, pengubah dokumen yang",
                    "ditulis dengan Haskell, memakai pola ini di mana-mana: membaca dokumen",
                    "bisa gagal, dan kegagalannya dibawa sebagai nilai, bukan sebagai crash.",
                    "",
                    "Kasus kecil: kamu menulis skrip Haskell yang membaca berkas konfigurasi",
                    "berisi port, dan port bisa kosong, bukan angka, atau di luar 1 sampai",
                    "65535.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buat satu fungsi per pemeriksaan, masing-masing mengembalikan",
                    "     Either String Int dengan pesan yang jelas.",
                    "       bacaPort :: String -> Either String Int",
                    "       cekRentang :: Int -> Either String Int",
                    "  2. Rangkai dengan do, supaya pemeriksaan pertama yang gagal",
                    "     menghentikan rantai dan membawa pesannya.",
                    "  3. Di main, bongkar hasilnya dengan case: Left pesan dicetak ke",
                    "     layar, Right port dipakai untuk melanjutkan.",
                    "  4. Uji dengan tiga isi berkas yang salah dan satu yang benar.",
                ],
            },
        ],
    },
    {
        "title": "29. Peta Fungsional dan Transpiler JavaScript",
        "sections": [
            {
                "body": [
                    "Haskell punya banyak kerabat. Sebagian lahir dari keluarga ML, bahasa yang",
                    "dibuat Robin Milner di Universitas Edinburgh tahun 1973 sebagai bahasa",
                    "untuk alat pembuktian. Sebagian lagi lahir karena orang ingin menulis",
                    "front-end web dengan gaya fungsional, lalu mengompilasinya jadi JavaScript",
                    "supaya bisa jalan di browser. Bahasa yang dikompilasi ke bahasa lain",
                    "seperti ini sering disebut transpiler.",
                    "",
                    "Materi ini memetakan tujuh nama: OCaml, Caml, Elm, PureScript, ReScript,",
                    "CoffeeScript, dan Roc. Untuk tiap bahasa kamu cukup tahu bentuk kodenya,",
                    "kegunaannya, dan statusnya per Oktober 2026.",
                ],
            },
            {
                "heading": "OCaml dan leluhurnya, Caml",
                "bahasa": "ocaml",
                "code": "let () = print_endline \"Halo, Dunia!\"\n\nlet rec faktorial n = if n = 0 then 1 else n * faktorial (n - 1)\n\nlet rata xs = List.fold_left ( +. ) 0.0 xs /. float_of_int (List.length xs)\n\nlet () =\n  Printf.printf \"%d\\n\" (faktorial 5);          (* 120 *)\n  Printf.printf \"%.2f\\n\" (rata [85.; 70.; 92.]) (* 82.33 *)",
            },
            {
                "body": [
                    "OCaml adalah anggota keluarga ML yang paling banyak dipakai. Ia cepat,",
                    "bertipe kuat dengan inferensi penuh, dan sejak OCaml 5 (2022) mendukung",
                    "multicore. Versi terbarunya 5.5.1 (September 2026). Alat standarnya opam",
                    "(pengelola paket) dan dune (alat build). Software terbuka yang ditulis",
                    "dengan OCaml antara lain asisten pembuktian Rocq (dulu Coq), pemeriksa",
                    "tipe JavaScript Flow, dan sistem operasi mini MirageOS.",
                    "",
                    "Jebakan: OCaml memisahkan operator bilangan bulat dan pecahan. 1 + 2 untuk",
                    "int, sedangkan 1.0 +. 2.0 untuk float, dengan titik di belakang",
                    "operatornya. Mencampur keduanya adalah error tipe, bukan konversi",
                    "otomatis.",
                    "",
                    "Caml adalah leluhur langsung OCaml, dikembangkan di INRIA, Prancis,",
                    "sejak 1985. Implementasi terakhirnya, Caml Light 0.75, dirilis tahun",
                    "2002 dan sudah nggak dikembangkan. Caml masih muncul di peringkat TIOBE,",
                    "tapi untuk belajar langsung pakai OCaml; contoh Caml Light sederhana",
                    "umumnya jalan di REPL ocaml.",
                    "",
                    "F# yang kamu pelajari di bab sebelumnya juga meminjam banyak dari OCaml,",
                    "dan ReScript di bawah ini lahir langsung dari kompilator OCaml.",
                ],
            },
            {
                "heading": "Elm: front-end tanpa error saat jalan",
                "bahasa": "elm",
                "code": "module Main exposing (main)\n\nimport Html exposing (text)\n\n\nmain =\n    text \"Halo, Dunia!\"",
            },
            {
                "body": [
                    "Elm adalah bahasa khusus front-end web yang dikompilasi ke JavaScript.",
                    "Janjinya: kalau kodenya lolos kompilasi, aplikasi praktis nggak pernah",
                    "error saat jalan. Pesan error kompilatornya terkenal paling ramah di",
                    "antara semua bahasa. Pola The Elm Architecture (model, update, view)",
                    "ditiru banyak pustaka JavaScript, termasuk Redux.",
                    "",
                    "Elm sempat nggak merilis apa pun sejak 0.19.1 (2019), lalu muncul 0.19.2",
                    "(Juli 2026) dan 0.19.3 (Oktober 2026) yang memperbarui infrastruktur",
                    "kompilatornya tanpa mengubah bahasanya. Di Survei Stack Overflow 2026,",
                    "94,1% pemakai Elm ingin terus memakainya, tapi pemakainya cuma 0,1%",
                    "responden, jadi angka itu dari sampel yang kecil sekali. Interaksi dengan",
                    "JavaScript hanya lewat ports, dan ekosistem paketnya terbatas.",
                ],
            },
            {
                "heading": "PureScript dan ReScript",
                "bahasa": "purescript",
                "code": "module Main where\n\nimport Prelude\n\nimport Effect (Effect)\nimport Effect.Console (log)\n\nmain :: Effect Unit\nmain = log \"Halo, Dunia!\"",
            },
            {
                "heading": "Contoh ReScript",
                "bahasa": "rescript",
                "code": """let kuadrat = x => x * x

Console.log("Halo, Dunia!")
Console.log(kuadrat(4))""",
            },
            {
                "body": [
                    "PureScript terlihat seperti Haskell yang dikompilasi ke JavaScript: tanda",
                    "tangan tipe yang sama, typeclass yang sama, dan efek samping yang ditandai",
                    "lewat tipe Effect (padanan IO). Versinya 0.15.16 (Maret 2026) dan sudah",
                    "lama di bawah 1.0. Proyeknya dikelola dengan Spago, dan pustaka UI yang",
                    "populer adalah Halogen. Cocok untuk tim yang sudah suka Haskell dan ingin",
                    "gaya yang sama di front-end.",
                    "",
                    "ReScript berasal dari keluarga OCaml (dulu bernama BuckleScript, lalu",
                    "sempat memakai sintaks Reason). Ia menghasilkan JavaScript yang rapi dan",
                    "mudah dibaca, dan sering dipakai bersama React oleh tim yang ingin tipe",
                    "lebih ketat daripada TypeScript. Versi stabilnya 12.3.1 (Agustus 2026),",
                    "dengan versi 13 masih alpha. Jebakan: banyak artikel lama memakai nama dan",
                    "sintaks Reason yang sudah ditinggalkan.",
                ],
            },
            {
                "heading": "CoffeeScript: masih ada di kode lama",
                "bahasa": "coffeescript",
                "code": """console.log "Halo, Dunia!"
kuadrat = (x) -> x * x
nilai = [85, 70, 92]
console.log (n + 5 for n in nilai)          # [ 90, 75, 97 ]
console.log (n for n in nilai when n > 80)  # [ 85, 92 ]
console.log kuadrat 4                       # 16""",
            },
            {
                "body": [
                    "CoffeeScript populer sekitar 2010 sampai 2015 karena menawarkan fungsi",
                    "panah, comprehension, dan sintaks ringkas saat JavaScript belum punya",
                    "semua itu. Begitu JavaScript modern (ES2015 dan sesudahnya) menyerap",
                    "fitur-fitur tersebut, alasan memakainya hilang. Rilis terakhirnya 2.7.0",
                    "pada April 2022. Contoh di atas sudah dijalankan dengan CoffeeScript",
                    "2.7.0.",
                    "",
                    "Statusnya: masih ada di kode lama, misalnya aplikasi Rails generasi awal,",
                    "jangan dipilih untuk proyek baru. Kalau kamu merawat berkas .coffee, jalur",
                    "migrasinya adalah mengompilasi berkas itu sekali jadi JavaScript (coffee",
                    "-c berkas.coffee), merapikan hasilnya, lalu melanjutkan dengan JavaScript",
                    "atau TypeScript.",
                ],
            },
            {
                "heading": "Roc: masih eksperimen",
                "bahasa": "roc",
                "code": """main! = |_args| {
    echo!("Halo, Dunia!")
    Ok({})
}""",
            },
            {
                "body": [
                    "Roc adalah bahasa fungsional baru yang ingin cepat dan ramah pemula.",
                    "Idenya, efek samping seperti membaca berkas atau jaringan disediakan oleh",
                    "platform yang dipilih aplikasi, sehingga kode aplikasinya tetap murni.",
                    "Statusnya eksperimental: belum ada rilis 0.1, kompilatornya sedang ditulis",
                    "ulang dengan Zig, dan sintaksnya sudah beberapa kali berubah. Contoh di",
                    "atas diambil dari tutorial kompilator barunya; contoh dari tahun-tahun",
                    "sebelumnya banyak yang nggak berlaku lagi. Menarik untuk diikuti, belum",
                    "untuk produksi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Saat PKL di tim front-end, kamu lebih mungkin menemukan berkas .coffee",
                    "atau .res di repositori lama daripada diminta memulai proyek Elm baru.",
                    "Yang penting adalah mengenali bahasanya dari ekstensi dan sintaksnya, lalu",
                    "tahu cara mengompilasinya.",
                    "",
                    "Kasus kecil: repositori lama punya folder assets berisi berkas .coffee,",
                    "dan build-nya gagal karena alat build baru nggak lagi memproses",
                    "CoffeeScript.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Pastikan dulu itu CoffeeScript: ekstensi .coffee, tanpa kurung",
                    "     kurawal, fungsi ditulis dengan tanda panah ->.",
                    "  2. Pasang kompilatornya di folder proyek.",
                    "       npm install --save-dev coffeescript",
                    "  3. Kompilasi semua berkas jadi JavaScript sekali saja.",
                    "       npx coffee -c -o assets/js assets/coffee",
                    "  4. Jalankan aplikasinya, rapikan JavaScript hasilnya, lalu hapus",
                    "     berkas .coffee setelah semua fitur dicek.",
                ],
            },
        ],
    },
    {
        "title": "30. Keluarga Lisp: Common Lisp, Scheme, Racket, Clojure",
        "sections": [
            {
                "body": [
                    "Lisp dibuat John McCarthy tahun 1958, jadi termasuk keluarga bahasa tertua",
                    "yang masih dipakai, cuma sedikit lebih muda dari Fortran. Ciri yang",
                    "langsung terlihat adalah tanda kurungnya. Semua kode Lisp ditulis sebagai",
                    "daftar dalam kurung, yang disebut S-expression (symbolic expression):",
                    "",
                    "  (+ 1 (* 2 3))",
                    "",
                    "Bacanya: elemen pertama adalah operator atau fungsi, sisanya argumen. Jadi",
                    "itu artinya 1 + (2 * 3), hasilnya 7. Nggak ada aturan prioritas operator",
                    "yang perlu dihafal, karena kurunglah yang menentukan urutannya.",
                    "",
                    "Lisp sekarang lebih tepat disebut keluarga. Anggota yang paling sering",
                    "kamu temui adalah Common Lisp, Scheme, Racket, dan Clojure, ditambah Emacs",
                    "Lisp untuk mengatur editor Emacs. Di Survei Stack Overflow 2026, 2,6%",
                    "responden memakai salah satu Lisp, dan 1,3% memakai Clojure.",
                ],
            },
            {
                "heading": "Kode sebagai data (Common Lisp)",
                "bahasa": "lisp",
                "code": """(defun kuadrat (x) (* x x))
(format t "Halo, Dunia!~%")
(format t "~a~%" (kuadrat 4))                 ; 16
(format t "~a~%" (mapcar #'kuadrat '(1 2 3))) ; (1 4 9)

(let ((kode '(+ 1 (* 2 3))))
  (format t "~a~%" (first kode))   ; +
  (format t "~a~%" (rest kode))    ; (1 (* 2 3))
  (format t "~a~%" (eval kode)))   ; 7

(format t "~a~%" (/ 247 3))        ; 247/3""",
            },
            {
                "body": [
                    "Contoh ini sudah dijalankan dengan SBCL 2.6.9 (sbcl --script berkas.lisp),",
                    "dan komentar sesudah titik koma adalah keluarannya.",
                    "",
                    "Perhatikan bagian let. Tanda kutip di depan '(+ 1 (* 2 3)) artinya \"jangan",
                    "jalankan, simpan sebagai data\". Hasilnya list biasa dengan tiga elemen:",
                    "simbol +, angka 1, dan list (* 2 3). Kamu bisa mengambil elemen pertamanya",
                    "dengan first, sisanya dengan rest, lalu menjalankannya dengan eval. Kode",
                    "program dan data punya bentuk yang sama persis. Sifat ini disebut",
                    "homoiconicity, dan dari sinilah kekuatan Lisp berasal.",
                    "",
                    "Baris terakhir memperlihatkan hal lain: 247 dibagi 3 di Common Lisp",
                    "menghasilkan pecahan persis 247/3, bukan 82.333.",
                ],
            },
            {
                "heading": "Macro: program yang menulis program",
                "bahasa": "lisp",
                "code": """(defmacro kecuali (syarat &body isi)
  `(if ,syarat nil (progn ,@isi)))

(kecuali (> 1 2) (format t "1 nggak lebih dari 2~%"))

(macroexpand-1 '(kecuali (> 1 2) (print 1)))
;; => (IF (> 1 2) NIL (PROGN (PRINT 1)))""",
            },
            {
                "body": [
                    "Karena kode adalah list, Lisp punya macro: fungsi yang berjalan saat kode",
                    "dibaca, menerima potongan kode sebagai data, dan mengembalikan kode baru.",
                    "Macro kecuali di atas mengubah (kecuali syarat isi...) jadi (if syarat nil",
                    "(progn isi...)). Tanda backtick ` membuat templat, koma , menyisipkan satu",
                    "nilai, dan ,@ menyisipkan isi list. macroexpand-1 menunjukkan kode hasil",
                    "ubahannya.",
                    "",
                    "Macro di bahasa lain (misalnya #define di C) bekerja pada teks dan gampang",
                    "merusak kode. Macro Lisp bekerja pada struktur yang sudah terurai, jadi",
                    "kamu bisa menambah konstruksi baru ke bahasa yang terasa seperti bawaan.",
                    "Common Lisp sendiri sudah punya unless yang persis sama dengan kecuali;",
                    "banyak \"kata kunci\" Lisp ternyata macro seperti ini.",
                    "",
                    "Ada efek samping yang lebih praktis: karena sintaks Lisp cuma list,",
                    "interpreter Lisp bisa ditulis dalam satu sore. Di bawah ini versi mininya",
                    "dalam Python.",
                ],
            },
            {
                "heading": "Evaluator S-expression mini di Python",
                "code": """def token(teks):
    return teks.replace("(", " ( ").replace(")", " ) ").split()


def baca(t):
    x = t.pop(0)
    if x == "(":
        daftar = []
        while t[0] != ")":
            daftar.append(baca(t))
        t.pop(0)
        return daftar
    return int(x) if x.lstrip("-").isdigit() else x


OPERATOR = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
            "*": lambda a, b: a * b}


def hitung(x):
    if isinstance(x, int):
        return x
    op, *arg = x
    nilai = [hitung(a) for a in arg]
    hasil = nilai[0]
    for v in nilai[1:]:
        hasil = OPERATOR[op](hasil, v)
    return hasil


pohon = baca(token("(+ 1 (* 2 3))"))
print(pohon)
print(hitung(pohon))
print(hitung(baca(token("(- (* 4 5) (+ 1 2 3))"))))""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  ['+', 1, ['*', 2, 3]]",
                    "  7",
                    "  14",
                    "",
                    "Tiga langkah, masing-masing beberapa baris. token memecah teks jadi",
                    "potongan. baca mengubah potongan jadi list bersarang, yaitu pohon",
                    "sintaksnya. hitung menelusuri pohon itu: angka dikembalikan apa adanya,",
                    "list dihitung dengan menghitung argumennya dulu lalu menerapkan",
                    "operatornya. Interpreter untuk bahasa seperti Python butuh ribuan baris",
                    "hanya untuk tahap baca. Latihan bab ini melanjutkan kode ini sampai bisa",
                    "menangani define, lambda, dan if.",
                ],
            },
            {
                "heading": "Empat dialek yang perlu kamu kenali",
                "body": [
                    "Common Lisp distandarkan ANSI tahun 1994 dan standarnya nggak berubah",
                    "sejak itu, tapi implementasinya aktif. Yang paling populer SBCL, dengan",
                    "rilis bulanan; versi terbarunya 2.6.9 (September 2026). Pustaka dipasang",
                    "lewat Quicklisp. Pengembangannya khas: REPL dibiarkan hidup terus, dan",
                    "fungsi diganti satu per satu saat program masih jalan. Kerabat dekatnya,",
                    "Emacs Lisp, dipakai untuk menulis konfigurasi dan ekstensi Emacs, dan",
                    "AutoLISP dipakai di AutoCAD.",
                    "",
                    "Scheme adalah Lisp yang kecil dan rapi, lahir tahun 1975. Standarnya",
                    "R7RS-small (2013). Implementasi yang umum: GNU Guile (bahasa ekstensi GNU,",
                    "dipakai GNU Guix), Chez Scheme yang cepat, dan Chibi yang kecil. Scheme",
                    "terkenal sebagai bahasa buku klasik Structure and Interpretation of",
                    "Computer Programs, yang bisa dibaca gratis secara online.",
                    "",
                    "Racket berawal dari Scheme lalu tumbuh jadi bahasa sendiri, dengan tujuan",
                    "pendidikan dan membuat bahasa baru. Ia datang dengan DrRacket, editor yang",
                    "ramah pemula, dan dipakai buku How to Design Programs. Versi terbarunya",
                    "9.3 (Agustus 2026). Setiap berkas Racket diawali baris #lang yang menyebut",
                    "bahasa apa yang dipakai berkas itu.",
                    "",
                    "Clojure adalah Lisp modern di atas JVM, dibuat Rich Hickey tahun 2007. Ia",
                    "mengutamakan data immutable dan bisa memakai semua pustaka Java. Versi",
                    "terbarunya 1.12.6 (September 2026). Kerabatnya ClojureScript mengompilasi",
                    "ke JavaScript, dan Babashka menjalankan skrip Clojure dengan cepat tanpa",
                    "menunggu JVM menyala.",
                ],
            },
            {
                "heading": "Scheme: faktorial dan list",
                "bahasa": "scheme",
                "code": """(define (faktorial n)
  (if (= n 0)
      1
      (* n (faktorial (- n 1)))))

(display (faktorial 5))                    ; 120
(newline)
(display (map (lambda (x) (* x x)) '(1 2 3)))   ; (1 4 9)
(newline)""",
            },
            {
                "heading": "Racket: #lang dan pecahan persis",
                "bahasa": "racket",
                "code": """#lang racket

(define (rata daftar)
  (/ (apply + daftar) (length daftar)))

(displayln (rata '(85 70 92)))                   ; 247/3
(displayln (exact->inexact (rata '(85 70 92))))  ; 82.33333333333333""",
            },
            {
                "heading": "Clojure: data immutable dan threading macro",
                "bahasa": "clojure",
                "code": """(def siswa [{:nama "Ani" :nilai 85}
            {:nama "Budi" :nilai 70}
            {:nama "Citra" :nilai 92}])

(->> siswa
     (filter #(> (:nilai %) 80))
     (map :nama)
     println)                      ; (Ani Citra)

(def ani-baru (assoc (first siswa) :nilai 90))
(println (first siswa))            ; {:nama Ani, :nilai 85}
(println ani-baru)                 ; {:nama Ani, :nilai 90}""",
            },
            {
                "body": [
                    "Contoh Scheme sudah dijalankan dengan Chibi Scheme, dan contoh Clojure",
                    "dengan Clojure 1.12.6. Di implementasi Scheme yang ketat mengikuti R7RS",
                    "seperti Chibi, program diawali baris (import (scheme base) (scheme",
                    "write)); Guile menerima contoh di atas tanpa baris itu.",
                    "",
                    "Clojure menambahkan kurung siku untuk vektor dan kurung kurawal untuk map,",
                    "jadi kodenya nggak cuma kurung biasa. Kata yang diawali titik dua seperti",
                    ":nama adalah keyword, dan keyword juga bisa dipakai sebagai fungsi untuk",
                    "mengambil nilai dari map. ->> adalah macro threading: ia menyisipkan hasil",
                    "langkah sebelumnya sebagai argumen terakhir langkah berikutnya, mirip pipe",
                    "di F#. assoc membuat map baru dengan nilai yang diganti, dan map yang lama",
                    "tetap utuh.",
                    "",
                    "Jebakan: kurung yang nggak seimbang adalah kesalahan paling umum pemula",
                    "Lisp, dan pesan errornya sering muncul jauh dari tempat kurungnya hilang.",
                    "Pakai editor yang membantu menyeimbangkan kurung, misalnya mode paredit",
                    "atau parinfer, dan biarkan editor yang mengatur indentasinya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lisp jarang jadi bahasa utama lowongan, tapi muncul di tempat yang nggak",
                    "terduga. Pengguna Emacs menulis Emacs Lisp setiap kali mengubah",
                    "konfigurasinya. GNU Guix, pengelola paket untuk Linux, ditulis dan",
                    "dikonfigurasi dengan Guile Scheme. Clojure dipakai di sejumlah layanan",
                    "backend, terutama di sektor keuangan, karena data immutable memudahkan",
                    "penalaran tentang perubahan saldo.",
                    "",
                    "Kasus kecil: kamu ingin menambah satu pintasan di Emacs supaya tombol F5",
                    "menyimpan semua berkas yang terbuka, tapi berkas init.el berisi kurung di",
                    "mana-mana.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Buka ~/.emacs.d/init.el dan cari pola yang sudah ada, biasanya",
                    "     berbentuk (global-set-key (kbd \"...\") 'nama-perintah).",
                    "  2. Cari nama perintahnya lewat M-x apropos atau dokumentasi Emacs;",
                    "     untuk menyimpan semua berkas namanya save-some-buffers.",
                    "  3. Tambahkan satu S-expression baru di akhir berkas.",
                    "       (global-set-key (kbd \"<f5>\") 'save-some-buffers)",
                    "  4. Jalankan dengan M-x eval-buffer, tekan F5, dan pastikan Emacs",
                    "     menawarkan menyimpan berkas yang belum disimpan.",
                ],
            },
        ],
    },
    {
        "title": "31. Prolog dan Lean: Logika yang Bisa Dijalankan",
        "sections": [
            {
                "body": [
                    "Semua bahasa yang sudah kamu pelajari menyuruh komputer melakukan sesuatu,",
                    "langkah demi langkah atau fungsi demi fungsi. Prolog berbeda. Di Prolog",
                    "kamu menuliskan fakta dan aturan, lalu bertanya. Prolog sendiri yang",
                    "mencari jawabannya. Paradigma ini disebut pemrograman logika.",
                    "",
                    "Prolog lahir di Prancis tahun 1972. Implementasi yang paling banyak",
                    "dipakai adalah SWI-Prolog, versi stabil 10.0.2 (2026), berlisensi BSD. Ada",
                    "juga GNU Prolog dan Scryer Prolog, dan kamu bisa mencoba Prolog tanpa",
                    "memasang apa pun lewat SWISH di browser. Di Survei Stack Overflow 2026,",
                    "0,9% responden memakai Prolog.",
                ],
            },
            {
                "heading": "Fakta, aturan, dan pertanyaan",
                "bahasa": "prolog",
                "code": """orangtua(budi, ani).
orangtua(budi, dodi).
orangtua(ani, citra).
orangtua(dodi, eka).
orangtua(dodi, fajar).

kakek(X, Z) :- orangtua(X, Y), orangtua(Y, Z).

leluhur(X, Y) :- orangtua(X, Y).
leluhur(X, Z) :- orangtua(X, Y), leluhur(Y, Z).""",
            },
            {
                "body": [
                    "Lima baris pertama adalah fakta: budi orang tua ani, dan seterusnya. Kata",
                    "berhuruf kecil (budi, ani) adalah atom, yaitu nama tetap. Kata berhuruf",
                    "besar (X, Y, Z) adalah variabel. Baris kakek adalah aturan, dibaca \"X",
                    "kakek Z jika X orang tua Y dan Y orang tua Z\". Tanda :- artinya jika, dan",
                    "koma artinya dan.",
                    "",
                    "Aturan leluhur punya dua klausa. Klausa pertama: orang tua adalah leluhur.",
                    "Klausa kedua: orang tua dari leluhur juga leluhur. Aturan yang memakai",
                    "dirinya sendiri ini menggantikan perulangan.",
                    "",
                    "Simpan sebagai keluarga.pl, jalankan swipl keluarga.pl, lalu ketik",
                    "pertanyaan (query) di prompt ?-. Tekan titik koma untuk meminta jawaban",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Sesi tanya jawab",
                "bahasa": "teks",
                "code": """?- kakek(budi, Cucu).
Cucu = citra ;
Cucu = eka ;
Cucu = fajar.

?- orangtua(X, citra).
X = ani.

?- kakek(ani, X).
false.

?- orangtua(budi, dodi).
true.

?- leluhur(budi, Keturunan).
Keturunan = ani ;
Keturunan = dodi ;
Keturunan = citra ;
Keturunan = eka ;
Keturunan = fajar.""",
            },
            {
                "body": [
                    "Jawaban-jawaban ini sudah dicek dengan menjalankan program yang sama di",
                    "Tau Prolog. Perhatikan bahwa aturan yang sama bisa dipakai ke dua arah.",
                    "orangtua(X, citra) bertanya \"siapa orang tua citra\", padahal nggak ada",
                    "fungsi khusus untuk itu.",
                    "",
                    "Dua mekanisme bekerja di balik layar:",
                    "",
                    "  - Unifikasi: mencocokkan dua bentuk dan mengisi variabel supaya",
                    "    keduanya sama. kakek(budi, Cucu) dicocokkan dengan kepala aturan",
                    "    kakek(X, Z), jadi X diikat ke budi dan Z ke Cucu. Mirip pattern",
                    "    matching di Elixir, tapi variabelnya boleh ada di kedua sisi.",
                    "  - Backtracking: Prolog mencoba fakta dan aturan dari atas ke",
                    "    bawah. Kalau satu jalan buntu atau kamu meminta jawaban lain,",
                    "    Prolog mundur ke pilihan terakhir dan mencoba alternatif",
                    "    berikutnya. Untuk kakek(budi, Cucu), Prolog mencoba Y = ani",
                    "    (menemukan citra), lalu mundur dan mencoba Y = dodi (menemukan",
                    "    eka dan fajar).",
                    "",
                    "Jebakan: urutan klausa dan urutan tujuan di badan aturan memengaruhi",
                    "hasil, bahkan bisa membuat program nggak pernah selesai. Kalau klausa",
                    "kedua leluhur ditulis leluhur(X, Z) :- leluhur(X, Y), orangtua(Y, Z).,",
                    "Prolog memanggil leluhur lagi sebelum sempat memeriksa fakta apa pun,",
                    "terus begitu tanpa akhir, sampai memorinya habis. Taruh tujuan yang",
                    "memeriksa fakta lebih dulu.",
                ],
            },
            {
                "heading": "Lean: kode yang dibuktikan benar",
                "bahasa": "lean",
                "code": """def jumlah : List Nat → Nat
  | [] => 0
  | x :: xs => x + jumlah xs

#eval jumlah [1, 2, 3]   -- 6

example : jumlah [1, 2, 3] = 6 := rfl

theorem jumlah_satu (n : Nat) : jumlah [n] = n := by
  simp [jumlah]""",
            },
            {
                "body": [
                    "Tes biasa memeriksa beberapa contoh: jumlah [1, 2, 3] harus 6. Lean bisa",
                    "melangkah lebih jauh, yaitu membuktikan sifat untuk semua kemungkinan",
                    "masukan. Teorema jumlah_satu menyatakan \"untuk setiap bilangan asli n,",
                    "jumlah dari list berisi n saja adalah n\". Bagian sesudah := adalah",
                    "buktinya. rfl artinya \"kedua sisi sama kalau dihitung\", dan by simp",
                    "[jumlah] meminta Lean menyederhanakan ekspresi memakai definisi jumlah",
                    "sampai kedua sisinya sama. Kalau buktinya salah atau definisinya diubah",
                    "sehingga teorema itu nggak lagi benar, Lean menolak berkasnya, persis",
                    "seperti kompilator menolak kesalahan tipe.",
                    "",
                    "Lean 4 adalah bahasa pemrograman fungsional sekaligus asisten pembuktian",
                    "teorema. Rilisnya bulanan; versi terbarunya v4.35.0 (Oktober 2026),",
                    "berlisensi Apache 2.0. Pustaka Mathlib berisi ratusan ribu teorema",
                    "matematika yang sudah diformalkan, dan Lean makin sering dipakai di riset",
                    "AI untuk penalaran matematika. Lean nggak ada di repositori Fedora; pasang",
                    "lewat elan (pengelola versi Lean), dan pakai ekstensi Lean 4 di VS Code",
                    "untuk melihat keadaan bukti baris demi baris. Contoh Lean di atas belum",
                    "dijalankan saat materi ini ditulis karena Lean nggak terpasang di mesin",
                    "penulis; bentuknya mengikuti contoh di dokumentasi resmi.",
                    "",
                    "Beberapa kerabat yang akan kamu dengar namanya:",
                    "",
                    "  - Rocq (dulu bernama Coq) adalah asisten pembuktian yang lebih",
                    "    tua. Kompilator C CompCert dibuktikan benar memakai Rocq.",
                    "  - Agda dan Idris adalah bahasa dengan tipe dependen, yaitu tipe",
                    "    yang boleh bergantung pada nilai, misalnya \"list yang panjangnya",
                    "    tepat n\".",
                ],
            },
            {
                "heading": "Kapan logika dan bukti dipakai",
                "body": [
                    "Prolog cocok untuk masalah yang lebih mudah dijelaskan sebagai aturan",
                    "daripada sebagai langkah: sistem pakar, penjadwalan dengan banyak syarat,",
                    "teka-teki kombinatorik, dan pengolahan bahasa alami klasik. Datalog,",
                    "turunan Prolog yang lebih sederhana, dipakai di beberapa database dan alat",
                    "analisis kode untuk menulis query rekursif.",
                    "",
                    "Lean, Rocq, dan kawan-kawan dipakai ketika kesalahan mahal sekali:",
                    "kompilator, protokol kriptografi, dan pustaka matematika. Untuk pemula,",
                    "nilainya ada di cara berpikir: ada jarak besar antara \"sudah dites dengan",
                    "beberapa contoh\" dan \"terbukti benar untuk semua masukan\".",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pola Prolog muncul di tempat yang lebih dekat daripada dugaanmu. Pengecek",
                    "tipe di banyak kompilator memakai unifikasi untuk menebak tipe, persis",
                    "seperti Prolog mencocokkan kakek(budi, Cucu). Sistem rekomendasi berbasis",
                    "aturan dan pemeriksa kelayakan (misalnya \"boleh ambil mata kuliah ini",
                    "kalau sudah lulus prasyaratnya\") juga mudah ditulis sebagai fakta dan",
                    "aturan.",
                    "",
                    "Kasus kecil: bagian akademik punya daftar prasyarat mata kuliah dan ingin",
                    "tahu semua mata kuliah yang harus diambil sebelum Kecerdasan Buatan,",
                    "termasuk prasyarat dari prasyarat.",
                    "",
                    "Cara memecahkannya:",
                    "",
                    "  1. Tulis setiap prasyarat langsung sebagai fakta.",
                    "       prasyarat(ai, struktur_data).",
                    "       prasyarat(struktur_data, pemrograman_dasar).",
                    "  2. Tulis aturan rekursif seperti leluhur, dengan fakta diperiksa",
                    "     lebih dulu.",
                    "       butuh(A, B) :- prasyarat(A, B).",
                    "       butuh(A, C) :- prasyarat(A, B), butuh(B, C).",
                    "  3. Jalankan query butuh(ai, X) di swipl atau SWISH dan tekan",
                    "     titik koma sampai semua jawaban keluar.",
                    "  4. Tambah satu fakta baru dan pastikan jawabannya ikut bertambah",
                    "     tanpa mengubah aturan apa pun.",
                ],
            },
        ],
    },
    {
        "title": "32. Assembly: Register, Instruksi, dan Syscall",
        "sections": [
            {
                "body": [
                    "Assembly adalah bahasa yang paling dekat dengan isi CPU. Satu",
                    "baris assembly biasanya sama dengan satu instruksi mesin, yaitu",
                    "perintah paling kecil yang dimengerti prosesor: pindahkan angka",
                    "ini, tambahkan dua angka itu, lompat ke alamat sana.",
                    "",
                    "Program C, Rust, atau Go yang kamu tulis pada akhirnya juga",
                    "berubah jadi instruksi seperti itu. Bedanya, di assembly kamu",
                    "menulis instruksinya sendiri satu per satu. Nggak ada variabel",
                    "bernama, nggak ada if, nggak ada perulangan. Yang ada cuma",
                    "register, memori, dan lompatan.",
                    "",
                    "Hampir nggak ada yang menulis aplikasi utuh pakai assembly",
                    "sekarang. Yang sering terjadi, programmer perlu membaca",
                    "assembly: waktu melacak crash di program C, waktu mengecek",
                    "apakah compiler sudah mengoptimasi sebuah perulangan, atau waktu",
                    "membongkar program yang nggak ada kode sumbernya. Di Survei",
                    "Stack Overflow 2026, 7,2% responden bilang masih memakainya.",
                    "",
                    "Yang beda dari bahasa lain: assembly terikat pada jenis CPU.",
                    "Kode untuk x86-64 (prosesor Intel dan AMD di laptop dan",
                    "server) nggak bisa jalan di ARM64 (ponsel, Mac keluaran baru,",
                    "Raspberry Pi) atau RISC-V. Materi ini memakai x86-64 di Linux,",
                    "karena itulah yang dipakai mesin Fedora pada umumnya.",
                ],
            },
            {
                "heading": "Register: laci kecil di dalam CPU",
                "body": [
                    "Register adalah tempat penyimpanan super cepat di dalam CPU.",
                    "Jumlahnya sedikit, di x86-64 ada 16 register umum yang",
                    "masing-masing menampung 64 bit. Namanya rax, rbx, rcx, rdx,",
                    "rsi, rdi, rbp, rsp, lalu r8 sampai r15.",
                    "",
                    "Bayangkan meja kerja tukang kayu. Memori itu gudang besar di",
                    "belakang, register itu beberapa alat yang lagi dipegang di",
                    "tangan. Hampir semua hitungan cuma bisa dilakukan di register,",
                    "jadi data diambil dulu dari memori, diolah, lalu disimpan lagi.",
                    "",
                    "Satu register bisa dipakai sebagian. eax adalah 32 bit bawah",
                    "dari rax, ax 16 bit bawahnya, dan al 8 bit paling bawah. Kalau",
                    "kamu melihat eax di kode, itu biasanya tanda datanya int 32 bit.",
                    "",
                    "Instruksi yang paling sering muncul:",
                    "",
                    "  mov rax, 5      isi rax dengan 5",
                    "  add rax, rbx    rax = rax + rbx",
                    "  sub rax, 1      rax = rax - 1",
                    "  cmp rax, rbx    bandingkan, hasilnya disimpan di flag",
                    "  jmp label       lompat ke label",
                    "  je / jne label  lompat kalau sama / kalau tidak sama",
                    "",
                    "Flag adalah beberapa bit khusus yang mencatat hasil hitungan",
                    "terakhir, misalnya apakah hasilnya nol atau negatif. cmp",
                    "mengurangkan dua angka tanpa menyimpan hasilnya,",
                    "cuma menyetel flag. Lompatan bersyarat seperti jne lalu membaca",
                    "flag itu. Pasangan cmp dan lompatan itulah bahan dasar if dan",
                    "perulangan.",
                ],
            },
            {
                "heading": "Halo Dunia tanpa printf (halo.asm, sintaks NASM)",
                "bahasa": "assembly",
                "code": """section .data
    pesan   db "Halo, Dunia!", 10
    panjang equ $ - pesan

section .text
    global _start

_start:
    mov rax, 1          ; nomor syscall write
    mov rdi, 1          ; berkas 1 = stdout
    mov rsi, pesan      ; alamat teks
    mov rdx, panjang    ; banyaknya byte
    syscall

    mov rax, 60         ; nomor syscall exit
    xor rdi, rdi        ; kode keluar 0
    syscall""",
            },
            {
                "body": [
                    "Program ini nggak memakai pustaka apa pun, termasuk printf.",
                    "Ia langsung minta tolong ke kernel Linux lewat syscall.",
                    "Syscall adalah pintu resmi program untuk meminta sesuatu ke",
                    "sistem operasi: menulis ke layar, membuka berkas, atau selesai.",
                    "",
                    "Caranya: taruh nomor syscall di rax, isi argumennya di rdi,",
                    "rsi, dan rdx, lalu jalankan instruksi syscall. Di Linux x86-64,",
                    "write bernomor 1 dan exit bernomor 60.",
                    "",
                    "  section .data   bagian data: teks yang mau dicetak",
                    "  db              define byte, simpan byte apa adanya;",
                    "                  angka 10 di ujung adalah karakter baris baru",
                    "  equ $ - pesan   panjang teks dihitung assembler: posisi",
                    "                  sekarang dikurangi posisi awal pesan",
                    "  _start          titik mulai program, dicari linker",
                    "  xor rdi, rdi    cara singkat mengisi rdi dengan 0",
                    "",
                    "Panjang \"Halo, Dunia!\" ditambah baris baru adalah 13 byte, jadi",
                    "rdx berisi 13. Kalau rdx kamu isi 5, yang tercetak cuma \"Halo,\".",
                    "Kernel nggak membaca teksnya sampai ketemu tanda akhir. Ia",
                    "menulis persis sebanyak byte yang kamu minta.",
                ],
            },
            {
                "heading": "Merakit dan menjalankannya",
                "bahasa": "terminal",
                "code": """# versi NASM (nasm perlu dipasang: sudo dnf install nasm)
nasm -f elf64 halo.asm -o halo.o
ld halo.o -o halo
./halo

# versi GNU as, sudah ikut terpasang bersama gcc
gcc -nostdlib -static halo.s -o halo
./halo""",
            },
            {
                "heading": "Sintaks Intel dan AT&T (halo.s, GNU as)",
                "bahasa": "assembly",
                "code": "        .section .data\npesan:  .ascii \"Halo, Dunia!\\n\"\n        .set panjang, . - pesan\n\n        .section .text\n        .globl _start\n_start:\n        movq $1, %rax           # nomor syscall write\n        movq $1, %rdi           # berkas 1 = stdout\n        leaq pesan(%rip), %rsi  # alamat teks\n        movq $panjang, %rdx     # banyaknya byte\n        syscall\n\n        movq $60, %rax          # nomor syscall exit\n        xorq %rdi, %rdi         # kode keluar 0\n        syscall",
            },
            {
                "body": [
                    "Program di atas sama persis dengan versi NASM, cuma ditulis",
                    "dengan sintaks AT&T, bawaan assembler GNU as. Ada dua gaya",
                    "penulisan assembly x86, dan dua-duanya kamu bakal ketemu:",
                    "",
                    "  hal               Intel (NASM)     AT&T (GNU as)",
                    "  urutan operan     mov tujuan, asal movq asal, tujuan",
                    "  nama register     rax              %rax",
                    "  angka langsung    5                $5",
                    "  ukuran data       dari register    akhiran q, l, w, b",
                    "  komentar          ; ...            # ...",
                    "",
                    "Jebakan: urutan operannya terbalik. mov rax, 1 di Intel dan",
                    "movq $1, %rax di AT&T artinya sama, isi rax dengan 1. Kalau",
                    "kamu membaca kode AT&T dengan kebiasaan Intel, semua arah data",
                    "jadi kebalik dan programnya terasa nggak masuk akal.",
                    "",
                    "Dokumentasi Intel dan AMD, NASM, serta kebanyakan buku memakai",
                    "sintaks Intel. Keluaran gcc, objdump, dan gdb di Linux secara",
                    "bawaan memakai AT&T, tapi bisa diubah. Contoh berikutnya",
                    "memakai sintaks Intel lagi.",
                ],
            },
            {
                "heading": "Perulangan dari cmp dan jne (jumlah.asm)",
                "bahasa": "assembly",
                "code": """section .text
    global _start

_start:
    mov rbx, 0          ; total = 0
    mov rcx, 10         ; penghitung mulai dari 10

ulang:
    add rbx, rcx        ; total = total + penghitung
    dec rcx             ; penghitung dikurangi 1
    cmp rcx, 0          ; bandingkan penghitung dengan 0
    jne ulang           ; belum 0? lompat lagi ke ulang

    mov rax, 60         ; syscall exit
    mov rdi, rbx        ; kode keluar = total
    syscall""",
            },
            {
                "body": [
                    "Program ini menjumlahkan 10 + 9 + ... + 1. Label ulang cuma",
                    "nama untuk sebuah alamat. dec rcx mengurangi penghitung, cmp",
                    "membandingkannya dengan 0, dan jne melompat balik selama",
                    "hasilnya belum sama. Begitu rcx jadi 0, jne nggak melompat dan",
                    "program lanjut ke baris sesudahnya.",
                    "",
                    "Totalnya dikirim sebagai kode keluar program, karena mencetak",
                    "angka di assembly butuh puluhan baris untuk mengubah angka jadi",
                    "teks. Sesudah ./jumlah, perintah echo $? menampilkan 55.",
                    "",
                    "Ingat: kode keluar di Linux cuma 0 sampai 255. Total yang lebih",
                    "besar dari itu bakal terpotong, jadi cara ini cuma cocok untuk",
                    "eksperimen kecil.",
                ],
            },
            {
                "heading": "Melihat assembly buatan compiler",
                "code": "#include <stdio.h>\n\nint tambah(int a, int b) {\n    return a + b;\n}\n\nint main(void) {\n    printf(\"%d\\n\", tambah(40, 2));\n    return 0;\n}",
                "bahasa": "c",
            },
            {
                "body": [
                    "Keluaran:",
                    "  42",
                    "",
                    "Cara paling enak belajar membaca assembly adalah melihat hasil",
                    "compiler untuk kode yang sudah kamu pahami. Opsi -S menyuruh",
                    "gcc berhenti di tahap assembly dan menulis hasilnya ke berkas:",
                    "",
                    "  gcc -O1 -S -masm=intel tambah.c -o tambah.s",
                    "",
                    "Isi tambah.s untuk fungsi tambah, setelah baris direktif",
                    "dibuang (dihasilkan GCC 16 di Fedora 44):",
                    "",
                    "  tambah:",
                    "      lea     eax, [rdi+rsi]",
                    "      ret",
                    "",
                    "Dua baris saja. Argumen pertama datang lewat rdi, argumen kedua",
                    "lewat rsi, dan hasil dikembalikan lewat eax. Instruksi lea",
                    "aslinya untuk menghitung alamat, tapi compiler suka memakainya",
                    "sebagai penjumlahan cepat. Aturan siapa lewat register mana",
                    "disebut konvensi panggilan, dan dibahas di materi berikutnya.",
                    "",
                    "Coba ganti -O1 dengan -O0. Hasilnya jauh lebih panjang, karena",
                    "tanpa optimasi compiler menyimpan setiap variabel ke memori",
                    "dulu. Situs Compiler Explorer (godbolt.org) menampilkan hal yang",
                    "sama di browser, lengkap dengan warna yang menghubungkan tiap",
                    "baris C dengan instruksinya.",
                ],
            },
            {
                "heading": "ARM64, RISC-V, dan jebakan pemula",
                "body": [
                    "Konsepnya sama di arsitektur lain, nama dan aturannya beda.",
                    "ARM64 punya 31 register umum bernama x0 sampai x30, dan hampir",
                    "semua hitungan cuma boleh antar register. RISC-V adalah",
                    "arsitektur terbuka yang bebas dipakai siapa pun, register-nya",
                    "bernama x0 sampai x31 (x0 selalu bernilai nol). Nomor syscall",
                    "juga beda: di ARM64 Linux, write bernomor 64 dan exit 93.",
                    "",
                    "Jebakan: banyak tutorial lama memakai int 0x80 dengan register",
                    "eax dan ebx. Itu cara Linux 32 bit. Di program 64 bit, pakai",
                    "instruksi syscall dengan register 64 bit seperti contoh di atas.",
                    "",
                    "Satu lagi yang bikin kaget: assembly nggak punya pesan error",
                    "saat jalan. Alamat yang salah atau lupa memanggil exit langsung",
                    "berakhir dengan \"Segmentation fault\" tanpa keterangan baris.",
                    "Kalau itu terjadi, gdb adalah alat untuk melihat isi register",
                    "langkah demi langkah.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Assembly tulisan tangan masih ada di tempat yang butuh",
                    "kecepatan maksimal. Dekoder video AV1 dav1d, yang dipakai",
                    "browser dan pemutar video, punya ribuan baris assembly untuk",
                    "x86 dan ARM. Bootloader dan bagian awal kernel Linux juga",
                    "ditulis dengan assembly, karena saat itu belum ada stack untuk",
                    "menjalankan C. Yang lebih sering kamu alami: membaca keluaran",
                    "objdump atau gdb waktu mencari penyebab crash.",
                    "",
                    "Kasus kecil: temanmu membagikan program kecil tanpa kode",
                    "sumber. Hasil objdump -d -M intel menunjukkan potongan ini, dan",
                    "kamu diminta menebak apa yang dikerjakannya:",
                    "",
                    "  mov  eax, edi",
                    "  imul eax, edi",
                    "  add  eax, 1",
                    "  ret",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ingat konvensinya: argumen pertama datang lewat edi, hasil",
                    "     dikembalikan lewat eax.",
                    "  2. Ikuti isi eax baris demi baris. Mula-mula eax = x, lalu",
                    "     eax = x * x, lalu eax = x * x + 1.",
                    "  3. Tulis ulang dalam C supaya bisa diuji:",
                    "      int f(int x) { return x * x + 1; }",
                    "  4. Bandingkan dengan gcc -O1 -S -masm=intel. Kalau hasilnya",
                    "     mirip, tebakanmu kemungkinan besar benar.",
                ],
            },
        ],
    },
    {
        "title": "33. Assembly Lanjut: Stack, Fungsi, dan Konvensi Panggilan",
        "sections": [
            {
                "body": [
                    "Di materi sebelumnya semua instruksi jalan lurus dari atas ke",
                    "bawah. Program sungguhan penuh fungsi yang saling memanggil, dan",
                    "assembly nggak punya kata function. Yang ada cuma stack dan dua",
                    "instruksi: call dan ret.",
                    "",
                    "Stack di sini adalah satu area memori yang dipakai seperti",
                    "tumpukan piring. Register rsp (stack pointer) selalu menunjuk ke",
                    "piring paling atas. Di x86-64, stack tumbuh ke alamat yang lebih",
                    "kecil, jadi menaruh data berarti rsp dikurangi.",
                    "",
                    "  push rax   rsp dikurangi 8, lalu isi rax disalin ke [rsp]",
                    "  pop rax    isi [rsp] disalin ke rax, lalu rsp ditambah 8",
                    "  call f     push alamat instruksi sesudahnya, lalu lompat ke f",
                    "  ret        pop alamat itu, lalu lompat ke sana",
                    "",
                    "Alamat yang disimpan call disebut alamat balik. Dengan cara",
                    "itulah fungsi tahu harus kembali ke mana, walaupun dipanggil",
                    "dari seratus tempat berbeda.",
                ],
            },
            {
                "heading": "Fungsi kuadrat yang dipanggil dengan call (kuadrat.s)",
                "bahasa": "assembly",
                "code": """        .section .text
        .globl _start
_start:
        movq $7, %rdi           # argumen pertama: 7
        call kuadrat            # simpan alamat balik, lalu lompat
        movq %rax, %rdi         # hasil jadi kode keluar
        movq $60, %rax          # nomor syscall exit
        syscall

kuadrat:
        pushq %rbp              # simpan rbp milik pemanggil
        movq %rsp, %rbp         # rbp = awal stack frame baru
        movq %rdi, %rax         # salin argumen ke rax
        imulq %rdi, %rax        # rax = rax * rdi
        popq %rbp               # pulihkan rbp milik pemanggil
        ret                     # ambil alamat balik, lompat ke sana""",
            },
            {
                "heading": "Merakit dan melihat hasilnya",
                "bahasa": "terminal",
                "code": """gcc -nostdlib -static kuadrat.s -o kuadrat
./kuadrat
echo $?        # menampilkan 49""",
            },
            {
                "body": [
                    "Urutan kejadiannya:",
                    "  1. _start mengisi rdi dengan 7. rdi dipilih karena aturan",
                    "     di Linux bilang argumen pertama lewat rdi.",
                    "  2. call kuadrat menaruh alamat baris movq %rax, %rdi di",
                    "     stack, lalu lompat ke label kuadrat.",
                    "  3. kuadrat menyimpan rbp lama dengan pushq, lalu menjadikan",
                    "     rsp sekarang sebagai rbp baru. Dua baris ini disebut",
                    "     prolog, dan membuat satu stack frame.",
                    "  4. Hasil 49 ditaruh di rax, karena nilai balik selalu lewat",
                    "     rax.",
                    "  5. popq %rbp memulihkan rbp lama (epilog), lalu ret mengambil",
                    "     alamat balik dari stack dan melompat ke sana.",
                    "",
                    "Stack frame adalah potongan stack milik satu panggilan fungsi:",
                    "alamat balik, rbp milik pemanggil, dan variabel lokal. Setiap",
                    "panggilan dapat frame baru di atas frame pemanggilnya.",
                ],
            },
            {
                "heading": "Konvensi panggilan System V AMD64",
                "body": [
                    "Konvensi panggilan adalah kesepakatan antara fungsi pemanggil",
                    "dan fungsi yang dipanggil. Tanpa kesepakatan itu, fungsi buatan",
                    "gcc nggak bisa memanggil fungsi buatan compiler lain. Linux,",
                    "macOS, dan BSD di x86-64 memakai aturan bernama System V AMD64",
                    "ABI. Windows punya aturannya sendiri.",
                    "",
                    "  argumen bilangan bulat ke-1 s/d 6   rdi, rsi, rdx, rcx, r8, r9",
                    "  argumen ke-7 dan seterusnya          lewat stack",
                    "  argumen float                        xmm0 sampai xmm7",
                    "  nilai balik                          rax (float: xmm0)",
                    "  wajib dipulihkan fungsi yang dipanggil",
                    "                                       rbx, rbp, r12 s/d r15",
                    "  boleh dirusak fungsi yang dipanggil  rax, rcx, rdx, rsi, rdi,",
                    "                                       r8 s/d r11",
                    "",
                    "Ada satu aturan lagi yang sering dilupakan: tepat sebelum",
                    "instruksi call, rsp harus kelipatan 16. Kalau nggak, fungsi",
                    "pustaka seperti printf bisa crash di instruksi yang butuh data",
                    "rata 16 byte.",
                    "",
                    "Jebakan: kalau fungsi assembly buatanmu memakai rbx tanpa",
                    "menyimpannya dulu, fungsi C yang memanggilnya bisa rusak nilai",
                    "variabelnya. Error-nya muncul jauh dari tempat salahnya.",
                ],
            },
            {
                "heading": "Rekursi dan tumpukan frame (faktorial.c)",
                "bahasa": "c",
                "code": "#include <stdio.h>\n\nint faktorial(int n) {\n    printf(\"masuk faktorial(%d)\\n\", n);\n    int hasil = 1;\n    if (n > 1) {\n        hasil = n * faktorial(n - 1);\n    }\n    printf(\"keluar faktorial(%d) = %d\\n\", n, hasil);\n    return hasil;\n}\n\nint main(void) {\n    printf(\"hasil: %d\\n\", faktorial(3));\n    return 0;\n}",
            },
            {
                "body": [
                    "Keluaran:",
                    "  masuk faktorial(3)",
                    "  masuk faktorial(2)",
                    "  masuk faktorial(1)",
                    "  keluar faktorial(1) = 1",
                    "  keluar faktorial(2) = 2",
                    "  keluar faktorial(3) = 6",
                    "  hasil: 6",
                    "",
                    "Tiga panggilan faktorial masuk berurutan dan keluar dengan",
                    "urutan terbalik, persis tumpukan piring. Saat faktorial(1)",
                    "berjalan, ada empat frame di stack: main, faktorial(3),",
                    "faktorial(2), dan faktorial(1). Masing-masing punya n dan hasil",
                    "sendiri.",
                    "",
                    "Begini assembly yang dibuat gcc -O0 -S -masm=intel untuk",
                    "fungsi itu. Baris pemanggilan printf diganti ... supaya pendek:",
                ],
            },
            {
                "heading": "Assembly faktorial dari gcc -O0 (dipangkas)",
                "bahasa": "assembly",
                "code": """faktorial:
    push    rbp                     ; simpan rbp pemanggil
    mov     rbp, rsp                ; rbp = dasar frame ini
    sub     rsp, 32                 ; pesan 32 byte untuk variabel lokal
    mov     DWORD PTR [rbp-20], edi ; n disimpan di [rbp-20]
    ...                             ; printf("masuk ...")
    mov     DWORD PTR [rbp-4], 1    ; hasil = 1, di [rbp-4]
    cmp     DWORD PTR [rbp-20], 1   ; n dibandingkan dengan 1
    jle     .L2                     ; n <= 1? lewati rekursi
    mov     eax, DWORD PTR [rbp-20]
    sub     eax, 1
    mov     edi, eax                ; argumen: n - 1
    call    faktorial               ; frame baru di atas frame ini
    mov     edx, DWORD PTR [rbp-20]
    imul    eax, edx                ; hasil panggilan * n
    mov     DWORD PTR [rbp-4], eax
.L2:
    ...                             ; printf("keluar ...")
    mov     eax, DWORD PTR [rbp-4]  ; nilai balik lewat eax
    leave                           ; rsp = rbp, lalu pop rbp
    ret""",
            },
            {
                "body": [
                    "Perhatikan [rbp-20] dan [rbp-4]. Variabel lokal C nggak punya",
                    "nama di assembly. Mereka cuma posisi relatif terhadap rbp di",
                    "frame masing-masing. Karena tiap panggilan punya rbp sendiri,",
                    "n milik faktorial(3) dan n milik faktorial(2) nggak saling",
                    "timpa walaupun alamat relatifnya sama.",
                    "",
                    "Instruksi leave adalah singkatan dua langkah epilog: kembalikan",
                    "rsp ke rbp, lalu pop rbp.",
                ],
            },
            {
                "heading": "Assembly di dalam C (inline asm)",
                "bahasa": "c",
                "code": "#include <stdio.h>\n\nint main(void) {\n    long a = 7, b = 5, hasil;\n\n    __asm__(\"movq %1, %0\\n\\t\"\n            \"addq %2, %0\"\n            : \"=&r\"(hasil)\n            : \"r\"(a), \"r\"(b));\n\n    printf(\"%ld + %ld = %ld\\n\", a, b, hasil);\n    return 0;\n}",
            },
            {
                "body": [
                    "Keluaran:",
                    "  7 + 5 = 12",
                    "",
                    "GCC dan Clang bisa menyisipkan assembly langsung di tengah",
                    "kode C lewat __asm__. %0, %1, %2 diganti register yang dipilih",
                    "compiler untuk hasil, a, dan b. Bagian sesudah titik dua",
                    "pertama adalah keluaran (\"=&r\" artinya register yang ditulis),",
                    "bagian kedua masukan. Sintaksnya AT&T, bawaan GCC.",
                    "",
                    "Bentuk seperti ini yang paling sering kamu temui di proyek",
                    "nyata: beberapa baris di dalam fungsi C, bukan program utuh.",
                    "Kernel Linux memakainya untuk instruksi khusus yang nggak punya",
                    "padanan di C.",
                ],
            },
            {
                "heading": "Alat untuk membongkar program",
                "bahasa": "terminal",
                "code": """objdump -d -M intel ./kuadrat     # bongkar jadi assembly
gdb ./kuadrat
(gdb) break kuadrat               # berhenti di fungsi
(gdb) run
(gdb) info registers rdi rsp      # lihat isi register
(gdb) x/2gx $rsp                  # lihat 2 x 8 byte di stack
(gdb) stepi                       # maju satu instruksi""",
            },
            {
                "body": [
                    "objdump membaca berkas program dan menerjemahkan byte mesinnya",
                    "kembali jadi assembly. gdb menjalankan program sambil",
                    "memperlihatkan register dan memori. Saat berhenti di kuadrat,",
                    "x/2gx $rsp menampilkan alamat balik yang ditaruh call tadi.",
                    "",
                    "Untuk program yang lebih besar, orang memakai disassembler",
                    "grafis seperti Ghidra, buatan NSA yang dirilis sebagai open",
                    "source, yang bisa menebak bentuk kode C dari assembly-nya.",
                    "",
                    "Pengetahuan soal stack frame juga dasar keamanan. Serangan",
                    "buffer overflow klasik menulis lewat ujung array lokal sampai",
                    "menimpa alamat balik, sehingga ret melompat ke kode milik",
                    "penyerang. Pelindung seperti stack canary di GCC ada untuk",
                    "mendeteksi hal itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pustaka kriptografi seperti OpenSSL punya rutin assembly per",
                    "arsitektur untuk AES dan SHA, karena instruksi khusus CPU",
                    "bisa jauh lebih cepat daripada C biasa. Analis keamanan dan",
                    "pemain CTF (lomba keamanan siber) membaca stack frame di gdb",
                    "dan Ghidra hampir setiap hari.",
                    "",
                    "Kasus kecil: program C temanmu crash dengan \"stack smashing",
                    "detected\". Ia nggak paham artinya, padahal kodenya cuma",
                    "menyalin nama pengguna ke array char nama[8].",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami pesannya: GCC menaruh angka penjaga (canary) di",
                    "     frame, antara variabel lokal dan alamat balik. Kalau angka",
                    "     itu berubah saat fungsi selesai, program dihentikan.",
                    "  2. Artinya ada tulisan yang melewati ujung array lokal. Cari",
                    "     strcpy, gets, atau perulangan yang menulis ke nama.",
                    "  3. Pastikan dengan gdb: break di fungsi itu, cetak alamat",
                    "     nama dan isi stack dengan x/8gx $rsp sebelum dan sesudah",
                    "     penyalinan.",
                    "  4. Perbaiki dengan penyalinan yang tahu batas, misalnya",
                    "      snprintf(nama, sizeof nama, \"%s\", masukan);",
                ],
            },
        ],
    },
    {
        "title": "34. Zig: Alokator Eksplisit dan comptime",
        "sections": [
            {
                "body": [
                    "Zig adalah bahasa sistem yang ingin jadi pengganti C. Ia",
                    "dikompilasi jadi program asli seperti C, nggak punya garbage",
                    "collector, dan bisa memanggil kode C langsung. Yang dibuang",
                    "dari C adalah hal-hal yang sering bikin bingung: preprocessor",
                    "dengan makro, alokasi memori tersembunyi, dan error yang bisa",
                    "terlewat begitu saja lewat nilai balik -1.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026)",
                    "adalah 0.17.0, rilis 1 Oktober 2026. Fedora 44 mengemas 0.16.0",
                    "lewat sudo dnf install zig. Zig belum 1.0, dan itu berpengaruh",
                    "nyata: pustaka standarnya berubah hampir tiap rilis. Versi 0.15",
                    "merombak I/O, 0.16 memperkenalkan std.Io. Tutorial dari tahun",
                    "lalu sering gagal dikompilasi di versi sekarang.",
                    "",
                    "Di Survei Stack Overflow 2026, Zig dipakai 2,8% responden tapi",
                    "ingin dipakai 8,0%, hampir tiga kali lipatnya. Selisih seperti",
                    "itu biasanya tanda bahasa yang sedang naik.",
                ],
            },
            {
                "heading": "Halo Dunia (halo.zig)",
                "bahasa": "zig",
                "code": "const std = @import(\"std\");\n\npub fn main() void {\n    std.debug.print(\"Halo, {s}!\\n\", .{\"Dunia\"});\n}",
            },
            {
                "body": [
                    "Jalankan dengan zig run halo.zig. @import adalah fungsi bawaan",
                    "(semua fungsi bawaan diawali @), dan .{\"Dunia\"} adalah tuple",
                    "berisi argumen untuk {s}, penanda tempat teks.",
                    "",
                    "Jebakan: std.debug.print menulis ke stderr, bukan stdout.",
                    "Di terminal kelihatannya sama, tapi kalau keluarannya kamu",
                    "alihkan dengan > hasil.txt, berkas itu kosong. Contoh resmi",
                    "untuk stdout di versi 0.17 memakai std.Io.File.stdout() dan",
                    "parameter init milik main, yang lebih panjang.",
                ],
            },
            {
                "heading": "Alokator yang kelihatan (kuadrat.zig)",
                "bahasa": "zig",
                "code": "const std = @import(\"std\");\n\npub fn main(init: std.process.Init) !void {\n    const alokator = init.gpa;\n\n    const angka = try alokator.alloc(u32, 5);\n    defer alokator.free(angka);\n\n    for (angka, 0..) |*isi, i| {\n        isi.* = @intCast(i * i);\n    }\n    std.debug.print(\"{any}\\n\", .{angka});\n}",
            },
            {
                "body": [
                    "Keluarannya { 0, 1, 4, 9, 16 }.",
                    "",
                    "Di Zig, setiap fungsi yang butuh memori heap harus diberi",
                    "alokator lewat parameter. Alokator adalah objek yang tahu cara",
                    "meminta dan mengembalikan memori. Nggak ada fungsi malloc",
                    "global yang dipanggil tanpa sepengetahuanmu di dalam pustaka. Kalau sebuah",
                    "fungsi nggak menerima alokator, kamu bisa yakin ia nggak",
                    "mengalokasikan apa pun di heap.",
                    "",
                    "init.gpa adalah alokator umum yang disiapkan Zig untuk main.",
                    "Ada juga alokator lain untuk keperluan khusus, misalnya",
                    "ArenaAllocator yang membebaskan semuanya sekaligus di akhir,",
                    "atau FixedBufferAllocator yang cuma memakai array tetap.",
                    "",
                    "defer alokator.free(angka) artinya: jalankan baris ini waktu",
                    "keluar dari blok, apa pun penyebabnya. Pembebasan memori jadi",
                    "ditulis tepat di sebelah alokasinya, bukan di ujung fungsi yang",
                    "gampang terlewat.",
                ],
            },
            {
                "heading": "Lupa free? Zig memberi tahu",
                "bahasa": "zig",
                "code": "const std = @import(\"std\");\n\npub fn main(init: std.process.Init) !void {\n    const alokator = init.gpa;\n    const nama = try alokator.dupe(u8, \"budi\");\n    std.debug.print(\"halo {s}\\n\", .{nama});\n    // lupa: alokator.free(nama);\n}",
            },
            {
                "body": [
                    "Dalam mode Debug, alokator bawaan memeriksa kebocoran saat",
                    "program selesai. Keluarannya kira-kira begini (jalur berkas",
                    "dipangkas):",
                    "",
                    "  halo budi",
                    "  error(SafeAllocator): leaked [addr: ..., len: 4 ...]",
                    "  bocor.zig:5:35: ... in main (bocor.zig)",
                    "      const nama = try alokator.dupe(u8, \"budi\");",
                    "",
                    "Ia menunjuk baris tempat memori itu diminta. Di C, kebocoran",
                    "seperti ini baru ketahuan kalau kamu menjalankan alat terpisah",
                    "seperti Valgrind.",
                ],
            },
            {
                "heading": "Error union dan try (bagi.zig)",
                "bahasa": "zig",
                "code": "const std = @import(\"std\");\n\nconst GalatHitung = error{BagiNol};\n\nfn bagi(a: i32, b: i32) GalatHitung!i32 {\n    if (b == 0) return error.BagiNol;\n    return @divTrunc(a, b);\n}\n\nfn rataRata(total: i32, banyak: i32) GalatHitung!i32 {\n    const hasil = try bagi(total, banyak);\n    return hasil;\n}\n\npub fn main() void {\n    const a = rataRata(240, 3) catch 0;\n    std.debug.print(\"rata-rata: {d}\\n\", .{a});\n\n    if (rataRata(240, 0)) |nilai| {\n        std.debug.print(\"rata-rata: {d}\\n\", .{nilai});\n    } else |galat| {\n        std.debug.print(\"gagal: {s}\\n\", .{@errorName(galat)});\n    }\n}",
            },
            {
                "body": [
                    "Keluarannya:",
                    "",
                    "  rata-rata: 80",
                    "  gagal: BagiNol",
                    "",
                    "GalatHitung!i32 dibaca \"error union\": hasilnya bisa i32, bisa",
                    "juga salah satu error dari himpunan GalatHitung. Kamu nggak",
                    "bisa memakai hasilnya sebagai angka sebelum menangani",
                    "kemungkinan error-nya. Ada tiga cara menangani:",
                    "",
                    "  - try: kalau error, langsung kembalikan error itu ke",
                    "    pemanggil. Mirip ? di Rust.",
                    "  - catch nilai: kalau error, pakai nilai pengganti.",
                    "  - if (...) |nilai| ... else |galat| ...: tangani dua",
                    "    kemungkinan secara terpisah.",
                    "",
                    "Mengabaikan error yang mungkin terjadi adalah error kompilasi.",
                    "Bandingkan dengan C, tempat fungsi mengembalikan -1 atau NULL",
                    "dan kamu bebas lupa mengeceknya.",
                ],
            },
            {
                "heading": "errdefer: bersih-bersih hanya saat gagal",
                "bahasa": "zig",
                "code": "const std = @import(\"std\");\n\nconst Pengguna = struct {\n    nama: []u8,\n    skor: []u32,\n};\n\nfn buatPengguna(alokator: std.mem.Allocator, nama: []const u8) !Pengguna {\n    const salinan = try alokator.dupe(u8, nama);\n    errdefer alokator.free(salinan);\n\n    const skor = try alokator.alloc(u32, 3);\n    @memset(skor, 0);\n    return .{ .nama = salinan, .skor = skor };\n}\n\npub fn main(init: std.process.Init) !void {\n    const alokator = init.gpa;\n    const p = try buatPengguna(alokator, \"ani\");\n    defer alokator.free(p.nama);\n    defer alokator.free(p.skor);\n    std.debug.print(\"{s} {any}\\n\", .{ p.nama, p.skor });\n}",
            },
            {
                "body": [
                    "errdefer cuma dijalankan kalau fungsi keluar karena error.",
                    "Di buatPengguna, kalau alloc kedua gagal, salinan nama ikut",
                    "dibebaskan supaya nggak bocor. Kalau semua berhasil, salinan",
                    "itu dikembalikan ke pemanggil dan tanggung jawab membebaskannya",
                    "pindah ke sana (lihat dua defer di main). Keluarannya:",
                    "ani { 0, 0, 0 }.",
                ],
            },
            {
                "heading": "comptime: kode yang jalan saat kompilasi",
                "bahasa": "zig",
                "code": "const std = @import(\"std\");\n\nfn terbesar(comptime T: type, a: T, b: T) T {\n    return if (a > b) a else b;\n}\n\nfn fibonacci(n: u32) u64 {\n    var a: u64 = 0;\n    var b: u64 = 1;\n    for (0..n) |_| {\n        const c = a + b;\n        a = b;\n        b = c;\n    }\n    return a;\n}\n\npub fn main() void {\n    const fib50 = comptime fibonacci(50);\n    std.debug.print(\"{d} {d}\\n\", .{ terbesar(i32, -3, 8), terbesar(f64, 2.5, 1.5) });\n    std.debug.print(\"fib(50) = {d}\\n\", .{fib50});\n}",
            },
            {
                "body": [
                    "Keluarannya \"8 2.5\" lalu \"fib(50) = 12586269025\".",
                    "",
                    "comptime artinya nilai itu dihitung waktu kompilasi. fib(50)",
                    "di atas sudah jadi angka di dalam program sebelum programnya",
                    "dijalankan. Parameter comptime T: type membuat terbesar bisa",
                    "dipakai untuk tipe apa pun: begitulah Zig membuat generik, tanpa",
                    "sintaks khusus seperti template C++. Tipe di Zig adalah nilai",
                    "biasa yang bisa dioper ke fungsi, asal saat kompilasi.",
                    "",
                    "Zig juga membatasi hitungan comptime supaya kompilasi nggak",
                    "macet. Versi rekursif fibonacci(20) sempat ditolak dengan pesan",
                    "evaluation exceeded 1000 backwards branches. Batasnya bisa",
                    "dinaikkan dengan @setEvalBranchQuota.",
                ],
            },
            {
                "heading": "zig cc: kompilator C silang",
                "bahasa": "terminal",
                "code": """zig cc halo.c -o halo                        # seperti gcc
zig cc -target aarch64-linux-musl halo.c -o halo_arm
file halo_arm   # ELF 64-bit LSB executable, ARM aarch64""",
            },
            {
                "body": [
                    "Banyak orang memakai Zig tanpa menulis satu baris Zig pun. zig",
                    "cc membawa header dan pustaka C untuk banyak target, jadi dari",
                    "laptop x86-64 kamu bisa membuat program untuk ARM64 atau",
                    "Windows tanpa memasang toolchain silang terpisah.",
                    "",
                    "Perbandingan tiga bahasa sistem yang paling sering dibandingkan:",
                    "",
                    "  hal              C              Zig              Rust",
                    "  memori heap      malloc/free    alokator + defer kepemilikan",
                    "  error            kode -1/NULL   error union, try Result, ?",
                    "  generik          makro          comptime         trait",
                    "  pengaman memori  hampir nol     cek di mode Debug dicek compiler",
                    "  status           standar ISO    belum 1.0        stabil sejak 2015",
                    "",
                    "Rust mencegah kesalahan memori saat kompilasi, dengan harga",
                    "aturan kepemilikan yang perlu dipelajari. Zig memilih tetap",
                    "sederhana seperti C dan menangkap banyak kesalahan saat program",
                    "jalan di mode Debug.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Runtime JavaScript Bun, database keuangan TigerBeetle, dan",
                    "emulator terminal Ghostty ditulis dengan Zig. Banyak proyek C",
                    "dan Go juga memakai zig cc di skrip build-nya untuk membuat",
                    "rilis ke banyak sistem operasi sekaligus.",
                    "",
                    "Kasus kecil: kamu menyalin contoh Zig dari blog tahun lalu.",
                    "Saat dikompilasi dengan Zig 0.17, muncul error bahwa sebuah",
                    "fungsi di std nggak ada.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek versi yang kamu pakai dengan zig version, lalu cari",
                    "     tahu versi yang dipakai blog itu.",
                    "  2. Baca catatan rilis di ziglang.org untuk versi di antara",
                    "     keduanya. Bagian perubahan std biasanya menyebut nama lama",
                    "     dan penggantinya.",
                    "  3. Buka dokumentasi bahasa untuk versimu (langref) dan cari",
                    "     contoh yang setara, misalnya untuk menulis ke stdout.",
                    "  4. Untuk sekadar mencetak saat belajar, pakai yang paling",
                    "     jarang berubah:",
                    "      std.debug.print(\"{d}\\n\", .{nilai});",
                ],
            },
        ],
    },
    {
        "title": "35. Peta Bahasa Sistem Generasi Baru",
        "sections": [
            {
                "body": [
                    "Selain Zig dan Rust, ada belasan bahasa lain yang menawarkan",
                    "diri sebagai C yang lebih nyaman. Sebagian sudah dipakai di",
                    "produk nyata, sebagian masih eksperimen. Materi ini memetakan",
                    "sepuluh di antaranya supaya kamu bisa mengenali kodenya dan",
                    "menilai klaimnya dengan tenang.",
                    "",
                    "Pertanyaan yang dipakai untuk tiap bahasa sama: sudah 1.0 atau",
                    "belum, memorinya dibersihkan siapa, dan dipakai untuk apa.",
                    "Versi yang disebut adalah versi saat materi ini ditulis",
                    "(Oktober 2026). Kebanyakan bahasa ini belum ada di repo Fedora,",
                    "jadi cara memasangnya disebut di tiap bagian.",
                ],
            },
            {
                "heading": "Odin",
                "bahasa": "odin",
                "code": """package main

import "core:fmt"

main :: proc() {
    fmt.println("Halo, Dunia!")
}""",
            },
            {
                "body": [
                    "Odin adalah alternatif C yang dirancang untuk game dan grafis.",
                    "Paket raylib, SDL, dan Vulkan ikut di dalam distribusinya, jadi",
                    "membuat jendela grafis nggak perlu memasang pustaka terpisah.",
                    "Memorinya dikelola manual lewat alokator yang dioper secara",
                    "implisit lewat context. Alat simulasi api dan asap EmberGen",
                    "dari JangaFX ditulis dengan Odin.",
                    "",
                    "Odin belum 1.0. Rilisnya bulanan dan dinamai dev-tahun-bulan,",
                    "terbaru dev-2026-10. Lisensinya Zlib. Di Survei Stack Overflow",
                    "2026, Odin mencatat angka admired 82,4%, tapi pemakainya cuma",
                    "0,2% responden, jadi angka itu datang dari sampel yang kecil",
                    "sekali. Pasang dari halaman rilis GitHub odin-lang/Odin, lalu",
                    "jalankan dengan odin run . di foldernya.",
                ],
            },
            {
                "heading": "Nim",
                "bahasa": "nim",
                "code": "echo \"Halo, Dunia!\"",
            },
            {
                "body": [
                    "Nim bersintaks mirip Python (indentasi bermakna) tapi",
                    "dikompilasi ke C, C++, atau JavaScript, lalu ke program asli.",
                    "Sejak Nim 2.0, memori dikelola ORC: hitungan referensi",
                    "ditambah pengumpul siklus, jadi nggak ada jeda garbage",
                    "collector yang panjang. Klien Ethereum Nimbus ditulis dengan",
                    "Nim. Versi terbaru 2.2.12, lisensi MIT.",
                    "",
                    "Jebakan: nama di Nim nggak peka gaya. nama_var, namaVar, dan",
                    "namavar dianggap sama, kecuali huruf pertamanya. Paket Fedora",
                    "untuk Nim sudah pensiun, jadi pasang lewat choosenim atau",
                    "tarball resmi, lalu jalankan dengan nim r halo.nim.",
                ],
            },
            {
                "heading": "Crystal",
                "bahasa": "crystal",
                "code": "puts \"Halo, Dunia!\"",
            },
            {
                "body": [
                    "Crystal terlihat hampir sama dengan Ruby, tapi bertipe statis",
                    "dan dikompilasi. Tipenya ditebak compiler, jadi kamu jarang",
                    "menulisnya, dan nil diperiksa saat kompilasi: variabel bertipe",
                    "String? harus dicek dulu sebelum dipakai. Memori dibersihkan",
                    "garbage collector. Dipakai untuk backend web (Kemal, Lucky) dan",
                    "untuk layanan Ruby yang butuh lebih cepat.",
                    "",
                    "Versi terbaru 1.22.0 (Oktober 2026), lisensi Apache-2.0, rilis",
                    "minor tiap tiga bulan. Kompilasi proyek besar bisa lama.",
                    "Pasang dengan skrip resmi dari crystal-lang.org, jalankan",
                    "dengan crystal run halo.cr.",
                ],
            },
            {
                "heading": "V",
                "bahasa": "v",
                "code": """fn main() {
    println('Halo, Dunia!')
}""",
            },
            {
                "body": [
                    "V bergaya mirip Go dan mengklaim kompilasi yang cepat sekali dengan",
                    "hasil kecil. Versinya 0.5.2, masih jauh dari 1.0, dengan rilis",
                    "mingguan. Sejak awal, sebagian klaim fiturnya dikritik",
                    "komunitas karena diumumkan sebelum benar ada, dan API-nya masih",
                    "berubah cepat. Secara bawaan V memakai garbage collector; mode",
                    "autofree yang membebaskan memori otomatis tanpa GC masih",
                    "eksperimental. Cocok untuk dicoba, belum untuk proyek kerja.",
                    "Pasang dengan git clone github.com/vlang/v lalu make.",
                ],
            },
            {
                "heading": "D",
                "bahasa": "d",
                "code": """import std.stdio;

void main()
{
    writeln("Halo, Dunia!");
}""",
            },
            {
                "body": [
                    "D lahir sebagai C++ yang dirancang ulang. Ia sudah matang dan",
                    "stabil, dengan komunitas kecil. Memakai garbage collector",
                    "secara bawaan, tapi bisa dimatikan per fungsi dengan @nogc atau",
                    "untuk seluruh program dengan -betterC. Kompilatornya ada tiga:",
                    "DMD (acuan, versi 2.113.0, lisensi Boost), LDC berbasis LLVM,",
                    "dan GDC berbasis GCC. Di Fedora: sudo dnf install ldc, lalu",
                    "ldc2 halo.d && ./halo.",
                ],
            },
            {
                "heading": "Ada dan SPARK",
                "bahasa": "ada",
                "code": """with Ada.Text_IO;

procedure Halo is
begin
   Ada.Text_IO.Put_Line ("Halo, Dunia!");
end Halo;""",
            },
            {
                "body": [
                    "Ada dirancang untuk sistem yang nggak boleh gagal: avionik",
                    "pesawat, persinyalan kereta, satelit, dan perangkat medis.",
                    "Tipenya ketat sekali. Misalnya kamu bisa membuat tipe Persen",
                    "yang cuma menerima 0 sampai 100, dan nilai di luar itu ditolak.",
                    "Nggak ada garbage collector; memori dikelola lewat lingkup dan",
                    "storage pool. Standar terbarunya Ada 2022 (ISO/IEC 8652:2023).",
                    "",
                    "SPARK adalah bagian dari Ada yang bisa dibuktikan dengan alat",
                    "otomatis, misalnya dibuktikan nggak akan pernah membagi dengan",
                    "nol atau membaca di luar array. Kompilator GNAT ikut GCC; di",
                    "Fedora pasang gcc-gnat, simpan sebagai halo.adb (nama berkas",
                    "harus sama dengan nama prosedurnya), lalu gnatmake halo.adb.",
                ],
            },
            {
                "heading": "Mojo",
                "bahasa": "mojo",
                "code": """def main():
    print("Halo, Dunia!")""",
            },
            {
                "body": [
                    "Mojo dari perusahaan Modular bersintaks mirip Python tapi",
                    "dikompilasi dan bisa memprogram GPU NVIDIA dan AMD. Tujuannya",
                    "bagian AI yang butuh kecepatan, misalnya kernel perkalian",
                    "matriks. Mojo mencapai 1.0 pada 11 Agustus 2026, versi",
                    "terbarunya 1.1.0, dan kompilatornya dibuka sebagai open source",
                    "dengan lisensi Apache-2.0. Memorinya dikelola lewat aturan",
                    "kepemilikan, tanpa garbage collector.",
                    "",
                    "Jebakan: Mojo bukan superset Python penuh. Banyak artikel dan",
                    "video sebelum 1.0 memakai sintaks yang sudah berubah, jadi",
                    "rujuk dokumentasi 1.x. Pasang dengan uv pip install mojo atau",
                    "pixi add mojo, jalankan dengan mojo halo.mojo.",
                ],
            },
            {
                "heading": "Carbon (eksperimental)",
                "bahasa": "carbon",
                "code": """import Core library "io";

fn Run() {
  Core.Print(42);
}""",
            },
            {
                "body": [
                    "Carbon dimulai Google sebagai calon penerus C++ yang bisa",
                    "saling panggil dengan kode C++ lama. Proyeknya sendiri",
                    "menyatakan belum siap dipakai: milestone 0.1 belum tercapai dan",
                    "yang tersedia cuma toolchain nightly bernomor 0.0.0. Contoh",
                    "resmi di README-nya memang cuma mencetak angka 42 seperti di",
                    "atas. Pantau saja, jangan dipilih untuk proyek apa pun dulu.",
                ],
            },
            {
                "heading": "MoonBit (beta)",
                "bahasa": "moonbit",
                "code": """fn main {
  println("Halo, Dunia!")
}""",
            },
            {
                "body": [
                    "MoonBit adalah bahasa baru yang dirancang untuk WebAssembly",
                    "dan komputasi tepi, dengan toolchain terpadu bernama moon.",
                    "Targetnya wasm-gc, JavaScript, dan program asli. Versinya 0.9,",
                    "masih beta, jadi sintaks dan pustakanya bisa berubah. Pasang",
                    "dengan skrip dari cli.moonbitlang.com, buat proyek dengan moon",
                    "new halo, lalu moon run cmd/main.",
                ],
            },
            {
                "heading": "Forth",
                "bahasa": "forth",
                "code": """: halo  ." Halo, Dunia!" cr ;
halo
bye""",
            },
            {
                "body": [
                    "Forth adalah bahasa mungil dari tahun 1970-an yang",
                    "seluruhnya bekerja di atas stack. Angka ditaruh di stack, lalu",
                    "kata (sebutan Forth untuk fungsi) mengambil dan menaruh nilai",
                    "di sana. 2 3 + . artinya taruh 2, taruh 3, jumlahkan, cetak.",
                    "Kata baru dibuat dengan titik dua dan ditutup titik koma,",
                    "seperti halo di atas. Spasi wajib memisahkan setiap kata.",
                    "",
                    "Interpreter Forth bisa muat di beberapa kilobyte, makanya ia",
                    "dulu dipakai di firmware dan bootloader (Open Firmware) serta",
                    "sistem embedded yang mungil. Rilis stabil Gforth masih",
                    "0.7.3 dari 2014, pengembangan berlanjut lewat snapshot, dan",
                    "standarnya Forth-2012. Di Fedora: sudo dnf install gforth, lalu",
                    "gforth halo.fs. Latihan bab ini memintamu membuat Forth mini.",
                ],
            },
            {
                "heading": "Ringkasan: mana yang layak dipilih",
                "body": [
                    "  - Untuk proyek kerja yang harus dirawat bertahun-tahun: Ada",
                    "    di industri kritis keselamatan, D kalau timnya memang",
                    "    sudah memakainya. Keduanya stabil dan matang.",
                    "  - Untuk game dan grafis: Odin layak dicoba, dengan catatan",
                    "    belum 1.0.",
                    "  - Untuk kamu yang suka Python atau Ruby tapi butuh cepat: Nim",
                    "    dan Crystal sudah dipakai di produksi.",
                    "  - Untuk AI di GPU: Mojo, yang baru saja mencapai 1.0.",
                    "  - Untuk dipantau saja: V, Carbon, dan MoonBit.",
                    "  - Untuk wawasan: Forth, yang mengajarkan cara kerja mesin",
                    "    stack.",
                    "",
                    "Ingat: klaim di halaman depan sebuah bahasa adalah pemasaran.",
                    "Cek tiga hal sebelum percaya: sudah 1.0 atau belum, kapan rilis",
                    "terakhirnya, dan adakah produk nyata yang memakainya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pilihan bahasa sistem di dunia kerja jarang soal mana yang",
                    "paling keren. Klien Ethereum Nimbus memilih Nim, EmberGen",
                    "memilih Odin, dan proyek avionik memilih Ada karena alat",
                    "sertifikasinya tersedia. Yang menentukan biasanya kematangan,",
                    "pustaka, dan orang yang bisa merawatnya.",
                    "",
                    "Kasus kecil: teman satu tim PKL mengusulkan menulis ulang alat",
                    "baris perintah kantor dengan V, karena ia membaca klaim bahwa",
                    "V lebih cepat dan lebih aman daripada Go.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek status: V masih 0.5.x, belum 1.0, dan API-nya berubah",
                    "     cepat. Alat kantor perlu dirawat orang lain nanti.",
                    "  2. Cek siapa yang memakainya di produksi. Bandingkan dengan Go",
                    "     yang sudah dipakai luas dan punya kurikulum di aplikasi ini.",
                    "  3. Ukur sendiri kalau kecepatan memang masalah: tulis bagian",
                    "     yang lambat di dua bahasa, lalu bandingkan dengan perintah",
                    "     time.",
                    "  4. Tulis hasilnya sebagai catatan singkat untuk tim: bahasa,",
                    "     versi, risiko, dan keputusan.",
                ],
            },
        ],
    },
    {
        "title": "36. COBOL: Bahasa Transaksi yang Masih Bekerja",
        "sections": [
            {
                "body": [
                    "COBOL (Common Business-Oriented Language) lahir tahun 1959",
                    "untuk satu tujuan: mengolah data bisnis. Gaji, tagihan, saldo",
                    "rekening, premi asuransi. Kodenya sengaja dibuat mirip kalimat",
                    "bahasa Inggris, supaya manajer bisa ikut membaca.",
                    "",
                    "Lebih dari 60 tahun kemudian, COBOL masih menjalankan banyak",
                    "sistem inti bank, asuransi, dan pemerintahan. Biasanya di",
                    "mainframe, yaitu komputer besar milik IBM yang dirancang untuk",
                    "memproses jutaan transaksi tanpa berhenti. Di Survei Stack",
                    "Overflow 2026 pemakainya cuma 1,1%, tapi di indeks TIOBE",
                    "Oktober 2026 COBOL ada di peringkat 16. Kodenya banyak, orang",
                    "yang menguasainya makin sedikit.",
                    "",
                    "Bahasanya masih dirawat. Standar terbarunya ISO/IEC 1989:2023.",
                    "Untuk belajar di Fedora ada GnuCOBOL 3.2, kompilator bebas yang",
                    "menerjemahkan COBOL ke C lalu mengompilasinya dengan gcc.",
                ],
            },
            {
                "heading": "Halo Dunia (halo.cob)",
                "bahasa": "cobol",
                "code": """       IDENTIFICATION DIVISION.
       PROGRAM-ID. HALO.
       PROCEDURE DIVISION.
           DISPLAY "Halo, Dunia!".
           STOP RUN.""",
            },
            {
                "body": [
                    "Perhatikan spasi di depan setiap baris. COBOL klasik memakai",
                    "format kolom tetap, warisan zaman kartu berlubang yang lebarnya",
                    "80 kolom:",
                    "",
                    "  kolom 1-6     nomor urut (dulu untuk mengurutkan kartu)",
                    "  kolom 7       penanda: * berarti baris komentar",
                    "  kolom 8-11    area A: nama DIVISION, SECTION, paragraf, 01",
                    "  kolom 12-72   area B: pernyataan biasa",
                    "",
                    "Jadi judul divisi di contoh tadi mulai di kolom 8, dan perintah",
                    "mencetaknya mulai di kolom 12. Salah kolom berarti error",
                    "kompilasi. GnuCOBOL juga menerima format bebas lewat opsi -free,",
                    "tapi kode di mainframe hampir selalu format tetap.",
                    "",
                    "Setiap program COBOL dibagi jadi empat divisi, selalu dengan",
                    "urutan yang sama:",
                    "",
                    "  IDENTIFICATION   nama program (PROGRAM-ID)",
                    "  ENVIRONMENT      berkas dan perangkat yang dipakai",
                    "  DATA             semua variabel dan bentuk record",
                    "  PROCEDURE        langkah-langkah yang dijalankan",
                    "",
                    "Halo Dunia di atas cuma butuh dua. Program sungguhan hampir",
                    "selalu punya keempatnya.",
                ],
            },
            {
                "heading": "Menjalankan di Fedora",
                "bahasa": "terminal",
                "code": """sudo dnf install gnucobol
cobc -x -Wall halo.cob   # -x: buat program, -Wall: semua peringatan
./halo""",
            },
            {
                "heading": "PIC: bentuk data ditulis di depan",
                "bahasa": "cobol",
                "code": """       IDENTIFICATION DIVISION.
       PROGRAM-ID. BUNGA.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 SALDO         PIC 9(7)V99 VALUE 1500000.00.
       01 PERSEN        PIC 9V99    VALUE 2.50.
       01 BUNGA         PIC 9(7)V99.
       01 TAMPIL        PIC Z,ZZZ,ZZ9.99.
       01 KECIL         PIC 9(5).
       PROCEDURE DIVISION.
           COMPUTE BUNGA ROUNDED = SALDO * PERSEN / 100.
           DISPLAY "Bunga mentah: " BUNGA.
           MOVE BUNGA TO TAMPIL.
           DISPLAY "Bunga: " TAMPIL.
           ADD BUNGA TO SALDO.
           MOVE SALDO TO TAMPIL.
           DISPLAY "Saldo baru: " TAMPIL.
           MOVE 1234567 TO KECIL.
           DISPLAY "KECIL: " KECIL.
           STOP RUN.""",
            },
            {
                "body": [
                    "Keluaran (GnuCOBOL 3.2):",
                    "",
                    "  Bunga mentah: 0037500.00",
                    "  Bunga:    37,500.00",
                    "  Saldo baru: 1,537,500.00",
                    "  KECIL: 34567",
                    "",
                    "Picture, biasa disingkat PIC, adalah cetakan bentuk sebuah data.",
                    "Setiap huruf di dalamnya mewakili satu posisi:",
                    "",
                    "  9           satu digit angka",
                    "  X           satu karakter apa saja",
                    "  V           titik desimal tersirat, nggak memakan tempat",
                    "  S           angka bertanda (boleh negatif)",
                    "  Z           digit yang diganti spasi kalau nol di depan",
                    "  9(7)        singkatan dari 9999999",
                    "",
                    "Jadi 9(7)V99 artinya tujuh digit sebelum koma dan dua sesudahnya,",
                    "disimpan sebagai sembilan digit. Field bertanda V dihitung tepat",
                    "sampai sen, tanpa pembulatan biner seperti float. Bentuk",
                    "Z,ZZZ,ZZ9.99 adalah picture tampilan: koma dan titik ikut dicetak,",
                    "dan nol di depan diganti spasi. Makanya \"Bunga:\" diikuti beberapa",
                    "spasi.",
                    "",
                    "Jebakan: baris terakhir memindahkan 1234567 ke field 9(5), dan",
                    "hasilnya 34567. Digit paling kiri dibuang. Untuk angka yang",
                    "ditulis langsung seperti ini, cobc -Wall memberi peringatan",
                    "value size exceeds data size. Tapi kalau angkanya datang dari",
                    "variabel atau hasil hitungan, pemotongan terjadi saat program",
                    "jalan tanpa peringatan apa pun. Di sistem gaji, itu berarti",
                    "angka jutaan hilang begitu saja, jadi programmer COBOL selalu",
                    "mengecek lebar picture setiap kali memindahkan angka.",
                ],
            },
            {
                "heading": "Record dan copybook (rekening.cob)",
                "bahasa": "cobol",
                "code": """       IDENTIFICATION DIVISION.
       PROGRAM-ID. REKENING.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 REKENING.
          05 NO-REK     PIC 9(6).
          05 NAMA       PIC X(10).
          05 SALDO      PIC 9(7)V99.
       01 TAMPIL        PIC Z,ZZZ,ZZ9.99.
       PROCEDURE DIVISION.
           MOVE "000123BUDI      001234567" TO REKENING.
           MOVE SALDO TO TAMPIL.
           DISPLAY NO-REK " [" NAMA "] " TAMPIL.
           IF SALDO > 10000
               DISPLAY "saldo di atas 10 ribu"
           ELSE
               DISPLAY "saldo kecil"
           END-IF.
           STOP RUN.""",
            },
            {
                "body": [
                    "Keluaran:",
                    "",
                    "  000123 [BUDI      ]    12,345.67",
                    "  saldo di atas 10 ribu",
                    "",
                    "Angka 01 dan 05 di depan nama adalah nomor level. Level 01",
                    "adalah record utuh, level 05 adalah bagian-bagiannya. Record",
                    "rekening berisi 6 + 10 + 9 = 25 karakter. Satu perintah move",
                    "mengisi semuanya sekaligus. Enam karakter pertama jadi nomor",
                    "rekening, sepuluh berikutnya jadi nama (lengkap dengan spasinya),",
                    "dan sisanya jadi saldo.",
                    "",
                    "Begitulah data di mainframe disimpan: baris dengan lebar tetap,",
                    "tanpa pemisah koma. Bentuk record seperti ini biasanya disimpan",
                    "di berkas terpisah bernama copybook, lalu dipakai banyak program",
                    "lewat pernyataan copy. Kalau satu field berubah lebar, semua",
                    "program yang memakai copybook itu harus dikompilasi ulang.",
                    "",
                    "Jebakan: titik mengakhiri satu kalimat COBOL, dan titik juga",
                    "menutup semua if yang masih terbuka. Kode lama yang belum memakai",
                    "penutup end-if sering punya bug karena titik yang salah tempat.",
                    "Biasakan menutup setiap if dengan end-if seperti contoh di atas.",
                ],
            },
            {
                "heading": "Kenapa bank masih memakainya",
                "body": [
                    "Ada beberapa alasan yang saling menguatkan:",
                    "",
                    "  - Hitungan desimal tetap. Uang harus tepat sampai sen, dan",
                    "    COBOL menghitung desimal langsung, bukan lewat float biner.",
                    "  - Kode yang sudah teruji puluhan tahun. Aturan bisnis yang",
                    "    tertanam di jutaan baris itu sering nggak tercatat di",
                    "    dokumen mana pun selain kodenya sendiri.",
                    "  - Mainframe IBM z/OS memang dibuat untuk volume transaksi",
                    "    besar, dengan CICS untuk transaksi online (misalnya cek",
                    "    saldo dari ATM) dan job batch malam hari untuk proses",
                    "    seperti bunga dan gajian.",
                    "  - Menulis ulang itu mahal dan berisiko. Proyek migrasi yang",
                    "    gagal bisa menghentikan layanan bank berhari-hari.",
                    "",
                    "Saat pandemi April 2020, beberapa negara bagian Amerika",
                    "Serikat, termasuk New Jersey, terbuka meminta bantuan programmer",
                    "COBOL karena sistem tunjangan pengangguran mereka kewalahan.",
                    "",
                    "Masalah desimal itu bisa kamu lihat sendiri di Python. Modul",
                    "decimal bekerja seperti 9(7)V99, float nggak:",
                ],
            },
            {
                "heading": "Padanan di Python",
                "code": """from decimal import Decimal, ROUND_HALF_UP

saldo = Decimal("1500000.00")
persen = Decimal("2.50")
bunga = (saldo * persen / 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print("Bunga:", f"{bunga:,.2f}")
saldo += bunga
print("Saldo baru:", f"{saldo:,.2f}")
print("Kalau pakai float:", 0.1 + 0.2)""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Bunga: 37,500.00",
                    "  Saldo baru: 1,537,500.00",
                    "  Kalau pakai float: 0.30000000000000004",
                ],
            },
            {
                "heading": "JCL: cara mainframe menjalankan program",
                "bahasa": "jcl",
                "code": """//GAJIAN   JOB (AKUN),'HITUNG GAJI',CLASS=A,MSGCLASS=X
//LANGKAH1 EXEC PGM=GAJI01
//MASUK    DD DSN=HR.KARYAWAN.DATA,DISP=SHR
//KELUAR   DD DSN=HR.SLIP.BULANINI,DISP=(NEW,CATLG),
//            SPACE=(TRK,(10,5))
//SYSOUT   DD SYSOUT=*""",
            },
            {
                "body": [
                    "Di mainframe, program batch nggak dijalankan dengan mengetik",
                    "namanya. Ia dijalankan lewat JCL (Job Control Language), naskah",
                    "yang bilang program mana yang dijalankan dan berkas mana yang jadi",
                    "masukan serta keluarannya. Setiap barisnya diawali //. Kamu cukup",
                    "bisa membacanya. Menulis JCL biasanya pekerjaan tim operasi",
                    "mainframe.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Sistem inti bank, pemrosesan kartu, asuransi, dan penggajian",
                    "di banyak negara masih berjalan di mainframe dengan COBOL. IBM",
                    "masih menjual kompilatornya untuk z/OS, dan pekerjaan merawat",
                    "atau memigrasikan kode lama itu ditawarkan banyak perusahaan",
                    "konsultan TI.",
                    "",
                    "Kasus kecil: kamu menerima berkas teks hasil ekspor mainframe",
                    "dan copybook berikut. Atasan minta total saldo dihitung di",
                    "Python, tanpa mengubah sistem lamanya.",
                    "",
                    "  05 NO-REK   PIC 9(6).",
                    "  05 NAMA     PIC X(10).",
                    "  05 SALDO    PIC 9(7)V99.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung posisi tiap field dari picture-nya: nomor rekening",
                    "     kolom 0-5, nama 6-15, saldo 16-24. Satu baris pasti 25 karakter.",
                    "  2. Potong tiap baris dengan slice, misalnya baris[16:25] untuk",
                    "     saldo. Jangan memakai split, karena nama bisa berisi spasi.",
                    "  3. Ingat V: \"001234567\" artinya 12345.67. Bagi dengan 100",
                    "     memakai Decimal, bukan float:",
                    "      saldo = Decimal(baris[16:25]) / 100",
                    "  4. Tolak baris yang panjangnya bukan 25 atau field angkanya",
                    "     bukan digit, dan laporkan nomor barisnya. Latihan bab ini",
                    "     memintamu membuat persis ini.",
                ],
            },
        ],
    },
    {
        "title": "37. VBA: Makro untuk Excel dan Office",
        "sections": [
            {
                "body": [
                    "VBA (Visual Basic for Applications) adalah bahasa makro yang",
                    "tertanam di Microsoft Office. Makro adalah rekaman langkah atau",
                    "program kecil yang mengerjakan tugas berulang untukmu: merapikan",
                    "laporan, menjumlahkan kolom, mengirim email dari daftar di",
                    "Excel.",
                    "",
                    "Kalau kamu PKL di kantor, kemungkinan besar kamu bakal ketemu",
                    "berkas .xlsm warisan pegawai lama yang \"ada tombolnya\". Tombol",
                    "itu menjalankan VBA. Di Survei Stack Overflow 2026, 3,9%",
                    "responden masih memakai VBA, walaupun cuma 20,1% yang senang",
                    "memakainya.",
                    "",
                    "Versinya VBA 7.1, dipakai sejak Office 2010 sampai Microsoft",
                    "365 sekarang. VBA cuma jalan di Office desktop untuk Windows",
                    "dan macOS. Excel versi web nggak menjalankan VBA, dan di Fedora",
                    "nggak ada VBA. Yang terdekat adalah LibreOffice Basic, mirip",
                    "tapi nggak sepenuhnya kompatibel.",
                ],
            },
            {
                "heading": "Halo Dunia",
                "bahasa": "vba",
                "code": """Sub HaloDunia()
    MsgBox "Halo, Dunia!"
End Sub""",
            },
            {
                "body": [
                    "Cara membuatnya di Excel: tekan Alt+F11 untuk membuka editor",
                    "VBA, pilih Insert lalu Module, tempel kodenya, lalu tekan F5.",
                    "Sebuah kotak pesan muncul.",
                    "",
                    "Sub adalah prosedur, yaitu kumpulan langkah tanpa nilai balik.",
                    "Function mirip Sub tapi mengembalikan nilai, dan bisa dipakai",
                    "di sel seperti rumus bawaan. Berkas yang berisi makro harus",
                    "disimpan sebagai .xlsm. Kalau disimpan sebagai .xlsx, makronya",
                    "dibuang.",
                ],
            },
            {
                "heading": "Model objek: Application sampai Range",
                "body": [
                    "Semua yang ada di Excel adalah objek yang bersarang:",
                    "",
                    "  Application              Excel itu sendiri",
                    "    Workbooks(\"lap.xlsm\")  satu berkas yang terbuka",
                    "      Worksheets(\"Data\")   satu lembar kerja",
                    "        Range(\"B2:B5\")     sekumpulan sel",
                    "        Cells(2, 2)        satu sel: baris 2, kolom 2 (B2)",
                    "",
                    "Range memakai alamat gaya A1 seperti di rumus. Cells memakai",
                    "angka baris dan kolom, jadi lebih enak dipakai di perulangan.",
                    "Cells(3, 28) sama dengan Range(\"AB3\"), karena kolom ke-27",
                    "adalah AA dan ke-28 adalah AB.",
                    "",
                    "Jebakan: kalau kamu menulis Range(\"B2\") tanpa menyebut lembar",
                    "kerjanya, VBA memakai lembar yang sedang aktif. Makro yang",
                    "jalan benar di komputermu bisa menulis ke lembar yang salah",
                    "kalau pemakainya kebetulan sedang membuka lembar lain. Sebut",
                    "lembarnya dengan jelas, seperti contoh berikut.",
                ],
            },
            {
                "heading": "Menjumlahkan kolom sampai baris terakhir",
                "bahasa": "vba",
                "code": """Sub HitungTotal()
    Dim ws As Worksheet
    Dim baris As Long, terakhir As Long
    Dim total As Double

    Set ws = ThisWorkbook.Worksheets("Data")
    terakhir = ws.Cells(ws.Rows.Count, "B").End(xlUp).Row

    For baris = 2 To terakhir
        If IsNumeric(ws.Cells(baris, 2).Value) Then
            total = total + ws.Cells(baris, 2).Value
        End If
    Next baris

    ws.Range("B" & terakhir + 1).Value = total
    ws.Range("A" & terakhir + 1).Value = "Total"
End Sub""",
            },
            {
                "body": [
                    "Baris yang paling sering kamu temui di makro warisan adalah",
                    "pencari baris terakhir:",
                    "",
                    "  ws.Cells(ws.Rows.Count, \"B\").End(xlUp).Row",
                    "",
                    "Artinya: mulai dari sel paling bawah kolom B, lalu lompat ke",
                    "atas sampai ketemu sel berisi, seperti menekan Ctrl+Panah Atas.",
                    "Dengan begitu makro tetap benar walaupun datanya bertambah.",
                    "",
                    "Dim mendeklarasikan variabel. Tipe yang umum: Long untuk",
                    "bilangan bulat, Double untuk pecahan, String untuk teks, dan",
                    "Worksheet untuk objek. Objek diisi dengan Set, bukan sama dengan",
                    "biasa. Lupa Set adalah error yang hampir pasti dialami pemula.",
                    "Tambahkan Option Explicit di baris paling atas modul supaya",
                    "variabel yang salah ketik langsung ketahuan.",
                ],
            },
            {
                "heading": "Function yang bisa dipakai di sel",
                "bahasa": "vba",
                "code": """Function Diskon(harga As Double, persen As Double) As Double
    If persen < 0 Or persen > 100 Then
        Diskon = CVErr(xlErrValue)
        Exit Function
    End If
    Diskon = harga * (1 - persen / 100)
End Function""",
            },
            {
                "body": [
                    "Sesudah fungsi ini ada di modul, kamu bisa menulis",
                    "=Diskon(A2; 15) di sel mana pun (pemisahnya koma atau titik koma,",
                    "tergantung pengaturan bahasa Excel). Fungsi buatan seperti ini",
                    "disebut UDF (user-defined function). CVErr(xlErrValue) membuat",
                    "sel menampilkan #VALUE!, sama seperti rumus bawaan yang diberi",
                    "masukan salah.",
                ],
            },
            {
                "heading": "Menangani error dengan On Error",
                "bahasa": "vba",
                "code": "Sub BukaLaporan()\n    On Error GoTo Gagal\n    Workbooks.Open \"C:\\Laporan\\penjualan.xlsx\"\n    Application.ScreenUpdating = False\n    ' ... olah data di sini ...\n    Application.ScreenUpdating = True\n    Exit Sub\nGagal:\n    Application.ScreenUpdating = True\n    MsgBox \"Gagal membuka laporan: \" & Err.Description\nEnd Sub",
            },
            {
                "body": [
                    "VBA nggak punya try/catch. Polanya On Error GoTo label: kalau",
                    "terjadi error, lompat ke label itu. Exit Sub sebelum label",
                    "penting, supaya baris penanganan error nggak ikut jalan saat",
                    "semuanya lancar.",
                    "",
                    "Jebakan: On Error Resume Next menyuruh VBA mengabaikan semua",
                    "error dan lanjut ke baris berikutnya. Makro warisan sering",
                    "memakainya di baris paling atas, sehingga kesalahan apa pun",
                    "lewat tanpa jejak dan hasilnya salah tanpa ada yang tahu.",
                ],
            },
            {
                "heading": "Keamanan makro dan penggantinya",
                "body": [
                    "Makro bisa menjalankan apa saja dengan hak pemakainya,",
                    "termasuk mengunduh dan menjalankan program lain. Karena itu",
                    "lampiran dokumen bermakro jadi jalur malware klasik. Sejak 2022,",
                    "Office memblokir makro secara bawaan untuk berkas yang diunduh",
                    "dari internet. Pemakai harus membuka Properties berkas itu dan",
                    "mencentang Unblock, atau menaruhnya di lokasi tepercaya.",
                    "",
                    "Microsoft sekarang mendorong dua pengganti:",
                    "",
                    "  - Office Scripts: skrip TypeScript yang jalan di Excel web",
                    "    dan desktop, disimpan di cloud.",
                    "  - Power Automate: alur otomasi lintas aplikasi (Excel,",
                    "    Outlook, SharePoint) yang disusun lewat antarmuka visual.",
                    "",
                    "VBA belum diumumkan akan dihapus dari Office desktop, tapi",
                    "fitur baru masuk ke dua jalur itu. Untuk mengolah data besar di",
                    "luar Excel, Python dengan modul csv sudah cukup. Logika makro",
                    "HitungTotal tadi kalau ditulis ulang di Python:",
                ],
            },
            {
                "heading": "Padanan di Python",
                "code": "import csv\nimport io\n\ndata = \"\"\"Barang,Jumlah\nPulpen,12500\nBuku,30000\nMap,2500\n\"\"\"\nbaris = list(csv.reader(io.StringIO(data)))\ntotal = 0\nfor nama, jumlah in baris[1:]:\n    total += int(jumlah)\nprint(\"Total:\", total)",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Total: 45000",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Bagian keuangan, gudang, dan HR di banyak kantor punya berkas",
                    "Excel bermakro untuk rekap bulanan: menggabungkan lembar dari",
                    "beberapa cabang, membuat laporan, lalu mengirimnya lewat",
                    "Outlook. Makro itu biasanya ditulis satu orang bertahun-tahun",
                    "lalu, dan nggak ada dokumentasinya.",
                    "",
                    "Kasus kecil: makro rekap penjualan di kantor tempatmu PKL",
                    "tiba-tiba menulis total ke lembar Grafik, padahal mestinya ke",
                    "lembar Data. Nggak ada pesan error sama sekali.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buka editor dengan Alt+F11 dan cari Range atau Cells yang",
                    "     dipakai tanpa nama lembar di depannya.",
                    "  2. Cek apakah ada On Error Resume Next di atas. Kalau ada,",
                    "     matikan sementara supaya error yang tersembunyi muncul.",
                    "  3. Ganti akses tanpa lembar dengan lembar yang disebut jelas:",
                    "      Set ws = ThisWorkbook.Worksheets(\"Data\")",
                    "      ws.Range(\"B\" & terakhir + 1).Value = total",
                    "  4. Jalankan langkah demi langkah dengan F8 sambil melihat",
                    "     jendela Locals, lalu simpan sebagai .xlsm dan catat",
                    "     perubahannya untuk orang berikutnya.",
                ],
            },
        ],
    },
    {
        "title": "38. Peta Bahasa Enterprise: ABAP, Apex, X++, RPG, PL/I",
        "sections": [
            {
                "body": [
                    "Perusahaan besar jarang membuat aplikasi akuntansi atau",
                    "penjualan dari nol. Mereka membeli sistem ERP (Enterprise",
                    "Resource Planning, sistem yang mengurus keuangan, gudang,",
                    "pembelian, dan SDM sekaligus) atau CRM (Customer Relationship",
                    "Management, sistem pengelola data pelanggan dan penjualan).",
                    "Lalu sistem itu disesuaikan dengan cara kerja perusahaan.",
                    "",
                    "Penyesuaian itu ditulis dengan bahasa milik vendornya. Materi",
                    "ini memetakan lima bahasa yang paling mungkin kamu temui:",
                    "ABAP untuk SAP, Apex untuk Salesforce, X++ untuk Microsoft",
                    "Dynamics 365, RPG untuk IBM i, dan PL/I di mainframe. Semuanya",
                    "nggak bisa dipasang di Fedora seperti bahasa biasa. Kodenya",
                    "jalan di server vendor, jadi cara belajarnya lewat akun uji",
                    "coba gratis.",
                ],
            },
            {
                "heading": "ABAP (SAP), gaya klasik",
                "bahasa": "abap",
                "code": """REPORT zlaporan_pelanggan.

DATA lt_pelanggan TYPE STANDARD TABLE OF kna1.

SELECT kunnr, name1, ort01
  FROM kna1
  WHERE land1 = 'ID'
  INTO CORRESPONDING FIELDS OF TABLE @lt_pelanggan
  UP TO 10 ROWS.

LOOP AT lt_pelanggan INTO DATA(ls_baris).
  WRITE: / ls_baris-kunnr, ls_baris-name1, ls_baris-ort01.
ENDLOOP.""",
            },
            {
                "body": [
                    "ABAP adalah bahasa SAP untuk membuat laporan, form, dan logika",
                    "bisnis di SAP S/4HANA dan pendahulunya, SAP ECC. Versi platform",
                    "terbarunya ABAP Platform 2025, bersama SAP S/4HANA 2025 yang",
                    "rilis Oktober 2025.",
                    "",
                    "Contoh di atas gaya klasik: SELECT dari tabel pelanggan KNA1",
                    "ke tabel internal (daftar baris di memori, mirip list of dict",
                    "di Python), lalu dicetak dengan perintah write. Nama objek buatan",
                    "pelanggan wajib berawalan Z atau Y, supaya nggak bentrok",
                    "dengan objek bawaan SAP.",
                ],
            },
            {
                "heading": "ABAP Cloud",
                "bahasa": "abap",
                "code": """CLASS zcl_halo DEFINITION PUBLIC FINAL CREATE PUBLIC.
  PUBLIC SECTION.
    INTERFACES if_oo_adt_classrun.
ENDCLASS.

CLASS zcl_halo IMPLEMENTATION.
  METHOD if_oo_adt_classrun~main.
    out->write( 'Halo, Dunia!' ).
  ENDMETHOD.
ENDCLASS.""",
            },
            {
                "body": [
                    "SAP sekarang mendorong gaya baru bernama ABAP Cloud. Di sana",
                    "perintah write nggak diizinkan. Program dibuat sebagai kelas yang",
                    "mengimplementasikan if_oo_adt_classrun, dan keluarannya muncul",
                    "di konsol Eclipse lewat out->write. Belajar gratis bisa lewat",
                    "akun trial SAP BTP dengan Eclipse ABAP Development Tools.",
                ],
            },
            {
                "heading": "Apex (Salesforce)",
                "bahasa": "apex",
                "code": """// Salah: satu query per akun. Lebih dari 100 akun = batas query habis.
for (Account a : akunBaru) {
    Integer n = [SELECT COUNT() FROM Contact WHERE AccountId = :a.Id];
}

// Benar: satu query untuk semua akun sekaligus.
Map<Id, Integer> jumlahKontak = new Map<Id, Integer>();
for (AggregateResult r : [SELECT AccountId, COUNT(Id) n FROM Contact
                          WHERE AccountId IN :akunBaru GROUP BY AccountId]) {
    jumlahKontak.put((Id) r.get('AccountId'), (Integer) r.get('n'));
}
System.debug(jumlahKontak);""",
            },
            {
                "body": [
                    "Apex mirip Java dan jalan di server Salesforce, bukan di",
                    "komputermu. Query ke database Salesforce ditulis langsung di",
                    "dalam kode dengan SOQL, dialek SQL milik Salesforce, di antara",
                    "kurung siku. Rilis terbarunya Winter '27 (API versi 68.0).",
                    "Salesforce merilis tiga kali setahun: Spring, Summer, Winter.",
                    "",
                    "Karena satu server dipakai banyak perusahaan, Salesforce",
                    "memasang governor limits, yaitu batas per transaksi. Contoh",
                    "yang terkenal: paling banyak 100 query SOQL dalam satu",
                    "transaksi biasa. Karena itu query di dalam perulangan, pola",
                    "\"Salah\" di atas, langsung gagal begitu datanya lebih dari 100.",
                    "Kode juga baru boleh dipasang ke produksi kalau tesnya mencakup",
                    "minimal 75% baris.",
                    "",
                    "Cara mencoba gratis: buat Developer Edition org di situs",
                    "Salesforce, pasang Salesforce CLI (npm install -g",
                    "@salesforce/cli), lalu jalankan kode dengan sf apex run.",
                ],
            },
            {
                "heading": "X++ (Microsoft Dynamics 365)",
                "bahasa": "xpp",
                "code": """class LaporanPelanggan
{
    public static void main(Args _args)
    {
        CustTable pelanggan;

        while select AccountNum, CustGroup from pelanggan
            where pelanggan.CustGroup == '10'
        {
            info(strFmt("%1 (%2)", pelanggan.AccountNum, pelanggan.CustGroup));
        }
    }
}""",
            },
            {
                "body": [
                    "X++ dipakai untuk menyesuaikan Dynamics 365 Finance dan Supply",
                    "Chain Management (dulu Dynamics AX). Sintaksnya dekat dengan C#,",
                    "ditambah select yang menyatu dengan bahasa, seperti while",
                    "select di atas yang membaca baris tabel CustTable satu per satu.",
                    "info() menampilkan pesan di panel infolog.",
                    "",
                    "Versi terbarunya 10.0.49 (September 2026, menurut blog mitra",
                    "Microsoft), yang mewajibkan Visual Studio 2026. Pengembangannya",
                    "cuma di Windows, lewat lingkungan dari lisensi perusahaan atau",
                    "mitra Microsoft. Nggak ada jalur coba gratis yang mudah.",
                ],
            },
            {
                "heading": "RPG (IBM i)",
                "bahasa": "rpg",
                "code": """**free
dcl-s nama varchar(20) inz('Dunia');

dsply ('Halo, ' + nama + '!');
*inlr = *on;
return;""",
            },
            {
                "body": [
                    "RPG adalah bahasa bisnis untuk IBM i, sistem yang dulu dikenal",
                    "sebagai AS/400 dan masih dipakai di ritel, distribusi,",
                    "logistik, dan manufaktur. Versi RPG mengikuti versi sistem",
                    "operasinya; yang terbaru IBM i 7.6 (April 2025).",
                    "",
                    "Baris **free menandai format bebas. Kode RPG lama memakai",
                    "format kolom tetap yang jauh lebih susah dibaca. dsply",
                    "menampilkan pesan, dan *inlr = *on menandai program selesai.",
                    "Cara belajar gratis: akun di PUB400.com, layanan komunitas",
                    "(bukan milik IBM) yang membuka akses ke mesin IBM i sungguhan.",
                ],
            },
            {
                "heading": "PL/I (mainframe)",
                "bahasa": "pli",
                "code": """HALO: PROCEDURE OPTIONS(MAIN);
   PUT LIST('Halo, Dunia!');
END HALO;""",
            },
            {
                "body": [
                    "PL/I dibuat IBM tahun 1960-an untuk menggabungkan kekuatan",
                    "COBOL (bisnis) dan Fortran (sains). Sekarang ia tinggal di",
                    "aplikasi mainframe lama di bank, asuransi, dan pemerintahan.",
                    "Kompilatornya IBM Enterprise PL/I for z/OS, versi 6.2 yang",
                    "diumumkan April 2025. Nggak ada kompilator bebas yang umum",
                    "untuk Fedora, jadi cukup bisa mengenalinya: PROCEDURE",
                    "OPTIONS(MAIN) dan PUT LIST.",
                ],
            },
            {
                "heading": "Membandingkan kelimanya",
                "body": [
                    "  bahasa  platform              coba gratis            status",
                    "  ABAP    SAP S/4HANA           trial SAP BTP          aktif",
                    "  Apex    Salesforce            Developer Edition org  aktif",
                    "  X++     Dynamics 365 F&SCM    lewat lisensi/mitra    aktif",
                    "  RPG     IBM i (AS/400)        PUB400.com             menurun",
                    "  PL/I    mainframe IBM z/OS    nggak ada yang umum    menurun",
                    "",
                    "Ingat: keahlian bahasa ini laku karena terikat pada platform.",
                    "Konsultan SAP atau Salesforce dicari perusahaan pemakai",
                    "platform itu, tapi keahliannya nggak mudah dibawa ke tempat",
                    "lain. Pelajari dasar umum (SQL, OOP, satu bahasa populer) lebih",
                    "dulu, baru tambahkan bahasa platform sesuai tempat kerja.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan berjudul ABAP developer, Salesforce developer, atau",
                    "Dynamics 365 technical consultant mudah ditemukan di situs",
                    "lowongan kerja Indonesia, biasanya dari perusahaan konsultan",
                    "implementasi ERP dan CRM. Pekerjaannya kebanyakan menyesuaikan",
                    "laporan, form, dan aturan bisnis di sistem yang sudah ada.",
                    "",
                    "Kasus kecil: trigger Apex buatan pendahulumu jalan lancar saat",
                    "diuji dengan 10 akun. Saat tim penjualan mengimpor 500 akun",
                    "sekaligus, impornya gagal dengan pesan Too many SOQL queries:",
                    "101.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca angkanya: 101 artinya batas 100 query per transaksi",
                    "     terlewati. Penyebab paling umum adalah query di dalam",
                    "     perulangan.",
                    "  2. Cari for yang di dalamnya ada [SELECT ...].",
                    "  3. Kumpulkan dulu semua Id, lalu ambil datanya dengan satu",
                    "     query memakai IN:",
                    "      [SELECT ... FROM Contact WHERE AccountId IN :akunBaru]",
                    "  4. Tambahkan tes yang memasukkan 200 akun sekaligus, supaya",
                    "     masalah yang sama ketahuan sebelum sampai produksi.",
                ],
            },
        ],
    },
    {
        "title": "39. Peta Dialek SQL Prosedural: PL/SQL, T-SQL, PL/pgSQL",
        "sections": [
            {
                "body": [
                    "SQL standar cuma bisa bertanya dan mengubah data. Begitu kamu",
                    "butuh variabel, if, perulangan, atau penanganan error di dalam",
                    "database, setiap vendor punya bahasa tambahannya sendiri. Dasar",
                    "stored procedure sudah kamu pelajari di kurikulum SQL (materi",
                    "\"View, Stored Procedure & Trigger\" dan \"Bahasa Prosedural di",
                    "Database\"). Materi ini nggak mengulangnya. Fokusnya membaca",
                    "satu prosedur yang sama di tiga dialek dan mengenali bedanya.",
                    "",
                    "  - PL/SQL: milik Oracle, sekarang di Oracle AI Database 26ai.",
                    "    Paling banyak di bank, telko, dan perusahaan besar.",
                    "  - Transact-SQL (T-SQL): milik Microsoft SQL Server dan Azure",
                    "    SQL. Versi terbarunya SQL Server 2025 (17.x).",
                    "  - PL/pgSQL: bahasa prosedural bawaan PostgreSQL. Versi stabil",
                    "    PostgreSQL saat materi ini ditulis 18.6, dan PostgreSQL 19",
                    "    baru sampai tahap RC1.",
                    "",
                    "Contohnya sama di ketiga dialek: prosedur naikkan_harga yang",
                    "menaikkan harga semua produk sekian persen, melaporkan berapa",
                    "baris yang berubah, lalu query tiga produk termahal.",
                ],
            },
            {
                "heading": "PL/SQL (Oracle)",
                "bahasa": "plsql",
                "code": """CREATE OR REPLACE PROCEDURE naikkan_harga (p_persen IN NUMBER) AS
  v_jumlah NUMBER;
BEGIN
  UPDATE produk SET harga = harga * (1 + p_persen / 100);
  v_jumlah := SQL%ROWCOUNT;
  DBMS_OUTPUT.PUT_LINE(v_jumlah || ' produk dinaikkan');
EXCEPTION
  WHEN OTHERS THEN
    ROLLBACK;
    RAISE;
END;
/

SELECT nama, harga FROM produk ORDER BY harga DESC
FETCH FIRST 3 ROWS ONLY;""",
            },
            {
                "body": [
                    "Ciri PL/SQL yang gampang dikenali:",
                    "",
                    "  v_jumlah NUMBER;      variabel dideklarasikan sebelum BEGIN",
                    "  :=                    mengisi variabel",
                    "  SQL%ROWCOUNT          banyaknya baris yang kena perintah terakhir",
                    "  DBMS_OUTPUT.PUT_LINE  mencetak teks; di SQL*Plus atau SQLcl baru",
                    "                        tampil sesudah SET SERVEROUTPUT ON",
                    "  ||                    menggabung teks",
                    "  /                     baris berisi garis miring saja menyuruh",
                    "                        SQL*Plus menjalankan blok di atasnya",
                    "  FETCH FIRST n ROWS    membatasi baris (diakhiri ROWS ONLY)",
                ],
            },
            {
                "heading": "T-SQL (SQL Server)",
                "bahasa": "tsql",
                "code": """CREATE OR ALTER PROCEDURE naikkan_harga @persen DECIMAL(5,2) AS
BEGIN
  DECLARE @jumlah INT;
  BEGIN TRY
    UPDATE produk SET harga = harga * (1 + @persen / 100);
    SET @jumlah = @@ROWCOUNT;
    PRINT CAST(@jumlah AS VARCHAR(10)) + ' produk dinaikkan';
  END TRY
  BEGIN CATCH
    THROW;
  END CATCH
END;
GO

SELECT TOP 3 nama, harga FROM produk ORDER BY harga DESC;""",
            },
            {
                "body": [
                    "Ciri T-SQL:",
                    "",
                    "  @nama                 semua variabel diawali @",
                    "  SET @x = ...          mengisi variabel (bisa juga lewat SELECT)",
                    "  @@ROWCOUNT            variabel sistem: banyaknya baris yang kena",
                    "  PRINT                 mencetak pesan; angka diubah jadi teks dulu",
                    "                        dengan CAST sebelum digabung memakai +",
                    "  BEGIN TRY/CATCH       menangani error",
                    "  SELECT TOP n          membatasi baris, ditulis tepat sesudah SELECT",
                    "",
                    "Jebakan: GO bukan perintah T-SQL. GO adalah pemisah batch milik",
                    "alat klien seperti sqlcmd dan SSMS. Kalau kamu mengirim teks",
                    "berisi GO lewat kode aplikasi (misalnya dari Python), server",
                    "menolaknya sebagai sintaks salah.",
                ],
            },
            {
                "heading": "PL/pgSQL (PostgreSQL)",
                "bahasa": "postgresql",
                "code": """CREATE OR REPLACE PROCEDURE naikkan_harga(p_persen numeric)
LANGUAGE plpgsql AS $$
DECLARE
  v_jumlah integer;
BEGIN
  UPDATE produk SET harga = harga * (1 + p_persen / 100);
  GET DIAGNOSTICS v_jumlah = ROW_COUNT;
  RAISE NOTICE '% produk dinaikkan', v_jumlah;
END;
$$;

CALL naikkan_harga(10);
SELECT nama, harga FROM produk ORDER BY harga DESC LIMIT 3;""",
            },
            {
                "body": [
                    "Ciri PL/pgSQL:",
                    "",
                    "  $$ ... $$             isi prosedur ditulis sebagai teks di antara",
                    "                        dua tanda dolar ganda",
                    "  LANGUAGE plpgsql      menyebut bahasa isinya",
                    "  GET DIAGNOSTICS       mengambil banyaknya baris yang berubah",
                    "  RAISE NOTICE '%'      mencetak pesan, % diganti nilai",
                    "  CALL nama(...)        memanggil prosedur; fungsi biasa dipanggil",
                    "                        di dalam SELECT",
                    "  LIMIT n               membatasi baris, sama seperti SQLite dan MySQL",
                    "",
                    "Sintaks PL/pgSQL sengaja dibuat mirip PL/SQL, jadi orang yang",
                    "pindah dari Oracle ke PostgreSQL merasa cukup akrab. Yang perlu",
                    "diwaspadai justru detail kecil seperti cara menghitung baris yang",
                    "berubah dan cara mencetak.",
                ],
            },
            {
                "heading": "Ringkasan perbedaan",
                "body": [
                    "  hal              PL/SQL           T-SQL           PL/pgSQL",
                    "  variabel         v_x NUMBER;      DECLARE @x INT  v_x int;",
                    "  mengisi          :=               SET @x =        :=",
                    "  baris kena       SQL%ROWCOUNT     @@ROWCOUNT      GET DIAGNOSTICS",
                    "  mencetak         DBMS_OUTPUT      PRINT           RAISE NOTICE",
                    "  gabung teks      ||               +               ||",
                    "  batasi baris     FETCH FIRST n    TOP n           LIMIT n",
                    "  pemisah blok     /                GO              $$ ... $$",
                    "",
                    "Ingat: dialek-dialek ini nggak bisa dicoba dengan sqlite3 yang",
                    "ada di aplikasi ini, karena SQLite nggak punya stored procedure",
                    "sama sekali. Oracle menyediakan Oracle Live SQL di browser.",
                    "SQL Server dan PostgreSQL bisa dijalankan di kontainer podman",
                    "kalau kamu sudah belajar kurikulum devops, atau PostgreSQL",
                    "langsung dari dnf.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir, gudang, dan keuangan yang dibangun 10 sampai 20",
                    "tahun lalu sering menyimpan aturan bisnisnya di stored",
                    "procedure, bukan di kode aplikasi. Saat perusahaan pindah",
                    "database, misalnya dari SQL Server ke PostgreSQL untuk menghemat",
                    "lisensi, prosedur-prosedur itulah yang paling banyak makan",
                    "waktu.",
                    "",
                    "Kasus kecil: kamu diminta memindahkan prosedur T-SQL kecil ke",
                    "PostgreSQL. Isinya SELECT TOP 5, variabel @total, dan PRINT.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat kerangka PL/pgSQL dulu: CREATE PROCEDURE ... LANGUAGE",
                    "     plpgsql AS $$ DECLARE ... BEGIN ... END; $$;",
                    "  2. Pindahkan variabel: @total INT jadi v_total integer di",
                    "     bagian DECLARE, dan SET @total = ... jadi v_total := ....",
                    "  3. Ganti TOP 5 dengan LIMIT 5 di ujung query, PRINT dengan",
                    "     RAISE NOTICE, dan + penggabung teks dengan ||:",
                    "      RAISE NOTICE 'total: %', v_total;",
                    "  4. Jalankan dengan CALL dan bandingkan hasilnya dengan",
                    "     prosedur lama di data yang sama.",
                ],
            },
        ],
    },
    {
        "title": "40. Peta Kode Warisan: Delphi, VB6, FoxPro, CFML, ActionScript",
        "sections": [
            {
                "body": [
                    "Kode warisan (legacy) adalah program lama yang masih dipakai",
                    "tapi dibuat dengan teknologi yang sudah nggak populer. Di",
                    "tempat PKL, kamu bisa ketemu aplikasi kasir buatan tahun 2005",
                    "atau situs intranet yang nggak pernah diganti. Materi ini",
                    "membantumu menjawab dua pertanyaan: bahasa apa ini, dan apakah",
                    "sebaiknya tetap dirawat atau dimigrasi.",
                    "",
                    "Ada enam bahasa yang dibahas, dari yang masih aktif sampai yang",
                    "sudah mati. Statusnya ditulis apa adanya.",
                ],
            },
            {
                "heading": "Delphi dan Object Pascal (masih aktif)",
                "bahasa": "pascal",
                "code": """program Halo;

begin
  WriteLn('Halo, Dunia!');
end.""",
            },
            {
                "body": [
                    "Delphi adalah IDE komersial untuk membuat aplikasi desktop",
                    "Windows dengan cepat: gambar form, taruh tombol, tulis kode di",
                    "baliknya. Bahasanya Object Pascal. Di Indonesia, banyak aplikasi",
                    "kasir, akuntansi, dan inventori lama dibuat dengan Delphi.",
                    "",
                    "Delphi masih dirilis. Versi terbarunya Delphi 13.2 (RAD Studio",
                    "13 Florence, September 2026 menurut daftar harga penjual resmi), dan",
                    "ada Community Edition gratis dengan syarat. Di indeks TIOBE",
                    "Oktober 2026 ia di peringkat 19. Pasangan bebasnya Free Pascal",
                    "dan Lazarus, yang ada di Fedora: sudo dnf install fpc lazarus,",
                    "lalu fpc halo.pas && ./halo.",
                    "",
                    "Jebakan: di Pascal, := untuk mengisi variabel dan = untuk",
                    "membandingkan. Kebalikan dari kebiasaanmu di Python dan C.",
                ],
            },
            {
                "heading": "Classic Visual Basic 6 (usang)",
                "bahasa": "basic",
                "code": """Private Sub Form_Load()
    MsgBox "Halo, Dunia!"
End Sub""",
            },
            {
                "body": [
                    "VB6 adalah Visual Basic versi lama, sebelum VB.NET, dirilis",
                    "1998. IDE-nya sudah lama nggak dijual dan nggak didukung, tapi",
                    "program hasilnya masih bisa jalan di Windows. Sintaksnya hampir",
                    "sama dengan VBA di materi sebelumnya. Masih ada di kode lama,",
                    "jangan dipilih untuk proyek baru. Jalur migrasi yang umum ke",
                    "VB.NET atau C#, dan aplikasi ini punya kurikulum untuk",
                    "keduanya.",
                ],
            },
            {
                "heading": "Visual FoxPro (usang)",
                "bahasa": "foxpro",
                "code": """? "Halo, Dunia!"

USE pelanggan
SCAN FOR kota = "Bandung"
    ? nama, telepon
ENDSCAN""",
            },
            {
                "body": [
                    "Visual FoxPro adalah bahasa sekaligus database desktop dari",
                    "keluarga dBase/xBase. Datanya disimpan di berkas .dbf. Versi",
                    "terakhirnya 9.0 SP2 (2007), dan dukungan diperpanjangnya",
                    "berakhir 13 Januari 2015. Nggak akan ada versi baru. Aplikasi",
                    "FoxPro yang masih jalan sebaiknya dimigrasi: datanya ke",
                    "database seperti PostgreSQL atau SQL Server, aplikasinya ke",
                    "web atau desktop modern.",
                ],
            },
            {
                "heading": "CFML (menurun)",
                "bahasa": "cfml",
                "code": """<cfquery name="produk" datasource="toko">
    SELECT nama, harga FROM produk
</cfquery>

<cfoutput query="produk">
    <p>#nama#: #harga#</p>
</cfoutput>""",
            },
            {
                "body": [
                    "CFML (ColdFusion Markup Language) adalah bahasa web sisi server",
                    "berbentuk tag mirip HTML. Nama di antara tanda # diganti",
                    "nilainya. Mesinnya ada dua: Adobe ColdFusion (komersial, versi",
                    "2025) dan Lucee (open source, versi 7.0.4). Masih dirawat, tapi",
                    "hampir nggak dipakai untuk proyek baru. Situs CFML lama",
                    "biasanya dimigrasi ke PHP, Node.js, atau Java, yang semuanya",
                    "punya kurikulum di aplikasi ini.",
                ],
            },
            {
                "heading": "ActionScript 3 (usang)",
                "bahasa": "actionscript",
                "code": """package {
    import flash.display.Sprite;

    public class Halo extends Sprite {
        public function Halo() {
            trace("Halo, Dunia!");
        }
    }
}""",
            },
            {
                "body": [
                    "ActionScript 3 adalah bahasa untuk Adobe Flash. Flash Player",
                    "dihentikan 31 Desember 2020, dan browser sudah nggak",
                    "menjalankannya. Adobe AIR, tempat ActionScript masih bisa",
                    "dipakai untuk aplikasi dan game mobile, sekarang dirawat",
                    "HARMAN. Game dan animasi Flash lama biasanya dibuat ulang",
                    "dengan JavaScript dan HTML5 canvas, atau dengan engine game.",
                ],
            },
            {
                "heading": "Hack (menurun di luar Meta)",
                "bahasa": "hack",
                "code": "<<__EntryPoint>>\nfunction main(): void {\n  echo \"Halo, Dunia!\\n\";\n}",
            },
            {
                "body": [
                    "Hack adalah bahasa buatan Meta (Facebook) yang lahir dari PHP",
                    "dan menambahkan sistem tipe, berjalan di mesin virtual HHVM.",
                    "Sejak pengumuman Oktober 2023, Meta nggak lagi membuat rilis",
                    "resmi HHVM dan Hack untuk publik. Di luar Meta pemakainya",
                    "sedikit sekali. Ini contoh risiko bahasa milik satu perusahaan:",
                    "begitu perusahaannya berhenti merilis, pemakai di luar ikut",
                    "terdampar. PHP modern dengan deklarasi tipe adalah jalur pulang",
                    "yang wajar.",
                ],
            },
            {
                "heading": "Merawat atau memigrasi?",
                "body": [
                    "  bahasa         era         status           migrasi umum",
                    "  Delphi         1995-kini   aktif            tetap, atau ke C#",
                    "  VB6            1991-1998   usang            VB.NET atau C#",
                    "  Visual FoxPro  1995-2007   usang sejak 2015 web + PostgreSQL",
                    "  CFML           1995-kini   menurun          PHP, Node.js, Java",
                    "  ActionScript 3 2006-2020   usang            JavaScript, engine",
                    "  Hack           2014-2023   tanpa rilis      PHP bertipe",
                    "",
                    "Pertanyaan yang menentukan:",
                    "  - Apakah alat pembuatnya masih bisa dipasang dan didukung?",
                    "  - Apakah masih ada orang yang bisa merawatnya?",
                    "  - Seberapa berisiko kalau program itu berhenti jalan?",
                    "  - Apakah datanya bisa dikeluarkan ke format terbuka?",
                    "",
                    "Migrasi besar sekaligus jarang berhasil. Pola yang lebih aman",
                    "disebut strangler fig: bangun bagian baru di sistem modern satu",
                    "per satu sambil sistem lama tetap jalan, sampai sistem lama",
                    "bisa dimatikan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Koperasi, toko bangunan, klinik, dan pabrik kecil di Indonesia",
                    "masih banyak memakai aplikasi desktop buatan Delphi, VB6, atau",
                    "FoxPro yang dibuat programmer lepas belasan tahun lalu. Datanya",
                    "sering berupa berkas .dbf atau database Access di satu",
                    "komputer.",
                    "",
                    "Kasus kecil: pemilik toko tempatmu PKL minta laporan penjualan",
                    "bisa dibuka di HP. Aplikasi kasirnya FoxPro, dan programmer",
                    "aslinya sudah nggak bisa dihubungi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Jangan sentuh aplikasi kasirnya dulu. Ia masih jalan dan",
                    "     toko bergantung padanya setiap hari.",
                    "  2. Cari berkas datanya (.dbf) dan buat salinan. Format .dbf",
                    "     terdokumentasi dan bisa dibaca banyak alat, termasuk",
                    "     LibreOffice Calc di Fedora.",
                    "  3. Buat skrip yang membaca salinan itu setiap malam dan",
                    "     mengekspornya ke CSV atau database baru.",
                    "  4. Bangun halaman laporan dari data baru itu. Aplikasi lama",
                    "     tetap jalan, dan bagian berikutnya bisa dipindah satu per",
                    "     satu dengan pola strangler fig.",
                ],
            },
        ],
    },
    {
        "title": "41. Verilog dan VHDL: Menulis Rangkaian sebagai Kode",
        "sections": [
            {
                "body": [
                    "Semua bahasa yang sudah kamu pelajari menulis langkah untuk",
                    "CPU: kerjakan ini, lalu itu. Verilog dan VHDL beda jenis. Kamu",
                    "nggak menulis program untuk dijalankan chip. Kamu menulis",
                    "rancangan chip-nya sendiri: gerbang logika, kabel, dan register",
                    "yang menyusun rangkaian digital.",
                    "",
                    "Bahasa seperti ini disebut HDL (hardware description language).",
                    "Hasilnya bisa jadi dua hal. Pertama, chip pesanan khusus yang",
                    "dicetak pabrik (ASIC), seperti CPU dan GPU. Kedua, konfigurasi",
                    "untuk FPGA, yaitu chip yang rangkaiannya bisa disusun ulang",
                    "berkali-kali lewat berkas konfigurasi. FPGA dipakai untuk",
                    "prototipe chip, pengolahan sinyal, dan perangkat jaringan.",
                    "",
                    "Ada dua bahasa utama:",
                    "",
                    "  - Verilog dan penerusnya SystemVerilog (standar IEEE",
                    "    1800-2023). Paling umum di industri semikonduktor,",
                    "    termasuk proyek prosesor RISC-V terbuka.",
                    "  - VHDL (standar IEEE 1076-2019). Banyak dipakai di Eropa,",
                    "    dirgantara, dan pertahanan.",
                ],
            },
            {
                "heading": "Half adder (half_adder.v)",
                "bahasa": "verilog",
                "code": """module half_adder(
    input  a,
    input  b,
    output s,
    output c
);
    assign s = a ^ b;   // jumlah: 1 kalau tepat satu input 1
    assign c = a & b;   // carry: 1 kalau dua-duanya 1
endmodule""",
            },
            {
                "body": [
                    "Half adder adalah rangkaian penjumlah dua bit. Ia punya dua",
                    "input (a dan b) dan dua output: s untuk jumlah dan c untuk",
                    "carry (simpanan ke bit berikutnya).",
                    "",
                    "  - module ... endmodule membungkus satu komponen, lengkap",
                    "    dengan daftar port masuk dan keluarnya.",
                    "  - assign menyambung output ke sebuah rumus. ^ adalah XOR,",
                    "    & adalah AND, | adalah OR, ~ adalah NOT.",
                    "",
                    "Ini bagian yang paling susah dibiasakan: dua baris assign itu",
                    "nggak jalan berurutan. Keduanya adalah kabel yang selalu",
                    "tersambung. Begitu a atau b berubah, s dan c ikut berubah saat",
                    "itu juga, seperti lampu yang langsung nyala waktu saklarnya",
                    "ditekan. Menukar urutan dua baris itu nggak mengubah apa pun.",
                ],
            },
            {
                "heading": "Testbench: menguji rangkaian dalam simulasi (tb.v)",
                "bahasa": "verilog",
                "code": """module tb;
    reg a, b;
    wire s, c;
    integer i;

    half_adder uji(.a(a), .b(b), .s(s), .c(c));

    initial begin
        $display("a b | s c");
        for (i = 0; i < 4; i = i + 1) begin
            {a, b} = i;          // 0 -> 00, 1 -> 01, 2 -> 10, 3 -> 11
            #1;                  // tunggu sebentar supaya assign terhitung
            $display("%b %b | %b %b", a, b, s, c);
        end
        $finish;
    end
endmodule""",
            },
            {
                "body": [
                    "Rangkaian nggak bisa diuji dengan print biasa. Yang dibuat",
                    "adalah testbench, modul pembungkus yang memberi input lalu",
                    "mencatat output. Testbench hanya hidup di simulator.",
                    "",
                    "  - reg menyimpan nilai yang diatur testbench, wire cuma kabel",
                    "    yang membawa nilai dari output half_adder.",
                    "  - initial begin ... end dijalankan sekali saat simulasi",
                    "    mulai.",
                    "  - #1 menunggu satu satuan waktu simulasi.",
                    "  - $display mencetak seperti printf, dan $finish menghentikan",
                    "    simulasi.",
                    "",
                    "Jalankan dengan Icarus Verilog:",
                    "",
                    "  iverilog -o sim half_adder.v tb.v",
                    "  vvp sim",
                    "",
                    "Keluarannya tabel kebenaran half adder:",
                    "",
                    "  a b | s c",
                    "  0 0 | 0 0",
                    "  0 1 | 1 0",
                    "  1 0 | 1 0",
                    "  1 1 | 0 1",
                ],
            },
            {
                "heading": "Memasang alat simulasi di Fedora",
                "bahasa": "terminal",
                "code": """sudo dnf install iverilog verilator gtkwave ghdl
iverilog -o sim half_adder.v tb.v && vvp sim
verilator --lint-only -Wall half_adder.v   # cek gaya dan galat""",
            },
            {
                "heading": "Rangkaian yang punya ingatan: counter",
                "bahasa": "verilog",
                "code": """module counter(
    input            clk,
    input            reset,
    output reg [3:0] hitung
);
    always @(posedge clk) begin
        if (reset)
            hitung <= 4'd0;
        else
            hitung <= hitung + 4'd1;   // dari 15 kembali ke 0
    end
endmodule""",
            },
            {
                "body": [
                    "Half adder tadi rangkaian kombinasional: outputnya cuma",
                    "bergantung pada input saat itu. Counter adalah rangkaian",
                    "sekuensial, yang punya ingatan. Isinya berubah hanya di tepi",
                    "naik sinyal clock (posedge clk), yaitu denyut teratur yang",
                    "menggerakkan seluruh chip. Di papan FPGA latihan, clock-nya",
                    "sering 50 MHz, artinya 50 juta denyut per detik.",
                    "",
                    "  - reg [3:0] adalah register 4 bit, isinya 0 sampai 15.",
                    "  - always @(posedge clk) berarti blok ini bereaksi setiap",
                    "    tepi naik clock.",
                    "  - 4'd1 artinya angka 1 desimal selebar 4 bit.",
                    "",
                    "Jebakan: di blok always yang dipicu clock, pakai <= (assignment",
                    "nonblocking), bukan =. Dengan <=, semua register membaca nilai",
                    "lama dulu lalu berubah bersamaan, seperti flip-flop sungguhan.",
                    "Memakai = di sini bisa membuat simulasi dan chip hasil sintesis",
                    "berperilaku beda, dan bug seperti itu susah sekali dicari.",
                ],
            },
            {
                "heading": "Simulasi dan sintesis",
                "body": [
                    "Kode HDL melewati dua jalan yang berbeda:",
                    "",
                    "  - Simulasi: Icarus Verilog atau Verilator menjalankan",
                    "    rancangan di komputer. Hasilnya keluaran teks atau",
                    "    gelombang sinyal yang dilihat dengan GTKWave. Di sini",
                    "    $display, initial, dan tunda #1 boleh dipakai.",
                    "  - Sintesis: alat seperti Yosys (open source), AMD Vivado,",
                    "    atau Intel Quartus menerjemahkan rancangan jadi gerbang",
                    "    dan flip-flop sungguhan, lalu jadi berkas konfigurasi FPGA.",
                    "    $display dan tunda #1 diabaikan atau ditolak, karena chip",
                    "    nggak punya layar dan nggak bisa menunggu \"1 satuan\".",
                    "",
                    "Ingat: kode yang lulus simulasi belum tentu bisa disintesis.",
                    "Tulis bagian rancangan (modul seperti half_adder dan counter)",
                    "dengan gaya yang bisa disintesis, dan simpan trik khusus",
                    "simulasi di testbench saja.",
                    "",
                    "Versi alat saat materi ini ditulis (Oktober 2026): Icarus",
                    "Verilog 13.0, Verilator 5.052 (Fedora 44 mengemas 5.046), dan",
                    "GHDL 6.0.0 untuk VHDL. Untuk verifikasi chip skala industri,",
                    "orang memakai SystemVerilog dengan metodologi UVM, atau cocotb",
                    "kalau ingin menulis testbench dengan Python.",
                ],
            },
            {
                "heading": "Half adder yang sama di VHDL",
                "bahasa": "vhdl",
                "code": """library ieee;
use ieee.std_logic_1164.all;

entity half_adder is
    port (
        a, b : in  std_logic;
        s, c : out std_logic
    );
end entity half_adder;

architecture rtl of half_adder is
begin
    s <= a xor b;
    c <= a and b;
end architecture rtl;""",
            },
            {
                "body": [
                    "VHDL lebih panjang dan lebih ketat soal tipe. entity",
                    "menjelaskan port (bagian luar komponen), architecture",
                    "menjelaskan isinya. <= di VHDL adalah penugasan sinyal, dan",
                    "operatornya ditulis sebagai kata: xor, and, or, not.",
                    "",
                    "  hal               Verilog            VHDL",
                    "  gaya              ringkas, mirip C   panjang, mirip Ada",
                    "  tipe              longgar            ketat (std_logic)",
                    "  huruf besar-kecil dibedakan          nggak dibedakan",
                    "  wilayah kuat      chip komersial     Eropa, dirgantara",
                    "  simulator bebas   Icarus, Verilator  GHDL",
                    "",
                    "Simulasi VHDL dengan GHDL berjalan tiga langkah: ghdl -a untuk",
                    "menganalisis, ghdl -e untuk menyusun, ghdl -r untuk",
                    "menjalankan. Pesan dari perintah report dicetak dengan awalan",
                    "nama berkas dan baris, jadi keluarannya nggak sebersih",
                    "$display.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Desainer chip di perusahaan semikonduktor menulis",
                    "SystemVerilog setiap hari, dan verifikasinya sering makan waktu",
                    "lebih banyak daripada desainnya. Di kampus dan komunitas, papan",
                    "FPGA murah dipakai untuk belajar membuat CPU sendiri, dan",
                    "banyak inti prosesor RISC-V terbuka ditulis dengan Verilog atau",
                    "SystemVerilog.",
                    "",
                    "Kasus kecil: kamu punya papan FPGA dengan clock 50 MHz dan",
                    "ingin LED berkedip sekali per detik. Counter 4 bit di atas",
                    "membuat LED berkedip jutaan kali per detik, terlalu cepat untuk",
                    "dilihat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hitung: 50 juta denyut per detik. Supaya LED nyala setengah",
                    "     detik dan mati setengah detik, balik keadaannya setiap",
                    "     25.000.000 denyut.",
                    "  2. Butuh counter yang muat sampai 25 juta. 2 pangkat 25 sudah",
                    "     lebih dari 33 juta, jadi pakai register 25 bit.",
                    "  3. Tulis blok always yang menghitung dan membalik LED:",
                    "      if (hitung == 25'd24999999) begin",
                    "          hitung <= 0;  led <= ~led;",
                    "      end else hitung <= hitung + 1;",
                    "  4. Uji dulu di simulasi dengan batas kecil (misalnya 5),",
                    "     baru ganti ke 24999999 dan sintesis ke papan.",
                ],
            },
        ],
    },
    {
        "title": "42. MicroPython: Python di Mikrokontroler",
        "sections": [
            {
                "body": [
                    "Mikrokontroler adalah komputer kecil dalam satu chip: CPU,",
                    "sedikit RAM, memori flash, dan kaki-kaki (pin) yang bisa",
                    "menyalakan LED atau membaca tombol. Harganya puluhan ribu",
                    "rupiah, dan ia ada di mesin cuci, remote, sampai sensor kebun.",
                    "",
                    "Biasanya mikrokontroler diprogram dengan C atau C++. MicroPython",
                    "membuatnya bisa diprogram dengan Python. Ia adalah Python 3",
                    "versi ramping yang jalan langsung di chip, tanpa sistem operasi.",
                    "Versi terbarunya 1.29.0 (Agustus 2026), lisensi MIT. Di Survei",
                    "Stack Overflow 2026, 2,7% responden memakainya.",
                    "",
                    "Dua papan yang paling sering dipakai:",
                    "",
                    "  - ESP32: punya Wi-Fi dan Bluetooth, cocok untuk proyek IoT.",
                    "  - Raspberry Pi Pico: chip RP2040 (RAM 264 KB) atau RP2350",
                    "    (RAM 520 KB) buatan Raspberry Pi. Murah dan dokumentasinya",
                    "    bagus.",
                    "",
                    "Materi ini membahas bahasanya. Soal perangkat keras (rangkaian,",
                    "sensor, protokol) dibahas di kurikulum iot.",
                ],
            },
            {
                "heading": "LED berkedip (main.py)",
                "bahasa": "micropython",
                "code": """from machine import Pin
import time

led = Pin(2, Pin.OUT)          # LED bawaan banyak papan ESP32 ada di GPIO 2
# di Raspberry Pi Pico: led = Pin("LED", Pin.OUT)

while True:
    led.value(not led.value())   # balik: nyala jadi mati, mati jadi nyala
    time.sleep_ms(500)""",
            },
            {
                "body": [
                    "Modul machine adalah pintu ke perangkat keras. Pin(2,",
                    "Pin.OUT) menyiapkan pin nomor 2 sebagai output. value()",
                    "tanpa argumen membaca keadaannya, value(1) atau value(0)",
                    "mengubahnya. time.sleep_ms(500) menunggu setengah detik.",
                    "",
                    "Perhatikan while True. Di laptop, program tanpa ujung itu",
                    "aneh. Di mikrokontroler justru normal: papan menyala, menjalankan",
                    "main.py, lalu terus bekerja sampai listriknya dicabut.",
                    "",
                    "Jebakan: nomor pin di kode adalah nomor GPIO milik chip, belum",
                    "tentu sama dengan nomor yang tercetak di papan. Selalu cek",
                    "diagram pinout papanmu sebelum menyambung kabel.",
                ],
            },
            {
                "heading": "Tombol dan PWM",
                "bahasa": "micropython",
                "code": """from machine import Pin, PWM
import time

tombol = Pin(14, Pin.IN, Pin.PULL_UP)   # lepas = 1, ditekan = 0
lampu = PWM(Pin(15), freq=1000)

while True:
    if tombol.value() == 0:
        for terang in range(0, 65536, 4096):
            lampu.duty_u16(terang)          # 0 = mati, 65535 = paling terang
            time.sleep_ms(30)
        lampu.duty_u16(0)
    time.sleep_ms(20)""",
            },
            {
                "body": [
                    "Pin.PULL_UP menyalakan resistor di dalam chip, sehingga pin",
                    "bernilai 1 saat tombol dilepas dan 0 saat ditekan (tombolnya",
                    "menyambung pin ke ground). Logika terbalik ini sering bikin",
                    "pemula bingung.",
                    "",
                    "PWM (pulse width modulation) menyalakan dan mematikan pin",
                    "ribuan kali per detik. Makin lama porsi nyalanya, makin terang",
                    "LED terlihat. duty_u16 menerima 0 sampai 65535. Cara yang sama",
                    "dipakai untuk mengatur kecepatan motor dan posisi servo.",
                ],
            },
            {
                "heading": "Mengirim kode ke papan",
                "bahasa": "terminal",
                "code": """pip install --user mpremote
sudo usermod -aG dialout $USER     # izin port serial, lalu login ulang
mpremote connect list              # cari papan yang tersambung
mpremote                           # masuk REPL di papan
mpremote fs cp main.py :main.py    # salin berkas ke papan
mpremote run coba.py               # jalankan tanpa menyalin
mpremote mip install aioble        # pasang pustaka MicroPython""",
            },
            {
                "body": [
                    "Firmware MicroPython dipasang sekali dari micropython.org/download.",
                    "Untuk Pico caranya paling gampang: tahan tombol BOOTSEL sambil",
                    "mencolok USB, papan muncul sebagai flashdisk, lalu seret berkas",
                    ".uf2 ke sana. ESP32 dipasang dengan alat esptool.",
                    "",
                    "Sesudah itu papan bicara lewat port serial USB. REPL (tempat",
                    "mengetik perintah Python satu per satu) jalan di papan itu",
                    "sendiri. Ketik led.value(1), dan LED langsung menyala tanpa",
                    "kompilasi. mpremote adalah alat resmi untuk REPL, menyalin",
                    "berkas, dan memasang pustaka. Kalau lebih suka editor grafis,",
                    "Thonny punya dukungan MicroPython bawaan.",
                    "",
                    "Di Fedora, akunmu harus masuk grup dialout supaya bisa membuka",
                    "port serial. Tanpa itu, mpremote gagal dengan pesan izin",
                    "ditolak. Fedora juga mengemas MicroPython untuk Linux (sudo dnf",
                    "install micropython, versi 1.28.0), berguna untuk mencoba",
                    "bahasanya, tapi modul machine untuk pin nggak ada di sana.",
                ],
            },
            {
                "heading": "Apa yang beda dari Python biasa",
                "body": [
                    "  - Cuma sebagian pustaka standar. Banyak modul dipangkas, dan",
                    "    sebagian berganti nama atau bentuk, misalnya time punya",
                    "    sleep_ms dan ticks_ms yang nggak ada di CPython.",
                    "  - Nggak ada pip di papan. Pustaka dipasang dengan mip, dan",
                    "    paket PyPI biasa umumnya nggak bisa dipakai.",
                    "  - RAM terbatas sekali: ratusan kilobyte, bukan gigabyte.",
                    "    gc.mem_free() menunjukkan sisa memori. Membuat list besar",
                    "    atau string panjang di dalam perulangan cepat menghabiskan",
                    "    memori.",
                    "  - Nggak ada sistem operasi. Satu program menguasai chip, dan",
                    "    kalau programnya macet, papan perlu direset.",
                    "",
                    "Satu kebiasaan yang menolong: pisahkan logika dari akses pin,",
                    "supaya logikanya bisa diuji di laptop dengan Python biasa",
                    "memakai pin palsu. Contohnya di bawah ini jalan di CPython.",
                ],
            },
            {
                "heading": "Menguji logika dengan pin palsu",
                "code": """class PinPalsu:
    OUT = 1

    def __init__(self, nomor, mode):
        self.nomor = nomor
        self.isi = 0
        self.riwayat = []

    def value(self, v=None):
        if v is None:
            return self.isi
        self.isi = int(v)
        self.riwayat.append(self.isi)


def kedip(led, kali):
    for _ in range(kali):
        led.value(not led.value())


led = PinPalsu(2, PinPalsu.OUT)
kedip(led, 4)
print("riwayat LED:", led.riwayat)
print("akhir:", led.value())""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  riwayat LED: [1, 0, 1, 0]",
                    "  akhir: 0",
                    "",
                    "Fungsi kedip nggak peduli pin-nya asli atau palsu, asal punya",
                    "method value. Di papan, kamu cukup mengopernya Pin(2, Pin.OUT).",
                ],
            },
            {
                "heading": "CircuitPython",
                "bahasa": "micropython",
                "code": """import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(0.5)""",
            },
            {
                "body": [
                    "CircuitPython adalah turunan MicroPython buatan Adafruit yang",
                    "dibuat lebih ramah pemula. Papannya muncul sebagai flashdisk",
                    "bernama CIRCUITPY, dan kamu cukup menyimpan berkas code.py di",
                    "sana. Pin diakses lewat modul board dan digitalio, bukan",
                    "machine, jadi kode MicroPython dan CircuitPython nggak bisa",
                    "saling tukar begitu saja.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "MicroPython dipakai di prototipe perangkat IoT, alat ukur",
                    "sederhana, robot sekolah, dan lomba. Papan BBC micro:bit yang",
                    "dipakai di banyak sekolah juga bisa diprogram dengan",
                    "MicroPython.",
                    "",
                    "Kasus kecil: kebun hidroponik di sekolahmu butuh pompa yang",
                    "menyala kalau sensor kelembapan di pin 34 ESP32 membaca terlalu",
                    "kering. Pompa dikendalikan relay di pin 26.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Coba baca sensornya dulu di REPL lewat mpremote dan catat",
                    "     angkanya saat tanah kering dan basah.",
                    "  2. Tulis logikanya sebagai fungsi biasa yang bisa diuji di",
                    "     laptop, misalnya perlu_siram(nilai, batas).",
                    "  3. Di main.py, sambungkan ke pin sungguhan:",
                    "      sensor = ADC(Pin(34))",
                    "      relay = Pin(26, Pin.OUT)",
                    "      relay.value(perlu_siram(sensor.read_u16(), batas))",
                    "  4. Beri jeda dengan time.sleep, dan tambahkan batas lama",
                    "     menyala supaya pompa nggak jalan terus kalau sensornya",
                    "     rusak.",
                ],
            },
        ],
    },
    {
        "title": "43. Peta Otomasi Industri: Ladder Logic dan LabVIEW",
        "sections": [
            {
                "body": [
                    "Di pabrik, mesin dikendalikan PLC (programmable logic",
                    "controller): komputer industri yang tahan panas, debu, dan",
                    "getaran, dengan banyak terminal untuk sensor, tombol, motor, dan",
                    "lampu. Konveyor, mesin pengemas, pompa air, dan lampu lalu",
                    "lintas biasanya dikendalikan PLC.",
                    "",
                    "Bahasa untuk PLC diatur standar IEC 61131-3. Edisi terbarunya",
                    "edisi ke-4, terbit Mei 2025 (IEC 61131-3:2025). Ada beberapa",
                    "bahasa di dalamnya:",
                    "",
                    "  - Ladder Diagram (LD): bahasa grafis yang meniru gambar",
                    "    rangkaian relay listrik. Paling umum di pabrik.",
                    "  - Structured Text (ST): bahasa teks mirip Pascal.",
                    "  - Function Block Diagram (FBD): blok fungsi yang disambung",
                    "    kabel.",
                    "  - Sequential Function Chart (SFC): langkah dan transisi untuk",
                    "    proses berurutan.",
                    "",
                    "Instruction List, bahasa teks mirip assembly, sudah ditandai",
                    "usang sejak edisi 2013. Kamu mungkin masih melihatnya di program",
                    "lama.",
                ],
            },
            {
                "heading": "Satu rung: motor dengan pola seal-in",
                "bahasa": "teks",
                "code": """ |   mulai        henti                motor   |
 |----] [----+----]/[------------------( )-----|
 |           |                                 |
 |   motor   |                                 |
 |----] [----+                                 |
 |                                             |
 |   motor        penuh                lampu   |
 |----] [---------]/[------------------( )-----|""",
            },
            {
                "body": [
                    "Ladder dibaca seperti tangga. Dua garis tegak di kiri dan kanan",
                    "adalah rel daya. Setiap anak tangga (rung) adalah satu aturan.",
                    "Listrik dibayangkan mengalir dari kiri ke kanan:",
                    "",
                    "  ] [    kontak normally open: tersambung kalau sinyalnya 1",
                    "  ]/[    kontak normally closed: tersambung kalau sinyalnya 0",
                    "  ( )    koil: output yang menyala kalau ada aliran sampai sini",
                    "",
                    "Rung pertama adalah pola seal-in yang ada di hampir semua",
                    "panel. Tombol mulai cuma ditekan sebentar, tapi begitu motor",
                    "menyala, kontak motor di cabang bawah ikut tersambung dan",
                    "menahan aliran. Motor tetap jalan walaupun tombol mulai sudah",
                    "dilepas, sampai tombol henti ditekan dan memutus aliran.",
                    "",
                    "Rung kedua menyalakan lampu selama motor jalan, kecuali sensor",
                    "penuh aktif.",
                ],
            },
            {
                "heading": "Padanan Structured Text",
                "bahasa": "st",
                "code": """PROGRAM Konveyor
VAR
    mulai, henti, penuh : BOOL;
    motor, lampu, sirene : BOOL;
    tunda : TON;
END_VAR

motor := (mulai OR motor) AND NOT henti;
lampu := motor AND NOT penuh;

tunda(IN := penuh, PT := T#5s);   (* penuh selama 5 detik *)
sirene := tunda.Q;
END_PROGRAM""",
            },
            {
                "body": [
                    "Logika yang sama ditulis sebagai rumus boolean. Sambungan seri",
                    "jadi AND, sambungan paralel jadi OR, dan kontak normally closed",
                    "jadi NOT. := adalah tanda isi, seperti di Pascal.",
                    "",
                    "TON adalah timer on-delay. Outputnya Q baru menyala kalau IN",
                    "sudah menyala terus selama PT, di contoh ini 5 detik. Timer",
                    "dan counter adalah blok yang paling sering dipakai di program",
                    "PLC.",
                ],
            },
            {
                "heading": "Siklus scan",
                "body": [
                    "PLC nggak menjalankan program sekali lalu selesai. Ia mengulang",
                    "tiga langkah terus-menerus, biasanya dalam hitungan milidetik:",
                    "",
                    "  1. Baca semua input dan simpan sebagai gambar input.",
                    "  2. Jalankan rung dari atas ke bawah memakai gambar itu.",
                    "  3. Tulis semua output ke terminal sekaligus.",
                    "",
                    "Satu putaran disebut scan. Karena input dibaca di awal, tombol",
                    "yang ditekan di tengah scan baru terlihat di scan berikutnya.",
                    "Karena rung dijalankan berurutan, rung di bawah sudah melihat",
                    "hasil rung di atasnya dalam scan yang sama, sedangkan rung di",
                    "atas baru melihat hasil rung bawah di scan berikutnya.",
                    "",
                    "Simulasi siklus scan untuk rung motor di Python:",
                ],
            },
            {
                "heading": "Simulasi siklus scan",
                "code": """rung = [
    ("motor", lambda m: (m["mulai"] or m["motor"]) and not m["henti"]),
]
masukan_per_scan = [
    {"mulai": 1, "henti": 0},
    {"mulai": 0, "henti": 0},
    {"mulai": 0, "henti": 1},
    {"mulai": 0, "henti": 0},
]
memori = {"motor": 0}

for nomor, masukan in enumerate(masukan_per_scan, 1):
    memori.update(masukan)                   # 1. baca semua input
    for nama, logika in rung:                # 2. evaluasi rung berurutan
        memori[nama] = int(logika(memori))
    print(f"scan {nomor}: mulai={masukan['mulai']} "
          f"henti={masukan['henti']} motor={memori['motor']}")  # 3. tulis output""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  scan 1: mulai=1 henti=0 motor=1",
                    "  scan 2: mulai=0 henti=0 motor=1",
                    "  scan 3: mulai=0 henti=1 motor=0",
                    "  scan 4: mulai=0 henti=0 motor=0",
                    "",
                    "Di scan 2 tombol mulai sudah dilepas, tapi motor tetap 1 berkat",
                    "seal-in. Di scan 4 henti sudah dilepas lagi, tapi motor tetap",
                    "mati sampai mulai ditekan ulang. Itu perilaku yang diinginkan:",
                    "mesin nggak boleh menyala sendiri sesudah dihentikan.",
                ],
            },
            {
                "heading": "Vendor dan alat",
                "body": [
                    "Setiap merek PLC punya alat pemrogramannya sendiri, dan",
                    "kebanyakan cuma jalan di Windows serta berbayar:",
                    "",
                    "  merek                alat",
                    "  Allen-Bradley        Rockwell Studio 5000",
                    "  Siemens              TIA Portal",
                    "  Omron                Sysmac Studio",
                    "  Mitsubishi           GX Works",
                    "  (bebas)              OpenPLC Editor",
                    "",
                    "Konsepnya sama, tapi tiap vendor punya dialek dan nama blok",
                    "sendiri. Untuk belajar gratis, OpenPLC adalah PLC open source:",
                    "editornya mendukung bahasa IEC 61131-3, dan runtime-nya bisa",
                    "dijalankan di komputer biasa atau Raspberry Pi.",
                ],
            },
            {
                "heading": "LabVIEW: program yang digambar",
                "bahasa": "teks",
                "code": """ Block Diagram (bahasa G)

  [ DAQ Read: suhu ]──●──────────────▶[ > ]──▶[ LED Terlalu Panas ]
                     │                  ▲
                     │         [ 80.0 ]─┘
                     │
                     └──▶[ Waveform Chart ]

 Blok jalan begitu semua kabel masuknya sudah membawa data.""",
            },
            {
                "body": [
                    "LabVIEW dari NI memakai bahasa grafis bernama G. Program",
                    "disusun dengan menyambung blok pakai kabel di Block Diagram,",
                    "sementara tombol dan grafiknya ada di Front Panel. Aturannya",
                    "dataflow: sebuah blok berjalan begitu semua kabel masuknya",
                    "membawa data, bukan karena urutan baris. Akibatnya dua cabang",
                    "yang nggak saling tergantung bisa jalan bersamaan.",
                    "",
                    "LabVIEW dipakai di laboratorium, pengujian otomatis di jalur",
                    "produksi, dan kendali alat ukur, terutama dengan perangkat",
                    "akuisisi data NI. Versi terbarunya LabVIEW 2026 Q3 (Juli 2026),",
                    "dengan dua rilis per tahun. Ada Community Edition gratis untuk",
                    "pemakaian non-komersial.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lulusan SMK dan politeknik jurusan otomasi atau mekatronika di",
                    "Indonesia banyak bekerja dengan PLC Siemens, Omron, dan",
                    "Mitsubishi di pabrik makanan, minuman, otomotif, dan",
                    "pengolahan air. Pekerjaannya sering memperbaiki atau menambah",
                    "rung di program yang sudah berjalan.",
                    "",
                    "Kasus kecil: konveyor sering tetap jalan sebentar sesudah",
                    "sensor penuh aktif, dan karton menumpuk. Programnya punya",
                    "rung lampu (berisi syarat penuh) di atas rung motor, dan motor",
                    "dihentikan oleh lampu itu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ingat siklus scan: rung di atas memakai nilai motor dari",
                    "     scan sebelumnya, jadi ada keterlambatan satu scan.",
                    "  2. Tuliskan urutan rung dan simulasikan beberapa scan di",
                    "     kertas atau dengan skrip Python seperti di atas.",
                    "  3. Pindahkan syarat penuh langsung ke rung motor:",
                    "      motor := (mulai OR motor) AND NOT henti AND NOT penuh;",
                    "  4. Uji di OpenPLC atau simulator vendor dulu, baru unggah ke",
                    "     PLC saat mesin berhenti dan sudah dikunci sesuai prosedur",
                    "     keselamatan.",
                ],
            },
        ],
    },
    {
        "title": "44. Solidity dan Bahasa Smart Contract Lain",
        "sections": [
            {
                "body": [
                    "Smart contract adalah program yang disimpan dan dijalankan di",
                    "blockchain. Blockchain di sini adalah buku catatan bersama yang",
                    "disalin ribuan komputer di seluruh dunia, sehingga nggak ada",
                    "satu pihak pun yang bisa mengubah isinya sendirian. Begitu",
                    "kontrak dipasang (deploy), kodenya nggak bisa diubah lagi, dan",
                    "siapa pun bisa memanggil fungsinya.",
                    "",
                    "Akibatnya ada dua hal yang beda dari program biasa. Pertama,",
                    "setiap langkah komputasi dibayar dengan gas, biaya kecil dalam",
                    "mata uang kripto jaringan itu. Kode yang boros berarti pemakai",
                    "membayar lebih mahal. Kedua, bug di kontrak yang memegang uang",
                    "sering berarti uangnya hilang, dan perbaikannya nggak bisa",
                    "sekadar menyunting berkas.",
                    "",
                    "Solidity adalah bahasa smart contract paling banyak dipakai,",
                    "untuk Ethereum dan jaringan lain yang memakai mesin virtual",
                    "yang sama, EVM (Ethereum Virtual Machine). Sintaksnya mirip",
                    "JavaScript dan C++. Versi terbarunya 0.8.37 (September 2026),",
                    "lisensi kompilatornya GPL-3.0. Di Survei Stack Overflow 2026",
                    "pemakainya 0,8% responden.",
                ],
            },
            {
                "heading": "Halo Dunia ala smart contract",
                "bahasa": "solidity",
                "code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Halo {
    function sapa() public pure returns (string memory) {
        return "Halo, Dunia!";
    }
}""",
            },
            {
                "body": [
                    "Smart contract nggak mencetak ke layar, karena nggak ada layar",
                    "di blockchain. Halo Dunia-nya berupa fungsi yang mengembalikan",
                    "teks, lalu dipanggil lewat alat seperti Remix atau dari tes.",
                    "",
                    "  - Baris SPDX menyebut lisensi kode sumber kontrak itu.",
                    "  - pragma solidity ^0.8.20 artinya kontrak ini butuh kompilator",
                    "    versi 0.8.20 atau lebih baru di jalur 0.8.",
                    "  - pure artinya fungsi nggak membaca maupun mengubah data",
                    "    kontrak. view artinya cuma membaca. Fungsi pure atau view",
                    "    yang dipanggil langsung dari aplikasi, bukan dari dalam",
                    "    transaksi, nggak membayar gas.",
                ],
            },
            {
                "heading": "Token sederhana",
                "bahasa": "solidity",
                "code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TokenKelas {
    string public nama = "Token Kelas";
    address public pemilik;
    uint256 public totalPasokan;
    mapping(address => uint256) public saldo;

    event Transfer(address indexed dari, address indexed ke, uint256 jumlah);

    constructor() {
        pemilik = msg.sender;
    }

    function mint(address ke, uint256 jumlah) external {
        require(msg.sender == pemilik, "bukan pemilik");
        saldo[ke] += jumlah;
        totalPasokan += jumlah;
        emit Transfer(address(0), ke, jumlah);
    }

    function transfer(address ke, uint256 jumlah) external {
        require(saldo[msg.sender] >= jumlah, "saldo kurang");
        saldo[msg.sender] -= jumlah;
        saldo[ke] += jumlah;
        emit Transfer(msg.sender, ke, jumlah);
    }

    function saldoKu() external view returns (uint256) {
        return saldo[msg.sender];
    }
}""",
            },
            {
                "body": [
                    "Kontrak ini dikompilasi dengan solc 0.8.37 tanpa error. Bagian",
                    "yang penting:",
                    "",
                    "  - Variabel di luar fungsi (pemilik, saldo, totalPasokan)",
                    "    adalah state, yaitu data yang disimpan permanen di",
                    "    blockchain. Menulis state paling mahal gas-nya.",
                    "  - mapping(address => uint256) mirip dict Python: kunci alamat",
                    "    akun, nilai jumlah token. Kunci yang belum pernah diisi",
                    "    bernilai 0.",
                    "  - msg.sender adalah alamat yang memanggil fungsi. Di",
                    "    constructor, itu alamat yang memasang kontrak.",
                    "  - require(syarat, \"alasan\") membatalkan seluruh transaksi",
                    "    kalau syaratnya salah. Ini disebut revert: semua perubahan",
                    "    di transaksi itu dibatalkan, seolah nggak pernah terjadi.",
                    "  - event dan emit mencatat kejadian ke log transaksi. Aplikasi",
                    "    web membaca log itu untuk menampilkan riwayat.",
                    "",
                    "Sejak Solidity 0.8.0, operasi aritmetika yang meluap",
                    "(overflow) otomatis membatalkan transaksi. Di kode lama sebelum",
                    "0.8, kamu bakal melihat pustaka SafeMath yang dulu dipakai untuk",
                    "keperluan ini.",
                    "",
                    "Token sungguhan biasanya mengikuti standar ERC-20 dan nggak",
                    "ditulis dari nol. Pustaka OpenZeppelin menyediakan kontrak",
                    "ERC-20 yang sudah diaudit, dan kamu tinggal mewarisinya.",
                ],
            },
            {
                "heading": "Reentrancy: bug yang paling terkenal",
                "bahasa": "solidity",
                "code": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CelenganRawan {
    mapping(address => uint256) public simpanan;

    function setor() external payable {
        simpanan[msg.sender] += msg.value;
    }

    // RAWAN: uang dikirim dulu, catatan baru dinolkan sesudahnya
    function tarik() external {
        uint256 jumlah = simpanan[msg.sender];
        (bool berhasil, ) = msg.sender.call{value: jumlah}("");
        require(berhasil, "gagal kirim");
        simpanan[msg.sender] = 0;
    }
}

contract CelenganAman {
    mapping(address => uint256) public simpanan;

    function setor() external payable {
        simpanan[msg.sender] += msg.value;
    }

    // AMAN: cek, ubah catatan, baru berinteraksi dengan pihak luar
    function tarik() external {
        uint256 jumlah = simpanan[msg.sender];
        require(jumlah > 0, "simpanan kosong");
        simpanan[msg.sender] = 0;
        (bool berhasil, ) = msg.sender.call{value: jumlah}("");
        require(berhasil, "gagal kirim");
    }
}""",
            },
            {
                "body": [
                    "Di CelenganRawan, uang dikirim dulu lewat call, baru simpanan",
                    "dinolkan. Masalahnya, kalau penerimanya juga kontrak, call itu",
                    "menjalankan kode milik penerima. Kode jahat bisa memanggil",
                    "tarik() lagi sebelum baris simpanan = 0 sempat dijalankan,",
                    "dan menarik uang yang sama berulang-ulang sampai celengannya",
                    "kosong. Serangan ini disebut reentrancy, dan pernah menguras",
                    "dana besar, misalnya pada kasus The DAO tahun 2016.",
                    "",
                    "CelenganAman memakai pola cek, ubah, interaksi",
                    "(checks-effects-interactions): periksa syarat, ubah catatan,",
                    "baru kirim uang. Saat penerima mencoba masuk lagi, simpanannya",
                    "sudah nol. OpenZeppelin juga menyediakan ReentrancyGuard untuk",
                    "mengunci fungsi selama sedang berjalan.",
                    "",
                    "Jebakan: kode kontrak yang lolos kompilasi dan lolos tes biasa",
                    "belum tentu aman. Kontrak yang memegang uang sungguhan diaudit",
                    "orang lain dulu sebelum dipasang.",
                ],
            },
            {
                "heading": "Alat kerja Solidity",
                "bahasa": "terminal",
                "code": """npm install solc              # kompilator solcjs di proyek
npx solcjs --bin --abi TokenKelas.sol -o hasil

curl -L https://foundry.paradigm.xyz | bash   # pasang foundryup
foundryup                     # pasang forge dan kawan-kawan
forge init proyek-token && cd proyek-token
forge test                    # tes ditulis dengan Solidity""",
            },
            {
                "body": [
                    "Untuk mencoba tanpa memasang apa pun, buka Remix IDE di",
                    "browser: tulis kontrak, kompilasi, lalu pasang ke blockchain",
                    "tiruan dan panggil fungsinya dengan tombol. Untuk proyek",
                    "sungguhan, orang memakai Foundry (tes ditulis dengan Solidity)",
                    "atau Hardhat (tes ditulis dengan JavaScript atau TypeScript).",
                    "Aplikasi web berbicara dengan kontrak lewat pustaka seperti",
                    "ethers.js atau viem.",
                ],
            },
            {
                "heading": "Vyper",
                "bahasa": "vyper",
                "code": "# pragma version ^0.4.0\n\n@external\n@view\ndef halo() -> String[32]:\n    return \"Halo, Dunia!\"",
            },
            {
                "body": [
                    "Vyper juga untuk EVM, tapi sintaksnya mirip Python dan",
                    "fiturnya sengaja dibatasi supaya kontrak gampang diaudit. Nggak",
                    "ada pewarisan kelas, dan string wajib punya panjang maksimum",
                    "seperti String[32]. Versi stabilnya 0.4.3, dan 0.5.0 masih",
                    "beta. Pasang dengan pip install vyper. Protokol Curve Finance",
                    "terkenal memakai Vyper. Pada 2023, beberapa pool Curve diretas",
                    "karena bug di kompilator Vyper versi lama, contoh nyata bahwa",
                    "kompilator pun bisa salah.",
                ],
            },
            {
                "heading": "Move",
                "bahasa": "move",
                "code": """module halo::halo;

use std::string::String;

public fun halo(): String {
    b"Halo, Dunia!".to_string()
}""",
            },
            {
                "body": [
                    "Move berasal dari proyek blockchain Diem milik Meta dan",
                    "sekarang dipakai jaringan Sui dan Aptos. Ide utamanya: aset",
                    "diperlakukan sebagai resource yang nggak bisa disalin dan nggak",
                    "bisa hilang begitu saja. Compiler menolak kode yang menggandakan",
                    "atau membuang token tanpa sengaja. Versinya mengikuti edisi",
                    "dan versi Sui CLI yang sering berganti, jadi rujuk dokumentasi",
                    "jaringan yang kamu pakai.",
                ],
            },
            {
                "heading": "Cairo",
                "bahasa": "cairo",
                "code": """#[executable]
fn main() {
    println!("Halo, Dunia!");
}""",
            },
            {
                "body": [
                    "Cairo mirip Rust dan dipakai di Starknet. Programnya bisa",
                    "dibuktikan secara kriptografis sudah dijalankan dengan benar,",
                    "tanpa orang lain perlu menjalankannya ulang. Teknik ini disebut",
                    "zero-knowledge proof. Versi terbarunya 2.21.0 (Oktober 2026),",
                    "dengan alat build Scarb.",
                    "",
                    "  bahasa    jaringan              gaya          ciri",
                    "  Solidity  Ethereum dan EVM      mirip JS/C++  paling banyak",
                    "  Vyper     Ethereum dan EVM      mirip Python  dibatasi, mudah",
                    "                                                diaudit",
                    "  Move      Sui, Aptos            mirip Rust    aset = resource",
                    "  Cairo     Starknet              mirip Rust    bisa dibuktikan",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Token ERC-20, NFT, bursa terdesentralisasi, dan protokol",
                    "pinjaman di Ethereum ditulis dengan Solidity atau Vyper. Karena",
                    "kodenya publik dan memegang uang, perusahaan audit keamanan",
                    "kontrak dan program bug bounty jadi bagian penting ekosistem",
                    "ini.",
                    "",
                    "Kasus kecil: kamu diminta meninjau fungsi tarik di kontrak",
                    "celengan sebuah proyek kampus sebelum dipasang ke jaringan uji.",
                    "Fungsinya mengirim uang dengan call lalu menolkan simpanan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari setiap panggilan ke luar (call, transfer ke kontrak",
                    "     lain) dan lihat apakah ada perubahan state sesudahnya.",
                    "  2. Kalau ada, urutkan ulang jadi cek, ubah, interaksi:",
                    "      require(jumlah > 0, \"simpanan kosong\");",
                    "      simpanan[msg.sender] = 0;",
                    "      (bool berhasil, ) = msg.sender.call{value: jumlah}(\"\");",
                    "  3. Tambahkan ReentrancyGuard dari OpenZeppelin sebagai lapisan",
                    "     kedua.",
                    "  4. Tulis tes di Foundry dengan kontrak penyerang yang memanggil",
                    "     tarik() berulang, dan pastikan serangannya gagal.",
                ],
            },
        ],
    },
    {
        "title": "45. Peta Konfigurasi dan Integrasi: Nix, XSLT, Ballerina",
        "sections": [
            {
                "body": [
                    "Nggak semua bahasa dibuat untuk menulis aplikasi. Sebagian",
                    "dibuat untuk satu pekerjaan saja, dan untuk pekerjaan itu ia",
                    "lebih ringkas dan lebih aman daripada bahasa umum. Bahasa",
                    "seperti ini disebut DSL (domain-specific language).",
                    "",
                    "Materi ini membahas tiga yang paling mungkin kamu temui:",
                    "",
                    "  - Nix: menulis paket dan konfigurasi sistem supaya hasilnya",
                    "    bisa diulang persis sama di komputer mana pun.",
                    "  - XSLT: mengubah dokumen XML jadi XML lain, HTML, atau teks.",
                    "  - Ballerina: menyambungkan API dan layanan.",
                ],
            },
            {
                "heading": "Nix: Halo Dunia (halo.nix)",
                "bahasa": "nix",
                "code": "let\n  sapa = nama: \"Halo, ${nama}!\";\nin\nsapa \"Dunia\"",
            },
            {
                "body": [
                    "Nix adalah satu nama untuk tiga hal: bahasa Nix, package",
                    "manager Nix, dan distro Linux NixOS. Bahasanya fungsional dan",
                    "kecil. nama: \"...\" adalah fungsi dengan satu parameter, ${nama}",
                    "menyisipkan nilai ke dalam teks, dan let ... in memberi nama",
                    "sementara. Jalankan dengan:",
                    "",
                    "  nix-instantiate --eval halo.nix",
                    "",
                    "Keluarannya \"Halo, Dunia!\" lengkap dengan tanda kutipnya,",
                    "karena Nix mencetak nilai, bukan teks polos.",
                    "",
                    "Versi terbarunya Nix 2.35.3 (Oktober 2026), lisensi LGPL-2.1.",
                    "Fedora 44 mengemas 2.34.8 lewat sudo dnf install nix. Di Survei",
                    "Stack Overflow 2026, 4,4% responden memakai Nix, hampir sama",
                    "dengan Dart (4,9%) dan jauh di atas Elixir (2,6%).",
                ],
            },
            {
                "heading": "Malas: yang nggak dipakai nggak dihitung",
                "bahasa": "nix",
                "code": """let
  harga = { kopi = 12000; teh = 8000; roti = 15000; };
  total = harga.kopi + harga.teh;
  rusak = throw "nilai ini nggak pernah dihitung";
  hasil = { inherit total; cadangan = rusak; };
in
hasil.total""",
            },
            {
                "body": [
                    "Hasilnya 20000. Nilai rusak berisi throw, yang akan",
                    "menghentikan evaluasi dengan error kalau dihitung. Tapi Nix",
                    "malas (lazy): sebuah nilai baru dihitung kalau benar dipakai.",
                    "Karena yang diminta cuma hasil.total, cadangan nggak pernah",
                    "disentuh dan error-nya nggak pernah terjadi.",
                    "",
                    "Sifat malas ini penting untuk Nixpkgs, kumpulan resep lebih",
                    "dari seratus ribu paket. Saat kamu memasang satu paket, Nix",
                    "cuma mengevaluasi resep yang dibutuhkan paket itu.",
                ],
            },
            {
                "heading": "Lingkungan kerja yang sama untuk satu tim (shell.nix)",
                "bahasa": "nix",
                "code": """{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [ pkgs.python3 pkgs.nodejs_22 pkgs.sqlite ];

  shellHook = ''
    echo "Lingkungan siap: $(python3 --version)"
  '';
}""",
            },
            {
                "body": [
                    "Jalankan nix-shell di folder itu, dan kamu masuk ke shell yang",
                    "punya Python, Node.js 22, dan SQLite persis versi yang",
                    "ditentukan Nixpkgs, tanpa memasangnya ke sistem. Selama kalian",
                    "memakai revisi Nixpkgs yang sama, temanmu yang menjalankan",
                    "perintah itu mendapat versi yang sama persis.",
                    "",
                    "Rahasianya ada di /nix/store. Setiap paket dibangun dari",
                    "derivation, yaitu resep lengkap berisi sumber kode, dependensi,",
                    "dan langkah build. Semua masukan itu di-hash, lalu hasilnya",
                    "disimpan di folder bernama hash tersebut, misalnya",
                    "/nix/store/<hash>-python3-<versi>. Masukan beda menghasilkan",
                    "hash beda, jadi dua versi bisa hidup berdampingan tanpa saling",
                    "timpa.",
                    "",
                    "Proyek modern biasanya memakai flakes (berkas flake.nix plus",
                    "flake.lock yang mengunci versi Nixpkgs), dijalankan dengan nix",
                    "develop. Flakes masih berlabel eksperimental, tapi sudah",
                    "dipakai luas. Pemakaian Nix untuk DevOps dibahas lebih jauh di",
                    "kurikulum devops.",
                    "",
                    "Jebakan: pesan error Nix terkenal susah dibaca, sering",
                    "menunjuk ke dalam Nixpkgs alih-alih ke berkasmu. Mulai dari",
                    "baris paling bawah pesan, lalu cari nama berkasmu sendiri.",
                ],
            },
            {
                "heading": "XSLT: data menu (menu.xml)",
                "bahasa": "xml",
                "code": """<?xml version="1.0" encoding="UTF-8"?>
<menu>
  <item kategori="makanan">
    <nama>Nasi Goreng</nama>
    <harga>18000</harga>
  </item>
  <item kategori="minuman">
    <nama>Es Teh</nama>
    <harga>5000</harga>
  </item>
  <item kategori="makanan">
    <nama>Mie Ayam</nama>
    <harga>15000</harga>
  </item>
</menu>""",
            },
            {
                "heading": "Stylesheet XSLT (menu.xsl)",
                "bahasa": "xml",
                "code": """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="text"/>

  <xsl:template match="/menu">
    <xsl:text>Menu makanan:&#10;</xsl:text>
    <xsl:apply-templates select="item[@kategori='makanan']">
      <xsl:sort select="harga" data-type="number"/>
    </xsl:apply-templates>
    <xsl:text>Jumlah item: </xsl:text>
    <xsl:value-of select="count(item)"/>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>

  <xsl:template match="item">
    <xsl:text>- </xsl:text>
    <xsl:value-of select="nama"/>
    <xsl:text>: Rp</xsl:text>
    <xsl:value-of select="harga"/>
    <xsl:text>&#10;</xsl:text>
  </xsl:template>
</xsl:stylesheet>""",
            },
            {
                "body": [
                    "Jalankan dengan xsltproc, yang sudah terpasang di Fedora:",
                    "",
                    "  xsltproc menu.xsl menu.xml",
                    "",
                    "Keluarannya (diuji dengan libxslt 1.1.43):",
                    "",
                    "  Menu makanan:",
                    "  - Mie Ayam: Rp15000",
                    "  - Nasi Goreng: Rp18000",
                    "  Jumlah item: 3",
                    "",
                    "XSLT bekerja dengan template, bukan perulangan. Template",
                    "pertama cocok dengan elemen menu. apply-templates memilih item",
                    "berkategori makanan dengan ekspresi XPath, mengurutkannya",
                    "menurut harga, lalu menyerahkan tiap item ke template yang",
                    "cocok dengannya, yaitu template kedua. Cara berpikirnya mirip",
                    "CSS: kamu menulis aturan untuk bentuk tertentu, dan mesinnya",
                    "yang menelusuri dokumen.",
                    "",
                    "Standar terbarunya XSLT 3.0 (W3C, 2017), dan XSLT 4.0 masih",
                    "draf. xsltproc cuma mendukung XSLT 1.0. Untuk 3.0 dipakai",
                    "Saxon-HE, versi terbarunya 13.1, yang jalan di Java. XSLT masih",
                    "hidup di dokumen teknis (DocBook dan DITA diubah jadi HTML atau",
                    "PDF), faktur elektronik, dan laporan keuangan XBRL.",
                ],
            },
            {
                "heading": "Ballerina",
                "bahasa": "ballerina",
                "code": """import ballerina/http;

service /halo on new http:Listener(8080) {
    resource function get .() returns string {
        return "Halo, Dunia!";
    }
}""",
            },
            {
                "body": [
                    "Ballerina dari WSO2 dirancang khusus untuk integrasi: memanggil",
                    "API, mengolah JSON, dan menyambungkan layanan. Layanan HTTP",
                    "adalah bagian dari bahasanya. Contoh di atas membuat endpoint",
                    "GET /halo di port 8080 tanpa framework tambahan. Versi",
                    "terbarunya 2201.14.1 (Swan Lake Update 14, Oktober 2026),",
                    "lisensi Apache-2.0. Popularitasnya menurun di peringkat RedMonk,",
                    "jadi pelajari kalau tempat kerjamu memang memakainya.",
                ],
            },
            {
                "heading": "Kapan bahasa khusus lebih tepat",
                "body": [
                    "  - Kalau hasilnya harus bisa diulang persis dan dicek orang",
                    "    lain, pilih Nix. Skrip Bash yang memasang paket satu per",
                    "    satu hasilnya bergantung pada keadaan mesin saat dijalankan.",
                    "  - Kalau masukannya XML dan keluarannya dokumen: XSLT lebih",
                    "    ringkas daripada menulis penelusur pohon sendiri di Python.",
                    "  - Kalau pekerjaan utamanya menyambung API: Ballerina atau alat",
                    "    integrasi serupa mengurangi kode penghubung.",
                    "",
                    "Sebaliknya, jangan memaksa DSL di luar wilayahnya. Logika",
                    "bisnis rumit yang ditulis dengan XSLT atau Nix cepat jadi",
                    "susah dibaca. Untuk itu, bahasa umum seperti Python lebih",
                    "cocok.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim yang memakai NixOS atau Nix menyimpan konfigurasi server dan",
                    "lingkungan pengembangan di Git, sehingga mesin baru bisa",
                    "disiapkan dengan satu perintah. Kantor pajak dan perbankan di",
                    "banyak negara bertukar data dalam XML, dan XSLT dipakai untuk",
                    "mengubahnya jadi laporan yang bisa dibaca manusia.",
                    "",
                    "Kasus kecil: proyek PKL-mu butuh Python 3 dan SQLite, tapi",
                    "laptop tiap anggota tim punya versi berbeda, dan skrip yang",
                    "jalan di satu laptop gagal di laptop lain.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pasang Nix di semua laptop (di Fedora lewat dnf, lalu",
                    "     aktifkan daemon sesuai panduan paketnya).",
                    "  2. Taruh shell.nix di akar repositori:",
                    "      pkgs.mkShell { packages = [ pkgs.python3 pkgs.sqlite ]; }",
                    "  3. Minta semua anggota menjalankan nix-shell sebelum bekerja,",
                    "     lalu cek python3 --version di tiap laptop. Kalau channel",
                    "     Nixpkgs semua orang sama, hasilnya juga sama.",
                    "  4. Kalau ingin versi Nixpkgs ikut terkunci, pindah ke",
                    "     flake.nix dan commit flake.lock bersama kode.",
                ],
            },
        ],
    },
]
