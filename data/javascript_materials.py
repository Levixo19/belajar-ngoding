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
                    "  5. File JavaScript berekstensi .js",
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
                    "  const  -> untuk nilai yang TIDAK BERUBAH (konstan).",
                    "            Block-scoped juga. GUNAKAN INI SEBAGAI DEFAULT,",
                    "            baru pakai 'let' jika memang perlu diubah nanti.",
                    "",
                    "  const nama = \"Andi\";      // tidak bisa di-assign ulang",
                    "  let umur = 20;             // bisa diubah: umur = 21;",
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
        ],
    },
    {
        "title": "4. Percabangan (if / else / switch)",
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
        ],
    },
    {
        "title": "5. Perulangan (for, while, for...of, for...in)",
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
        ],
    },
    {
        "title": "6. String & Template Literal",
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
        ],
    },
    {
        "title": "7. Array & Method Array (map/filter/reduce)",
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
        ],
    },
    {
        "title": "8. Object & Destructuring",
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
        ],
    },
    {
        "title": "9. Function: Declaration, Expression & Arrow Function",
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
                    "",
                    "Function sebagai 'first-class citizen': bisa disimpan ke variabel,",
                    "dikirim sebagai argumen, dan dikembalikan dari fungsi lain",
                    "(dasar dari higher-order function & callback).",
                ]
            },
        ],
    },
    {
        "title": "10. Scope & Closure",
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
        ],
    },
    {
        "title": "11. Keyword 'this' & Context",
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
        ],
    },
    {
        "title": "12. OOP: Class & Object (ES6+)",
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
        ],
    },
    {
        "title": "13. Prototype: OOP di Balik Layar JavaScript",
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
        "title": "14. Exception Handling",
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
        ],
    },
    {
        "title": "15. Asynchronous JavaScript: Callback",
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
                ]
            },
        ],
    },
    {
        "title": "16. Asynchronous JavaScript: Promise",
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
        "title": "17. Asynchronous JavaScript: async/await",
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
        "title": "18. DOM Manipulation & Event Dasar",
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
        "title": "19. JSON & Fetch API",
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
        ],
    },
    {
        "title": "20. Module (import/export) & npm Dasar",
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
        "title": "21. Roadmap Menjadi JavaScript Developer Handal",
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
