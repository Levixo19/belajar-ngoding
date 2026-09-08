JAVASCRIPT_MATERIALS = [
    {
        "title": "1. Pengenalan JavaScript & Cara Menjalankan",
        "sections": [
            {
                "body": [
                    "Apa itu JavaScript?",
                    "  - Bahasa pemrograman utama untuk web, berjalan di browser.",
                    "  - Dibuat oleh Brendan Eich tahun 1995 (awalnya untuk Netscape).",
                    "  - Sejak ada Node.js (2009), JavaScript juga dipakai di server/backend.",
                    "  - Satu-satunya bahasa yang berjalan NATIF di semua browser modern.",
                    "",
                    "JavaScript dipakai untuk:",
                    "  - Frontend web: interaktivitas halaman (React, Vue, Angular).",
                    "  - Backend: server & API (Node.js, Express).",
                    "  - Mobile app: React Native.",
                    "  - Desktop app: Electron (VS Code dibuat dengan ini!).",
                    "",
                    "Cara menjalankan JavaScript (3 cara umum):",
                    "  1. Browser Console: tekan F12 > tab Console, ketik kode langsung.",
                    "  2. File HTML: <script>...</script> atau <script src='file.js'>.",
                    "  3. Node.js (di luar browser): node nama_file.js",
                    "",
                    "Contoh kode di aplikasi ini dijalankan dengan node. Artinya objek khas",
                    "BROWSER (document, alert, localStorage) tidak ada di sini, dan sebaliknya",
                    "objek khas NODE (process, require) tidak ada di browser. Tidak ada satu",
                    "lingkungan pun yang punya keduanya sekaligus. Jadi kalau sebuah contoh",
                    "menyebut document, contoh itu memang ditulis untuk browser - bukan",
                    "kodenya yang salah.",
                ]
            },
            {
                "heading": "Program pertama (jalankan dengan: node hello.js)",
                "code": """console.log("Halo Dunia!");
console.log("Aku sedang belajar JavaScript.");"""
            },
            {
                "body": [
                    "Penjelasan:",
                    "  console.log(...)  -> fungsi bawaan untuk menampilkan output.",
                    "  Titik koma (;)     -> opsional di JS (ada 'Automatic Semicolon",
                    "                        Insertion'), TAPI disarankan tetap dipakai",
                    "                        agar kode konsisten & terhindar dari bug halus.",
                    "",
                    "Aturan penting sintaks JavaScript:",
                    "  1. Case-sensitive: nama beda dengan Nama.",
                    "  2. Blok kode pakai kurung kurawal { } (mirip Java/C).",
                    "  3. Komentar satu baris: // teks",
                    "  4. Komentar banyak baris: /* teks */",
                    "  5. Komentar dokumentasi: /** teks */ - bentuk berbintang dua.",
                    "     Kamu akan melihatnya di atas hampir tiap fungsi di kode nyata.",
                    "     Isinya punya aturan sendiri (namanya JSDoc) dan dibahas di",
                    "     materi 'Membaca Repo JavaScript Sungguhan'.",
                    "  6. File JavaScript berekstensi .js",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel (var, let, const) & Tipe Data",
        "sections": [
            {
                "body": [
                    "JavaScript punya 3 cara deklarasi variabel - PENTING dipahami",
                    "perbedaannya karena ini sumber bug klasik di JS:",
                    "",
                    "  var    -> cara LAMA (sebelum ES6/2015). Function-scoped,",
                    "            bisa di-redeclare, HINDARI dipakai di kode baru.",
                    "  let    -> cara MODERN untuk variabel yang NILAINYA BERUBAH.",
                    "            Block-scoped (hanya dikenal di dalam { } terdekat).",
                    "  const  -> untuk nama yang TIDAK DI-ASSIGN ULANG.",
                    "            Block-scoped juga. GUNAKAN INI SEBAGAI DEFAULT,",
                    "            baru pakai 'let' jika memang perlu diubah nanti.",
                    "",
                    "  const nama = \"Andi\";      // tidak bisa di-assign ulang",
                    "  let umur = 20;             // bisa diubah: umur = 21;",
                    "",
                    "Hati-hati pada kata 'konstan'. Yang dikunci const adalah PENUGASAN",
                    "ULANG, bukan isinya. Untuk array dan object, isinya tetap boleh berubah:",
                    "",
                    "  const arr = [];",
                    "  arr.push(1);      // SAH - arr masih menunjuk array yang sama",
                    "  arr = [1];        // TypeError: Assignment to constant variable.",
                    "",
                    "Kenapa 'menunjuk' dan bukan 'berisi' dibahas di materi",
                    "'Nilai vs Referensi & Menyalin Data'.",
                ]
            },
            {
                "heading": "Tipe data primitif JavaScript",
                "code": """let umur = 20;                  // number (JS TIDAK bedakan int/float)
let harga = 15000.50;           // number juga
let nama = "Budi";              // string
let lulus = true;               // boolean
let kosong = null;               // null: sengaja 'tidak ada nilai'
let belumDiisi;                  // undefined: belum diberi nilai
let id = Symbol("id");           // symbol: nilai unik (jarang dipakai pemula)
let bigNum = 123456789012345678901234567890n;  // BigInt (angka sangat besar)

console.log(typeof umur);       // "number"
console.log(typeof nama);       // "string"
console.log(typeof belumDiisi); // "undefined"
console.log(typeof null);       // "object" (ini QUIRK/bug lama JS, sudah diketahui)"""
            },
            {
                "body": [
                    "Perbedaan null vs undefined:",
                    "  undefined -> variabel dideklarasikan tapi BELUM diisi nilai.",
                    "  null      -> SENGAJA diisi 'kosong/tidak ada' oleh programmer.",
                    "",
                    "\"JS TIDAK bedakan int/float\" di komentar atas artinya SEMUA angka -",
                    "termasuk 20 dan 7 - disimpan sebagai float 64-bit. Akibatnya 0.1 + 0.2",
                    "tidak persis 0.3, dan bilangan bulat punya batas aman. Rinciannya di",
                    "materi 'Angka: Konversi Tipe, Math, dan Presisi Desimal'.",
                    "",
                    "Aturan penamaan variabel:",
                    "  1. Boleh huruf, angka, _, $. Tidak boleh diawali angka.",
                    "  2. Konvensi JS: camelCase untuk variabel/fungsi (jumlahSiswa).",
                    "  3. Konstanta global sering ditulis UPPER_SNAKE_CASE: MAX_SIZE.",
                    "",
                    "Template literal (cara modern gabung teks, pakai backtick `):",
                    "  const nama = \"Andi\"; const umur = 20;",
                    "  console.log(`Nama saya ${nama}, umur ${umur} tahun`);",
                    "  console.log(`Tahun depan: ${umur + 1}`);   // bisa ekspresi",
                    "  Bisa multi-baris langsung tanpa karakter escape khusus.",
                ]
            },
        ],
    },
    {
        "title": "3. Operator",
        "sections": [
            {
                "body": [
                    "Operator aritmatika:",
                    "  +  penjumlahan    -  pengurangan",
                    "  *  perkalian      /  pembagian (SELALU desimal jika perlu)",
                    "  %  modulus        ** pangkat (ES2016+)",
                    "  ++ increment      -- decrement",
                    "",
                    "PERHATIAN KHUSUS operator + pada JavaScript:",
                    "  5 + 3        -> 8        (angka + angka = angka)",
                    "  \"5\" + 3      -> \"53\"     (string + angka = STRING, digabung!)",
                    "  5 + \"3\"      -> \"53\"     (sama, otomatis jadi string)",
                    "  \"5\" - 3      -> 2        (- , *, / otomatis convert ke angka)",
                    "  Ini disebut 'type coercion' - sering jadi sumber bug pemula!",
                ]
            },
            {
                "body": [
                    "Operator perbandingan - JavaScript punya DUA jenis:",
                    "  ==   perbandingan LONGGAR (loose), MELAKUKAN type coercion.",
                    "  ===  perbandingan KETAT (strict), TIDAK convert tipe.",
                    "  !=   tidak sama (longgar)      !==  tidak sama (ketat)",
                    "",
                    "  5 == \"5\"    -> true   (\"5\" di-convert jadi angka dulu)",
                    "  5 === \"5\"   -> false  (beda tipe: number vs string)",
                    "  null == undefined   -> true",
                    "  null === undefined  -> false",
                    "",
                    "ATURAN EMAS: SELALU gunakan === dan !== (strict), HINDARI",
                    "== dan != karena perilaku coercion-nya sering membingungkan.",
                ]
            },
            {
                "heading": "Operator logika & nullish coalescing",
                "code": """console.log(5 > 3 && 2 > 1);   // true
console.log(5 > 3 || 2 > 5);   // true
console.log(!(5 > 3));         // false

// Short-circuit evaluation
const nama = null;
console.log(nama || "Tanpa Nama");        // "Tanpa Nama" (jika nama falsy)

// Nullish coalescing (??) - ES2020, BEDA dari ||
// || anggap 0, "", false sebagai 'kosong'. ?? HANYA anggap null/undefined.
let stok = 0;
console.log(stok || 10);   // 10   (bug! padahal stok=0 itu valid)
console.log(stok ?? 10);   // 0    (benar, karena 0 bukan null/undefined)

// Optional chaining (?.) - ES2020, aman akses property bersarang
const user = { profil: null };
console.log(user.profil?.nama);   // undefined (tidak error walau profil null)"""
            },
            {
                "body": [
                    "Tiga operator turunan yang belum muncul di atas, padahal ketiganya ada",
                    "di kode sehari-hari:",
                    "",
                    "1. Logical assignment (ES2021) - menggabungkan operator logika dengan",
                    "   tanda sama dengan, jadi 'isi kalau perlu' cukup satu baris:",
                    "     a ??= b   isi a HANYA kalau a null/undefined",
                    "     a ||= b   isi a kalau a falsy (0 dan \"\" ikut kena)",
                    "     a &&= b   isi a HANYA kalau a truthy",
                    "",
                    "2. Optional chaining bukan cuma bentuk titik yang kamu lihat di atas:",
                    "     obj?.[key]     indeks opsional, untuk nama key yang dinamis",
                    "     callback?.()   PANGGIL fungsinya hanya kalau fungsinya ada",
                    "   Bentuk kedua itu pengganti 'if (callback) callback();'.",
                    "",
                    "3. Operator bitwise: &  |  ^  ~  <<  >>  >>>",
                    "   Ia bekerja pada BIT angka, bukan pada nilainya. Kamu jarang menulisnya",
                    "   sendiri, tapi wajib mengenalinya - kalau tidak, x | 0 di kode orang",
                    "   akan terbaca sebagai OR biasa dan artinya salah total.",
                ],
            },
            {
                "heading": "Logical assignment & optional chaining bentuk lain",
                "code": """// ---- Logical assignment: isi HANYA kalau perlu ----
const opsi = { judul: "Laporan", timeout: 0 };

opsi.timeout ??= 5000;          // isi HANYA kalau null/undefined -> 0 dipertahankan
opsi.ukuran ??= "A4";           // ukuran belum ada -> jadi "A4"
opsi.judul ||= "Tanpa Judul";   // isi kalau FALSY -> judul sudah terisi, tetap
console.log(opsi);              // { judul: 'Laporan', timeout: 0, ukuran: 'A4' }

let pesan = "halo";
pesan &&= pesan.toUpperCase();  // ubah HANYA kalau isinya truthy
console.log(pesan);             // HALO

// ---- Optional chaining bukan cuma untuk titik ----
const kunci = "nama";
const user = { nama: "Andi" };
console.log(user?.[kunci]);         // Andi        indeks opsional
console.log(user.alamat?.[kunci]);  // undefined   aman, bukan TypeError

function jalankan(selesai) {
    selesai?.();                    // panggil HANYA kalau callback-nya dikirim
}
jalankan();                                        // aman, tidak error
jalankan(() => console.log("callback dipanggil")); // callback dipanggil"""
            },
            {
                "heading": "Operator bitwise dan idiom yang membuatnya muncul",
                "code": """// Operator bitwise bekerja pada BIT angka, setelah diubah ke bulat 32-bit.
console.log(5 & 3);     // 1    0101 & 0011 = 0001   AND
console.log(5 | 3);     // 7    0101 | 0011 = 0111   OR
console.log(5 ^ 3);     // 6    0101 ^ 0011 = 0110   XOR
console.log(~5);        // -6   NOT; ~x selalu sama dengan -(x + 1)
console.log(5 << 1);    // 10   geser kiri 1 bit  = dikali 2
console.log(5 >> 1);    // 2    geser kanan 1 bit = dibagi 2, dibulatkan ke bawah
console.log(-8 >>> 28); // 15   geser kanan TANPA tanda: angka negatif jadi besar

// Idiom yang membuat operator ini muncul di kode nyata:
console.log(7.9 | 0);              // 7    memotong desimal, bukan membulatkan
console.log(~~(-7.9));             // -7   idiom lama yang sama, NOT dua kali
console.log(~"abc".indexOf("z"));  // 0    falsy  -> berarti TIDAK ketemu
console.log(~"abc".indexOf("b"));  // -2   truthy -> berarti ketemu

// Flag: banyak boolean dipadatkan jadi SATU angka.
const BACA = 1, TULIS = 2, HAPUS = 4;
const izin = BACA | TULIS;          // 3 -> bit baca dan tulis menyala
console.log((izin & TULIS) !== 0);  // true  boleh menulis
console.log((izin & HAPUS) !== 0);  // false tidak boleh menghapus

// Hash string sederhana - bentuk yang sering ditemui di utilitas kecil.
let hash = 0;
for (const ch of "halo") {
    hash = (hash << 5) - hash + ch.charCodeAt(0);
    hash |= 0;                      // paksa hasilnya kembali ke 32-bit
}
console.log(hash);                  // 3194940"""
            },
        ],
    },
    {
        "title": "4. Angka: Konversi Tipe, Math, dan Presisi Desimal",
        "sections": [
            {
                "body": [
                    "Materi Operator menunjukkan JavaScript mengubah tipe SENDIRI: \"5\" + 3 jadi \"53\".",
                    "Itu coercion OTOMATIS, dan hasilnya sering bukan yang kita mau. Di kode nyata",
                    "kita hampir selalu mengubah tipe dengan SENGAJA -- namanya konversi eksplisit.",
                    "",
                    "Kenapa ini penting sekali: hampir SEMUA data yang masuk program berupa STRING.",
                    "  - isi kotak input di halaman web           -> string",
                    "  - argumen dari terminal (process.argv)     -> string",
                    "  - isi berkas teks dan balasan dari server  -> string",
                    "Kalau lupa mengubahnya jadi angka, operator + akan MENGGABUNG, bukan menjumlah.",
                    "Bug ini tidak melempar error apa pun; ia hanya memberi hasil salah dalam diam.",
                    "",
                    "Alat konversi yang wajib dikenali:",
                    "  Number(x)        teks -> angka. Teksnya harus bersih total, kalau tidak: NaN.",
                    "  parseInt(x, 10)  baca angka BULAT dari depan, berhenti di karakter aneh.",
                    "  parseFloat(x)    sama, tapi bagian desimalnya ikut terbaca.",
                    "  String(x)        apa pun -> teks.",
                    "  x.toString(2)    angka -> teks dalam basis lain (2 biner, 16 heksadesimal).",
                    "  Boolean(x)       apa pun -> true/false (truthy/falsy dibahas di materi Percabangan).",
                    "  +x  dan  !!x     bentuk singkat dari Number(x) dan Boolean(x).",
                    "",
                    "Angka 10 di parseInt(x, 10) itu RADIX alias basis bilangan. Sekarang boleh",
                    "dilewat, tapi biasakan menulisnya: saat suatu hari teksnya berbentuk \"0x1f\"",
                    "atau datang dari kode lama, kamu tidak perlu menebak basis mana yang dipakai.",
                    "",
                    "Number(\"12abc\") memberi NaN, sedangkan parseInt(\"12abc\") memberi 12.",
                    "Bedanya disengaja, dan memilih yang salah adalah sumber bug yang nyata:",
                    "  - Pakai Number kalau datanya HARUS angka murni -- harga, jumlah, umur.",
                    "    Data kotor langsung ketahuan sebagai NaN, dan itu memang yang kita mau.",
                    "  - Pakai parseInt/parseFloat kalau angkanya memang menempel satuan,",
                    "    misalnya \"16px\" dari CSS atau \"250 gram\" dari teks yang diketik orang.",
                    "  - Jangan pakai parseInt untuk memvalidasi. parseInt(\"7 ekor kambing\")",
                    "    tetap 7, jadi input ngawur lolos begitu saja.",
                ],
            },
            {
                "heading": "Semua cara konversi, plus yang gagal (jalankan: node konversi.js)",
                "code": """// Hampir semua data yang masuk program JS berbentuk STRING: isi kotak input,
// argumen terminal, isi berkas, balasan dari server.
const dariForm = "42";

console.log(Number(dariForm) + 8);                 // 50
console.log(dariForm + 8, typeof (dariForm + 8));  // 428 string  <- + menggabung!

console.log(Number("3.14"));      // 3.14
console.log(Number("  7  "));     // 7     spasi di pinggir dibuang
console.log(Number(""));          // 0     string KOSONG jadi nol, bukan NaN
console.log(Number("12abc"));     // NaN   Number menuntut teks bersih seluruhnya
console.log(parseInt("12abc"));   // 12    baca dari depan, berhenti saat aneh
console.log(parseInt("abc12"));   // NaN   depannya bukan angka
console.log(parseInt("3.9", 10)); // 3     parseInt MEMBUANG desimal, tidak membulatkan
console.log(parseFloat("3.9"));   // 3.9
console.log(parseFloat("16px"));  // 16    satuannya ikut dibuang

// Argumen kedua parseInt adalah radix alias basis bilangan.
console.log(parseInt("ff", 16));  // 255   basis 16
console.log(parseInt("1010", 2)); // 10    basis 2

// Arah sebaliknya: angka menjadi teks
console.log(String(255) + 1);     // 2551  bukan 256, karena sudah jadi teks
console.log((255).toString(2));   // 11111111   biner
console.log((255).toString(16));  // ff         heksadesimal

// Idiom singkat yang akan kamu temui di mana-mana
console.log(+"42", typeof +"42"); // 42 number    unary + sama dengan Number
console.log(!!"teks", !!0);       // true false   !! sama dengan Boolean
console.log(Boolean("false"));    // true   string berisi apa pun itu truthy

// NaN = hasil konversi yang GAGAL, dan ia menular ke seluruh hitungan
const gagal = Number("dua");
console.log(gagal, gagal + 1, gagal * 100);   // NaN NaN NaN
console.log(gagal === NaN);          // false  NaN tidak sama dengan dirinya sendiri
console.log(Number.isNaN(gagal));    // true   satu-satunya cara benar memeriksanya
console.log(isNaN("dua"));           // true   versi global: dikonversi dulu
console.log(Number.isNaN("dua"));    // false  teks "dua" itu string, bukan NaN

// Pembagian dengan nol TIDAK melempar error di JavaScript
console.log(10 / 0);                   // Infinity
console.log(-10 / 0);                  // -Infinity
console.log(0 / 0);                    // NaN
console.log(Number.isFinite(10 / 0));  // false""",
            },
            {
                "body": [
                    "Kenapa NaN begitu merepotkan: ia MENULAR. Sekali satu nilai jadi NaN, semua",
                    "hitungan sesudahnya ikut NaN, dan yang terlihat di layar cuma \"NaN\" di ujung",
                    "-- jauh dari baris yang sebenarnya salah. Kalau kamu melihat NaN, cari ke",
                    "belakang sampai ketemu konversi pertama yang gagal.",
                    "",
                    "NaN === NaN bernilai false. Itu memang sengaja: NaN artinya \"bukan angka yang",
                    "diketahui\", dan dua hal yang sama-sama tidak diketahui tidak bisa disebut sama.",
                    "Akibat praktisnya: JANGAN pernah memeriksa NaN dengan === atau ==.",
                    "  Number.isNaN(x)  -> true hanya kalau x memang NaN. Pakai yang ini.",
                    "  isNaN(x)         -> versi global, MENGKONVERSI x dulu. isNaN(\"dua\") true,",
                    "                      padahal \"dua\" itu string. Menyesatkan, hindari.",
                    "",
                    "Infinity juga tipe number. Pembagian dengan nol di JS tidak melempar error",
                    "seperti di Java atau Python -- programmu jalan terus membawa nilai tak hingga",
                    "sampai akhirnya muncul di layar sebagai \"Infinity\". Penjaganya:",
                    "  Number.isFinite(x)   -> false untuk Infinity, -Infinity, dan NaN sekaligus.",
                    "",
                    "Math adalah objek bawaan berisi fungsi matematika. Tidak perlu import apa pun,",
                    "dan tidak pernah dibuat dengan new -- isinya dipanggil langsung: Math.abs(-9).",
                    "",
                    "Empat fungsi pembulatan, dan bedanya baru kelihatan pada angka MINUS:",
                    "  Math.floor(x)   ke bawah        floor(4.7) = 4    floor(-4.7) = -5",
                    "  Math.ceil(x)    ke atas         ceil(4.1)  = 5    ceil(-4.1)  = -4",
                    "  Math.round(x)   ke terdekat     round(4.5) = 5    round(-4.5) = -4",
                    "  Math.trunc(x)   buang desimal   trunc(4.7) = 4    trunc(-4.7) = -4",
                    "Dua jebakannya: Math.round(-4.5) itu -4 bukan -5 (angka 0.5 SELALU dibulatkan",
                    "ke arah plus), dan floor bukan trunc -- keduanya cuma sama selama angkanya",
                    "positif.",
                    "",
                    "Yang lain: Math.abs (nilai mutlak), Math.sqrt (akar), Math.pow(a, b) yang sama",
                    "saja dengan operator a ** b, dan Math.PI. Math.max/Math.min menerima ANGKA satu",
                    "per satu, bukan array, jadi array harus dibongkar dengan spread dari materi Array:",
                    "  Math.max(...nilai)   benar",
                    "  Math.max(nilai)      NaN -- array-nya dicoba diubah jadi satu angka",
                    "",
                    "Math.random() memberi pecahan acak dari 0 sampai kurang dari 1. Ini SATU-SATUNYA",
                    "sumber angka acak di JavaScript; tidak ada fungsi lain. Resep bakunya:",
                    "  Math.floor(Math.random() * 6)              -> 0..5",
                    "  Math.floor(Math.random() * 6) + 1          -> 1..6, sebuah dadu",
                    "  Math.floor(Math.random() * arr.length)     -> indeks acak sebuah array",
                    "Selalu floor, jangan round: dengan round, angka ujung hanya punya setengah",
                    "peluang dibanding angka tengah. Contoh di materi ini tidak memakai random",
                    "karena outputnya harus bisa diprediksi supaya bisa kamu cocokkan.",
                ],
            },
            {
                "heading": "Math dan presisi desimal (jalankan: node angka.js)",
                "code": """// Math tidak perlu di-import dan tidak pernah dibuat dengan new.
console.log(Math.floor(4.7), Math.floor(-4.7));   // 4 -5    ke bawah
console.log(Math.ceil(4.1), Math.ceil(-4.1));     // 5 -4    ke atas
console.log(Math.round(4.5), Math.round(-4.5));   // 5 -4    0.5 selalu ke arah plus
console.log(Math.trunc(4.7), Math.trunc(-4.7));   // 4 -4    desimal dibuang
console.log(Math.abs(-9), Math.sqrt(144));        // 9 12
console.log(Math.pow(2, 10), 2 ** 10);            // 1024 1024   sama saja
console.log(Math.PI);                             // 3.141592653589793

const nilai = [80, 95, 60, 88];
console.log(Math.max(...nilai), Math.min(...nilai));  // 95 60   array dibongkar
console.log(Math.max(nilai));                         // NaN     tanpa spread: gagal

// ---- Presisi: SEMUA angka JavaScript adalah float 64-bit ----
console.log(0.1 + 0.2);            // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);    // false   inilah perbandingan harga yang gagal
console.log(1.005 * 100);          // 100.49999999999999

const total = 0.1 + 0.2;
console.log(total.toFixed(2), typeof total.toFixed(2));  // 0.30 string  <- BUKAN number
console.log(total.toFixed(2) + 1);           // 0.301  teks digabung, bukan dijumlah
console.log(Number(total.toFixed(2)) + 1);   // 1.3    dikonversi balik dulu
console.log(Math.round(total * 100) / 100);  // 0.3    membulatkan, hasilnya number
console.log(Math.abs(total - 0.3) < 1e-9);   // true   1e-9 artinya 0.000000001

// ---- Batas bilangan bulat ----
console.log(Number.MAX_SAFE_INTEGER);   // 9007199254740991
console.log(9007199254740993);          // 9007199254740992   meleset tanpa peringatan
console.log(9007199254740993n);         // 9007199254740993n  BigInt tetap tepat""",
            },
            {
                "body": [
                    "Kenapa 0.1 + 0.2 bukan 0.3? Karena JavaScript hanya punya SATU tipe angka:",
                    "float 64-bit. Tidak ada int terpisah seperti di Java atau C -- bilangan bulat",
                    "dan desimal disimpan dengan cara yang sama persis.",
                    "",
                    "Komputer menyimpan angka dalam basis DUA, dan 0.1 di basis dua adalah pecahan",
                    "yang tidak pernah habis -- sama seperti 1/3 = 0,3333... di basis sepuluh yang",
                    "kita pakai sehari-hari. Yang tersimpan sudah dibulatkan sedikit, dan remah",
                    "pembulatan itulah yang muncul saat dua angka dijumlahkan. Ini BUKAN bug",
                    "JavaScript; Python, Java, dan C berperilaku sama. Kesalahannya cuma satu:",
                    "mengira angka desimal tersimpan persis seperti yang kita tulis.",
                    "",
                    "Akibat yang paling sering bikin bingung: perbandingan uang dengan === gagal",
                    "padahal di layar angkanya terlihat sama. Bandingkan SELISIHNYA, bukan nilainya:",
                    "  if (Math.abs(total - 0.3) < 1e-9) { ... }   // benar",
                    "  if (total === 0.3) { ... }                  // rapuh, hindari",
                    "",
                    "Tiga cara menangani desimal, dan kapan masing-masing tepat:",
                    "  1. toFixed(2)  -> untuk DITAMPILKAN saja. Hasilnya STRING, bukan number.",
                    "     Ini jebakan besar: menjumlahkan hasilnya berarti menggabung teks.",
                    "     Bungkus dengan Number(...) kalau nilainya masih akan dihitung lagi.",
                    "     toFixed juga membulatkan, jadi jangan dipakai kalau butuh angka utuh.",
                    "  2. Math.round(x * 100) / 100  -> membulatkan ke 2 desimal, tetap number.",
                    "     Pakai ini untuk nilai yang masih ikut perhitungan berikutnya.",
                    "  3. Simpan uang dalam SATUAN TERKECIL sebagai bilangan bulat. Rp 19.999",
                    "     disimpan sebagai 19999, harga 4,50 dolar disimpan sebagai 450 sen.",
                    "     Formatnya baru dipasang saat ditampilkan. Ini yang dipakai sistem",
                    "     pembayaran sungguhan, karena bilangan bulat tidak punya remah sama sekali.",
                    "",
                    "Batas bilangan bulat: Number.MAX_SAFE_INTEGER = 9007199254740991, sekitar 9",
                    "kuadriliun. Di atas itu dua angka yang berbeda bisa tersimpan menjadi angka",
                    "yang sama, dan tidak ada peringatan apa pun -- program tetap jalan dengan data",
                    "yang salah. Kalau memang butuh lebih besar (ID dari database besar, stempel",
                    "waktu nanodetik, saldo kripto), pakai BigInt yang berakhiran n -- tipe yang sudah",
                    "disinggung di materi Variabel & Tipe Data. Syaratnya: BigInt tidak boleh",
                    "dicampur langsung dengan number biasa dalam satu operasi -- salah satunya",
                    "harus dikonversi lebih dulu.",
                ],
            },
        ],
    },
    {
        "title": "5. Percabangan (if / else / switch)",
        "sections": [
            {
                "body": [
                    "Sintaks if-else JavaScript mirip Java/C:",
                    "  if (kondisi) {",
                    "      // jalankan jika true",
                    "  } else if (kondisi2) {",
                    "      // jalankan jika kondisi2 true",
                    "  } else {",
                    "      // jalankan jika semua false",
                    "  }",
                    "",
                    "'Truthy' dan 'Falsy' (nilai yang dianggap true/false di if):",
                    "  Falsy: 0, \"\", null, undefined, NaN, false",
                    "  Truthy: SEMUA nilai lain (termasuk \"0\", [], {} - hati-hati!)",
                    "",
                    "  if ([])  { console.log(\"jalan\"); }   // JALAN! array kosong = truthy",
                    "  if (\"0\") { console.log(\"jalan\"); }  // JALAN! string \"0\" = truthy",
                ]
            },
            {
                "heading": "Ternary operator & switch",
                "code": """const nilai = 85;
const status = nilai >= 75 ? "Lulus" : "Tidak Lulus";
console.log(status);   // Lulus

// switch-case
const hari = 3;
switch (hari) {
    case 1:
        console.log("Senin");
        break;
    case 2:
        console.log("Selasa");
        break;
    case 3:
        console.log("Rabu");
        break;
    default:
        console.log("Hari tidak valid");
}
// Output: Rabu
// PENTING: switch di JS pakai perbandingan === (strict), bukan ==!"""
            },
            {
                "heading": "Fallthrough: yang terjadi kalau break dihilangkan",
                "body": [
                    "Kenapa tiap case di atas diakhiri break: TANPA break, eksekusi tidak",
                    "berhenti di case yang cocok. Ia JATUH TERUS ke case-case berikutnya",
                    "sampai bertemu break atau habis. Namanya fallthrough.",
                    "",
                    "Ini bukan cuma jebakan - ia juga dipakai dengan SENGAJA. Case yang",
                    "ditumpuk tanpa isi di antaranya berarti 'beberapa nilai, satu tindakan'.",
                    "Jangan dibaca sebagai 'case kosong yang tidak melakukan apa-apa'.",
                ],
                "code": """// Tanpa break, eksekusi JATUH TERUS ke case berikutnya (fallthrough).
const nilai = 2;
switch (nilai) {
    case 1:
        console.log("satu");
    case 2:
        console.log("dua");     // cocok di sini, tapi tidak ada break...
    case 3:
        console.log("tiga");    // ...jadi baris ini IKUT jalan
        break;
    case 4:
        console.log("empat");   // tidak jalan, sudah kena break
}
// Output: dua, lalu tiga

// Fallthrough yang DISENGAJA: beberapa case menuju satu tindakan yang sama.
function jenisHari(hari) {
    switch (hari) {
        case "sabtu":
        case "minggu":
            return "akhir pekan";
        default:
            return "hari kerja";
    }
}
console.log(jenisHari("sabtu"));   // akhir pekan
console.log(jenisHari("senin"));   // hari kerja

// Catatan: return juga menghentikan switch, jadi break tidak diperlukan lagi
// kalau tiap case langsung mengembalikan nilai seperti contoh di atas."""
            },
        ],
    },
    {
        "title": "6. Perulangan (for, while, for...of, for...in)",
        "sections": [
            {
                "body": [
                    "1. for klasik (mirip Java/C):",
                    "   for (let i = 0; i < 5; i++) { ... }",
                    "",
                    "2. while - cek kondisi dulu, baru jalan:",
                    "   while (kondisi) { ... }",
                    "",
                    "3. do...while - jalan dulu, baru cek kondisi:",
                    "   do { ... } while (kondisi);",
                    "",
                    "4. for...of - iterasi NILAI dari iterable (array, string, Map, Set):",
                    "   for (const item of array) { ... }",
                    "",
                    "5. for...in - iterasi KEY/index dari object atau array:",
                    "   for (const key in object) { ... }",
                    "   (untuk array, LEBIH DISARANKAN pakai for...of atau .forEach)",
                    "",
                    "Satu peringatan untuk for...in: ia ikut menyapu property WARISAN dari",
                    "prototype, bukan hanya milik objectnya sendiri. Saringannya",
                    "Object.hasOwn(obj, key), dibahas di materi 'Object & Destructuring'.",
                    "",
                    "Dua hal yang dipakai di contoh berikut, supaya tidak bikin tertegun:",
                    "  process.stdout.write(teks)  mencetak TANPA menambah baris baru,",
                    "      berbeda dari console.log yang selalu menambahnya. Ini objek",
                    "      khusus Node; di Console browser hasilnya 'process is not",
                    "      defined'. Selengkapnya di materi 'Node.js: Process, Berkas,",
                    "      dan Path'.",
                    "  buah.entries()  memberi pasangan [index, nilai] untuk tiap elemen.",
                    "      Bentuk const [index, b] di sisi kiri namanya destructuring,",
                    "      dibahas di materi 'Array & Method Array (map/filter/reduce)'.",
                ]
            },
            {
                "heading": "Contoh semua jenis loop",
                "code": """// for klasik
for (let i = 1; i <= 5; i++) {
    process.stdout.write(i + " ");
}
console.log();   // 1 2 3 4 5

// for...of untuk array
const buah = ["apel", "jeruk", "mangga"];
for (const b of buah) {
    console.log(b);
}

// for...of dengan entries() untuk dapat index juga
for (const [index, b] of buah.entries()) {
    console.log(`${index}: ${b}`);
}

// for...in untuk object
const mahasiswa = { nama: "Andi", umur: 20 };
for (const key in mahasiswa) {
    console.log(`${key}: ${mahasiswa[key]}`);
}

// while & break/continue
let j = 1;
while (j <= 10) {
    if (j === 5) { j++; continue; }
    if (j === 8) break;
    process.stdout.write(j + " ");
    j++;
}
console.log();   // 1 2 3 4 6 7"""
            },
            {
                "heading": "Label: break dan continue yang menembus loop bersarang",
                "body": [
                    "break dan continue selalu mengenai loop TERDALAM tempat ia ditulis.",
                    "Pada loop bersarang, itu sering bukan yang kita mau: menemukan hasil di",
                    "loop dalam tidak menghentikan loop luar. Jalan keluarnya LABEL - sebuah",
                    "nama yang ditempel di depan loop, lalu disebut oleh break/continue.",
                    "",
                    "  namaLabel: for (...) { for (...) { break namaLabel; } }",
                    "",
                    "Label ditulis 'nama:' persis sebelum kata for atau while. Ia bukan",
                    "variabel dan tidak perlu dideklarasikan. Pakai seperlunya saja: dua",
                    "loop bersarang masih terbaca, empat sudah tanda kode perlu dipecah",
                    "jadi fungsi tersendiri.",
                ],
                "code": """const matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

luar: for (const baris of matriks) {
    for (const sel of baris) {
        if (sel === 5) {
            console.log("ketemu 5, berhenti total");
            break luar;              // keluar dari KEDUA loop sekaligus
        }
        console.log(sel);
    }
}
// Output: 1, 2, 3, 4, lalu "ketemu 5, berhenti total"
// Tanpa label, break hanya keluar dari loop dalam dan baris [7,8,9] tetap diproses.

// continue berlabel: langsung lanjut ke iterasi berikutnya dari loop LUAR.
ganjilSaja: for (const baris of matriks) {
    for (const sel of baris) {
        if (sel % 2 === 0) continue ganjilSaja;   // sisa baris ini ditinggalkan
        process.stdout.write(sel + " ");
    }
}
console.log();   // 1 7"""
            },
        ],
    },
    {
        "title": "7. String & Template Literal",
        "sections": [
            {
                "body": [
                    "String di JavaScript bisa pakai kutip tunggal '...', ganda \"...\",",
                    "atau backtick `...` (template literal, cara MODERN & disarankan).",
                    "",
                    "String bersifat IMMUTABLE (tidak bisa diubah langsung per karakter).",
                    "",
                    "Indexing & slicing:",
                    "  const s = \"JavaScript\";",
                    "  s[0]              -> 'J'",
                    "  s.length          -> 10 (PAKAI .length, bukan .length())",
                    "  s.slice(0, 4)     -> 'Java'",
                    "  s.slice(-6)       -> 'Script'  (dari belakang)",
                ]
            },
            {
                "heading": "Method string yang sering dipakai",
                "code": """const s = "  Belajar JavaScript  ";

console.log(s.trim());               // "Belajar JavaScript"
console.log(s.toUpperCase());        // "  BELAJAR JAVASCRIPT  "
console.log(s.trim().replace("JavaScript", "Coding"));  // "Belajar Coding"
console.log(s.includes("Script"));   // true
console.log(s.trim().split(" "));    // ['Belajar', 'JavaScript']

const kata = ["Aku", "suka", "JavaScript"];
console.log(kata.join(" "));         // "Aku suka JavaScript"

console.log("javascript".padStart(12, "*"));  // "**javascript"
console.log("5".repeat(3));                    // "555"
console.log("Halo".charAt(0));                 // "H"
console.log("Halo".indexOf("lo"));             // 2"""
            },
            {
                "heading": "Template literal (backtick) - cara modern format string",
                "code": """const nama = "Andi";
const umur = 20;

console.log(`Nama: ${nama}, Umur: ${umur}`);
console.log(`Tahun depan: ${umur + 1} tahun`);   // bisa ekspresi langsung

// Multi-baris TANPA karakter escape khusus
const puisi = `Baris pertama
Baris kedua
Baris ketiga`;
console.log(puisi);

// Nested template literal
const status = `Status: ${umur >= 17 ? "Dewasa" : "Anak-anak"}`;
console.log(status);   // Status: Dewasa"""
            },
            {
                "heading": "Method string yang melengkapi daftar di atas",
                "body": [
                    "Daftar di atas baru separuh. Beberapa method yang hilang justru",
                    "pasangan dari yang sudah ada, dan tanpa pasangannya kamu akan menulis",
                    "loop panjang untuk hal yang sudah ada satu barisnya:",
                    "",
                    "  toLowerCase()      pasangan toUpperCase()",
                    "  startsWith(t)      diawali t?      endsWith(t)   diakhiri t?",
                    "  substring(a, b)    mirip slice, tapi TIDAK mengerti indeks negatif",
                    "  replaceAll(a, b)   ganti SEMUA kemunculan",
                    "  trimStart()        pasangan trimEnd(); trim() membuang kedua sisi",
                    "  padEnd(n, isi)     pasangan padStart()",
                    "  at(-1)             karakter terakhir tanpa menghitung length",
                    "  a.localeCompare(b) -1/0/1, untuk mengurutkan teks",
                    "",
                    "Satu jebakan yang wajib kamu tahu sekarang: s.replace(\"a\", \"b\") dengan",
                    "string biasa HANYA mengganti kemunculan PERTAMA - diam-diam, tanpa",
                    "peringatan. Obatnya replaceAll(), dan alasannya dibahas tuntas di",
                    "materi 'Regular Expression: Mencari Pola dalam Teks'.",
                ],
                "code": """const s = "Belajar JavaScript";

console.log(s.toLowerCase());          // belajar javascript
console.log(s.startsWith("Belajar"));  // true
console.log(s.endsWith("Script"));     // true
console.log(s.substring(0, 7));        // Belajar
console.log(s.at(-1));                 // t   karakter terakhir
console.log("7".padEnd(4, "."));       // 7...
console.log("[" + "  rapi  ".trimStart() + "]");   // [rapi  ]
console.log("[" + "  rapi  ".trimEnd() + "]");     // [  rapi]
console.log(s.replaceAll("a", "@"));   // Bel@j@r J@v@Script

// Pencarian yang tidak peduli huruf besar-kecil: samakan dulu KEDUA sisinya.
// Ini idiom paling sering dipakai untuk kotak pencarian.
const daftar = ["Andi Wijaya", "budi santoso", "Citra ANGGRAINI"];
const kueri = "CIT";
console.log(daftar.filter(n => n.toLowerCase().includes(kueri.toLowerCase())));
// [ 'Citra ANGGRAINI' ]

// Mengurutkan teks: sort() biasa memakai urutan kode karakter, jadi SEMUA
// huruf besar datang sebelum huruf kecil. localeCompare mengerti maksud kita.
const buah = ["apel", "Bayam", "cabai"];
console.log([...buah].sort());                             // [ 'Bayam', 'apel', 'cabai' ]
console.log([...buah].sort((a, b) => a.localeCompare(b))); // [ 'apel', 'Bayam', 'cabai' ]"""
            },
            {
                "heading": "Tagged template literal",
                "body": [
                    "Satu bentuk terakhir yang kelihatan mustahil kalau belum pernah",
                    "dijelaskan: NAMA FUNGSI yang menempel langsung di depan backtick.",
                    "",
                    "  nama`teks ${nilai} lagi`",
                    "",
                    "Itu PEMANGGILAN FUNGSI - tanpa tanda kurung sama sekali. Namanya",
                    "tagged template literal. Fungsinya menerima dua hal secara terpisah:",
                    "array potongan teksnya, lalu nilai-nilai di dalam ${...} sebagai rest",
                    "parameter. Karena terpisah, fungsinya bebas memperlakukan nilai itu -",
                    "misalnya membungkusnya, meloloskannya, atau menerjemahkannya.",
                    "",
                    "Inilah yang membuat baris-baris berikut bisa dibaca saat kamu",
                    "membuka proyek orang:",
                    "  styled.button`color: red;`   library styled-components (CSS di JS)",
                    "  gql`query { user { id } }`   query GraphQL",
                    "  String.raw`C:\\folder`        bawaan JS, tidak menerjemahkan escape",
                ],
                "code": """// Fungsinya menerima potongan teks dan nilainya SECARA TERPISAH.
function tebal(potongan, ...nilai) {
    return potongan.reduce(
        (hasil, teks, i) => hasil + teks + (i < nilai.length ? `**${nilai[i]}**` : ""),
        ""
    );
}

const nama = "Andi";
const umur = 20;
console.log(tebal`Halo ${nama}, umur ${umur} tahun.`);
// Halo **Andi**, umur **20** tahun.

// Bandingkan dengan template literal biasa: nilainya langsung dilebur apa adanya.
console.log(`Halo ${nama}, umur ${umur} tahun.`);
// Halo Andi, umur 20 tahun.

// String.raw adalah tagged template BAWAAN: ia tidak menerjemahkan \\n dkk.
console.log(String.raw`baris1\\nbaris2`);   // baris1\\nbaris2   apa adanya
console.log(`baris1\\nbaris2`);             // benar-benar dua baris"""
            },
        ],
    },
    {
        "title": "8. Tanggal & Waktu dengan Date",
        "sections": [
            {
                "body": [
                    "Hampir semua aplikasi nyata menyentuh waktu: kolom createdAt yang datang dari API,",
                    "teks \"diposting 3 jam lalu\", umur, tanggal jatuh tempo, mengukur lama sebuah proses.",
                    "Di JavaScript semuanya diurus satu objek bawaan: Date.",
                    "",
                    "Tiga cara membuat Date:",
                    "  new Date()                      -> detik ini juga, saat baris itu dijalankan",
                    "  new Date(\"2026-03-17T08:30:00\") -> dari teks format ISO (tahun-bulan-tanggal)",
                    "  new Date(2026, 2, 17, 8, 30)    -> dari angka: tahun, bulan, tanggal, jam, menit",
                    "",
                    "JEBAKAN NOMOR SATU: pada bentuk angka, BULAN DIHITUNG MULAI DARI 0.",
                    "  0 = Januari, 1 = Februari, 2 = Maret, ... 11 = Desember",
                    "Jadi new Date(2026, 8, 6) itu 6 SEPTEMBER, bukan 6 Agustus. Ini sulit disadari karena",
                    "programnya tidak error dan hasilnya tetap tanggal yang masuk akal - cuma meleset satu",
                    "bulan. Tahun, tanggal, jam, dan menit dihitung normal; HANYA bulan yang mulai dari 0.",
                    "",
                    "Di balik layar sebuah Date cuma menyimpan SATU angka: milidetik sejak 1 Januari 1970",
                    "pukul 00:00 UTC. Titik nol itu namanya epoch, dan angkanya disebut timestamp.",
                    "  Date.now()               -> timestamp sekarang (number), tanpa membuat objek Date",
                    "  tanggal.getTime()        -> timestamp dari sebuah objek Date",
                    "  new Date(1773711000000)  -> mengubah timestamp kembali jadi Date",
                    "Timestamp dipakai di mana-mana karena ia cuma angka: gampang disimpan di database,",
                    "dikirim lewat JSON, dan dibandingkan pakai < atau > untuk tahu mana yang lebih dulu.",
                ],
            },
            {
                "heading": "Membuat Date & membaca bagian-bagiannya",
                "code": """// Tiga cara membuat objek Date
const sekarang = new Date();                        // waktu saat kode ini dijalankan
const dariTeks = new Date("2026-03-17T08:30:00");   // dari string ISO, dibaca waktu LOKAL
const dariAngka = new Date(2026, 2, 17, 8, 30, 0);  // 2 = MARET, bukan Februari!

console.log(sekarang instanceof Date);                    // true
console.log(dariTeks.getTime() === dariAngka.getTime());  // true - keduanya waktu yang sama

// Membaca bagian-bagiannya satu per satu
const d = dariAngka;
console.log(d.getFullYear());   // 2026
console.log(d.getMonth());      // 2  <- MARET dihitung dari 0, bukan 3
console.log(d.getDate());       // 17 (tanggal 1-31; jangan tertukar dengan getDay)
console.log(d.getDay());        // 2  (nama hari: 0=Minggu, 1=Senin, 2=Selasa, ...)
console.log(d.getHours(), d.getMinutes(), d.getSeconds());   // 8 30 0

// Karena getMonth() dan getDay() memberi ANGKA, siapkan array namanya
const NAMA_HARI = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];
const NAMA_BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                    "Juli", "Agustus", "September", "Oktober", "November", "Desember"];
const hari = NAMA_HARI[d.getDay()];
const bulan = NAMA_BULAN[d.getMonth()];
console.log(`${hari}, ${d.getDate()} ${bulan} ${d.getFullYear()}`);
// Selasa, 17 Maret 2026  <- array pas dengan getMonth() justru KARENA dimulai dari 0

// Timestamp: milidetik sejak 1 Januari 1970 pukul 00:00 UTC (epoch)
console.log(new Date("2026-03-17T01:30:00Z").getTime());   // 1773711000000
console.log(new Date(0).toISOString());                    // 1970-01-01T00:00:00.000Z
console.log(typeof Date.now());                            // "number"

// Tanggal yang gagal dibaca TIDAK memicu error - ia jadi Invalid Date yang diam saja
const rusak = new Date("17/03/2026");        // format hari/bulan/tahun tidak dikenali
console.log(rusak.getFullYear());            // NaN
console.log(Number.isNaN(rusak.getTime()));  // true  <- beginilah cara mengeceknya""",
            },
            {
                "heading": "Menampilkan: ISO untuk mesin, locale untuk manusia",
                "code": """const d = new Date(2026, 2, 17, 8, 30, 0);   // 17 Maret 2026, 08:30 waktu lokal

// 1. toISOString(): format baku antar-sistem. SELALU dicetak dalam UTC (akhiran Z).
//    Inilah bentuk yang dipakai API dan database - bukan untuk dibaca pengguna.
const utc = new Date("2026-03-17T01:30:00Z");
console.log(utc.toISOString());                 // 2026-03-17T01:30:00.000Z
console.log(utc.toISOString().slice(0, 10));    // 2026-03-17  (ambil tanggalnya saja)

// 2. toLocale...(): format sesuai kebiasaan negara. Ini yang untuk DIBACA MANUSIA.
console.log(d.toLocaleDateString("id-ID"));     // 17/3/2026
console.log(d.toLocaleDateString("en-US"));     // 3/17/2026  <- bulan dulu, beda arti!
console.log(d.toLocaleDateString("id-ID", {
    weekday: "long", day: "numeric", month: "long", year: "numeric",
}));                                            // Selasa, 17 Maret 2026
console.log(d.toLocaleTimeString("id-ID", { hour: "2-digit", minute: "2-digit" }));
// 08.30   <- Indonesia memisahkan jam dan menit dengan TITIK, bukan titik dua

// 3. Format manual: kendali penuh. padStart membuat "8" jadi "08".
function formatTanggal(t) {
    const tgl = String(t.getDate()).padStart(2, "0");
    const bln = String(t.getMonth() + 1).padStart(2, "0");   // +1 WAJIB di sini
    const jam = String(t.getHours()).padStart(2, "0");
    const mnt = String(t.getMinutes()).padStart(2, "0");
    return `${tgl}/${bln}/${t.getFullYear()} ${jam}:${mnt}`;
}
console.log(formatTanggal(d));    // 17/03/2026 08:30""",
            },
            {
                "heading": "Menghitung selisih, umur, \"3 jam lalu\", dan menggeser tanggal",
                "code": """const mulai = new Date(2026, 0, 10, 9, 0);      // 10 Januari 2026, 09:00
const selesai = new Date(2026, 0, 12, 15, 30);  // 12 Januari 2026, 15:30

// Mengurangkan dua Date menghasilkan MILIDETIK, bukan hari
const selisihMs = selesai - mulai;
console.log(selisihMs);                          // 196200000
console.log(selisihMs / (1000 * 60 * 60));       // 54.5  (jam)
console.log(Math.floor(selisihMs / 86400000));   // 2     (hari; 86400000 ms = 1 hari)

// Umur: selisih tahun, lalu dikurangi 1 kalau ulang tahunnya BELUM lewat tahun ini
function hitungUmur(lahir, acuan) {
    let umur = acuan.getFullYear() - lahir.getFullYear();
    const belumUlangTahun = acuan.getMonth() < lahir.getMonth()
        || (acuan.getMonth() === lahir.getMonth() && acuan.getDate() < lahir.getDate());
    if (belumUlangTahun) umur--;
    return umur;
}
console.log(hitungUmur(new Date(2005, 7, 20), new Date(2026, 2, 17)));   // 20

// "3 jam lalu". Waktu acuan dikirim sebagai PARAMETER, bukan new Date() di dalam,
// supaya fungsinya bisa diuji dan hasilnya bisa diramalkan.
function waktuLalu(waktu, sekarang) {
    const detik = Math.floor((sekarang - waktu) / 1000);
    if (detik < 60) return "baru saja";
    if (detik < 3600) return `${Math.floor(detik / 60)} menit lalu`;
    if (detik < 86400) return `${Math.floor(detik / 3600)} jam lalu`;
    return `${Math.floor(detik / 86400)} hari lalu`;
}
const acuan = new Date(2026, 2, 17, 12, 0);
console.log(waktuLalu(new Date(2026, 2, 17, 9, 0), acuan));    // 3 jam lalu
console.log(waktuLalu(new Date(2026, 2, 14, 12, 0), acuan));   // 3 hari lalu

// Menggeser tanggal: setDate() boleh diberi angka di luar 1-31, bulannya ikut maju
const jatuhTempo = new Date(2026, 0, 25);
jatuhTempo.setDate(jatuhTempo.getDate() + 10);          // 25 + 10 = "35 Januari"
console.log(jatuhTempo.toLocaleDateString("id-ID"));    // 4/2/2026

// JEBAKAN: Date itu MUTABLE - setDate MENGUBAH objek aslinya, tidak membuat yang baru
const asli = new Date(2026, 0, 10);
const salinan = new Date(asli);                  // salin dulu sebelum digeser!
salinan.setDate(salinan.getDate() + 7);
console.log(asli.getDate(), salinan.getDate());  // 10 17

// JEBAKAN setMonth: tanggal yang tidak ada meluber ke bulan berikutnya
const akhirJanuari = new Date(2026, 0, 31);
akhirJanuari.setMonth(1);                                 // minta "31 Februari"
console.log(akhirJanuari.toLocaleDateString("id-ID"));    // 3/3/2026, bukan 28/2/2026""",
            },
            {
                "body": [
                    "Empat jebakan yang paling sering menggigit, dan cara menghindarinya:",
                    "",
                    "1. Date itu MUTABLE. setDate/setMonth/setHours mengubah objek yang sudah ada, bukan",
                    "   mengembalikan yang baru. Kalau objek itu juga dipegang variabel lain, variabel itu",
                    "   ikut berubah - sama seperti object dan array yang dioper lewat referensi.",
                    "   Kebiasaan yang aman: const baru = new Date(lama); baru saja digeser.",
                    "",
                    "2. Zona waktu. Isi Date selalu UTC, tapi getDate/getHours dan kawan-kawan membacanya",
                    "   dalam zona waktu KOMPUTER yang menjalankan. Kode yang sama bisa menyebut tanggal",
                    "   berbeda di server Amerika dan di laptop Jakarta.",
                    "   new Date(\"2026-03-17\") - tanggal saja, tanpa jam - dibaca sebagai tengah malam UTC.",
                    "   Di Jakarta itu 17 Maret pukul 07:00, tapi di New York masih 16 Maret pukul 20:00,",
                    "   sehingga getDate() di sana menjawab 16. Kalau jamnya penting, tulis jamnya:",
                    "   new Date(\"2026-03-17T00:00:00\") dibaca sebagai waktu LOKAL, bukan UTC.",
                    "   Tiap getter punya kembaran UTC: getUTCDate(), getUTCHours(), getUTCFullYear(), dst.",
                    "",
                    "3. Parsing string tidak baku. Yang dijamin sama di semua browser dan Node hanya format",
                    "   ISO: \"2026-03-17\" dan \"2026-03-17T08:30:00\". Selain itu terserah mesinnya -",
                    "   \"17/03/2026\" jadi Invalid Date, sedangkan \"03/17/2026\" dibaca bulan-dulu ala",
                    "   Amerika. Kalau datanya berformat lain, pecah sendiri dengan split() lalu susun:",
                    "   new Date(tahun, bulan - 1, tanggal).",
                    "",
                    "4. Kegagalannya diam. Tanggal ngawur menghasilkan Invalid Date tanpa error, dan semua",
                    "   hitungan sesudahnya jadi NaN yang menyebar entah sampai mana. Periksa lebih dulu:",
                    "   if (Number.isNaN(d.getTime())) { ... }",
                    "",
                    "Kenapa kode nyata sering memakai library (date-fns, Day.js, Luxon)?",
                    "Bukan karena Date tidak mampu, tapi karena format tampilan, selisih \"berapa bulan\",",
                    "zona waktu, dan bahasa harus ditulis tangan berulang-ulang, dan sifat mutable-nya",
                    "gampang jadi bug. Library membungkus itu jadi satu baris dan objeknya immutable.",
                    "JavaScript sendiri sedang menyiapkan pengganti resmi bernama Temporal.",
                    "Tetap kuasai Date lebih dulu: semua library itu berdiri di atasnya, dan tanggal yang",
                    "datang dari API tetap berupa string ISO yang harus kamu baca sendiri.",
                ],
            },
        ],
    },
    {
        "title": "9. Regular Expression: Mencari Pola dalam Teks",
        "sections": [
            {
                "body": [
                    "Regular expression (regex) adalah cara menuliskan POLA teks.",
                    "includes() dan === bertanya \"apakah teksnya PERSIS ini?\";",
                    "regex bertanya \"apakah teksnya BERBENTUK seperti ini?\" -",
                    "empat angka, tanda hubung, dua angka, tanda hubung, dua angka.",
                    "Tanpa regex, pertanyaan sesederhana \"apakah semua karakternya",
                    "angka?\" butuh loop dan belasan baris if.",
                    "",
                    "Bentuk penulisannya yang paling bikin bingung pertama kali:",
                    "",
                    "  const pola = /\\d+/g;",
                    "",
                    "Baris itu berisi SATU nilai, sama seperti \"halo\" adalah satu",
                    "nilai. Garis miringnya BUKAN pembagian - ia pembatas, perannya",
                    "sama persis dengan tanda kutip pada string. Yang di dalam",
                    "pembatas adalah polanya; huruf yang menempel di belakang",
                    "pembatas penutup adalah FLAG-nya. Begitu ini masuk, baris",
                    "seperti if (/^\\d+$/.test(input)) berhenti terlihat seperti",
                    "pembagian yang salah ketik.",
                    "",
                    "Flag yang perlu kamu kenal (boleh digabung, misalnya /abc/gi):",
                    "",
                    "  g   global    - cari SEMUA kemunculan, bukan yang pertama saja",
                    "  i   ignore    - huruf besar dan kecil dianggap sama",
                    "  m   multiline - ^ dan $ berlaku per BARIS, bukan per teks utuh",
                    "  s   dotAll    - titik ikut mencocoki karakter baris baru",
                    "",
                    "Kalau polanya harus DIRAKIT dari variabel, literal /.../ tidak",
                    "bisa dipakai: isinya tidak pernah dievaluasi. Pakai",
                    "konstruktornya, dan flag jadi argumen kedua berupa string:",
                    "",
                    "  const kata = \"budi\";",
                    "  const pola = new RegExp(kata + \"\\d+\", \"gi\");",
                    "",
                    "Perhatikan backslash-nya DUA. Yang pertama dimakan aturan",
                    "string JavaScript, yang kedua baru sampai ke regex-nya.",
                    "Menulis new RegExp(\"\\d+\") menghasilkan pola d+ - mencari huruf",
                    "d, bukan angka. Ini salah satu bug regex paling sering di JS.",
                ],
            },
            {
                "heading": "Kamus polanya - hafal deret atas, sisanya cukup dikenali",
                "body": [
                    "  \\d  satu digit 0-9          \\D  apa pun SELAIN digit",
                    "  \\w  huruf, angka, atau _    \\W  selain itu",
                    "  \\s  spasi, tab, baris baru  \\S  selain karakter kosong",
                    "  .   karakter apa saja (kecuali baris baru)",
                    "",
                    "  [aiu]     salah satu dari a, i, atau u",
                    "  [a-z]     satu huruf kecil, a sampai z",
                    "  [^0-9]    satu karakter yang BUKAN angka",
                    "            (^ di dalam kurung siku berarti \"kecuali\")",
                    "",
                    "  ^abc      teks DIAWALI abc      abc$  teks DIAKHIRI abc",
                    "  \\babc\\b   abc sebagai kata utuh, bukan potongan kata lain",
                    "",
                    "Berapa kali sesuatu boleh muncul - selalu menempel pada hal",
                    "yang ada TEPAT SEBELUMNYA:",
                    "",
                    "  a+       satu atau lebih         a*     nol atau lebih",
                    "  a?       nol atau satu           a{3}   tepat tiga kali",
                    "  a{2,4}   dua sampai empat kali   a{2,}  dua kali atau lebih",
                    "",
                    "  kucing|anjing   salah satu dari dua pilihan",
                    "  (ku)+           grup: + berlaku untuk \"ku\" utuh, dan",
                    "                  isinya IKUT DITANGKAP",
                    "  (?:ku)+         grup non-capture: mengelompokkan saja",
                    "",
                    "Grup penangkap (...) bukan sekadar kurung: potongan yang",
                    "cocok di dalamnya disimpan terpisah supaya bisa kamu ambil",
                    "kembali - itu bahan bagian berikutnya. Kalau kamu cuma butuh",
                    "mengelompokkan, misalnya supaya + berlaku ke beberapa karakter",
                    "sekaligus, pakai (?:...) supaya hasilnya tidak dipenuhi grup",
                    "yang tidak pernah dipakai.",
                ],
            },
            {
                "heading": "Mencari dan mengambil: test, match, matchAll, split",
                "code": """const teks = "Pesanan #A12 dikirim ke Budi pada 2024-05-17, total Rp 250000.";

// test() menjawab satu pertanyaan saja: cocok atau tidak -> true/false
console.log(/\\d/.test(teks));            // true  : ada angka di dalamnya
console.log(/^Pesanan/.test(teks));      // true  : teks DIAWALI kata Pesanan
console.log(/budi/.test(teks));          // false : huruf besar-kecil dihitung
console.log(/budi/i.test(teks));         // true  : flag i mengabaikan kapital

// match() TANPA flag g -> satu kecocokan, lengkap dengan isi grupnya
const tgl = teks.match(/(\\d{4})-(\\d{2})-(\\d{2})/);
console.log(tgl[0], "| grup 1:", tgl[1], "| mulai di indeks:", tgl.index);

// Named group: dibaca lewat nama, bukan lewat nomor yang gampang tertukar
const pola = /(?<tahun>\\d{4})-(?<bulan>\\d{2})-(?<hari>\\d{2})/;
const g = teks.match(pola).groups;
console.log(g.hari + "-" + g.bulan + "-" + g.tahun);   // 17-05-2024

// match() DENGAN flag g -> semua kecocokan, TAPI grupnya hilang
console.log(teks.match(/\\d+/g));   // [ '12', '2024', '05', '17', '250000' ]

// matchAll() -> semua kecocokan LENGKAP dengan grupnya (wajib pakai flag g)
const baris = "user=budi status=aktif level=3";
for (const m of baris.matchAll(/(\\w+)=(\\w+)/g)) {
    console.log(m[1], "->", m[2]);
}

// split() dengan regex: memisah kata walau pemisahnya tidak seragam
console.log("satu   dua \\t tiga  empat".split(/\\s+/));

// Validasi sederhana - sederhana, BUKAN sempurna
const polaHP = /^08\\d{8,11}$/;
console.log(polaHP.test("081234567890"));    // true
console.log(polaHP.test("81234567890"));     // false : tidak diawali 08
console.log(polaHP.test("0812-3456-7890"));  // false : ada tanda hubung

const polaEmail = /^[\\w.+-]+@[\\w-]+\\.[a-z]{2,}$/i;
console.log(polaEmail.test("budi@contoh.com"));   // true
console.log(polaEmail.test("budi@contoh"));       // false : tidak ada .com""",
            },
            {
                "heading": "Mengganti: lubang di replace() yang wajib kamu tahu",
                "body": [
                    "Di materi String kamu melihat s.replace(\"JavaScript\", \"Coding\").",
                    "Yang tidak disebut di sana: replace() dengan string biasa hanya",
                    "mengganti kemunculan PERTAMA. Sisanya dibiarkan utuh, tanpa",
                    "error, tanpa peringatan - jadi bug ini baru ketahuan saat",
                    "datanya kebetulan memuat kata itu dua kali. Obatnya ada dua:",
                    "regex ber-flag g, atau replaceAll().",
                ],
                "code": """const s = "Belajar JavaScript itu seru, JavaScript ada di mana-mana.";

console.log(s.replace("JavaScript", "Coding"));
// Belajar Coding itu seru, JavaScript ada di mana-mana.  <- yang kedua LOLOS

console.log(s.replace(/JavaScript/g, "Coding"));   // obat 1: regex ber-flag g
console.log(s.replaceAll("JavaScript", "Coding")); // obat 2: replaceAll, ES2021

// $1 dan $2 di teks pengganti = isi grup ke-1 dan ke-2 (named group: $<nama>)
console.log("17-05-2024".replace(/(\\d{2})-(\\d{2})-(\\d{4})/, "$3-$2-$1"));
// 2024-05-17

// Pengganti boleh berupa FUNGSI. Ia dipanggil untuk TIAP kecocokan, dan
// nilai kembaliannya yang dipakai sebagai teks pengganti.
const harga = "Kaos 75000, Topi 40000";
console.log(harga.replace(/\\d+/g, (angka) => Number(angka) * 2));
// Kaos 150000, Topi 80000

// Merapikan spasi berlebih: satu baris menggantikan loop yang panjang
const berantakan = "   Halo    dunia   yang    renggang   ";
console.log("[" + berantakan.trim().replace(/\\s+/g, " ") + "]");
// [Halo dunia yang renggang]

// Membuat slug URL. Tiap replace mengurus SATU aturan, jadi tetap terbaca.
function slug(judul) {
    return judul
        .toLowerCase()
        .trim()
        .replace(/[^a-z0-9\\s-]/g, "")   // buang selain huruf, angka, spasi, -
        .replace(/\\s+/g, "-")           // spasi berapa pun jadi satu tanda hubung
        .replace(/-+/g, "-");           // tanda hubung beruntun jadi satu
}
console.log(slug("  Belajar Regex: Mudah, Kok!  "));   // belajar-regex-mudah-kok""",
            },
            {
                "heading": "Jebakan yang benar-benar menjebak",
                "body": [
                    "SERAKAH vs MALAS. Kuantitas * dan + mengambil sebanyak mungkin",
                    "dulu, baru mundur secukupnya supaya sisa polanya tetap cocok.",
                    "Pada teks \"<b>satu</b> dan <b>dua</b>\", pola <b>.*<\\/b> cocok",
                    "dengan SELURUH baris, bukan tag pertama saja. Tambahkan ?",
                    "sesudah kuantitasnya supaya jadi malas (lazy) dan berhenti di",
                    "kecocokan terpendek: <b>.*?<\\/b> menghasilkan \"<b>satu</b>\".",
                    "",
                    "TITIK BUKAN TITIK. Titik berarti \"karakter apa saja\", jadi pola",
                    "\\d+.\\d+ juga cocok dengan \"10x000\". Kalau maksudmu titik",
                    "sungguhan, escape jadi \\. Hal yang sama berlaku untuk semua",
                    "karakter berperan: + * ? ( ) [ ] { } ^ $ | dan backslash",
                    "sendiri. Garis miring / juga di-escape di dalam literal karena",
                    "ia pembatasnya - itu sebabnya tag penutup di contoh atas",
                    "ditulis <\\/b>, bukan </b>.",
                    "",
                    "REGEX BER-FLAG g PUNYA INGATAN. Kalau ia DISIMPAN di variabel,",
                    "posisi pencarian terakhir tersimpan di properti lastIndex, dan",
                    "test() berikutnya melanjutkan dari sana. Efeknya:",
                    "const p = /\\d+/g; lalu p.test(t) tiga kali atas teks yang SAMA",
                    "menghasilkan true, false, true. Aturan amannya: jangan simpan",
                    "regex ber-g di variabel untuk dipakai berulang oleh test() -",
                    "tulis literalnya langsung di tempat, buang flag g-nya, atau",
                    "setel ulang p.lastIndex = 0 sebelum memakainya lagi.",
                    "",
                    "JANGAN MENGURAI HTML DENGAN REGEX. Nasihat klasik, dan",
                    "alasannya nyata: HTML boleh bersarang sedalam apa pun,",
                    "sedangkan regex tidak punya cara menghitung sarang. Pola apa",
                    "pun yang kamu tulis akan benar untuk contohmu dan salah untuk",
                    "halaman sungguhan. Pakai parser - di browser itu DOM.",
                    "",
                    "REGEX YANG TIDAK TERBACA ADALAH REGEX YANG SALAH. Kalau polamu",
                    "sudah sepanjang satu baris penuh, pecah pekerjaannya jadi",
                    "beberapa langkah kecil seperti slug() di atas, atau beri nama",
                    "grup-grupnya. Kode dibaca jauh lebih sering daripada ditulis,",
                    "dan regex adalah tempat aturan itu paling sering dilupakan.",
                ],
            },
        ],
    },
    {
        "title": "10. Array & Method Array (map/filter/reduce)",
        "sections": [
            {
                "body": [
                    "Array = koleksi data berurutan, BISA campur tipe data,",
                    "ukurannya dinamis (mirip List di Java/Python, bukan array C).",
                    "",
                    "  const angka = [10, 20, 30, 40];",
                    "  const campur = [1, \"dua\", true, null];",
                    "",
                    "Operasi dasar:",
                    "  angka.push(50)       -> tambah di akhir",
                    "  angka.pop()          -> hapus & kembalikan elemen terakhir",
                    "  angka.unshift(5)     -> tambah di awal",
                    "  angka.shift()        -> hapus elemen pertama",
                    "  angka.length         -> jumlah elemen",
                    "  angka.indexOf(20)    -> posisi elemen (atau -1 jika tak ada)",
                    "  angka.includes(20)   -> true/false",
                    "",
                    "Di contoh berikut akan muncul bentuk n => n * 2. Itu arrow function,",
                    "cara ringkas menulis fungsi; bentuk penuhnya dibahas di materi",
                    "'Function: Declaration, Expression & Arrow Function'. Untuk sekarang",
                    "bacalah begini: 'untuk tiap n, hasilkan n * 2'.",
                ]
            },
            {
                "heading": "map, filter, reduce - method array PALING PENTING di JS modern",
                "code": """const nilai = [80, 90, 75, 85, 60, 95];

// map: transformasi TIAP elemen, hasil array BARU (sama panjang)
const dikali2 = nilai.map(n => n * 2);
console.log(dikali2);    // [160, 180, 150, 170, 120, 190]

// filter: menyaring elemen sesuai kondisi, hasil array BARU (bisa lebih pendek)
const lulus = nilai.filter(n => n >= 75);
console.log(lulus);      // [80, 90, 75, 85, 95]

// reduce: gabungkan SEMUA elemen jadi SATU nilai
const total = nilai.reduce((acc, n) => acc + n, 0);
console.log(total);      // 485

// method chaining (menggabungkan beberapa method berurutan)
const hasil = nilai
    .filter(n => n >= 75)
    .map(n => n * 1.1)
    .reduce((acc, n) => acc + n, 0);
console.log(hasil.toFixed(2));

// forEach: menjalankan fungsi untuk tiap elemen, TIDAK mengembalikan array baru
nilai.forEach((n, i) => console.log(`Indeks ${i}: ${n}`));

// find & some & every
console.log(nilai.find(n => n > 90));      // 95 (elemen PERTAMA yang cocok)
console.log(nilai.some(n => n > 90));      // true (ADA yang > 90?)
console.log(nilai.every(n => n > 50));     // true (SEMUA > 50?)

// sort (PERHATIAN: default sorting berdasarkan STRING, perlu compare function untuk angka!)
const angkaAcak = [40, 1, 100, 20];
console.log(angkaAcak.sort());               // [1, 100, 20, 40]  -- SALAH! (string order)
console.log(angkaAcak.sort((a, b) => a - b)); // [1, 20, 40, 100] -- BENAR (numeric)"""
            },
            {
                "body": [
                    "Destructuring array (ES6+): mengambil elemen jadi variabel langsung.",
                    "  const [pertama, kedua, ...sisanya] = [1, 2, 3, 4, 5];",
                    "  console.log(pertama, kedua, sisanya);  // 1 2 [3, 4, 5]",
                    "",
                    "Spread operator (...) untuk array:",
                    "  const a = [1, 2, 3];",
                    "  const b = [...a, 4, 5];       // [1, 2, 3, 4, 5] (salinan baru + tambahan)",
                    "  const gabung = [...a, ...b];  // menggabung 2 array",
                    "",
                    "Array.from() & Array.isArray():",
                    "  Array.from({length: 5}, (_, i) => i * 2)  // [0, 2, 4, 6, 8]",
                    "  Array.isArray([1,2,3])   -> true",
                ]
            },
            {
                "heading": "Method array yang melengkapi daftar di atas",
                "body": [
                    "Selain map/filter/reduce, ada sekelompok method yang muncul terus di",
                    "kode nyata. Perhatikan satu hal yang mudah terlewat: slice() ternyata",
                    "bukan cuma milik string - array punya slice() sendiri, dan ia bersaudara",
                    "nama dengan splice() yang artinya jauh berbeda.",
                    "",
                    "  slice(a, b)      MENYALIN sepotong, array asli utuh",
                    "  splice(a, n, ..) MEMOTONG array aslinya di tempat",
                    "",
                    "Daftar lengkap method mana yang mengubah aslinya dan mana yang tidak ada",
                    "di materi 'Nilai vs Referensi & Menyalin Data'.",
                ],
                "code": """const nilai = [80, 90, 75, 85];

// at(): indeks negatif dihitung dari belakang, pengganti arr[arr.length - 1].
console.log(nilai.at(-1), nilai.at(0));       // 85 80

// concat: menyambung dua array, hasilnya array BARU.
console.log(nilai.concat([60, 70]));          // [ 80, 90, 75, 85, 60, 70 ]

// findIndex: saudara find, tapi mengembalikan POSISI (-1 kalau tidak ada).
const daftar = [
    { id: 1, nama: "Andi" },
    { id: 2, nama: "Budi" },
    { id: 3, nama: "Citra" },
];
const i = daftar.findIndex(u => u.id === 2);
console.log(i);                               // 1

// splice(mulai, berapaDihapus, ...yangDisisipkan) MENGUBAH array aslinya.
// Pasangan findIndex + splice adalah pola baku "cari dulu, baru ubah".
daftar.splice(i, 1);
console.log(daftar.map(u => u.nama));         // [ 'Andi', 'Citra' ]
daftar.splice(1, 0, { id: 9, nama: "Dewi" }); // hapus 0, sisipkan di posisi 1
console.log(daftar.map(u => u.nama));         // [ 'Andi', 'Dewi', 'Citra' ]

// slice(mulai, sampai) juga ada di array - dan ia hanya MENYALIN.
console.log([10, 20, 30, 40].slice(1, 3));    // [ 20, 30 ]

// flat & flatMap: meratakan array bersarang.
console.log([1, [2, 3], [4, [5]]].flat());    // [ 1, 2, 3, 4, [ 5 ] ]
console.log([1, [2, 3], [4, [5]]].flat(2));   // [ 1, 2, 3, 4, 5 ]
console.log(["a b", "c d"].flatMap(t => t.split(" ")));   // [ 'a', 'b', 'c', 'd' ]

// fill & Array(n): menyiapkan array berisi nilai awal.
console.log(Array(4).fill(0));                // [ 0, 0, 0, 0 ]
console.log([1, 2, 3, 4].fill(9, 1, 3));      // [ 1, 9, 9, 4 ]

// Versi ES2023 yang TIDAK mengubah aslinya (perhatikan awalan "to").
const asli = [3, 1, 2];
console.log(asli.toSorted((a, b) => a - b));  // [ 1, 2, 3 ]
console.log(asli.toReversed());               // [ 2, 1, 3 ]
console.log(asli.with(0, 99));                // [ 99, 1, 2 ]
console.log(asli);                            // [ 3, 1, 2 ]  <- tetap utuh"""
            },
            {
                "heading": "reduce dibedah: akumulator dan nilai awal",
                "body": [
                    "reduce pantas dibedah sendiri, karena ia satu-satunya method di daftar",
                    "ini yang punya argumen KEDUA - dan argumen itulah yang sering bikin",
                    "orang menghindarinya.",
                    "",
                    "  array.reduce((acc, elemen) => ..., nilaiAwal)",
                    "",
                    "acc ('accumulator') adalah hasil sementara yang DIBAWA dari satu iterasi",
                    "ke iterasi berikutnya. Apa pun yang kamu return jadi acc berikutnya.",
                    "nilaiAwal menentukan acc di iterasi pertama sekaligus TIPE hasil akhir:",
                    "0 untuk menjumlah, {} untuk mengelompokkan, [] untuk menyusun array.",
                    "",
                    "Kalau nilaiAwal dihilangkan, elemen pertama dipakai sebagai acc. Untuk",
                    "array KOSONG itu berarti tidak ada acc sama sekali, dan JavaScript",
                    "melempar TypeError. Kebiasaan menulis nilai awal menutup lubang itu.",
                ],
                "code": """const nilai = [80, 90, 75];

const total = nilai.reduce((acc, n) => acc + n, 0);
//   iterasi 1: acc = 0   n = 80  -> kembalikan 80
//   iterasi 2: acc = 80  n = 90  -> kembalikan 170
//   iterasi 3: acc = 170 n = 75  -> kembalikan 245
console.log(total);   // 245

// Tanpa nilai awal, elemen PERTAMA dipakai sebagai acc dan iterasi dimulai
// dari elemen kedua. Untuk array KOSONG itu langsung melempar error:
try {
    [].reduce((a, b) => a + b);
} catch (e) {
    console.log(e.constructor.name + ":", e.message);
    // TypeError: Reduce of empty array with no initial value
}
console.log([].reduce((a, b) => a + b, 0));   // 0   aman, karena ada nilai awal

// Nilai awalnya tidak harus angka. {} dipakai untuk MENGELOMPOKKAN data:
const siswa = [
    { nama: "Andi", kelas: "A" },
    { nama: "Budi", kelas: "B" },
    { nama: "Citra", kelas: "A" },
];
const perKelas = siswa.reduce((acc, s) => {
    acc[s.kelas] ??= [];      // siapkan wadahnya kalau kelas ini baru muncul
    acc[s.kelas].push(s.nama);
    return acc;               // WAJIB dikembalikan; kalau lupa, acc jadi undefined
}, {});
console.log(perKelas);        // { A: [ 'Andi', 'Citra' ], B: [ 'Budi' ] }

// [] sebagai nilai awal, untuk menyaring dan mengubah dalam satu jalan:
const lulus = [70, 85, 90].reduce((acc, n) => {
    if (n >= 75) acc.push(`nilai ${n}`);
    return acc;
}, []);
console.log(lulus);           // [ 'nilai 85', 'nilai 90' ]"""
            },
            {
                "heading": "Array.from, dan cara array DICETAK",
                "body": [
                    "Array.from sudah lewat sekilas di daftar di atas, satu baris tanpa",
                    "penjelasan. Baris itu menyimpan dua hal yang mustahil ditebak sendiri:",
                    "dari mana { length: 5 } boleh jadi sumber array, dan kenapa parameter",
                    "pertamanya dinamai _. Keduanya dibedah di sini.",
                ],
                "code": """// Array.from(sumber, fungsiMap)
// Sumbernya boleh 'array-like': object yang punya property length tapi BUKAN
// array. { length: 5 } adalah bentuk array-like paling minimal yang ada.
console.log(Array.from({ length: 3 }));   // [ undefined, undefined, undefined ]

// Argumen kedua adalah fungsi map dengan parameter (elemen, indeks). Elemennya
// di sini selalu undefined, jadi dinamai _ - kebiasaan menandai parameter yang
// SENGAJA tidak dipakai. _ cuma nama variabel biasa, bukan operator.
console.log(Array.from({ length: 5 }, (_, i) => i * 2));   // [ 0, 2, 4, 6, 8 ]
console.log(Array.from("halo"));          // [ 'h', 'a', 'l', 'o' ]

// Cara console.log MENCETAK array berbeda dari isi array di dalam teks:
const huruf = ["a", "b"];
console.log(huruf);              // [ 'a', 'b' ]   ada spasi dan tanda kutip
console.log(`${huruf}`);         // a,b            koma saja, tanpa kutip
console.log(huruf.join(", "));   // a, b
console.log(`${[80, 90]}`);      // 80,90
// Perbedaan ini penting: penilai latihan membandingkan keluaranmu huruf per
// huruf, jadi salah memilih di antara ketiganya membuat jawaban ditolak."""
            },
        ],
    },
    {
        "title": "11. Object & Destructuring",
        "sections": [
            {
                "body": [
                    "Object = koleksi pasangan key: value, mirip dict Python /",
                    "HashMap Java. Key biasanya string (bisa tanpa kutip jika valid).",
                    "",
                    "  const mahasiswa = {",
                    "      nama: \"Andi\",",
                    "      umur: 20,",
                    "      jurusan: \"Informatika\"",
                    "  };",
                    "",
                    "  mahasiswa.nama            -> \"Andi\"   (dot notation)",
                    "  mahasiswa[\"nama\"]         -> \"Andi\"   (bracket notation)",
                    "  mahasiswa.kota = \"Jakarta\" -> tambah property baru",
                    "  delete mahasiswa.umur      -> hapus property",
                    "  \"nama\" in mahasiswa        -> true (cek property ada)",
                ]
            },
            {
                "heading": "Object methods & destructuring",
                "code": """const mahasiswa = { nama: "Andi", umur: 20, jurusan: "Informatika" };

console.log(Object.keys(mahasiswa));     // ['nama', 'umur', 'jurusan']
console.log(Object.values(mahasiswa));   // ['Andi', 20, 'Informatika']
console.log(Object.entries(mahasiswa));  // [['nama','Andi'], ['umur',20], ...]

for (const [key, value] of Object.entries(mahasiswa)) {
    console.log(`${key} -> ${value}`);
}

// Object destructuring: ambil property jadi variabel langsung
const { nama, umur } = mahasiswa;
console.log(nama, umur);   // Andi 20

// Dengan default value & rename
const { jurusan: prodi, ipk = 0 } = mahasiswa;
console.log(prodi, ipk);   // Informatika 0

// Spread operator untuk object (menggabung/menyalin)
const tambahan = { ...mahasiswa, ipk: 3.8 };
console.log(tambahan);

// Shorthand property (jika nama variabel = nama key)
const nilai = 90;
const obj = { nilai };   // sama dengan { nilai: nilai }"""
            },
            {
                "body": [
                    "Nested object & optional chaining:",
                    "  const user = { profil: { alamat: { kota: \"Jakarta\" } } };",
                    "  console.log(user.profil?.alamat?.kota);        // 'Jakarta'",
                    "  console.log(user.profil?.pekerjaan?.gaji);     // undefined (aman, tak error)",
                    "",
                    "JSON.stringify & JSON.parse (konversi object <-> teks JSON):",
                    "  const teks = JSON.stringify(mahasiswa);   // object -> string JSON",
                    "  const objek = JSON.parse(teks);           // string JSON -> object",
                ]
            },
            {
                "heading": "Bentuk object literal yang sering ditemui",
                "body": [
                    "Object literal punya beberapa bentuk yang tidak akan pernah kamu tebak",
                    "sendiri, padahal ketiganya ada di hampir tiap object konfigurasi:",
                    "",
                    "  1. Shorthand METHOD. Di atas kamu belajar shorthand PROPERTI",
                    "     ({ nilai } untuk { nilai: nilai }). Method juga punya bentuk",
                    "     ringkasnya: hitung() { ... } saja, tanpa 'function' dan tanpa ':'.",
                    "",
                    "  2. Computed key: { [namaKey]: nilai }. Isi kurung sikunya DIHITUNG",
                    "     dulu, hasilnya jadi nama key. Kurung siku di dalam { } BUKAN",
                    "     array - kalau salah baca ini, seluruh objectnya salah dimengerti.",
                    "",
                    "  3. get dan set boleh ditulis di object literal juga, bukan hanya di",
                    "     dalam class. Getter dibaca tanpa kurung; setter dipanggil oleh",
                    "     tanda sama dengan.",
                ],
                "code": """const hargaSatuan = 5000;
const namaKey = "kode";

const produk = {
    nama: "Pensil",
    hargaSatuan,                 // shorthand PROPERTI: sama dengan hargaSatuan: hargaSatuan

    // shorthand METHOD: tanpa kata 'function', tanpa titik dua.
    hitung(jumlah) {
        return this.hargaSatuan * jumlah;
    },

    // computed key: isi kurung siku dihitung dulu, hasilnya jadi nama key.
    [namaKey]: "PSL-01",
    [`${namaKey}Lama`]: "PSL-00",

    get label() {
        return `${this.nama} (${this.kode})`;
    },
    set label(teks) {
        this.nama = teks.trim();
    },
};

console.log(produk.hitung(3));               // 15000
console.log(produk.kode, produk.kodeLama);   // PSL-01 PSL-00
console.log(produk.label);       // Pensil (PSL-01)   getter dibaca TANPA kurung
produk.label = "  Pulpen  ";     // setter dipanggil oleh tanda = di kiri
console.log(produk.nama);        // Pulpen

// Pola { [item.id]: item }: mengubah array jadi 'kamus' berindeks id, supaya
// mencari satu data tidak perlu menyusur seluruh array berulang kali.
const daftar = [{ id: 7, nama: "Andi" }, { id: 9, nama: "Budi" }];
const perId = daftar.reduce((acc, item) => ({ ...acc, [item.id]: item }), {});
console.log(perId[9].nama);      // Budi"""
            },
            {
                "heading": "Milik sendiri vs warisan: Object.hasOwn",
                "body": [
                    "Pertanyaan yang cepat atau lambat muncul: bagaimana memastikan sebuah",
                    "key benar-benar MILIK object itu, bukan warisan dari prototype?",
                    "",
                    "  Object.hasOwn(obj, key)   true hanya kalau key milik obj sendiri",
                    "  \"key\" in obj              true juga untuk key WARISAN",
                    "  Object.keys(obj)          sejak awal hanya memberi milik sendiri",
                    "",
                    "Ini bukan soal teori. for...in ikut menyapu property warisan, jadi loop",
                    "yang kelihatan benar bisa memproses key yang tidak pernah kamu tulis.",
                    "Di kode lama saringannya ditulis panjang:",
                    "Object.prototype.hasOwnProperty.call(obj, key) - bentuk berbelit itu",
                    "dipakai karena obj sendiri bisa saja punya key bernama hasOwnProperty.",
                    "Object.hasOwn (ES2022) adalah versi pendek yang aman dari masalah itu.",
                ],
                "code": """const dasar = { warna: "hitam" };
const kursi = Object.create(dasar);    // kursi mewarisi dari dasar
kursi.kaki = 4;

for (const key in kursi) {
    console.log("for...in melihat:", key);   // kaki, LALU warna
}

console.log(Object.hasOwn(kursi, "kaki"));    // true
console.log(Object.hasOwn(kursi, "warna"));   // false  warisan, bukan miliknya
console.log("warna" in kursi);                // true   'in' ikut melihat warisan
console.log(Object.keys(kursi));              // [ 'kaki' ]

// Saringan bakunya:
for (const key in kursi) {
    if (!Object.hasOwn(kursi, key)) continue;
    console.log("milik sendiri:", key);       // hanya: kaki
}"""
            },
            {
                "heading": "Destructuring bersarang, di parameter, dan rest property",
                "code": """const respons = {
    status: 200,
    data: { user: { nama: "Andi", alamat: { kota: "Jakarta" } } },
};

// Destructuring BERSARANG: bentuk di sisi kiri meniru bentuk objectnya.
const { data: { user: { nama, alamat: { kota } } } } = respons;
console.log(nama, kota);          // Andi Jakarta

// Destructuring di PARAMETER: isi object yang dipakai langsung terbaca dari
// baris pertama fungsinya, lengkap dengan nilai bawaannya.
const sapa = ({ nama, sapaan = "Halo" }) => `${sapaan}, ${nama}!`;
console.log(sapa({ nama: "Budi" }));                  // Halo, Budi!
console.log(sapa({ nama: "Citra", sapaan: "Hai" }));  // Hai, Citra!

// Rest property: ambil beberapa key, SISANYA dikumpulkan jadi object baru.
const akun = { id: 1, nama: "Andi", sandi: "rahasia", email: "a@b.c" };
const { sandi, ...aman } = akun;
console.log(aman);   // { id: 1, nama: 'Andi', email: 'a@b.c' }
// Inilah pola baku membuang field sensitif sebelum data dikirim keluar."""
            },
        ],
    },
    {
        "title": "12. Nilai vs Referensi & Menyalin Data",
        "sections": [
            {
                "body": [
                    "Ada DUA cara JavaScript menyimpan nilai di dalam variabel. Bedanya menentukan apakah",
                    "kode yang kamu baca masuk akal atau terasa seperti sihir yang berubah sendiri.",
                    "",
                    "  Primitif  -> number, string, boolean, null, undefined, symbol, bigint.",
                    "               Variabel menyimpan NILAInya langsung.",
                    "               Menyalin variabel = menyalin isinya. Dua salinan berdiri sendiri.",
                    "",
                    "  Referensi -> object, array, dan function (array & function juga object di JS).",
                    "               Variabel menyimpan ALAMAT sebuah kotak di memori, bukan isi kotaknya.",
                    "               Menyalin variabel = menyalin alamatnya. Kotaknya tetap SATU.",
                    "",
                    "Gambar yang perlu kamu bawa terus, 'dua nama satu kotak':",
                    "",
                    "  const a = { x: 1 };",
                    "  const b = a;          // b tidak menyalin isinya, ia menyalin alamatnya",
                    "  b.x = 99;",
                    "  console.log(a.x);     // 99  <- a ikut berubah, padahal yang disentuh b",
                    "",
                    "      a --+",
                    "          +--> [ { x: 99 } ]    satu kotak, dua nama menunjuk ke sana",
                    "      b --+",
                    "",
                    "Ini bukan keanehan JavaScript. Java, Python, C#, dan Go berperilaku sama persis;",
                    "yang berbeda cuma istilah yang dipakai buku masing-masing.",
                    "",
                    "KENAPA const angka = [] TETAP BOLEH DI-PUSH?",
                    "",
                    "Materi 'Variabel (var, let, const)' menyebut const 'untuk nilai yang TIDAK BERUBAH',",
                    "lalu materi 'Array & Method Array' menulis const angka = [10, 20, 30] dan langsung",
                    "memanggil angka.push(50). Itu bukan salah ketik: const mengunci NAMA ke satu alamat,",
                    "bukan membekukan isi kotaknya.",
                    "",
                    "  const angka = [1, 2];",
                    "  angka.push(3);      // BOLEH -> isi kotak berubah, alamatnya tetap itu-itu juga",
                    "  angka = [9];        // TypeError -> ini mengganti ALAMAT yang dipegang 'angka'",
                    "",
                    "Jadi bacalah const sebagai 'nama ini tidak akan pernah menunjuk ke tempat lain',",
                    "bukan 'isinya beku'. Yang benar-benar membekukan isi ada di bagian akhir materi ini.",
                ],
            },
            {
                "heading": "Nilai vs alamat, dan fungsi yang diam-diam mengubah milik pemanggilnya",
                "code": """// Primitif: yang disalin adalah NILAInya
let a = 10;
let b = a;
b = 99;
console.log(a, b);              // 10 99  -> a sama sekali tidak terpengaruh

// Object: yang disalin adalah ALAMATnya
const user1 = { nama: "Andi", umur: 20 };
const user2 = user1;            // BUKAN salinan: dua nama, satu kotak
user2.umur = 21;
console.log(user1.umur);        // 21  <- ikut berubah, ini yang mengagetkan
console.log(user1 === user2);   // true (memang object yang SAMA)

// const menahan PENUGASAN ULANG, bukan isi kotaknya
const angka = [10, 20, 30];
angka.push(40);                 // BOLEH: isi berubah, alamatnya tetap
console.log(angka);             // [ 10, 20, 30, 40 ]
// angka = [1, 2];              // TypeError: Assignment to constant variable.

// === membandingkan IDENTITAS, bukan isi
console.log([1, 2] === [1, 2]);      // false (dua kotak berbeda)
console.log({ x: 1 } === { x: 1 });  // false
console.log("ab" === "ab");          // true (primitif dibanding per nilai)

// Fungsi menerima ALAMAT, jadi ia bisa mengubah object milik pemanggil
function tambahBonus(pegawai) {
    pegawai.gaji += 500000;     // mengubah object ASLI di luar fungsi
}
const budi = { nama: "Budi", gaji: 5000000 };
tambahBonus(budi);
console.log(budi.gaji);         // 5500000

// Kebiasaan yang lebih aman: jangan ubah argumen, kembalikan object BARU
function denganBonus(pegawai) {
    return { ...pegawai, gaji: pegawai.gaji + 500000 };
}
const citra = { nama: "Citra", gaji: 5000000 };
const citraBaru = denganBonus(citra);
console.log(citra.gaji, citraBaru.gaji);   // 5000000 5500000""",
            },
            {
                "body": [
                    "AKIBAT PERTAMA: === membandingkan IDENTITAS, bukan isi.",
                    "",
                    "  [1, 2] === [1, 2]           -> false   dua kotak berbeda yang kebetulan seisi",
                    "  { a: 1 } === { a: 1 }       -> false",
                    "  const x = [1, 2]; x === x   -> true    satu kotak yang sama",
                    "",
                    "Karena itu arr.includes(obj) dan arr.indexOf(obj) mencari object yang IDENTIK,",
                    "bukan yang isinya mirip. Untuk mencari 'yang isinya cocok' pakai find/findIndex",
                    "dengan syarat per field (lihat materi 'Array & Method Array').",
                    "",
                    "Cara membandingkan ISI:",
                    "  1. Per field: a.nama === b.nama && a.umur === b.umur",
                    "     Paling jelas dan paling cepat. Pakai ini kalau fieldnya sedikit.",
                    "  2. JSON.stringify(a) === JSON.stringify(b) - gampang ditulis, TAPI:",
                    "       - urutan key ikut dibandingkan: {x:1,y:2} vs {y:2,x:1} dianggap BERBEDA;",
                    "       - undefined, function, dan symbol hilang, sedangkan Date jadi string;",
                    "       - object yang melingkar (a.diri = a) melempar TypeError.",
                    "     Boleh untuk data sederhana, jangan dijadikan alat banding serius.",
                    "  3. Di proyek nyata orang memakai isEqual() dari lodash untuk kasus rumit.",
                    "",
                    "AKIBAT KEDUA: sebagian method array MENGUBAH array aslinya.",
                    "",
                    "  MENGUBAH ASLINYA (mutasi)     MENGEMBALIKAN ARRAY BARU",
                    "  push, pop                     map, filter, reduce",
                    "  shift, unshift                slice, concat",
                    "  splice, fill                  toSorted, toReversed, toSpliced (ES2023)",
                    "  sort, reverse                 flat, flatMap, with(indeks, nilai)",
                    "",
                    "Jebakan yang paling sering menggigit: sort() dan reverse() bukan cuma",
                    "mengembalikan hasil - keduanya mengaduk array aslinya di tempat. Kalau aslinya",
                    "masih dipakai, salin dulu: [...arr].sort((a, b) => a - b), atau pakai",
                    "arr.toSorted((a, b) => a - b) yang memang membuat array baru.",
                    "Perhatikan juga slice() yang MENYALIN versus splice() yang MEMOTONG aslinya:",
                    "dua nama nyaris kembar, dua akibat yang jauh berbeda.",
                ],
            },
            {
                "heading": "Salinan dangkal, salinan dalam, dan Object.freeze",
                "code": """const user = {
    nama: "Andi",
    alamat: { kota: "Jakarta", pos: "10110" },
};

// SALINAN DANGKAL: hanya lapisan PERTAMA yang benar-benar disalin
const salinan = { ...user };
salinan.nama = "Budi";              // aman, ini lapisan pertama
salinan.alamat.kota = "Bandung";    // JEBAKAN: alamat masih kotak yang SAMA
console.log(user.nama);             // Andi
console.log(user.alamat.kota);      // Bandung  <- ikut berubah!

// Object.assign: bentuk sebelum spread ada, masih banyak di kode lama
const gabung = Object.assign({}, user, { nama: "Citra" });
console.log(gabung.nama);                    // Citra
console.log(gabung.alamat === user.alamat);  // true (sama dangkalnya)

// Salinan DALAM manual: salin ulang tiap lapisan yang ikut berubah
const rapi = { ...user, alamat: { ...user.alamat, kota: "Surabaya" } };
console.log(user.alamat.kota, rapi.alamat.kota);   // Bandung Surabaya

// structuredClone: salinan dalam bawaan (Node 17+ dan browser modern)
const klon = structuredClone(user);
klon.alamat.kota = "Medan";
console.log(user.alamat.kota, klon.alamat.kota);   // Bandung Medan

// JSON.parse(JSON.stringify(x)): cara lama, ADA yang hilang di jalan
const asal = { tanggal: new Date(0), kosong: undefined, sapa: () => "hai" };
const lewatJson = JSON.parse(JSON.stringify(asal));
console.log(typeof asal.tanggal, typeof lewatJson.tanggal);  // object string
console.log("kosong" in lewatJson, "sapa" in lewatJson);     // false false

// Object.freeze: mengunci object -- tapi juga cuma SATU lapis
const setelan = Object.freeze({ tema: "gelap", font: { ukuran: 14 } });
setelan.tema = "terang";       // gagal diam-diam (non-strict), tema tetap
setelan.font.ukuran = 20;      // TEMBUS: lapisan dalam tidak ikut dibekukan
console.log(setelan.tema, setelan.font.ukuran);   // gelap 20""",
            },
            {
                "body": [
                    "Rangkuman cara menyalin, diurutkan dari yang paling dangkal:",
                    "",
                    "  {...obj} atau Object.assign({}, obj)",
                    "      Satu lapis. Paling sering dipakai, dan cukup untuk object yang datar.",
                    "  [...arr] atau arr.slice()",
                    "      Satu lapis juga. Array barunya berisi object-object yang SAMA persis.",
                    "  { ...u, alamat: { ...u.alamat } }",
                    "      Dalam, tapi hanya di jalur yang kamu tulis sendiri.",
                    "  structuredClone(obj)",
                    "      Dalam dan benar: object bersarang, array, Date, Map, Set ikut tersalin.",
                    "      Tidak bisa menyalin function; object berisi function melempar DataCloneError.",
                    "  JSON.parse(JSON.stringify(obj))",
                    "      Dalam tapi rugi: Date jadi string, undefined & function lenyap,",
                    "      dan object melingkar langsung error. Pakai hanya untuk data JSON polos.",
                    "",
                    "Object.assign({}, a, b) adalah bentuk sebelum spread lahir (ES6, 2015). Kamu akan",
                    "terus menemukannya di kode Redux dan library lama; artinya persis sama dengan",
                    "{ ...a, ...b }, termasuk sama-sama cuma satu lapis.",
                    "",
                    "Kebiasaan yang menyelamatkan:",
                    "  1. Curigai setiap 'b = a' pada object atau array - itu bukan salinan.",
                    "  2. Jangan mengubah object yang diterima sebagai argumen; kembalikan yang baru.",
                    "  3. Ingat 'cuma satu lapis'. Pola { ...state, user: { ...state.user, nama: 'X' } }",
                    "     adalah cara baku memperbarui state di React & Redux, dan alasannya ada di",
                    "     materi ini: kalau lapisan dalam tidak ikut disalin, data lama ikut berubah.",
                    "  4. Object.freeze() enak untuk konstanta konfigurasi, tapi ia pun satu lapis.",
                    "     Yang harus beku sampai ke dalam wajib dibekukan lapis demi lapis sendiri.",
                ],
            },
        ],
    },
    {
        "title": "13. Map & Set",
        "sections": [
            {
                "body": [
                    "Di materi Object & Destructuring, object literal sudah dipakai sebagai 'kamus'",
                    "key -> value. Untuk data kecil itu memang cukup. Tapi object punya empat batas",
                    "yang baru terasa ketika datanya sungguhan:",
                    "",
                    "  - Key-nya SELALU diubah jadi string. obj[1] dan obj[\"1\"] menunjuk tempat yang",
                    "    sama, dan obj[{ id: 7 }] menyimpan ke key bernama \"[object Object]\" - jadi",
                    "    dua object berbeda saling menimpa tanpa satu pun peringatan.",
                    "  - Urutannya bukan urutan penulisan. Key yang berbentuk angka dilompatkan ke",
                    "    depan dan diurutkan menaik: Object.keys({ 2: \"b\", 1: \"a\", z: \"z\" }) memberi",
                    "    ['1', '2', 'z'].",
                    "  - Tidak ada obj.length. Menghitung isinya harus lewat Object.keys(obj).length.",
                    "  - Ia mewarisi property dari prototype (lihat materi Prototype), jadi",
                    "    obj[\"toString\"] sudah berisi sesuatu padahal kamu tidak pernah menaruhnya.",
                    "",
                    "Map dan Set adalah dua struktur data bawaan yang menutup semua itu. Namanya",
                    "sempat lewat di materi Perulangan sebagai contoh iterable; di sini kita pakai",
                    "sungguhan, karena di kode nyata keduanya ada di mana-mana.",
                    "",
                    "  Map -> kumpulan pasangan key -> value. Key boleh APA SAJA dan urutannya",
                    "         dijamin persis urutan penyisipan.",
                    "  Set -> kumpulan nilai yang dijamin TIDAK punya duplikat.",
                    "",
                    "Keduanya punya .size untuk jumlah isi - .size, BUKAN .length. Menulis",
                    "map.length tidak menimbulkan error; ia cuma undefined, dan kodenya salah diam-diam.",
                ],
            },
            {
                "heading": "Map: mengisi, membaca, dan menelusuri",
                "code": """// Map dibuat kosong, atau dari daftar pasangan [key, value]
const stok = new Map([
    ["beras", 12],
    ["gula", 5],
]);

stok.set("kopi", 8);       // menambah
stok.set("gula", 7);       // key yang sudah ada -> nilainya DIGANTI, bukan ditambah

console.log(stok.get("gula"));   // 7
console.log(stok.get("teh"));    // undefined  (key tidak ada, bukan error)
console.log(stok.has("teh"));    // false
console.log(stok.size);          // 3   <- .size, BUKAN .length

stok.delete("beras");            // true kalau key-nya memang ada
console.log(stok.size);          // 2

// Key tidak harus string, dan tipenya ikut dibedakan
const label = new Map();
label.set(1, "angka satu");
label.set("1", "teks satu");     // 1 dan "1" adalah DUA key berbeda
label.set(true, "ya");
console.log(label.get(1), label.get("1"), label.get(true));

// Bahkan object dan fungsi boleh jadi key -- ini yang MUSTAHIL di object literal
const budi = { nama: "Budi" };
const sapa = () => "halo";
const catatan = new Map();
catatan.set(budi, 90);
catatan.set(sapa, "fungsi penyapa");
console.log(catatan.get(budi), catatan.get(sapa));   // 90 fungsi penyapa

// Menelusuri: urutannya persis urutan penyisipan, selalu
for (const [nama, jumlah] of stok) {
    console.log(`${nama}: ${jumlah}`);
}

console.log([...stok.keys()]);      // [ 'gula', 'kopi' ]
console.log([...stok.values()]);    // [ 7, 8 ]
console.log([...stok.entries()]);   // [ [ 'gula', 7 ], [ 'kopi', 8 ] ]
console.log([...stok]);             // sama persis dengan .entries()

// Map tidak punya .map/.filter. Ubah dulu jadi array, baru diolah seperti biasa
const banyak = [...stok].filter(([, jumlah]) => jumlah >= 8);
console.log(banyak);                // [ [ 'kopi', 8 ] ]

// Bolak-balik dengan object biasa
const objek = { a: 1, b: 2 };
const dariObjek = new Map(Object.entries(objek));
console.log(dariObjek.get("b"));              // 2
console.log(Object.fromEntries(dariObjek));   // { a: 1, b: 2 }

stok.clear();                       // kosongkan seluruh isinya
console.log(stok.size);             // 0""",
            },
            {
                "body": [
                    "Empat jebakan Map yang tidak memunculkan error:",
                    "",
                    "1. map[key] BUKAN cara mengakses isi Map.",
                    "   cache[\"x\"] = 1 memasang property biasa pada objek Map-nya, persis seperti",
                    "   menempel stiker di luar kotak. Isi Map-nya tidak tersentuh:",
                    "   cache.size tetap 0 dan cache.get(\"x\") tetap undefined.",
                    "   Yang benar cuma .set() dan .get(). Ini kesalahan nomor satu orang yang baru",
                    "   pindah dari object, dan tidak ada satu pun pesan yang memberitahu.",
                    "",
                    "2. Key berupa object dibandingkan lewat IDENTITAS, bukan isinya.",
                    "   m.set({ id: 1 }, \"a\"); m.get({ id: 1 })  ->  undefined,",
                    "   karena kurung kurawal kedua membuat object BARU di alamat lain.",
                    "   Simpan dulu objectnya di variabel kalau mau dipakai sebagai key.",
                    "",
                    "3. JSON.stringify(map) menghasilkan \"{}\".",
                    "   Map bukan object biasa, jadi JSON tidak tahu cara membacanya. Untuk",
                    "   menyimpannya: JSON.stringify(Object.fromEntries(map)) atau",
                    "   JSON.stringify([...map]) kalau key-nya bukan string.",
                    "",
                    "4. Map tidak ikut ter-clone oleh { ...map }. Hasilnya object kosong.",
                    "   Salinan Map dibuat dengan new Map(map).",
                    "",
                    "Kapan pakai Map, kapan cukup object literal:",
                    "",
                    "  Kebutuhan                                  Pilih",
                    "  -----------------------------------------  ---------------------",
                    "  Key bukan string (angka, object, fungsi)   Map",
                    "  Key datang dari input pemakai              Map (aman dari prototype)",
                    "  Urutan isi harus terjaga apa adanya        Map",
                    "  Sering menambah & menghapus key            Map",
                    "  Butuh jumlah isi setiap saat               Map (.size)",
                    "  Bentuk data tetap, field-nya sudah pasti   object literal",
                    "  Perlu langsung jadi JSON                   object literal",
                    "",
                    "Sepupu lemahnya: WeakMap & WeakSet. Keduanya hanya menerima object sebagai",
                    "key/isi, tidak bisa ditelusuri, dan tidak punya .size. Gunanya satu: entri di",
                    "dalamnya TIDAK menghalangi object itu dibersihkan dari memori saat tidak ada",
                    "lagi yang memakainya. Map biasa menahan key-nya hidup selamanya - itu jadi",
                    "kebocoran memori kalau key-nya elemen DOM atau object yang berumur pendek.",
                    "Kamu akan melihatnya di kode library; untuk sekarang cukup tahu kenapa ia ada.",
                ],
            },
            {
                "heading": "Set: membuang duplikat dan operasi himpunan",
                "code": """const id = [7, 3, 7, 9, 3, 3, 1];

// new Set(array) membuang duplikat; urutan kemunculan PERTAMA dipertahankan
const unik = new Set(id);
console.log(unik.size);        // 4  (dari 7 angka, yang unik cuma 4)
console.log([...unik]);        // [ 7, 3, 9, 1 ]

// Idiom baku deduplikasi array, satu baris, hafalkan bentuknya:
const idUnik = [...new Set(id)];
console.log(idUnik);           // [ 7, 3, 9, 1 ]

const izin = new Set(["baca", "tulis"]);
izin.add("hapus");
izin.add("baca");              // sudah ada -> tidak terjadi apa-apa, bukan error
console.log(izin.has("tulis"), izin.has("admin"));   // true false
izin.delete("hapus");
console.log(izin.size);        // 2
for (const nama of izin) console.log(nama);          // baca, tulis

// Irisan & selisih: filter + has
const a = [1, 2, 3, 4, 5];
const b = [4, 5, 6, 7];
const setB = new Set(b);
console.log(a.filter((n) => setB.has(n)));    // [ 4, 5 ]  ada di A DAN di B
console.log(a.filter((n) => !setB.has(n)));   // [ 1, 2, 3 ]  ada di A saja
console.log([...new Set([...a, ...b])]);      // gabungan, tanpa duplikat

// Kenapa lewat Set, bukan b.includes(n)? includes menyisir b dari awal untuk
// SETIAP elemen a. Pada daftar ribuan baris bedanya terasa jelas.

// JEBAKAN: Set membandingkan object lewat identitas, bukan isinya
console.log(new Set([{ id: 1 }, { id: 1 }]).size);   // 2, bukan 1!
console.log(new Set(["1", 1]).size);                 // 2, "1" bukan 1""",
            },
            {
                "heading": "Contoh nyata: cache hasil dan menghitung frekuensi kata",
                "code": """// 1. Cache -- pola paling umum kenapa Map dipakai di kode nyata
const cache = new Map();
let kerjaBerat = 0;

function pangkatTiga(n) {
    if (cache.has(n)) return cache.get(n);   // sudah pernah dihitung -> ambil saja
    kerjaBerat++;
    const hasil = n * n * n;
    cache.set(n, hasil);
    return hasil;
}

console.log(pangkatTiga(4), pangkatTiga(4), pangkatTiga(9));   // 64 64 729
console.log(`Perhitungan sungguhan: ${kerjaBerat}x`);          // 2x, bukan 3x

// PENTING: cek dengan .has(), jangan `if (cache.get(n))`. Nilai 0, "", null,
// dan false itu falsy, jadi hasil yang SAH pun akan dikira "belum ada"
// dan dihitung ulang terus-menerus.

// 2. Menghitung frekuensi kata
const kalimat = "ada gula ada semut ada gula";
const frekuensi = new Map();

for (const kata of kalimat.split(" ")) {
    frekuensi.set(kata, (frekuensi.get(kata) || 0) + 1);   // 0 untuk kata baru
}

for (const [kata, jumlah] of frekuensi) {
    console.log(`${kata}: ${jumlah}`);
}

// Urutkan dari yang paling sering: ubah jadi array dulu
const terbanyak = [...frekuensi].sort((x, y) => y[1] - x[1]);
console.log(terbanyak[0]);        // [ 'ada', 3 ]

// 3. Deduplikasi daftar id sambil menjaga urutannya
const kunjungan = ["u9", "u2", "u9", "u5", "u2"];
console.log([...new Set(kunjungan)]);    // [ 'u9', 'u2', 'u5' ]""",
            },
        ],
    },
    {
        "title": "14. Function: Declaration, Expression & Arrow Function",
        "sections": [
            {
                "body": [
                    "JavaScript punya BEBERAPA cara membuat fungsi:",
                    "",
                    "1. Function declaration (di-'hoist', bisa dipanggil sebelum",
                    "   dideklarasikan di kode):",
                    "   function tambah(a, b) {",
                    "       return a + b;",
                    "   }",
                    "",
                    "2. Function expression (disimpan ke variabel, TIDAK di-hoist):",
                    "   const tambah = function(a, b) {",
                    "       return a + b;",
                    "   };",
                    "",
                    "3. Arrow function (ES6+, sintaks ringkas, PALING UMUM dipakai):",
                    "   const tambah = (a, b) => a + b;",
                ]
            },
            {
                "heading": "Berbagai bentuk arrow function",
                "code": """// Satu parameter, satu ekspresi (kurung parameter opsional)
const kuadrat = x => x * x;
console.log(kuadrat(5));    // 25

// Banyak parameter
const tambah = (a, b) => a + b;
console.log(tambah(3, 4));  // 7

// Banyak statement, perlu { } dan return eksplisit
const proses = (a, b) => {
    const hasil = a + b;
    console.log("Menghitung...");
    return hasil;
};

// Tanpa parameter
const sapa = () => console.log("Halo!");

// Default parameter & rest parameter
function sapaOrang(nama, sapaan = "Halo") {
    console.log(`${sapaan}, ${nama}!`);
}
sapaOrang("Andi");              // Halo, Andi!
sapaOrang("Budi", "Hai");       // Hai, Budi!

function total(...angka) {      // rest parameter: kumpulkan jadi array
    return angka.reduce((a, b) => a + b, 0);
}
console.log(total(1, 2, 3, 4)); // 10"""
            },
            {
                "body": [
                    "Perbedaan PENTING arrow function vs function biasa (dibahas",
                    "lebih detail di materi 'this Keyword'):",
                    "  1. Arrow function TIDAK punya 'this' sendiri - mewarisi",
                    "     'this' dari scope di luarnya (lexical this).",
                    "  2. Arrow function TIDAK bisa dipakai sebagai constructor (new).",
                    "  3. Arrow function TIDAK punya objek 'arguments'.",
                    "     ('arguments' itu apa dijelaskan di materi 'Pola Fungsi: IIFE,",
                    "      Rekursi, dan Currying' - ia peninggalan sebelum rest parameter",
                    "      ada, dan masih sering muncul di kode lama.)",
                    "",
                    "Function sebagai 'first-class citizen': bisa disimpan ke variabel,",
                    "dikirim sebagai argumen, dan dikembalikan dari fungsi lain",
                    "(dasar dari higher-order function & callback).",
                ]
            },
            {
                "heading": "Arrow yang mengembalikan object WAJIB dibungkus kurung",
                "body": [
                    "Satu jebakan sintaks arrow function yang PASTI kamu temui, dan yang",
                    "paling jahat karena tidak melempar error apa pun:",
                    "",
                    "  data.map(u => { nama: u.nama })     <- hasilnya undefined semua",
                    "  data.map(u => ({ nama: u.nama }))   <- yang benar",
                    "",
                    "Sesudah tanda =>, kurung kurawal { dibaca sebagai awal BLOK KODE, bukan",
                    "awal object literal. Blok itu tidak punya return, jadi tiap panggilan",
                    "mengembalikan undefined - diam-diam, tanpa peringatan. Membungkus",
                    "objectnya dengan kurung biasa memaksa JavaScript membacanya sebagai",
                    "EKSPRESI, dan artinya kembali seperti yang kamu maksud.",
                    "",
                    "Kalau ragu, tulis saja bentuk panjangnya dengan return eksplisit.",
                ],
                "code": """const data = [{ nama: "Andi", umur: 20 }, { nama: "Budi", umur: 21 }];

// SALAH: kurung kurawal sesudah => dibaca sebagai awal BLOK KODE, bukan object.
const salah = data.map(u => { nama: u.nama });
console.log(salah);   // [ undefined, undefined ]  <- tanpa error sama sekali

// BENAR: bungkus objectnya dengan kurung supaya dibaca sebagai EKSPRESI.
const benar = data.map(u => ({ nama: u.nama }));
console.log(benar);   // [ { nama: 'Andi' }, { nama: 'Budi' } ]

// Bentuk panjang yang selalu aman kalau ragu - return-nya ditulis sendiri:
const jelas = data.map(u => {
    return { nama: u.nama };
});
console.log(jelas);   // [ { nama: 'Andi' }, { nama: 'Budi' } ]"""
            },
        ],
    },
    {
        "title": "15. Scope & Closure",
        "sections": [
            {
                "body": [
                    "Scope = area di mana sebuah variabel bisa diakses.",
                    "",
                    "  Global scope   -> variabel bisa diakses dari mana saja.",
                    "  Function scope -> var hanya dikenal di dalam fungsi.",
                    "  Block scope    -> let/const hanya dikenal di dalam { } terdekat.",
                    "",
                    "  if (true) {",
                    "      var x = 1;     // 'bocor' keluar blok if (function-scoped)",
                    "      let y = 2;     // HANYA ada di dalam blok if ini",
                    "  }",
                    "  console.log(x);   // 1 (bisa diakses!)",
                    "  console.log(y);   // ReferenceError! (tidak bisa diakses)",
                    "",
                    "Inilah salah satu alasan UTAMA kenapa 'let/const' lebih",
                    "disarankan daripada 'var' di kode JavaScript modern.",
                ]
            },
            {
                "heading": "Closure: fungsi yang 'mengingat' scope tempat ia dibuat",
                "code": """function buatCounter() {
    let hitung = 0;              // variabel privat, tersembunyi di luar

    return function () {         // fungsi dalam 'menutup' (closure) atas 'hitung'
        hitung++;
        return hitung;
    };
}

const counter1 = buatCounter();
console.log(counter1());   // 1
console.log(counter1());   // 2
console.log(counter1());   // 3

const counter2 = buatCounter();  // instance BARU, hitung terpisah
console.log(counter2());   // 1 (tidak terpengaruh counter1)

// Closure untuk membuat fungsi 'privat' (mirip encapsulation)
function buatRekening(saldoAwal) {
    let saldo = saldoAwal;
    return {
        setor: (jumlah) => { saldo += jumlah; return saldo; },
        cekSaldo: () => saldo,
    };
}
const rekening = buatRekening(100000);
rekening.setor(50000);
console.log(rekening.cekSaldo());   // 150000
// 'saldo' TIDAK BISA diakses langsung dari luar - hanya lewat method!"""
            },
            {
                "body": [
                    "Kenapa closure penting & sering ditanyakan saat wawancara kerja:",
                    "  1. Dasar dari banyak pola JavaScript (module pattern, currying).",
                    "  2. Menjadi cara membuat 'private variable' sebelum ada class.",
                    "  3. Dipakai luas di React (custom hooks) dan library modern lain.",
                    "",
                    "Classic bug closure di dalam loop (SERING ditanya):",
                    "  for (var i = 0; i < 3; i++) {",
                    "      setTimeout(() => console.log(i), 100);",
                    "  }",
                    "  // Output: 3 3 3  (BUKAN 0 1 2!) karena 'var' function-scoped,",
                    "  // ketiga closure berbagi 'i' YANG SAMA.",
                    "  // SOLUSI: ganti 'var' jadi 'let' (block-scoped, tiap iterasi",
                    "  // punya salinan 'i' sendiri) -> hasilnya jadi 0 1 2.",
                ]
            },
            {
                "heading": "Hoisting var vs Temporal Dead Zone let/const",
                "body": [
                    "Kebocoran blok di atas baru separuh cerita 'var'. Separuh lainnya",
                    "namanya HOISTING, dan ia bukan cuma soal fungsi.",
                    "",
                    "Sebelum sebuah scope dijalankan, JavaScript mendaftarkan dulu semua",
                    "deklarasi di dalamnya. Yang naik ke atas hanya DEKLARASINYA; nilainya",
                    "tetap tinggal di barisnya semula. Untuk var, akibatnya:",
                    "",
                    "  console.log(x);   // undefined  <- bukan error!",
                    "  var x = 5;",
                    "",
                    "let dan const JUGA terangkat, tapi JavaScript menolak membacanya sampai",
                    "baris deklarasinya benar-benar dijalankan. Rentang 'sudah terdaftar tapi",
                    "belum boleh dipakai' itu namanya Temporal Dead Zone (TDZ), dan pesan",
                    "errornya berbunyi:",
                    "",
                    "  ReferenceError: Cannot access 'x' before initialization",
                    "",
                    "Pesan itu terdengar tidak masuk akal kalau kamu belum tahu TDZ -",
                    "variabelnya jelas-jelas ada di kode, beberapa baris di bawah. Bedakan",
                    "dari 'x is not defined', yang berarti nama itu memang tidak ada",
                    "di mana pun.",
                    "",
                    "Inilah alasan yang lebih tajam untuk memilih let/const: var memberi",
                    "undefined dalam diam, let/const berhenti dan memberi tahu.",
                ],
                "code": """// 1. var: DEKLARASINYA diangkat ke atas scope, NILAINYA tidak ikut naik.
console.log(x);      // undefined  <- bukan error, dan justru itu masalahnya
var x = 5;
console.log(x);      // 5

// Yang sebenarnya dijalankan mesin JS:
//     var x;              deklarasi naik, isinya masih undefined
//     console.log(x);
//     x = 5;

// 2. let dan const juga terdaftar sejak awal, tapi HARAM disentuh sampai
//    baris deklarasinya dijalankan. Itulah Temporal Dead Zone.
try {
    console.log(y);
    let y = 5;
} catch (e) {
    console.log(e.constructor.name + ":", e.message);
    // ReferenceError: Cannot access 'y' before initialization
}

// Bandingkan dengan nama yang memang TIDAK PERNAH ada di mana pun:
try {
    console.log(belumPernahDitulis);
} catch (e) {
    console.log(e.constructor.name + ":", e.message);
    // ReferenceError: belumPernahDitulis is not defined
}"""
            },
        ],
    },
    {
        "title": "16. Pola Fungsi: IIFE, Rekursi, dan Currying",
        "sections": [
            {
                "body": [
                    "Tiga pola di materi ini semuanya berdiri di atas closure yang baru saja",
                    "kamu pelajari. Ketiganya jarang diajarkan, tapi ketiganya ADA di kode yang",
                    "akan kamu buka besok - jadi tujuannya bukan supaya kamu menulisnya, tapi",
                    "supaya kamu tidak berhenti membaca saat menemukannya.",
                    "",
                    "IIFE (Immediately Invoked Function Expression) = fungsi yang LANGSUNG",
                    "dipanggil di tempat ia ditulis, tanpa pernah diberi nama.",
                    "",
                    "  (function () { ... })();     <- bentuk klasik",
                    "  (() => { ... })();           <- bentuk arrow",
                    "",
                    "Bacanya dua bagian:",
                    "  - Kurung LUAR membungkus fungsinya jadi sebuah EKSPRESI. Tanpa kurung",
                    "    itu, baris yang diawali kata 'function' dibaca sebagai DEKLARASI",
                    "    fungsi, dan deklarasi tidak boleh langsung dipanggil. Node menjawab:",
                    "    SyntaxError: Function statements require a function name.",
                    "  - Kurung KEDUA, () yang di ujung, adalah pemanggilannya. Sama persis",
                    "    dengan () yang kamu tulis saat memanggil fungsi biasa.",
                    "",
                    "Kenapa bentuk ini ada: sebelum ES6 punya module (materi 'Module",
                    "(import/export) & npm Dasar'), JavaScript tidak punya cara lain membuat",
                    "scope privat. Semua 'var' di level atas sebuah berkas menempel ke objek",
                    "global, jadi dua <script> di satu halaman bisa saling menimpa variabel",
                    "tanpa ada yang memberi tahu. Membungkus seluruh isi berkas dengan IIFE",
                    "membuatnya tidak bocor ke mana-mana.",
                    "Itu sebabnya berkas JS lama - dan hampir semua hasil bundling di folder",
                    "dist/ - DIBUKA oleh baris yang bentuknya seperti itu.",
                    "",
                    "Baris pertama di dalamnya sering \"use strict\"; karena mode ketat berlaku",
                    "PER FUNGSI. Menaruhnya di dalam IIFE menyalakannya untuk kode kita saja,",
                    "tanpa ikut mengubah aturan main skrip orang lain di halaman yang sama.",
                    "",
                    "Satu pemakaian IIFE yang masih hidup sampai hari ini: 'await' hanya boleh",
                    "dipakai di dalam fungsi async (materi 'Asynchronous JavaScript:",
                    "async/await'). Level atas sebuah skrip biasa (berkas .js CommonJS di",
                    "Node, atau <script> tanpa type=\"module\") bukan fungsi async, jadi",
                    "menulis 'await ambilData()' di baris paling luar = SyntaxError.",
                    "Pembungkus standarnya:",
                    "",
                    "  (async () => {",
                    "      const data = await ambilData();",
                    "      console.log(data);",
                    "  })();",
                ],
            },
            {
                "heading": "IIFE, async IIFE, dan module pattern",
                "code": """// 1. IIFE klasik: function expression yang LANGSUNG dipanggil.
//    Kurung LUAR membuatnya jadi ekspresi; kurung () di ujung memanggilnya.
(function () {
    "use strict";
    var pesan = "aku hanya hidup di dalam IIFE ini";
    console.log(pesan);
})();

// console.log(pesan);   // ReferenceError: pesan is not defined -> tidak bocor keluar

// 2. Versi arrow, bentuk yang paling sering ditulis sekarang.
(() => {
    console.log("IIFE versi arrow");
})();

// 3. IIFE boleh menerima argumen dan mengembalikan nilai.
const versi = (function (nama) {
    return nama + " v1.0";
})("Kalkulator");
console.log(versi);                  // Kalkulator v1.0

// 4. Module pattern: IIFE + closure yang mengembalikan object berisi method publik.
const Keranjang = (function () {
    let isi = [];                    // PRIVAT: tidak ada jalan ke sini dari luar

    function hitungTotal() {         // helper privat, tidak ikut dikembalikan
        return isi.reduce((jml, b) => jml + b.harga, 0);
    }

    return {                         // yang di-return inilah "API publik"-nya
        tambah(nama, harga) {
            isi.push({ nama, harga });
            return this;             // supaya pemanggilannya bisa dirangkai
        },
        total: () => hitungTotal(),
        jumlahItem: () => isi.length,
    };
})();

Keranjang.tambah("Buku", 50000).tambah("Pulpen", 5000);
console.log(Keranjang.jumlahItem(), Keranjang.total());   // 2 55000
console.log(Keranjang.isi);          // undefined - 'isi' benar-benar tersembunyi

// 5. Async IIFE: cara memakai await di level atas sebuah skrip biasa.
(async () => {
    const data = await Promise.resolve("data sudah siap");
    console.log("di dalam async IIFE:", data);
})();
console.log("baris ini tercetak DULUAN, tidak menunggu await di atas");""",
            },
            {
                "heading": "Peninggalan sebelum arrow function: arguments & var self = this",
                "body": [
                    "Dua pola berikut sudah ada penggantinya, tapi kode lama penuh dengan",
                    "keduanya. Perlu bisa DIBACA, tidak perlu lagi ditulis.",
                    "",
                    "1. Objek 'arguments'. Materi 'Function: Declaration, Expression &",
                    "   Arrow Function' menyebutnya sebagai sesuatu yang TIDAK dimiliki",
                    "   arrow function - ini bendanya. Setiap function BIASA otomatis",
                    "   punya variabel bernama 'arguments' berisi SEMUA argumen yang masuk,",
                    "   termasuk yang tidak ditulis di daftar parameter. Sebelum ada rest",
                    "   parameter (...angka), inilah satu-satunya cara membuat fungsi yang",
                    "   menerima argumen sebanyak-banyaknya.",
                    "   Jebakannya: bentuknya MIRIP array - punya .length dan arguments[0] -",
                    "   tapi BUKAN array. Tidak ada .map, .filter, .reduce di sana. Karena itu",
                    "   kode lama penuh Array.prototype.slice.call(arguments): 'meminjam'",
                    "   method slice milik array untuk mengubahnya jadi array betulan.",
                    "   Jebakan kedua, khas Node: berkas .js CommonJS diam-diam dibungkus",
                    "   sebuah fungsi oleh Node, jadi 'arguments' di level atas berkas TIDAK",
                    "   error - isinya malah 5 argumen internal Node (exports, require,",
                    "   module, __filename, __dirname). Di browser, itu ReferenceError.",
                    "",
                    "2. 'var self = this' (kadang ditulis 'var that = this'). Sebelum arrow",
                    "   function ada, callback di dalam sebuah method punya 'this' sendiri",
                    "   yang salah (materi 'Keyword this'). Akalnya: salin 'this' ke",
                    "   variabel biasa, sebab VARIABEL ikut tertangkap closure sedangkan",
                    "   'this' tidak. Begitu kamu lihat 'self' atau 'that' di kode lama,",
                    "   itulah yang sedang terjadi.",
                ],
                "code": """// Setiap function BIASA otomatis punya variabel 'arguments'.
function jumlahLama() {                  // perhatikan: daftar parameternya KOSONG
    console.log(arguments.length);       // 3
    console.log(arguments[0]);           // 10
    // arguments MIRIP array, tapi BUKAN array: tidak punya .map/.filter/.reduce
    var angka = Array.prototype.slice.call(arguments);   // "pinjam" slice milik array
    return angka.reduce(function (a, b) { return a + b; }, 0);
}
console.log(jumlahLama(10, 20, 30));     // 60

// Penggantinya di kode modern: rest parameter (materi Function). Ini array betulan.
const jumlahBaru = (...angka) => angka.reduce((a, b) => a + b, 0);
console.log(jumlahBaru(10, 20, 30));     // 60

// Arrow function tidak punya 'arguments' sendiri - ia MEMINJAM milik fungsi luar.
function luar() {
    const dalam = () => arguments[0];    // 'arguments' di sini milik luar()
    return dalam();
}
console.log(luar("A", "B"));             // A  (bukan undefined, bukan error)

// Pola lama 'var self = this', dipakai sebelum arrow function ada.
function Pencacah() {
    var self = this;                     // salin 'this' ke variabel biasa...
    self.nilai = 0;
    this.mulai = function () {
        setTimeout(function () {
            self.nilai++;                // ...supaya callback ini masih menemukannya
            console.log("nilai:", self.nilai);
            // kalau di sini ditulis 'this', isinya BUKAN objek Pencacah - lihat materi this
        }, 0);
    };
}
new Pencacah().mulai();                  // nilai: 1""",
            },
            {
                "heading": "Rekursi: fungsi yang memanggil dirinya sendiri",
                "body": [
                    "Rekursi = fungsi yang memanggil DIRINYA SENDIRI dengan soal yang lebih",
                    "kecil setiap kali, sampai ketemu soal yang jawabannya sudah jelas.",
                    "",
                    "Dua bagian yang WAJIB ada, dan urutan menulisnya penting:",
                    "  1. Base case - kondisi berhenti. Ditulis PALING ATAS, pakai return.",
                    "  2. Langkah rekursif - memanggil diri sendiri dengan nilai yang",
                    "     BERGERAK MENUJU base case (n - 1, anak berikutnya, dan seterusnya).",
                    "",
                    "Lupa base case - atau menulis langkah yang tidak pernah sampai ke sana -",
                    "menghasilkan error yang cepat atau lambat pasti kamu temui:",
                    "",
                    "  RangeError: Maximum call stack size exceeded",
                    "",
                    "Ingat call stack dari materi 'Asynchronous JavaScript: Callback':",
                    "tiap pemanggilan fungsi menaruh satu 'kartu' di tumpukan, dan kartu",
                    "itu baru diangkat setelah fungsinya return. Rekursi yang tidak pernah",
                    "return terus menumpuk kartu sampai tumpukannya penuh (sekitar sepuluh",
                    "ribu tingkat di Node) lalu meledak.",
                    "Jadi error itu hampir selalu berarti satu hal saja: base case-nya tidak",
                    "pernah kena. Cek dua hal - apakah base case-nya ada, dan apakah nilai",
                    "yang dikirim ke pemanggilan berikutnya benar-benar bergerak ke arahnya.",
                    "",
                    "Kapan rekursi dipakai di kode nyata: saat KEDALAMAN datanya tidak",
                    "diketahui sejak awal. JSON bersarang dari API, pohon komentar, struktur",
                    "folder, pohon DOM (element.children yang isinya element lagi, materi",
                    "'DOM Manipulation & Event Dasar'), dan menyalin object sampai ke",
                    "dalam-dalamnya. Loop biasa tidak bisa dipakai di situ karena kamu tidak",
                    "tahu harus menulis berapa lapis for.",
                ],
                "code": """function faktorial(n) {
    if (n <= 1) return 1;                // BASE CASE: berhenti di sini
    return n * faktorial(n - 1);         // soal yang sama, ukurannya lebih kecil
}
console.log(faktorial(5));               // 120  = 5*4*3*2*1

function jumlahSampai(n) {
    if (n === 0) return 0;               // base case
    return n + jumlahSampai(n - 1);
}
console.log(jumlahSampai(10));           // 55

// Kasus nyata 1: menelusuri JSON bersarang yang kedalamannya tidak diketahui.
const menu = {
    nama: "Root",
    anak: [
        {
            nama: "Produk",
            anak: [
                { nama: "Sepatu", anak: [] },
                { nama: "Tas", anak: [] },
            ],
        },
        { nama: "Tentang", anak: [] },
    ],
};

function cetakMenu(simpul, tingkat = 0) {
    console.log("  ".repeat(tingkat) + simpul.nama);
    for (const anak of simpul.anak) {
        cetakMenu(anak, tingkat + 1);    // fungsi yang sama, satu tingkat lebih dalam
    }
}
cetakMenu(menu);
// Root
//   Produk
//     Sepatu
//     Tas
//   Tentang

// Kasus nyata 2: menyalin object sampai ke dalam-dalamnya (deep copy).
function salinDalam(nilai) {
    if (nilai === null || typeof nilai !== "object") return nilai;   // base case
    if (Array.isArray(nilai)) return nilai.map((x) => salinDalam(x));
    const hasil = {};
    for (const kunci of Object.keys(nilai)) {
        hasil[kunci] = salinDalam(nilai[kunci]);   // isinya bisa object lagi
    }
    return hasil;
}
const asli = { nama: "Andi", alamat: { kota: "Bandung" } };
const salinan = salinDalam(asli);
salinan.alamat.kota = "Medan";
console.log(asli.alamat.kota, salinan.alamat.kota);   // Bandung Medan

// Lupa base case: tumpukan pemanggilan penuh, lalu meledak.
function tanpaBaseCase(n) {
    return tanpaBaseCase(n - 1);         // tidak ada satu pun yang menghentikannya
}
try {
    tanpaBaseCase(5);
} catch (galat) {
    console.log(galat.name + ": " + galat.message);
    // RangeError: Maximum call stack size exceeded
}""",
            },
            {
                "heading": "Currying: fungsi yang mengembalikan fungsi",
                "body": [
                    "Currying = memecah fungsi ber-banyak-argumen jadi rantai fungsi yang",
                    "masing-masing menerima SATU argumen.",
                    "",
                    "  const tambah = (a, b) => a + b;      dipanggil:  tambah(2, 3)",
                    "  const tambah = a => b => a + b;      dipanggil:  tambah(2)(3)",
                    "",
                    "Cara membaca dua panah beruntun: yang dikembalikan panah pertama BUKAN",
                    "angka, melainkan FUNGSI baru yang masih mengingat nilai a - closure lagi.",
                    "Kalau bingung, bacalah dengan kurung khayalan: a => (b => a + b).",
                    "Dua pasang kurung saat memanggil, tambah(2)(3), artinya kamu memanggil",
                    "dua fungsi: hasil dari yang pertama langsung dipanggil oleh yang kedua.",
                    "",
                    "Gunanya bukan gaya-gayaan, namanya partial application: kunci argumen",
                    "yang itu-itu saja sekali di depan, lalu pakai fungsi hasilnya berkali-",
                    "kali. Karena sisanya tinggal satu argumen, ia langsung pas dipasang ke",
                    ".map(), ke event handler, atau ke daftar middleware.",
                    "",
                    "Bentuk inilah yang bikin kaget saat pertama kali membuka kode Express",
                    "atau Redux:",
                    "",
                    "  store => next => action => { ... }         (middleware Redux)",
                    "  (opsi) => (req, res, next) => { ... }      (middleware Express)",
                    "",
                    "Itu bukan sintaks khusus library; itu cuma tiga fungsi bersarang biasa.",
                    "Framework memanggil lapisan LUARNYA sekali saat setup - untuk menyimpan",
                    "konfigurasi ke dalam closure - lalu memanggil lapisan paling DALAM tiap",
                    "kali ada request atau action masuk.",
                ],
                "code": """// Fungsi biasa: semua argumen sekaligus.
const tambahBiasa = (a, b) => a + b;
console.log(tambahBiasa(2, 3));            // 5

// Versi curry: satu argumen per panggilan, tiap panah mengembalikan FUNGSI baru.
const tambah = (a) => (b) => a + b;
console.log(tambah(2)(3));                 // 5  <- perhatikan DUA pasang kurung

// Gunanya: partial application - kunci argumen pertama, pakai berkali-kali.
const tambah10 = tambah(10);               // ini FUNGSI, bukan angka: (b) => 10 + b
console.log(tambah10(5), tambah10(90));    // 15 100
console.log([1, 2, 3].map(tambah10));      // [ 11, 12, 13 ]

// Tiga tingkat: pola yang persis dipakai logger dan middleware.
const buatLog = (tingkat) => (modul) => (pesan) => `[${tingkat}] ${modul}: ${pesan}`;
const logError = buatLog("ERROR");         // tingkat terkunci di closure
const logErrorDb = logError("database");   // modul ikut terkunci
console.log(logErrorDb("koneksi putus"));  // [ERROR] database: koneksi putus

// Bentuk yang sama persis di middleware Redux: store => next => action => {...}
const pencatat = (store) => (next) => (action) => {
    console.log("sebelum:", action.type, "| state:", store.getState());
    const hasil = next(action);            // teruskan ke lapisan berikutnya
    console.log("sesudah:", action.type);
    return hasil;
};

const store = { getState: () => ({ jumlah: 0 }) };
const berikutnya = (action) => "ditangani " + action.type;
const siapPakai = pencatat(store)(berikutnya);   // dipanggil SEKALI saat setup
console.log(siapPakai({ type: "TAMBAH" }));      // dipanggil tiap ada action masuk""",
            },
        ],
    },
    {
        "title": "17. Iterator & Generator",
        "sections": [
            {
                "body": [
                    "Kenapa for...of jalan di array, string, Map, dan Set, tapi ERROR",
                    "di object biasa? Jawabannya: for...of sama sekali tidak tahu apa",
                    "itu array. Yang ia cari cuma SATU hal - apakah objek itu punya",
                    "method bernama Symbol.iterator. Kalau ada, dipakai. Kalau tidak",
                    "ada, JavaScript berhenti: TypeError: mahasiswa is not iterable.",
                    "",
                    "Kesepakatan itu namanya PROTOKOL ITERABLE. Dua istilahnya sering",
                    "tertukar:",
                    "",
                    "  iterable -> objek yang PUNYA method [Symbol.iterator]().",
                    "              Bawaan JS: Array, String, Map, Set, NodeList.",
                    "  iterator -> objek HASIL panggilan method itu; punya .next().",
                    "              Tiap .next() memberi { value: ..., done: true/false }.",
                    "",
                    "Symbol.iterator sendiri bukan string 'iterator', melainkan sebuah",
                    "Symbol: nilai unik bawaan JavaScript yang dipakai sebagai NAMA",
                    "property. Dipilih Symbol supaya tidak akan pernah bentrok dengan",
                    "key biasa milikmu yang kebetulan juga bernama 'iterator'.",
                    "",
                    "Tiga sintaks berikut memakai protokol yang SAMA. Jadi kalau satu",
                    "jalan, ketiganya jalan; kalau satu error, ketiganya error:",
                    "",
                    "  for (const x of data) { ... }   // materi Perulangan",
                    "  const salinan = [...data];      // spread",
                    "  const [a, b] = data;            // destructuring array",
                    "",
                    "Object literal sengaja DIBIARKAN tidak iterable. JavaScript tidak",
                    "mau menebak apakah yang ingin kamu jalani itu key-nya, value-nya,",
                    "atau pasangannya - kamu yang harus memilih, lewat Object.keys /",
                    "Object.values / Object.entries (materi Object & Destructuring).",
                ],
            },
            {
                "heading": "Membongkar for...of: memanggil .next() dengan tangan sendiri",
                "code": """const buah = ["apel", "jeruk", "mangga"];

// Inilah yang dikerjakan for...of di balik layar:
const it = buah[Symbol.iterator]();      // minta objek iterator ke array
console.log(it.next());                  // { value: 'apel', done: false }
console.log(it.next());                  // { value: 'jeruk', done: false }
console.log(it.next());                  // { value: 'mangga', done: false }
console.log(it.next());                  // { value: undefined, done: true }

// Versi manual yang persis setara dengan: for (const b of buah)
const it2 = buah[Symbol.iterator]();
let langkah = it2.next();
while (!langkah.done) {                  // 'done' yang menghentikan loop
    console.log(langkah.value);
    langkah = it2.next();
}

// Object literal tak punya method itu, jadi for...of menolak mentah-mentah
const mahasiswa = { nama: "Andi", umur: 20 };
console.log(typeof buah[Symbol.iterator]);        // function
console.log(typeof mahasiswa[Symbol.iterator]);   // undefined

try {
    for (const x of mahasiswa) console.log(x);
} catch (e) {
    console.log(e.name + ": " + e.message);
    // TypeError: mahasiswa is not iterable
}

// Solusinya bukan memaksa for...of, tapi jadikan array pasangan dulu
for (const [key, value] of Object.entries(mahasiswa)) {
    console.log(key, "->", value);
}""",
            },
            {
                "heading": "Memasang Symbol.iterator sendiri supaya objekmu bisa di-for...of",
                "code": """class Kelas {
    constructor(nama) {
        this.nama = nama;
        this.siswa = [];
    }

    tambah(orang) {
        this.siswa.push(orang);
        return this;
    }

    // Nama method-nya bukan string biasa melainkan Symbol.iterator, jadi
    // ditulis di dalam kurung siku. Ini SATU-SATUNYA syarat agar for...of mau.
    [Symbol.iterator]() {
        const daftar = this.siswa;
        let i = 0;                   // 'i' hidup lewat closure (materi Scope & Closure)
        return {
            next() {
                if (i < daftar.length) {
                    return { value: daftar[i++], done: false };
                }
                return { value: undefined, done: true };
            },
        };
    }
}

const kelas = new Kelas("TI-1");
kelas.tambah("Andi").tambah("Budi").tambah("Citra");

for (const s of kelas) console.log(s);       // Andi / Budi / Citra
console.log([...kelas]);                     // [ 'Andi', 'Budi', 'Citra' ]
const [ketua, wakil] = kelas;                // destructuring ikut jalan sendiri
console.log(ketua, wakil);                   // Andi Budi
console.log(Array.from(kelas).length);       // 3""",
            },
            {
                "heading": "function* dan yield: fungsi yang bisa DIJEDA lalu dilanjutkan",
                "body": [
                    "Menulis objek { next() { ... } } seperti di atas melelahkan dan",
                    "mudah salah: kamu sendiri yang mengurus penghitung, batas, dan",
                    "kapan done jadi true. Generator adalah cara singkat menulis hal",
                    "yang sama - JavaScript yang membuatkan iterator-nya untukmu.",
                    "",
                    "  function* nama() { ... }   <- tanda BINTANG setelah kata",
                    "                                function. Itu saja bedanya.",
                    "  yield nilai;               <- kirim satu nilai keluar, lalu",
                    "                                TIDUR di baris ini.",
                    "",
                    "Fungsi biasa sekali dipanggil harus lari sampai selesai. Generator",
                    "tidak: tiap yield membekukan fungsi lengkap dengan seluruh variabel",
                    "lokalnya, dan .next() berikutnya membangunkannya persis dari baris",
                    "itu. Perhatikan urutan cetakan di contoh - badan generator baru",
                    "mulai berjalan saat .next() PERTAMA, bukan saat fungsinya dipanggil.",
                ],
                "code": """// Tanda * setelah kata function = fungsi ini boleh dijeda di tengah jalan.
function* hitungMundur(dari) {
    console.log("   (badan generator mulai berjalan)");
    while (dari > 0) {
        yield dari;              // JEDA di sini, kirim 'dari' ke pemanggil
        dari--;                  // baru dikerjakan saat next() berikutnya
    }
    console.log("   (badan generator selesai)");
}

const g = hitungMundur(3);       // BELUM menjalankan apa pun, baru menyiapkan
console.log("sudah dipanggil, tapi badan generator masih diam");
console.log(g.next());   // (mulai berjalan) lalu { value: 3, done: false }
console.log(g.next());   // { value: 2, done: false }
console.log(g.next());   // { value: 1, done: false }
console.log(g.next());   // (selesai) lalu { value: undefined, done: true }

// Generator OTOMATIS iterable - tak perlu menulis Symbol.iterator lagi
function* tigaWarna() {
    yield "merah";
    yield "hijau";
    yield "biru";
}
for (const w of tigaWarna()) process.stdout.write(w + " ");
console.log();                                    // merah hijau biru
console.log([...tigaWarna()]);                    // [ 'merah', 'hijau', 'biru' ]
console.log(Array.from(tigaWarna(), (w) => w.toUpperCase()));

// Tak berhingga TAPI aman: nilai dihitung hanya saat diminta (lazy/malas)
function* pembuatId() {
    let id = 1;
    while (true) yield id++;     // while(true) yang TIDAK menggantung
}
const idNota = pembuatId();
console.log(idNota.next().value, idNota.next().value, idNota.next().value);
// 1 2 3

// yield* = serahkan giliran ke iterable lain sampai habis, baru lanjut
function* daftarLengkap() {
    yield* tigaWarna();          // semua nilai dari generator lain
    yield* ["hitam", "putih"];   // array juga iterable, jadi boleh
    yield "selesai";
}
console.log([...daftarLengkap()]);""",
            },
            {
                "body": [
                    "Jebakan yang benar-benar menjebak:",
                    "",
                    "  1. Generator SEKALI PAKAI. Setelah done: true, ia habis selamanya.",
                    "       const g = tigaWarna();",
                    "       console.log([...g]);   // [ 'merah', 'hijau', 'biru' ]",
                    "       console.log([...g]);   // []  <- bukan bug, memang habis",
                    "     Mau mengulang? Panggil fungsinya lagi: [...tigaWarna()].",
                    "     Generator itu satu 'kunjungan', bukan wadah data - beda dari",
                    "     array yang isinya menetap dan bisa dibaca berkali-kali.",
                    "",
                    "  2. Menyebar generator TAK BERHINGGA = program menggantung.",
                    "     [...pembuatId()] meminta nilai terus sampai memori habis. Yang",
                    "     aman: ambil sejumlah tertentu lewat .next(), atau for...of yang",
                    "     dihentikan break.",
                    "",
                    "  3. Lupa meminta. Baris hitungMundur(3); sendirian tidak mencetak",
                    "     apa-apa dan tidak error juga - orang menyangka kodenya rusak,",
                    "     padahal generator memang menunggu diminta. Harus ada .next(),",
                    "     for...of, spread, atau Array.from.",
                    "",
                    "  4. return di dalam generator BUKAN nilai terakhir yang kamu dapat.",
                    "     Ia muncul sebagai { value: ..., done: true } di .next(), tapi",
                    "     for...of dan spread membuang nilai yang datang bersama",
                    "     done: true. Untuk nilai yang ingin dibaca, pakai yield.",
                    "",
                    "  5. Bintangnya menempel ke function, bukan ke nama: function* f()",
                    "     sama saja dengan function *f(). Untuk method di dalam class",
                    "     atau object, ditulis  *namaMethod() { ... }.",
                    "",
                    "Di mana generator muncul di kode nyata:",
                    "  - redux-saga (dunia React): tiap alur efek samping ditulis",
                    "    function* dengan yield call(...) / yield put(...). Itulah sebab",
                    "    kode saga kelihatan asing kalau belum kenal generator.",
                    "  - Pembuat id / nomor urut yang tak boleh kembar, seperti pembuatId.",
                    "  - Membaca data BESAR sepotong demi sepotong: baris demi baris berkas",
                    "    log, atau hasil query jutaan baris, tanpa menaruh semuanya di",
                    "    memori sekaligus.",
                    "  - Versi async-nya, async function* dipasangkan dengan",
                    "    for await (const x of ...), dipakai membaca stream jaringan",
                    "    (nyambung ke materi async/await).",
                ],
            },
        ],
    },
    {
        "title": "18. Keyword 'this' & Context",
        "sections": [
            {
                "body": [
                    "'this' merujuk ke 'objek pemilik' dari kode yang sedang berjalan -",
                    "TAPI nilainya BERGANTUNG pada BAGAIMANA fungsi dipanggil, bukan",
                    "di mana fungsi didefinisikan. Ini yang sering membingungkan pemula.",
                    "",
                    "Aturan umum nilai 'this':",
                    "  1. Dipanggil sebagai method objek -> this = objek itu.",
                    "  2. Dipanggil sebagai fungsi biasa -> this = undefined (strict",
                    "     mode) atau objek global (non-strict, HINDARI).",
                    "  3. Di dalam arrow function -> this = mewarisi dari scope luar",
                    "     (TIDAK punya this sendiri).",
                    "  4. Dipanggil dengan new -> this = objek baru yang dibuat.",
                ]
            },
            {
                "heading": "Contoh perilaku 'this' yang berbeda",
                "code": """const mahasiswa = {
    nama: "Andi",
    sapaBiasa: function () {
        console.log(`Halo, saya ${this.nama}`);   // this = mahasiswa
    },
    sapaArrow: () => {
        console.log(`Halo, saya ${this.nama}`);   // this = scope luar (bukan mahasiswa!)
    },
};

mahasiswa.sapaBiasa();   // Halo, saya Andi
mahasiswa.sapaArrow();   // Halo, saya undefined  (BUG umum!)

// Masalah klasik: kehilangan konteks 'this'
const sapa = mahasiswa.sapaBiasa;
// sapa();   // ERROR/undefined - 'this' hilang karena dipanggil tanpa objek

// Solusi 1: bind()
const sapaTerikat = mahasiswa.sapaBiasa.bind(mahasiswa);
sapaTerikat();    // Halo, saya Andi (this terikat permanen)

// Solusi 2: pakai arrow function untuk callback (mewarisi this dg benar)
class Timer {
    constructor() {
        this.detik = 0;
    }
    mulai() {
        setInterval(() => {
            this.detik++;             // arrow function: this = instance Timer
            console.log(this.detik);
        }, 1000);
    }
}"""
            },
            {
                "body": [
                    "Catatan untuk contoh Timer di atas: ia memakai 'class' (materi 'OOP:",
                    "Class & Object') dan setInterval (materi 'Asynchronous JavaScript:",
                    "Callback') - dua hal yang baru dibahas nanti. Yang perlu dilihat",
                    "sekarang cuma satu: arrow function di dalam setInterval membuat 'this'",
                    "tetap menunjuk objek Timer-nya.",
                    "",
                    "call(), apply(), bind() - mengatur 'this' secara eksplisit:",
                    "  fungsi.call(objekThis, arg1, arg2)   -> panggil langsung dengan this tertentu",
                    "  fungsi.apply(objekThis, [arg1, arg2]) -> sama, tapi argumen dalam array",
                    "  fungsi.bind(objekThis)                -> mengembalikan fungsi BARU",
                    "                                            dengan this yang sudah terikat",
                    "",
                    "Rule of thumb praktis:",
                    "  - Method di dalam object/class -> pakai function biasa (perlu this).",
                    "  - Callback (setTimeout, event handler, array method) -> pakai",
                    "    arrow function agar 'this' tetap mengacu ke konteks luar yang benar.",
                ]
            },
            {
                "heading": "Apa yang berubah di strict mode",
                "body": [
                    "Aturan nomor 2 di atas menyebut 'strict mode' sambil lalu, padahal",
                    "seluruh perilaku 'this' bertumpu padanya. Ini definisinya.",
                    "",
                    "Strict mode = sekumpulan aturan yang lebih ketat, dinyalakan dengan",
                    "menulis satu baris berisi teks \"use strict\"; di paling atas sebuah",
                    "BERKAS (berlaku untuk seluruh berkas) atau di paling atas sebuah FUNGSI",
                    "(berlaku untuk fungsi itu saja). Harus benar-benar baris pertama;",
                    "ditaruh di tengah, ia cuma jadi string yang tidak berguna.",
                    "",
                    "Yang berubah, tiga yang paling terasa:",
                    "  1. this = undefined di fungsi biasa yang dipanggil tanpa objek.",
                    "     Tanpa strict, this diam-diam jadi objek global - dan bug 'kok",
                    "     nilainya nyasar ke mana-mana' lahir dari situ.",
                    "  2. Menugaskan ke variabel yang tidak pernah dideklarasikan jadi",
                    "     ReferenceError. Tanpa strict, salah ketik nama variabel akan",
                    "     MEMBUAT variabel global baru tanpa memberi tahu siapa pun.",
                    "  3. Perubahan yang dulu gagal diam-diam sekarang melempar error,",
                    "     misalnya menulis ke object yang sudah di-Object.freeze().",
                    "",
                    "Itu sebabnya berkas Node lama sering dibuka baris \"use strict\";, dan",
                    "kenapa kode di dalam IIFE sering diawali baris yang sama.",
                    "",
                    "Kabar baiknya: kamu semakin jarang perlu menulisnya. ES Module (berkas",
                    "dengan import/export) dan SELURUH isi class SELALU strict mode, tanpa",
                    "bisa dimatikan dan tanpa perlu ditulis.",
                ],
                "code": """"use strict";   // WAJIB baris paling atas berkas (atau paling atas sebuah fungsi)

// 1. Menugaskan ke variabel yang tidak pernah dideklarasikan jadi ERROR.
//    Tanpa strict, salah ketik nama diam-diam membuat variabel global baru.
try {
    jumlahh = 10;
} catch (e) {
    console.log(e.constructor.name + ":", e.message);
    // ReferenceError: jumlahh is not defined
}

// 2. Di fungsi BIASA yang dipanggil tanpa objek pemilik, this = undefined.
function siapaAku() {
    return this;
}
console.log(siapaAku());   // undefined   (tanpa strict: objek global)

// 3. Perubahan yang dulu gagal DIAM-DIAM sekarang melempar error.
const setelan = Object.freeze({ tema: "gelap" });
try {
    setelan.tema = "terang";
} catch (e) {
    console.log(e.constructor.name);   // TypeError
}"""
            },
        ],
    },
    {
        "title": "19. OOP: Class & Object (ES6+)",
        "sections": [
            {
                "body": [
                    "ES6 (2015) memperkenalkan syntax 'class' yang lebih mirip",
                    "Java/Python, walau di baliknya JS tetap pakai prototype",
                    "(dibahas di materi selanjutnya).",
                    "",
                    "  class NamaClass {",
                    "      constructor(param) {",
                    "          this.atribut = param;",
                    "      }",
                    "      method() {",
                    "          console.log(this.atribut);",
                    "      }",
                    "  }",
                ]
            },
            {
                "heading": "Contoh class, constructor, dan inheritance",
                "code": """class Hewan {
    constructor(nama) {
        this.nama = nama;
    }

    bersuara() {
        console.log(`${this.nama} bersuara.`);
    }
}

class Kucing extends Hewan {
    bersuara() {                      // override method induk
        console.log(`${this.nama}: Meong!`);
    }
}

class Anjing extends Hewan {
    constructor(nama, ras) {
        super(nama);                  // panggil constructor induk
        this.ras = ras;
    }
    bersuara() {
        console.log(`${this.nama} (${this.ras}): Guk!`);
    }
}

const daftarHewan = [new Kucing("Tom"), new Anjing("Bobby", "Herder")];
daftarHewan.forEach(h => h.bersuara());
// Tom: Meong!
// Bobby (Herder): Guk!"""
            },
            {
                "heading": "Getter/Setter, static method, dan private field",
                "code": """class Rekening {
    #saldo;                     // private field (ES2022+, diawali #)

    constructor(pemilik, saldoAwal) {
        this.pemilik = pemilik;
        this.#saldo = saldoAwal;
    }

    get saldo() {                // getter: diakses seperti atribut biasa
        return this.#saldo;
    }

    set saldo(nilai) {           // setter: dengan validasi
        if (nilai < 0) throw new Error("Saldo tidak boleh negatif!");
        this.#saldo = nilai;
    }

    setor(jumlah) {
        this.#saldo += jumlah;
    }

    static bandingkan(r1, r2) {  // static method: dipanggil lewat class, bukan objek
        return r1.saldo - r2.saldo;
    }
}

const r = new Rekening("Andi", 100000);
console.log(r.saldo);      // 100000 (getter, tanpa kurung)
r.setor(50000);
console.log(r.saldo);      // 150000
// console.log(r.#saldo);  // SyntaxError! private field tak bisa diakses dari luar"""
            },
            {
                "heading": "Class field publik, static field, dan arrow property",
                "body": [
                    "(throw new Error di setter di atas melempar error dengan sengaja;",
                    "cara menangkapnya dibahas di materi 'Exception Handling'.)",
                    "",
                    "Badan class masih menyimpan beberapa bentuk yang lebih sering muncul",
                    "daripada #privateField, tapi mustahil ditebak kalau yang diajarkan cuma",
                    "constructor dan method:",
                    "",
                    "  1. CLASS FIELD publik: hitung = 0; atau items = []; ditulis langsung",
                    "     di badan class, tanpa kata kunci apa pun. Tiap objek baru otomatis",
                    "     mendapatkannya, jadi constructor tidak perlu mengulanginya.",
                    "     Hati-hati satu hal: items = [] memberi array BARU untuk tiap objek",
                    "     - persis yang kita mau, dan bukan satu array yang dipakai bersama.",
                    "",
                    "  2. STATIC FIELD: static jumlah = 0; milik CLASS-nya sendiri, bukan",
                    "     milik tiap objek. Dibaca lewat nama class: Keranjang.jumlah.",
                    "",
                    "  3. Arrow function sebagai class property: handleKlik = () => {...};",
                    "     Karena arrow mewarisi 'this' dari tempat ia dibuat, method bentuk",
                    "     ini tetap benar walau dilepas dari objeknya dan diserahkan ke",
                    "     tombol, timer, atau event listener. Inilah cara baku mengikat",
                    "     'this' di komponen - alternatif dari bind() di constructor.",
                ],
                "code": """class Keranjang {
    items = [];                    // class field publik: tiap objek dapat array sendiri
    diskon = 0;

    static jumlahDibuat = 0;       // static field: milik CLASS-nya, bukan tiap objek

    constructor(pemilik) {
        this.pemilik = pemilik;
        Keranjang.jumlahDibuat++;  // dibaca lewat NAMA CLASS, bukan this
    }

    tambah(nama, harga) {
        this.items.push({ nama, harga });
        return this;
    }

    total() {
        return this.items.reduce((j, b) => j + b.harga, 0);
    }
}

const k = new Keranjang("Andi");
k.tambah("Pensil", 5000).tambah("Buku", 20000);
console.log(k.items.length, k.total());   // 2 25000
console.log(Keranjang.jumlahDibuat);      // 1

// Arrow function sebagai class property: 'this' terikat ke objeknya SELAMANYA.
class Tombol {
    label = "Simpan";
    klasik() { console.log("klasik:", this.label); }
    handleKlik = () => { console.log("arrow :", this.label); };
}

const t = new Tombol();
const lepasArrow = t.handleKlik;   // dilepas dari objeknya, seperti saat diserahkan
const lepasKlasik = t.klasik;      // ke addEventListener atau setTimeout
lepasArrow();                      // arrow : Simpan   <- tetap benar
try {
    lepasKlasik();                 // this hilang: isi class SELALU strict mode
} catch (e) {
    console.log(e.constructor.name + ":", e.message);
    // TypeError: Cannot read properties of undefined (reading 'label')
}"""
            },
            {
                "heading": "super.namaMethod(): override yang memperluas",
                "body": [
                    "Terakhir: super(nama) di contoh Anjing tadi memanggil CONSTRUCTOR induk.",
                    "Tapi super punya bentuk kedua yang justru lebih sering dipakai -",
                    "super.namaMethod(), yang memanggil versi INDUK dari method yang sedang",
                    "kamu timpa.",
                    "",
                    "Bedanya besar. Override tanpa super.method() MENGGANTI perilaku induk",
                    "seluruhnya (itu yang dilakukan Kucing dan Anjing di contoh sebelumnya).",
                    "Override dengan super.method() MEMPERLUAS: kerjakan dulu yang dikerjakan",
                    "induk, baru tambahkan bagianmu. Pola ini ada di mana-mana pada kode yang",
                    "memakai class - misalnya method yang perlu memanggil versi dasarnya dulu",
                    "sebelum menambahkan langkah khusus.",
                ],
                "code": """class Hewan {
    constructor(nama) { this.nama = nama; }
    deskripsi() { return `${this.nama} adalah seekor hewan`; }
}

class Kucing extends Hewan {
    constructor(nama, warna) {
        super(nama);              // super(...) memanggil CONSTRUCTOR induk
        this.warna = warna;
    }
    deskripsi() {
        // super.deskripsi() memanggil versi INDUK dari method yang sedang
        // ditimpa: kerjakan dulu bagian induk, baru tambahkan bagian sendiri.
        return super.deskripsi() + `, tepatnya kucing ${this.warna}`;
    }
}

console.log(new Kucing("Tom", "abu-abu").deskripsi());
// Tom adalah seekor hewan, tepatnya kucing abu-abu"""
            },
        ],
    },
    {
        "title": "20. Prototype: OOP di Balik Layar JavaScript",
        "sections": [
            {
                "body": [
                    "Sebelum ada 'class' (ES6), JavaScript sudah punya OOP lewat",
                    "PROTOTYPE - dan 'class' sebenarnya hanya 'syntactic sugar'",
                    "(pembungkus lebih rapi) di atas mekanisme prototype ini.",
                    "",
                    "Setiap objek JS punya properti tersembunyi __proto__ yang",
                    "menunjuk ke objek LAIN (prototype-nya). Jika suatu property/method",
                    "tidak ditemukan di objek itu sendiri, JS mencarinya di prototype",
                    "-nya, lalu ke prototype dari prototype-nya (disebut 'prototype chain').",
                ]
            },
            {
                "heading": "Contoh prototype (cara lama sebelum class)",
                "code": """function Hewan(nama) {
    this.nama = nama;
}

// Menambah method lewat prototype (dibagi SEMUA instance, hemat memori)
Hewan.prototype.bersuara = function () {
    console.log(`${this.nama} bersuara.`);
};

const kucing = new Hewan("Tom");
kucing.bersuara();    // Tom bersuara.

console.log(kucing.__proto__ === Hewan.prototype);   // true

// Ini setara PERSIS dengan:
class HewanClass {
    constructor(nama) {
        this.nama = nama;
    }
    bersuara() {                 // method class OTOMATIS taruh di prototype
        console.log(`${this.nama} bersuara.`);
    }
}"""
            },
            {
                "body": [
                    "Kenapa method ditaruh di prototype (bukan di dalam constructor)?",
                    "  - HEMAT MEMORI: satu method dibagi oleh SEMUA instance,",
                    "    tidak perlu disalin ulang tiap kali objek baru dibuat.",
                    "  - Ini alasan class method OTOMATIS memakai mekanisme ini.",
                    "",
                    "Object.create() - membuat objek dengan prototype tertentu",
                    "secara langsung tanpa function constructor:",
                    "  const hewanProto = { bersuara() { console.log('...'); } };",
                    "  const kucing = Object.create(hewanProto);",
                    "",
                    "Kamu TIDAK WAJIB menulis kode prototype manual di JS modern -",
                    "cukup pakai 'class' - tapi paham konsepnya PENTING untuk",
                    "mengerti error/perilaku aneh dan membaca kode JS yang lebih lama.",
                ]
            },
        ],
    },
    {
        "title": "21. Exception Handling",
        "sections": [
            {
                "body": [
                    "Error di JavaScript bisa ditangani dengan try-catch-finally,",
                    "mirip bahasa lain.",
                    "",
                    "  try {",
                    "      // kode yang mungkin error",
                    "  } catch (error) {",
                    "      // penanganan error",
                    "  } finally {",
                    "      // selalu jalan, error atau tidak",
                    "  }",
                    "",
                    "Error bawaan yang umum:",
                    "  TypeError       -> memanggil method pada nilai yang salah tipe",
                    "  ReferenceError  -> memakai variabel yang belum dideklarasikan",
                    "  RangeError      -> nilai di luar rentang valid",
                    "  SyntaxError     -> kesalahan sintaks (biasanya saat parsing)",
                ]
            },
            {
                "heading": "Contoh try-catch & custom Error",
                "code": """function bagi(a, b) {
    if (b === 0) {
        throw new Error("Tidak bisa membagi dengan nol!");
    }
    return a / b;
}

try {
    console.log(bagi(10, 2));   // 5
    console.log(bagi(10, 0));   // akan melempar error
} catch (error) {
    console.log("Terjadi error:", error.message);
} finally {
    console.log("Selesai mencoba pembagian.");
}

// Membuat custom Error class (turunan dari Error)
class SaldoTidakCukup extends Error {
    constructor(pesan) {
        super(pesan);
        this.name = "SaldoTidakCukup";
    }
}

function tarik(saldo, jumlah) {
    if (jumlah > saldo) {
        throw new SaldoTidakCukup(`Saldo ${saldo} tidak cukup untuk menarik ${jumlah}`);
    }
    return saldo - jumlah;
}

try {
    tarik(50000, 100000);
} catch (e) {
    if (e instanceof SaldoTidakCukup) {
        console.log("Error khusus:", e.message);
    } else {
        throw e;   // lempar ulang jika bukan error yang kita duga
    }
}"""
            },
            {
                "heading": "instanceof vs typeof",
                "body": [
                    "Contoh di atas bertumpu pada satu operator yang belum pernah dijelaskan:",
                    "instanceof. Ia bersaudara dengan typeof yang kamu pelajari di materi",
                    "Variabel, tapi menjawab pertanyaan yang berbeda.",
                    "",
                    "  typeof x       tipe DASAR x, hasilnya string: \"number\", \"string\", ...",
                    "  x instanceof C apakah x lahir dari class/constructor C? hasilnya boolean",
                    "",
                    "typeof buntu begitu berhadapan dengan object: array, Date, dan semua",
                    "jenis Error sama-sama menjawab \"object\". Untuk membedakan mereka",
                    "instanceof-lah alatnya - dan itu sebabnya ia muncul di dalam catch,",
                    "tempat kita perlu tahu error JENIS APA yang barusan tertangkap.",
                    "",
                    "Satu aturan menyertainya: karena turunan juga cocok dengan induknya",
                    "(TypeError instanceof Error itu true), urutan pemeriksaan harus dari",
                    "yang PALING KHUSUS ke yang paling umum. Terbalik, cabang khususnya",
                    "tidak akan pernah tercapai.",
                ],
                "code": """// typeof memeriksa TIPE DASAR dan hasilnya berupa string. Untuk semua object
// -- termasuk array, Date, dan Error -- jawabannya cuma "object".
console.log(typeof "teks", typeof 5, typeof {});    // string number object
console.log(typeof [], typeof new Error("x"));      // object object  <- tak menolong

// instanceof memeriksa GARIS KETURUNAN sebuah object, hasilnya boolean.
const e = new TypeError("salah tipe");
console.log(e instanceof TypeError);   // true
console.log(e instanceof Error);       // true   TypeError adalah turunan Error
console.log(e instanceof RangeError);  // false
console.log([] instanceof Array);      // true   pertanyaan yang typeof tak bisa jawab

// Urutan pemeriksaan: dari yang PALING KHUSUS ke yang paling umum.
class GagalValidasi extends Error {}
class GagalJaringan extends Error {}

function tangani(err) {
    if (err instanceof GagalValidasi) return "periksa isian";
    if (err instanceof GagalJaringan) return "coba lagi nanti";
    if (err instanceof Error) return "error tak terduga: " + err.message;
    return "yang dilempar bahkan bukan Error, melainkan " + typeof err;
}

console.log(tangani(new GagalValidasi("email kosong")));   // periksa isian
console.log(tangani(new RangeError("kebesaran")));         // error tak terduga: kebesaran
console.log(tangani("kehabisan stok"));                    // ... melainkan string"""
            },
            {
                "heading": "catch tanpa binding, error.stack, dan error.cause",
                "body": [
                    "Empat hal kecil yang melengkapi try-catch, dan satu yang besar.",
                    "",
                    "  catch tanpa binding: catch { ... } tanpa (e), boleh sejak ES2019",
                    "  kalau errornya memang tidak dipakai.",
                    "",
                    "  error.stack: jejak pemanggilan sampai titik error terjadi. Baris",
                    "  pertamanya nama dan pesan error, sisanya daftar fungsi yang sedang",
                    "  berjalan. Inilah yang kamu baca lebih dulu saat program gagal.",
                    "",
                    "  error.cause (ES2022): membungkus error asli tanpa menghilangkannya,",
                    "  lewat argumen kedua new Error(pesan, { cause: errorAsli }). Tanpa",
                    "  ini, membungkus error berarti membuang sebab aslinya.",
                    "",
                    "  throw menerima nilai APA SAJA - string, angka, object polos. Jangan.",
                    "  Yang bukan Error tidak punya .message dan tidak punya .stack, jadi",
                    "  jejaknya lenyap dan catch di hulu tidak bisa memeriksa jenisnya.",
                    "",
                    "Yang besar: try-catch biasa TIDAK menangkap error dari Promise. Kalau",
                    "sebuah Promise ditolak dan tidak ada .catch() atau await di dalam",
                    "try-catch yang menangkapnya, jadilah 'unhandled rejection'. Di browser",
                    "ia muncul sebagai peringatan merah di Console; di Node, program LANGSUNG",
                    "BERHENTI dengan kode keluar 1. Yang tercetak tergantung apa yang ditolak:",
                    "kalau sebuah Error, Node mencetak Error itu beserta stack-nya apa adanya;",
                    "kalau bukan Error, barulah muncul UnhandledPromiseRejection berikut",
                    "code: 'ERR_UNHANDLED_REJECTION'. Cara menghindarinya dibahas di materi",
                    "Promise dan async/await berikutnya - intinya: tiap rantai Promise wajib",
                    "berujung pada .catch(), atau tiap await wajib berada di dalam try-catch.",
                ],
                "code": """// catch boleh ditulis TANPA (e) kalau errornya memang tidak dipakai (ES2019).
try {
    JSON.parse("{bukan json}");
} catch {
    console.log("format tidak valid");
}

// error.stack: baris pertamanya nama dan pesan error.
const jejak = new Error("contoh").stack.split("\\n");
console.log(jejak[0]);   // Error: contoh

// error.cause: membungkus error asli TANPA menghilangkannya.
function bacaKonfigurasi() {
    try {
        JSON.parse("{rusak}");
    } catch (asli) {
        throw new Error("Konfigurasi gagal dibaca", { cause: asli });
    }
}
try {
    bacaKonfigurasi();
} catch (err) {
    console.log(err.message);                  // Konfigurasi gagal dibaca
    console.log(err.cause.constructor.name);   // SyntaxError  <- sebab asli utuh
}

// throw menerima nilai apa saja - tapi yang bukan Error kehilangan jejaknya.
try {
    throw "kehabisan stok";
} catch (err) {
    console.log(typeof err, err.message);      // string undefined
}"""
            },
        ],
    },
    {
        "title": "22. Asynchronous JavaScript: Callback",
        "sections": [
            {
                "body": [
                    "JavaScript bersifat SINGLE-THREADED (satu 'jalur' eksekusi),",
                    "tapi bisa menangani operasi yang LAMA (network request, timer,",
                    "baca file) TANPA memblokir program lewat model ASYNCHRONOUS.",
                    "",
                    "Callback = fungsi yang dikirim sebagai ARGUMEN ke fungsi lain,",
                    "untuk dijalankan NANTI setelah suatu proses selesai.",
                    "",
                    "  setTimeout(() => {",
                    "      console.log(\"Ini jalan setelah 2 detik\");",
                    "  }, 2000);",
                    "  console.log(\"Ini jalan DULUAN\");   // tidak menunggu setTimeout!",
                ]
            },
            {
                "heading": "Contoh callback & masalah 'Callback Hell'",
                "code": """function ambilData(id, callback) {
    setTimeout(() => {                     // simulasi request butuh waktu
        console.log(`Data ${id} diambil.`);
        callback(`Data-${id}`);
    }, 1000);
}

// Callback sederhana
ambilData(1, (hasil) => {
    console.log("Hasil:", hasil);
});

// "Callback Hell": callback bersarang berkali-kali, SULIT dibaca!
ambilData(1, (data1) => {
    ambilData(2, (data2) => {
        ambilData(3, (data3) => {
            console.log(data1, data2, data3);
            // semakin dalam bersarang = semakin sulit dirawat & di-debug
        });
    });
});
// Masalah inilah yang diselesaikan oleh Promise & async/await
// di dua materi berikutnya."""
            },
            {
                "body": [
                    "Event loop (konsep penting di balik async JS):",
                    "  1. Call stack menjalankan kode SINKRON satu per satu.",
                    "  2. Operasi async (setTimeout, fetch, dll) diserahkan ke",
                    "     Web API/Node API browser, TIDAK memblokir call stack.",
                    "  3. Setelah selesai, callback-nya masuk ke 'queue'.",
                    "  4. Event loop memindahkan callback dari queue ke call stack",
                    "     HANYA jika call stack sedang KOSONG.",
                    "  Inilah kenapa setTimeout(fn, 0) TETAP jalan SETELAH semua",
                    "  kode sinkron selesai, walau delay-nya 0 milidetik.",
                    "",
                    "Satu koreksi penting untuk poin 3: antreannya BUKAN satu, melainkan DUA.",
                    "",
                    "  Antrean MICROTASK  -> Promise.then/catch/finally, await, queueMicrotask",
                    "  Antrean MACROTASK  -> setTimeout, setInterval, event I/O, event DOM",
                    "",
                    "Aturannya: setiap kali call stack kosong, event loop MENGURAS HABIS",
                    "antrean microtask lebih dulu - termasuk microtask baru yang lahir di",
                    "tengah proses - baru mengambil SATU macrotask.",
                    "",
                    "Akibat yang langsung terasa: Promise.then selalu jalan LEBIH DULU",
                    "daripada setTimeout(fn, 0), walau setTimeout ditulis di baris atasnya.",
                    "Dengan model satu antrean, kesimpulanmu akan terbalik.",
                ]
            },
            {
                "heading": "Membatalkan timer: clearTimeout & clearInterval",
                "body": [
                    "setTimeout dan setInterval punya satu sifat yang belum disebut sama",
                    "sekali, padahal ia yang membuat keduanya bisa dikendalikan:",
                    "",
                    "  const id = setTimeout(fn, 1000);   -> setTimeout MENGEMBALIKAN id",
                    "  clearTimeout(id);                  -> batalkan sebelum waktunya tiba",
                    "",
                    "  const id2 = setInterval(fn, 1000); -> ulang TERUS tiap 1000 ms",
                    "  clearInterval(id2);                -> satu-satunya cara menghentikannya",
                    "",
                    "setInterval tidak pernah berhenti sendiri. Contoh class Timer di materi",
                    "'Keyword this' akan mencetak angka selamanya sampai programnya dimatikan,",
                    "karena tidak ada clearInterval di sana - id-nya bahkan tidak disimpan.",
                    "Biasakan: setiap setInterval harus punya syarat berhenti yang jelas.",
                    "",
                    "Pasangan simpan-id lalu batalkan inilah yang menjadi tumpuan pola",
                    "'debounce' - menunda sebuah tindakan sampai orangnya berhenti mengetik,",
                    "dengan cara membatalkan timer lama tiap kali ada ketikan baru. Kamu akan",
                    "membangunnya sendiri di Latihan 16.",
                ],
                "code": """// setTimeout MENGEMBALIKAN id timer. Simpan id-nya kalau ada kemungkinan
// jadwal itu perlu DIBATALKAN sebelum waktunya tiba.
const id = setTimeout(() => console.log("ini tidak akan pernah tampil"), 500);
clearTimeout(id);

// setInterval mengulang terus dan tidak pernah berhenti sendiri.
let detak = 0;
const idInterval = setInterval(() => {
    detak++;
    console.log("detak", detak);
    if (detak === 3) {
        clearInterval(idInterval);   // syarat berhenti WAJIB ada
        console.log("interval dihentikan");
    }
}, 50);
// Output: detak 1, detak 2, detak 3, interval dihentikan"""
            },
            {
                "heading": "Dua antrean: microtask selalu didahulukan",
                "code": """console.log("1. sinkron - dijalankan langsung");

setTimeout(() => console.log("5. macrotask: setTimeout 0"), 0);

Promise.resolve().then(() => console.log("3. microtask: Promise.then"));
queueMicrotask(() => console.log("4. microtask: queueMicrotask"));

console.log("2. sinkron - juga langsung");

// Urutan keluarannya persis 1, 2, 3, 4, 5 - walau setTimeout ditulis paling
// dulu dan delay-nya 0. Seluruh antrean microtask dikuras habis lebih dulu,
// baru satu macrotask diambil."""
            },
        ],
    },
    {
        "title": "23. Asynchronous JavaScript: Promise",
        "sections": [
            {
                "body": [
                    "Promise = objek yang MEWAKILI hasil dari operasi asynchronous",
                    "yang BELUM TENTU sudah selesai - bisa berakhir SUKSES (resolve)",
                    "atau GAGAL (reject). Solusi untuk masalah 'Callback Hell'.",
                    "",
                    "3 status Promise:",
                    "  pending    -> masih berjalan, belum selesai.",
                    "  fulfilled  -> berhasil, punya nilai hasil (resolve).",
                    "  rejected   -> gagal, punya alasan kegagalan (reject).",
                ]
            },
            {
                "heading": "Membuat & memakai Promise",
                "code": """function ambilData(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id > 0) {
                resolve(`Data-${id}`);        // berhasil
            } else {
                reject(new Error("ID tidak valid"));  // gagal
            }
        }, 1000);
    });
}

// .then() untuk sukses, .catch() untuk error, .finally() selalu jalan
ambilData(1)
    .then((hasil) => console.log("Sukses:", hasil))
    .catch((error) => console.log("Gagal:", error.message))
    .finally(() => console.log("Selesai."));

// Promise chaining: MENGGANTIKAN callback hell yang bersarang
ambilData(1)
    .then((data1) => {
        console.log(data1);
        return ambilData(2);          // return Promise BARU untuk chaining
    })
    .then((data2) => {
        console.log(data2);
        return ambilData(3);
    })
    .then((data3) => console.log(data3))
    .catch((error) => console.log("Ada yang gagal:", error.message));"""
            },
            {
                "heading": "Promise.all, Promise.race, Promise.allSettled",
                "code": """const p1 = ambilData(1);
const p2 = ambilData(2);
const p3 = ambilData(3);

// Promise.all: tunggu SEMUA selesai, gagal jika SALAH SATU gagal
Promise.all([p1, p2, p3])
    .then((hasil) => console.log("Semua selesai:", hasil))
    .catch((error) => console.log("Salah satu gagal:", error.message));

// Promise.allSettled: tunggu SEMUA selesai, TIDAK peduli sukses/gagal
Promise.allSettled([p1, p2, p3])
    .then((hasil) => console.log(hasil));
    // [{status:'fulfilled', value:...}, {status:'rejected', reason:...}, ...]

// Promise.race: ambil hasil PALING CEPAT selesai (sukses atau gagal)
Promise.race([p1, p2, p3])
    .then((hasil) => console.log("Tercepat:", hasil));"""
            },
        ],
    },
    {
        "title": "24. Asynchronous JavaScript: async/await",
        "sections": [
            {
                "body": [
                    "async/await (ES2017) = cara MENULIS kode asynchronous agar",
                    "TERLIHAT seperti kode sinkron biasa - jauh lebih mudah dibaca",
                    "daripada .then().then().then() berantai.",
                    "",
                    "Aturan dasar:",
                    "  1. Fungsi yang memakai 'await' HARUS ditandai 'async'.",
                    "  2. 'await' HANYA bisa dipakai di dalam fungsi async.",
                    "  3. 'await' 'menjeda' fungsi sampai Promise selesai,",
                    "     TANPA memblokir thread utama JavaScript.",
                    "  4. Fungsi async SELALU mengembalikan sebuah Promise.",
                ]
            },
            {
                "heading": "Mengubah Promise chain jadi async/await",
                "code": """function ambilData(id) {
    return new Promise((resolve) => {
        setTimeout(() => resolve(`Data-${id}`), 1000);
    });
}

// Versi Promise chain (dari materi sebelumnya):
// ambilData(1).then(d1 => { ... return ambilData(2); }).then(d2 => {...});

// Versi async/await - JAUH lebih mudah dibaca:
async function prosesSemuaData() {
    const data1 = await ambilData(1);
    console.log(data1);

    const data2 = await ambilData(2);
    console.log(data2);

    const data3 = await ambilData(3);
    console.log(data3);

    return "Semua selesai!";
}

prosesSemuaData().then((pesan) => console.log(pesan));

// Menangani error dengan try-catch (BUKAN .catch()!)
async function amanAmbilData(id) {
    try {
        const hasil = await ambilData(id);
        console.log("Berhasil:", hasil);
    } catch (error) {
        console.log("Gagal:", error.message);
    }
}"""
            },
            {
                "heading": "Menjalankan beberapa Promise PARALEL dengan async/await",
                "code": """async function ambilSemuaParalel() {
    // SALAH (lambat): berurutan, total waktu = jumlah semua delay
    // const d1 = await ambilData(1);
    // const d2 = await ambilData(2);   // BARU mulai setelah d1 selesai!

    // BENAR (cepat): mulai SEMUA duluan, baru tunggu bersamaan
    const [d1, d2, d3] = await Promise.all([
        ambilData(1),
        ambilData(2),
        ambilData(3),
    ]);
    console.log(d1, d2, d3);
    // Total waktu HANYA selama Promise TERLAMA, bukan dijumlah semua!
}

ambilSemuaParalel();"""
            },
            {
                "body": [
                    "Kapan pakai await berurutan vs Promise.all paralel:",
                    "  - Berurutan (await satu-satu): jika operasi kedua BUTUH",
                    "    hasil dari operasi pertama (saling bergantung).",
                    "  - Paralel (Promise.all): jika operasi-operasi TIDAK saling",
                    "    bergantung - jauh lebih cepat karena berjalan bersamaan.",
                    "",
                    "async/await adalah standar de-facto JavaScript modern -",
                    "hampir semua kode async production memakainya, bukan .then().",
                ]
            },
        ],
    },
    {
        "title": "25. DOM Manipulation & Event Dasar",
        "sections": [
            {
                "body": [
                    "DOM (Document Object Model) = representasi struktur halaman",
                    "HTML sebagai objek yang bisa diakses & diubah lewat JavaScript.",
                    "Ini yang membuat halaman web jadi INTERAKTIF.",
                    "",
                    "Catatan: materi ini HANYA berlaku di lingkungan BROWSER",
                    "(bukan Node.js, karena Node tidak punya HTML/DOM).",
                    "",
                    "Memilih elemen HTML:",
                    "  document.getElementById(\"id\")",
                    "  document.querySelector(\".class\")      -> elemen PERTAMA yang cocok",
                    "  document.querySelectorAll(\".class\")   -> SEMUA elemen yang cocok",
                ]
            },
            {
                "heading": "Contoh manipulasi DOM (jalankan di browser console)",
                "code": """// Mengubah isi teks & style elemen
const judul = document.querySelector("h1");
judul.textContent = "Judul Baru";
judul.style.color = "blue";

// Menambah/menghapus class CSS
judul.classList.add("aktif");
judul.classList.remove("nonaktif");
judul.classList.toggle("highlight");   // tambah jika belum ada, hapus jika sudah ada

// Membuat elemen baru & menambahkannya ke halaman
const liBaru = document.createElement("li");
liBaru.textContent = "Item baru";
document.querySelector("ul").appendChild(liBaru);

// Menghapus elemen
document.querySelector(".hapus-saya").remove();"""
            },
            {
                "heading": "Event handling (merespons interaksi user)",
                "code": """const tombol = document.querySelector("#tombolKlik");

// addEventListener: cara STANDAR menangani event (bisa banyak listener)
tombol.addEventListener("click", function () {
    console.log("Tombol diklik!");
});

// Dengan arrow function & event object
tombol.addEventListener("click", (event) => {
    console.log("Elemen yang diklik:", event.target);
});

// Event umum lainnya:
// 'input'   -> tiap kali nilai <input> berubah (real-time, tiap ketikan)
// 'change'  -> nilai berubah & elemen kehilangan fokus
// 'submit'  -> form dikirim
// 'keydown' -> tombol keyboard ditekan
// 'load'    -> halaman/gambar selesai dimuat

document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();    // mencegah reload halaman (perilaku default form)
    console.log("Form dikirim tanpa reload!");
});"""
            },
        ],
    },
    {
        "title": "26. Form, Atribut, dan Event Lanjutan",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya mengajarkan cara MENULIS ke halaman: textContent, style,",
                    "classList, createElement. Yang belum sama sekali: cara MEMBACA dari halaman.",
                    "Akibatnya rantainya putus tepat sebelum bagian yang berguna - kamu bisa tahu",
                    "sebuah form dikirim, tapi tidak tahu isinya apa.",
                    "",
                    "JEBAKAN NOMOR SATU: querySelector mengembalikan null.",
                    "  Browser membaca HTML dari atas ke bawah. <script> di dalam <head> dijalankan",
                    "  SEBELUM <body> dibaca, jadi elemen yang dicari memang belum ada. Yang muncul",
                    "  di console: \"Cannot read properties of null (reading 'addEventListener')\".",
                    "  Ini bukan salah selektormu; kodenya cuma kepagian.",
                    "",
                    "  Tiga cara benar - pilih SATU:",
                    "    1. <script defer src=\"app.js\"></script>  di dalam <head>   <- paling dianjurkan",
                    "    2. <script src=\"app.js\"></script>  tepat sebelum </body>",
                    "    3. document.addEventListener(\"DOMContentLoaded\", () => { ... });",
                    "",
                    "  defer hanya berlaku untuk <script src=...>; <script> yang isinya ditulis",
                    "  langsung di HTML mengabaikannya. DOMContentLoaded menyala saat seluruh HTML",
                    "  selesai dibaca. Jangan tertukar dengan event \"load\", yang masih menunggu",
                    "  semua gambar selesai - biasanya jauh terlalu lambat untuk memasang listener.",
                    "",
                    "Cara membaca tiap kontrol form:",
                    "  <input type=\"text\">      el.value     -> string",
                    "  <input type=\"number\">    el.value     -> TETAP string (\"12\", bukan 12)",
                    "  <textarea>               el.value     -> string (BUKAN textContent)",
                    "  <select>                 el.value     -> value dari <option> yang terpilih",
                    "  <input type=\"checkbox\">  el.checked   -> boolean; .value hampir tak berguna",
                    "  <input type=\"radio\">     cari dulu yang terpilih, baru baca .value:",
                    "      document.querySelector('input[name=\"jk\"]:checked')  -> null kalau belum dipilih",
                    "",
                    "el.value SELALU string, bahkan dari type=\"number\". Konversinya wajib manual",
                    "(lihat materi konversi tipe). Contoh berikutnya menunjukkan akibatnya kalau lupa.",
                    "",
                    "Kecuali satu contoh yang ditandai, seluruh kode di materi ini berjalan di BROWSER.",
                    "Kalau dijalankan dengan node, hasilnya \"ReferenceError: document is not defined\" -",
                    "node tidak punya halaman untuk dibaca. Cara memakainya: simpan sebagai app.js,",
                    "tautkan dengan <script defer src=\"app.js\">, lalu buka berkas HTML-nya di browser.",
                ],
            },
            {
                "heading": "Nilai form selalu string (contoh ini justru bisa dijalankan dengan node)",
                "code": """// Meniru nilai yang keluar dari sebuah form: semuanya bertipe string.
const harga = "15000";   // dari <input type="number">
const jumlah = "3";      // dari <input type="text">

console.log(typeof harga);        // "string" -- walaupun input-nya type="number"
console.log(harga + jumlah);      // 150003  <- DIGABUNG sebagai teks, bukan dijumlah
console.log(Number(harga) * Number(jumlah));   // 45000

// Konversi yang gagal tidak melempar error. Ia diam-diam menghasilkan NaN,
// dan NaN menular: semua hitungan sesudahnya ikut jadi NaN.
console.log(Number("12rb"));                 // NaN
console.log(Number("12rb") * 2);             // NaN
console.log(Number.isNaN(Number("12rb")));   // true  <- cara benar mengeceknya

// Beda parseInt dengan Number pada isian yang "hampir" angka:
console.log(parseInt("12rb", 10));   // 12   <- berhenti di huruf pertama
console.log(Number(""));             // 0    <- isian KOSONG jadi nol, ini berbahaya
console.log(parseInt("", 10));       // NaN

// Karena Number("") = 0, isian kosong bisa lolos sebagai "harga nol".
// Periksa kosongnya DULU, baru konversi.
const isian = "   ";
if (isian.trim() === "") {
    console.log("Harga wajib diisi");
} else {
    console.log("Harga:", Number(isian));
}

// Checkbox tidak punya nilai teks yang berguna; yang dibaca .checked (boolean).
const setuju = true;
console.log(setuju ? "setuju" : "belum setuju");""",
            },
            {
                "heading": "Membaca satu form utuh saat dikirim (browser)",
                "body": [
                    "HTML yang diasumsikan contoh di bawah - simpan sebagai index.html:",
                    "",
                    "  <form id=\"form-pesan\">",
                    "    <input type=\"text\" name=\"nama\" id=\"nama\">",
                    "    <input type=\"number\" name=\"jumlah\" id=\"jumlah\" value=\"1\">",
                    "    <select name=\"ukuran\" id=\"ukuran\">",
                    "      <option value=\"s\">Kecil</option>",
                    "      <option value=\"l\" selected>Besar</option>",
                    "    </select>",
                    "    <input type=\"checkbox\" name=\"pedas\" id=\"pedas\">",
                    "    <button type=\"submit\">Pesan</button>",
                    "  </form>",
                    "  <p id=\"pesan\"></p>",
                    "",
                    "ATRIBUT vs PROPERTI - beda yang bikin bingung saat debug:",
                    "  atribut  = apa yang TERTULIS di HTML.   dibaca: el.getAttribute(\"value\")",
                    "  properti = keadaan objeknya SEKARANG.   dibaca: el.value",
                    "  Begitu pengguna mengetik, el.value berubah tapi getAttribute(\"value\") tetap",
                    "  \"1\" selamanya. Nilai awal itu juga tersedia sebagai el.defaultValue, dan",
                    "  el.defaultChecked untuk checkbox. Itulah yang dikembalikan form.reset().",
                    "",
                    "Empat fungsi untuk atribut apa pun, termasuk yang tidak punya properti sendiri:",
                    "  el.getAttribute(\"href\")          baca; null kalau atributnya memang tidak ada",
                    "  el.setAttribute(\"disabled\", \"\")  pasang (atribut boolean cukup diisi string kosong)",
                    "  el.removeAttribute(\"disabled\")   copot",
                    "  el.hasAttribute(\"disabled\")      true/false",
                ],
                "code": """const form = document.querySelector("#form-pesan");
const kotakPesan = document.querySelector("#pesan");

form.addEventListener("submit", (e) => {
    e.preventDefault();   // tanpa ini halaman RELOAD dan semua isian hilang

    // form.elements.<name> mencari isian lewat atribut name-nya.
    // Sama saja dengan document.querySelector("#nama"), tapi tidak butuh id.
    const nama = form.elements.nama.value.trim();
    const jumlah = Number(form.elements.jumlah.value);
    const ukuran = form.elements.ukuran.value;     // "s" atau "l"
    const pedas = form.elements.pedas.checked;     // true / false

    if (nama === "") {
        kotakPesan.textContent = "Nama wajib diisi";
        return;                                    // hentikan, jangan lanjut
    }
    if (!Number.isInteger(jumlah) || jumlah < 1) {
        kotakPesan.textContent = "Jumlah harus angka bulat minimal 1";
        return;
    }

    kotakPesan.textContent =
        `${nama} pesan ${jumlah} porsi ukuran ${ukuran}` + (pedas ? " (pedas)" : "");

    form.reset();   // kembalikan tiap isian ke defaultValue/defaultChecked-nya

    // Cara lain membaca SELURUH isian sekaligus tanpa menyebutnya satu per satu.
    // Syaratnya tiap isian punya atribut name="..." di HTML:
    //   const data = new FormData(form);
    //   data.get("nama")           -> "Andi"  (string, sama seperti .value)
    //   Object.fromEntries(data)   -> { nama: "Andi", jumlah: "2", ukuran: "l" }
    //   Checkbox yang TIDAK dicentang sama sekali tidak muncul di FormData.
});""",
            },
            {
                "heading": "Merender daftar ke halaman: innerHTML, insertAdjacentHTML, data-*",
                "body": [
                    "textContent vs innerHTML - keduanya mengisi elemen, akibatnya jauh berbeda:",
                    "  el.textContent = \"<b>halo</b>\"  -> pengguna melihat tulisan <b>halo</b> apa adanya",
                    "  el.innerHTML   = \"<b>halo</b>\"  -> browser MEMBUAT elemen <b>, halo jadi tebal",
                    "",
                    "Karena innerHTML benar-benar membangun elemen, memasukkan teks dari pengguna ke",
                    "dalamnya sama dengan mengizinkan pengguna menulis HTML di halamanmu. Itulah XSS",
                    "(Cross-Site Scripting): satu komentar berisi <img src=x onerror=\"...\"> sudah cukup",
                    "untuk menjalankan kode di browser pengunjung lain. Aturan praktisnya:",
                    "  - innerHTML hanya untuk template yang KAMU tulis sendiri.",
                    "  - Isi yang datang dari pengguna: pakai textContent, atau ubah dulu karakter",
                    "    < > & \" jadi entitas seperti fungsi escapeHtml di contoh.",
                    "",
                    "insertAdjacentHTML menyisipkan HTML tanpa menyentuh isi yang sudah ada.",
                    "el.innerHTML += ... terlihat sama tapi membangun ULANG seluruh isi: elemen lama",
                    "dibuang dan dibuat ulang, sehingga listener yang menempel padanya hilang dan",
                    "ketikan yang sedang berlangsung di dalam <input> ikut terhapus.",
                    "  Empat posisinya:",
                    "    \"beforebegin\" sebelum elemen        \"afterbegin\" jadi anak PERTAMA",
                    "    \"beforeend\"   jadi anak TERAKHIR    \"afterend\"   sesudah elemen",
                    "",
                    "data-* menempelkan datamu sendiri ke sebuah elemen (sintaksnya dibahas di materi",
                    "HTML tentang atribut). Di JavaScript dibaca lewat el.dataset:",
                    "  <li data-id=\"7\" data-harga-satuan=\"15000\">",
                    "      el.dataset.id            -> \"7\"",
                    "      el.dataset.hargaSatuan   -> \"15000\"",
                    "  Namanya berubah dari kebab-case jadi camelCase, dan nilainya SELALU string.",
                    "  Inilah cara baku menempelkan id ke sebuah tombol atau baris daftar.",
                ],
                "code": """const menu = [
    { id: 1, nama: "Nasi Goreng", harga: 15000 },
    { id: 2, nama: "Soto Ayam", harga: 12000 },
];

function escapeHtml(teks) {
    return String(teks)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;");
}

// map() menghasilkan array potongan HTML; join("") menyatukannya jadi satu string.
// Tanpa join(""), JavaScript menyambung array dengan KOMA di antara tiap potongan.
const html = menu
    .map((m) => `<li data-id="${m.id}">
    ${escapeHtml(m.nama)} - Rp${m.harga}
    <button class="hapus">hapus</button>
  </li>`)
    .join("");

const daftar = document.querySelector("#daftar-menu");
daftar.innerHTML = html;

// Menambah satu baris tanpa membangun ulang baris yang sudah ada:
daftar.insertAdjacentHTML(
    "beforeend",
    `<li data-id="3">${escapeHtml("Es Teh")} - Rp5000</li>`,
);""",
            },
            {
                "heading": "Bubbling, event delegation, dan melepas listener",
                "body": [
                    "Sebuah klik tidak berhenti di elemen yang diklik. Setelah listener di situ",
                    "selesai, event NAIK ke induknya, lalu ke induk induknya, sampai document.",
                    "Itu namanya bubbling. Sumber bug klasiknya: dropdown atau modal yang menutup",
                    "sendiri begitu isinya diklik - karena klik di dalam ikut naik sampai ke listener",
                    "\"klik di luar berarti tutup\" yang dipasang di document.",
                    "",
                    "Dua nilai yang gampang tertukar di dalam handler:",
                    "  e.target         elemen yang BENAR-BENAR diklik (bisa <span> di dalam tombol)",
                    "  e.currentTarget  elemen tempat listener ini dipasang",
                    "  e.stopPropagation()  menghentikan perjalanan naik tadi",
                    "",
                    "  Jangan jadikan stopPropagation kebiasaan: ia juga mematikan listener lain yang",
                    "  mungkin memang butuh event itu, dan bug yang ditimbulkannya sulit dilacak",
                    "  karena kodenya ada di berkas lain. Sering yang sebenarnya kamu mau cuma",
                    "  e.preventDefault() - itu menahan perilaku bawaan, bukan penyebarannya.",
                    "",
                    "Event delegation: pasang SATU listener di container, bukan satu per baris.",
                    "  - Baris yang dibuat createElement atau innerHTML SESUDAH listener terpasang",
                    "    tetap tertangani, karena yang mendengarkan adalah induknya yang sudah ada.",
                    "    Ini satu-satunya cara rapi menangani elemen yang dibuat dinamis.",
                    "  - 1000 baris cukup 1 listener, bukan 1000.",
                    "  e.target.closest(\".hapus\") naik dari elemen yang diklik sampai menemukan",
                    "  elemen yang cocok selektornya, dan null kalau tidak ada - itu penyaringnya.",
                    "",
                    "removeEventListener butuh fungsi yang SAMA PERSIS dengan yang didaftarkan:",
                    "  el.addEventListener(\"click\", () => tutup());",
                    "  el.removeEventListener(\"click\", () => tutup());   // TIDAK melepas apa pun",
                    "  Dua arrow function itu dua objek berbeda walaupun isinya identik. Simpan",
                    "  fungsinya di variabel dulu, atau pakai opsi { once: true } kalau listener-nya",
                    "  memang cuma perlu jalan sekali.",
                ],
                "code": """const daftar = document.querySelector("#daftar-menu");

// SATU listener untuk seluruh daftar, termasuk baris yang belum dibuat.
daftar.addEventListener("click", (e) => {
    const tombol = e.target.closest(".hapus");
    if (!tombol) return;          // kliknya bukan di tombol hapus -> abaikan

    const baris = tombol.closest("li");
    console.log("hapus id:", baris.dataset.id);   // string, misalnya "2"
    baris.remove();
});

// target vs currentTarget - bedanya kelihatan kalau tombolnya berisi <span>.
daftar.addEventListener("click", (e) => {
    console.log(e.target.tagName);          // SPAN atau BUTTON: yang benar-benar diklik
    console.log(e.currentTarget.tagName);   // UL: tempat listener ini dipasang
});

// Dropdown yang menutup saat diklik DI LUAR kotaknya. Tanpa stopPropagation,
// klik DI DALAM kotak ikut naik sampai document dan menutup kotaknya sendiri.
const kotak = document.querySelector("#kotak");
kotak.addEventListener("click", (e) => {
    e.stopPropagation();
});
document.addEventListener("click", () => {
    kotak.classList.remove("tampil");
});

// Cara lain yang tidak mengganggu listener milik fitur lain: event-nya tidak
// dihentikan, cukup ditanya dari mana asalnya.
//   document.addEventListener("click", (e) => {
//       if (!e.target.closest("#kotak")) kotak.classList.remove("tampil");
//   });

// Melepas listener: fungsinya disimpan di variabel supaya bisa disebut lagi.
function tekanEsc(e) {
    if (e.key === "Escape") {
        kotak.classList.remove("tampil");
        document.removeEventListener("keydown", tekanEsc);
    }
}
document.addEventListener("keydown", tekanEsc);

// Listener yang melepas dirinya sendiri sesudah sekali jalan:
document.querySelector("#sekali").addEventListener("click", () => {
    console.log("cuma muncul sekali");
}, { once: true });""",
            },
        ],
    },
    {
        "title": "27. JSON & Fetch API",
        "sections": [
            {
                "body": [
                    "JSON (JavaScript Object Notation) = format data berbasis teks",
                    "yang PALING UMUM dipakai untuk pertukaran data web (REST API).",
                    "Formatnya sangat mirip object literal JavaScript.",
                    "",
                    "  JSON.stringify(objek)   -> object JS jadi STRING JSON",
                    "  JSON.parse(teks)        -> string JSON jadi OBJECT JS",
                    "",
                    "Fetch API = cara STANDAR (built-in) untuk melakukan network",
                    "request (mengambil data dari server/API) di JavaScript modern,",
                    "menggantikan XMLHttpRequest yang lebih rumit.",
                ]
            },
            {
                "heading": "Contoh fetch dengan async/await (GET request)",
                "code": """async function ambilDataUser(id) {
    try {
        const response = await fetch(`https://api.contoh.com/users/${id}`);

        if (!response.ok) {                 // cek status HTTP (200-299 = ok)
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json(); // parse body response jadi object JS
        console.log(data);
        return data;
    } catch (error) {
        console.log("Gagal mengambil data:", error.message);
    }
}

ambilDataUser(1);"""
            },
            {
                "heading": "POST request dengan body JSON",
                "code": """async function buatUser(dataUser) {
    const response = await fetch("https://api.contoh.com/users", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(dataUser),    // object JS -> string JSON
    });

    const hasil = await response.json();
    return hasil;
}

buatUser({ nama: "Andi", umur: 20 })
    .then((hasil) => console.log("User dibuat:", hasil));

// Ringkasan method HTTP yang sering dipakai di REST API:
//   GET    -> mengambil data
//   POST   -> membuat data baru
//   PUT    -> mengubah SELURUH data (ganti total)
//   PATCH  -> mengubah SEBAGIAN data
//   DELETE -> menghapus data"""
            },
            {
                "body": [
                    "Empat hal kecil di sekitar fetch yang menyelamatkan banyak waktu:",
                    "",
                    "  response.text()   pasangan response.json(), untuk balasan yang BUKAN",
                    "      JSON: HTML, CSV, atau teks biasa. Pakai ini juga saat sebuah API",
                    "      gagal dan balasannya ternyata halaman error - response.json()",
                    "      pada halaman HTML melempar SyntaxError yang membingungkan.",
                    "",
                    "  JSON.stringify(obj, null, 2)  argumen ketiga = jumlah spasi indentasi.",
                    "      Wajib dipakai saat menulis berkas konfigurasi atau mencetak data",
                    "      untuk dibaca manusia. (Argumen keduanya, null di sini, adalah",
                    "      penyaring key yang jarang dipakai.)",
                    "",
                    "  Tidak semua isi object selamat melewati JSON.stringify: undefined dan",
                    "      function lenyap, Date berubah jadi string. Daftar lengkapnya di",
                    "      materi 'Nilai vs Referensi & Menyalin Data'.",
                    "",
                    "  CORS. Kalau fetch ke alamat domain LAIN gagal padahal alamatnya benar",
                    "      dan servernya hidup, tersangka pertamanya CORS. Browser menolak",
                    "      memberikan hasilnya ke JavaScript kalau server tujuan tidak",
                    "      mengirim header izin (Access-Control-Allow-Origin). Ini keputusan",
                    "      SERVER, bukan bug di kodemu - dan tidak bisa diperbaiki dari sisi",
                    "      browser. Node tidak punya aturan ini sama sekali, jadi fetch yang",
                    "      sama bisa berhasil dari terminal dan gagal dari halaman web.",
                ],
            },
            {
                "heading": "localStorage: hanya string, jadi lewat JSON",
                "body": [
                    "Masih di keluarga JSON: cara browser menyimpan data supaya tidak hilang",
                    "saat halaman ditutup.",
                    "",
                    "  localStorage     bertahan sampai dihapus, walau browser ditutup",
                    "  sessionStorage   hilang begitu tab-nya ditutup",
                    "",
                    "Keduanya punya method yang sama persis:",
                    "  setItem(kunci, nilai)   simpan",
                    "  getItem(kunci)          baca; kunci yang belum ada memberi null",
                    "  removeItem(kunci)       hapus satu",
                    "  clear()                 hapus semua",
                    "",
                    "Dan keduanya punya satu batasan yang PASTI menjebak: isinya HANYA BISA",
                    "STRING. Menyimpan object langsung tidak melempar error - JavaScript",
                    "diam-diam mengubahnya jadi teks \"[object Object]\", dan datanya hilang",
                    "untuk selamanya. Karena itu object dan array WAJIB lewat JSON.stringify",
                    "saat disimpan, lalu JSON.parse saat dibaca kembali.",
                    "",
                    "Pasangan inilah yang kamu perlukan untuk project 'To-do list dengan",
                    "localStorage' di materi Roadmap.",
                ],
                "code": """// localStorage HANYA ada di browser. Supaya contoh ini bisa dicoba dengan
// node, di bawah ada tiruan sederhananya. Yang ditiru justru sifat yang paling
// sering menjebak: ia MEMAKSA setiap nilai menjadi string.
const localStorage = {
    _isi: {},
    setItem(k, v) { this._isi[k] = String(v); },
    getItem(k) { return k in this._isi ? this._isi[k] : null; },
    removeItem(k) { delete this._isi[k]; },
    clear() { this._isi = {}; },
};

localStorage.setItem("tema", "gelap");
console.log(localStorage.getItem("tema"));        // gelap
console.log(localStorage.getItem("belum ada"));   // null  <- null, bukan undefined

// JEBAKANNYA: menyimpan object atau array apa adanya.
const tugas = [{ teks: "Belajar JS", selesai: false }];
localStorage.setItem("tugas", tugas);
console.log(localStorage.getItem("tugas"));   // [object Object]  <- datanya HILANG

// Yang benar: JSON.stringify saat menyimpan, JSON.parse saat membaca.
localStorage.setItem("tugas", JSON.stringify(tugas));
const kembali = JSON.parse(localStorage.getItem("tugas"));
console.log(kembali[0].teks, kembali[0].selesai);   // Belajar JS false

// Kunci yang belum pernah diisi memberi null, dan JSON.parse(null) juga null.
// Jadi sediakan nilai cadangan untuk kali pertama program dijalankan.
const daftar = JSON.parse(localStorage.getItem("belum ada")) ?? [];
console.log(daftar);                          // []

localStorage.removeItem("tema");
console.log(localStorage.getItem("tema"));    // null

// Argumen ketiga JSON.stringify = jumlah spasi indentasi, untuk keluaran
// yang enak dibaca manusia.
console.log(JSON.stringify({ nama: "Andi", nilai: [80, 90] }, null, 2));"""
            },
        ],
    },
    {
        "title": "28. Module (import/export) & npm Dasar",
        "sections": [
            {
                "body": [
                    "Module = memecah kode jadi banyak file agar lebih terorganisir",
                    "dan bisa dipakai ulang (mirip module Python / package Java).",
                    "",
                    "ES Module (standar modern, dipakai di browser & Node.js):",
                    "",
                    "  // file matematika.js",
                    "  export function tambah(a, b) {",
                    "      return a + b;",
                    "  }",
                    "  export const PI = 3.14159;",
                    "  export default function kali(a, b) {   // HANYA BOLEH 1 default per file",
                    "      return a * b;",
                    "  }",
                    "",
                    "  // file main.js",
                    "  import kali, { tambah, PI } from './matematika.js';",
                    "  console.log(tambah(2, 3));   // 5",
                    "  console.log(kali(2, 3));     // 6",
                ]
            },
            {
                "body": [
                    "npm (Node Package Manager) = package manager bawaan Node.js",
                    "untuk menginstall & mengelola library eksternal JavaScript.",
                    "",
                    "  npm init -y              -> membuat file package.json baru",
                    "  npm install nama_paket   -> install library (masuk ke node_modules/)",
                    "  npm install -D nama_paket -> install SEBAGAI dev dependency saja",
                    "  npm uninstall nama_paket  -> hapus library",
                    "  npm run nama_script       -> jalankan script custom di package.json",
                    "",
                    "package.json: file konfigurasi project Node.js, mencatat:",
                    "  - nama & versi project",
                    "  - daftar dependency (\"dependencies\" & \"devDependencies\")",
                    "  - script custom (\"scripts\": { \"start\": \"node index.js\" })",
                    "",
                    "  npm start    -> menjalankan script 'start' di package.json",
                ]
            },
            {
                "body": [
                    "CommonJS (cara LAMA di Node.js, masih sering ditemui di kode legacy):",
                    "  // file matematika.js",
                    "  function tambah(a, b) { return a + b; }",
                    "  module.exports = { tambah };",
                    "",
                    "  // file main.js",
                    "  const { tambah } = require('./matematika.js');",
                    "",
                    "Bedanya dari ES Module: pakai 'require()' bukan 'import',",
                    "dan 'module.exports' bukan 'export'. Node.js modern mendukung",
                    "KEDUANYA, tergantung konfigurasi \"type\" di package.json.",
                ]
            },
        ],
    },
    {
        "title": "29. Module Lanjutan: Semua Bentuk Import & Export",
        "sections": [
            {
                "body": [
                    "Materi Module (import/export) & npm Dasar mengajarkan dua bentuk: named export dan",
                    "default export. Itu cukup untuk MENULIS modul sendiri, tapi belum cukup untuk MEMBACA",
                    "kode orang lain. Begitu kamu membuka repo sungguhan, deretan baris paling atas tiap",
                    "berkas justru berisi bentuk yang belum pernah kamu lihat - dan baris paling atas adalah",
                    "baris yang paling tidak bisa dilewati: kalau kamu tidak tahu dari mana sebuah nama",
                    "datang, seluruh sisa berkas jadi teka-teki.",
                    "",
                    "Semua bentuk import yang akan kamu temui, lengkap:",
                    "",
                    "  import { a } from \"./m.js\"           ambil export bernama a; namanya HARUS persis",
                    "  import { a as b } from \"./m.js\"      ambil a, tapi di berkas ini panggil dia b",
                    "  import bawaan from \"./m.js\"          ambil export default; namanya BEBAS kamu pilih",
                    "  import bawaan, { a } from \"./m.js\"   default dan named sekaligus, satu baris",
                    "  import * as m from \"./m.js\"          semua named export jadi satu object: m.a, m.b",
                    "  import \"./m.js\"                      jalankan berkasnya, jangan ambil apa pun",
                    "  const m = await import(\"./m.js\")     muat SAAT ITU JUGA, bukan di awal program",
                    "",
                    "Dan semua bentuk export-nya:",
                    "",
                    "  export function f() {}                  menempel langsung di deklarasinya",
                    "  export { f, g }                         satu daftar di KAKI berkas",
                    "  export { f as hitung }                  keluar memakai nama yang berbeda",
                    "  export default f                        hanya boleh SATU per berkas",
                    "  export * from \"./x.js\"                  teruskan semua named export berkas lain",
                    "  export { default as F } from \"./F.js\"   default milik orang lain -> named di sini",
                    "",
                    "Dua bentuk yang paling sering bikin bingung saat pertama kali dilihat:",
                    "",
                    "  - import * as React from \"react\" tidak mengambil satu nama; ia mengambil SELURUH",
                    "    isi modul jadi satu object. Sesudah itu semuanya dipanggil lewat titik:",
                    "    React.useState(), React.Fragment. Object itu HANYA BISA DIBACA.",
                    "  - import \"./gaya.css\" tidak menugaskan apa pun ke variabel, dan itu terlihat persis",
                    "    seperti salah ketik. Ia disengaja: yang dibutuhkan bukan nilainya, melainkan EFEK",
                    "    dimuatnya berkas itu. Di proyek ber-bundler, memuat CSS berarti gayanya ikut",
                    "    dipasang ke halaman. Bentuk yang sama dipakai untuk polyfill dan berkas setup.",
                    "",
                    "Alias (kata 'as') juga bukan gaya-gayaan. Ia dipakai ketika dua modul mengekspor nama",
                    "yang sama persis, atau ketika nama aslinya terlalu umum untuk dibiarkan berkeliaran:",
                    "import { get as ambilUser } from \"./api/user.js\".",
                ],
            },
            {
                "heading": "Proyek kecil: daftar export di kaki berkas, alias, dan barrel index.js",
                "code": """// ==== File: package.json ====
{
    "name": "contoh-module",
    "version": "1.0.0",
    "type": "module"
}

// ==== File: alat/matematika.js ====
// Perhatikan: TIDAK ADA kata 'export' yang menempel di deklarasi mana pun.
const PPN = 0.11;

function hitungPajak(harga) {
    return Math.round(harga * PPN);
}

function totalBayar(harga) {
    return harga + hitungPajak(harga);
}

// Satu daftar export di KAKI berkas. Sekali lihat, ketahuan apa saja yang keluar
// dari berkas ini - tidak perlu memindai seluruh isinya mencari kata 'export'.
// 'hitungPajak as pajak': di dalam berkas ini namanya tetap hitungPajak,
// tapi berkas lain melihatnya bernama 'pajak'.
export { PPN, hitungPajak as pajak, totalBayar };

// ==== File: alat/uang.js ====
function rupiah(angka) {
    return "Rp" + angka;
}

// default = "isi utama berkas ini". Hanya boleh SATU per berkas.
export default rupiah;

// ==== File: alat/index.js ====
// Berkas 'barrel': tidak punya logika sendiri, cuma menyalurkan isi tetangganya
// supaya pemakainya cukup menyebut SATU alamat, bukan tiga.
export * from "./matematika.js";                  // semua NAMED export matematika.js
export { default as rupiah } from "./uang.js";    // default uang.js -> named di sini

// ==== File: utama.js ====
import * as alat from "./alat/index.js";
import { pajak as hitungPpn, PPN } from "./alat/index.js";

console.log("Isi namespace :", Object.keys(alat).join(", "));
console.log("PPN           :", PPN);
console.log("Pajak 100000  :", alat.pajak(100000));
console.log("Lewat alias   :", hitungPpn(100000));
console.log("Total bayar   :", alat.rupiah(alat.totalBayar(100000)));

// Jalankan dengan: node utama.js
// Isi namespace : PPN, pajak, rupiah, totalBayar
// PPN           : 0.11
// Pajak 100000  : 11000
// Lewat alias   : 11000
// Total bayar   : Rp111000""",
            },
            {
                "body": [
                    "Enam hal yang membuat import gagal padahal 'kelihatannya sudah benar'. Semuanya pasti",
                    "kamu temui, jadi kenali pesannya sekarang supaya tidak kehilangan satu jam nanti.",
                    "",
                    "  1. Di Node, ekstensi .js WAJIB ditulis. from \"./alat/matematika\" langsung berhenti:",
                    "       Error [ERR_MODULE_NOT_FOUND]: Cannot find module .../alat/matematika",
                    "       Did you mean to import \"./alat/matematika.js\"?",
                    "     Bundler (Vite, webpack, Next.js) memang menebaknya untukmu, dan ITU sebabnya kode",
                    "     React di internet menulis from \"./Tombol\" tanpa ekstensi. Node polos tidak menebak.",
                    "",
                    "  2. Meng-import sebuah FOLDER berarti meng-import index.js di dalamnya. Ini konvensi",
                    "     murni - mustahil ditebak sendiri, dan tidak ada tanda apa pun di kodenya:",
                    "     from \"./alat\" berarti from \"./alat/index.js\". Itulah alasan berkas bernama",
                    "     index.js ada di mana-mana. Yang menebak lagi-lagi bundler dan require() CommonJS;",
                    "     Node ESM murni menolak dan menyebut alasannya terang-terangan:",
                    "       Error [ERR_UNSUPPORTED_DIR_IMPORT]: Directory import .../alat is not supported",
                    "",
                    "  3. export * TIDAK ikut membawa default. Barrel yang mau meneruskan default tetangganya",
                    "     harus menulisnya sendiri: export { default as rupiah } from \"./uang.js\".",
                    "",
                    "  4. Salah ketik nama import bukan menghasilkan undefined, melainkan MATI TOTAL sebelum",
                    "     satu baris pun sempat jalan:",
                    "       SyntaxError: The requested module './alat/index.js' does not provide an export",
                    "       named 'pajakk'",
                    "     Ini justru kabar baik. Import statis diperiksa saat modul dirangkai, bukan saat",
                    "     dipakai - beda dari object biasa yang salah ketiknya diam-diam jadi undefined.",
                    "",
                    "  5. Object hasil import * as m hanya bisa DIBACA. m.PPN = 0.2 melempar",
                    "     TypeError: Cannot assign to read only property 'PPN' of object '[object Module]'.",
                    "",
                    "  6. Satu berkas dimuat SEKALI saja seumur hidup program. Diimpor sepuluh berkas",
                    "     berbeda, badan modulnya tetap dijalankan satu kali dan hasilnya dipakai bersama.",
                    "     Karena itu menaruh state (misalnya sebuah array) di level module berarti state itu",
                    "     dipakai ramai-ramai - global tanpa terlihat global.",
                ],
            },
            {
                "heading": "Import efek samping, hoisting, dan import() dinamis",
                "body": [
                    "Tiga hal sekaligus di contoh ini, dan semuanya lazim di kode nyata:",
                    "",
                    "  - import \"./pengaturan.mjs\" tanpa { } dan tanpa nama: yang dicari efeknya, bukan",
                    "    nilainya. Ini bentuk yang sama dengan import \"./gaya.css\" di proyek React.",
                    "  - Baris import itu sengaja ditaruh PALING BAWAH untuk membuktikan import di-HOIST:",
                    "    ia tetap dijalankan lebih dulu daripada baris pertama berkasnya.",
                    "  - await import(\"./berat.mjs\") memuat modul HANYA ketika dibutuhkan. Inilah dasar",
                    "    code-splitting dan lazy loading: halaman tidak perlu mengunduh kode fitur yang",
                    "    belum tentu dibuka. Ekstensi .mjs dipakai supaya berkas ini jadi module tanpa",
                    "    perlu package.json sama sekali.",
                ],
                "code": """// ==== File: pengaturan.mjs ====
// Berkas ini tidak meng-export APA PUN. Ia cuma mengerjakan sesuatu saat dimuat.
console.log("[pengaturan] dijalankan saat berkas ini dimuat");
globalThis.NAMA_APP = "Toko Levi";

// ==== File: berat.mjs ====
console.log("[berat] BARU dimuat sekarang, bukan di awal program");

export function laporan(judul) {
    return "== " + judul + " ==";
}

export default "aku export default milik berat.mjs";

// ==== File: utama.mjs ====
console.log("[utama] ini baris PERTAMA yang ditulis di berkas utama.mjs");
console.log("[utama] NAMA_APP =", globalThis.NAMA_APP);

const perluLaporan = true;   // ganti jadi false: berat.mjs tak akan pernah dimuat

if (perluLaporan) {
    // import() adalah FUNGSI, bukan pernyataan. Ia mengembalikan Promise, jadi
    // hasilnya ditunggu dengan await (lihat materi async/await).
    const modul = await import("./berat.mjs");
    console.log(modul.laporan("Penjualan"));
    console.log(modul.default);   // export default-nya ada di property .default
} else {
    console.log("[utama] berat.mjs tidak pernah disentuh");
}

// Sengaja ditaruh PALING BAWAH. Perhatikan urutan keluarannya.
import "./pengaturan.mjs";

// Jalankan dengan: node utama.mjs
// [pengaturan] dijalankan saat berkas ini dimuat      <- paling atas, walau ditulis paling bawah
// [utama] ini baris PERTAMA yang ditulis di berkas utama.mjs
// [utama] NAMA_APP = Toko Levi
// [berat] BARU dimuat sekarang, bukan di awal program
// == Penjualan ==
// aku export default milik berat.mjs""",
            },
            {
                "body": [
                    "Pertanyaan yang menentukan segalanya: sebuah berkas .js itu ES Module atau CommonJS?",
                    "Tiga aturan, dibaca berurutan:",
                    "",
                    "  berkas.mjs   SELALU ES Module, apa pun isi package.json",
                    "  berkas.cjs   SELALU CommonJS, apa pun isi package.json",
                    "  berkas.js    ikut \"type\" di package.json TERDEKAT ke atas:",
                    "                 \"type\": \"module\"     -> ES Module (import/export)",
                    "                 \"type\": \"commonjs\"   -> CommonJS (require/module.exports)",
                    "                 tidak ditulis         -> Node 22+ menebak dari isinya; ada import",
                    "                                          di dalamnya berarti ES Module",
                    "",
                    "Dua ekstensi aneh itu ada justru karena aturan ketiga terlalu bergantung pada berkas",
                    "lain. .mjs dan .cjs memutuskan nasib satu berkas tanpa peduli konteksnya - dipakai",
                    "saat sebuah library harus menyediakan dua versi sekaligus.",
                    "",
                    "Dua pesan error paling sering di dunia nyata, dan artinya:",
                    "",
                    "  SyntaxError: Cannot use import statement outside a module",
                    "    -> berkasnya berisi import, tapi dibaca sebagai CommonJS. Penyebab lazimnya:",
                    "       ekstensi .cjs, atau package.json menulis \"type\": \"commonjs\" secara eksplisit.",
                    "  ReferenceError: require is not defined in ES module scope",
                    "    -> kebalikannya: menulis require() di berkas yang statusnya sudah ES Module.",
                    "",
                    "Tiga beda praktis lain dari require() yang jarang disebut tapi terasa tiap hari:",
                    "  - Module SELALU strict mode, tanpa perlu menulis \"use strict\". Salah ketik nama",
                    "    variabel jadi error, bukan variabel global baru yang terbuat diam-diam.",
                    "  - Tiap module punya SCOPE sendiri. const di sebuah module bukan variabel global,",
                    "    jadi dua berkas boleh memakai nama yang sama tanpa bentrok.",
                    "  - import di-hoist dan wajib di level teratas berkas; ia tidak boleh ditaruh di",
                    "    dalam if. require() sebaliknya - baris biasa yang jalan saat gilirannya tiba.",
                    "    Kalau butuh memuat bersyarat di ES Module, pakai import() dinamis tadi.",
                    "",
                    "Di BROWSER, import hanya hidup lewat atribut type=\"module\":",
                    "",
                    "  <script type=\"module\" src=\"utama.js\"></script>",
                    "",
                    "Tanpa type=\"module\", browser membaca berkasnya sebagai script biasa dan berhenti di",
                    "baris pertama dengan pesan yang sama persis: Cannot use import statement outside a",
                    "module. Bonusnya: script bertipe module otomatis DEFER - dijalankan setelah seluruh",
                    "HTML selesai dibaca, jadi document.querySelector di materi DOM langsung menemukan",
                    "elemennya tanpa perlu dibungkus DOMContentLoaded.",
                    "",
                    "Satu jebakan terakhir yang memakan waktu banyak orang: berkas ber-type=\"module\" TIDAK",
                    "bisa dicoba dengan klik dua kali di file manager (alamat file:///...). Browser",
                    "memblokirnya dengan galat CORS, dan halamannya diam saja seolah kodenya tidak ada.",
                    "Modul butuh alamat http. Nyalakan server lokal dari folder yang sama, lalu buka",
                    "http://localhost:8000 di browser:",
                    "",
                    "  python3 -m http.server 8000",
                ],
            },
        ],
    },
    {
        "title": "30. Node.js: Process, Berkas, dan Path",
        "sections": [
            {
                "body": [
                    "Node.js bukan 'JavaScript versi lain' - bahasanya sama persis dengan yang di browser.",
                    "Yang berbeda adalah LINGKUNGANNYA: objek bawaan apa yang tersedia di sekitarmu.",
                    "",
                    "  Hanya ada di browser : document, window, alert, localStorage",
                    "  Hanya ada di Node    : process, require, __dirname, modul fs / path / http",
                    "",
                    "Tidak ada yang punya keduanya, dan itu menjelaskan satu error yang PASTI kamu temui.",
                    "Contoh loop di materi 'Perulangan' memakai process.stdout.write. Kalau contoh",
                    "itu ditempel ke Console browser (F12), hasilnya: 'ReferenceError: process is",
                    "not defined'. Bukan kodenya yang salah - contoh itu memang ditulis untuk",
                    "dijalankan dengan 'node file.js'.",
                    "",
                    "process = objek global di Node yang mewakili PROSES yang sedang berjalan:",
                    "",
                    "  process.argv                -> array argumen yang diketik di terminal",
                    "  process.env                 -> variabel lingkungan (konfigurasi dari luar kode)",
                    "  process.exit(kode)          -> hentikan program SEKARANG JUGA dengan kode keluar",
                    "  process.stdout.write(teks)  -> cetak TANPA menambah baris baru",
                    "",
                    "process.stdout.write vs console.log - bedanya dua hal, bukan satu:",
                    "  1. console.log selalu menambah baris baru; stdout.write tidak menambah apa pun.",
                    "  2. console.log menerima banyak argumen dan tipe apa saja; stdout.write HANYA",
                    "     menerima string. process.stdout.write(5) langsung melempar TypeError.",
                    "  Itulah sebabnya materi 'Perulangan' menulis process.stdout.write(i + \" \")",
                    "  - tanda + \" \" di situ bukan cuma pemisah, tapi juga yang mengubah angka i",
                    "  jadi string.",
                    "",
                    "process.argv selalu diawali dua hal yang BUKAN argumenmu:",
                    "  argv[0] = path program node        argv[1] = path berkas .js yang dijalankan",
                    "  argv[2] dan seterusnya = argumen sungguhan yang kamu ketik",
                    "Karena itu di mana-mana kamu akan melihat process.argv.slice(2).",
                    "",
                    "process.env dipakai untuk hal yang BERBEDA di tiap komputer: nomor port, alamat",
                    "database, kunci API. Isinya SELALU string atau undefined - tidak pernah angka,",
                    "tidak pernah boolean. Jadi process.env.PORT + 1 menghasilkan \"30001\", bukan 3001.",
                ],
            },
            {
                "heading": "Argumen terminal, environment, dan kode keluar",
                "code": """// Argumen sungguhan mulai dari indeks 2, dua yang pertama milik Node sendiri.
const argumen = process.argv.slice(2);

console.log("Jumlah argumen:", argumen.length);
for (const [i, arg] of argumen.entries()) {
    console.log(`  argumen ke-${i}: ${arg}`);
}
if (argumen.length === 0) {
    console.log("  (kosong - coba jalankan ulang dengan menambahkan: kopi teh)");
}

// || memberi nilai cadangan kalau variabelnya belum diset di lingkungan.
const port = process.env.PORT || "3000";
console.log("PORT :", port, "| tipe:", typeof port);   // selalu "string"
console.log("Angka:", Number(port) + 1);               // ubah dulu baru dihitung

// stdout.write tidak menambah baris baru, jadi semuanya menempel di satu baris.
for (let i = 1; i <= 5; i++) {
    process.stdout.write(i + " ");
}
process.stdout.write("\\n");        // baris baru ditulis SENDIRI kalau perlu

// Kode keluar dibaca oleh shell dan oleh CI: 0 = sukses, selain 0 = gagal.
// Kalau tidak dipanggil, Node otomatis keluar dengan 0 saat kodenya habis.
process.exit(0);""",
            },
            {
                "body": [
                    "Modul BAWAAN vs paket npm",
                    "",
                    "Sebagian modul sudah ikut terpasang bersama Node: tidak ada npm install, tidak masuk",
                    "node_modules, dan tidak pernah muncul di package.json. Ini yang paling sering",
                    "kelihatan di baris-baris pertama sebuah berkas Node:",
                    "",
                    "  fs        membaca & menulis berkas dan folder",
                    "  path      merangkai dan membedah jalur berkas",
                    "  readline  membaca ketikan baris per baris dari terminal",
                    "  os        info sistem: os.platform(), os.homedir(), os.cpus()",
                    "  url       membedah alamat: new URL(...), .searchParams",
                    "  crypto    hash & nilai acak aman: crypto.randomUUID()",
                    "  http      membuat server web tanpa library apa pun (Express dibangun di atas ini)",
                    "",
                    "Dua cara memanggilnya - lihat materi 'Module (import/export) & npm Dasar'",
                    "soal CommonJS vs ES Module:",
                    "  const fs = require(\"node:fs\");     // CommonJS",
                    "  import fs from \"node:fs\";          // ES Module",
                    "",
                    "Awalan node: menegaskan 'ini bawaan Node, bukan paket dari npm'. Untungnya dua:",
                    "pembaca kodemu tahu seketika tanpa mengecek package.json, dan beberapa modul baru",
                    "(mis. node:test) MEMANG hanya bisa dipanggil dengan awalan itu. Kode lama menulis",
                    "require(\"fs\") tanpa awalan dan tetap jalan - keduanya modul yang sama persis.",
                    "",
                    "Jebakan path yang paling sering menjatuhkan orang: 'di sini' itu di mana?",
                    "",
                    "Jalur relatif seperti \"data/catatan.txt\" dihitung dari FOLDER TEMPAT KAMU MENGETIK",
                    "perintah node, bukan dari folder berkas .js-nya. Program yang sama, dijalankan dari",
                    "folder lain, mendadak bilang berkasnya tidak ditemukan.",
                    "",
                    "  __dirname      -> folder tempat berkas INI berada (CommonJS)",
                    "  __filename     -> jalur lengkap berkas ini berikut namanya (CommonJS)",
                    "  process.cwd()  -> folder tempat perintah node diketik",
                    "",
                    "Di ES Module (\"type\": \"module\" di package.json, atau berkas .mjs) __dirname TIDAK",
                    "ADA sama sekali. Penggantinya empat baris ini, dan kamu akan sering melihatnya:",
                    "",
                    "  import path from \"node:path\";",
                    "  import { fileURLToPath } from \"node:url\";",
                    "  const __filename = fileURLToPath(import.meta.url);   // import.meta.url berupa URL",
                    "  const __dirname = path.dirname(__filename);          // file:///... jadi jalur biasa",
                    "",
                    "Merangkai jalur: pakai path.join, JANGAN menyambung sendiri dengan + \"/\"",
                    "  path.join(\"data\", \"arsip\", \"c.txt\")  -> \"data/arsip/c.txt\"",
                    "  \"data/\" + \"/arsip\" + \"/c.txt\"         -> \"data//arsip/c.txt\"  <- slash ganda",
                    "  Di Windows path.join menghasilkan \"data\\arsip\\c.txt\" - pemisahnya backslash,",
                    "  dan path.join otomatis memakai yang benar sesuai sistemnya. Menyambung sendiri tidak.",
                    "  path.join juga merapikan \"..\" dan \"./\" yang ada di tengah jalur.",
                    "  path.resolve(...) mirip, tapi hasilnya SELALU jalur absolut dari root.",
                    "  path.basename(\"/a/b/c.txt\") -> \"c.txt\"    path.extname(\"/a/b/c.txt\") -> \".txt\"",
                ],
            },
            {
                "heading": "Menulis dan membaca berkas dengan fs + path",
                "code": """const fs = require("node:fs");      // modul bawaan, tidak perlu npm install
const path = require("node:path");

// Dirangkai dari __dirname, jadi hasilnya sama dari folder mana pun node dijalankan.
const jalur = path.join(__dirname, "data", "catatan.txt");

console.log("Nama berkas :", path.basename(jalur));   // catatan.txt
console.log("Ekstensi    :", path.extname(jalur));    // .txt
console.log("Nama folder :", path.basename(path.dirname(jalur)));   // data

// recursive: true -> folder induk ikut dibuat, dan tidak error kalau sudah ada.
fs.mkdirSync(path.dirname(jalur), { recursive: true });

fs.writeFileSync(jalur, "baris pertama\\n");   // MENIMPA seluruh isi lama!
fs.appendFileSync(jalur, "baris kedua\\n");    // menambah di akhir, isi lama aman

console.log("Berkasnya ada?", fs.existsSync(jalur));   // true

// Tanpa "utf8", readFileSync mengembalikan Buffer (deretan byte), bukan string.
const isi = fs.readFileSync(jalur, "utf8");
process.stdout.write(isi);
console.log("Jumlah baris:", isi.trimEnd().split("\\n").length);

fs.rmSync(path.dirname(jalur), { recursive: true });   // bersihkan lagi
console.log("Masih ada?", fs.existsSync(jalur));       // false""",
            },
            {
                "heading": "Tiga gaya fs: callback, await, dan membaca ketikan",
                "body": [
                    "Konvensi error-first callback",
                    "",
                    "Sebelum ada Promise, SELURUH API async Node memakai satu bentuk yang sama: argumen",
                    "terakhir sebuah fungsi adalah callback, dan parameter PERTAMA callback itu selalu",
                    "error - null kalau sukses, objek Error kalau gagal. Hasilnya baru di parameter kedua.",
                    "",
                    "  fs.readFile(jalur, \"utf8\", (err, data) => { ... });",
                    "                              ^^^ error dulu, BARU hasilnya",
                    "",
                    "Lupa memeriksa if (err) adalah bug klasik: 'data' diam-diam bernilai undefined, dan",
                    "errornya baru meledak beberapa baris kemudian di tempat yang tidak ada hubungannya.",
                    "Kode Node lama penuh bentuk ini, jadi kamu harus bisa MEMBACANYA - tapi untuk kode",
                    "BARU pakai fs/promises + await, dengan try-catch seperti di materi async/await.",
                    "",
                    "Ada tiga wajah untuk fungsi fs yang sama, dan ketiganya beredar di kode nyata:",
                    "  fs.readFileSync(...)          -> memblokir; program berhenti sampai selesai",
                    "  fs.readFile(..., callback)    -> error-first callback, gaya lama",
                    "  fsp.readFile(...) + await     -> dari \"node:fs/promises\", gaya sekarang",
                    "Versi Sync boleh dipakai untuk skrip kecil dan saat program baru menyala; jangan",
                    "dipakai di dalam server, karena ia membekukan SELURUH proses untuk semua pengguna.",
                    "",
                    "Membaca ketikan pemakai: di Node TIDAK ADA prompt() seperti di browser. Penggantinya",
                    "modul readline, dan cara kerjanya berbasis EVENT - bukan \"berhenti lalu kembalikan",
                    "nilai\". Ia memancarkan \"line\" setiap satu baris masuk, dan \"close\" saat masukannya",
                    "habis (Ctrl+D di terminal, atau berkas yang dipipe sudah tamat). Untuk satu pertanyaan",
                    "saja ada bentuk singkat rl.question(\"Nama? \", (jawab) => { ... }) - callback juga.",
                ],
                "code": """const fs = require("node:fs");                 // versi sync + versi callback
const fsp = require("node:fs/promises");       // versi Promise, dipakai dengan await
const path = require("node:path");
const readline = require("node:readline");

const jalur = path.join(__dirname, "sementara.txt");

// 1. Gaya LAMA: callback error-first.
fs.writeFile(jalur, "halo dari callback\\n", (err) => {
    if (err) {                                 // WAJIB dicek lebih dulu
        console.error("Gagal menulis:", err.message);
        return;                                // dan WAJIB berhenti di sini
    }
    fs.readFile(jalur, "utf8", (errBaca, isi) => {
        if (errBaca) return console.error(errBaca.message);
        process.stdout.write("callback -> " + isi);
        lanjutModern();
    });
});

// 2. Gaya SEKARANG: fs/promises + await, error ditangkap try-catch.
async function lanjutModern() {
    try {
        await fsp.appendFile(jalur, "halo dari await\\n");
        const isi = await fsp.readFile(jalur, "utf8");
        process.stdout.write("await    -> " + isi.split("\\n")[1] + "\\n");
        await fsp.rm(jalur);
    } catch (e) {
        console.error("Gagal:", e.message);
    }
    bacaKetikan();
}

// 3. Membaca ketikan dari terminal baris per baris.
function bacaKetikan() {
    const rl = readline.createInterface({ input: process.stdin });
    let jumlah = 0;
    rl.on("line", (baris) => {
        jumlah++;
        console.log(`baris ${jumlah}: ${baris.toUpperCase()}`);
    });
    // 'close' jalan saat masukan habis (Ctrl+D di terminal).
    rl.on("close", () => console.log(`Selesai, ${jumlah} baris dibaca.`));
}""",
            },
        ],
    },
    {
        "title": "31. Membaca Repo JavaScript Sungguhan",
        "sections": [
            {
                "body": [
                    "Bahasa JavaScript-nya sudah kamu kuasai. Yang belum pernah disebut: apa",
                    "yang benar-benar muncul di layar saat kamu membuka repo JavaScript orang",
                    "lain di GitHub. Yang pertama terlihat bukan kode, melainkan dua puluhan",
                    "berkas asing di akar folder - dan rasa \"ada yang aku lewatkan\" yang",
                    "muncul dari situ hampir selalu keliru.",
                    "",
                    "Aturan pertama yang menghemat berjam-jam: sebagian besar isi sebuah repo",
                    "TIDAK ditulis manusia. Ia dihasilkan mesin, dan memang bukan untuk dibaca.",
                    "Dari seluruh pohon di bawah, yang perlu kamu buka cuma dua folder.",
                ],
                "code": """toko-online/
├── README.md            baca ini DULUAN - untuk apa proyek ini dan cara memakainya
├── package.json         nama, dependency, dan daftar perintah "scripts"
├── package-lock.json    dihasilkan npm   - jangan disunting, jangan dibaca
├── .gitignore           daftar apa yang TIDAK ikut disimpan Git
├── .env                 rahasia: password, API key - tidak ikut di-commit
├── vite.config.js       setelan build tool
├── node_modules/        dihasilkan npm   - ribuan folder milik paket orang lain
├── dist/                dihasilkan build - hasil jadi, tertimpa tiap kali build
├── src/                 DITULIS MANUSIA  - di sinilah kode sungguhannya
│   ├── main.js          titik masuk program
│   ├── keranjang.js
│   └── komponen/
└── tests/               DITULIS MANUSIA  - sering lebih banyak dari isi src/
    └── keranjang.test.js""",
            },
            {
                "heading": "Berkas di akar: yang MENGATUR perkakas, bukan yang dijalankan",
                "body": [
                    "Berkas yang namanya diawali titik atau berakhiran .config.js hampir selalu",
                    "bukan bagian program. Ia menyetel perkakas di sekitar program.",
                    "",
                    "  .gitignore         daftar yang tidak ikut disimpan Git. node_modules/ dan",
                    "                     .env hampir selalu tercantum di sini",
                    "  package-lock.json  versi PERSIS tiap paket, sampai ke dependency milik",
                    "                     dependency. Dihasilkan npm, ikut di-commit, tapi tidak",
                    "                     pernah disunting tangan dan tidak untuk dibaca",
                    "  node_modules/      isi semua paket terpasang. Jangan pernah dicari-cari:",
                    "                     hasil pencarian di sana bukan kode proyekmu",
                    "  .env               password database, API key. JANGAN di-commit - sekali",
                    "                     masuk riwayat Git ia tetap ada walau berkasnya dihapus",
                    "                     besoknya. Yang di-commit cuma .env.example tanpa isi",
                    "  .eslintrc.json     aturan linter (bentuk barunya: eslint.config.js)",
                    "  .prettierrc        aturan perapian otomatis: kutip, koma, lebar baris",
                    "  tsconfig.json      setelan TypeScript. Adanya berkas ini berarti repo-nya",
                    "                     TypeScript, walau sebagian berkasnya berakhiran .js",
                    "  vite.config.js     setelan build tool - bagaimana src/ diubah jadi dist/",
                    "",
                    "Angka versi di \"dependencies\" bukan sekadar angka. Tanda di depannya",
                    "menentukan paket mana yang boleh naik SENDIRI saat orang lain menjalankan",
                    "npm install, dan urutannya major.minor.patch:",
                    "",
                    "  \"react\": \"18.2.0\"    persis segitu, tidak pernah bergerak",
                    "  \"react\": \"^18.2.0\"   boleh naik selama angka PERTAMA tetap 18",
                    "                       (18.3.1 boleh, 19.0.0 tidak) - ini bawaan npm install",
                    "  \"react\": \"~18.2.0\"   boleh naik pada angka KETIGA saja",
                    "                       (18.2.9 boleh, 18.3.0 tidak)",
                    "",
                    "major naik = ada yang dirombak dan kode lama bisa rusak. minor = fitur",
                    "baru yang tidak merusak. patch = perbaikan bug. Itulah gunanya",
                    "package-lock.json: ia mengunci versi yang benar-benar terpasang, supaya",
                    "mesin temanmu memasang persis yang sama dengan mesinmu.",
                    "",
                    "Satu perintah lagi yang membuka README hampir semua proyek modern: npx.",
                    "Ia menjalankan sebuah paket TANPA memasangnya lebih dulu, untuk perkakas",
                    "yang cuma dipakai sekali seumur proyek.",
                    "",
                    "  npx create-vite@latest aplikasiku   membuat kerangka proyek baru",
                    "  npx eslint src/                     menjalankan linter tanpa memasangnya",
                ],
            },
            {
                "heading": "JSDoc, dan bukti bahwa describe/it/expect cuma fungsi biasa",
                "body": [
                    "Di atas ribuan fungsi di repo sungguhan ada blok komentar berbintang dua:",
                    "/** ... */. Itu JSDoc - komentar dengan aturan, dan biasanya bagian PALING",
                    "berguna saat membaca fungsi asing, karena ia menyebutkan tipe tiap",
                    "parameter, sesuatu yang tidak bisa kamu lihat dari kodenya sendiri.",
                    "",
                    "  @param {string} nama    parameter 'nama', isinya string",
                    "  @param {number} [umur]  kurung siku berarti opsional, boleh tidak diisi",
                    "  @returns {number}       apa yang dikembalikan",
                    "  @throws {Error}         kapan fungsinya melempar error",
                    "",
                    "Editor seperti VS Code membaca blok ini dan memunculkannya sebagai bantuan",
                    "saat kamu mengetik pemanggilan fungsinya. Menulis tipenya salah tidak",
                    "membuat program error - ia cuma menyesatkan pembaca berikutnya.",
                    "",
                    "Program di bawah ini juga menjawab pertanyaan yang pasti muncul saat kamu",
                    "membuka berkas tes: describe, it, dan expect itu kata kunci apa? Bukan.",
                    "Buktinya, tiga belas baris di bawah cukup untuk membuatnya sendiri.",
                ],
                "code": """/**
 * Menghitung harga yang harus dibayar setelah diskon.
 *
 * @param {number} harga  Harga awal dalam rupiah.
 * @param {number} persen Besar diskon, 0 sampai 100.
 * @returns {number} Harga akhir setelah dipotong.
 */
function hargaSetelahDiskon(harga, persen) {
    return harga - (harga * persen) / 100;
}

// Di repo sungguhan, tiga fungsi di bawah DISEDIAKAN Jest atau Vitest.
// Di sini kita menulisnya sendiri supaya jelas: mereka fungsi biasa.
function describe(nama, isi) {
    console.log(nama);
    isi();
}

function it(nama, isi) {
    try {
        isi();
        console.log("  lulus  - " + nama);
    } catch (e) {
        console.log("  GAGAL  - " + nama + " -> " + e.message);
    }
}

function expect(nilai) {
    return {
        toBe(harapan) {
            if (nilai !== harapan) {
                throw new Error(nilai + " bukan " + harapan);
            }
        },
    };
}

describe("hargaSetelahDiskon", () => {
    it("memotong 10 persen dari 200000", () => {
        expect(hargaSetelahDiskon(200000, 10)).toBe(180000);
    });

    it("mengembalikan harga apa adanya kalau diskonnya 0", () => {
        expect(hargaSetelahDiskon(50000, 0)).toBe(50000);
    });

    it("sengaja salah, supaya kelihatan bentuk kegagalannya", () => {
        expect(hargaSetelahDiskon(100000, 50)).toBe(60000);
    });
});

// Keluaran:
//   hargaSetelahDiskon
//     lulus  - memotong 10 persen dari 200000
//     lulus  - mengembalikan harga apa adanya kalau diskonnya 0
//     GAGAL  - sengaja salah, supaya kelihatan bentuk kegagalannya -> 50000 bukan 60000""",
            },
            {
                "heading": "Berkas tes: bacaan TERBAIK di repo yang belum kamu kenal",
                "body": [
                    "Namanya mengikuti berkas yang diujinya, ditambah .test.js atau .spec.js:",
                    "",
                    "  src/keranjang.js          kode yang diuji",
                    "  tests/keranjang.test.js   tesnya",
                    "",
                    "Bentuknya selalu bersarang tiga tingkat - describe membungkus beberapa it,",
                    "dan tiap it berisi satu atau beberapa expect:",
                    "",
                    "  import { totalHarga } from \"../src/keranjang.js\";",
                    "",
                    "  describe(\"totalHarga\", () => {",
                    "      it(\"menjumlahkan harga semua item\", () => {",
                    "          expect(totalHarga([{ harga: 1000 }, { harga: 2000 }])).toBe(3000);",
                    "      });",
                    "",
                    "      it(\"mengembalikan 0 untuk keranjang kosong\", () => {",
                    "          expect(totalHarga([])).toBe(0);",
                    "      });",
                    "  });",
                    "",
                    "Berkas ini tidak dijalankan dengan 'node' - fungsi describe/it/expect baru",
                    "ada saat Jest atau Vitest yang menjalankannya, lewat script di package.json:",
                    "",
                    "  npm test     (isinya biasanya \"jest\" atau \"vitest run\")",
                    "",
                    "Kenapa justru tes yang paling layak dibaca duluan:",
                    "  - Ia memperlihatkan sebuah fungsi DIPANGGIL dengan data sungguhan, lengkap",
                    "    dengan hasil yang diharapkan. Dokumentasi bisa basi tanpa ketahuan",
                    "    siapa pun. Tes yang basi langsung gagal.",
                    "  - Kalimat di dalam it(\"...\") menuliskan maksud fungsinya dengan bahasa",
                    "    manusia, sering lebih jelas daripada nama fungsinya sendiri.",
                    "  - Kasus aneh - array kosong, angka minus, teks kosong - biasanya cuma",
                    "    tercatat di tes, tidak di README mana pun.",
                ],
            },
            {
                "heading": "Berkas .js yang isinya BUKAN JavaScript polos",
                "body": [
                    "Cepat atau lambat kamu akan membuka berkas .js atau .jsx dan menemukan",
                    "sesuatu yang mirip HTML di tengah-tengah sebuah fungsi:",
                    "",
                    "  function Tombol({ label }) {",
                    "      return <button className=\"utama\">{label}</button>;",
                    "  }",
                    "",
                    "Itu JSX, dipakai React. Atau berkas .ts/.tsx dengan titik dua di mana-mana:",
                    "",
                    "  interface User { nama: string; umur: number; }",
                    "  const sapa = (u: User): string => `Halo ${u.nama}`;",
                    "  import type { Produk } from \"./produk\";   // impor yang cuma bawa tipe",
                    "",
                    "Keduanya BUKAN JavaScript yang bisa dijalankan browser atau Node apa adanya.",
                    "Ada langkah kompilasi lebih dulu (Vite, Babel, atau tsc) yang mengubahnya",
                    "jadi JavaScript biasa - JavaScript yang persis seperti yang kamu pelajari.",
                    "Jadi kalau membacanya membuatmu merasa ada sintaks yang terlewat dipelajari:",
                    "tidak ada yang terlewat. Itu bahasa lain yang ditumpuk di atas bahasa yang",
                    "sudah kamu kuasai, dan dipelajari terpisah nanti (lihat materi Roadmap).",
                    "",
                    "URUTAN membuka repo yang sama sekali asing, dipakai orang berpengalaman:",
                    "  1. README.md - untuk apa proyek ini dan cara menjalankannya.",
                    "  2. \"scripts\" di package.json - perintah yang benar-benar tersedia",
                    "     (npm run dev, npm test, npm run build). Ini daftar isi sesungguhnya.",
                    "  3. src/main.js atau src/index.js - titik masuk. Dari sana ikuti import",
                    "     satu per satu, sedalam yang kamu butuhkan saja.",
                    "  4. Berkas tes dari bagian yang ingin kamu ubah.",
                    "",
                    "Yang tidak dilakukan siapa pun: membuka berkas satu per satu dari atas ke",
                    "bawah, atau mencoba memahami isi node_modules/.",
                ],
            },
        ],
    },
    {
        "title": "32. Roadmap Menjadi JavaScript Developer Handal",
        "sections": [
            {
                "body": [
                    "Kamu sudah menguasai fondasi JavaScript yang solid: sintaks,",
                    "closure, this, OOP, exception, hingga async/await & fetch.",
                    "Berikut roadmap realistis untuk melangkah lebih jauh.",
                    "",
                    "TAHAP 1 - Kuatkan Fondasi (kamu di sini):",
                    "  - Paham perbedaan var/let/const, closure, this, dan async.",
                    "  - Latihan: kerjakan soal JavaScript di HackerRank/Codewars.",
                    "",
                    "TAHAP 2 - Pilih Jalur Spesialisasi:",
                    "  Frontend Development:",
                    "    - React (paling populer) / Vue / Angular - framework UI.",
                    "    - HTML & CSS (WAJIB dikuasai bersamaan dengan JS).",
                    "    - TypeScript - JavaScript + static typing, standar industri.",
                    "  Backend Development:",
                    "    - Node.js + Express/Fastify/NestJS - REST API server.",
                    "    - Database: MongoDB (NoSQL) atau PostgreSQL (relasional).",
                    "  Mobile Development:",
                    "    - React Native - membuat app iOS & Android dengan JS/React.",
                ]
            },
            {
                "body": [
                    "TAHAP 3 - Bangun Project Nyata:",
                    "  1. To-do list dengan localStorage (data tersimpan di browser).",
                    "  2. Aplikasi cuaca yang fetch data dari API publik.",
                    "  3. REST API sederhana dengan Node.js + Express + database.",
                    "  4. Full-stack app: frontend React + backend Node.js + database.",
                    "  5. Semua project WAJIB pakai Git & disertai testing dasar.",
                    "",
                    "TAHAP 4 - Kebiasaan Profesional:",
                    "  1. Pakai ESLint & Prettier untuk kerapian & konsistensi kode.",
                    "  2. Pelajari TypeScript - hampir jadi standar wajib di industri.",
                    "  3. Pahami build tools: Vite/Webpack untuk bundling project.",
                    "  4. Testing: Jest atau Vitest untuk unit test JavaScript.",
                    "  5. Baca kode open source populer (React, Express) di GitHub.",
                ]
            },
            {
                "body": [
                    "Kebiasaan harian agar handal:",
                    "  1. Ketik ulang semua contoh di aplikasi ini, jangan copy-paste.",
                    "  2. Buka browser console (F12), eksperimen langsung di sana.",
                    "  3. Pahami BENAR-BENAR closure, this, dan event loop - ini yang",
                    "     paling sering ditanyakan saat wawancara kerja JavaScript.",
                    "  4. Baca error message di console dengan teliti (stack trace",
                    "     menunjukkan PERSIS baris mana yang bermasalah).",
                    "  5. Kuasai SQL (lihat menu SQL di aplikasi ini) untuk melengkapi",
                    "     kemampuan sebagai full-stack JavaScript developer.",
                    "",
                    "JavaScript terus berkembang PESAT - fitur ES6+ (2015 ke atas)",
                    "yang kamu pelajari di sini adalah fondasi WAJIB sebelum",
                    "mempelajari framework apapun (React, Vue, Node.js, dll).",
                ]
            },
        ],
    },
]
