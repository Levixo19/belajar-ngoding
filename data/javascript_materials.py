JAVASCRIPT_MATERIALS = [
    {
        "title": "1. Pengenalan JavaScript & Cara Menjalankan",
        "sections": [
            {
                "body": [
                    "JavaScript adalah bahasa pemrograman utama untuk web. Kodenya jalan di",
                    "dalam browser, jadi halaman bisa bereaksi waktu diklik, diketik, atau",
                    "digulir.",
                    "",
                    "Sedikit sejarahnya:",
                    "  - JavaScript dibikin Brendan Eich tahun 1995, awalnya untuk browser",
                    "    Netscape.",
                    "  - Sejak Node.js muncul tahun 2009, JavaScript juga dipakai di server",
                    "    atau backend, yaitu komputer yang melayani permintaan dari browser.",
                    "  - Cuma JavaScript yang bisa langsung dijalankan semua browser modern",
                    "    tanpa memasang apa pun.",
                    "",
                    "Pakai JavaScript, kamu bisa bikin:",
                    "  - Frontend web, yaitu bagian halaman yang interaktif. Biasanya pakai",
                    "    React, Vue, atau Angular.",
                    "  - Backend: server dan API pakai Node.js dan Express. API itu pintu",
                    "    yang dipakai program lain untuk minta atau mengirim data.",
                    "  - Aplikasi ponsel pakai React Native.",
                    "  - Aplikasi desktop pakai Electron. VS Code juga dibikin pakai",
                    "    Electron.",
                    "",
                    "Ada tiga cara umum menjalankan JavaScript:",
                    "  1. Console browser. Tekan F12, buka tab Console, lalu ketik kodenya",
                    "     langsung di situ.",
                    "  2. Berkas HTML. Tulis kodenya di antara <script> dan </script>, atau",
                    "     panggil berkas terpisah pakai <script src='file.js'>.",
                    "  3. Node.js, untuk menjalankan JavaScript di luar browser. Perintahnya",
                    "     node nama_file.js",
                    "",
                    "Contoh kode di aplikasi ini dijalankan pakai node. Artinya, objek yang",
                    "cuma ada di browser (document, alert, localStorage) nggak ada di sini.",
                    "Sebaliknya, objek khas Node (process, require) nggak ada di browser.",
                    "Nggak ada satu lingkungan pun yang punya keduanya sekaligus. Jadi kalau",
                    "sebuah contoh menyebut document, contoh itu memang ditulis untuk",
                    "browser. Kodenya nggak salah.",
                ]
            },
            {
                "heading": "Program pertama (jalankan dengan: node hello.js)",
                "code": """console.log("Halo Dunia!");
console.log("Aku sedang belajar JavaScript.");"""
            },
            {
                "heading": "Titik koma, aturan dasar, dan komentar",
                "body": [
                    "console.log(...) adalah fungsi bawaan untuk menampilkan output, yaitu",
                    "tulisan yang muncul waktu program dijalankan.",
                    "",
                    "Titik koma (;) di akhir baris boleh nggak ditulis. JavaScript punya",
                    "aturan bernama Automatic Semicolon Insertion yang menambahkannya",
                    "sendiri. Tapi biasakan tetap menulisnya. Kodemu jadi seragam, dan kamu",
                    "terhindar dari bug halus yang baru kelihatan waktu program berperilaku",
                    "aneh.",
                    "",
                    "Aturan dasar menulis JavaScript:",
                    "  1. Huruf besar dan kecil dibedakan (case-sensitive). nama dan Nama",
                    "     dianggap dua nama yang beda.",
                    "  2. Blok kode dibungkus kurung kurawal { }, mirip Java dan C.",
                    "  3. Komentar adalah catatan yang dilewati waktu program jalan.",
                    "     Komentar satu baris ditulis // teks",
                    "  4. Komentar banyak baris ditulis /* teks */",
                    "  5. Komentar dokumentasi ditulis /** teks */, dengan dua bintang di",
                    "     awal. Kamu bakal sering lihat bentuk ini di atas fungsi di kode",
                    "     nyata. Isinya punya aturan sendiri, namanya JSDoc, dan dibahas di",
                    "     materi 'Membaca Repo JavaScript Sungguhan'.",
                    "  6. Berkas JavaScript berakhiran .js",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setiap kali kamu klik \"Tambah ke keranjang\" di toko online dan angka di",
                    "ikon keranjang langsung naik tanpa halaman dimuat ulang, itu JavaScript",
                    "yang jalan di browser. Programmer juga sering membuka Console (F12)",
                    "untuk mencoba satu baris kode sebelum menaruhnya di berkas, dan memakai",
                    "node untuk skrip kecil di komputer, misalnya merapikan berkas laporan.",
                    "",
                    "Kasus kecil: berkas struk.js berisi tiga baris console.log untuk",
                    "mencetak nama toko, alamat, dan ucapan terima kasih. Waktu dijalankan",
                    "pakai node struk.js, yang tercetak cuma nama toko, lalu muncul",
                    "ReferenceError: Console is not defined.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca keluarannya dulu. Baris pertama sempat tercetak, jadi",
                    "     masalahnya ada di baris kedua. Program berhenti di baris yang",
                    "     error, dan baris sesudahnya nggak pernah dijalankan.",
                    "  2. Perhatikan nama yang disebut errornya: Console, dengan C besar.",
                    "     JavaScript membedakan huruf besar dan kecil, dan yang bawaan cuma",
                    "     console.",
                    "  3. Betulkan barisnya, lalu jalankan ulang:",
                    "      console.log(\"Toko Sumber Rejeki\");",
                    "      console.log(\"Jl. Merdeka No. 10\");",
                    "      console.log(\"Terima kasih sudah belanja\");",
                    "  4. Kasus pinggir: tanda kutip di baris ketiga lupa ditutup. Kali ini",
                    "     nggak ada satu baris pun yang tercetak. node memeriksa tulisan",
                    "     seluruh berkas dulu, lalu langsung berhenti dengan SyntaxError.",
                    "",
                    "Ingat: pesan \"is not defined\" selalu menyebut nama yang nggak dikenal.",
                    "Bandingkan huruf demi huruf dengan nama yang kamu maksud.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel (var, let, const) & Tipe Data",
        "sections": [
            {
                "body": [
                    "Variabel itu nama untuk menyimpan sebuah nilai, mirip label di toples.",
                    "JavaScript punya tiga cara bikin variabel: var, let, dan const. Bedanya",
                    "perlu kamu pahami dari awal, soalnya salah pilih di sini sering jadi",
                    "sumber bug.",
                    "",
                    "  - var adalah cara lama, dari sebelum ES6 (versi JavaScript tahun",
                    "    2015). Variabel var berlaku di seluruh fungsi (function-scoped) dan",
                    "    boleh dideklarasikan ulang, artinya dibikin lagi dengan nama yang",
                    "    sama. Hindari var di kode baru.",
                    "  - let adalah cara modern untuk variabel yang nilainya bakal berubah.",
                    "    Variabel let cuma dikenal di dalam kurung kurawal { } terdekat",
                    "    (block-scoped).",
                    "  - const dipakai untuk nama yang nggak akan diisi ulang. Sama seperti",
                    "    let, const juga block-scoped. Pakai const sebagai pilihan pertama,",
                    "    lalu ganti ke let kalau ternyata nilainya memang perlu diubah.",
                    "",
                    "  const nama = \"Andi\";      // tidak bisa di-assign ulang",
                    "  let umur = 20;             // bisa diubah: umur = 21;",
                    "",
                    "Hati-hati dengan kata \"konstan\". Yang dikunci const cuma penugasan",
                    "ulangnya, yaitu memasang nilai baru ke nama itu pakai tanda =. Isinya",
                    "nggak ikut dikunci. Untuk array (daftar nilai) dan object (kumpulan",
                    "nilai bernama), isinya tetap boleh berubah:",
                    "",
                    "  const arr = [];",
                    "  arr.push(1);      // SAH - arr masih menunjuk array yang sama",
                    "  arr = [1];        // TypeError: Assignment to constant variable.",
                    "",
                    "Kenapa di situ ditulis \"menunjuk\" dan bukan \"berisi\" dibahas di materi",
                    "'Nilai vs Referensi & Menyalin Data'. Untuk sekarang belum perlu",
                    "dipahami.",
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
                "heading": "Beda null dan undefined serta template literal",
                "body": [
                    "Beda null dan undefined:",
                    "  - undefined artinya variabelnya sudah dideklarasikan, tapi belum diisi",
                    "    nilai apa pun.",
                    "  - null artinya programmer sengaja mengisinya dengan \"kosong\" atau",
                    "    \"nggak ada\".",
                    "",
                    "Komentar di kode atas bilang JS nggak membedakan int dan float. Int itu",
                    "bilangan bulat, float itu bilangan berkoma. Di JavaScript, semua angka,",
                    "termasuk 20 dan 7, disimpan sebagai float 64-bit. Akibatnya 0.1 + 0.2",
                    "nggak persis 0.3, dan bilangan bulat punya batas aman. Rinciannya ada di",
                    "materi 'Angka: Konversi Tipe, Math, dan Presisi Desimal'.",
                    "",
                    "Aturan memberi nama variabel:",
                    "  1. Boleh pakai huruf, angka, _, dan $, tapi nggak boleh diawali angka.",
                    "  2. Kebiasaan di JavaScript: variabel dan fungsi ditulis camelCase,",
                    "     yaitu kata kedua dan seterusnya diawali huruf besar (jumlahSiswa).",
                    "  3. Konstanta global sering ditulis UPPER_SNAKE_CASE, misalnya",
                    "     MAX_SIZE.",
                    "",
                    "Template literal adalah cara modern menggabungkan teks. Teksnya",
                    "dibungkus backtick (`), dan nilai variabel bisa diselipkan pakai ${...}:",
                    "",
                    "  const nama = \"Andi\"; const umur = 20;",
                    "  console.log(`Nama saya ${nama}, umur ${umur} tahun`);",
                    "  console.log(`Tahun depan: ${umur + 1}`);   // bisa ekspresi",
                    "",
                    "Di dalam ${...} boleh ada ekspresi, misalnya umur + 1. Template literal",
                    "juga boleh ditulis beberapa baris langsung, tanpa karakter escape",
                    "khusus.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di aplikasi kasir, ada nilai yang tetap selama satu transaksi, misalnya",
                    "nama pembeli dan harga satuan barang, dan ada yang terus berubah,",
                    "misalnya jumlah barang yang discan. Programmer memakai const untuk yang",
                    "tetap dan let untuk yang berubah, jadi orang yang membaca kodenya",
                    "langsung tahu mana yang boleh diisi ulang. Kolom yang sengaja",
                    "dikosongkan, seperti kode voucher yang belum dipakai, diisi null.",
                    "",
                    "Kasus kecil: Sari membeli 3 bungkus mi instan seharga Rp 3.500",
                    "sebungkus dan belum memakai voucher. Cetak satu baris ringkasan",
                    "belanjanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan yang tetap dari yang berubah. Nama pembeli dan harga",
                    "     satuan nggak berubah selama transaksi, jadi pakai const. Jumlah",
                    "     bisa ditambah kasir, jadi pakai let.",
                    "  2. Voucher belum dipakai artinya sengaja kosong. Isi dengan null,",
                    "     jangan dibiarkan undefined, supaya jelas itu keputusan dan bukan",
                    "     kelupaan.",
                    "  3. Rangkai keluarannya pakai template literal:",
                    "      const pembeli = \"Sari\";",
                    "      const harga = 3500;",
                    "      let jumlah = 3;",
                    "      let voucher = null;",
                    "      console.log(`${pembeli}: ${jumlah} bungkus, Rp ${harga * jumlah}`);",
                    "     Hasilnya satu baris: Sari: 3 bungkus, Rp 10500.",
                    "  4. Kasus pinggir: kasir menambah satu bungkus lagi. jumlah = 4 jalan",
                    "     karena jumlah dibuat pakai let. Kalau tadi kamu pakai const, baris",
                    "     itu berhenti dengan TypeError: Assignment to constant variable.",
                ]
            },
        ],
    },
    {
        "title": "3. Operator",
        "sections": [
            {
                "body": [
                    "Operator aritmatika, yaitu tanda untuk berhitung:",
                    "  +  penjumlahan    -  pengurangan",
                    "  *  perkalian      /  pembagian (SELALU desimal jika perlu)",
                    "  %  modulus        ** pangkat (ES2016+)",
                    "  ++ increment      -- decrement",
                    "",
                    "Perhatikan operator + di JavaScript. Hasilnya tergantung tipe nilainya:",
                    "  5 + 3        -> 8        (angka + angka = angka)",
                    "  \"5\" + 3      -> \"53\"     (string + angka = STRING, digabung!)",
                    "  5 + \"3\"      -> \"53\"     (sama, otomatis jadi string)",
                    "  \"5\" - 3      -> 2        (- , *, / otomatis convert ke angka)",
                    "",
                    "Kejadian ini namanya type coercion: JavaScript mengubah tipe nilai",
                    "secara otomatis. Ini sering jadi sumber bug di kode pemula.",
                ]
            },
            {
                "body": [
                    "JavaScript punya dua jenis operator perbandingan:",
                    "  - == membandingkan secara longgar (loose). Kalau tipenya beda,",
                    "    nilainya diubah dulu (type coercion), baru dibandingkan.",
                    "  - === membandingkan secara ketat (strict). Tipenya nggak diubah, jadi",
                    "    beda tipe berarti nggak sama.",
                    "  - Untuk \"nggak sama\" ada pasangannya: != yang longgar dan !== yang",
                    "    ketat.",
                    "",
                    "  5 == \"5\"    -> true   (\"5\" di-convert jadi angka dulu)",
                    "  5 === \"5\"   -> false  (beda tipe: number vs string)",
                    "  null == undefined   -> true",
                    "  null === undefined  -> false",
                    "",
                    "Ingat: selalu pakai === dan !==. Hindari == dan !=, karena cara mereka",
                    "mengubah tipe sering bikin bingung.",
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
                "heading": "Operator ??=, obj?.[key], dan bitwise",
                "body": [
                    "Ada tiga operator turunan yang belum muncul di atas. Ketiganya sering",
                    "ketemu di kode sehari-hari.",
                    "",
                    "1. Logical assignment (ES2021). Operator ini menggabungkan operator",
                    "   logika dengan tanda sama dengan, jadi \"isi kalau perlu\" cukup ditulis",
                    "   satu baris:",
                    "     a ??= b   isi a HANYA kalau a null/undefined",
                    "     a ||= b   isi a kalau a falsy (0 dan \"\" ikut kena)",
                    "     a &&= b   isi a HANYA kalau a truthy",
                    "   Falsy artinya nilai yang dianggap false oleh if, misalnya 0 dan \"\".",
                    "   Truthy kebalikannya.",
                    "",
                    "2. Optional chaining punya bentuk lain selain titik yang kamu lihat di",
                    "   atas:",
                    "     obj?.[key]     indeks opsional, untuk nama key yang dinamis",
                    "   Ada satu bentuk lagi, fn?.(), yang memanggil sebuah fungsi hanya",
                    "   kalau fungsinya ada. Bentuk itu baru kepakai sesudah kamu kenal",
                    "   fungsi, jadi contohnya ada nanti di materi \"Function: Declaration,",
                    "   Expression & Arrow Function\".",
                    "",
                    "3. Operator bitwise: &  |  ^  ~  <<  >>  >>>",
                    "   Operator ini bekerja pada bit, yaitu angka 0 dan 1 penyusun sebuah",
                    "   bilangan. Kamu jarang menulisnya sendiri, tapi perlu bisa",
                    "   mengenalinya. Kalau nggak, x | 0 di kode orang bakal kebaca sebagai",
                    "   OR biasa, dan artinya salah total.",
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
console.log(user.alamat?.[kunci]);  // undefined   aman, bukan TypeError"""
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

// x |= 0 memaksa angka kembali ke bulat 32-bit bertanda. Bentuk ini sering
// ditemui di fungsi hash kecil, supaya angkanya tidak membengkak.
let hash = 2147483647 + 1;          // 2147483648, lewat batas 32-bit
hash |= 0;                          // paksa kembali ke 32-bit
console.log(hash);                  // -2147483648"""
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Operator ada di setiap hitungan aplikasi: total belanja, sisa kuota",
                    "internet, atau syarat \"umur minimal 17 tahun\" di formulir pendaftaran.",
                    "Masalah yang sering muncul di toko online ada di nilai cadangan",
                    "(default): stok 0 yang harusnya tampil 0 malah diganti teks cadangan,",
                    "karena kodenya pakai ||.",
                    "",
                    "Kasus kecil: data dari gudang punya field stok. Kalau field itu belum",
                    "diisi (undefined), tampilkan \"belum dicek\". Kalau isinya 0, tampilkan",
                    "angka 0. Ada tiga barang: { stok: 12 }, { stok: 0 }, dan {}.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan nilai mana yang dianggap kosong. Di sini cuma undefined",
                    "     dan null. Stok 0 itu data sah.",
                    "  2. Pilih operatornya. || menganggap 0 kosong, jadi stok 0 ikut",
                    "     berubah jadi \"belum dicek\". ?? cuma menganggap null dan undefined",
                    "     kosong.",
                    "  3. Coba ketiganya:",
                    "      const a = { stok: 12 }, b = { stok: 0 }, c = {};",
                    "      console.log(a.stok ?? \"belum dicek\");   // 12",
                    "      console.log(b.stok ?? \"belum dicek\");   // 0",
                    "      console.log(c.stok ?? \"belum dicek\");   // belum dicek",
                    "  4. Kasus pinggir: data barangnya sendiri nggak ada. Kalau barang",
                    "     bernilai null, barang.stok melempar TypeError. Tulis",
                    "     barang?.stok ?? \"belum dicek\" supaya aman di dua keadaan itu.",
                    "",
                    "Jebakan: kebalikannya juga ada. Nama tampilan yang kosong (\"\") memang",
                    "mau diganti \"Tamu\", jadi di situ || yang tepat. ?? membiarkan teks",
                    "kosong lolos.",
                ]
            },
        ],
    },
    {
        "title": "4. Angka: Konversi Tipe, Math, dan Presisi Desimal",
        "sections": [
            {
                "body": [
                    "Di materi Operator kamu sudah lihat JavaScript mengubah tipe sendiri:",
                    "\"5\" + 3 jadi \"53\". Itu coercion otomatis, dan hasilnya sering nggak",
                    "sesuai keinginan. Di kode nyata, kita hampir selalu mengubah tipe",
                    "dengan sengaja. Namanya konversi eksplisit.",
                    "",
                    "Ini penting karena hampir semua data yang masuk ke program berupa",
                    "string (teks):",
                    "  - isi kotak input di halaman web           -> string",
                    "  - argumen dari terminal (process.argv)     -> string",
                    "  - isi berkas teks dan balasan dari server  -> string",
                    "",
                    "Kalau lupa diubah jadi angka, operator + bakal menggabungkan teks,",
                    "bukan menjumlahkan angka. Bug ini nggak memunculkan error apa pun.",
                    "Hasilnya cuma salah, tanpa tanda apa-apa.",
                    "",
                    "Alat konversi yang perlu kamu kenal:",
                    "  Number(x)        teks -> angka. Teksnya harus bersih total, kalau",
                    "                   nggak hasilnya NaN.",
                    "  parseInt(x, 10)  baca angka bulat dari depan, berhenti di karakter",
                    "                   aneh.",
                    "  parseFloat(x)    sama, tapi bagian desimalnya ikut terbaca.",
                    "  String(x)        apa pun -> teks.",
                    "  x.toString(2)    angka -> teks dalam basis lain (2 biner,",
                    "                   16 heksadesimal).",
                    "  Boolean(x)       apa pun -> true/false (truthy/falsy dibahas di",
                    "                   materi Percabangan).",
                    "  +x  dan  !!x     bentuk singkat dari Number(x) dan Boolean(x).",
                    "",
                    "Angka 10 di parseInt(x, 10) itu radix, alias basis bilangan. Sekarang",
                    "boleh nggak ditulis, tapi biasakan menulisnya. Suatu hari teksnya bisa",
                    "berbentuk \"0x1f\" atau datang dari kode lama, dan kamu nggak perlu",
                    "menebak basis mana yang dipakai.",
                    "",
                    "Number(\"12abc\") memberi NaN, sedangkan parseInt(\"12abc\") memberi 12.",
                    "NaN artinya Not a Number, \"bukan angka\". Bedanya memang disengaja, dan",
                    "salah pilih bisa bikin bug sungguhan:",
                    "  - Pakai Number kalau datanya harus angka murni, misalnya harga,",
                    "    jumlah, atau umur. Data kotor langsung ketahuan sebagai NaN, dan",
                    "    memang itu yang kita mau.",
                    "  - Pakai parseInt atau parseFloat kalau angkanya memang nempel dengan",
                    "    satuan, misalnya \"16px\" dari CSS atau \"250 gram\" dari teks yang",
                    "    diketik orang.",
                    "  - Jangan pakai parseInt untuk memvalidasi. parseInt(\"7 ekor kambing\")",
                    "    tetap 7, jadi input ngawur lolos gitu aja.",
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
                "heading": "NaN, Infinity, pembulatan Math, dan angka acak",
                "body": [
                    "NaN merepotkan karena dia menular. Sekali satu nilai jadi NaN, semua",
                    "hitungan sesudahnya ikut jadi NaN. Yang kelihatan di layar cuma \"NaN\"",
                    "di ujung, jauh dari baris yang salah. Kalau kamu ketemu NaN, telusuri",
                    "ke belakang sampai ketemu konversi pertama yang gagal.",
                    "",
                    "NaN === NaN hasilnya false, dan itu disengaja. NaN artinya \"angka yang",
                    "nggak diketahui\", dan dua hal yang sama-sama nggak diketahui nggak bisa",
                    "disebut sama. Akibatnya, jangan pernah ngecek NaN pakai === atau ==.",
                    "Ada dua fungsi untuk ngecek NaN:",
                    "  Number.isNaN(x)  -> true hanya kalau x memang NaN. Pakai yang ini.",
                    "  isNaN(x)         -> versi global, mengonversi x dulu. isNaN(\"dua\")",
                    "                      true, padahal \"dua\" itu string. Menyesatkan,",
                    "                      hindari.",
                    "",
                    "Infinity (tak hingga) juga bertipe number. Di Python, atau di Java",
                    "untuk bilangan bulat, pembagian dengan nol bikin error. Di JavaScript",
                    "nggak. Programmu jalan terus membawa nilai tak hingga, sampai akhirnya",
                    "muncul di layar sebagai \"Infinity\". Penjaganya:",
                    "  Number.isFinite(x)   -> false untuk Infinity, -Infinity, dan NaN",
                    "                          sekaligus.",
                    "",
                    "Math adalah objek bawaan yang berisi fungsi matematika. Kamu nggak",
                    "perlu import apa pun, dan Math nggak pernah dibikin pakai new. Isinya",
                    "langsung dipanggil, misalnya Math.abs(-9).",
                    "",
                    "Ada empat fungsi pembulatan. Bedanya baru kelihatan di angka minus:",
                    "  Math.floor(x)   ke bawah        floor(4.7) = 4    floor(-4.7) = -5",
                    "  Math.ceil(x)    ke atas         ceil(4.1)  = 5    ceil(-4.1)  = -4",
                    "  Math.round(x)   ke terdekat     round(4.5) = 5    round(-4.5) = -4",
                    "  Math.trunc(x)   buang desimal   trunc(4.7) = 4    trunc(-4.7) = -4",
                    "",
                    "Jebakan: Math.round(-4.5) hasilnya -4, bukan -5, karena angka .5 selalu",
                    "dibulatkan ke arah plus. Selain itu, floor dan trunc cuma sama selama",
                    "angkanya positif.",
                    "",
                    "Fungsi lainnya: Math.abs (nilai mutlak), Math.sqrt (akar), Math.pow(a, b)",
                    "yang sama dengan operator a ** b, dan Math.PI. Math.max dan Math.min",
                    "menerima angka satu per satu, bukan array. Jadi array harus dibongkar",
                    "dulu pakai spread (...), yang dibahas di materi Array:",
                    "  Math.max(...nilai)   benar",
                    "  Math.max(nilai)      NaN -- array-nya dicoba diubah jadi satu angka",
                    "",
                    "Math.random() memberi pecahan acak dari 0 sampai kurang dari 1. Ini",
                    "cara paling umum bikin angka acak di JavaScript. Untuk keperluan",
                    "keamanan, misalnya token login, ada crypto.getRandomValues(). Resep",
                    "bakunya:",
                    "  Math.floor(Math.random() * 6)              -> 0..5",
                    "  Math.floor(Math.random() * 6) + 1          -> 1..6, sebuah dadu",
                    "  Math.floor(Math.random() * arr.length)     -> indeks acak sebuah array",
                    "",
                    "Selalu pakai floor, jangan round. Kalau pakai round, angka paling ujung",
                    "cuma dapat setengah peluang dibanding angka di tengah. Contoh di materi",
                    "ini nggak pakai random, karena outputnya harus bisa ditebak supaya bisa",
                    "kamu cocokkan.",
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
                "heading": "Presisi float, uang, dan batas bilangan bulat",
                "body": [
                    "Kenapa 0.1 + 0.2 nggak sama dengan 0.3? Penyebabnya, JavaScript cuma",
                    "punya satu tipe angka, yaitu float 64-bit. Nggak ada int terpisah",
                    "seperti di Java atau C. Bilangan bulat dan desimal disimpan dengan cara",
                    "yang sama.",
                    "",
                    "Komputer menyimpan angka dalam basis dua. Di basis dua, 0.1 adalah",
                    "pecahan yang nggak pernah habis, sama seperti 1/3 = 0,3333... di basis",
                    "sepuluh yang kita pakai sehari-hari. Yang tersimpan sudah dibulatkan",
                    "sedikit, dan sisa pembulatan itu muncul waktu dua angka dijumlahkan.",
                    "Python, Java, dan C juga begitu, jadi ini bukan bug JavaScript. Yang",
                    "keliru cuma satu: mengira angka desimal tersimpan persis seperti yang",
                    "kita tulis.",
                    "",
                    "Akibat yang paling sering bikin bingung: membandingkan uang pakai ===",
                    "gagal, padahal di layar angkanya kelihatan sama. Bandingkan selisihnya:",
                    "  if (Math.abs(total - 0.3) < 1e-9) { ... }   // benar",
                    "  if (total === 0.3) { ... }                  // rapuh, hindari",
                    "",
                    "Ada tiga cara menangani desimal, masing-masing untuk keperluan beda:",
                    "  1. toFixed(2) dipakai untuk ditampilkan aja. Hasilnya string, bukan",
                    "     number. Ini jebakan besar: kalau hasilnya dijumlahkan, yang terjadi",
                    "     penggabungan teks. Bungkus pakai Number(...) kalau nilainya masih",
                    "     mau dihitung lagi. toFixed juga membulatkan, jadi jangan dipakai",
                    "     kalau kamu butuh angka utuh.",
                    "  2. Math.round(x * 100) / 100 membulatkan ke 2 desimal, dan hasilnya",
                    "     tetap number. Pakai ini untuk nilai yang masih ikut perhitungan",
                    "     berikutnya.",
                    "  3. Simpan uang dalam satuan terkecil sebagai bilangan bulat. Harga",
                    "     Rp 19.999 disimpan sebagai 19999, harga 4,50 dolar disimpan",
                    "     sebagai 450 sen. Formatnya baru dipasang waktu ditampilkan. Sistem",
                    "     pembayaran sungguhan pakai cara ini, karena bilangan bulat nggak",
                    "     punya sisa pembulatan sama sekali.",
                    "",
                    "Batas bilangan bulat: Number.MAX_SAFE_INTEGER = 9007199254740991,",
                    "sekitar 9 kuadriliun. Di atas angka itu, dua angka yang beda bisa",
                    "tersimpan jadi angka yang sama. Nggak ada peringatan apa pun, dan",
                    "program tetap jalan dengan data yang salah.",
                    "",
                    "Kalau memang butuh angka lebih besar, misalnya ID dari database besar,",
                    "stempel waktu nanodetik, atau saldo kripto, pakai BigInt. Angka BigInt",
                    "ditulis dengan akhiran n, dan tipenya sudah disinggung di materi",
                    "Variabel & Tipe Data. Syaratnya, BigInt nggak boleh dicampur langsung",
                    "dengan number biasa dalam satu operasi. Salah satunya harus dikonversi",
                    "dulu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi patungan (split bill), kasir, dan laporan keuangan UMKM",
                    "menghitung rupiah dari angka yang datang sebagai teks: isian form,",
                    "kolom spreadsheet, atau balasan server. Dua masalah dari materi ini",
                    "sering muncul di sana: teks yang lupa diubah jadi angka, dan pecahan",
                    "rupiah yang nggak bisa dibayar.",
                    "",
                    "Kasus kecil: tagihan makan bersama Rp 100.000 dibagi 3 orang. Dua",
                    "angka itu diketik di kotak isian, jadi datangnya sebagai teks \"100000\"",
                    "dan \"3\". Tiap orang harus membayar rupiah bulat, dan uang yang",
                    "terkumpul nggak boleh kurang dari tagihan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ubah masukannya jadi angka pakai Number. Isinya harus angka murni,",
                    "     jadi isian ngawur seperti \"tiga\" langsung jadi NaN dan ketahuan.",
                    "  2. Hitung pembagiannya: 100000 / 3 = 33333.333..., dan nggak ada",
                    "     pecahan rupiah sekecil itu.",
                    "  3. Pilih arah pembulatan. Math.floor memberi 33333, terkumpul 99999,",
                    "     kurang Rp 1. Math.ceil memberi 33334, terkumpul 100002, lebih",
                    "     Rp 2. Untuk tagihan, yang aman ke atas:",
                    "      const tagihan = Number(\"100000\");",
                    "      const orang = Number(\"3\");",
                    "      const bayar = Math.ceil(tagihan / orang);",
                    "      console.log(bayar, bayar * orang - tagihan);   // 33334 2",
                    "  4. Kasus pinggir: kotak jumlah orang dibiarkan kosong. Number(\"\")",
                    "     memberi 0, dan 100000 / 0 jadi Infinity tanpa error. Periksa",
                    "     Number.isFinite(bayar) sebelum hasilnya ditampilkan.",
                ]
            },
        ],
    },
    {
        "title": "5. Percabangan (if / else / switch)",
        "sections": [
            {
                "body": [
                    "Percabangan artinya program memilih jalan sesuai kondisi. Sintaks",
                    "if-else di JavaScript mirip Java dan C:",
                    "  if (kondisi) {",
                    "      // jalankan jika true",
                    "  } else if (kondisi2) {",
                    "      // jalankan jika kondisi2 true",
                    "  } else {",
                    "      // jalankan jika semua false",
                    "  }",
                    "",
                    "Di dalam if, setiap nilai dianggap true atau false. Nilai yang dianggap",
                    "false disebut falsy, sisanya disebut truthy. Nilai falsy yang perlu",
                    "kamu ingat: 0, \"\", null, undefined, NaN, dan false. Ada juga -0 dan 0n",
                    "(BigInt nol), tapi jarang ketemu.",
                    "",
                    "Semua nilai lain truthy, termasuk \"0\", [] (array kosong), dan {}",
                    "(object kosong). Tiga yang terakhir ini sering bikin kaget:",
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
                    "Kenapa tiap case di atas diakhiri break? Tanpa break, program nggak",
                    "berhenti di case yang cocok. Dia jalan terus ke case-case berikutnya",
                    "sampai ketemu break atau sampai switch-nya habis. Kejadian ini namanya",
                    "fallthrough, artinya \"jatuh terus\".",
                    "",
                    "Fallthrough bisa jadi jebakan, tapi juga sering dipakai dengan sengaja.",
                    "Beberapa case yang ditumpuk tanpa isi di antaranya artinya \"beberapa",
                    "nilai, satu tindakan\". Jangan dibaca sebagai case kosong yang nggak",
                    "ngapa-ngapain.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua aturan bisnis berbentuk percabangan: ongkir gratis kalau",
                    "belanja minimal sekian, tarif parkir beda untuk motor dan mobil.",
                    "Aplikasi rapor sekolah juga mengubah nilai angka jadi predikat huruf",
                    "dengan rantai if dan else if.",
                    "",
                    "Kasus kecil: ubah nilai rapor jadi predikat. Nilai 90 ke atas A, 80",
                    "sampai 89 B, 70 sampai 79 C, dan di bawah 70 D. Coba dengan 85, 70,",
                    "dan 69.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya sebagai rentang yang nggak tumpang tindih, lalu",
                    "     urutkan dari batas tertinggi.",
                    "  2. Pakai if dan else if. Karena dicek berurutan, cabang kedua cukup",
                    "     menulis nilai >= 80, sebab nilai 95 sudah ditangkap cabang pertama.",
                    "      const nilai = 85;",
                    "      let predikat;",
                    "      if (nilai >= 90) predikat = \"A\";",
                    "      else if (nilai >= 80) predikat = \"B\";",
                    "      else if (nilai >= 70) predikat = \"C\";",
                    "      else predikat = \"D\";",
                    "  3. Uji tepat di batasnya: 70 harus C dan 69 harus D. Salah tulis >",
                    "     dan >= paling sering terjadi di sini.",
                    "  4. Kasus pinggir: nilai siswa belum diisi (undefined). Semua",
                    "     perbandingan dengan undefined menghasilkan false, jadi siswa itu",
                    "     dapat D tanpa ada error. Tambahkan cabang paling atas untuk nilai",
                    "     yang belum ada.",
                    "",
                    "Ingat: switch membandingkan pakai ===, jadi cocok untuk nilai yang",
                    "persis seperti kode hari, dan kurang cocok untuk rentang seperti ini.",
                ]
            },
        ],
    },
    {
        "title": "6. Perulangan (for, while, for...of, for...in)",
        "sections": [
            {
                "body": [
                    "Perulangan (loop) adalah cara menjalankan kode yang sama berkali-kali.",
                    "JavaScript punya lima jenis:",
                    "1. for klasik, mirip Java dan C:",
                    "     for (let i = 0; i < 5; i++) { ... }",
                    "2. while: cek kondisi dulu, baru jalan.",
                    "     while (kondisi) { ... }",
                    "3. do...while: jalan dulu, baru cek kondisi.",
                    "     do { ... } while (kondisi);",
                    "4. for...of: mengambil nilai satu per satu dari iterable, yaitu sesuatu",
                    "   yang isinya bisa diambil berurutan, seperti array, string, Map, dan",
                    "   Set.",
                    "     for (const item of array) { ... }",
                    "5. for...in: mengambil key (nama property) atau index dari object atau",
                    "   array.",
                    "     for (const key in object) { ... }",
                    "   Untuk array, lebih baik pakai for...of atau .forEach.",
                    "",
                    "Hati-hati dengan for...in: dia ikut mengambil property warisan dari",
                    "prototype, selain property milik object itu sendiri. Prototype itu",
                    "object induk tempat sebuah object mewarisi sifat. Penyaringnya",
                    "Object.hasOwn(obj, key), yang dibahas di materi 'Object & Destructuring'.",
                    "",
                    "Ada dua hal di contoh berikut yang mungkin belum kamu kenal:",
                    "  - process.stdout.write(teks) mencetak tanpa menambah baris baru.",
                    "    Beda dengan console.log, yang selalu menambahkannya. process cuma",
                    "    ada di Node. Di Console browser hasilnya 'process is not defined'.",
                    "    Lebih lengkapnya di materi 'Node.js: Process, Berkas, dan Path'.",
                    "  - buah.entries() memberi pasangan [index, nilai] untuk tiap elemen.",
                    "    Bentuk const [index, b] di sebelah kiri namanya destructuring, dan",
                    "    dibahas di materi 'Array & Method Array (map/filter/reduce)'.",
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
                    "break menghentikan loop, continue melompat ke putaran berikutnya.",
                    "Keduanya selalu mengenai loop terdalam tempat mereka ditulis. Di loop",
                    "bersarang (loop di dalam loop), sering bukan itu yang kita mau.",
                    "Menemukan hasil di loop dalam nggak ikut menghentikan loop luar.",
                    "",
                    "Jalan keluarnya label, yaitu nama yang ditempel di depan sebuah loop,",
                    "lalu disebut oleh break atau continue:",
                    "",
                    "  namaLabel: for (...) { for (...) { break namaLabel; } }",
                    "",
                    "Label ditulis 'nama:' persis sebelum kata for atau while. Label bukan",
                    "variabel, jadi nggak perlu dideklarasikan. Pakai seperlunya aja. Dua",
                    "loop bersarang masih gampang dibaca. Kalau sudah empat, itu tanda",
                    "kodenya perlu dipecah jadi fungsi sendiri.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Begitu datanya lebih dari satu, loop muncul: mencetak semua baris",
                    "struk, menjumlah setoran tabungan selama seminggu, atau mengirim",
                    "pengingat ke setiap siswa yang belum bayar SPP.",
                    "",
                    "Kasus kecil: bendahara kelas mencatat setoran tabungan lima hari:",
                    "[5000, 0, 2000, 10000, 3000]. Ia mau tahu totalnya dan hari ke berapa",
                    "pertama kali nggak ada setoran.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya array lima angka, satu per hari. Keluarannya dua: total",
                    "     dan nomor hari pertama yang setorannya 0.",
                    "  2. Satu kali jalan cukup untuk keduanya. Pakai for...of dengan",
                    "     entries() supaya dapat indeks dan nilainya sekaligus:",
                    "      const setoran = [5000, 0, 2000, 10000, 3000];",
                    "      let total = 0, hariKosong = -1;",
                    "      for (const [i, s] of setoran.entries()) {",
                    "        total += s;",
                    "        if (s === 0 && hariKosong === -1) hariKosong = i + 1;",
                    "      }",
                    "  3. Indeks array mulai dari 0, jadi ditambah 1 sebelum disebut hari.",
                    "     Hasilnya total 20000 dan hari ke-2.",
                    "  4. Kasus pinggir: semua hari ada setorannya. hariKosong tetap -1, dan",
                    "     itu tanda untuk menulis \"setiap hari ada setoran\", jangan",
                    "     \"hari ke-0\".",
                    "",
                    "Jebakan: break begitu ketemu 0 memang menghemat putaran, tapi totalnya",
                    "jadi cuma menjumlah sampai hari kedua. break menghentikan seluruh loop,",
                    "jadi pakai kalau sisa data memang nggak dibutuhkan lagi.",
                ]
            },
        ],
    },
    {
        "title": "7. String & Template Literal",
        "sections": [
            {
                "body": [
                    "String adalah teks. Di JavaScript, string boleh ditulis pakai kutip",
                    "tunggal '...', kutip ganda \"...\", atau backtick `...`. Bentuk backtick",
                    "namanya template literal, cara modern yang disarankan.",
                    "",
                    "String bersifat immutable, artinya nggak bisa diubah langsung per",
                    "karakter. Kalau mau isinya beda, kamu bikin string baru.",
                    "",
                    "Mengambil satu karakter (indexing) dan mengambil potongan (slicing):",
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
                    "Daftar method di atas baru separuh. Method itu fungsi yang nempel pada",
                    "sebuah nilai, dipanggil pakai titik, misalnya s.trim(). Beberapa",
                    "method yang belum disebut ternyata pasangan dari yang sudah ada. Kalau",
                    "belum kenal, kamu bakal nulis loop panjang untuk hal yang bisa selesai",
                    "dalam satu baris:",
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
                    "Jebakan: s.replace(\"a\", \"b\") dengan string biasa cuma mengganti",
                    "kemunculan pertama, tanpa peringatan apa pun. Solusinya replaceAll().",
                    "Alasannya dibahas lengkap di materi 'Regular Expression: Mencari Pola",
                    "dalam Teks'.",
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
                    "Ada satu bentuk lagi yang kelihatan aneh kalau belum pernah dijelaskan:",
                    "nama fungsi yang nempel langsung di depan backtick.",
                    "",
                    "  nama`teks ${nilai} lagi`",
                    "",
                    "Itu pemanggilan fungsi, tanpa tanda kurung sama sekali. Namanya tagged",
                    "template literal. Fungsinya menerima dua hal secara terpisah: array",
                    "berisi potongan-potongan teksnya, lalu nilai-nilai di dalam ${...}",
                    "sebagai rest parameter, yaitu parameter yang menampung sisa argumen.",
                    "Karena terpisah, fungsinya bebas mengolah nilai itu, misalnya",
                    "membungkusnya, meloloskannya (escape), atau menerjemahkannya.",
                    "",
                    "Kalau sudah kenal bentuk ini, baris-baris berikut jadi bisa kamu baca",
                    "waktu membuka proyek orang lain:",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir semua data dari pengguna berupa teks, dan teks dari manusia",
                    "jarang rapi: spasi di ujung, huruf kapital acak, panjang yang",
                    "beda-beda. Form pendaftaran merapikan nama sebelum disimpan, kotak",
                    "pencarian toko online menyamakan huruf besar-kecil, dan aplikasi kasir",
                    "menata nama barang dan harga supaya lurus di struk.",
                    "",
                    "Kasus kecil: misalkan printer strukmu muat 32 karakter per baris. Nama",
                    "barang harus rata kiri dan harganya rata kanan, misalnya \"Minyak",
                    "goreng 2L\" dengan harga 38000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya nama dan harga. Keluarannya satu baris yang panjangnya",
                    "     persis 32 karakter, dengan harga menempel di tepi kanan.",
                    "  2. Bagi lebarnya, misalnya 22 karakter untuk nama dan 10 untuk harga.",
                    "     padEnd mengisi spasi di kanan nama, padStart mengisi spasi di kiri",
                    "     harga:",
                    "      const nama = \"Minyak goreng 2L\";",
                    "      const harga = String(38000);",
                    "      const baris = nama.padEnd(22) + harga.padStart(10);",
                    "      console.log(baris);",
                    "      console.log(baris.length);   // 32",
                    "  3. Harga diubah jadi string dulu pakai String, karena padStart milik",
                    "     string. Angka nggak punya method itu, jadi (38000).padStart(10)",
                    "     berhenti dengan TypeError.",
                    "  4. Kasus pinggir: nama barang lebih dari 22 karakter. padEnd nggak",
                    "     memotong apa pun, jadi barisnya kepanjangan dan harganya terdorong",
                    "     keluar lebar struk. Potong dulu pakai nama.slice(0, 22).",
                ]
            },
        ],
    },
    {
        "title": "8. Tanggal & Waktu dengan Date",
        "sections": [
            {
                "body": [
                    "Hampir semua aplikasi nyata berurusan dengan waktu. Misalnya kolom",
                    "createdAt yang datang dari API, teks \"diposting 3 jam lalu\", umur,",
                    "tanggal jatuh tempo, atau mengukur lama sebuah proses. Di JavaScript,",
                    "semuanya diurus satu objek bawaan: Date.",
                    "",
                    "Ada tiga cara bikin Date:",
                    "  new Date()                      -> detik ini juga, saat dijalankan",
                    "  new Date(\"2026-03-17T08:30:00\") -> dari teks format ISO",
                    "  new Date(2026, 2, 17, 8, 30)    -> tahun, bulan, tanggal, jam, menit",
                    "",
                    "ISO itu format tanggal baku yang urutannya tahun-bulan-tanggal.",
                    "",
                    "Jebakan nomor satu: di bentuk angka, bulan dihitung mulai dari 0.",
                    "",
                    "  0 = Januari, 1 = Februari, 2 = Maret, ... 11 = Desember",
                    "",
                    "Jadi new Date(2026, 8, 6) itu 6 September, bukan 6 Agustus. Kesalahan",
                    "ini susah disadari, karena programnya nggak error dan hasilnya tetap",
                    "tanggal yang masuk akal, cuma meleset satu bulan. Tahun, tanggal, jam,",
                    "dan menit dihitung biasa. Cuma bulan yang mulai dari 0.",
                    "",
                    "Di balik layar, sebuah Date cuma menyimpan satu angka: jumlah milidetik",
                    "sejak 1 Januari 1970 pukul 00:00 UTC. Titik nol itu namanya epoch, dan",
                    "angkanya disebut timestamp.",
                    "  Date.now()               -> timestamp sekarang (number), tanpa",
                    "                              membuat objek Date",
                    "  tanggal.getTime()        -> timestamp dari sebuah objek Date",
                    "  new Date(1773711000000)  -> mengubah timestamp kembali jadi Date",
                    "",
                    "Timestamp dipakai di mana-mana karena bentuknya cuma angka. Gampang",
                    "disimpan di database, gampang dikirim lewat JSON, dan bisa dibandingkan",
                    "pakai < atau > untuk tahu mana yang lebih dulu.",
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
                "heading": "Date mutable, zona waktu, dan Invalid Date",
                "body": [
                    "Ada empat jebakan yang paling sering kena, plus cara menghindarinya:",
                    "1. Date itu mutable, artinya isinya bisa diubah. setDate, setMonth, dan",
                    "   setHours mengubah objek yang sudah ada, dan nggak bikin objek baru.",
                    "   Kalau objek itu juga dipegang variabel lain, variabel itu ikut",
                    "   berubah, sama seperti object dan array yang dioper lewat referensi.",
                    "   Kebiasaan yang aman: salin dulu, lalu geser salinannya aja.",
                    "     const baru = new Date(lama);",
                    "2. Zona waktu. Isi Date selalu UTC, tapi getDate, getHours, dan",
                    "   kawan-kawannya membacanya dalam zona waktu komputer yang",
                    "   menjalankan. Kode yang sama bisa menyebut tanggal berbeda di server",
                    "   Amerika dan di laptop Jakarta.",
                    "   Contohnya new Date(\"2026-03-17\"), yang cuma berisi tanggal tanpa",
                    "   jam. Teks itu dibaca sebagai tengah malam UTC. Di Jakarta itu 17",
                    "   Maret pukul 07:00, tapi di New York masih 16 Maret pukul 20:00, jadi",
                    "   getDate() di sana menjawab 16. Kalau jamnya penting, tulis jamnya.",
                    "   new Date(\"2026-03-17T00:00:00\") dibaca sebagai waktu lokal, bukan",
                    "   UTC. Tiap fungsi pembaca (getter) punya kembaran UTC: getUTCDate(),",
                    "   getUTCHours(), getUTCFullYear(), dan seterusnya.",
                    "3. Membaca teks tanggal yang nggak baku. Format yang dijamin sama di",
                    "   semua browser dan Node cuma ISO: \"2026-03-17\" dan",
                    "   \"2026-03-17T08:30:00\". Selain itu terserah mesinnya. \"17/03/2026\"",
                    "   jadi Invalid Date, sedangkan \"03/17/2026\" dibaca bulan dulu ala",
                    "   Amerika. Kalau datanya berformat lain, pecah sendiri pakai split()",
                    "   lalu susun:",
                    "     new Date(tahun, bulan - 1, tanggal)",
                    "4. Gagalnya nggak kelihatan. Tanggal ngawur menghasilkan Invalid Date",
                    "   tanpa error, dan semua hitungan sesudahnya jadi NaN yang menyebar",
                    "   ke mana-mana. Cek dulu:",
                    "     if (Number.isNaN(d.getTime())) { ... }",
                    "",
                    "Kode nyata sering pakai library, yaitu kumpulan kode siap pakai buatan",
                    "orang lain, seperti date-fns, Day.js, atau Luxon. Date sendiri",
                    "sanggup, tapi format tampilan, selisih \"berapa bulan\", zona waktu, dan",
                    "bahasa harus ditulis tangan berulang-ulang, dan sifat mutable-nya",
                    "gampang jadi bug. Library membungkus semua itu jadi satu baris, dan",
                    "objeknya immutable. JavaScript sendiri sedang menyiapkan pengganti",
                    "resmi bernama Temporal.",
                    "",
                    "Tetap kuasai Date lebih dulu. Semua library itu dibangun di atas Date,",
                    "dan tanggal yang datang dari API tetap berupa string ISO yang harus",
                    "kamu baca sendiri.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi perpustakaan menghitung denda keterlambatan, aplikasi cicilan",
                    "menentukan tanggal jatuh tempo, dan media sosial menulis \"3 jam lalu\".",
                    "Semuanya berangkat dari dua hal yang sama: menggeser tanggal dan",
                    "menghitung selisih dua tanggal dalam milidetik.",
                    "",
                    "Kasus kecil: perpustakaan sekolah meminjamkan buku selama 7 hari",
                    "dengan denda Rp 500 per hari terlambat. Buku dipinjam 25 Januari 2026",
                    "dan dikembalikan 5 Februari 2026.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat kedua tanggalnya pakai bentuk angka, dan ingat bulannya mulai",
                    "     dari 0: Januari 0, Februari 1.",
                    "  2. Hitung jatuh tempo dari salinan tanggal pinjam, supaya tanggal",
                    "     aslinya nggak ikut bergeser. setDate dengan angka lewat 31 membawa",
                    "     bulannya maju sendiri.",
                    "      const pinjam = new Date(2026, 0, 25);",
                    "      const kembali = new Date(2026, 1, 5);",
                    "      const tempo = new Date(pinjam);",
                    "      tempo.setDate(tempo.getDate() + 7);   // 1 Februari 2026",
                    "      const telat = Math.floor((kembali - tempo) / 86400000);",
                    "      console.log(telat, telat * 500);      // 4 2000",
                    "  3. Selisih dua Date berupa milidetik. Dibagi 86400000, yaitu jumlah",
                    "     milidetik dalam sehari, hasilnya jadi hari.",
                    "  4. Kasus pinggir: buku dikembalikan sebelum jatuh tempo. telat jadi",
                    "     negatif, dan denda minus nggak masuk akal. Pakai Math.max(0, telat)",
                    "     sebelum dikali tarif denda.",
                    "",
                    "Jebakan: jangan menulis const tempo = pinjam lalu memanggil setDate.",
                    "Date itu mutable, jadi tanggal pinjam ikut berubah jadi 1 Februari.",
                ]
            },
        ],
    },
    {
        "title": "9. Regular Expression: Mencari Pola dalam Teks",
        "sections": [
            {
                "body": [
                    "Regular expression (regex) adalah cara menuliskan pola teks.",
                    "includes() dan === bertanya \"apakah teksnya persis ini?\". Regex",
                    "bertanya \"apakah teksnya berbentuk seperti ini?\", misalnya empat angka,",
                    "tanda hubung, dua angka, tanda hubung, dua angka. Tanpa regex,",
                    "pertanyaan sesederhana \"apakah semua karakternya angka?\" butuh loop",
                    "dan belasan baris if.",
                    "",
                    "Cara nulisnya yang paling bikin bingung di awal:",
                    "",
                    "  const pola = /\\d+/g;",
                    "",
                    "Baris itu berisi satu nilai, sama seperti \"halo\" juga satu nilai. Garis",
                    "miringnya bukan pembagian. Dia pembatas, perannya sama dengan tanda",
                    "kutip pada string. Yang di dalam pembatas adalah polanya. Huruf yang",
                    "nempel di belakang pembatas penutup adalah flag-nya, yaitu pengaturan",
                    "cara mencari. Kalau ini sudah kamu pahami, baris seperti",
                    "if (/^\\d+$/.test(input)) nggak lagi kelihatan seperti pembagian yang",
                    "salah ketik.",
                    "",
                    "Flag yang perlu kamu kenal (boleh digabung, misalnya /abc/gi):",
                    "",
                    "  g   global    - cari SEMUA kemunculan, bukan yang pertama saja",
                    "  i   ignore    - huruf besar dan kecil dianggap sama",
                    "  m   multiline - ^ dan $ berlaku per BARIS, bukan per teks utuh",
                    "  s   dotAll    - titik ikut mencocoki karakter baris baru",
                    "",
                    "Kalau polanya harus dirakit dari variabel, literal /.../ nggak bisa",
                    "dipakai, karena isinya nggak pernah dievaluasi. Pakai konstruktornya,",
                    "new RegExp(...), dan flag jadi argumen kedua berupa string:",
                    "",
                    "  const kata = \"budi\";",
                    "  const pola = new RegExp(kata + \"\\\\d+\", \"gi\");",
                    "",
                    "Perhatikan backslash-nya ada dua. Yang pertama dimakan aturan string",
                    "JavaScript, yang kedua baru sampai ke regex-nya. Kalau kamu nulis",
                    "new RegExp(\"\\d+\"), hasilnya pola d+, yang mencari huruf d, bukan",
                    "angka. Ini salah satu bug regex yang paling sering terjadi di JS.",
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
                    "Tanda berikut mengatur berapa kali sesuatu boleh muncul. Tanda itu",
                    "selalu berlaku untuk hal yang ada tepat sebelumnya:",
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
                    "Grup penangkap (...) punya tugas tambahan. Potongan yang cocok di",
                    "dalamnya disimpan terpisah, supaya bisa kamu ambil lagi. Itu bahan",
                    "bagian berikutnya. Kalau kamu cuma butuh mengelompokkan, misalnya",
                    "supaya + berlaku ke beberapa karakter sekaligus, pakai (?:...). Dengan",
                    "begitu hasilnya nggak penuh dengan grup yang nggak pernah dipakai.",
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
                    "Di materi String kamu sudah lihat s.replace(\"JavaScript\", \"Coding\").",
                    "Yang belum disebut di sana: replace() dengan string biasa cuma",
                    "mengganti kemunculan pertama. Sisanya dibiarkan utuh, tanpa error dan",
                    "tanpa peringatan. Jadi bug ini baru ketahuan waktu datanya kebetulan",
                    "memuat kata itu dua kali. Solusinya ada dua: regex ber-flag g, atau",
                    "replaceAll().",
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
                    "Serakah dan malas. Kuantitas * dan + mengambil sebanyak mungkin dulu,",
                    "baru mundur secukupnya supaya sisa polanya tetap cocok. Sifat ini",
                    "disebut serakah (greedy). Pada teks \"<b>satu</b> dan <b>dua</b>\", pola",
                    "<b>.*<\\/b> cocok dengan seluruh baris, padahal yang kamu mau cuma tag",
                    "pertama. Tambahkan ? sesudah kuantitasnya supaya jadi malas (lazy) dan",
                    "berhenti di",
                    "kecocokan terpendek: <b>.*?<\\/b> menghasilkan \"<b>satu</b>\".",
                    "",
                    "Titik di regex artinya \"karakter apa saja\", jadi pola \\d+.\\d+ juga",
                    "cocok dengan \"10x000\". Kalau maksudmu titik sungguhan, escape jadi \\.",
                    "dengan backslash di depannya. Hal yang sama berlaku untuk semua",
                    "karakter yang punya peran khusus: + * ? ( ) [ ] { } ^ $ | dan",
                    "backslash sendiri. Garis miring / juga di-escape di dalam literal,",
                    "karena dia pembatasnya. Makanya tag penutup di contoh atas ditulis",
                    "<\\/b>, bukan </b>.",
                    "",
                    "Regex ber-flag g punya ingatan. Kalau regex itu disimpan di variabel,",
                    "posisi pencarian terakhirnya tersimpan di properti lastIndex, dan",
                    "test() berikutnya melanjutkan dari situ. Contohnya const p = /\\d+/g;",
                    "lalu p.test(t) dipanggil tiga kali atas teks yang sama, yang cuma",
                    "berisi satu angka. Hasilnya true, false, true. Aturan amannya: jangan",
                    "simpan regex ber-g di variabel untuk dipakai berulang oleh test().",
                    "Tulis literalnya langsung di tempat, buang flag g-nya, atau setel",
                    "ulang p.lastIndex = 0 sebelum dipakai lagi.",
                    "",
                    "Jangan mengurai HTML pakai regex. Nasihat ini sudah lama, dan",
                    "alasannya nyata. HTML boleh bersarang sedalam apa pun, sedangkan regex",
                    "nggak punya cara menghitung sarang. Pola apa pun yang kamu tulis bakal",
                    "benar untuk contohmu dan salah untuk halaman sungguhan. Pakai parser,",
                    "yaitu program pembaca HTML. Di browser, parser itu DOM.",
                    "",
                    "Kalau polamu sudah sepanjang satu baris penuh, susah dibaca dan gampang",
                    "salah. Pecah pekerjaannya jadi beberapa langkah kecil seperti slug()",
                    "di atas, atau kasih nama grup-grupnya. Kode lebih sering dibaca",
                    "daripada ditulis, dan di regex hal ini paling sering dilupakan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Form pendaftaran memeriksa nomor HP dan email pakai regex sebelum data",
                    "dikirim ke server. Admin toko online juga memakainya untuk merapikan",
                    "data pelanggan hasil impor dari spreadsheet, yang nomor HP-nya ditulis",
                    "dengan gaya berbeda-beda.",
                    "",
                    "Kasus kecil: daftar kontak pelanggan berisi nomor \"0812-3456-7890\",",
                    "\"+62 812 3456 7890\", dan \"0812 345 678 90\". Sebelum dikirimi pesan",
                    "pengingat, semuanya harus berbentuk 08 diikuti angka saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan bentuk akhirnya: diawali 08, isinya angka semua, total 10",
                    "     sampai 13 digit. Itu persis polaHP di atas: /^08\\d{8,11}$/.",
                    "  2. Pecah jadi dua langkah kecil. Buang semua yang bukan angka, lalu",
                    "     ganti awalan 62 jadi 0:",
                    "      const mentah = \"+62 812 3456 7890\";",
                    "      const angka = mentah.replace(/\\D/g, \"\");   // 6281234567890",
                    "      const hp = angka.replace(/^62/, \"0\");      // 081234567890",
                    "      console.log(/^08\\d{8,11}$/.test(hp));      // true",
                    "  3. Tanda ^ di /^62/ menjaga supaya cuma awalan yang diganti. Tanpa",
                    "     itu, nomor seperti 0813 6210 5555 ikut berubah, karena 62 di",
                    "     tengahnya diganti jadi 0.",
                    "  4. Kasus pinggir: nomor yang sesudah dibersihkan cuma 9 digit, atau",
                    "     diawali 021 karena itu telepon rumah. Keduanya gagal di test().",
                    "     Kumpulkan yang gagal untuk diperiksa manusia, jangan dipaksa lolos.",
                    "",
                    "Ingat: flag g di /\\D/g wajib ada. Tanpa g, replace cuma membuang",
                    "karakter pertama yang bukan angka, yaitu tanda +.",
                ]
            },
        ],
    },
    {
        "title": "10. Array & Method Array (map/filter/reduce)",
        "sections": [
            {
                "body": [
                    "Array adalah kumpulan data yang berurutan. Isinya boleh campur tipe,",
                    "dan ukurannya bisa bertambah atau berkurang. Mirip List di Java atau",
                    "Python, dan beda dengan array di C yang ukurannya tetap.",
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
                    "Di contoh berikut bakal muncul bentuk n => n * 2. Itu arrow function,",
                    "cara ringkas menulis fungsi. Bentuk lengkapnya dibahas di materi",
                    "'Function: Declaration, Expression & Arrow Function'. Untuk sekarang,",
                    "baca aja begini: \"untuk tiap n, hasilkan n * 2\".",
                ]
            },
            {
                "heading": "map, filter, reduce - method array paling penting di JS modern",
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
                    "Destructuring array (ES6+) artinya mengambil isi array langsung ke",
                    "beberapa variabel sekaligus:",
                    "  const [pertama, kedua, ...sisanya] = [1, 2, 3, 4, 5];",
                    "  console.log(pertama, kedua, sisanya);  // 1 2 [3, 4, 5]",
                    "",
                    "Spread operator (...) membongkar isi array. Gunanya untuk bikin",
                    "salinan atau menggabungkan array:",
                    "  const a = [1, 2, 3];",
                    "  const b = [...a, 4, 5];       // [1, 2, 3, 4, 5] (salinan baru + tambahan)",
                    "  const gabung = [...a, ...b];  // menggabung 2 array",
                    "",
                    "Array.from() bikin array baru, dan Array.isArray() ngecek apakah",
                    "sebuah nilai berupa array:",
                    "  Array.from({length: 5}, (_, i) => i * 2)  // [0, 2, 4, 6, 8]",
                    "  Array.isArray([1,2,3])   -> true",
                ]
            },
            {
                "heading": "Method array yang melengkapi daftar di atas",
                "body": [
                    "Selain map, filter, dan reduce, ada sekelompok method lain yang terus",
                    "muncul di kode nyata. Yang gampang terlewat: slice() juga dimiliki",
                    "array, nggak cuma string. Namanya mirip splice(), padahal",
                    "artinya jauh beda.",
                    "",
                    "  slice(a, b)      MENYALIN sepotong, array asli utuh",
                    "  splice(a, n, ..) MEMOTONG array aslinya di tempat",
                    "",
                    "Method mana yang mengubah array aslinya dan mana yang nggak? Daftar",
                    "lengkapnya ada di materi 'Nilai vs Referensi & Menyalin Data'.",
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
                    "reduce perlu dibahas sendiri. Di antara method di daftar ini, cuma",
                    "reduce yang argumen keduanya penting, dan argumen itu yang sering bikin",
                    "orang menghindarinya.",
                    "",
                    "  array.reduce((acc, elemen) => ..., nilaiAwal)",
                    "",
                    "acc (accumulator) adalah hasil sementara yang dibawa dari satu putaran",
                    "ke putaran berikutnya. Apa pun yang kamu return jadi acc di putaran",
                    "berikutnya. nilaiAwal menentukan acc di putaran pertama, sekaligus",
                    "menentukan tipe hasil akhirnya: 0 untuk menjumlah, {} untuk",
                    "mengelompokkan, [] untuk menyusun array.",
                    "",
                    "Kalau nilaiAwal nggak ditulis, elemen pertama dipakai sebagai acc.",
                    "Untuk array kosong, itu berarti nggak ada acc sama sekali, dan",
                    "JavaScript melempar TypeError. Biasakan selalu menulis nilai awal",
                    "supaya masalah ini nggak terjadi.",
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
                "heading": "Array.from, dan cara array dicetak",
                "body": [
                    "Array.from sudah lewat sekilas di daftar atas, cuma satu baris tanpa",
                    "penjelasan. Padahal baris itu menyimpan dua hal yang susah ditebak",
                    "sendiri: kenapa { length: 5 } boleh jadi sumber array, dan kenapa",
                    "parameter pertamanya dinamai _. Keduanya dibahas di sini.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data aplikasi hampir selalu datang sebagai array: pesanan hari ini,",
                    "siswa satu kelas, riwayat transaksi sebulan. map, filter, dan reduce",
                    "dipakai untuk menjawab pertanyaan sehari-hari pemilik usaha: berapa",
                    "omzet hari ini, pesanan mana yang belum dibayar, menu apa yang paling",
                    "laku.",
                    "",
                    "Kasus kecil: warung kopi menyimpan pesanan hari ini di array pesanan,",
                    "tiap isinya object { menu, harga, lunas }. Ada kopi susu Rp 15.000",
                    "yang sudah lunas, teh tarik Rp 12.000 yang belum lunas, dan kopi hitam",
                    "Rp 10.000 yang sudah lunas. Pemilik mau tahu uang yang sudah masuk dan",
                    "banyaknya pesanan yang belum lunas.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua pertanyaannya. Uang masuk adalah jumlah harga pesanan",
                    "     yang lunas. Belum lunas adalah banyaknya pesanan yang lunas-nya",
                    "     false.",
                    "  2. Pertanyaan pertama: saring yang lunas, lalu jumlahkan harganya",
                    "     dengan reduce. Pertanyaan kedua: saring yang belum, lalu ambil",
                    "     length-nya.",
                    "      const masuk = pesanan",
                    "        .filter(p => p.lunas)",
                    "        .reduce((acc, p) => acc + p.harga, 0);",
                    "      const belum = pesanan.filter(p => !p.lunas).length;",
                    "      console.log(masuk, belum);   // 25000 1",
                    "  3. Cocokkan sekali dengan hitungan tangan: 15000 + 10000 = 25000, dan",
                    "     cuma teh tarik yang belum lunas.",
                    "  4. Kasus pinggir: pagi hari, belum ada pesanan yang lunas. filter",
                    "     menghasilkan array kosong. Tanpa nilai awal 0, reduce melempar",
                    "     TypeError. Dengan nilai awal 0, hasilnya 0.",
                ]
            },
        ],
    },
    {
        "title": "11. Object & Destructuring",
        "sections": [
            {
                "body": [
                    "Object adalah kumpulan pasangan key: value, yaitu nama dan nilainya.",
                    "Mirip dict di Python atau HashMap di Java. Key biasanya string, dan",
                    "boleh ditulis tanpa kutip kalau namanya valid sebagai nama variabel.",
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
                    "",
                    "Pasangan key dan value di dalam object disebut property.",
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
                    "Object bisa berisi object lain (nested object). Untuk mengaksesnya",
                    "dengan aman, pakai optional chaining ?. supaya nggak error kalau ada",
                    "bagian yang kosong:",
                    "  const user = { profil: { alamat: { kota: \"Jakarta\" } } };",
                    "  console.log(user.profil?.alamat?.kota);     // 'Jakarta'",
                    "  console.log(user.profil?.pekerjaan?.gaji);  // undefined (aman, tak error)",
                    "",
                    "JSON.stringify dan JSON.parse mengubah object jadi teks JSON dan",
                    "sebaliknya. JSON adalah format teks yang biasa dipakai untuk mengirim",
                    "data:",
                    "  const teks = JSON.stringify(mahasiswa);   // object -> string JSON",
                    "  const objek = JSON.parse(teks);           // string JSON -> object",
                ]
            },
            {
                "heading": "Bentuk object literal yang sering ditemui",
                "body": [
                    "Object literal, yaitu object yang ditulis langsung pakai { }, punya",
                    "beberapa bentuk yang susah ditebak sendiri. Padahal ketiganya ada di",
                    "hampir tiap object konfigurasi:",
                    "  1. Shorthand method. Di atas kamu sudah belajar shorthand property:",
                    "     { nilai } sebagai pengganti { nilai: nilai }. Method juga punya",
                    "     bentuk ringkas: cukup hitung() { ... }, tanpa kata function dan",
                    "     tanpa titik dua.",
                    "  2. Computed key: { [namaKey]: nilai }. Isi kurung sikunya dihitung",
                    "     dulu, lalu hasilnya jadi nama key. Kurung siku di dalam { } ini",
                    "     bukan array. Kalau salah baca di sini, seluruh object-nya ikut",
                    "     salah dimengerti.",
                    "  3. get dan set boleh ditulis di object literal juga, nggak cuma di",
                    "     dalam class. Getter dibaca tanpa kurung, dan setter dipanggil",
                    "     lewat tanda sama dengan.",
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
                    "Cepat atau lambat kamu bakal butuh ini: gimana caranya memastikan",
                    "sebuah key memang milik object itu sendiri, dan bukan warisan dari",
                    "prototype?",
                    "",
                    "  Object.hasOwn(obj, key)   true hanya kalau key milik obj sendiri",
                    "  \"key\" in obj              true juga untuk key WARISAN",
                    "  Object.keys(obj)          sejak awal hanya memberi milik sendiri",
                    "",
                    "Ini kepakai di kode sungguhan. for...in ikut mengambil property",
                    "warisan, jadi loop yang kelihatan benar bisa memproses key yang nggak",
                    "pernah kamu tulis. Di kode lama, saringannya ditulis panjang:",
                    "",
                    "  Object.prototype.hasOwnProperty.call(obj, key)",
                    "",
                    "Bentuk berbelit itu dipakai karena obj sendiri bisa aja punya key",
                    "bernama hasOwnProperty. Object.hasOwn (ES2022) adalah versi pendek yang",
                    "aman dari masalah itu.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data satu pelanggan, satu produk, atau satu pesanan ojek online",
                    "disimpan sebagai object: nama, nomor HP, alamat, titik jemput. Sebelum",
                    "data itu dikirim ke halaman lain, programmer memilih field yang",
                    "dibutuhkan dan membuang yang rahasia, seperti kata sandi.",
                    "",
                    "Kasus kecil: object akun dari database berisi id 17, nama Rina, email",
                    "rina@contoh.id, sandi rahasia123, dan object alamat yang memuat kota",
                    "Malang. Halaman profil butuh id, nama, email, dan kota. Sandi nggak",
                    "boleh ikut terkirim.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan bentuk keluarannya dulu: object baru berisi id, nama,",
                    "     email, dan kota, tanpa object alamat yang bersarang.",
                    "  2. Pisahkan sandi dan alamat lewat destructuring dengan rest",
                    "     property, lalu susun object barunya:",
                    "      const { sandi, alamat, ...aman } = akun;",
                    "      const profil = { ...aman, kota: alamat?.kota ?? \"-\" };",
                    "      console.log(profil);",
                    "     Hasilnya { id: 17, nama: 'Rina', email: 'rina@contoh.id',",
                    "     kota: 'Malang' }.",
                    "  3. Pikirkan field yang ditambah belakangan. Kalau suatu hari tabel",
                    "     akun dapat field pin, ...aman ikut membawanya keluar. Untuk data",
                    "     rahasia, menyebut satu per satu field yang boleh keluar lebih aman:",
                    "     const { id, nama, email } = akun.",
                    "  4. Kasus pinggir: pelanggan baru yang belum mengisi alamat. alamat",
                    "     bernilai undefined, jadi alamat.kota bakal TypeError. Bentuk",
                    "     alamat?.kota ?? \"-\" memberi tanda strip.",
                ]
            },
        ],
    },
    {
        "title": "12. Nilai vs Referensi & Menyalin Data",
        "sections": [
            {
                "body": [
                    "JavaScript punya dua cara menyimpan nilai di dalam variabel. Kalau",
                    "bedanya sudah paham, kode yang tadinya terasa \"berubah sendiri\" jadi",
                    "masuk akal.",
                    "",
                    "  - Primitif: number, string, boolean, null, undefined, symbol, dan",
                    "    bigint. Variabel menyimpan nilainya langsung. Menyalin variabel",
                    "    berarti menyalin isinya, jadi kedua salinan berdiri sendiri.",
                    "  - Referensi: object, array, dan function. (Di JS, array dan function",
                    "    juga termasuk object.) Variabel menyimpan alamat sebuah kotak di",
                    "    memori, dan isi kotaknya ada di tempat lain. Menyalin variabel",
                    "    berarti menyalin alamatnya. Kotaknya tetap satu.",
                    "",
                    "Bayangkan \"dua nama, satu kotak\". Gambaran ini bakal kepakai terus:",
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
                    "Ini bukan keanehan JavaScript. Java dan Python berperilaku sama untuk",
                    "object. C# dan Go juga mirip, tapi keduanya punya struct, tipe yang",
                    "disalin utuh seperti primitif. Istilah yang dipakai buku tiap bahasa",
                    "aja yang beda-beda.",
                    "",
                    "Kenapa const angka = [] tetap boleh di-push?",
                    "",
                    "Di materi Variabel, const disebut untuk nama yang nggak akan diisi",
                    "ulang. Lalu di materi 'Array & Method Array' ada const angka = [10, 20,",
                    "30] yang langsung dipanggil angka.push(50). Itu bukan salah ketik.",
                    "const mengunci nama ke satu alamat. Isi kotaknya nggak ikut dibekukan.",
                    "",
                    "  const angka = [1, 2];",
                    "  angka.push(3);  // BOLEH -> isi kotak berubah, alamatnya tetap itu-itu juga",
                    "  angka = [9];    // TypeError -> ini mengganti ALAMAT yang dipegang 'angka'",
                    "",
                    "Jadi baca const sebagai \"nama ini nggak akan pernah menunjuk ke tempat",
                    "lain\". Cara membekukan isinya ada di bagian akhir materi ini.",
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
                "heading": "Membandingkan isi object dan memutasi array",
                "body": [
                    "Akibat pertama: === membandingkan identitas, yaitu apakah dua nilai itu",
                    "kotak yang sama. Isinya nggak dilihat.",
                    "",
                    "  [1, 2] === [1, 2]           -> false  dua kotak berbeda yang kebetulan seisi",
                    "  { a: 1 } === { a: 1 }       -> false",
                    "  const x = [1, 2]; x === x   -> true   satu kotak yang sama",
                    "",
                    "Makanya arr.includes(obj) dan arr.indexOf(obj) mencari object yang",
                    "identik, alias kotak yang sama, dan nggak peduli object lain yang",
                    "isinya mirip. Untuk mencari yang isinya cocok, pakai find atau",
                    "findIndex dengan syarat per field (lihat materi 'Array & Method",
                    "Array').",
                    "",
                    "Cara membandingkan isi:",
                    "  1. Per field: a.nama === b.nama && a.umur === b.umur. Ini paling",
                    "     jelas dan paling cepat. Pakai cara ini kalau field-nya sedikit.",
                    "  2. JSON.stringify(a) === JSON.stringify(b). Gampang ditulis dan boleh",
                    "     untuk data sederhana, tapi jangan dijadikan alat banding serius.",
                    "     Masalahnya ada tiga:",
                    "     - Urutan key ikut dibandingkan. {x:1,y:2} dan {y:2,x:1} dianggap",
                    "       beda.",
                    "     - undefined, function, dan symbol hilang, sedangkan Date jadi",
                    "       string.",
                    "     - Object yang melingkar (a.diri = a) melempar TypeError.",
                    "  3. Di proyek nyata, untuk kasus rumit orang pakai isEqual() dari",
                    "     lodash.",
                    "",
                    "Akibat kedua: sebagian method array mengubah array aslinya. Mengubah",
                    "data yang sudah ada disebut mutasi.",
                    "",
                    "  MENGUBAH ASLINYA (mutasi)     MENGEMBALIKAN ARRAY BARU",
                    "  push, pop                     map, filter, reduce",
                    "  shift, unshift                slice, concat",
                    "  splice, fill                  toSorted, toReversed, toSpliced (ES2023)",
                    "  sort, reverse                 flat, flatMap, with(indeks, nilai)",
                    "",
                    "Jebakan: sort() dan reverse() mengembalikan hasil, dan sekaligus",
                    "mengaduk array aslinya di tempat. Kalau array aslinya masih dipakai,",
                    "salin dulu: [...arr].sort((a, b) => a - b). Atau pakai",
                    "arr.toSorted((a, b) => a - b), yang memang bikin array baru.",
                    "",
                    "Perhatikan juga pasangan slice() dan splice(). slice() menyalin,",
                    "splice() memotong array aslinya. Namanya nyaris kembar, akibatnya jauh",
                    "beda.",
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
                "heading": "Cara menyalin dari spread sampai structuredClone",
                "body": [
                    "Rangkuman cara menyalin, diurutkan dari yang paling dangkal. Salinan",
                    "dangkal cuma menyalin lapis teratas. Salinan dalam ikut menyalin",
                    "object di dalamnya.",
                    "",
                    "  {...obj} atau Object.assign({}, obj)",
                    "      Satu lapis. Paling sering dipakai, dan cukup untuk object datar.",
                    "  [...arr] atau arr.slice()",
                    "      Satu lapis juga. Array barunya berisi object-object yang SAMA",
                    "      persis.",
                    "  { ...u, alamat: { ...u.alamat } }",
                    "      Dalam, tapi hanya di jalur yang kamu tulis sendiri.",
                    "  structuredClone(obj)",
                    "      Dalam dan benar: object bersarang, array, Date, Map, Set ikut",
                    "      tersalin. Tidak bisa menyalin function; object berisi function",
                    "      melempar DataCloneError.",
                    "  JSON.parse(JSON.stringify(obj))",
                    "      Dalam tapi rugi: Date jadi string, undefined & function lenyap,",
                    "      dan object melingkar langsung error. Pakai hanya untuk data JSON",
                    "      polos.",
                    "",
                    "Object.assign({}, a, b) muncul di ES6 (2015), sebelum spread untuk",
                    "object ada (ES2018). Kamu bakal sering ketemu bentuk ini di kode Redux",
                    "dan library lama. Artinya sama dengan { ...a, ...b }, termasuk",
                    "sama-sama cuma satu lapis.",
                    "",
                    "Kebiasaan yang bikin aman:",
                    "  1. Curigai setiap b = a pada object atau array. Itu bukan salinan.",
                    "  2. Jangan mengubah object yang diterima sebagai argumen. Kembalikan",
                    "     object baru.",
                    "  3. Ingat, spread cuma satu lapis. Pola",
                    "     { ...state, user: { ...state.user, nama: 'X' } } adalah cara baku",
                    "     memperbarui state di React dan Redux. Alasannya ada di materi ini:",
                    "     kalau lapisan dalam nggak ikut disalin, data lama ikut berubah.",
                    "  4. Object.freeze() enak untuk konstanta konfigurasi, tapi dia juga",
                    "     cuma satu lapis. Kalau isinya harus beku sampai ke dalam, bekukan",
                    "     sendiri lapis demi lapis.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Bug \"datanya berubah sendiri\" sering muncul di fitur yang punya tombol",
                    "Batal atau riwayat: form edit profil, keranjang yang bisa dikembalikan",
                    "ke isi sebelumnya, atau editor dengan tombol undo. Kalau draf yang",
                    "diedit ternyata kotak yang sama dengan data aslinya, tombol Batal",
                    "nggak membatalkan apa pun.",
                    "",
                    "Kasus kecil: form edit profil memuat data Dodi yang tinggal di Solo,",
                    "dengan kota disimpan di dalam object alamat. Pengguna mengganti kota",
                    "jadi Klaten, lalu menekan Batal. Ternyata data aslinya juga sudah",
                    "berisi Klaten.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari baris yang membuat draf. Kalau tertulis const draf = asli,",
                    "     itu dua nama untuk satu kotak, jadi wajar keduanya berubah",
                    "     bersama.",
                    "  2. Ganti jadi { ...asli } lalu coba lagi. Nama sekarang aman, tapi",
                    "     kota tetap ikut berubah. Spread cuma menyalin satu lapis, dan",
                    "     alamat di dalamnya masih kotak yang sama.",
                    "  3. Pakai salinan dalam:",
                    "      const asli = { nama: \"Dodi\", alamat: { kota: \"Solo\" } };",
                    "      const draf = structuredClone(asli);",
                    "      draf.alamat.kota = \"Klaten\";",
                    "      console.log(asli.alamat.kota, draf.alamat.kota);   // Solo Klaten",
                    "  4. Kasus pinggir: object yang berisi function membuat structuredClone",
                    "     melempar DataCloneError. Untuk data seperti itu, salin sendiri",
                    "     lapis yang memang diedit: { ...asli, alamat: { ...asli.alamat } }.",
                ]
            },
        ],
    },
    {
        "title": "13. Map & Set",
        "sections": [
            {
                "body": [
                    "Di materi Object & Destructuring, object literal sudah dipakai sebagai",
                    "\"kamus\" key -> value. Untuk data kecil itu memang cukup. Tapi object",
                    "punya empat batasan yang baru kerasa waktu datanya sungguhan:",
                    "  - Key-nya selalu diubah jadi string. obj[1] dan obj[\"1\"] menunjuk",
                    "    tempat yang sama. obj[{ id: 7 }] menyimpan ke key bernama",
                    "    \"[object Object]\", jadi dua object yang beda saling menimpa tanpa",
                    "    peringatan apa pun.",
                    "  - Urutannya nggak sama dengan urutan penulisan. Key berbentuk angka",
                    "    dipindah ke depan dan diurutkan dari kecil ke besar:",
                    "    Object.keys({ 2: \"b\", 1: \"a\", z: \"z\" }) memberi ['1', '2', 'z'].",
                    "  - Nggak ada obj.length. Untuk menghitung isinya, kamu harus lewat",
                    "    Object.keys(obj).length.",
                    "  - Object mewarisi property dari prototype (lihat materi Prototype).",
                    "    Jadi obj[\"toString\"] sudah berisi sesuatu, padahal kamu nggak",
                    "    pernah menaruhnya.",
                    "",
                    "Map dan Set adalah dua struktur data bawaan yang mengatasi semua itu.",
                    "Namanya sempat lewat di materi Perulangan sebagai contoh iterable. Di",
                    "sini keduanya dipakai sungguhan, karena di kode nyata keduanya ada di",
                    "mana-mana.",
                    "  - Map adalah kumpulan pasangan key -> value. Key boleh apa aja, dan",
                    "    urutannya dijamin persis urutan waktu dimasukkan.",
                    "  - Set adalah kumpulan nilai yang dijamin nggak punya duplikat.",
                    "",
                    "Jebakan: untuk jumlah isi, keduanya pakai .size, bukan .length. Kalau",
                    "kamu nulis map.length, nggak muncul error. Hasilnya cuma undefined,",
                    "dan kodemu salah tanpa ketahuan.",
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
                "heading": "Jebakan Map dan kapan lebih baik dari object",
                "body": [
                    "Ada empat jebakan Map yang nggak memunculkan error:",
                    "1. map[key] bukan cara mengakses isi Map. cache[\"x\"] = 1 cuma memasang",
                    "   property biasa pada objek Map-nya, ibarat menempel stiker di luar",
                    "   kotak. Isi Map-nya nggak tersentuh: cache.size tetap 0 dan",
                    "   cache.get(\"x\") tetap undefined. Yang benar cuma .set() dan .get().",
                    "   Ini kesalahan nomor satu orang yang baru pindah dari object, dan",
                    "   nggak ada satu pun pesan yang ngasih tahu.",
                    "2. Key berupa object dibandingkan lewat identitasnya, alias kotak yang",
                    "   sama, dan isinya nggak dilihat.",
                    "     m.set({ id: 1 }, \"a\"); m.get({ id: 1 })  ->  undefined,",
                    "   karena kurung kurawal kedua membuat object baru di alamat lain.",
                    "   Simpan dulu object-nya di variabel kalau mau dipakai sebagai key.",
                    "3. JSON.stringify(map) menghasilkan \"{}\". Map itu bukan object biasa,",
                    "   jadi JSON nggak tahu cara membacanya. Untuk menyimpannya, pakai",
                    "   JSON.stringify(Object.fromEntries(map)), atau JSON.stringify([...map])",
                    "   kalau key-nya bukan string.",
                    "4. Map nggak ikut tersalin oleh { ...map }. Hasilnya object kosong.",
                    "   Salinan Map dibuat pakai new Map(map).",
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
                    "Map dan Set punya sepupu yang lebih \"lemah\": WeakMap dan WeakSet.",
                    "Keduanya cuma menerima object sebagai key atau isi, nggak bisa",
                    "ditelusuri, dan nggak punya .size. Gunanya satu: isinya nggak menahan",
                    "object itu tetap di memori. Begitu object-nya nggak dipakai siapa pun",
                    "lagi, dia bisa dibersihkan. Map biasa menahan key-nya selamanya, dan",
                    "itu jadi kebocoran memori kalau key-nya elemen DOM atau object yang",
                    "umurnya pendek. Kamu bakal ketemu WeakMap di kode library. Untuk",
                    "sekarang, cukup tahu kenapa dia ada.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Map dan Set dipakai di tempat yang butuh pencarian cepat atau data",
                    "tanpa kembar. Contohnya rekap jumlah terjual per barang di laporan",
                    "harian, daftar pengunjung unik sebuah halaman, atau cache hasil yang",
                    "mahal dihitung.",
                    "",
                    "Kasus kecil: mesin kasir mencatat setiap barang yang discan, berurutan:",
                    "gula, kopi, gula, teh, gula, kopi. Pemilik toko mau rekap jumlah per",
                    "barang dan tahu ada berapa jenis barang yang terjual.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Keluaran pertama berbentuk pasangan barang ke jumlah. Itu Map,",
                    "     dengan nama barang sebagai key.",
                    "  2. Susuri daftarnya sekali. Barang yang baru pertama muncul memberi",
                    "     undefined dari get, jadi beri cadangan 0 pakai ??.",
                    "      const scan = [\"gula\", \"kopi\", \"gula\", \"teh\", \"gula\", \"kopi\"];",
                    "      const rekap = new Map();",
                    "      for (const b of scan) rekap.set(b, (rekap.get(b) ?? 0) + 1);",
                    "      console.log(rekap.get(\"gula\"), rekap.get(\"teh\"));   // 3 1",
                    "      console.log(new Set(scan).size);                    // 3",
                    "  3. Jumlah jenis barang bisa dibaca dari rekap.size atau dari",
                    "     new Set(scan).size. Hasilnya sama, 3, karena key Map dan isi Set",
                    "     dijamin nggak punya kembar.",
                    "  4. Kasus pinggir: rekap.length memberi undefined tanpa error. Jumlah",
                    "     isi Map dan Set selalu dibaca dari .size.",
                    "",
                    "Ingat: urutan isi Map mengikuti urutan barang pertama kali discan.",
                    "Untuk peringkat terlaris, ubah dulu jadi array lalu urutkan:",
                    "[...rekap].sort((x, y) => y[1] - x[1]).",
                ]
            },
        ],
    },
    {
        "title": "14. Function: Declaration, Expression & Arrow Function",
        "sections": [
            {
                "body": [
                    "Fungsi adalah sekumpulan kode yang diberi nama, supaya bisa dipanggil",
                    "berulang kali. JavaScript punya beberapa cara bikin fungsi:",
                    "1. Function declaration. Fungsi ini di-hoist, artinya bisa dipanggil",
                    "   di baris sebelum fungsinya ditulis.",
                    "     function tambah(a, b) {",
                    "         return a + b;",
                    "     }",
                    "2. Function expression, yaitu fungsi yang disimpan ke variabel. Fungsi",
                    "   ini nggak di-hoist.",
                    "     const tambah = function(a, b) {",
                    "         return a + b;",
                    "     };",
                    "3. Arrow function (ES6+). Tulisannya ringkas, dan bentuk ini yang",
                    "   paling sering dipakai.",
                    "     const tambah = (a, b) => a + b;",
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
console.log(total(1, 2, 3, 4)); // 10

// Optional call ?.() (bentuk lain optional chaining dari materi Operator):
// panggil fungsinya HANYA kalau fungsinya ada. Pengganti if (selesai) selesai();
// selesai di sini callback, yaitu fungsi yang dikirim ke fungsi lain untuk
// dipanggil nanti.
function jalankan(selesai) {
    selesai?.();
}
jalankan();                                  // aman, tidak error
jalankan(() => console.log("callback dipanggil")); // callback dipanggil"""
            },
            {
                "body": [
                    "Arrow function beda dari function biasa dalam tiga hal. Ketiganya",
                    "dibahas lebih detail di materi \"Keyword 'this' & Context\".",
                    "  1. Arrow function nggak punya this sendiri. Dia memakai this dari",
                    "     scope di luarnya (lexical this).",
                    "  2. Arrow function nggak bisa dipakai sebagai constructor (dipanggil",
                    "     pakai new).",
                    "  3. Arrow function nggak punya objek arguments. Apa itu arguments",
                    "     dijelaskan di materi 'Pola Fungsi: IIFE, Rekursi, dan Currying'.",
                    "     Singkatnya, arguments itu peninggalan dari sebelum rest parameter",
                    "     ada, dan masih sering muncul di kode lama.",
                    "",
                    "Di JavaScript, fungsi adalah first-class citizen, artinya fungsi",
                    "diperlakukan seperti nilai biasa. Fungsi bisa disimpan ke variabel,",
                    "dikirim sebagai argumen, dan dikembalikan dari fungsi lain. Sifat ini jadi",
                    "dasar higher-order function (fungsi yang menerima atau",
                    "mengembalikan fungsi) dan callback.",
                ]
            },
            {
                "heading": "Arrow yang mengembalikan object wajib dibungkus kurung",
                "body": [
                    "Ada satu jebakan di arrow function yang pasti bakal kamu temui. Yang",
                    "bikin repot, jebakan ini nggak memunculkan error apa pun:",
                    "",
                    "  data.map(u => { nama: u.nama })     <- hasilnya undefined semua",
                    "  data.map(u => ({ nama: u.nama }))   <- yang benar",
                    "",
                    "Sesudah tanda =>, kurung kurawal { dibaca sebagai awal blok kode,",
                    "bukan awal object literal. Blok itu nggak punya return, jadi tiap",
                    "panggilan mengembalikan undefined tanpa peringatan. Kalau object-nya",
                    "dibungkus kurung biasa, JavaScript terpaksa membacanya sebagai",
                    "ekspresi, dan artinya kembali seperti yang kamu maksud.",
                    "",
                    "Kalau ragu, tulis aja bentuk panjangnya dengan return yang jelas.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Begitu satu hitungan dipakai di lebih dari satu tempat, programmer",
                    "membungkusnya jadi fungsi. Di toko online, hitungan ongkir dipakai di",
                    "halaman keranjang, halaman pembayaran, dan email konfirmasi. Kalau",
                    "tarifnya berubah, cukup satu fungsi yang diganti, dan ketiga tempat",
                    "itu ikut benar.",
                    "",
                    "Kasus kecil: kurir lokal menarik Rp 10.000 untuk 3 km pertama, lalu",
                    "Rp 2.500 per km berikutnya. Jaraknya dibulatkan ke atas. Hitung ongkir",
                    "untuk 2 km, 3 km, dan 5,4 km.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan masukan dan keluarannya: satu angka jarak masuk, satu",
                    "     angka rupiah keluar. Fungsi berbentuk begini paling gampang diuji.",
                    "  2. Pecah aturannya: bulatkan jarak ke atas, lalu bedakan jarak sampai",
                    "     3 km dengan sisanya.",
                    "      const ongkir = (km, tarifAwal = 10000) => {",
                    "        const jarak = Math.ceil(km);",
                    "        if (jarak <= 3) return tarifAwal;",
                    "        return tarifAwal + (jarak - 3) * 2500;",
                    "      };",
                    "      console.log(ongkir(2), ongkir(3), ongkir(5.4));   // 10000 10000 17500",
                    "  3. Uji tepat di batasnya: 3 km harus masih tarif awal. Salah tulis <",
                    "     dan <= paling sering terjadi di sini.",
                    "  4. Kasus pinggir: pelanggan member dapat tarif awal Rp 8.000. Default",
                    "     parameter membuat semua panggilan lama tetap jalan, dan untuk",
                    "     member cukup ongkir(5.4, 8000), hasilnya 15500.",
                ]
            },
        ],
    },
    {
        "title": "15. Scope & Closure",
        "sections": [
            {
                "body": [
                    "Scope adalah wilayah tempat sebuah variabel bisa dipakai.",
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
                    "Ini salah satu alasan utama let dan const lebih disarankan daripada",
                    "var di kode JavaScript modern.",
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
                    "Closure, yaitu fungsi yang mengingat scope tempat dia dibuat seperti di",
                    "contoh atas, sering ditanyakan di wawancara kerja. Alasannya:",
                    "  1. Closure jadi dasar banyak pola JavaScript, misalnya module pattern",
                    "     dan currying.",
                    "  2. Closure dulu jadi cara bikin variabel privat (private variable),",
                    "     sebelum class punya field privat.",
                    "  3. Closure dipakai luas di React (custom hooks) dan library modern",
                    "     lain.",
                    "",
                    "Bug closure di dalam loop yang klasik, dan sering ditanyakan juga:",
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
                    "Bocornya var dari blok tadi baru separuh cerita. Separuh lainnya",
                    "namanya hoisting, dan hoisting nggak cuma terjadi pada fungsi.",
                    "",
                    "Sebelum sebuah scope dijalankan, JavaScript mendaftarkan dulu semua",
                    "deklarasi di dalamnya. Yang naik ke atas cuma deklarasinya. Nilainya",
                    "tetap tinggal di barisnya semula. Untuk var, akibatnya begini:",
                    "",
                    "  console.log(x);   // undefined  <- bukan error!",
                    "  var x = 5;",
                    "",
                    "let dan const juga ikut terangkat, tapi JavaScript menolak membacanya",
                    "sampai baris deklarasinya dijalankan. Rentang \"sudah terdaftar tapi",
                    "belum boleh dipakai\" itu namanya Temporal Dead Zone (TDZ), dan pesan",
                    "errornya berbunyi:",
                    "",
                    "  ReferenceError: Cannot access 'x' before initialization",
                    "",
                    "Pesan itu kedengaran aneh kalau kamu belum kenal TDZ, karena",
                    "variabelnya jelas ada di kode, beberapa baris di bawah. Bedakan dengan",
                    "'x is not defined', yang artinya nama itu memang nggak ada di mana pun.",
                    "",
                    "Ini alasan yang lebih kuat untuk memilih let dan const. var memberi",
                    "undefined tanpa bilang apa-apa, sedangkan let dan const langsung",
                    "berhenti dan ngasih tahu.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Closure dipakai setiap kali sebuah fungsi perlu mengingat sesuatu di",
                    "antara panggilan tanpa memakai variabel global. Contohnya pembuat nomor",
                    "antrean, penghitung percobaan login yang gagal, atau pengaturan yang",
                    "dikunci sekali di awal lalu dipakai berkali-kali.",
                    "",
                    "Kasus kecil: puskesmas punya dua loket, Umum dan Gigi. Masing-masing",
                    "butuh nomor antrean sendiri yang mulai dari 1: U-1, U-2, dan",
                    "seterusnya untuk Umum, lalu G-1, G-2 untuk Gigi. Nomor satu loket",
                    "nggak boleh mengganggu loket lain, dan nggak bisa diubah dari luar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Di antara panggilan, fungsinya cuma harus ingat nomor terakhir.",
                    "     Kalau nomor itu disimpan di variabel global, dua loket berbagi satu",
                    "     angka, dan kode mana pun bisa mengubahnya.",
                    "  2. Simpan angkanya di dalam fungsi pembuat, lalu kembalikan fungsi",
                    "     yang menaikkannya. ++nomor menaikkan dulu baru nilainya dipakai,",
                    "     jadi nomor pertama 1.",
                    "      function buatAntrean(kode) {",
                    "        let nomor = 0;",
                    "        return () => `${kode}-${++nomor}`;",
                    "      }",
                    "      const umum = buatAntrean(\"U\"), gigi = buatAntrean(\"G\");",
                    "      console.log(umum(), umum(), gigi());   // U-1 U-2 G-1",
                    "  3. Tiap panggilan buatAntrean menghasilkan closure dengan nomor",
                    "     sendiri, jadi loket Gigi tetap mulai dari 1. Variabel nomor nggak",
                    "     bisa disentuh dari luar, karena cuma closure itu yang mengenalnya.",
                    "  4. Kasus pinggir: hari berganti dan nomor harus kembali ke 1. Cukup",
                    "     panggil buatAntrean(\"U\") lagi, dan closure barunya mulai dari 0.",
                ]
            },
        ],
    },
    {
        "title": "16. Pola Fungsi: IIFE, Rekursi, dan Currying",
        "sections": [
            {
                "body": [
                    "Tiga pola di materi ini semuanya dibangun di atas closure yang baru",
                    "kamu pelajari. Ketiganya jarang diajarkan, padahal bakal kamu temui di",
                    "kode orang lain. Jadi tujuannya bukan supaya kamu rajin menulisnya.",
                    "Tujuannya supaya kamu nggak berhenti membaca waktu ketemu pola ini.",
                    "",
                    "IIFE (Immediately Invoked Function Expression) adalah fungsi yang",
                    "langsung dipanggil di tempat dia ditulis, tanpa pernah dikasih nama.",
                    "",
                    "  (function () { ... })();     <- bentuk klasik",
                    "  (() => { ... })();           <- bentuk arrow",
                    "",
                    "Cara bacanya, dibagi dua:",
                    "  - Kurung luar membungkus fungsinya jadi sebuah ekspresi. Tanpa kurung",
                    "    itu, baris yang diawali kata function dibaca sebagai deklarasi",
                    "    fungsi, dan deklarasi nggak boleh langsung dipanggil. Node bakal",
                    "    menjawab: SyntaxError: Function statements require a function name.",
                    "  - Kurung kedua, () di ujung, adalah pemanggilannya. Sama dengan ()",
                    "    yang kamu tulis waktu memanggil fungsi biasa.",
                    "",
                    "Bentuk ini ada karena dulu JavaScript nggak punya cara lain bikin",
                    "scope privat. Itu sebelum ES6 punya module (dibahas di materi 'Module",
                    "(import/export) & npm Dasar'). Semua var di level paling atas sebuah",
                    "berkas nempel ke objek global, jadi dua <script> di satu halaman bisa",
                    "saling menimpa variabel tanpa ada yang ngasih tahu. Kalau seluruh isi",
                    "berkas dibungkus IIFE, variabelnya nggak bocor ke mana-mana. Makanya",
                    "berkas JS lama, dan hampir semua hasil bundling di folder dist/, dibuka",
                    "dengan baris yang bentuknya seperti itu.",
                    "",
                    "Baris pertama di dalam IIFE sering berisi \"use strict\";. Mode ketat",
                    "(strict mode) ini bisa berlaku per fungsi. Kalau ditaruh di dalam IIFE,",
                    "mode itu cuma menyala untuk kode kita, dan aturan skrip orang lain di",
                    "halaman yang sama nggak ikut berubah.",
                    "",
                    "Ada satu pemakaian IIFE yang masih hidup sampai sekarang. await cuma",
                    "boleh dipakai di dalam fungsi async (materi 'Asynchronous JavaScript:",
                    "async/await'). Level atas sebuah skrip biasa, yaitu berkas .js",
                    "CommonJS di Node atau <script> tanpa type=\"module\", bukan fungsi async.",
                    "Jadi kalau kamu nulis await ambilData() di baris paling luar, hasilnya",
                    "SyntaxError. Pembungkus standarnya:",
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
                    "keduanya. Kamu perlu bisa membacanya, tapi nggak perlu menulisnya lagi.",
                    "1. Objek arguments. Di materi 'Function: Declaration, Expression &",
                    "   Arrow Function', arguments disebut sebagai sesuatu yang nggak",
                    "   dimiliki arrow function. Ini dia bendanya. Setiap function biasa",
                    "   otomatis punya variabel bernama arguments yang berisi semua argumen",
                    "   yang masuk, termasuk yang nggak ditulis di daftar parameter. Sebelum",
                    "   ada rest parameter (...angka), cuma ini cara bikin fungsi yang bisa",
                    "   menerima argumen sebanyak apa pun.",
                    "   Jebakannya: arguments mirip array, karena punya .length dan bisa",
                    "   dibaca pakai arguments[0], tapi dia bukan array. Di situ nggak ada",
                    "   .map, .filter, atau .reduce. Makanya kode lama penuh dengan",
                    "   Array.prototype.slice.call(arguments), yang \"meminjam\" method slice",
                    "   milik array untuk mengubahnya jadi array betulan.",
                    "   Jebakan kedua khusus Node. Node membungkus berkas .js CommonJS dengan",
                    "   sebuah fungsi tanpa bilang-bilang. Jadi arguments di level atas",
                    "   berkas nggak error, tapi malah berisi 5 argumen internal Node:",
                    "   exports, require, module, __filename, dan __dirname. Di browser,",
                    "   hasilnya ReferenceError.",
                    "2. var self = this (kadang ditulis var that = this). Sebelum arrow",
                    "   function ada, callback di dalam sebuah method punya this sendiri yang",
                    "   salah. Soal this dibahas di materi \"Keyword 'this' & Context\". Akalnya",
                    "   begini: salin this ke variabel biasa, karena variabel ikut ditangkap",
                    "   closure, sedangkan this nggak. Jadi kalau kamu lihat self atau that",
                    "   di kode lama, itulah yang sedang terjadi.",
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
                    "Rekursi adalah fungsi yang memanggil dirinya sendiri dengan soal yang",
                    "lebih kecil setiap kali, sampai ketemu soal yang jawabannya sudah",
                    "jelas.",
                    "",
                    "Ada dua bagian yang wajib ada, dan urutan menulisnya penting:",
                    "  1. Base case, yaitu kondisi berhenti. Ditulis paling atas, pakai",
                    "     return.",
                    "  2. Langkah rekursif, yaitu memanggil diri sendiri dengan nilai yang",
                    "     bergerak mendekati base case, misalnya n - 1 atau anak berikutnya.",
                    "",
                    "Kalau base case lupa ditulis, atau langkahnya nggak pernah sampai ke",
                    "sana, kamu bakal ketemu error ini:",
                    "",
                    "  RangeError: Maximum call stack size exceeded",
                    "",
                    "Call stack adalah tumpukan catatan pemanggilan fungsi. Tiap pemanggilan",
                    "fungsi menaruh satu \"kartu\" di tumpukan, dan kartu itu baru diangkat",
                    "sesudah fungsinya return. Rekursi yang nggak pernah return terus",
                    "menumpuk kartu sampai tumpukannya penuh (sekitar sepuluh ribu tingkat",
                    "di Node), lalu programnya berhenti dengan error. Call stack dibahas",
                    "lebih jauh di materi 'Asynchronous JavaScript: Callback'.",
                    "",
                    "Jadi error itu hampir selalu berarti satu hal: base case-nya nggak",
                    "pernah kena. Cek dua hal. Apakah base case-nya ada? Apakah nilai yang",
                    "dikirim ke pemanggilan berikutnya memang bergerak ke arah base case?",
                    "",
                    "Di kode nyata, rekursi dipakai kalau kedalaman datanya nggak diketahui",
                    "dari awal. Contohnya JSON bersarang dari API, pohon komentar, struktur",
                    "folder, pohon DOM (element.children yang isinya element lagi, materi",
                    "'DOM Manipulation & Event Dasar'), dan menyalin object sampai ke",
                    "dalam-dalamnya. Loop biasa nggak bisa dipakai di situ, karena kamu",
                    "nggak tahu harus menulis berapa lapis for.",
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
                    "Currying artinya memecah fungsi yang menerima banyak argumen jadi",
                    "rantai fungsi yang masing-masing cuma menerima satu argumen.",
                    "",
                    "  const tambah = (a, b) => a + b;      dipanggil:  tambah(2, 3)",
                    "  const tambah = a => b => a + b;      dipanggil:  tambah(2)(3)",
                    "",
                    "Cara membaca dua panah berturut-turut: panah pertama mengembalikan",
                    "fungsi baru yang masih mengingat nilai a. Ini closure lagi. Kalau",
                    "bingung, bayangkan ada kurung tambahan: a => (b => a + b). Dua pasang",
                    "kurung waktu memanggil, tambah(2)(3), artinya kamu memanggil dua",
                    "fungsi. Hasil fungsi pertama langsung dipanggil oleh kurung kedua.",
                    "",
                    "Gunanya nyata, namanya partial application. Kamu kunci argumen yang",
                    "itu-itu aja sekali di depan, lalu pakai fungsi hasilnya berkali-kali.",
                    "Karena sisanya tinggal satu argumen, fungsi itu langsung pas dipasang",
                    "ke .map(), ke event handler, atau ke daftar middleware.",
                    "",
                    "Bentuk ini yang sering bikin kaget waktu pertama kali membuka kode",
                    "Express atau Redux:",
                    "",
                    "  store => next => action => { ... }         (middleware Redux)",
                    "  (opsi) => (req, res, next) => { ... }      (middleware Express)",
                    "",
                    "Itu bukan sintaks khusus library. Isinya cuma tiga fungsi bersarang",
                    "biasa. Framework memanggil lapisan luarnya sekali waktu persiapan,",
                    "untuk menyimpan konfigurasi ke dalam closure. Lalu lapisan paling",
                    "dalam dipanggil tiap kali ada request atau action masuk.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rekursi muncul setiap kali data bercabang tanpa kedalaman yang tetap:",
                    "kategori toko online (Elektronik, lalu Ponsel, lalu Aksesoris),",
                    "komentar yang dibalas lalu dibalas lagi, atau folder di dalam folder.",
                    "Kamu nggak tahu harus menulis berapa lapis loop, jadi fungsinya",
                    "memanggil dirinya sendiri untuk tiap cabang.",
                    "",
                    "Kasus kecil: di kolom komentar sebuah artikel, komentar \"Mantap\" punya",
                    "dua balasan, dan balasan kedua dibalas lagi satu kali. Tiap komentar",
                    "berbentuk { teks, balasan: [...] }. Tampilkan jumlah semua komentar,",
                    "termasuk balasan di semua tingkat. Jawabannya harus 4.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kedalaman balasannya nggak diketahui, jadi loop bersarang biasa",
                    "     nggak cukup. Itu tanda untuk rekursi.",
                    "  2. Langkah rekursifnya: satu untuk komentar itu sendiri, ditambah",
                    "     jumlah dari tiap balasannya, yang dihitung pakai fungsi yang sama.",
                    "      function hitung(k) {",
                    "        let total = 1;",
                    "        for (const b of k.balasan) total += hitung(b);",
                    "        return total;",
                    "      }",
                    "      console.log(hitung(komentar));   // 4",
                    "  3. Base case-nya komentar tanpa balasan. Loop-nya nggak jalan sama",
                    "     sekali, jadi fungsinya langsung mengembalikan 1 dan rekursinya",
                    "     berhenti di situ.",
                    "  4. Kasus pinggir: data lama yang belum punya field balasan. for...of",
                    "     atas undefined melempar TypeError. Tulis k.balasan ?? [] supaya",
                    "     komentar seperti itu tetap dihitung 1.",
                ]
            },
        ],
    },
    {
        "title": "17. Iterator & Generator",
        "sections": [
            {
                "body": [
                    "for...of jalan di array, string, Map, dan Set, tapi error di object",
                    "biasa. Penyebabnya, for...of nggak tahu apa itu array. Dia cuma ngecek",
                    "satu hal: apakah objek itu punya method bernama Symbol.iterator. Kalau",
                    "ada, method itu dipakai. Kalau nggak ada, JavaScript berhenti dengan",
                    "pesan TypeError: mahasiswa is not iterable.",
                    "",
                    "Kesepakatan ini namanya protokol iterable. Dua istilahnya sering",
                    "ketuker:",
                    "",
                    "  iterable -> objek yang PUNYA method [Symbol.iterator]().",
                    "              Bawaan JS: Array, String, Map, Set, NodeList.",
                    "  iterator -> objek HASIL panggilan method itu; punya .next().",
                    "              Tiap .next() memberi { value: ..., done: true/false }.",
                    "",
                    "Symbol.iterator itu bukan string 'iterator'. Dia sebuah Symbol, yaitu",
                    "nilai unik bawaan JavaScript yang dipakai sebagai nama property.",
                    "Dipilih Symbol supaya nggak pernah bentrok dengan key biasa milikmu",
                    "yang kebetulan juga bernama 'iterator'.",
                    "",
                    "Tiga sintaks berikut pakai protokol yang sama. Kalau satu jalan,",
                    "ketiganya jalan. Kalau satu error, ketiganya error:",
                    "",
                    "  for (const x of data) { ... }   // materi Perulangan",
                    "  const salinan = [...data];      // spread",
                    "  const [a, b] = data;            // destructuring array",
                    "",
                    "Object literal sengaja dibiarkan nggak iterable. JavaScript nggak mau",
                    "menebak apa yang mau kamu telusuri: key-nya, value-nya, atau",
                    "pasangannya. Kamu yang memilih, lewat Object.keys, Object.values, atau",
                    "Object.entries (materi Object & Destructuring).",
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
                "heading": "function* dan yield: fungsi yang bisa dijeda lalu dilanjutkan",
                "body": [
                    "Menulis objek { next() { ... } } seperti di atas itu capek dan gampang",
                    "salah. Kamu sendiri yang harus mengurus penghitung, batas, dan kapan",
                    "done jadi true. Generator adalah cara singkat menulis hal yang sama.",
                    "JavaScript yang membuatkan iterator-nya untukmu.",
                    "",
                    "  function* nama() { ... }   <- tanda BINTANG setelah kata",
                    "                                function. Itu saja bedanya.",
                    "  yield nilai;               <- kirim satu nilai keluar, lalu",
                    "                                TIDUR di baris ini.",
                    "",
                    "Fungsi biasa, sekali dipanggil, harus jalan sampai selesai. Generator",
                    "beda. Tiap yield membekukan fungsi itu lengkap dengan semua variabel",
                    "lokalnya, dan .next() berikutnya membangunkannya lagi persis dari",
                    "baris itu. Perhatikan urutan cetakan di contoh: badan generator baru",
                    "mulai jalan waktu .next() pertama dipanggil, bukan waktu fungsinya",
                    "dipanggil.",
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
                "heading": "Jebakan generator dan tempat memakainya",
                "body": [
                    "Jebakan yang sering kena:",
                    "  1. Generator cuma sekali pakai. Sesudah done: true, dia habis",
                    "     selamanya.",
                    "       const g = tigaWarna();",
                    "       console.log([...g]);   // [ 'merah', 'hijau', 'biru' ]",
                    "       console.log([...g]);   // []  <- bukan bug, memang habis",
                    "     Mau mengulang? Panggil fungsinya lagi: [...tigaWarna()].",
                    "     Generator itu ibarat satu kali kunjungan, dan isinya nggak",
                    "     disimpan. Beda dengan array, yang isinya tetap ada dan bisa dibaca",
                    "     berkali-kali.",
                    "  2. Menyebar (spread) generator yang nggak ada habisnya bikin program",
                    "     menggantung. [...pembuatId()] terus meminta nilai sampai memori",
                    "     habis. Yang aman: ambil sejumlah tertentu lewat .next(), atau",
                    "     pakai for...of yang dihentikan dengan break.",
                    "  3. Lupa meminta. Baris hitungMundur(3); yang berdiri sendiri nggak",
                    "     mencetak apa-apa, dan nggak error juga. Orang jadi mengira kodenya",
                    "     rusak, padahal generator memang menunggu diminta. Harus ada",
                    "     .next(), for...of, spread, atau Array.from.",
                    "  4. return di dalam generator nggak jadi nilai terakhir yang kamu",
                    "     dapat. Nilainya muncul sebagai { value: ..., done: true } di",
                    "     .next(), tapi for...of dan spread membuang nilai yang datang",
                    "     bersama done: true. Kalau nilainya mau dibaca, pakai yield.",
                    "  5. Bintangnya nempel ke function, nggak ke nama. function* f() sama",
                    "     aja dengan function *f(). Untuk method di dalam class atau object,",
                    "     tulisannya *namaMethod() { ... }.",
                    "",
                    "Tempat generator muncul di kode nyata:",
                    "  - redux-saga (dunia React). Tiap alur efek samping ditulis sebagai",
                    "    function* dengan yield call(...) dan yield put(...). Makanya kode",
                    "    saga kelihatan asing kalau kamu belum kenal generator.",
                    "  - Pembuat id atau nomor urut yang nggak boleh kembar, seperti",
                    "    pembuatId.",
                    "  - Membaca data besar sepotong demi sepotong, misalnya berkas log baris",
                    "    demi baris, atau hasil query jutaan baris, tanpa menaruh semuanya di",
                    "    memori sekaligus.",
                    "  - Versi async-nya: async function* dipasangkan dengan",
                    "    for await (const x of ...) untuk membaca stream jaringan. Ini",
                    "    nyambung ke materi async/await.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Generator dipakai untuk barisan nilai yang dibuat sedikit demi",
                    "sedikit: nomor nota yang terus bertambah, atau berkas log besar yang",
                    "dibaca baris per baris. Nilainya baru dibuat saat diminta, jadi data",
                    "jutaan baris nggak perlu ditaruh di memori sekaligus.",
                    "",
                    "Kasus kecil: Toko Berkah butuh nomor nota TB-0001, TB-0002, dan",
                    "seterusnya. Nomornya nggak boleh kembar, dan nggak ada batas akhirnya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Barisan tanpa ujung nggak bisa disimpan sebagai array. Programnya",
                    "     cukup mengingat angka terakhir.",
                    "  2. Tulis generator yang menyimpan angka itu di variabel lokal dan",
                    "     menyerahkan satu nomor tiap diminta. padStart dari materi String",
                    "     menambahkan nol di depan.",
                    "      function* nomorNota(awalan) {",
                    "        let n = 1;",
                    "        while (true) yield `${awalan}-${String(n++).padStart(4, \"0\")}`;",
                    "      }",
                    "      const nota = nomorNota(\"TB\");",
                    "      console.log(nota.next().value, nota.next().value);   // TB-0001 TB-0002",
                    "  3. while (true) aman di sini, karena yield menjeda fungsinya. Badan",
                    "     generator cuma jalan sejauh nomor yang diminta.",
                    "  4. Kasus pinggir: [...nomorNota(\"TB\")] meminta nilai sampai habis,",
                    "     padahal generator ini nggak pernah habis, jadi programnya",
                    "     menggantung. Ambil secukupnya lewat next().",
                    "",
                    "Ingat: isi generator hilang waktu program berhenti. Aplikasi kasir",
                    "sungguhan menyimpan nomor terakhir di database, supaya besok pagi",
                    "nomornya nggak mulai dari TB-0001 lagi.",
                ]
            },
        ],
    },
    {
        "title": "18. Keyword 'this' & Context",
        "sections": [
            {
                "body": [
                    "this menunjuk ke \"objek pemilik\" dari kode yang sedang jalan. Yang",
                    "bikin pemula bingung: nilai this ditentukan oleh cara fungsinya",
                    "dipanggil, dan nggak peduli di mana fungsi itu ditulis.",
                    "",
                    "Aturan umum nilai this:",
                    "  1. Dipanggil sebagai method objek: this adalah objek itu.",
                    "  2. Dipanggil sebagai fungsi biasa: this bernilai undefined di strict",
                    "     mode, atau objek global kalau nggak strict. Yang kedua ini",
                    "     sebaiknya dihindari.",
                    "  3. Di dalam arrow function: arrow function nggak punya this sendiri,",
                    "     jadi dia mewarisi this dari scope di luarnya.",
                    "  4. Dipanggil pakai new: this adalah objek baru yang sedang dibikin.",
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
                    "Catatan untuk contoh Timer di atas: contoh itu pakai class (materi",
                    "'OOP: Class & Object') dan setInterval (materi 'Asynchronous",
                    "JavaScript: Callback'). Dua-duanya baru dibahas nanti. Sekarang cukup",
                    "perhatikan satu hal: arrow function di dalam setInterval bikin this",
                    "tetap menunjuk objek Timer-nya.",
                    "",
                    "call(), apply(), dan bind() dipakai untuk mengatur this secara",
                    "langsung:",
                    "  fungsi.call(objekThis, arg1, arg2)",
                    "      -> panggil langsung dengan this tertentu",
                    "  fungsi.apply(objekThis, [arg1, arg2])",
                    "      -> sama, tapi argumen dalam array",
                    "  fungsi.bind(objekThis)",
                    "      -> mengembalikan fungsi BARU dengan this yang sudah terikat",
                    "",
                    "Patokan praktisnya:",
                    "  - Method di dalam object atau class pakai function biasa, karena",
                    "    butuh this.",
                    "  - Callback (setTimeout, event handler, method array) pakai arrow",
                    "    function, supaya this tetap mengacu ke konteks luar yang benar.",
                ]
            },
            {
                "heading": "Apa yang berubah di strict mode",
                "body": [
                    "Aturan nomor 2 di atas menyebut strict mode sekilas, padahal seluruh",
                    "perilaku this bergantung padanya. Ini penjelasannya.",
                    "",
                    "Strict mode adalah sekumpulan aturan yang lebih ketat. Cara",
                    "menyalakannya: tulis satu baris berisi \"use strict\"; di paling atas",
                    "sebuah berkas (berlaku untuk seluruh berkas), atau di paling atas",
                    "sebuah fungsi (berlaku untuk fungsi itu aja). Baris itu harus jadi",
                    "pernyataan pertama. Kalau ditaruh di tengah, dia cuma jadi string yang",
                    "nggak ada gunanya.",
                    "",
                    "Tiga perubahan yang paling kerasa:",
                    "  1. this bernilai undefined di fungsi biasa yang dipanggil tanpa",
                    "     objek. Tanpa strict, this berubah jadi objek global tanpa bilang",
                    "     apa-apa, dan dari situ muncul bug \"kok nilainya nyasar ke",
                    "     mana-mana\".",
                    "  2. Mengisi variabel yang belum pernah dideklarasikan jadi",
                    "     ReferenceError. Tanpa strict, salah ketik nama variabel bakal",
                    "     bikin variabel global baru tanpa ngasih tahu siapa pun.",
                    "  3. Perubahan yang dulu gagal tanpa suara sekarang melempar error.",
                    "     Misalnya menulis ke object yang sudah di-Object.freeze().",
                    "",
                    "Makanya berkas Node lama sering dibuka dengan baris \"use strict\";, dan",
                    "kode di dalam IIFE juga sering diawali baris yang sama.",
                    "",
                    "Kabar baiknya, kamu makin jarang perlu menulisnya. ES Module (berkas",
                    "dengan import/export) dan seluruh isi class selalu dalam strict mode.",
                    "Nggak perlu ditulis, dan nggak bisa dimatikan.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Masalah this paling sering muncul waktu sebuah method diserahkan ke",
                    "kode lain: dipasang sebagai handler tombol, dikirim ke setTimeout, atau",
                    "dioper sebagai callback. Di aplikasi kasir berbasis web, method",
                    "keranjang.tambah yang dipasang langsung ke tombol tiba-tiba nggak",
                    "kenal keranjangnya sendiri.",
                    "",
                    "Kasus kecil: object keranjang punya array isi dan method",
                    "tambah(barang). Kode lain menerima method itu sebagai callback, lalu",
                    "memanggilnya: const pasang = keranjang.tambah; pasang(\"Kopi\").",
                    "Hasilnya TypeError, padahal keranjang.tambah(\"Kopi\") jalan normal.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat cara fungsinya dipanggil. pasang(\"Kopi\") nggak punya objek",
                    "     di depan titik, jadi this di dalamnya sudah bukan keranjang.",
                    "  2. Ikat this-nya sebelum method itu diserahkan, pakai bind:",
                    "      const keranjang = {",
                    "        isi: [],",
                    "        tambah(barang) { this.isi.push(barang); },",
                    "      };",
                    "      const pasang = keranjang.tambah.bind(keranjang);",
                    "      pasang(\"Kopi\");   // keranjang.isi sekarang [ 'Kopi' ]",
                    "  3. Cara lain yang sama benarnya: bungkus dengan arrow function,",
                    "     const pasang = (b) => keranjang.tambah(b). Pemanggilan di dalamnya",
                    "     punya objek di depan titik.",
                    "  4. Kasus pinggir: jangan mengubah tambah jadi arrow function di dalam",
                    "     object literal. Arrow nggak punya this sendiri, jadi this.isi",
                    "     menunjuk scope luar dan errornya tetap muncul.",
                ]
            },
        ],
    },
    {
        "title": "19. OOP: Class & Object (ES6+)",
        "sections": [
            {
                "body": [
                    "OOP (Object-Oriented Programming) adalah cara menyusun program sebagai",
                    "kumpulan objek yang punya data dan perilaku sendiri. ES6 (2015)",
                    "mengenalkan sintaks class yang lebih mirip Java dan Python. Di balik",
                    "layar, JavaScript tetap pakai prototype, yang dibahas di materi",
                    "berikutnya.",
                    "",
                    "  class NamaClass {",
                    "      constructor(param) {",
                    "          this.atribut = param;",
                    "      }",
                    "      method() {",
                    "          console.log(this.atribut);",
                    "      }",
                    "  }",
                    "",
                    "constructor adalah method khusus yang dijalankan waktu objek baru",
                    "dibikin pakai new.",
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
                    "Catatan: throw new Error di setter di atas memang sengaja melempar",
                    "error. Cara menangkapnya dibahas di materi 'Exception Handling'.",
                    "",
                    "Badan class masih punya beberapa bentuk lain. Bentuk-bentuk ini lebih",
                    "sering muncul daripada #privateField, tapi susah ditebak kalau yang",
                    "diajarkan cuma constructor dan method:",
                    "  1. Class field publik: hitung = 0; atau items = []; ditulis langsung",
                    "     di badan class, tanpa kata kunci apa pun. Tiap objek baru otomatis",
                    "     dapat field ini, jadi constructor nggak perlu mengulanginya.",
                    "     Perhatikan, items = [] memberi array baru untuk tiap objek. Memang",
                    "     itu yang kita mau, jadi nggak ada satu array yang dipakai bareng.",
                    "  2. Static field: static jumlah = 0; adalah milik class-nya sendiri,",
                    "     dan bukan milik tiap objek. Cara bacanya lewat nama class:",
                    "     Keranjang.jumlah.",
                    "  3. Arrow function sebagai class property: handleKlik = () => {...};",
                    "     Arrow mewarisi this dari tempat dia dibuat. Jadi method bentuk ini",
                    "     tetap benar walau dilepas dari objeknya, lalu diserahkan ke tombol,",
                    "     timer, atau event listener. Ini cara baku mengikat this di",
                    "     komponen, sebagai pengganti bind() di constructor.",
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
                    "Terakhir, super(nama) di contoh Anjing tadi memanggil constructor",
                    "induknya. super punya bentuk kedua yang malah lebih sering dipakai,",
                    "yaitu super.namaMethod(). Bentuk ini memanggil versi induk dari method",
                    "yang sedang kamu timpa (override).",
                    "",
                    "Bedanya besar. Override tanpa super.method() mengganti perilaku induk",
                    "seluruhnya. Itu yang dilakukan Kucing dan Anjing di contoh sebelumnya.",
                    "Override dengan super.method() memperluas perilaku induk: kerjakan dulu",
                    "yang dikerjakan induk, baru tambahkan bagianmu. Pola ini ada di",
                    "mana-mana di kode yang pakai class, misalnya method yang perlu",
                    "menjalankan versi dasarnya dulu sebelum menambahkan langkah khusus.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Class dipakai kalau aplikasi punya banyak benda sejenis dengan aturan",
                    "yang sama: rekening di aplikasi bank, produk di toko online, kendaraan",
                    "di sistem parkir. Aturannya ditulis sekali di class, dan tiap objek",
                    "membawa datanya sendiri.",
                    "",
                    "Kasus kecil: sistem parkir mal menarik Rp 2.000 per jam untuk motor",
                    "dan Rp 5.000 per jam untuk mobil. Jam yang belum penuh dihitung satu",
                    "jam. Sebuah mobil parkir 135 menit.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari bagian yang sama dan yang beda. Semua kendaraan punya plat",
                    "     dan lama parkir, dan cara membulatkan jamnya sama. Yang beda cuma",
                    "     tarif per jam.",
                    "  2. Taruh yang sama di class induk, dan tarifnya di class turunan:",
                    "      class Kendaraan {",
                    "        constructor(plat, menit) { this.plat = plat; this.menit = menit; }",
                    "        biaya() { return Math.ceil(this.menit / 60) * this.tarif; }",
                    "      }",
                    "      class Mobil extends Kendaraan { tarif = 5000; }",
                    "      console.log(new Mobil(\"AB 1234 CD\", 135).biaya());   // 15000",
                    "  3. 135 menit jadi 3 jam sesudah dibulatkan ke atas, jadi 15000. Motor",
                    "     cukup satu baris lagi:",
                    "     class Motor extends Kendaraan { tarif = 2000; }.",
                    "     Kalau tarif mobil naik, yang diubah cuma satu angka.",
                    "  4. Kasus pinggir: kendaraan keluar lagi di menit yang sama karena",
                    "     salah masuk. Math.ceil(0) memberi 0, jadi biayanya 0. Kalau aturan",
                    "     mal tetap menagih satu jam, pakai Math.max(1, ...) untuk jamnya.",
                ]
            },
        ],
    },
    {
        "title": "20. Prototype: OOP di Balik Layar JavaScript",
        "sections": [
            {
                "body": [
                    "Sebelum ada class (ES6), JavaScript sudah punya OOP lewat prototype.",
                    "class yang kamu pelajari di materi sebelumnya cuma syntactic sugar,",
                    "yaitu cara nulis yang lebih rapi di atas mekanisme prototype ini.",
                    "",
                    "Hampir setiap objek JS punya property tersembunyi bernama __proto__.",
                    "Property ini menunjuk ke objek lain, yang disebut prototype-nya. Kalau",
                    "sebuah property atau method nggak ketemu di objek itu sendiri, JS",
                    "mencarinya di prototype-nya. Kalau masih nggak ketemu, JS lanjut ke",
                    "prototype dari prototype-nya, dan seterusnya. Rantai pencarian ini",
                    "disebut prototype chain.",
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
                    "Kenapa method ditaruh di prototype, dan nggak di dalam constructor?",
                    "  - Lebih hemat memori. Satu method dipakai bareng oleh semua instance",
                    "    (objek yang dibikin dari constructor itu), jadi nggak perlu disalin",
                    "    ulang tiap kali objek baru dibikin.",
                    "  - Ini juga alasan method di class otomatis pakai mekanisme yang sama.",
                    "",
                    "Object.create() bikin objek dengan prototype tertentu secara langsung,",
                    "tanpa function constructor:",
                    "  const hewanProto = { bersuara() { console.log('...'); } };",
                    "  const kucing = Object.create(hewanProto);",
                    "",
                    "Di JS modern, kamu nggak wajib menulis kode prototype sendiri. Cukup",
                    "pakai class. Tapi kalau paham konsepnya, kamu bisa mengerti error atau",
                    "perilaku aneh, dan bisa membaca kode JS yang lebih lama.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kamu jarang menulis prototype sendiri, tapi kamu memakainya setiap",
                    "kali memanggil method bawaan. [3, 1, 2].sort() dan \"halo\".toUpperCase()",
                    "jalan karena JavaScript menemukan method itu di Array.prototype dan",
                    "String.prototype lewat prototype chain. Kode lama dan library yang",
                    "lahir sebelum class juga ditulis dengan pola function dan prototype.",
                    "",
                    "Kasus kecil: kamu meneruskan kode lama aplikasi koperasi sekolah. Di",
                    "situ ada function Anggota(nama, simpanan) yang mengisi this.nama dan",
                    "this.simpanan, dan beberapa objek anggota sudah telanjur dibuat. Kamu",
                    "perlu menambah method info() yang mengembalikan teks \"Ani: Rp 50000\".",
                    "",
                    "Cara memecahkannya:",
                    "  1. Lihat di mana method lain ditaruh. Kalau ditulis",
                    "     Anggota.prototype.namaMethod = function ..., ikuti pola yang sama",
                    "     supaya kodenya seragam.",
                    "  2. Tambahkan method-nya di prototype. Semua objek mencari method",
                    "     lewat rantai yang sama, jadi objek yang dibuat lebih dulu pun ikut",
                    "     mendapatkannya:",
                    "      const ani = new Anggota(\"Ani\", 50000);   // dibuat sebelum info ada",
                    "      Anggota.prototype.info = function () {",
                    "        return `${this.nama}: Rp ${this.simpanan}`;",
                    "      };",
                    "      console.log(ani.info());   // Ani: Rp 50000",
                    "  3. Pakai function biasa, jangan arrow. Method di prototype butuh this",
                    "     yang menunjuk objek pemanggilnya, dan arrow nggak punya this",
                    "     sendiri.",
                    "  4. Kasus pinggir: kalau sebuah objek punya property info miliknya",
                    "     sendiri, property itu ditemukan duluan dan method di prototype",
                    "     nggak pernah terpanggil. Cek pakai Object.hasOwn(objek, \"info\").",
                ]
            },
        ],
    },
    {
        "title": "21. Exception Handling",
        "sections": [
            {
                "body": [
                    "Exception adalah error yang terjadi waktu program jalan. Di",
                    "JavaScript, error bisa ditangani pakai try-catch-finally, mirip bahasa",
                    "lain.",
                    "",
                    "  try {",
                    "      // kode yang mungkin error",
                    "  } catch (error) {",
                    "      // penanganan error",
                    "  } finally {",
                    "      // selalu jalan, error atau tidak",
                    "  }",
                    "",
                    "Error bawaan yang sering ketemu:",
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
                    "Contoh di atas pakai satu operator yang belum dijelaskan: instanceof.",
                    "Operator ini saudara typeof yang kamu pelajari di materi Variabel, tapi",
                    "pertanyaan yang dijawabnya beda.",
                    "",
                    "  typeof x       tipe DASAR x, hasilnya string: \"number\", \"string\", ...",
                    "  x instanceof C apakah x lahir dari class/constructor C? hasilnya boolean",
                    "",
                    "typeof mentok begitu ketemu object. Array, Date, dan semua jenis Error",
                    "sama-sama dijawab \"object\". Untuk membedakan mereka, pakai instanceof.",
                    "Makanya instanceof sering muncul di dalam catch, tempat kita perlu tahu",
                    "jenis error apa yang barusan tertangkap.",
                    "",
                    "Ingat: turunan juga cocok dengan induknya (TypeError instanceof Error",
                    "hasilnya true). Jadi urutan pemeriksaannya harus dari yang paling",
                    "khusus ke yang paling umum. Kalau kebalik, cabang yang khusus nggak",
                    "akan pernah tercapai.",
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
                    "Ada empat hal kecil yang melengkapi try-catch, dan satu hal besar.",
                    "Yang kecil dulu:",
                    "  - catch tanpa binding. Sejak ES2019 kamu boleh nulis catch { ... }",
                    "    tanpa (e), kalau errornya memang nggak dipakai.",
                    "  - error.stack, yaitu jejak pemanggilan sampai titik error terjadi.",
                    "    Baris pertamanya nama dan pesan error, sisanya daftar fungsi yang",
                    "    sedang jalan. Bagian ini yang pertama kamu baca waktu program",
                    "    gagal.",
                    "  - error.cause (ES2022) membungkus error asli tanpa menghilangkannya,",
                    "    lewat argumen kedua: new Error(pesan, { cause: errorAsli }). Tanpa",
                    "    cause, membungkus error berarti membuang penyebab aslinya.",
                    "  - throw bisa melempar nilai apa aja: string, angka, atau object",
                    "    polos. Jangan lakukan itu. Nilai yang bukan Error nggak punya",
                    "    .message dan .stack, jadi jejaknya hilang, dan catch di atasnya",
                    "    nggak bisa ngecek jenisnya.",
                    "",
                    "Hal yang besar: try-catch biasa nggak menangkap error dari Promise.",
                    "Promise adalah nilai yang hasilnya baru datang nanti, dan dibahas di",
                    "materi berikutnya. Kalau sebuah Promise ditolak dan nggak ada .catch()",
                    "atau await di dalam try-catch yang menangkapnya, terjadilah unhandled",
                    "rejection. Di browser, dia muncul sebagai peringatan merah di Console.",
                    "Di Node, program langsung berhenti dengan kode keluar 1.",
                    "",
                    "Yang tercetak tergantung apa yang ditolak. Kalau yang ditolak sebuah",
                    "Error, Node mencetak Error itu beserta stack-nya apa adanya. Kalau",
                    "bukan Error, barulah muncul UnhandledPromiseRejection dengan",
                    "code: 'ERR_UNHANDLED_REJECTION'.",
                    "",
                    "Cara menghindarinya dibahas di materi Promise dan async/await.",
                    "Intinya, tiap rantai Promise harus berujung di .catch(), atau tiap",
                    "await harus ada di dalam try-catch.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program sungguhan cepat atau lambat ketemu data yang salah: berkas",
                    "konfigurasi rusak, isian form ngawur, saldo yang nggak cukup. Aplikasi",
                    "bank nggak boleh berhenti total gara-gara satu transfer gagal.",
                    "Transfernya ditolak dengan pesan yang jelas, dan aplikasinya tetap",
                    "jalan untuk transaksi berikutnya.",
                    "",
                    "Kasus kecil: fungsi transfer menerima saldo dan jumlah. Jumlah harus",
                    "angka positif dan nggak boleh melebihi saldo. Kalau ditolak, pengguna",
                    "harus tahu sebabnya, dan error lain yang nggak terduga jangan sampai",
                    "tertelan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dua jenis kegagalan. Yang memang bisa terjadi (jumlah",
                    "     ngawur, saldo kurang) dijelaskan ke pengguna. Yang nggak terduga,",
                    "     misalnya bug di kode, dilempar ulang supaya ketahuan.",
                    "  2. Buat class error sendiri untuk kegagalan yang terduga:",
                    "      class GagalTransfer extends Error {}",
                    "      function transfer(saldo, jumlah) {",
                    "        if (!(jumlah > 0)) throw new GagalTransfer(\"Jumlah tidak valid\");",
                    "        if (jumlah > saldo) throw new GagalTransfer(\"Saldo tidak cukup\");",
                    "        return saldo - jumlah;",
                    "      }",
                    "  3. Di pemanggilnya, bungkus dengan try-catch. Di dalam catch, cek",
                    "     e instanceof GagalTransfer. Kalau cocok, tampilkan e.message ke",
                    "     pengguna. Kalau nggak, throw e lagi.",
                    "  4. Kasus pinggir: jumlah dari form yang gagal dikonversi jadi NaN.",
                    "     NaN > 0 bernilai false, jadi !(jumlah > 0) ikut menolaknya. Kalau",
                    "     syaratnya ditulis jumlah <= 0, NaN lolos, karena NaN <= 0 juga",
                    "     false.",
                ]
            },
        ],
    },
    {
        "title": "22. Asynchronous JavaScript: Callback",
        "sections": [
            {
                "body": [
                    "JavaScript itu single-threaded, artinya cuma punya satu jalur untuk",
                    "menjalankan kode. Walau begitu, dia bisa menangani pekerjaan yang lama,",
                    "seperti request ke jaringan, timer, atau membaca berkas, tanpa bikin",
                    "program macet. Caranya pakai model asynchronous: pekerjaan lama",
                    "ditinggal jalan, dan program lanjut ke baris berikutnya.",
                    "",
                    "Callback adalah fungsi yang dikirim sebagai argumen ke fungsi lain,",
                    "untuk dijalankan nanti sesudah sebuah proses selesai.",
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
                "heading": "Event loop, call stack, dan antrean callback",
                "body": [
                    "Mesin di balik async JS namanya event loop. Cara kerjanya begini:",
                    "  1. Call stack menjalankan kode sinkron (yang jalan berurutan) satu",
                    "     per satu.",
                    "  2. Pekerjaan async (setTimeout, fetch, dan lainnya) diserahkan ke Web",
                    "     API milik browser atau ke API milik Node, jadi call stack nggak",
                    "     ikut tertahan.",
                    "  3. Sesudah pekerjaan itu selesai, callback-nya masuk ke antrean",
                    "     (queue).",
                    "  4. Event loop memindahkan callback dari antrean ke call stack, tapi",
                    "     cuma kalau call stack sedang kosong.",
                    "",
                    "Makanya setTimeout(fn, 0) tetap jalan sesudah semua kode sinkron",
                    "selesai, walau jedanya 0 milidetik.",
                    "",
                    "Ada satu koreksi penting untuk poin 3: antreannya ada dua.",
                    "",
                    "  Antrean MICROTASK  -> Promise.then/catch/finally, await, queueMicrotask",
                    "  Antrean MACROTASK  -> setTimeout, setInterval, event I/O, event DOM",
                    "",
                    "Aturannya: setiap kali call stack kosong, event loop menghabiskan dulu",
                    "seluruh antrean microtask, termasuk microtask baru yang muncul di",
                    "tengah proses. Sesudah itu baru dia mengambil satu macrotask.",
                    "",
                    "Akibatnya langsung kerasa: Promise.then selalu jalan lebih dulu",
                    "daripada setTimeout(fn, 0), walau setTimeout ditulis di baris atasnya.",
                    "Kalau kamu pakai gambaran satu antrean, kesimpulanmu bakal terbalik.",
                ]
            },
            {
                "heading": "Membatalkan timer: clearTimeout & clearInterval",
                "body": [
                    "setTimeout dan setInterval punya satu sifat yang belum disebut.",
                    "Sifat ini yang bikin keduanya bisa dikendalikan:",
                    "",
                    "  const id = setTimeout(fn, 1000);   -> setTimeout MENGEMBALIKAN id",
                    "  clearTimeout(id);                  -> batalkan sebelum waktunya tiba",
                    "",
                    "  const id2 = setInterval(fn, 1000); -> ulang TERUS tiap 1000 ms",
                    "  clearInterval(id2);                -> satu-satunya cara menghentikannya",
                    "",
                    "setInterval nggak pernah berhenti sendiri. Contoh class Timer di",
                    "materi \"Keyword 'this' & Context\" bakal mencetak angka terus sampai",
                    "programnya dimatikan. Di sana nggak ada clearInterval, dan id-nya",
                    "bahkan nggak disimpan. Biasakan setiap setInterval punya syarat",
                    "berhenti yang jelas.",
                    "",
                    "Pasangan \"simpan id, lalu batalkan\" ini jadi dasar pola debounce.",
                    "Debounce menunda sebuah tindakan sampai orangnya berhenti mengetik,",
                    "caranya dengan membatalkan timer lama tiap kali ada ketikan baru. Kamu",
                    "bakal membangunnya sendiri di Latihan 16.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Timer dan callback ada di fitur yang kelihatan sepele. Contohnya hitung",
                    "mundur \"kirim ulang kode OTP dalam 60 detik\", notifikasi yang hilang",
                    "sendiri sesudah 3 detik, atau kotak pencarian yang baru mencari setelah",
                    "kamu berhenti mengetik.",
                    "",
                    "Kasus kecil: halaman verifikasi OTP menampilkan hitung mundur sebelum",
                    "tombol kirim ulang aktif. Di aplikasi sungguhan bisa 60 detik, di sini",
                    "5 detik supaya cepat dicoba. Angkanya harus turun tiap detik dan",
                    "berhenti di 0.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kejadiannya berulang tiap detik dan harus berhenti sendiri. Itu",
                    "     tugas setInterval, dengan id yang disimpan untuk clearInterval.",
                    "  2. Simpan sisa waktu di variabel, kurangi di tiap detak, dan tulis",
                    "     syarat berhentinya di dalam callback:",
                    "      let sisa = 5;",
                    "      const id = setInterval(() => {",
                    "        sisa--;",
                    "        console.log(sisa > 0 ? `tunggu ${sisa} detik` : \"kirim ulang aktif\");",
                    "        if (sisa === 0) clearInterval(id);",
                    "      }, 1000);",
                    "  3. Hitung baris keluarannya: tunggu 4 detik, 3, 2, 1, lalu kirim",
                    "     ulang aktif. Lima baris, lalu program selesai sendiri karena nggak",
                    "     ada timer yang tersisa.",
                    "  4. Kasus pinggir: pengguna menekan kirim ulang lagi sebelum hitungan",
                    "     habis. Kalau tiap tekan memanggil setInterval baru tanpa",
                    "     clearInterval yang lama, dua timer jalan bersamaan dan angkanya",
                    "     turun dua kali lebih cepat. Batalkan timer lama dulu.",
                ]
            },
        ],
    },
    {
        "title": "23. Asynchronous JavaScript: Promise",
        "sections": [
            {
                "body": [
                    "Promise adalah objek yang mewakili hasil dari pekerjaan asynchronous",
                    "yang belum tentu sudah selesai. Ibaratnya nomor antrean: hasilnya",
                    "belum ada sekarang, tapi nanti pasti ada kabar. Akhirnya bisa sukses",
                    "(resolve) atau gagal (reject). Promise jadi solusi untuk masalah",
                    "Callback Hell, yaitu callback yang bersarang makin lama makin dalam.",
                    "",
                    "Promise punya 3 status:",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir setiap aksi yang menunggu sesuatu di luar program berupa",
                    "Promise: mengambil data dari server, membaca berkas, mengecek status",
                    "pembayaran. Dasbor toko online memuat beberapa data sekaligus, lalu",
                    "menampilkan apa pun yang berhasil dimuat.",
                    "",
                    "Kasus kecil: dasbor memuat data penjualan dan data stok dari dua",
                    "sumber berbeda. Sumber stok sedang gangguan. Dengan Promise.all,",
                    "seluruh dasbor gagal tampil cuma karena satu sumber yang bermasalah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan perilaku yang diinginkan: data yang berhasil tetap",
                    "     tampil, dan yang gagal diberi tanda gangguan.",
                    "  2. Pilih alatnya. Promise.all langsung gagal begitu satu Promise",
                    "     ditolak. Promise.allSettled menunggu semuanya, lalu melaporkan",
                    "     status masing-masing.",
                    "  3. Coba dengan tiruan dua sumber. Promise.resolve dan Promise.reject",
                    "     membuat Promise yang langsung selesai, cocok untuk mencoba:",
                    "      const muat = (nama, ok) => ok",
                    "        ? Promise.resolve(nama)",
                    "        : Promise.reject(new Error(nama + \" gangguan\"));",
                    "      const semua = [muat(\"penjualan\", true), muat(\"stok\", false)];",
                    "      Promise.allSettled(semua).then((hasil) => hasil.forEach((h) =>",
                    "        console.log(h.status, h.value ?? h.reason.message)));",
                    "     Hasilnya dua baris: fulfilled penjualan, lalu rejected stok",
                    "     gangguan.",
                    "  4. Kasus pinggir: kalau data kedua butuh hasil data pertama, misalnya",
                    "     detail pesanan butuh id dari daftar pesanan, keduanya nggak bisa",
                    "     dimuat bersamaan. Rangkai pakai .then yang mengembalikan Promise",
                    "     berikutnya.",
                ]
            },
        ],
    },
    {
        "title": "24. Asynchronous JavaScript: async/await",
        "sections": [
            {
                "body": [
                    "async/await (ES2017) adalah cara menulis kode asynchronous supaya",
                    "kelihatan seperti kode sinkron biasa. Hasilnya jauh lebih gampang",
                    "dibaca daripada .then().then().then() yang berantai.",
                    "",
                    "Aturan dasarnya:",
                    "  1. Fungsi yang memakai await harus ditandai async.",
                    "  2. await cuma bisa dipakai di dalam fungsi async, atau di level",
                    "     paling atas sebuah ES Module.",
                    "  3. await \"menjeda\" fungsinya sampai Promise selesai, tanpa bikin",
                    "     jalur utama JavaScript ikut tertahan.",
                    "  4. Fungsi async selalu mengembalikan sebuah Promise.",
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
                "heading": "Menjalankan beberapa Promise paralel dengan async/await",
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
                    "Kapan pakai await satu per satu, dan kapan pakai Promise.all:",
                    "  - Satu per satu (berurutan) kalau pekerjaan kedua butuh hasil dari",
                    "    pekerjaan pertama, alias saling bergantung.",
                    "  - Promise.all (paralel) kalau pekerjaan-pekerjaannya nggak saling",
                    "    bergantung. Cara ini jauh lebih cepat, karena semuanya jalan",
                    "    bersamaan.",
                    "",
                    "async/await sudah jadi standar di JavaScript modern. Hampir semua kode",
                    "async di aplikasi sungguhan pakai async/await, dan jarang pakai",
                    ".then().",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kode yang menunggu server, database, atau berkas di aplikasi sungguhan",
                    "sekarang umumnya ditulis dengan async/await. Kodenya dibaca dari atas",
                    "ke bawah seperti urutan kerja. Kesalahan yang paling sering di sini",
                    "soal kecepatan: permintaan ditunggu bergantian, padahal semuanya bisa",
                    "ditunggu bersamaan.",
                    "",
                    "Kasus kecil: halaman pembayaran butuh tiga data: profil pembeli,",
                    "daftar promo, dan saldo dompet digital. Ketiganya nggak saling",
                    "bergantung, dan masing-masing butuh sekitar 1 detik. Versi pertama",
                    "memakai tiga await berurutan, dan halamannya baru muncul sesudah 3",
                    "detik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek ketergantungannya dulu. Kalau data kedua butuh hasil data",
                    "     pertama, tunggu satu per satu. Di sini ketiganya berdiri sendiri.",
                    "  2. Mulai ketiganya sekaligus, lalu tunggu bersamaan pakai",
                    "     Promise.all. tunda di bawah meniru permintaan yang butuh 1 detik:",
                    "      const tunda = (v) => new Promise((ok) => setTimeout(() => ok(v), 1000));",
                    "      (async () => {",
                    "        const semua = [tunda(\"Rina\"), tunda(\"gratis ongkir\"), tunda(75000)];",
                    "        const [profil, promo, saldo] = await Promise.all(semua);",
                    "        console.log(profil, promo, saldo);   // sesudah sekitar 1 detik",
                    "      })();",
                    "  3. Ketiga timer mulai di baris yang sama, jadi total tunggunya",
                    "     sekitar 1 detik. Tiga await berurutan butuh sekitar 3 detik.",
                    "  4. Kasus pinggir: satu permintaan gagal. Promise.all ikut gagal, dan",
                    "     await melempar error. Bungkus dengan try-catch supaya halaman bisa",
                    "     menampilkan pesan, dan nggak macet di layar memuat.",
                ]
            },
        ],
    },
    {
        "title": "25. DOM Manipulation & Event Dasar",
        "sections": [
            {
                "body": [
                    "DOM (Document Object Model) adalah struktur halaman HTML yang disimpan",
                    "browser sebagai objek, sehingga bisa dibaca dan diubah lewat",
                    "JavaScript. Lewat DOM, halaman web jadi interaktif: bisa berubah waktu",
                    "diklik, diketik, atau dikirim.",
                    "",
                    "Catatan: materi ini cuma berlaku di browser. Node.js nggak punya",
                    "halaman HTML, jadi nggak punya DOM juga.",
                    "",
                    "Cara memilih elemen HTML:",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setiap halaman web yang berubah tanpa dimuat ulang memakai DOM.",
                    "Contohnya angka di ikon keranjang yang naik, pesan peringatan di bawah",
                    "kotak isian, atau tombol yang jadi abu-abu sesudah diklik.",
                    "",
                    "Kasus kecil: halaman pesan makanan punya tombol \"Tambah porsi\" dengan",
                    "id tambah, dan angka porsi di <span id=\"jumlah\">. Tiap klik menambah",
                    "satu porsi, maksimal 10. Kalau sudah 10 lalu tombolnya diklik lagi,",
                    "angkanya diberi class penuh supaya tampil merah lewat CSS.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan sumber datanya. Simpan jumlah di variabel JavaScript,",
                    "     lalu tulis ke halaman tiap kali berubah. Angkanya nggak perlu",
                    "     dibaca balik dari teks di layar.",
                    "  2. Pilih elemennya sekali di luar listener, lalu pasang listener",
                    "     click di tombolnya:",
                    "      let jumlah = 0;",
                    "      const label = document.querySelector(\"#jumlah\");",
                    "      document.querySelector(\"#tambah\").addEventListener(\"click\", () => {",
                    "        if (jumlah < 10) { jumlah++; label.textContent = jumlah; }",
                    "        else label.classList.add(\"penuh\");",
                    "      });",
                    "  3. JavaScript cuma memasang class-nya. Warna merahnya diatur di CSS,",
                    "     jadi kalau desainnya berubah, kode ini nggak perlu disentuh.",
                    "  4. Kasus pinggir: pengguna mengklik cepat 15 kali. jumlah tetap",
                    "     berhenti di 10, karena syaratnya dicek di setiap klik sebelum",
                    "     menambah.",
                ]
            },
        ],
    },
    {
        "title": "26. Form, Atribut, dan Event Lanjutan",
        "sections": [
            {
                "body": [
                    "Materi sebelumnya mengajarkan cara menulis ke halaman: textContent,",
                    "style, classList, createElement. Yang belum dibahas sama sekali: cara",
                    "membaca dari halaman. Akibatnya kamu bisa tahu sebuah form dikirim,",
                    "tapi nggak tahu isinya apa.",
                    "",
                    "Jebakan nomor satu: querySelector mengembalikan null.",
                    "",
                    "Browser membaca HTML dari atas ke bawah. <script> di dalam <head>",
                    "dijalankan sebelum <body> dibaca, jadi elemen yang dicari memang belum",
                    "ada. Di console muncul pesan \"Cannot read properties of null (reading",
                    "'addEventListener')\". Selektormu nggak salah. Kodenya cuma jalan",
                    "kepagian.",
                    "",
                    "Ada tiga cara yang benar. Pilih salah satu:",
                    "  1. <script defer src=\"app.js\"></script> di dalam <head>. Ini cara",
                    "     yang paling dianjurkan.",
                    "  2. <script src=\"app.js\"></script> tepat sebelum </body>.",
                    "  3. document.addEventListener(\"DOMContentLoaded\", () => { ... });",
                    "",
                    "defer cuma berlaku untuk <script src=...>. <script> yang isinya ditulis",
                    "langsung di HTML nggak peduli defer. DOMContentLoaded menyala waktu",
                    "seluruh HTML selesai dibaca. Jangan ketuker dengan event \"load\", yang",
                    "masih menunggu semua gambar selesai dimuat. Biasanya itu jauh terlalu",
                    "lambat untuk memasang listener.",
                    "",
                    "Cara membaca tiap kontrol form:",
                    "  <input type=\"text\">      el.value     -> string",
                    "  <input type=\"number\">    el.value     -> TETAP string (\"12\", bukan 12)",
                    "  <textarea>               el.value     -> string (BUKAN textContent)",
                    "  <select>                 el.value     -> value dari <option> terpilih",
                    "  <input type=\"checkbox\">  el.checked   -> boolean; .value hampir tak",
                    "                                           berguna",
                    "  <input type=\"radio\">     cari dulu yang terpilih, baru baca .value:",
                    "      document.querySelector('input[name=\"jk\"]:checked')",
                    "          -> null kalau belum dipilih",
                    "",
                    "el.value selalu string, termasuk dari type=\"number\". Kamu wajib",
                    "mengonversinya sendiri (lihat materi konversi tipe). Contoh berikutnya",
                    "menunjukkan akibatnya kalau lupa.",
                    "",
                    "Kecuali satu contoh yang ditandai, semua kode di materi ini jalan di",
                    "browser. Kalau dijalankan pakai node, hasilnya \"ReferenceError:",
                    "document is not defined\", karena node nggak punya halaman untuk dibaca.",
                    "Cara memakainya: simpan sebagai app.js, tautkan pakai",
                    "<script defer src=\"app.js\">, lalu buka berkas HTML-nya di browser.",
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
                    "Contoh di bawah butuh HTML ini. Simpan sebagai index.html:",
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
                    "Atribut dan properti sering bikin bingung waktu debug:",
                    "  - Atribut adalah apa yang tertulis di HTML. Cara bacanya",
                    "    el.getAttribute(\"value\").",
                    "  - Properti adalah keadaan objeknya sekarang. Cara bacanya el.value.",
                    "",
                    "Begitu pengguna mengetik, el.value berubah, tapi getAttribute(\"value\")",
                    "tetap \"1\" selamanya. Nilai awal itu juga tersedia sebagai",
                    "el.defaultValue, dan el.defaultChecked untuk checkbox. Nilai itulah",
                    "yang dipasang lagi oleh form.reset().",
                    "",
                    "Ada empat fungsi untuk atribut apa pun, termasuk atribut yang nggak",
                    "punya properti sendiri:",
                    "  el.getAttribute(\"href\")",
                    "      baca; null kalau atributnya memang tidak ada",
                    "  el.setAttribute(\"disabled\", \"\")",
                    "      pasang (atribut boolean cukup diisi string kosong)",
                    "  el.removeAttribute(\"disabled\")",
                    "      copot",
                    "  el.hasAttribute(\"disabled\")",
                    "      true/false",
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
                    "textContent dan innerHTML sama-sama mengisi elemen, tapi akibatnya",
                    "jauh beda:",
                    "  el.textContent = \"<b>halo</b>\"",
                    "      -> pengguna melihat tulisan <b>halo</b> apa adanya",
                    "  el.innerHTML   = \"<b>halo</b>\"",
                    "      -> browser MEMBUAT elemen <b>, halo jadi tebal",
                    "",
                    "innerHTML memang membangun elemen. Jadi memasukkan teks dari",
                    "pengguna ke dalamnya sama aja dengan mengizinkan pengguna menulis HTML",
                    "di halamanmu. Itulah XSS (Cross-Site Scripting). Satu komentar berisi",
                    "<img src=x onerror=\"...\"> sudah cukup untuk menjalankan kode di browser",
                    "pengunjung lain. Aturan praktisnya:",
                    "  - innerHTML cuma untuk template yang kamu tulis sendiri.",
                    "  - Untuk isi yang datang dari pengguna, pakai textContent. Atau ubah",
                    "    dulu karakter < > & \" jadi entitas, seperti fungsi escapeHtml di",
                    "    contoh.",
                    "",
                    "insertAdjacentHTML menyisipkan HTML tanpa menyentuh isi yang sudah",
                    "ada. el.innerHTML += ... kelihatannya sama, padahal dia membangun ulang",
                    "seluruh isi. Elemen lama dibuang lalu dibikin lagi, jadi listener yang",
                    "menempel di situ hilang, dan ketikan yang sedang diisi di dalam <input>",
                    "ikut terhapus.",
                    "",
                    "insertAdjacentHTML punya empat posisi:",
                    "  \"beforebegin\" sebelum elemen        \"afterbegin\" jadi anak PERTAMA",
                    "  \"beforeend\"   jadi anak TERAKHIR    \"afterend\"   sesudah elemen",
                    "",
                    "data-* dipakai untuk menempelkan datamu sendiri ke sebuah elemen",
                    "(sintaksnya dibahas di materi HTML tentang atribut). Di JavaScript,",
                    "data itu dibaca lewat el.dataset:",
                    "  <li data-id=\"7\" data-harga-satuan=\"15000\">",
                    "      el.dataset.id            -> \"7\"",
                    "      el.dataset.hargaSatuan   -> \"15000\"",
                    "",
                    "Namanya berubah dari kebab-case (pakai tanda hubung) jadi camelCase,",
                    "dan nilainya selalu string. Ini cara baku menempelkan id ke sebuah",
                    "tombol atau baris daftar.",
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
                    "Sebuah klik nggak berhenti di elemen yang diklik. Sesudah listener di",
                    "situ selesai, event-nya naik ke induknya, lalu ke induk dari induknya,",
                    "sampai document. Kejadian ini namanya bubbling. Bug klasiknya: dropdown",
                    "atau modal yang menutup sendiri begitu isinya diklik. Penyebabnya, klik",
                    "di dalam ikut naik sampai ke listener \"klik di luar berarti tutup\" yang",
                    "dipasang di document.",
                    "",
                    "Di dalam handler ada dua nilai yang gampang ketuker, plus satu fungsi:",
                    "  e.target",
                    "      elemen yang BENAR-BENAR diklik (bisa <span> di dalam tombol)",
                    "  e.currentTarget",
                    "      elemen tempat listener ini dipasang",
                    "  e.stopPropagation()",
                    "      menghentikan perjalanan naik tadi",
                    "",
                    "Jangan jadikan stopPropagation kebiasaan. Fungsi itu juga mematikan",
                    "listener lain yang mungkin memang butuh event itu, dan bug-nya susah",
                    "dilacak karena kodenya ada di berkas lain. Seringnya yang kamu mau",
                    "cuma e.preventDefault(). Fungsi itu menahan perilaku bawaan browser,",
                    "dan perjalanan naiknya tetap jalan.",
                    "",
                    "Event delegation artinya memasang satu listener di wadahnya (container),",
                    "dan nggak memasang satu per baris.",
                    "  - Baris yang dibikin pakai createElement atau innerHTML sesudah",
                    "    listener terpasang tetap tertangani, karena yang mendengarkan adalah",
                    "    induknya yang sudah ada dari awal. Ini cara paling rapi menangani",
                    "    elemen yang dibuat dinamis.",
                    "  - 1000 baris cukup 1 listener, nggak perlu 1000.",
                    "",
                    "e.target.closest(\".hapus\") naik dari elemen yang diklik sampai ketemu",
                    "elemen yang cocok dengan selektornya, atau null kalau nggak ada. Itu",
                    "penyaringnya.",
                    "",
                    "removeEventListener butuh fungsi yang sama persis dengan yang",
                    "didaftarkan:",
                    "  el.addEventListener(\"click\", () => tutup());",
                    "  el.removeEventListener(\"click\", () => tutup());   // TIDAK melepas apa pun",
                    "",
                    "Dua arrow function itu dua objek berbeda, walaupun isinya sama. Simpan",
                    "fungsinya di variabel dulu, atau pakai opsi { once: true } kalau",
                    "listener-nya memang cuma perlu jalan sekali.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Form ada di hampir semua aplikasi bisnis: pendaftaran siswa baru,",
                    "pemesanan katering, laporan kerusakan fasilitas kantor. Lubang keamanan",
                    "yang gampang muncul di kode pemula adalah teks pengguna yang dimasukkan",
                    "ke halaman lewat innerHTML.",
                    "",
                    "Kasus kecil: halaman daftar belanja punya form dengan input bernama",
                    "barang dan sebuah <ul>. Barang baru muncul sebagai <li> dengan tombol",
                    "hapus. Seorang pengguna iseng mengetik <img src=x onerror=\"alert(1)\">",
                    "sebagai nama barang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan template milikmu dari teks milik pengguna. Teks pengguna",
                    "     nggak boleh lewat innerHTML apa adanya.",
                    "  2. Buat barisnya pakai createElement dan isi teksnya pakai",
                    "     textContent. Tombol hapusnya template milikmu sendiri, jadi boleh",
                    "     disisipkan sebagai HTML:",
                    "      const li = document.createElement(\"li\");",
                    "      li.dataset.id = Date.now();",
                    "      li.textContent = form.elements.barang.value.trim();",
                    "      li.insertAdjacentHTML(\"beforeend\", '<button class=\"hapus\">x</button>');",
                    "      daftar.appendChild(li);",
                    "     Nama barang iseng tadi tampil sebagai tulisan biasa dan nggak",
                    "     pernah dijalankan.",
                    "  3. Pasang satu listener di <ul> untuk semua tombol hapus.",
                    "     e.target.closest(\".hapus\") menyaring kliknya, lalu",
                    "     closest(\"li\").remove() menghapus barisnya. Baris yang ditambah",
                    "     belakangan ikut tertangani.",
                    "  4. Kasus pinggir: input kosong atau cuma berisi spasi. Cek",
                    "     value.trim() === \"\" sebelum membuat <li>, supaya daftarnya nggak",
                    "     berisi baris kosong.",
                ]
            },
        ],
    },
    {
        "title": "27. JSON & Fetch API",
        "sections": [
            {
                "body": [
                    "JSON (JavaScript Object Notation) adalah format data berbentuk teks.",
                    "Format ini yang paling umum dipakai untuk bertukar data di web,",
                    "misalnya di REST API. Bentuknya mirip sekali dengan object literal",
                    "JavaScript.",
                    "",
                    "  JSON.stringify(objek)   -> object JS jadi STRING JSON",
                    "  JSON.parse(teks)        -> string JSON jadi OBJECT JS",
                    "",
                    "Fetch API adalah cara bawaan (built-in) untuk melakukan network",
                    "request, yaitu mengambil data dari server atau API, di JavaScript",
                    "modern. Fetch menggantikan XMLHttpRequest yang lebih ribet.",
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
                "heading": "Catatan fetch soal text(), indentasi, dan CORS",
                "body": [
                    "Ada empat hal kecil di sekitar fetch yang bisa menghemat banyak waktu:",
                    "  - response.text() adalah pasangan response.json(), untuk balasan yang",
                    "    bukan JSON: HTML, CSV, atau teks biasa. Pakai ini juga waktu sebuah",
                    "    API gagal dan balasannya ternyata halaman error. response.json() pada",
                    "    halaman HTML melempar SyntaxError yang membingungkan.",
                    "  - JSON.stringify(obj, null, 2): argumen ketiga adalah jumlah spasi",
                    "    indentasi. Pakai ini waktu menulis berkas konfigurasi atau mencetak",
                    "    data untuk dibaca manusia. Argumen keduanya, null di sini, adalah",
                    "    penyaring key yang jarang dipakai.",
                    "  - Nggak semua isi object selamat lewat JSON.stringify. undefined dan",
                    "    function hilang, Date berubah jadi string. Daftar lengkapnya ada di",
                    "    materi 'Nilai vs Referensi & Menyalin Data'.",
                    "  - CORS. Kalau fetch ke domain lain gagal padahal alamatnya benar dan",
                    "    servernya hidup, tersangka pertamanya CORS. Browser menolak",
                    "    menyerahkan hasilnya ke JavaScript kalau server tujuan nggak",
                    "    mengirim header izin (Access-Control-Allow-Origin). Ini keputusan",
                    "    server, jadi bukan bug di kodemu, dan nggak bisa diperbaiki dari",
                    "    sisi browser. Node nggak punya aturan ini sama sekali, jadi fetch",
                    "    yang sama bisa berhasil dari terminal dan gagal dari halaman web.",
                ],
            },
            {
                "heading": "localStorage: hanya string, jadi lewat JSON",
                "body": [
                    "Masih di keluarga JSON: cara browser menyimpan data supaya nggak",
                    "hilang waktu halaman ditutup.",
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
                    "Jebakan: isi localStorage dan sessionStorage cuma bisa string. Kalau",
                    "kamu menyimpan object langsung, nggak ada error. JavaScript mengubahnya",
                    "jadi teks \"[object Object]\" tanpa bilang apa-apa, dan datanya hilang",
                    "untuk selamanya. Jadi object dan array wajib diubah pakai",
                    "JSON.stringify waktu disimpan, lalu JSON.parse waktu dibaca lagi.",
                    "",
                    "Pasangan ini yang kamu perlukan untuk project 'To-do list dengan",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi cuaca, kurs mata uang, dan cek ongkir mengambil datanya dari",
                    "API lewat fetch, dan datanya datang sebagai JSON. Aplikasi catatan",
                    "atau to-do sederhana menyimpan datanya di localStorage sebagai teks",
                    "JSON supaya nggak hilang waktu browser ditutup.",
                    "",
                    "Kasus kecil: halaman daftar produk mengambil data dari",
                    "https://api.contoh.com/produk. Kadang servernya sedang perbaikan dan",
                    "membalas halaman HTML dengan status 503. Daftar produk harus tetap",
                    "tampil dari salinan terakhir yang pernah berhasil dimuat.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar kemungkinannya: berhasil, server membalas status error,",
                    "     atau jaringan putus. Dua yang terakhir sama-sama berarti pakai",
                    "     salinan lama.",
                    "  2. Periksa response.ok sebelum memanggil json(), karena json() atas",
                    "     halaman HTML melempar SyntaxError. Di dalam fungsi async, dengan",
                    "     let produk di atasnya:",
                    "      try {",
                    "        const res = await fetch(\"https://api.contoh.com/produk\");",
                    "        if (!res.ok) throw new Error(\"status \" + res.status);",
                    "        produk = await res.json();",
                    "        localStorage.setItem(\"produk\", JSON.stringify(produk));",
                    "      } catch { produk = JSON.parse(localStorage.getItem(\"produk\")) ?? []; }",
                    "  3. Setiap kali berhasil, salinannya disimpan lewat JSON.stringify,",
                    "     karena localStorage cuma menerima string.",
                    "  4. Kasus pinggir: pengunjung yang baru pertama kali membuka halaman,",
                    "     tepat saat servernya gangguan. getItem memberi null,",
                    "     JSON.parse(null) juga null, dan ?? [] membuat daftarnya kosong",
                    "     dengan rapi, tanpa error.",
                ]
            },
        ],
    },
    {
        "title": "28. Module (import/export) & npm Dasar",
        "sections": [
            {
                "body": [
                    "Module artinya memecah kode jadi beberapa berkas, supaya lebih rapi dan",
                    "bisa dipakai ulang. Mirip module di Python atau package di Java.",
                    "",
                    "ES Module adalah standar modern, dan dipakai di browser maupun Node.js:",
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
                    "npm (Node Package Manager) adalah pengelola paket bawaan Node.js.",
                    "Gunanya untuk memasang dan mengelola library JavaScript buatan orang",
                    "lain.",
                    "",
                    "  npm init -y              -> membuat file package.json baru",
                    "  npm install nama_paket   -> install library (masuk ke node_modules/)",
                    "  npm install -D nama_paket -> install SEBAGAI dev dependency saja",
                    "  npm uninstall nama_paket  -> hapus library",
                    "  npm run nama_script       -> jalankan script custom di package.json",
                    "",
                    "Dev dependency adalah library yang cuma dibutuhkan waktu mengembangkan",
                    "program, misalnya alat tes, dan nggak ikut dipakai waktu program jalan.",
                    "",
                    "package.json adalah berkas konfigurasi project Node.js. Isinya",
                    "mencatat:",
                    "  - nama dan versi project",
                    "  - daftar dependency (\"dependencies\" dan \"devDependencies\")",
                    "  - script buatan sendiri (\"scripts\": { \"start\": \"node index.js\" })",
                    "",
                    "  npm start    -> menjalankan script 'start' di package.json",
                ]
            },
            {
                "body": [
                    "CommonJS adalah cara lama di Node.js, dan masih sering ditemui di kode",
                    "legacy (kode lama yang masih dipakai):",
                    "  // file matematika.js",
                    "  function tambah(a, b) { return a + b; }",
                    "  module.exports = { tambah };",
                    "",
                    "  // file main.js",
                    "  const { tambah } = require('./matematika.js');",
                    "",
                    "Bedanya dengan ES Module: CommonJS pakai require() untuk mengambil, dan",
                    "module.exports untuk membagikan. ES Module pakai import dan export.",
                    "Node.js modern mendukung keduanya, tergantung pengaturan \"type\" di",
                    "package.json.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek sungguhan jarang berupa satu berkas. Aplikasi kasir, misalnya,",
                    "memisahkan hitungan harga, format rupiah, dan tampilan ke berkas yang",
                    "berbeda, lalu menyambungkannya dengan import. Library buatan orang",
                    "lain, seperti alat format tanggal atau alat tes, dipasang lewat npm",
                    "dan tercatat di package.json, jadi teman satu tim cukup menjalankan",
                    "npm install untuk mendapatkan semuanya.",
                    "",
                    "Kasus kecil: berkas kasir.js sudah ratusan baris dan berisi fungsi",
                    "formatRupiah yang ternyata dibutuhkan juga oleh laporan.js. Kalau",
                    "fungsinya disalin ke dua tempat, setiap bug harus dibetulkan dua kali.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan fungsi yang dipakai bersama ke berkas sendiri, misalnya",
                    "     uang.js, dan export dari sana.",
                    "  2. Import di setiap berkas yang membutuhkannya:",
                    "      // uang.js",
                    "      export function formatRupiah(n) { return \"Rp\" + n; }",
                    "      // kasir.js (laporan.js menulis baris import yang sama)",
                    "      import { formatRupiah } from \"./uang.js\";",
                    "      console.log(formatRupiah(15000));   // Rp15000",
                    "  3. Supaya Node mau membaca import, package.json butuh baris",
                    "     \"type\": \"module\". Buat package.json pakai npm init -y, lalu",
                    "     tambahkan baris itu.",
                    "  4. Kasus pinggir: nama yang di-import harus sama persis dengan yang",
                    "     di-export, termasuk huruf besarnya. import { formatrupiah } nggak",
                    "     akan menemukan formatRupiah, dan Node langsung menolak menjalankan",
                    "     programnya.",
                ]
            },
        ],
    },
    {
        "title": "29. Module Lanjutan: Semua Bentuk Import & Export",
        "sections": [
            {
                "body": [
                    "Materi 'Module (import/export) & npm Dasar' mengajarkan dua bentuk:",
                    "named export dan default export. Itu cukup untuk menulis modul sendiri,",
                    "tapi belum cukup untuk membaca kode orang lain. Begitu kamu membuka",
                    "repo sungguhan, baris-baris paling atas tiap berkas sering berisi",
                    "bentuk yang belum pernah kamu lihat. Padahal baris-baris itu nggak",
                    "bisa dilewati. Kalau kamu nggak tahu sebuah nama datang dari mana,",
                    "sisa berkasnya jadi teka-teki.",
                    "",
                    "Ini semua bentuk import yang bakal kamu temui:",
                    "",
                    "  import { a } from \"./m.js\"",
                    "      ambil export bernama a; namanya HARUS persis",
                    "  import { a as b } from \"./m.js\"",
                    "      ambil a, tapi di berkas ini panggil dia b",
                    "  import bawaan from \"./m.js\"",
                    "      ambil export default; namanya BEBAS kamu pilih",
                    "  import bawaan, { a } from \"./m.js\"",
                    "      default dan named sekaligus, satu baris",
                    "  import * as m from \"./m.js\"",
                    "      semua named export jadi satu object: m.a, m.b",
                    "  import \"./m.js\"",
                    "      jalankan berkasnya, jangan ambil apa pun",
                    "  const m = await import(\"./m.js\")",
                    "      muat SAAT ITU JUGA, bukan di awal program",
                    "",
                    "Dan ini semua bentuk export-nya:",
                    "",
                    "  export function f() {}",
                    "      menempel langsung di deklarasinya",
                    "  export { f, g }",
                    "      satu daftar di KAKI berkas",
                    "  export { f as hitung }",
                    "      keluar memakai nama yang berbeda",
                    "  export default f",
                    "      hanya boleh SATU per berkas",
                    "  export * from \"./x.js\"",
                    "      teruskan semua named export berkas lain",
                    "  export { default as F } from \"./F.js\"",
                    "      default milik orang lain -> named di sini",
                    "",
                    "Dua bentuk yang paling sering bikin bingung waktu pertama kali dilihat:",
                    "  - import * as React from \"react\" nggak mengambil satu nama. Dia",
                    "    mengambil seluruh isi modul jadi satu object. Sesudah itu semuanya",
                    "    dipanggil lewat titik: React.useState(), React.Fragment. Object itu",
                    "    cuma bisa dibaca.",
                    "  - import \"./gaya.css\" nggak memasukkan apa pun ke variabel, jadi",
                    "    kelihatannya seperti salah ketik. Padahal disengaja. Yang dibutuhkan",
                    "    adalah efek dari dimuatnya berkas itu, dan nilainya nggak dipakai.",
                    "    Di proyek yang pakai bundler (alat yang menggabungkan banyak berkas",
                    "    jadi satu), memuat CSS berarti gayanya ikut dipasang ke halaman.",
                    "    Bentuk yang sama dipakai untuk polyfill dan berkas setup.",
                    "",
                    "Alias, yaitu kata as, juga ada gunanya. Alias dipakai kalau dua modul",
                    "mengekspor nama yang sama persis, atau kalau nama aslinya terlalu umum",
                    "untuk dipakai begitu aja:",
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
                "heading": "Enam penyebab import gagal",
                "body": [
                    "Ada enam hal yang bikin import gagal padahal kelihatannya sudah benar.",
                    "Semuanya bakal kamu temui, jadi kenali pesannya dari sekarang supaya",
                    "nggak buang waktu nanti.",
                    "  1. Di Node, ekstensi .js wajib ditulis. from \"./alat/matematika\"",
                    "     langsung berhenti:",
                    "       Error [ERR_MODULE_NOT_FOUND]: Cannot find module .../alat/matematika",
                    "       Did you mean to import \"./alat/matematika.js\"?",
                    "     Bundler (Vite, webpack, Next.js) menebaknya untukmu. Makanya kode",
                    "     React di internet menulis from \"./Tombol\" tanpa ekstensi. Node",
                    "     polos nggak menebak.",
                    "  2. Meng-import sebuah folder berarti meng-import index.js di dalamnya.",
                    "     Ini cuma kebiasaan, jadi mustahil ditebak sendiri, dan nggak ada",
                    "     tanda apa pun di kodenya: from \"./alat\" berarti",
                    "     from \"./alat/index.js\". Itu alasan berkas bernama index.js ada di",
                    "     mana-mana. Yang menebak lagi-lagi bundler dan require() CommonJS.",
                    "     Node dengan ES Module murni menolak dan menyebut alasannya:",
                    "       Error [ERR_UNSUPPORTED_DIR_IMPORT]: Directory import .../alat",
                    "       is not supported",
                    "  3. export * nggak ikut membawa default. Barrel, yaitu berkas",
                    "     index.js yang meneruskan export dari berkas-berkas lain, harus",
                    "     menulis sendiri kalau mau meneruskan default:",
                    "     export { default as rupiah } from \"./uang.js\".",
                    "  4. Salah ketik nama import nggak menghasilkan undefined. Programnya",
                    "     langsung mati sebelum satu baris pun sempat jalan:",
                    "       SyntaxError: The requested module './alat/index.js' does not",
                    "       provide an export named 'pajakk'",
                    "     Ini justru kabar baik. Import statis diperiksa waktu modul",
                    "     dirangkai, sebelum dipakai. Beda dengan object biasa, yang salah",
                    "     ketiknya jadi undefined tanpa ketahuan.",
                    "  5. Object hasil import * as m cuma bisa dibaca. m.PPN = 0.2 melempar",
                    "     TypeError: Cannot assign to read only property 'PPN' of object",
                    "     '[object Module]'.",
                    "  6. Satu berkas dimuat sekali aja seumur hidup program. Walau diimpor",
                    "     sepuluh berkas berbeda, badan modulnya tetap dijalankan satu kali,",
                    "     dan hasilnya dipakai bersama. Jadi kalau kamu menaruh state",
                    "     (misalnya sebuah array) di level module, state itu dipakai",
                    "     ramai-ramai. Dia global, walau nggak kelihatan global.",
                ],
            },
            {
                "heading": "Import efek samping, hoisting, dan import() dinamis",
                "body": [
                    "Contoh ini menunjukkan tiga hal sekaligus, dan semuanya sering ada di",
                    "kode nyata:",
                    "  - import \"./pengaturan.mjs\" tanpa { } dan tanpa nama. Yang dicari",
                    "    efeknya, bukan nilainya. Bentuknya sama dengan import \"./gaya.css\"",
                    "    di proyek React.",
                    "  - Baris import itu sengaja ditaruh paling bawah, untuk membuktikan",
                    "    bahwa import di-hoist. Dia tetap dijalankan lebih dulu daripada",
                    "    baris pertama berkasnya.",
                    "  - await import(\"./berat.mjs\") memuat modul cuma waktu dibutuhkan. Ini",
                    "    dasar code-splitting dan lazy loading: halaman nggak perlu",
                    "    mengunduh kode fitur yang belum tentu dibuka. Ekstensi .mjs dipakai",
                    "    supaya berkas ini jadi module tanpa perlu package.json sama sekali.",
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
                "heading": "Menentukan ES Module atau CommonJS",
                "body": [
                    "Pertanyaan yang menentukan semuanya: sebuah berkas .js itu ES Module",
                    "atau CommonJS? Ada tiga aturan, dibaca berurutan:",
                    "",
                    "  berkas.mjs   SELALU ES Module, apa pun isi package.json",
                    "  berkas.cjs   SELALU CommonJS, apa pun isi package.json",
                    "  berkas.js    ikut \"type\" di package.json TERDEKAT ke atas:",
                    "                 \"type\": \"module\"     -> ES Module (import/export)",
                    "                 \"type\": \"commonjs\"   -> CommonJS (require/module.exports)",
                    "                 tidak ditulis         -> Node 22+ menebak dari isinya;",
                    "                                          ada import di dalamnya berarti",
                    "                                          ES Module",
                    "",
                    "Dua ekstensi aneh itu ada karena aturan ketiga terlalu bergantung pada",
                    "berkas lain. .mjs dan .cjs memutuskan jenis satu berkas tanpa peduli",
                    "sekitarnya. Biasanya dipakai waktu sebuah library harus menyediakan dua",
                    "versi sekaligus.",
                    "",
                    "Dua pesan error yang paling sering muncul, dan artinya:",
                    "",
                    "  SyntaxError: Cannot use import statement outside a module",
                    "    -> berkasnya berisi import, tapi dibaca sebagai CommonJS. Penyebab",
                    "       lazimnya: ekstensi .cjs, atau package.json menulis",
                    "       \"type\": \"commonjs\" secara eksplisit.",
                    "  ReferenceError: require is not defined in ES module scope",
                    "    -> kebalikannya: menulis require() di berkas yang statusnya sudah",
                    "       ES Module.",
                    "",
                    "Ada tiga beda lain dari require() yang jarang disebut, tapi kerasa",
                    "tiap hari:",
                    "  - Module selalu dalam strict mode, tanpa perlu menulis \"use strict\".",
                    "    Salah ketik nama variabel jadi error, dan nggak bikin variabel",
                    "    global baru tanpa ketahuan.",
                    "  - Tiap module punya scope sendiri. const di sebuah module bukan",
                    "    variabel global, jadi dua berkas boleh pakai nama yang sama tanpa",
                    "    bentrok.",
                    "  - import di-hoist dan wajib ada di level paling atas berkas. Dia",
                    "    nggak boleh ditaruh di dalam if. require() kebalikannya: dia baris",
                    "    biasa yang jalan waktu gilirannya tiba. Kalau kamu butuh memuat",
                    "    modul secara bersyarat di ES Module, pakai import() dinamis tadi.",
                    "",
                    "Di browser, import cuma jalan lewat atribut type=\"module\":",
                    "",
                    "  <script type=\"module\" src=\"utama.js\"></script>",
                    "",
                    "Tanpa type=\"module\", browser membaca berkasnya sebagai script biasa,",
                    "lalu berhenti di baris pertama dengan pesan yang sama persis: Cannot",
                    "use import statement outside a module. Bonusnya, script bertipe module",
                    "otomatis defer, yaitu dijalankan sesudah seluruh HTML selesai dibaca.",
                    "Jadi document.querySelector di materi DOM langsung menemukan",
                    "elemennya, tanpa perlu dibungkus DOMContentLoaded.",
                    "",
                    "Jebakan terakhir yang sering bikin orang buang waktu: berkas",
                    "ber-type=\"module\" nggak bisa dicoba dengan klik dua kali di file",
                    "manager (alamat file:///...). Browser memblokirnya dengan galat CORS,",
                    "dan halamannya diam aja seolah kodenya nggak ada. Modul butuh alamat",
                    "http. Nyalakan server lokal dari folder yang sama, lalu buka",
                    "http://localhost:8000 di browser:",
                    "",
                    "  python3 -m http.server 8000",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Begitu kamu membuka proyek React atau Node di tempat PKL atau kerja,",
                    "baris paling atas tiap berkas berisi import dengan bentuk yang",
                    "macam-macam. Tim biasanya mengumpulkan helper dalam satu folder dengan",
                    "index.js sebagai pintu masuknya, dan memuat fitur berat seperti ekspor",
                    "PDF hanya saat tombolnya diklik, pakai import() dinamis.",
                    "",
                    "Kasus kecil: folder utils/ berisi tanggal.js, uang.js, dan teks.js.",
                    "Tiap berkas halaman menulis tiga baris import ke tiga berkas itu.",
                    "Lebih repot lagi, uang.js dan teks.js sama-sama mengekspor fungsi",
                    "bernama format.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali dua masalahnya: alamat import yang diulang di banyak",
                    "     berkas, dan dua export yang namanya bentrok.",
                    "  2. Buat barrel utils/index.js yang meneruskan isi ketiganya, sambil",
                    "     memberi nama berbeda untuk dua format tadi:",
                    "      // utils/index.js",
                    "      export * from \"./tanggal.js\";",
                    "      export { format as formatUang } from \"./uang.js\";",
                    "      export { format as formatTeks } from \"./teks.js\";",
                    "      // halaman.js",
                    "      import { formatUang, formatTeks } from \"./utils/index.js\";",
                    "  3. Di Node polos, tulis jalurnya lengkap sampai index.js. Bentuk",
                    "     from \"./utils\" cuma ditebak bundler, sedangkan Node dengan ES",
                    "     Module menolaknya dengan ERR_UNSUPPORTED_DIR_IMPORT.",
                    "  4. Kasus pinggir: kalau tanggal.js punya export default, export *",
                    "     nggak ikut meneruskannya. Tulis sendiri:",
                    "     export { default as tanggal } from \"./tanggal.js\".",
                ]
            },
        ],
    },
    {
        "title": "30. Node.js: Process, Berkas, dan Path",
        "sections": [
            {
                "body": [
                    "Node.js itu JavaScript yang sama persis dengan yang di browser.",
                    "Bahasanya nggak beda. Yang beda adalah lingkungannya, yaitu objek",
                    "bawaan apa aja yang tersedia di sekitarmu.",
                    "",
                    "  Hanya ada di browser : document, window, alert, localStorage",
                    "  Hanya ada di Node    : process, require, __dirname, modul fs / path / http",
                    "",
                    "Nggak ada lingkungan yang punya keduanya, dan dari situ muncul satu",
                    "error yang pasti bakal kamu temui. Contoh loop di materi 'Perulangan'",
                    "pakai process.stdout.write. Kalau contoh itu ditempel ke Console",
                    "browser (F12), hasilnya 'ReferenceError: process is not defined'.",
                    "Kodenya nggak salah. Contoh itu memang ditulis untuk dijalankan pakai",
                    "'node file.js'.",
                    "",
                    "process adalah objek global di Node yang mewakili proses, yaitu",
                    "program yang sedang jalan:",
                    "",
                    "  process.argv                -> array argumen yang diketik di terminal",
                    "  process.env                 -> variabel lingkungan (konfigurasi dari",
                    "                                 luar kode)",
                    "  process.exit(kode)          -> hentikan program SEKARANG JUGA dengan",
                    "                                 kode keluar",
                    "  process.stdout.write(teks)  -> cetak TANPA menambah baris baru",
                    "",
                    "process.stdout.write dan console.log bedanya ada dua:",
                    "  1. console.log selalu menambah baris baru. stdout.write nggak",
                    "     menambah apa pun.",
                    "  2. console.log menerima banyak argumen dengan tipe apa aja.",
                    "     stdout.write cuma menerima string, jadi process.stdout.write(5)",
                    "     langsung melempar TypeError.",
                    "",
                    "Makanya materi 'Perulangan' menulis process.stdout.write(i + \" \"). Di",
                    "situ + \" \" punya dua tugas: jadi pemisah, sekaligus mengubah angka i",
                    "jadi string.",
                    "",
                    "process.argv selalu diawali dua hal yang bukan argumenmu:",
                    "  argv[0] = path program node",
                    "  argv[1] = path berkas .js yang dijalankan",
                    "  argv[2] dan seterusnya = argumen sungguhan yang kamu ketik",
                    "",
                    "Karena itu kamu bakal sering lihat process.argv.slice(2).",
                    "",
                    "process.env dipakai untuk hal yang beda di tiap komputer: nomor port,",
                    "alamat database, kunci API. Isinya selalu string atau undefined,",
                    "nggak pernah angka atau boolean. Jadi process.env.PORT + 1 menghasilkan",
                    "\"30001\", bukan 3001.",
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
                "heading": "Modul bawaan Node, jalur relatif, dan path.join",
                "body": [
                    "Modul bawaan vs paket npm",
                    "",
                    "Sebagian modul sudah ikut terpasang bersama Node. Kamu nggak perlu npm",
                    "install, modul itu nggak masuk node_modules, dan nggak pernah muncul di",
                    "package.json. Modul-modul ini yang paling sering kelihatan di",
                    "baris-baris pertama sebuah berkas Node:",
                    "",
                    "  fs        membaca & menulis berkas dan folder",
                    "  path      merangkai dan membedah jalur berkas",
                    "  readline  membaca ketikan baris per baris dari terminal",
                    "  os        info sistem: os.platform(), os.homedir(), os.cpus()",
                    "  url       membedah alamat: new URL(...), .searchParams",
                    "  crypto    hash & nilai acak aman: crypto.randomUUID()",
                    "  http      membuat server web tanpa library apa pun",
                    "            (Express dibangun di atas ini)",
                    "",
                    "Ada dua cara memanggilnya. Soal CommonJS dan ES Module, lihat materi",
                    "'Module (import/export) & npm Dasar':",
                    "  const fs = require(\"node:fs\");     // CommonJS",
                    "  import fs from \"node:fs\";          // ES Module",
                    "",
                    "Awalan node: menegaskan bahwa ini modul bawaan Node, dan bukan paket",
                    "dari npm. Untungnya dua. Pembaca kodemu langsung tahu tanpa ngecek",
                    "package.json, dan beberapa modul baru (misalnya node:test) memang cuma",
                    "bisa dipanggil dengan awalan itu. Kode lama menulis require(\"fs\") tanpa",
                    "awalan dan tetap jalan, karena keduanya modul yang sama persis.",
                    "",
                    "Jebakan path yang paling sering bikin orang jatuh: \"di sini\" itu di",
                    "mana?",
                    "",
                    "Jalur relatif seperti \"data/catatan.txt\" dihitung dari folder tempat",
                    "kamu mengetik perintah node, dan nggak dihitung dari folder berkas",
                    ".js-nya. Program yang sama, kalau dijalankan dari folder lain, tiba-tiba",
                    "bilang berkasnya nggak ketemu.",
                    "",
                    "  __dirname      -> folder tempat berkas INI berada (CommonJS)",
                    "  __filename     -> jalur lengkap berkas ini berikut namanya (CommonJS)",
                    "  process.cwd()  -> folder tempat perintah node diketik",
                    "",
                    "Di ES Module (\"type\": \"module\" di package.json, atau berkas .mjs),",
                    "__dirname nggak ada sama sekali. Penggantinya empat baris ini, dan kamu",
                    "bakal sering lihat:",
                    "",
                    "  import path from \"node:path\";",
                    "  import { fileURLToPath } from \"node:url\";",
                    "  // import.meta.url berupa URL file:///..., diubah jadi jalur biasa",
                    "  const __filename = fileURLToPath(import.meta.url);",
                    "  const __dirname = path.dirname(__filename);",
                    "",
                    "Untuk merangkai jalur, pakai path.join. Jangan menyambung sendiri pakai",
                    "+ \"/\":",
                    "  path.join(\"data\", \"arsip\", \"c.txt\")  -> \"data/arsip/c.txt\"",
                    "  \"data/\" + \"/arsip\" + \"/c.txt\"         -> \"data//arsip/c.txt\"  <- slash ganda",
                    "",
                    "Di Windows, path.join menghasilkan \"data\\arsip\\c.txt\", karena",
                    "pemisahnya backslash. path.join otomatis pakai pemisah yang benar sesuai",
                    "sistemnya. Kalau menyambung sendiri, nggak. path.join juga merapikan",
                    "\"..\" dan \"./\" yang ada di tengah jalur.",
                    "",
                    "Fungsi path lain yang sering dipakai:",
                    "  path.resolve(...)   mirip, tapi hasilnya SELALU jalur absolut dari root",
                    "  path.basename(\"/a/b/c.txt\") -> \"c.txt\"",
                    "  path.extname(\"/a/b/c.txt\")  -> \".txt\"",
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
                    "Sebelum ada Promise, seluruh API async di Node pakai satu bentuk yang",
                    "sama. Argumen terakhir sebuah fungsi adalah callback, dan parameter",
                    "pertama callback itu selalu error: null kalau sukses, objek Error kalau",
                    "gagal. Hasilnya baru ada di parameter kedua.",
                    "",
                    "  fs.readFile(jalur, \"utf8\", (err, data) => { ... });",
                    "                              ^^^ error dulu, BARU hasilnya",
                    "",
                    "Lupa ngecek if (err) adalah bug klasik. data bernilai undefined tanpa",
                    "ketahuan, dan error-nya baru muncul beberapa baris kemudian, di tempat",
                    "yang nggak ada hubungannya. Kode Node lama penuh dengan bentuk ini,",
                    "jadi kamu harus bisa membacanya. Tapi untuk kode baru, pakai",
                    "fs/promises + await, dengan try-catch seperti di materi async/await.",
                    "",
                    "Fungsi fs yang sama punya tiga bentuk, dan ketiganya beredar di kode",
                    "nyata:",
                    "  fs.readFileSync(...)          -> memblokir; program berhenti sampai selesai",
                    "  fs.readFile(..., callback)    -> error-first callback, gaya lama",
                    "  fsp.readFile(...) + await     -> dari \"node:fs/promises\", gaya sekarang",
                    "",
                    "Versi Sync boleh dipakai untuk skrip kecil dan waktu program baru",
                    "menyala. Jangan dipakai di dalam server, karena dia membekukan seluruh",
                    "proses untuk semua pengguna.",
                    "",
                    "Membaca ketikan pemakai: di Node nggak ada prompt() seperti di browser.",
                    "Penggantinya modul readline, dan cara kerjanya berbasis event. Dia",
                    "nggak \"berhenti lalu mengembalikan nilai\". readline memancarkan event",
                    "\"line\" setiap satu baris masuk, dan \"close\" waktu masukannya habis",
                    "(Ctrl+D di terminal, atau berkas yang di-pipe sudah selesai). Untuk",
                    "satu pertanyaan aja, ada bentuk singkat",
                    "rl.question(\"Nama? \", (jawab) => { ... }), yang juga pakai callback.",
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
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Node sering dipakai untuk skrip kecil yang menghemat kerja manual:",
                    "mengganti nama ratusan foto produk, menggabungkan rekap absensi, atau",
                    "membuat laporan harian dari berkas log. Skrip seperti itu dijalankan",
                    "dari terminal dengan nama berkas sebagai argumen.",
                    "",
                    "Kasus kecil: berkas absensi.csv berisi baris nama,status, misalnya",
                    "Andi,hadir lalu Budi,izin lalu Citra,hadir. Guru piket mau menjalankan",
                    "node rekap.js absensi.csv dan melihat jumlah tiap status.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya jalur berkas di process.argv[2], karena dua isi pertama",
                    "     argv milik Node. Keluarannya object berisi jumlah per status.",
                    "  2. Baca berkasnya sebagai teks, pecah per baris, ambil kolom kedua,",
                    "     lalu hitung:",
                    "      const fs = require(\"node:fs\");",
                    "      const isi = fs.readFileSync(process.argv[2], \"utf8\").trim().split(\"\\n\");",
                    "      const rekap = {};",
                    "      for (const [, status] of isi.map((b) => b.split(\",\")))",
                    "        rekap[status] = (rekap[status] ?? 0) + 1;",
                    "      console.log(rekap);   // { hadir: 2, izin: 1 }",
                    "  3. trim() sebelum split membuang baris kosong di akhir berkas. Tanpa",
                    "     itu, baris kosong terakhir ikut terhitung sebagai status undefined.",
                    "  4. Kasus pinggir: nama berkasnya salah ketik. readFileSync melempar",
                    "     error ENOENT. Bungkus dengan try-catch, cetak pesan yang jelas,",
                    "     lalu process.exit(1) supaya terminal tahu programnya gagal.",
                    "",
                    "Jebakan: berkas CSV yang disimpan di Windows sering memakai akhir",
                    "baris \\r\\n. Statusnya jadi \"hadir\\r\" dan dihitung terpisah dari",
                    "\"hadir\". Pecah pakai split(/\\r?\\n/) supaya dua jenis akhir baris",
                    "sama-sama tertangani.",
                ]
            },
        ],
    },
    {
        "title": "31. Web API: Observer dan Animasi di Browser",
        "sections": [
            {
                "body": [
                    "Empat API di materi ini cuma ada di browser. Kalau kamu menjalankannya",
                    "lewat 'node namaberkas.js', nggak ada document, nggak ada window, dan",
                    "nggak ada elemen untuk diamati. Kodenya benar dan bisa kamu coba",
                    "sungguhan, tapi caranya beda. Tempel di Console browser (F12 -> tab",
                    "Console) sambil membuka halaman apa pun. Atau taruh di dalam tag",
                    "<script> pada berkas .html, lalu buka lewat server lokal (lihat materi",
                    "HTML 'Menjalankan Halaman Sendiri').",
                    "",
                    "Jangan berharap melihat baris 'akan mencetak ...' seperti di materi",
                    "lain. Di sini, kapan callback-nya jalan ditentukan oleh kejadian di",
                    "halaman: elemen masuk layar, ukurannya berubah, atau DOM-nya diubah.",
                    "Urutan baris kode dari atas ke bawah nggak menentukan.",
                    "",
                    "Keempatnya punya kesamaan. Sebelum API ini ada, satu-satunya cara",
                    "tahu \"sesuatu berubah\" adalah polling, yaitu ngecek berulang-ulang",
                    "pakai setInterval atau pakai event yang menyala puluhan kali per detik",
                    "(scroll, resize). Observer membalik arahnya. Kamu daftar sekali, lalu",
                    "browser yang ngasih tahu kamu tepat waktu perubahannya terjadi, nggak",
                    "lebih sering. CPU jadi lebih hemat, dan kodenya lebih pendek karena",
                    "nggak perlu lagi menghitung \"apakah ini sudah berubah dari terakhir",
                    "kali aku cek\".",
                ],
            },
            {
                "heading": "IntersectionObserver: tahu kapan elemen masuk layar",
                "body": [
                    "Masalah lamanya begini. Kamu mau tahu kapan sebuah <img> masuk area",
                    "yang kelihatan, supaya gambarnya baru dimuat saat itu (lazy load).",
                    "Atau kapan tombol 'muat lagi' di ujung daftar kelihatan (infinite",
                    "scroll). Cara lama:",
                    "",
                    "  window.addEventListener('scroll', () => {",
                    "      const rect = elemen.getBoundingClientRect();",
                    "      const terlihat = rect.top < window.innerHeight && rect.bottom > 0;",
                    "      // ...lalu apa yang dilakukan kalau terlihat",
                    "  });",
                    "",
                    "getBoundingClientRect() memaksa browser menghitung ulang tata letak",
                    "(layout) saat itu juga. Kalau dipanggil berkali-kali berturut-turut,",
                    "ini disebut layout thrashing. Ditambah lagi, event scroll bisa menyala",
                    "puluhan kali per detik selama jari masih menggeser. Untuk satu elemen",
                    "mungkin belum kerasa. Untuk lima puluh kartu yang masing-masing dicek",
                    "sendiri, halamannya jadi patah-patah.",
                    "",
                    "IntersectionObserver membalik arahnya. Kamu daftarkan elemen yang mau",
                    "diawasi sekali aja. Browser ngasih tahu lewat callback cuma waktu",
                    "status \"kelihatan atau nggak\"-nya berubah. Browser menghitungnya",
                    "sendiri di waktu yang pas, tanpa memaksa layout dihitung ulang, jadi",
                    "nggak ada yang tertahan.",
                ],
                "code": """// threshold: 0.5 -> callback jalan saat 50% tinggi elemen sudah terlihat
const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
        // entry.isIntersecting: true selama syarat threshold terpenuhi
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;      // baru sekarang gambar sungguhan dimuat
            observer.unobserve(img);        // sudah dimuat, tidak perlu diawasi lagi
        }
    }
}, {
    threshold: 0.5,     // 0 = sedikit saja masuk sudah dianggap terlihat, 1 = harus penuh
    rootMargin: "100px" // "perluas" area amatan 100px, supaya mulai dimuat SEBELUM
                         // benar-benar terlihat - pengguna tidak sempat lihat kotak kosong
});

// Daftarkan semua gambar yang src aslinya sengaja ditaruh di data-src dulu:
// <img data-src="foto-besar.jpg" src="placeholder-buram.jpg">
document.querySelectorAll("img[data-src]").forEach((img) => observer.observe(img));

// Pola yang sama, dipakai untuk infinite scroll: amati elemen "sentinel"
// (biasanya <div> kosong) di ujung paling bawah daftar.
const sentinel = document.querySelector("#sentinel-akhir-daftar");
const pemuatObserver = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
        muatHalamanBerikutnya();   // fungsi milikmu sendiri, memanggil API/menambah elemen
    }
});
pemuatObserver.observe(sentinel);""",
            },
            {
                "heading": "MutationObserver: tahu kapan DOM diubah",
                "body": [
                    "Kasusnya beda. Kamu nggak peduli posisi elemen di layar, tapi peduli",
                    "isi atau struktur DOM yang berubah. Misalnya elemen baru ditambahkan",
                    "library pihak ketiga, atribut class berubah karena skrip lain, atau",
                    "anak sebuah wadah dihapus. Nggak ada event bawaan untuk itu.",
                    "Jawabannya MutationObserver.",
                ],
                "code": """const wadah = document.querySelector("#daftar-notifikasi");

const mo = new MutationObserver((mutations) => {
    for (const m of mutations) {
        if (m.type === "childList" && m.addedNodes.length > 0) {
            console.log(`${m.addedNodes.length} elemen baru ditambahkan`);
        }
        if (m.type === "attributes") {
            console.log(`atribut '${m.attributeName}' berubah pada`, m.target);
        }
    }
});

mo.observe(wadah, {
    childList: true,   // amati elemen anak yang ditambah/dihapus
    attributes: true,  // amati perubahan atribut (class, style, data-*, dst)
    subtree: true,     // ikut amati anak dari anak, bukan cuma anak langsung
});

// Berhenti mengamati kalau sudah tidak perlu - MutationObserver TIDAK
// otomatis berhenti sendiri walau elemennya dihapus dari halaman.
// mo.disconnect();""",
            },
            {
                "heading": "ResizeObserver: tahu kapan ukuran elemen berubah",
                "body": [
                    "window.addEventListener('resize', ...) cuma menyala waktu jendela",
                    "browser berubah ukuran. Padahal sebuah elemen bisa berubah ukuran",
                    "tanpa jendelanya bergerak sama sekali. Misalnya isinya bertambah",
                    "panjang, font-nya baru selesai dimuat, atau elemen tetangganya diubah",
                    "ukurannya lewat CSS 'resize: both'. Untuk kasus begitu, resize di",
                    "window nggak pernah menyala. ResizeObserver mengamati elemen tertentu,",
                    "apa pun penyebab perubahannya.",
                ],
                "code": """const kotak = document.querySelector("#kotak-elastis");

const ro = new ResizeObserver((entries) => {
    for (const entry of entries) {
        // contentBoxSize lebih akurat dari entry.target.offsetWidth di sini,
        // karena sudah dihitung ULANG persis saat observer ini menembak.
        const { inlineSize, blockSize } = entry.contentBoxSize[0];
        console.log(`Ukuran baru: ${inlineSize}px x ${blockSize}px`);

        // Contoh pemakaian: sembunyikan teks kalau kotaknya jadi terlalu sempit
        entry.target.classList.toggle("terlalu-sempit", inlineSize < 200);
    }
});

ro.observe(kotak);
// ro.disconnect(); saat elemen tidak lagi butuh diawasi""",
            },
            {
                "heading": "requestAnimationFrame: dibuat khusus untuk animasi",
                "body": [
                    "setInterval(fungsi, 16) kelihatannya masuk akal untuk animasi 60fps",
                    "(1000ms / 60 ~ 16.7ms). Tapi ada tiga masalah nyata:",
                    "  - Interval tetap jalan walau tab-nya sedang nggak aktif. Baterai",
                    "    laptop terkuras untuk animasi yang nggak dilihat siapa pun.",
                    "  - Jadwalnya nggak disamakan dengan refresh rate layarnya. Di layar",
                    "    120Hz, animasi 60fps buatan setInterval",
                    "    kelihatan patah-patah.",
                    "  - setInterval nggak ngasih tahu waktu yang tepat kapan sebuah frame",
                    "    digambar.",
                    "",
                    "requestAnimationFrame (disingkat rAF) memperbaiki ketiganya. Browser",
                    "sendiri yang memanggil callback-nya, tepat sebelum frame berikutnya",
                    "digambar. rAF otomatis berhenti atau melambat waktu tab tersembunyi.",
                    "Callback-nya juga menerima satu argumen, yaitu timestamp presisi",
                    "tinggi dalam milidetik (bisa berkoma) sejak halaman dimuat.",
                ],
                "code": """let posisi = 0;
let waktuMulai = null;
let idFrame;

function animasikan(timestamp) {
    if (waktuMulai === null) waktuMulai = timestamp;
    const berlalu = timestamp - waktuMulai;   // milidetik sejak animasi dimulai

    // Gerak 100px per detik, dihitung dari WAKTU, bukan dari jumlah frame -
    // supaya kecepatannya tetap sama di layar 60Hz maupun 144Hz.
    posisi = (berlalu / 1000) * 100;
    kotak.style.transform = `translateX(${posisi}px)`;

    if (posisi < 300) {
        // Pola yang selalu dipakai: rAF memanggil DIRINYA SENDIRI tiap frame.
        // Tanpa baris ini, animasinya cuma jalan satu frame lalu berhenti.
        idFrame = requestAnimationFrame(animasikan);
    }
}

const kotak = document.querySelector("#kotak-animasi");
idFrame = requestAnimationFrame(animasikan);

// Batalkan kapan pun sebelum selesai, mis. saat pengguna pindah halaman:
// cancelAnimationFrame(idFrame);""",
            },
            {
                "heading": "Kapan pakai yang mana",
                "body": [
                    "Keempatnya sering ketuker karena sama-sama \"menunggu sesuatu terjadi\",",
                    "padahal yang ditunggu beda total:",
                    "",
                    "  IntersectionObserver  elemen masuk/keluar AREA TERLIHAT",
                    "                        (lazy load, infinite scroll, animasi",
                    "                        muncul saat di-scroll ke)",
                    "  MutationObserver      DOM berubah - elemen/atribut ditambah,",
                    "                        dihapus, atau diubah",
                    "  ResizeObserver        UKURAN sebuah elemen berubah, apa pun",
                    "                        sebabnya (bukan cuma jendela browser)",
                    "  requestAnimationFrame BUKAN observer - dipakai saat KAMU sendiri",
                    "                        yang mengubah sesuatu berulang-ulang demi",
                    "                        efek gerak (animasi, game, drag-and-drop)",
                    "",
                    "Jebakan yang sering kejadian:",
                    "  - Pakai MutationObserver untuk mendeteksi elemen yang masuk layar.",
                    "    Bisa, tapi jauh lebih mahal dan ribet. Itu tugasnya",
                    "    IntersectionObserver.",
                    "  - Pakai setInterval untuk animasi visual yang halus. Selalu pakai",
                    "    requestAnimationFrame.",
                    "  - Lupa melepas. Ketiga observer perlu disconnect() atau unobserve()",
                    "    waktu elemennya sudah nggak ada di halaman, dan rAF yang berulang",
                    "    dihentikan pakai cancelAnimationFrame(). Observer yang lupa dilepas",
                    "    terus menyimpan rujukan ke elemen lama, sehingga elemen itu nggak",
                    "    bisa dibersihkan oleh garbage collector (pembersih memori",
                    "    otomatis). Akibatnya memory leak, alias memori bocor.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko online dengan ratusan foto produk biasanya memuat gambar cuma saat",
                    "kartunya hampir masuk layar. Halaman pertama jadi cepat terbuka, dan",
                    "kuota pengunjung nggak habis untuk gambar yang nggak pernah dilihat.",
                    "Sebagian situs berita memakai cara yang sama untuk memuat artikel",
                    "berikutnya saat pembaca sampai di bawah halaman.",
                    "",
                    "Kasus kecil: redaksi situs berita ingin tahu berapa pembaca yang",
                    "membaca sampai akhir artikel, dan nggak berhenti di paragraf pertama.",
                    "Datanya cukup dikirim sekali per kunjungan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Terjemahkan \"sampai akhir\" jadi sesuatu yang bisa diamati: elemen",
                    "     penanda di kaki artikel masuk area yang terlihat.",
                    "  2. Pilih IntersectionObserver, karena yang ditunggu elemen yang masuk",
                    "     layar. DOM-nya nggak berubah, jadi MutationObserver nggak cocok,",
                    "     dan event scroll menyala puluhan kali per detik.",
                    "      const pengamat = new IntersectionObserver((entries) => {",
                    "        if (!entries[0].isIntersecting) return;",
                    "        console.log(\"pembaca sampai di akhir\");   // kirim datanya di sini",
                    "        pengamat.disconnect();",
                    "      });",
                    "      pengamat.observe(document.querySelector(\"#akhir-artikel\"));",
                    "  3. disconnect() di dalam callback membuat datanya terkirim sekali per",
                    "     kunjungan, walau pembaca menggulir naik turun berkali-kali.",
                    "  4. Kasus pinggir: artikel pendek, cuma dua paragraf. Penandanya sudah",
                    "     terlihat begitu halaman dibuka, jadi callback langsung menyala",
                    "     dengan isIntersecting true. Putuskan dulu apakah itu dihitung",
                    "     selesai membaca. Kalau nggak, kirim datanya hanya kalau pembaca",
                    "     sudah berada di halaman lebih dari beberapa detik.",
                ]
            },
        ],
    },
    {
        "title": "32. Web API: Geolocation, Clipboard, dan Perangkat",
        "sections": [
            {
                "body": [
                    "Dua API di materi ini, Geolocation dan Clipboard, sama-sama tinggal di",
                    "objek navigator, dan sama-sama cuma ada di browser sungguhan. Coba",
                    "jalankan contoh di bawah pakai 'node file.js', dan yang keluar cuma",
                    "'ReferenceError: navigator is not defined'. Itu bukan salah ketik.",
                    "navigator memang nggak pernah ada di Node, sama seperti document dan",
                    "window di materi DOM Manipulation.",
                    "",
                    "Karena itu, contoh kode di materi ini nggak dijalankan otomatis dan",
                    "nggak mencetak apa pun yang bisa diperiksa di sini. Untuk mencobanya",
                    "sungguhan, kamu butuh tiga hal:",
                    "  - berkas HTML yang dibuka lewat server (http://localhost boleh, tapi",
                    "    begitu online harus https://),",
                    "  - tombol yang memang diklik orang,",
                    "  - dan izin yang kamu setujui sendiri lewat popup browser.",
                    "",
                    "Tiga syarat itu penting. Kedua API ini menyentuh privasi, yaitu lokasi",
                    "sungguhanmu dan isi clipboard sistemmu. Jadi browser sengaja",
                    "mempersulit kode yang mau memanggilnya tanpa sepengetahuan pengguna.",
                ]
            },
            {
                "heading": "Geolocation: getCurrentPosition, sekali ambil posisi",
                "body": [
                    "navigator.geolocation.getCurrentPosition(sukses, gagal, opsi) pakai",
                    "pola dua callback, dan nggak pakai Promise. Beda dengan fetch di materi",
                    "sebelumnya. Argumen pertama dipanggil kalau berhasil, argumen kedua",
                    "kalau gagal atau ditolak. Nggak ada .then(), nggak ada await.",
                    "",
                    "Objek position yang diterima callback sukses:",
                    "",
                    "  position.coords.latitude   -> lintang, angka desimal",
                    "  position.coords.longitude  -> bujur, angka desimal",
                    "  position.coords.accuracy   -> radius ketidakpastian, dalam METER",
                    "                               (bukan jaminan lokasinya presisi -",
                    "                               accuracy 50 berarti 'kemungkinan besar",
                    "                               di dalam radius 50 meter dari titik ini')",
                    "",
                    "Objek error yang diterima callback gagal selalu punya .code, dan",
                    "kemungkinannya cuma tiga. Hafalkan, karena browser nggak",
                    "menerjemahkannya:",
                    "",
                    "  code 1  PERMISSION_DENIED     pengguna menolak (atau sudah pernah",
                    "                                menolak dan browser tidak tanya lagi)",
                    "  code 2  POSITION_UNAVAILABLE  GPS/jaringan tidak bisa menentukan",
                    "                                lokasi",
                    "  code 3  TIMEOUT               lebih lama dari opsi.timeout dan",
                    "                                belum dapat jawaban",
                    "",
                    "Callback gagal itu wajib ada. Pengguna boleh menolak izin kapan aja.",
                    "Kode yang cuma punya callback sukses bakal diam total begitu ditolak.",
                    "Nggak error, nggak crash, cuma nggak ngapa-ngapain, dan pengguna nggak",
                    "tahu kenapa tombolnya kayak nggak berfungsi.",
                ],
                "code": """// Dijalankan di browser, biasanya di dalam event klik tombol.
function ambilLokasiSekali() {
    navigator.geolocation.getCurrentPosition(
        (position) => {                          // callback SUKSES
            const { latitude, longitude, accuracy } = position.coords;
            console.log(`Lokasi: ${latitude}, ${longitude}`);
            console.log(`Radius ketidakpastian: ${accuracy} meter`);
        },
        (error) => {                             // callback GAGAL - wajib ada
            switch (error.code) {
                case error.PERMISSION_DENIED:
                    console.log("Kamu menolak izin lokasi.");
                    break;
                case error.POSITION_UNAVAILABLE:
                    console.log("Lokasi tidak bisa ditentukan saat ini.");
                    break;
                case error.TIMEOUT:
                    console.log("Waktu tunggu habis, coba lagi.");
                    break;
            }
        },
        {
            enableHighAccuracy: true,   // minta GPS kalau ada, bukan cuma Wi-Fi/IP (lebih lambat & boros baterai)
            timeout: 5000,               // ms, sebelum callback gagal dipanggil dengan code TIMEOUT
            maximumAge: 0,                // 0 = jangan pakai posisi lama yang di-cache, selalu ambil baru
        }
    );
}""",
            },
            {
                "heading": "watchPosition: terus memantau, dan jebakan kalau lupa clearWatch",
                "body": [
                    "getCurrentPosition mengambil posisi sekali, lalu selesai. watchPosition",
                    "dipanggil dengan cara yang sama, tapi callback suksesnya dipanggil",
                    "berulang kali, setiap browser mendeteksi posisinya berubah. Cocok untuk",
                    "peta yang mengikuti pergerakan pengguna.",
                    "",
                    "  getCurrentPosition(...)  -> ambil sekali, selesai",
                    "  watchPosition(...)       -> terus memantau, mengembalikan watchId (angka)",
                    "  clearWatch(watchId)      -> WAJIB dipanggil untuk menghentikannya",
                    "",
                    "Jebakan: watchPosition nggak berhenti sendiri. Kalau halaman pindah",
                    "bagian (misalnya keluar dari tampilan peta) dan kamu lupa memanggil",
                    "clearWatch, browser tetap ngecek GPS terus di latar belakang. Baterai",
                    "perangkat pengguna terkuras untuk sesuatu yang sudah nggak dipakai",
                    "siapa pun. Ini mirip lupa clearInterval, tapi akibatnya lebih kerasa",
                    "karena GPS jauh lebih boros daripada timer biasa.",
                ],
                "code": """let watchId = null;

function mulaiPantauLokasi() {
    if (watchId !== null) return;   // sudah jalan, jangan dobel
    watchId = navigator.geolocation.watchPosition(
        (position) => {
            console.log("Posisi baru:", position.coords.latitude, position.coords.longitude);
        },
        (error) => console.log("Gagal memantau:", error.message),
        { enableHighAccuracy: true }
    );
}

function berhentiPantauLokasi() {
    if (watchId === null) return;
    navigator.geolocation.clearWatch(watchId);   // WAJIB - lihat JEBAKAN di atas
    watchId = null;
}

// Dipasang di tombol "Mulai" dan "Berhenti", atau di titik halaman ditinggalkan:
// tombolMulai.addEventListener("click", mulaiPantauLokasi);
// tombolBerhenti.addEventListener("click", berhentiPantauLokasi);""",
            },
            {
                "heading": "Clipboard API: menyalin dan membaca clipboard",
                "body": [
                    "navigator.clipboard.writeText(teks) dan navigator.clipboard.readText()",
                    "dua-duanya mengembalikan Promise. Beda dengan Geolocation di atas, API",
                    "ini cocok dipakai bareng await, seperti fetch.",
                    "",
                    "  await navigator.clipboard.writeText(teks)   -> Promise<void>",
                    "  await navigator.clipboard.readText()        -> Promise<string>",
                    "",
                    "Sebelum Clipboard API ada, satu-satunya cara menyalin teks lewat kode",
                    "adalah document.execCommand('copy'), dan itu selalu butuh trik. Bikin",
                    "<textarea> tersembunyi, isi dengan teksnya, pilih teksnya pakai",
                    ".select(), baru panggil execCommand('copy'), lalu buang lagi",
                    "elemennya. execCommand sekarang berstatus deprecated, artinya sudah",
                    "ditinggalkan. Clipboard API menggantinya dengan satu panggilan async",
                    "langsung, tanpa elemen DOM buatan.",
                    "",
                    "Jebakan: Clipboard API menuntut pemanggilannya terjadi dalam user",
                    "gesture, yaitu respons langsung dari interaksi pengguna seperti klik.",
                    "Ini aman:",
                    "",
                    "  tombol.addEventListener('click', () => navigator.clipboard.writeText(teks));",
                    "",
                    "Yang ini sering ditolak browser. Promise-nya berakhir dengan error,",
                    "karena gesture-nya sudah \"basi\" waktu clipboard dipanggil:",
                    "",
                    "  tombol.addEventListener('click', () => {",
                    "      setTimeout(() => navigator.clipboard.writeText(teks), 1000);",
                    "  });",
                    "",
                    "Menunggu Promise lain dulu (misalnya await fetch(...)) sebelum",
                    "memanggil clipboard juga berisiko sama di sebagian browser. Jedanya",
                    "bisa dianggap terlalu lama sejak klik terakhir. Aturan amannya: panggil",
                    "clipboard secepat mungkin di dalam handler klik, jangan sesudah await",
                    "yang lain.",
                ],
                "code": """// AMAN: dipanggil langsung dari handler klik.
tombolSalin.addEventListener("click", async () => {
    try {
        await navigator.clipboard.writeText("teks yang mau disalin");
        console.log("Tersalin ke clipboard.");
    } catch (error) {
        // Ditolak kalau izin belum diberikan, atau dipanggil di luar user gesture.
        console.log("Gagal menyalin:", error.message);
    }
});

tombolTempel.addEventListener("click", async () => {
    try {
        const teks = await navigator.clipboard.readText();
        console.log("Dari clipboard:", teks);
    } catch (error) {
        console.log("Gagal membaca clipboard:", error.message);
    }
});""",
            },
            {
                "heading": "Pola yang sama muncul di banyak Web API lain",
                "body": [
                    "Geolocation dan Clipboard bukan kasus khusus. Pola \"minta izin dulu,",
                    "baru pakai\" dipakai lagi di hampir semua Web API yang menyentuh hal",
                    "sensitif, misalnya kamera dan mikrofon (getUserMedia), juga notifikasi:",
                    "",
                    "  const izin = await Notification.requestPermission();",
                    "  // izin bernilai 'granted', 'denied', atau 'default' (belum dijawab)",
                    "  if (izin === 'granted') {",
                    "      new Notification('Judul', { body: 'Isi pesannya' });",
                    "  }",
                    "",
                    "Pola itu terdiri dari tiga hal: callback ganda atau Promise, error yang",
                    "wajib ditangani, serta syarat HTTPS dan user gesture. Kalau ketiganya",
                    "sudah kamu kuasai, API sensitif lain yang belum pernah kamu sentuh",
                    "bakal terasa familiar.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman web pemesanan antar makanan meminta lokasi untuk mengisi titik",
                    "antar, dan absensi pegawai berbasis web memeriksa apakah pegawai ada",
                    "di sekitar kantor. Tombol \"Salin\" untuk nomor virtual account di",
                    "halaman pembayaran bisa dibuat dengan Clipboard API.",
                    "",
                    "Kasus kecil: tombol \"Absen masuk\" mengambil lokasi pegawai. Kalau izin",
                    "ditolak atau GPS lama merespons, pegawai harus tahu apa yang terjadi.",
                    "Tombolnya nggak boleh diam saja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar semua hasil yang mungkin: lokasi didapat, izin ditolak",
                    "     (code 1), lokasi nggak tersedia (code 2), atau waktu habis",
                    "     (code 3). Tiap hasil butuh pesan sendiri.",
                    "  2. Panggil getCurrentPosition langsung di handler klik, dengan dua",
                    "     callback dan batas waktu:",
                    "      tombolAbsen.addEventListener(\"click\", () => {",
                    "        navigator.geolocation.getCurrentPosition(",
                    "          (pos) => kirimAbsen(pos.coords),",
                    "          (err) => { info.textContent = pesanGagal[err.code]; },",
                    "          { timeout: 10000 });",
                    "      });",
                    "  3. pesanGagal berisi satu kalimat untuk tiap code. Yang untuk code 1",
                    "     menjelaskan cara memberi izin lewat pengaturan browser, karena",
                    "     browser nggak bertanya lagi sesudah ditolak.",
                    "  4. Kasus pinggir: accuracy-nya 800 meter karena lokasi cuma ditebak",
                    "     dari Wi-Fi. Lokasinya belum tentu salah, tapi terlalu kabur untuk",
                    "     memutuskan pegawai ada di kantor atau nggak. Tolak absen kalau",
                    "     accuracy melewati batas yang disepakati, misalnya 100 meter.",
                    "",
                    "Ingat: begitu online, halaman ini wajib dibuka lewat https://. Di http",
                    "biasa, browser menolak memberi lokasi.",
                ]
            },
        ],
    },
    {
        "title": "33. Canvas API: Menggambar dengan JavaScript",
        "sections": [
            {
                "body": [
                    "Materi 'Canvas' di kurikulum HTML sudah mengenalkan elemen <canvas>.",
                    "Di sana dijelaskan bahwa atribut width/height-nya beda dengan",
                    "width/height di CSS (lihat lagi materi itu kalau lupa kenapa). Yang",
                    "belum dijawab: gimana caranya sesuatu muncul di dalam kotak kosong",
                    "itu. Jawabannya ada di sini, dan semuanya lewat JavaScript. Nggak ada",
                    "satu pun atribut HTML yang bisa menggambar bentuk.",
                    "",
                    "Sama seperti dua materi Web API sebelumnya, kode di sini butuh",
                    "<canvas> sungguhan di sebuah halaman HTML yang dibuka di browser. Kalau",
                    "ditempel ke 'node file.js' polos, kodenya gagal di baris pertama,",
                    "karena document nggak ada di Node.",
                ],
            },
            {
                "heading": "getContext(\"2d\"): kuasnya, bukan kanvasnya",
                "body": [
                    "Elemen <canvas> sendiri cuma kotak kosong. Semua perintah menggambar",
                    "dikirim lewat objek lain yang diminta dari kanvas itu, namanya",
                    "rendering context. Ibaratnya kanvas itu kertasnya, dan context itu",
                    "kuasnya. Sebelum objek ini diminta, nggak ada satu pun method gambar",
                    "yang bisa dipanggil.",
                    "",
                    "  const kanvas = document.querySelector(\"canvas\");",
                    "  const ctx = kanvas.getContext(\"2d\");",
                    "",
                    "'2d' menyebut jenis context yang diminta. Ada juga 'webgl' untuk grafis",
                    "3D, tapi API itu jauh lebih rumit dan nggak dibahas di sini. Semua",
                    "perintah menggambar sesudah baris ini adalah method dan properti milik",
                    "ctx, dan bukan milik elemen kanvas-nya langsung.",
                ],
            },
            {
                "heading": "Sistem koordinat: (0,0) di pojok kiri atas",
                "body": [
                    "Jebakan pertama yang bikin hampir semua orang keliru: di pelajaran",
                    "matematika sekolah, sumbu Y bertambah ke atas. Di canvas, sumbu Y",
                    "bertambah ke bawah, dan titik (0,0) ada di pojok kiri atas kanvas.",
                    "Bukan di tengah, dan bukan di kiri bawah.",
                    "",
                    "  (0,0) ---------> x bertambah",
                    "    |",
                    "    v",
                    "  y bertambah",
                    "",
                    "Akibatnya, kalau kamu mau sebuah bentuk \"naik\", kurangi nilai y-nya.",
                    "Jangan ditambah. Ini sumber bug paling umum di animasi canvas pertama",
                    "seseorang. Bentuknya bergerak tanpa error, tapi ke arah yang",
                    "berlawanan dari bayangannya.",
                ],
            },
            {
                "heading": "Bentuk langsung: fillRect, strokeRect, clearRect",
                "body": [
                    "Tiga method ini nggak butuh path sama sekali. Satu panggilan langsung",
                    "jadi satu kotak. Keempat argumennya selalu berurutan sama: x, y, lebar,",
                    "tinggi.",
                ],
                "code": """const kanvas = document.querySelector("canvas");
const ctx = kanvas.getContext("2d");

ctx.fillStyle = "royalblue";
ctx.fillRect(20, 20, 100, 60);      // kotak terisi, mulai dari (20,20)

ctx.strokeStyle = "crimson";
ctx.lineWidth = 4;
ctx.strokeRect(140, 20, 100, 60);   // cuma garis tepinya

// clearRect BUKAN "gambar putih" - ia membuat area itu transparan lagi,
// mengembalikannya ke kondisi kosong seperti sebelum ada yang digambar.
ctx.clearRect(50, 30, 20, 20);      // melubangi bagian dari kotak biru di atas""",
            },
            {
                "heading": "Path: beginPath, moveTo, lineTo, arc",
                "body": [
                    "Untuk bentuk selain kotak, menggambarnya dua tahap. Pertama rangkai",
                    "dulu jalurnya (path), lalu gambar dengan fill() atau stroke(). Jalur",
                    "yang belum digambar nggak kelihatan sama sekali di kanvas.",
                    "",
                    "  ctx.beginPath()        mulai jalur baru, buang sisa jalur lama",
                    "  ctx.moveTo(x, y)       pindahkan 'pena' tanpa menggambar garis",
                    "  ctx.lineTo(x, y)       gambar garis lurus dari posisi pena ke sini",
                    "  ctx.closePath()        tutup jalur, garis balik ke titik awal",
                    "  ctx.fill() / .stroke() BARU di sini sesuatu muncul di layar",
                    "",
                    "arc() dipakai untuk lingkaran atau busur, dan punya lima argumen wajib.",
                    "Argumen sudutnya dalam radian, bukan derajat. Ini jebakan kedua, dan",
                    "sama seringnya dengan sumbu Y yang terbalik:",
                    "",
                    "  ctx.arc(x, y, radius, sudutMulai, sudutSelesai)",
                    "",
                    "Lingkaran penuh selalu ditulis 0 sampai Math.PI * 2, dan bukan 0",
                    "sampai 360. Kalau kamu nulis 0 sampai 360, kodenya tetap jalan tanpa",
                    "error. Selisih sudut yang lebih dari satu putaran penuh (Math.PI * 2)",
                    "digambar sebagai lingkaran penuh, jadi hasilnya tetap kelihatan seperti",
                    "lingkaran biasa. Bug ini gampang lolos sampai seseorang mencoba",
                    "menggambar setengah lingkaran pakai 0 sampai 180. 180 radian itu",
                    "lebih dari 28 putaran, jadi yang muncul malah lingkaran penuh.",
                ],
                "code": """ctx.beginPath();
ctx.moveTo(50, 150);
ctx.lineTo(120, 150);
ctx.lineTo(85, 90);
ctx.closePath();          // garis ketiga ke titik awal, membentuk segitiga
ctx.fillStyle = "seagreen";
ctx.fill();

ctx.beginPath();
// Lingkaran penuh: radius 40, dari sudut 0 sampai satu putaran penuh (2*PI radian).
ctx.arc(220, 130, 40, 0, Math.PI * 2);
ctx.fillStyle = "orange";
ctx.fill();

ctx.beginPath();
// Setengah lingkaran: PI radian = 180 derajat, BUKAN 180 yang ditulis langsung.
ctx.arc(320, 130, 40, 0, Math.PI);
ctx.strokeStyle = "purple";
ctx.lineWidth = 3;
ctx.stroke();""",
            },
            {
                "heading": "fillStyle dan strokeStyle: state yang menempel",
                "body": [
                    "Kalau kamu pernah pakai SVG, ini beda besarnya. Di SVG, tiap bentuk",
                    "punya atributnya sendiri-sendiri. Di canvas, fillStyle, strokeStyle,",
                    "dan lineWidth adalah properti milik context. Sekali diatur, nilainya",
                    "berlaku untuk semua gambar berikutnya sampai diubah lagi. Nggak ada",
                    "reset otomatis antar bentuk.",
                    "",
                    "Jebakan: kalau kamu lupa mengatur ulang warna sebelum menggambar",
                    "bentuk berikutnya, warna bentuk sebelumnya ikut kebawa ke bentuk baru.",
                    "Itu bukan bug, karena context memang dirancang menyimpan pengaturan",
                    "seperti itu. Kalau sebuah loop menggambar banyak bentuk dengan warna",
                    "yang beda-beda, fillStyle harus diatur ulang di setiap putaran.",
                ],
            },
            {
                "heading": "Animasi: clearRect tiap frame + requestAnimationFrame",
                "body": [
                    "Canvas nggak punya konsep \"gerakkan bentuk ini\". Sesudah digambar,",
                    "nggak ada objek bentuk yang tersimpan, yang tersisa cuma piksel. Jadi",
                    "animasi artinya: bersihkan seluruh kanvas, lalu gambar ulang semuanya",
                    "di posisi yang sedikit berbeda, dan ulangi puluhan kali per detik.",
                    "",
                    "requestAnimationFrame (rAF) dibahas lengkap di materi 'Web API:",
                    "Observer dan Animasi'. Di sini cukup ingat dua hal. rAF memanggil",
                    "fungsi yang kamu berikan tepat sebelum browser menggambar frame",
                    "berikutnya. Dan rAF harus dipanggil ulang sendiri di dalam fungsi itu,",
                    "supaya frame selanjutnya terjadi.",
                ],
                "code": """const kanvas = document.querySelector("canvas");
const ctx = kanvas.getContext("2d");

let x = 20;
const kecepatan = 3;

function gambarFrame() {
    // 1. Bersihkan SELURUH kanvas - tanpa ini, bola lama tetap tertinggal
    //    dan hasilnya jadi garis bola yang menumpuk, bukan satu bola bergerak.
    ctx.clearRect(0, 0, kanvas.width, kanvas.height);

    // 2. Gambar ulang di posisi baru.
    ctx.beginPath();
    ctx.arc(x, 75, 20, 0, Math.PI * 2);
    ctx.fillStyle = "tomato";
    ctx.fill();

    // 3. Perbarui posisi untuk frame BERIKUTNYA, lalu pantul di tepi.
    x += kecepatan;
    if (x > kanvas.width - 20 || x < 20) {
        // (Contoh sengaja tidak membalik arah supaya tetap pendek -
        //  materi 'Observer dan Animasi' membahas pola pantul penuh.)
        x = 20;
    }

    // 4. Minta browser memanggil gambarFrame lagi sebelum frame berikutnya.
    //    Tanpa baris ini animasinya berhenti setelah frame pertama.
    requestAnimationFrame(gambarFrame);
}

requestAnimationFrame(gambarFrame);   // mulai loop-nya""",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Canvas dipakai untuk gambar yang disusun piksel demi piksel: grafik",
                    "penjualan di dasbor, kolom tanda tangan digital di formulir serah",
                    "terima barang, dan game di browser. Library grafik seperti Chart.js",
                    "juga menggambar di elemen <canvas>.",
                    "",
                    "Kasus kecil: dasbor UMKM butuh grafik batang penjualan lima hari",
                    "terakhir, dalam ribuan rupiah: 120, 80, 150, 60, dan 100. Kanvasnya",
                    "300 x 200 piksel, dan batang tertinggi harus hampir menyentuh atas.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ubah angka jadi tinggi piksel. Nilai terbesar 150 dipetakan ke",
                    "     180 piksel, jadi tiap nilai dikali 180 / 150.",
                    "  2. Ingat sumbu Y terbalik. Batang tumbuh dari bawah, jadi y-nya",
                    "     adalah tinggi kanvas dikurangi tinggi batang. ctx di sini hasil",
                    "     getContext(\"2d\"):",
                    "      const data = [120, 80, 150, 60, 100];",
                    "      const skala = 180 / Math.max(...data);",
                    "      data.forEach((nilai, i) => {",
                    "        const t = nilai * skala;",
                    "        ctx.fillRect(10 + i * 58, 200 - t, 40, t);",
                    "      });",
                    "  3. Tiap slot lebarnya 58 piksel: batang 40 ditambah jarak 18. Lima",
                    "     slot ditambah margin kiri 10 piksel pas di kanvas selebar 300.",
                    "  4. Kasus pinggir: toko libur lima hari, semua nilainya 0. skala jadi",
                    "     180 / 0 = Infinity, dan 0 * Infinity menghasilkan NaN. Pakai skala",
                    "     0 kalau nilai terbesarnya 0.",
                    "",
                    "Jebakan: kalau batang hari ini mau diberi warna lain, atur fillStyle di",
                    "setiap putaran. Warna yang terakhir dipasang menempel ke batang-batang",
                    "sesudahnya.",
                ]
            },
        ],
    },
    {
        "title": "34. Membaca Repo JavaScript Sungguhan",
        "sections": [
            {
                "body": [
                    "Bahasa JavaScript-nya udah kamu kuasai. Sekarang soal yang belum pernah",
                    "dibahas: apa yang muncul di layar waktu kamu membuka repo JavaScript",
                    "orang lain di GitHub. Repo (repository) itu folder proyek yang isi dan",
                    "riwayat perubahannya dicatat Git.",
                    "",
                    "Yang pertama kelihatan biasanya bukan kode. Kamu bakal ketemu dua",
                    "puluhan berkas asing di akar folder, dan gampang ngerasa ada yang",
                    "kelewat waktu belajar. Perasaan itu hampir selalu keliru.",
                    "",
                    "Sebagian besar isi sebuah repo nggak ditulis manusia. Isinya dihasilkan",
                    "mesin, dan memang nggak untuk dibaca. Kalau kamu tahu ini dari awal,",
                    "kamu hemat waktu berjam-jam. Dari seluruh pohon di bawah, yang perlu",
                    "kamu buka cuma dua folder: src/ dan tests/.",
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
                "heading": "Berkas di akar: yang mengatur perkakas, bukan yang dijalankan",
                "body": [
                    "Berkas yang namanya diawali titik, atau berakhiran .config.js, hampir",
                    "selalu bukan bagian program. Berkas-berkas itu menyetel perkakas di",
                    "sekitar program.",
                    "",
                    "  - .gitignore: daftar berkas yang nggak ikut disimpan Git.",
                    "    node_modules/ dan .env hampir selalu tercantum di sini.",
                    "  - package-lock.json: versi persis tiap paket, sampai ke dependency",
                    "    milik dependency. Berkas ini dihasilkan npm dan ikut di-commit,",
                    "    tapi nggak pernah disunting pakai tangan dan nggak untuk dibaca.",
                    "  - node_modules/: isi semua paket yang terpasang. Jangan ikut mencari",
                    "    di folder ini. Hasil pencarian di sana bukan kode proyekmu.",
                    "  - .env: password database dan API key. Berkas ini jangan sampai",
                    "    di-commit. Sekali masuk riwayat Git, isinya tetap ada walaupun",
                    "    berkasnya kamu hapus besoknya. Yang di-commit cuma .env.example,",
                    "    yang nilai-nilainya dikosongkan.",
                    "  - .eslintrc.json: aturan linter, yaitu alat yang menandai kode yang",
                    "    rawan salah atau gayanya nggak seragam. Bentuk barunya",
                    "    eslint.config.js.",
                    "  - .prettierrc: aturan perapian otomatis, misalnya jenis tanda kutip,",
                    "    koma, dan lebar baris.",
                    "  - tsconfig.json: setelan TypeScript. Kalau berkas ini ada, repo-nya",
                    "    pakai TypeScript, walaupun sebagian berkasnya berakhiran .js.",
                    "  - vite.config.js: setelan build tool, yaitu alat yang mengolah kode",
                    "    di src/ jadi berkas siap pakai di dist/.",
                    "",
                    "Angka versi di bagian \"dependencies\" juga punya arti. Urutannya",
                    "major.minor.patch. Tanda di depan angka menentukan seberapa jauh paket",
                    "itu boleh naik versi sendiri waktu orang lain menjalankan npm install:",
                    "",
                    "  \"react\": \"18.2.0\"    persis segitu, nggak pernah bergerak",
                    "  \"react\": \"^18.2.0\"   boleh naik selama angka pertama tetap 18",
                    "                       (18.3.1 boleh, 19.0.0 nggak). Ini bawaan npm install",
                    "  \"react\": \"~18.2.0\"   boleh naik pada angka ketiga saja",
                    "                       (18.2.9 boleh, 18.3.0 nggak)",
                    "",
                    "Arti tiap angkanya:",
                    "  - major naik: ada yang dirombak, dan kode lama bisa rusak.",
                    "  - minor naik: ada fitur baru yang nggak merusak.",
                    "  - patch naik: ada perbaikan bug.",
                    "",
                    "Di sinilah package-lock.json berguna. Berkas itu mengunci versi yang",
                    "terpasang di komputermu, supaya komputer temanmu memasang versi yang",
                    "persis sama.",
                    "",
                    "Satu perintah lagi muncul di README hampir semua proyek modern, yaitu",
                    "npx. npx menjalankan sebuah paket tanpa memasangnya dulu. Biasanya",
                    "dipakai untuk perkakas yang cuma dijalankan sekali seumur proyek:",
                    "",
                    "  npx create-vite@latest aplikasiku   membuat kerangka proyek baru",
                    "  npx eslint src/                     menjalankan linter tanpa memasangnya",
                ],
            },
            {
                "heading": "JSDoc, dan bukti bahwa describe/it/expect cuma fungsi biasa",
                "body": [
                    "Di repo sungguhan, di atas ribuan fungsi ada blok komentar yang dibuka",
                    "dengan dua bintang: /** ... */. Namanya JSDoc, yaitu komentar yang",
                    "ditulis dengan aturan tertentu. Waktu membaca fungsi buatan orang lain,",
                    "blok ini biasanya bagian yang paling menolong. Isinya nyebutin tipe",
                    "tiap parameter, dan tipe itu nggak kelihatan dari kodenya sendiri.",
                    "",
                    "  @param {string} nama    parameter 'nama', isinya string",
                    "  @param {number} [umur]  kurung siku berarti opsional, boleh tidak diisi",
                    "  @returns {number}       apa yang dikembalikan",
                    "  @throws {Error}         kapan fungsinya melempar error",
                    "",
                    "Editor seperti VS Code membaca blok ini, lalu nampilinnya sebagai",
                    "bantuan waktu kamu ngetik pemanggilan fungsinya. Kalau tipe yang",
                    "ditulis salah, programnya nggak error. Yang kena cuma orang berikutnya",
                    "yang membaca: dia jadi salah paham.",
                    "",
                    "Program di bawah juga menjawab pertanyaan yang hampir pasti muncul",
                    "waktu kamu membuka berkas tes: describe, it, dan expect itu kata kunci",
                    "JavaScript, ya? Bukan. Ketiganya fungsi biasa. Buktinya, dua puluh satu",
                    "baris di program ini cukup untuk bikin ketiganya sendiri.",
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
                "heading": "Berkas tes: bacaan terbaik di repo yang belum kamu kenal",
                "body": [
                    "Nama berkas tes mengikuti nama berkas yang diujinya, ditambah .test.js",
                    "atau .spec.js:",
                    "",
                    "  src/keranjang.js          kode yang diuji",
                    "  tests/keranjang.test.js   tesnya",
                    "",
                    "Bentuknya bersarang tiga tingkat. describe membungkus beberapa it, dan",
                    "tiap it berisi satu atau beberapa expect:",
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
                    "Berkas ini nggak dijalankan pakai perintah node. Fungsi describe, it,",
                    "dan expect baru ada kalau berkasnya dijalankan Jest atau Vitest, yaitu",
                    "alat penjalan tes. Biasanya lewat script di package.json:",
                    "",
                    "  npm test     (isinya biasanya \"jest\" atau \"vitest run\")",
                    "",
                    "Tes justru paling layak dibaca duluan, karena:",
                    "  - Tes nunjukin sebuah fungsi dipanggil dengan data sungguhan, lengkap",
                    "    dengan hasil yang diharapkan. Dokumentasi bisa basi tanpa ada yang",
                    "    sadar. Tes yang basi langsung gagal.",
                    "  - Kalimat di dalam it(\"...\") menjelaskan maksud fungsinya pakai",
                    "    bahasa manusia, sering lebih jelas daripada nama fungsinya sendiri.",
                    "  - Kasus aneh, misalnya array kosong, angka minus, atau teks kosong,",
                    "    biasanya cuma tercatat di tes. Di README mana pun nggak ada.",
                ],
            },
            {
                "heading": "Berkas .js yang isinya bukan JavaScript polos",
                "body": [
                    "Cepat atau lambat kamu bakal membuka berkas .js atau .jsx, lalu nemu",
                    "sesuatu yang mirip HTML di tengah sebuah fungsi:",
                    "",
                    "  function Tombol({ label }) {",
                    "      return <button className=\"utama\">{label}</button>;",
                    "  }",
                    "",
                    "Itu JSX, yang dipakai React. Kamu juga bakal nemu berkas .ts atau .tsx",
                    "yang penuh titik dua:",
                    "",
                    "  interface User { nama: string; umur: number; }",
                    "  const sapa = (u: User): string => `Halo ${u.nama}`;",
                    "  import type { Produk } from \"./produk\";   // impor yang cuma bawa tipe",
                    "",
                    "Itu TypeScript, yaitu JavaScript yang ditambah keterangan tipe.",
                    "",
                    "Browser nggak bisa menjalankan keduanya apa adanya. Node versi baru",
                    "(misalnya Node 24) udah bisa menjalankan berkas .ts yang tambahannya",
                    "cuma keterangan tipe: tipenya dibuang dulu, sisanya dijalankan. Tapi",
                    "fitur TypeScript seperti enum tetap ditolak, dan JSX sama sekali nggak",
                    "dikenal Node. Makanya proyek sungguhan hampir selalu punya langkah",
                    "kompilasi (Vite, Babel, atau tsc). Langkah itu mengubah kodenya jadi",
                    "JavaScript biasa, persis JavaScript yang udah kamu pelajari.",
                    "",
                    "Jadi kalau waktu membacanya kamu ngerasa ada sintaks yang kelewat,",
                    "tenang aja. Nggak ada yang kelewat. JSX dan TypeScript itu bahasa lain",
                    "yang ditumpuk di atas JavaScript, dan dipelajari terpisah nanti (lihat",
                    "materi Roadmap Menjadi JavaScript Developer Handal).",
                    "",
                    "Urutan yang dipakai orang berpengalaman waktu membuka repo yang sama",
                    "sekali asing:",
                    "  1. README.md: untuk apa proyek ini dan cara menjalankannya.",
                    "  2. Bagian \"scripts\" di package.json: perintah yang memang tersedia",
                    "     (npm run dev, npm test, npm run build). Bagian ini daftar isi",
                    "     proyek yang asli.",
                    "  3. src/main.js atau src/index.js: titik masuk program. Dari situ,",
                    "     ikuti import satu per satu, sedalam yang kamu butuhkan aja.",
                    "  4. Berkas tes untuk bagian yang mau kamu ubah.",
                    "",
                    "Yang nggak dilakukan siapa pun: membuka berkas satu per satu dari atas",
                    "ke bawah, atau mencoba memahami isi node_modules/.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hari pertama PKL atau kerja, tugas pertamamu sering berupa membetulkan",
                    "bug kecil di repo yang sudah berjalan lama, dan jarang menulis fitur",
                    "baru dari nol. Yang diuji di situ kemampuan menemukan bagian kode yang",
                    "tepat di antara ratusan berkas, lalu membuktikan perbaikanmu benar.",
                    "",
                    "Kasus kecil: kasir melapor, \"Diskon 0 persen bikin total jadi Rp 0.\"",
                    "Repo-nya toko-online seperti pohon di atas, dan kamu belum pernah",
                    "membukanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca README.md dan bagian \"scripts\" di package.json untuk tahu",
                    "     cara menjalankan proyek dan tesnya, biasanya npm install lalu",
                    "     npm test.",
                    "  2. Cari kata dari laporannya, misalnya diskon, di src/ dan tests/",
                    "     saja. node_modules/ dan dist/ dilewati, karena isinya bukan kode",
                    "     yang ditulis tim.",
                    "  3. Buka berkas tes fungsi itu. Kalau belum ada kasus diskon 0, tulis",
                    "     dulu tesnya, jalankan, dan pastikan tes itu gagal. Tes yang gagal",
                    "     membuktikan kamu sudah menemukan bug yang sama dengan laporan:",
                    "      it(\"diskon 0 persen mengembalikan harga utuh\", () => {",
                    "        expect(hargaSetelahDiskon(50000, 0)).toBe(50000);",
                    "      });",
                    "  4. Betulkan kodenya sampai tes itu lulus, lalu jalankan seluruh tes.",
                    "     Tambahkan juga kasus pinggir di seberangnya, diskon 100 persen,",
                    "     yang hasilnya harus 0.",
                    "",
                    "Ingat: kalau proyek butuh berkas .env untuk jalan, salin dari",
                    ".env.example lalu isi sendiri. Berkas .env-mu jangan ikut di-commit.",
                ]
            },
        ],
    },
    {
        "title": "35. Roadmap Menjadi JavaScript Developer Handal",
        "sections": [
            {
                "body": [
                    "Fondasi JavaScript-mu sekarang udah kuat: sintaks, closure, this, OOP,",
                    "exception, sampai async/await dan fetch. Berikut peta jalan (roadmap)",
                    "yang realistis untuk melangkah lebih jauh.",
                    "",
                    "Tahap 1: kuatkan fondasi (kamu ada di sini)",
                    "  - Pahami beda var, let, dan const, juga closure, this, dan async.",
                    "  - Latihan soal JavaScript di HackerRank atau Codewars.",
                    "",
                    "Tahap 2: pilih jalur spesialisasi",
                    "",
                    "Frontend, yaitu bagian yang tampil di browser:",
                    "  - Framework UI: React (paling populer), Vue, atau Angular. Framework",
                    "    itu kerangka siap pakai untuk membangun tampilan.",
                    "  - HTML dan CSS. Dua-duanya wajib dikuasai bareng JavaScript.",
                    "  - TypeScript, yaitu JavaScript ditambah static typing: tipe tiap",
                    "    variabel diperiksa sebelum program jalan. Sekarang TypeScript udah",
                    "    jadi standar industri.",
                    "",
                    "Backend, yaitu program yang jalan di server:",
                    "  - Node.js dengan Express, Fastify, atau NestJS untuk bikin server",
                    "    REST API, yaitu server yang ngasih data ke aplikasi lain lewat",
                    "    HTTP.",
                    "  - Database: MongoDB (NoSQL) atau PostgreSQL (relasional).",
                    "",
                    "Mobile:",
                    "  - React Native, untuk bikin aplikasi iOS dan Android pakai",
                    "    JavaScript dan React.",
                ]
            },
            {
                "body": [
                    "Tahap 3: bangun proyek nyata",
                    "  1. To-do list dengan localStorage, jadi datanya tersimpan di browser.",
                    "  2. Aplikasi cuaca yang mengambil data dari API publik pakai fetch.",
                    "  3. REST API sederhana dengan Node.js, Express, dan database.",
                    "  4. Aplikasi full-stack: frontend React, backend Node.js, dan",
                    "     database.",
                    "  5. Apa pun proyeknya, wajib pakai Git dan disertai tes dasar.",
                    "",
                    "Tahap 4: kebiasaan profesional",
                    "  1. Pakai ESLint dan Prettier supaya kodenya rapi dan konsisten.",
                    "  2. Pelajari TypeScript, yang hampir jadi standar wajib di industri.",
                    "  3. Pahami build tool seperti Vite atau Webpack untuk bundling",
                    "     proyek, yaitu menggabungkan banyak berkas jadi berkas siap pakai.",
                    "  4. Testing: Jest atau Vitest untuk unit test JavaScript.",
                    "  5. Baca kode open source yang populer (React, Express) di GitHub.",
                ]
            },
            {
                "body": [
                    "Kebiasaan harian supaya makin jago:",
                    "  1. Ketik ulang semua contoh di aplikasi ini. Jangan copy-paste.",
                    "  2. Buka console browser (F12), lalu bereksperimen langsung di sana.",
                    "  3. Pahami betul closure, this, dan event loop (mesin di balik kode",
                    "     async). Tiga hal ini yang paling sering ditanyakan di wawancara",
                    "     kerja JavaScript.",
                    "  4. Baca pesan error di console dengan teliti. Stack trace, yaitu",
                    "     daftar pemanggilan fungsi saat error terjadi, nunjukin persis",
                    "     baris mana yang bermasalah.",
                    "  5. Kuasai SQL (ada kurikulumnya di aplikasi ini) untuk melengkapi",
                    "     kemampuanmu sebagai full-stack JavaScript developer.",
                    "",
                    "JavaScript terus berkembang cepat. Fitur ES6 ke atas (versi 2015 dan",
                    "sesudahnya) yang kamu pelajari di sini adalah fondasi wajib sebelum",
                    "belajar framework apa pun (React, Vue, dan lainnya) atau Node.js.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Waktu melamar posisi junior developer, kamu bakal sering ditanya",
                    "proyek apa yang pernah kamu buat, dan formulir lamaran sering meminta",
                    "tautan GitHub. Proyek kecil yang selesai dan bisa dicoba orang lain",
                    "lebih mudah dinilai daripada daftar materi yang sudah dibaca.",
                    "",
                    "Kasus kecil: kamu punya waktu sebulan dan mau satu proyek yang memakai",
                    "sebanyak mungkin yang sudah dipelajari: pencatat kas harian untuk",
                    "warung keluarga.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan versi paling kecil yang sudah berguna: catat pemasukan",
                    "     dan pengeluaran, lalu tampilkan saldo. Grafik menunggu versi",
                    "     berikutnya.",
                    "  2. Petakan fiturnya ke materi: form dan validasi angka, reduce untuk",
                    "     saldo, localStorage lewat JSON, dan Date untuk tanggal. Datanya",
                    "     cukup array object:",
                    "      const transaksi = [",
                    "        { tanggal: \"2026-10-01\", jenis: \"masuk\", jumlah: 250000 },",
                    "        { tanggal: \"2026-10-01\", jenis: \"keluar\", jumlah: 90000 },",
                    "      ];",
                    "      const saldo = transaksi.reduce((s, t) =>",
                    "        t.jenis === \"masuk\" ? s + t.jumlah : s - t.jumlah, 0);   // 160000",
                    "  3. Pecah jadi target mingguan: minggu 1 form dan daftar, minggu 2",
                    "     simpan dan muat, minggu 3 rekap per bulan, minggu 4 tulis README",
                    "     dan unggah ke GitHub.",
                    "  4. Sebelum bilang selesai, uji kasus pinggirnya: isian kosong, jumlah",
                    "     minus, dan localStorage yang masih kosong (null) waktu aplikasi",
                    "     pertama kali dibuka.",
                    "",
                    "Ingat: simpan jumlah sebagai bilangan bulat rupiah, seperti saran di",
                    "materi Angka, supaya saldo nggak meleset karena pecahan desimal.",
                ]
            },
        ],
    },
]
