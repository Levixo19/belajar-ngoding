TYPESCRIPT_MATERIALS = [
    {
        "title": "1. Pengenalan TypeScript & Instalasi",
        "sections": [
            {
                "body": [
                    "TypeScript itu JavaScript yang ditambahi tipe. Kamu nulis kode seperti",
                    "biasa, lalu di beberapa tempat kamu kasih keterangan jenis datanya: ini",
                    "teks, ini angka, ini daftar murid. Sebelum programnya jalan, TypeScript",
                    "ngecek apakah kodemu cocok dengan keterangan itu.",
                    "",
                    "Sedikit latar belakangnya:",
                    "  - Dibuat Microsoft dan dirilis tahun 2012.",
                    "  - Perancangnya Anders Hejlsberg, orang yang sama yang membuat Turbo",
                    "    Pascal, Delphi, dan C#.",
                    "  - TypeScript adalah superset JavaScript, artinya semua yang ada di",
                    "    JavaScript juga ada di TypeScript. Kode .js bisa dipindah ke berkas",
                    "    .ts apa adanya. Bedanya, di berkas .ts tipenya ikut diperiksa, jadi",
                    "    kode JavaScript yang sah pun bisa dapat error tipe.",
                    "  - Tambahan utamanya satu: sistem tipe statis. Statis artinya tipe",
                    "    diperiksa waktu kode ditulis dan dikompilasi, sebelum program",
                    "    dijalankan.",
                    "",
                    "Kalimat paling penting di seluruh materi TypeScript ada di sini, jadi",
                    "pegang dari sekarang: tipe hilang waktu program jalan.",
                    "",
                    "Komputer nggak pernah menjalankan TypeScript apa adanya. Kodenya selalu",
                    "diubah dulu jadi JavaScript biasa. Proses ini namanya kompilasi, dan",
                    "programnya disebut compiler (untuk TypeScript namanya tsc). Waktu",
                    "kompilasi, semua keterangan tipe dihapus. Di hasil akhirnya nggak",
                    "tersisa satu pun pemeriksaan tipe. Jadi yang kamu dapat adalah",
                    "pemeriksaan waktu menulis kode, bukan waktu kode dijalankan.",
                    "",
                    "Akibatnya sering bikin kaget:",
                    "  - Data yang datang dari API (layanan lain yang kamu mintai data), dari",
                    "    JSON, atau dari berkas nggak diperiksa sama sekali. Menulis",
                    "    `as Murid`, artinya \"anggap aja data ini Murid\", cuma janji ke",
                    "    compiler. Waktu program jalan, nggak ada yang ngecek janji itu.",
                    "  - Kamu nggak bisa memakai typeof untuk ngecek apakah sebuah nilai",
                    "    cocok dengan interface buatanmu sendiri. Interface adalah cara",
                    "    TypeScript menamai bentuk objek, dan waktu program jalan dia udah",
                    "    nggak ada.",
                    "  - Untuk memeriksa data dari luar, kamu butuh pustaka seperti Zod,",
                    "    atau menulis fungsi pemeriksa sendiri.",
                    "",
                    "Sebagai gantinya, kamu dapat ini:",
                    "  - Salah ketik nama properti ketahuan waktu kamu masih mengetik.",
                    "  - Autocomplete, yaitu saran isian dari editor, tahu persis isi",
                    "    objekmu.",
                    "  - Refactor jadi aman. Refactor artinya merapikan susunan kode tanpa",
                    "    mengubah perilakunya. Kalau kamu mengganti sebuah nama, semua",
                    "    tempat yang memakainya ikut berubah, dan cuma tempat-tempat itu.",
                    "  - Tipe jadi dokumentasi yang nggak bisa basi, karena compiler ikut",
                    "    memeriksanya.",
                    "",
                    "Memasang TypeScript lewat npm:",
                    "  npm install -g typescript          global",
                    "  npm install --save-dev typescript  per proyek (lebih baik)",
                    "  tsc --version",
                    "",
                    "Kalau dipasang per proyek, panggil compilernya lewat npx, misalnya",
                    "npx tsc --version.",
                    "",
                    "Menjalankan:",
                    "  tsc berkas.ts && node berkas.js     kompilasi, lalu jalankan hasilnya",
                    "  tsc --watch                         kompilasi ulang otomatis",
                    "  npx tsx berkas.ts                   jalankan langsung",
                    "  node --experimental-strip-types berkas.ts   Node 22.6 ke atas",
                    "",
                    "tsc --watch mengompilasi ulang setiap ada berkas yang berubah. Di Node",
                    "yang lebih baru, misalnya Node 24, opsi --experimental-strip-types",
                    "nggak perlu lagi: node berkas.ts langsung jalan.",
                    "",
                    "Jebakan: tsx dan node cuma membuang tipenya, tanpa memeriksanya. Kode",
                    "yang tipenya salah tetap dijalankan. Pemeriksa tipenya cuma tsc.",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """const nama: string = "Andi";
const umur: number = 20;
const aktif: boolean = true;

console.log(`Halo, ${nama}!`);
console.log(`Umurmu ${umur} tahun, status aktif: ${aktif}`);

function sapa(orang: string, salam: string = "Halo"): string {
  return `${salam}, ${orang}!`;
}

console.log(sapa("Budi"));
console.log(sapa("Cici", "Selamat pagi"));"""
            },
            {
                "heading": "Anotasi tipe, inferensi, dan strict",
                "body": [
                    "Bedanya dengan JavaScript cuma satu: ada anotasi tipe, yaitu keterangan",
                    "tipe yang ditulis sesudah tanda titik dua.",
                    "",
                    "  const nama: string = \"Andi\";",
                    "  function sapa(orang: string): string { ... }",
                    "",
                    "Kalau semua anotasinya dibuang, yang tersisa JavaScript yang sah. Itu",
                    "juga yang dikerjakan compiler waktu mengubah kodemu jadi JavaScript.",
                    "",
                    "Kamu nggak perlu menulis anotasi di semua tempat. TypeScript bisa",
                    "menyimpulkan tipe dari nilainya sendiri, dan kemampuan ini namanya",
                    "inferensi:",
                    "",
                    "  const nama = \"Andi\";      TypeScript tahu ini string",
                    "  const umur = 20;          tahu ini number",
                    "",
                    "Kebiasaan yang dipakai di kode TypeScript yang rapi:",
                    "  - Jangan tulis tipe kalau tipenya udah kelihatan dari nilainya.",
                    "  - Tulis tipe di batas: parameter fungsi, nilai yang dikembalikan",
                    "    fungsi yang dipakai bagian lain program, dan bentuk data yang",
                    "    datang dari luar.",
                    "",
                    "Menulis `const nama: string = \"Andi\"` nggak salah, cuma berlebihan. Dan",
                    "yang berlebihan itu ada ongkosnya: tiap anotasi harus ikut diperbarui",
                    "kalau kodenya berubah.",
                    "",
                    "Perilaku compiler diatur lewat berkas konfigurasi bernama",
                    "tsconfig.json. Dari semua setelannya, yang paling menentukan cuma satu:",
                    "",
                    "  { \"compilerOptions\": { \"strict\": true } }",
                    "",
                    "Tanpa strict, separuh manfaat TypeScript hilang. Nilai null (kosong)",
                    "diterima di mana aja, dan parameter yang nggak dikasih anotasi otomatis",
                    "jadi any tanpa kamu sadari. any adalah tipe yang mematikan pemeriksaan.",
                    "Nyalakan strict sejak berkas pertama. Aplikasi ini juga menjalankan",
                    "semua contoh TypeScript dengan strict menyala.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "TypeScript banyak dipakai di proyek web yang dikerjakan beberapa orang",
                    "sekaligus: halaman admin toko online, aplikasi kasir yang jalan di",
                    "browser, atau server Node. Editor VS Code sendiri ditulis dengan",
                    "TypeScript. Di tim seperti itu, tsc dijalankan sebelum kode digabung,",
                    "supaya salah pakai tipe ketahuan sebelum sampai ke pembeli.",
                    "",
                    "Kasus kecil: fungsi total menghitung tagihan dari harga, jumlah, dan",
                    "ongkir. Temanmu memanggilnya dengan ongkir yang diambil dari teks,",
                    "`total(15000, 3, \"10000\")`. JavaScript nggak protes, dan tagihannya",
                    "jadi 4500010000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukan dan keluarannya: tiga angka rupiah masuk, satu angka",
                    "     keluar. Tulis itu sebagai anotasi di parameter dan kembalian:",
                    "      function total(harga: number, jumlah: number, ongkir: number): number {",
                    "        return harga * jumlah + ongkir;",
                    "      }",
                    "  2. Jalankan tsc. Panggilan dengan \"10000\" langsung ditolak dengan pesan",
                    "     \"Argument of type 'string' is not assignable to parameter of type",
                    "     'number'\", lengkap dengan nomor barisnya.",
                    "  3. Betulkan pemanggilnya jadi `total(15000, 3, 10000)`. Hasilnya 55000.",
                    "  4. Periksa juga cara menjalankannya. Kalau kamu cuma memakai tsx atau",
                    "     node, panggilan yang salah tetap jalan dan mencetak 4500010000,",
                    "     karena keduanya membuang tipe tanpa memeriksanya.",
                    "",
                    "Ingat: anotasi nggak mengubah data. Kalau ongkir datang dari kotak isian,",
                    "isinya tetap teks, jadi ubah dulu dengan Number(...) sebelum dipakai.",
                ]
            },
        ],
    },
    {
        "title": "2. Tipe Dasar",
        "sections": [
            {
                "body": [
                    "Tipe primitif, yaitu tipe untuk nilai tunggal yang paling dasar,",
                    "semuanya ditulis huruf kecil:",
                    "  string   number   boolean",
                    "  bigint   symbol",
                    "  null     undefined",
                    "",
                    "Jebakan: String, Number, dan Boolean yang diawali huruf besar itu tipe",
                    "yang lain. Ketiganya tipe objek pembungkus, dan hampir nggak pernah",
                    "itu yang kamu maksud. Pakai yang huruf kecil.",
                    "",
                    "TypeScript cuma punya satu tipe angka, yaitu number. Isinya bilangan",
                    "pecahan 64-bit, dan dipakai juga untuk bilangan bulat. Nggak ada int,",
                    "long, atau float yang terpisah. Untuk bilangan bulat yang besar banget",
                    "ada bigint, yang ditulis dengan huruf n di belakang: 123n.",
                    "",
                    "Array, yaitu daftar nilai, bisa ditulis dengan dua cara. Hasilnya sama",
                    "persis:",
                    "  const a: number[] = [1, 2, 3];",
                    "  const a: Array<number> = [1, 2, 3];",
                    "",
                    "Tuple",
                    "",
                    "Tuple adalah array yang jumlah isinya tetap, dan tiap posisinya punya",
                    "tipe sendiri:",
                    "  const titik: [number, number] = [3, 4];",
                    "  const pasangan: [string, number] = [\"umur\", 20];",
                    "  const opsional: [string, number?] = [\"a\"];",
                    "  const sisanya: [string, ...number[]] = [\"a\", 1, 2];",
                    "",
                    "Tanda tanya di number? artinya posisi itu boleh kosong. ...number[]",
                    "artinya sisa isinya boleh berapa aja, asal semuanya number.",
                    "",
                    "Objek ditulis lewat bentuknya, yaitu nama tiap properti beserta",
                    "tipenya:",
                    "  const murid: { nama: string; nilai: number } = {",
                    "      nama: \"Andi\", nilai: 88,",
                    "  };",
                    "",
                    "Properti bisa dikasih penanda tambahan:",
                    "  nama?: string        opsional, boleh nggak ada",
                    "  readonly id: number  nggak bisa diubah sesudah objeknya dibuat",
                    "",
                    "Ada tiga tipe khusus yang wajib bisa kamu bedakan:",
                    "  - any mematikan pemeriksaan. Apa pun boleh masuk dan keluar. Anggap",
                    "    ini pintu darurat, bukan alat sehari-hari.",
                    "  - unknown artinya \"aku belum tahu tipenya\". Apa pun boleh masuk, tapi",
                    "    kamu nggak boleh melakukan apa-apa padanya sampai kamu",
                    "    memeriksanya.",
                    "  - never adalah tipe yang nggak punya nilai sama sekali. Dia dipakai",
                    "    sebagai tipe kembalian fungsi yang selalu melempar error, atau",
                    "    fungsi yang nggak pernah selesai.",
                    "",
                    "Untuk data yang datang dari luar, unknown hampir selalu lebih baik",
                    "daripada any. unknown memaksa kamu memeriksa datanya dulu sebelum",
                    "memakainya.",
                    "",
                    "Dua tipe lain yang juga sering muncul:",
                    "  void     fungsi yang nggak mengembalikan apa-apa",
                    "  object   apa pun yang bukan primitif; jarang berguna",
                ]
            },
            {
                "heading": "Tipe dasar dalam praktik",
                "code": """// Inferensi: tipenya disimpulkan, tidak perlu ditulis
const nama = "Andi";
const umur = 20;
const nilai = [78, 92, 65];

// Anotasi ditulis di BATAS: parameter dan kembalian
function rataRata(angka: number[]): number {
  if (angka.length === 0) return 0;
  return angka.reduce((a, b) => a + b, 0) / angka.length;
}

// Tuple: panjang dan tipe per posisi ditetapkan
const titik: [number, number] = [3, 4];
const [x, y] = titik;

// Objek dengan properti opsional dan readonly
type Murid = {
  readonly id: number;
  nama: string;
  nilai: number;
  catatan?: string;
};

const m: Murid = { id: 1, nama: "Andi", nilai: 88 };

// m.id = 2;            <- error: readonly
console.log(`nama   : ${nama}`);
console.log(`umur   : ${umur}`);
console.log(`nilai  : ${nilai.join(", ")}`);
console.log(`rata   : ${rataRata(nilai).toFixed(2)}`);
console.log(`titik  : (${x}, ${y})`);
console.log(`murid  : ${m.nama} ${m.nilai}`);
console.log(`catatan: ${m.catatan ?? "(tidak ada)"}`);

// unknown MEMAKSA pemeriksaan sebelum dipakai
function jelaskan(x: unknown): string {
  if (typeof x === "string") return `teks ${x.length} huruf`;
  if (typeof x === "number") return `angka ${x}`;
  if (typeof x === "boolean") return x ? "benar" : "salah";
  if (x === null) return "null";
  if (Array.isArray(x)) return `array ${x.length} elemen`;
  return `tipe lain: ${typeof x}`;
}

console.log("---");
for (const v of ["halo", 42, true, null, [1, 2], { a: 1 }]) {
  console.log(jelaskan(v));
}"""
            },
            {
                "heading": "Kenapa unknown lebih aman daripada any",
                "body": [
                    "Keluaran:",
                    "  nama   : Andi",
                    "  umur   : 20",
                    "  nilai  : 78, 92, 65",
                    "  rata   : 78.33",
                    "  titik  : (3, 4)",
                    "  murid  : Andi 88",
                    "  catatan: (tidak ada)",
                    "  ---",
                    "  teks 4 huruf",
                    "  angka 42",
                    "  benar",
                    "  null",
                    "  array 2 elemen",
                    "  tipe lain: object",
                    "",
                    "Fungsi jelaskan nunjukin kenapa unknown lebih aman daripada any. Kalau",
                    "parameternya any, `x.length` diterima begitu aja. Waktu x ternyata",
                    "angka, hasilnya undefined, dan program jalan terus dengan nilai yang",
                    "salah. Waktu x ternyata null, program berhenti dengan TypeError. Kalau",
                    "parameternya unknown, compiler menolak semua pemakaian x sampai kamu",
                    "mempersempit tipenya lebih dulu.",
                    "",
                    "Proses mempersempit tipe ini namanya narrowing. Alat yang bisa kamu",
                    "pakai:",
                    "  typeof x === \"string\"",
                    "  Array.isArray(x)",
                    "  x === null",
                    "  x instanceof Kelas",
                    "  \"nama\" in x",
                    "",
                    "Kenapa `x === null` ditulis terpisah? Soalnya `typeof null` hasilnya",
                    "\"object\". Ini bug JavaScript yang umurnya sekitar tiga puluh tahun.",
                    "Bug itu nggak pernah diperbaiki, karena terlalu banyak situs lama yang",
                    "bergantung pada perilaku itu.",
                    "",
                    "Operator ?? (nullish coalescing) ngasih nilai cadangan cuma kalau sisi",
                    "kirinya null atau undefined. Bedanya dengan || penting: `0 || 5`",
                    "hasilnya 5, sedangkan `0 ?? 5` hasilnya 0. Untuk angka, biasanya yang",
                    "kedua yang kamu maksud, karena 0 itu angka yang sah.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak data di aplikasi toko berupa objek dengan properti yang kadang",
                    "ada, kadang nggak: diskon, catatan untuk penjual, jumlah barang.",
                    "Tipe objek dengan tanda ? menuliskan hal itu terang-terangan, dan strict",
                    "memaksa setiap pemakai properti itu menangani kemungkinan kosongnya.",
                    "",
                    "Kasus kecil: keranjang belanja berisi Sabun 4500 tanpa jumlah (artinya",
                    "1), Susu 18000 sebanyak 2, dan Roti 12000 dengan jumlah 0 karena",
                    "dibatalkan pembeli. Totalnya harus 40500.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis bentuk satu barang, dengan jumlah sebagai properti opsional:",
                    "      type Barang = { nama: string; harga: number; jumlah?: number };",
                    "  2. Jumlahkan subtotal tiap barang dengan reduce, dan isi jumlah yang",
                    "     kosong dengan 1 lewat ??:",
                    "      const total = keranjang.reduce(",
                    "        (t, b) => t + b.harga * (b.jumlah ?? 1), 0);",
                    "  3. Periksa kasus pinggirnya, yaitu Roti dengan jumlah 0. Dengan ??,",
                    "     angka 0 tetap 0. Dengan ||, angka 0 dianggap kosong, Roti ikut",
                    "     terhitung sekali, dan totalnya jadi 52500.",
                    "  4. Coba hapus `?? 1`. Compiler menolak dengan pesan \"'b.jumlah' is",
                    "     possibly 'undefined'\". Itu strict yang bekerja: dia nggak",
                    "     membiarkan kamu lupa pada barang tanpa jumlah.",
                ]
            },
        ],
    },
    {
        "title": "3. Union, Literal & Narrowing",
        "sections": [
            {
                "body": [
                    "Union type artinya sebuah nilai boleh bertipe A atau B. Ini gagasan",
                    "yang paling khas dari TypeScript. Tanda | dibaca \"atau\":",
                    "",
                    "  let id: string | number;",
                    "  let mungkin: string | null;",
                    "  let hasil: Sukses | Gagal;",
                    "",
                    "Selama sebuah nilai masih berupa union, kamu cuma boleh memakai",
                    "properti dan method yang dimiliki semua anggotanya. Misalnya, pada",
                    "nilai bertipe `string | number` kamu boleh memanggil toString(), karena",
                    "string dan number sama-sama punya method itu. Properti length cuma",
                    "dimiliki string, jadi nilainya harus dipersempit dulu.",
                    "",
                    "Literal type adalah tipe yang isinya cuma satu nilai tertentu:",
                    "",
                    "  let arah: \"utara\" | \"timur\" | \"selatan\" | \"barat\";",
                    "  let kode: 200 | 404 | 500;",
                    "  let saklar: true;",
                    "",
                    "Variabel arah di atas cuma boleh diisi salah satu dari empat teks itu.",
                    "\"utara\" boleh, \"Utara\" atau \"barat daya\" ditolak.",
                    "",
                    "Union dari literal seperti ini bisa menggantikan enum di kebanyakan",
                    "kasus, dan lebih ringan. Union literal hilang seluruhnya waktu",
                    "kompilasi, sedangkan enum menghasilkan objek sungguhan di JavaScript.",
                    "Enum dibahas di materi Enum, const & Readonly.",
                    "",
                    "Cara mempersempit union (narrowing):",
                    "",
                    "  typeof x === \"string\"        untuk primitif",
                    "  Array.isArray(x)             untuk array",
                    "  x === null / x == null       null dan undefined",
                    "  x instanceof Kelas           untuk class",
                    "  \"nama\" in x                  untuk properti",
                    "  x.jenis === \"lingkaran\"      discriminated union",
                    "",
                    "`x == null`, dengan dua tanda sama dengan, menangkap null dan undefined",
                    "sekaligus.",
                    "",
                    "Discriminated union",
                    "",
                    "Pola paling penting di daftar itu adalah discriminated union. Kalau",
                    "kamu pernah belajar Kotlin atau Rust, pola ini setara sealed class di",
                    "Kotlin atau enum yang membawa data di Rust:",
                    "",
                    "  type Bentuk =",
                    "      | { jenis: \"lingkaran\"; jari: number }",
                    "      | { jenis: \"persegi\"; sisi: number };",
                    "",
                    "Semua anggotanya punya properti jenis dengan nama yang sama. Properti",
                    "itu disebut diskriminan, yaitu penanda yang membedakan anggota yang",
                    "satu dengan yang lain. Begitu kamu ngecek nilainya, tipenya otomatis",
                    "menyempit, dan compiler tahu properti apa aja yang tersedia di tiap",
                    "cabang.",
                    "",
                    "Exhaustiveness check, atau pemeriksaan kelengkapan, memastikan nggak",
                    "ada cabang yang terlewat:",
                    "",
                    "  default: {",
                    "      const _lengkap: never = bentuk;",
                    "      throw new Error(`belum ditangani: ${_lengkap}`);",
                    "  }",
                    "",
                    "Kalau suatu hari union-nya dapat anggota baru, baris itu gagal",
                    "dikompilasi. Compiler langsung nunjukin tempat yang perlu diperbarui.",
                ]
            },
            {
                "heading": "Discriminated union dan exhaustiveness",
                "code": """type Bentuk =
  | { jenis: "lingkaran"; jari: number }
  | { jenis: "persegi"; sisi: number }
  | { jenis: "persegiPanjang"; panjang: number; lebar: number };

const PI = 3.14159;

function luas(b: Bentuk): number {
  switch (b.jenis) {
    case "lingkaran":
      return PI * b.jari * b.jari;      // b.jari tersedia di sini
    case "persegi":
      return b.sisi * b.sisi;
    case "persegiPanjang":
      return b.panjang * b.lebar;
    default: {
      // Kalau ada anggota union BARU, baris ini gagal dikompilasi
      const _lengkap: never = b;
      throw new Error(`bentuk belum ditangani: ${JSON.stringify(_lengkap)}`);
    }
  }
}

function nama(b: Bentuk): string {
  return b.jenis === "persegiPanjang" ? "PersegiPanjang"
    : b.jenis.charAt(0).toUpperCase() + b.jenis.slice(1);
}

// Union dengan literal type
type Taraf = "info" | "peringatan" | "galat";

function warna(t: Taraf): string {
  const peta: Record<Taraf, string> = {
    info: "biru",
    peringatan: "kuning",
    galat: "merah",
  };
  return peta[t];
}

const semua: Bentuk[] = [
  { jenis: "persegi", sisi: 4 },
  { jenis: "lingkaran", jari: 3 },
  { jenis: "persegiPanjang", panjang: 6, lebar: 3 },
];

for (const b of semua) {
  console.log(`${nama(b).padEnd(16)}${luas(b).toFixed(2).padStart(8)}`);
}
const total = semua.reduce((t, b) => t + luas(b), 0);
console.log(`${"TOTAL".padEnd(16)}${total.toFixed(2).padStart(8)}`);

console.log("---");
const taraf: Taraf[] = ["info", "peringatan", "galat"];
for (const t of taraf) {
  console.log(`${t.padEnd(12)}${warna(t)}`);
}

console.log("---");
// Narrowing pada union primitif
function panjangnya(x: string | number | null): number {
  if (x === null) return 0;
  if (typeof x === "number") return String(x).length;
  return x.length;
}
for (const v of ["halo", 12345, null]) {
  console.log(`${JSON.stringify(v).padEnd(8)}-> ${panjangnya(v)}`);
}"""
            },
            {
                "heading": "Pemeriksaan never, Record, dan pilihan enum",
                "body": [
                    "Keluaran:",
                    "  Persegi            16.00",
                    "  Lingkaran          28.27",
                    "  PersegiPanjang     18.00",
                    "  TOTAL              62.27",
                    "  ---",
                    "  info        biru",
                    "  peringatan  kuning",
                    "  galat       merah",
                    "  ---",
                    "  \"halo\"  -> 4",
                    "  12345   -> 5",
                    "  null    -> 0",
                    "",
                    "Di dalam `case \"lingkaran\"`, TypeScript tahu b punya properti jari dan",
                    "nggak punya sisi. Kalau kamu menulis b.sisi di situ, kompilasinya",
                    "gagal. Coba bandingkan dengan bentuk yang ditulis sebagai satu objek",
                    "berisi banyak properti opsional: di sana compiler nggak tahu properti",
                    "mana yang datang berpasangan. Karena itu discriminated union jauh",
                    "lebih aman.",
                    "",
                    "Blok default dengan `const _lengkap: never = b;` layak kamu hafal.",
                    "Cara kerjanya begini. Kalau semua cabang udah ditangani, tipe b di",
                    "titik itu menyempit jadi never, dan nilai never boleh diisikan ke",
                    "variabel bertipe never. Begitu ada anggota baru yang belum ditangani,",
                    "tipe b di situ bukan never lagi, dan pengisiannya ditolak.",
                    "",
                    "`Record<Taraf, string>` menuntut semua anggota union punya entri.",
                    "Kalau satu lupa ditulis, kompilasinya gagal. Ini cara lain untuk dapat",
                    "kelengkapan yang diperiksa compiler.",
                    "",
                    "Kapan pakai union literal, kapan enum:",
                    "  - Union literal: hampir selalu. Dia hilang waktu kompilasi dan",
                    "    langsung cocok dengan string dari JSON.",
                    "  - enum: kalau kamu butuh nilainya tetap ada waktu program jalan, atau",
                    "    butuh penomoran otomatis.",
                    "  - const enum: hindari. Fitur ini bermasalah dengan bundler (alat yang",
                    "    menggabungkan banyak berkas jadi satu) dan dengan setelan",
                    "    isolatedModules.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Status pesanan di aplikasi ojek online atau toko online biasanya ditulis",
                    "sebagai union literal, misalnya \"menunggu\" | \"diantar\" | \"selesai\". Teks",
                    "itu datang apa adanya dari JSON server. Discriminated union muncul kalau",
                    "tiap jenis membawa data yang beda, seperti cara bayar di mesin kasir.",
                    "",
                    "Kasus kecil: kasir menerima tunai, kartu debit, atau dompet digital.",
                    "Untuk belanja 47500 yang dibayar tunai 50000, struk harus mencetak",
                    "\"Tunai 50000, kembali 2500\". Untuk debit, struk mencetak empat angka",
                    "terakhir kartunya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukannya: data tiap cara bayar beda, jadi tulis satu union",
                    "     dengan diskriminan cara:",
                    "      type Bayar =",
                    "        | { cara: \"tunai\"; diterima: number }",
                    "        | { cara: \"debit\"; akhirKartu: string }",
                    "        | { cara: \"dompet\"; aplikasi: string };",
                    "  2. Tulis `switch (b.cara)`. Di cabang \"tunai\", compiler tahu",
                    "     b.diterima ada, jadi kembaliannya cukup `b.diterima - total`.",
                    "  3. Tutup switch dengan default berisi `const _lengkap: never = b`.",
                    "     Kalau tahun depan ada cara bayar keempat, compiler langsung",
                    "     nunjukin fungsi struk yang belum menanganinya.",
                    "  4. Periksa kasus pinggir: uang tunai 45000 untuk belanja 47500.",
                    "     Tentukan sejak awal apa yang dicetak, misalnya \"Uang kurang 2500\",",
                    "     supaya struk nggak pernah menulis kembalian minus.",
                ]
            },
        ],
    },
    {
        "title": "4. Interface & Type Alias",
        "sections": [
            {
                "body": [
                    "Ada dua cara menamai bentuk sebuah objek, dan hasilnya hampir sama:",
                    "",
                    "  interface Murid {",
                    "      nama: string;",
                    "      nilai: number;",
                    "  }",
                    "",
                    "  type Murid = {",
                    "      nama: string;",
                    "      nilai: number;",
                    "  };",
                    "",
                    "Bedanya yang terasa cuma dua:",
                    "  - interface bisa digabung. Dua deklarasi interface dengan nama yang",
                    "    sama otomatis menyatu jadi satu. Fitur ini yang bikin pustaka bisa",
                    "    menambah isi tipe bawaan.",
                    "  - type bisa menamai apa aja: union, tuple, tipe primitif, dan tipe",
                    "    yang dihitung dari tipe lain. interface nggak bisa.",
                    "",
                    "Kebiasaan yang dipakai banyak proyek:",
                    "  - interface untuk bentuk objek, dan untuk kontrak (daftar kemampuan",
                    "    yang wajib dipenuhi) yang mungkin diperluas.",
                    "  - type untuk union, tuple, dan apa pun yang bukan objek biasa.",
                    "  - Jangan habiskan waktu memperdebatkannya. Yang penting konsisten di",
                    "    dalam satu proyek.",
                    "",
                    "Memperluas sebuah bentuk:",
                    "  interface Guru extends Murid { mapel: string }",
                    "  type Guru = Murid & { mapel: string };",
                    "",
                    "Tanda & disebut intersection. Hasilnya punya semua properti dari kedua",
                    "sisi sekaligus.",
                    "",
                    "Interface juga bisa menggambarkan fungsi dan objek berindeks:",
                    "",
                    "  interface Pembanding {",
                    "      (a: number, b: number): number;    dipanggil",
                    "  }",
                    "",
                    "  interface Kamus {",
                    "      [kunci: string]: number;           index signature",
                    "  }",
                    "",
                    "Pembanding adalah bentuk fungsi yang menerima dua number dan",
                    "mengembalikan number. Kamus adalah objek yang kuncinya boleh teks apa",
                    "aja, asal nilainya number. Penulisan [kunci: string] itu namanya index",
                    "signature.",
                    "",
                    "Jebakan: objek literal, yaitu objek yang ditulis langsung dengan kurung",
                    "kurawal, ditolak kalau punya properti tambahan. Objek yang sama lolos",
                    "kalau lewat variabel dulu. Pemeriksaan ini namanya excess property",
                    "check:",
                    "",
                    "  const m: Murid = { nama: \"a\", nilai: 1, x: 2 };  ERROR",
                    "  const t = { nama: \"a\", nilai: 1, x: 2 };",
                    "  const m: Murid = t;                             lolos",
                    "",
                    "Ini disengaja. Pemeriksaan ketat pada objek literal menangkap salah",
                    "ketik nama properti. Di tempat lain berlaku aturan kecocokan bentuk",
                    "yang lebih longgar: sebuah objek dianggap cocok selama dia punya semua",
                    "properti yang diminta.",
                ]
            },
            {
                "heading": "Interface, type, dan kecocokan bentuk",
                "code": """interface Murid {
  readonly id: number;
  nama: string;
  nilai: number;
}

interface Guru extends Murid {
  mapel: string;
}

// type bisa menamai apa pun, termasuk union dan fungsi
type Peran = "murid" | "guru";
type Pembanding<T> = (a: T, b: T) => number;
type Orang = Murid | Guru;

// Type guard buatan sendiri: `x is Guru` adalah PREDIKAT TIPE
function adalahGuru(o: Orang): o is Guru {
  return "mapel" in o;
}

function ringkas(o: Orang): string {
  const peran: Peran = adalahGuru(o) ? "guru" : "murid";
  const tambahan = adalahGuru(o) ? ` (${o.mapel})` : "";
  return `${o.nama.padEnd(8)}${peran.padEnd(7)}${String(o.nilai).padStart(3)}${tambahan}`;
}

const urutNilai: Pembanding<Orang> = (a, b) => b.nilai - a.nilai;

const semua: Orang[] = [
  { id: 1, nama: "Andi", nilai: 88 },
  { id: 2, nama: "Budi", nilai: 72, mapel: "Matematika" },
  { id: 3, nama: "Cici", nilai: 95 },
];

semua.sort(urutNilai).forEach((o) => console.log(ringkas(o)));

console.log("---");

// Index signature: objek yang kuncinya bebas
interface Frekuensi {
  [kata: string]: number;
}

const hitung: Frekuensi = {};
for (const k of "kucing makan ikan kucing tidur ikan kucing".split(" ")) {
  hitung[k] = (hitung[k] ?? 0) + 1;
}

Object.entries(hitung)
  .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
  .forEach(([k, n]) => console.log(`${k.padEnd(7)}: ${n}`));

console.log("---");

// Intersection: menggabungkan dua bentuk
type Berwaktu = { dibuat: string };
type MuridBerwaktu = Murid & Berwaktu;

const mw: MuridBerwaktu = {
  id: 4,
  nama: "Dedi",
  nilai: 64,
  dibuat: "2026-09-22",
};
console.log(`${mw.nama} dibuat ${mw.dibuat}`);"""
            },
            {
                "heading": "Predikat tipe dan index signature",
                "body": [
                    "Keluaran:",
                    "  Cici    murid   95",
                    "  Andi    murid   88",
                    "  Budi    guru    72 (Matematika)",
                    "  ---",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "  ---",
                    "  Dedi dibuat 2026-09-22",
                    "",
                    "`function adalahGuru(o: Orang): o is Guru` memakai predikat tipe. Tipe",
                    "kembaliannya ditulis `o is Guru`, dan artinya buat compiler: \"kalau",
                    "fungsi ini mengembalikan true, anggap o sebagai Guru mulai dari titik",
                    "itu\". Waktu dijalankan, fungsinya tetap cuma mengembalikan true atau",
                    "false.",
                    "",
                    "Tanpa predikat tipe, adalahGuru(o) cuma mengembalikan boolean biasa,",
                    "dan o.mapel sesudahnya tetap ditolak compiler.",
                    "",
                    "Hati-hati: predikat tipe adalah janji yang nggak diperiksa. Kalau",
                    "isinya salah, misalnya selalu mengembalikan true, compiler tetap",
                    "percaya, dan semua jaminannya hilang. Tulis isinya dengan teliti.",
                    "",
                    "`b[1] - a[1] || a[0].localeCompare(b[0])` adalah cara mengurutkan",
                    "dengan dua patokan di JavaScript. Kalau selisih jumlahnya nol, nol itu",
                    "dianggap false (falsy), jadi operator || pindah ke patokan kedua, yaitu",
                    "urutan abjad.",
                    "",
                    "Soal index signature: kalau setelan noUncheckedIndexedAccess",
                    "dinyalakan, `hitung[k]` bertipe `number | undefined`. Itu lebih jujur,",
                    "karena kuncinya memang belum tentu ada. Setelan ini nggak termasuk",
                    "strict, jadi perlu dinyalakan sendiri.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di toko online, bentuk data produk ditulis sekali sebagai interface,",
                    "lalu dipakai halaman daftar produk, keranjang, dan laporan. Produk yang punya",
                    "data tambahan, misalnya pulsa yang butuh nomor tujuan, ditulis dengan",
                    "extends supaya bagian yang sama nggak diketik ulang.",
                    "",
                    "Kasus kecil: keranjang berisi Beras 5 kg seharga 72000 dan Pulsa 25 ribu",
                    "seharga 26500 untuk nomor 081234567890. Halaman keranjang harus",
                    "menampilkan nomor tujuan, tapi cuma untuk produk digital.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari bagian yang sama dan yang beda. Semua produk punya kode, nama,",
                    "     dan harga, sedangkan produk digital menambah tujuan:",
                    "      interface Produk { kode: string; nama: string; harga: number }",
                    "      interface ProdukDigital extends Produk { tujuan: string }",
                    "  2. Tulis type guard untuk membedakan keduanya waktu keranjang dibaca:",
                    "      function digital(p: Produk): p is ProdukDigital {",
                    "        return \"tujuan\" in p;",
                    "      }",
                    "  3. Beri keranjang tipe `(Produk | ProdukDigital)[]`, lalu di perulangan",
                    "     cetak p.tujuan cuma kalau digital(p) bernilai true. Hasilnya dua",
                    "     baris, dan cuma baris pulsa yang memuat nomor.",
                    "  4. Periksa salah ketik. `tujaun: \"081234567890\"` di objek literal",
                    "     langsung ditolak excess property check. Kalau objeknya lewat",
                    "     variabel dulu, salah ketik itu lolos, dan pulsanya tampil sebagai",
                    "     produk biasa tanpa nomor.",
                ]
            },
        ],
    },
    {
        "title": "5. Fungsi & Tipe Fungsi",
        "sections": [
            {
                "body": [
                    "Fungsi bisa ditulis dengan tiga bentuk:",
                    "",
                    "  function tambah(a: number, b: number): number {",
                    "      return a + b;",
                    "  }",
                    "",
                    "  const tambah = (a: number, b: number): number => a + b;",
                    "",
                    "  const tambah: (a: number, b: number) => number =",
                    "      (a, b) => a + b;",
                    "",
                    "Bentuk ketiga nunjukin tipe fungsi: `(a: A, b: B) => C`. Perhatikan",
                    "panahnya. Di posisi tipe, panah artinya \"mengembalikan\", dan itu bukan",
                    "arrow function.",
                    "",
                    "Macam-macam parameter:",
                    "  a: number            wajib",
                    "  b?: number           opsional, tipenya number | undefined",
                    "  c: number = 10       punya nilai bawaan, otomatis opsional",
                    "  ...sisa: number[]    rest: menampung sisa argumen, harus terakhir",
                    "",
                    "Parameter opsional harus ditulis sesudah parameter yang wajib.",
                    "",
                    "Tipe kembalian, yaitu tipe nilai yang dikembalikan fungsi, biasanya",
                    "bisa disimpulkan sendiri oleh TypeScript. Tapi untuk fungsi yang",
                    "dipakai bagian lain program, menuliskannya ada gunanya. Kesalahan di",
                    "dalam fungsi ketahuan di fungsi itu sendiri, nggak nyasar ke tempat",
                    "fungsinya dipanggil, dan pesan errornya jauh lebih jelas.",
                    "",
                    "Dua tipe kembalian khusus:",
                    "  void    tidak mengembalikan apa-apa",
                    "  never   tidak pernah selesai dengan normal (selalu melempar error,",
                    "          atau perulangannya nggak pernah berhenti)",
                    "",
                    "Overload",
                    "",
                    "Overload artinya satu fungsi punya beberapa tanda tangan, yaitu",
                    "beberapa cara memanggil dengan tipe yang beda-beda, tapi isinya cuma",
                    "satu:",
                    "",
                    "  function cari(id: number): Murid | undefined;",
                    "  function cari(nama: string): Murid[] ;",
                    "  function cari(x: number | string): unknown { ... }",
                    "",
                    "Kalau dipanggil dengan angka, hasilnya satu Murid atau undefined. Kalau",
                    "dipanggil dengan teks, hasilnya array Murid. Tanda tangan di baris",
                    "ketiga milik isi fungsinya, dan dia nggak kelihatan dari luar.",
                    "",
                    "Dalam praktik, union sering lebih sederhana daripada overload. Pakai",
                    "overload cuma kalau tipe kembaliannya memang bergantung pada tipe",
                    "masukannya.",
                    "",
                    "Tipe this di dalam fungsi bisa ditentukan lewat parameter pertama yang",
                    "bernama this. Parameter ini cuma pura-pura, dan dihapus waktu",
                    "kompilasi:",
                    "  function f(this: HTMLElement, x: number) { ... }",
                    "",
                    "Arrow function nggak punya this sendiri. Dia memakai this dari tempat",
                    "dia ditulis. Karena itu arrow function jauh lebih aman dipakai sebagai",
                    "callback, yaitu fungsi yang kamu titipkan untuk dipanggil belakangan.",
                ]
            },
            {
                "heading": "Semua bentuk fungsi",
                "code": """// Tipe fungsi sebagai alias
type Syarat<T> = (x: T) => boolean;
type Ubah<T, U> = (x: T) => U;

// Parameter opsional, bawaan, dan rest
function garis(isi: string, lebar = 30, pengisi = "-"): string {
  const sisa = Math.max(lebar - isi.length, 0);
  const kiri = Math.floor(sisa / 2);
  return pengisi.repeat(kiri) + isi + pengisi.repeat(sisa - kiri);
}

function total(...angka: number[]): number {
  return angka.reduce((a, b) => a + b, 0);
}

// Higher-order: menerima fungsi
function saring<T>(data: T[], syarat: Syarat<T>): T[] {
  return data.filter(syarat);
}

// Higher-order: MENGEMBALIKAN fungsi
function pengali(faktor: number): Ubah<number, number> {
  return (x) => x * faktor;
}

// never: fungsi yang tidak pernah kembali normal
function gagal(pesan: string): never {
  throw new Error(pesan);
}

const angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log(garis(" REKAP "));
console.log(garis(" KECIL ", 20));
console.log(garis(" TEBAL ", 30, "="));

console.log("---");
console.log(`total()        = ${total()}`);
console.log(`total(1,2,3)   = ${total(1, 2, 3)}`);
console.log(`total(...arr)  = ${total(...angka)}`);

console.log("---");
console.log(`genap  : ${saring(angka, (n) => n % 2 === 0).join(", ")}`);
console.log(`> 7    : ${saring(angka, (n) => n > 7).join(", ")}`);
console.log(`kali 3 : ${angka.map(pengali(3)).join(", ")}`);

console.log("---");
// Fungsi disimpan di dalam objek
const operasi: Record<string, (a: number, b: number) => number> = {
  tambah: (a, b) => a + b,
  kurang: (a, b) => a - b,
  kali: (a, b) => a * b,
};

for (const [nama, fn] of Object.entries(operasi)) {
  console.log(`${nama.padEnd(7)}(9, 4) = ${fn(9, 4)}`);
}

console.log("---");
try {
  gagal("sengaja gagal");
} catch (e) {
  console.log(`tertangkap: ${e instanceof Error ? e.message : String(e)}`);
}"""
            },
            {
                "heading": "Variabel catch bertipe unknown dan never",
                "body": [
                    "Keluaran:",
                    "  ----------- REKAP ------------",
                    "  ------ KECIL -------",
                    "  =========== TEBAL ============",
                    "  ---",
                    "  total()        = 0",
                    "  total(1,2,3)   = 6",
                    "  total(...arr)  = 55",
                    "  ---",
                    "  genap  : 2, 4, 6, 8, 10",
                    "  > 7    : 8, 9, 10",
                    "  kali 3 : 3, 6, 9, 12, 15, 18, 21, 24, 27, 30",
                    "  ---",
                    "  tambah (9, 4) = 13",
                    "  kurang (9, 4) = 5",
                    "  kali   (9, 4) = 36",
                    "  ---",
                    "  tertangkap: sengaja gagal",
                    "",
                    "Bagian paling penting dari contoh itu ada di blok terakhir:",
                    "",
                    "  catch (e) {",
                    "      e instanceof Error ? e.message : String(e)",
                    "  }",
                    "",
                    "Di TypeScript modern, variabel e di dalam catch bertipe unknown. Tipe",
                    "Error nggak dijamin, dan alasannya masuk akal: di JavaScript, throw",
                    "boleh melempar apa aja, termasuk angka, string, atau objek biasa. Jadi",
                    "belum tentu yang tertangkap punya properti message.",
                    "",
                    "Karena itu tiap blok catch di TypeScript yang ketat harus ngecek dulu",
                    "sebelum membaca pesannya. Awalnya terasa merepotkan, tapi kebiasaan ini",
                    "menangkap jenis bug yang nyata.",
                    "",
                    "Perilaku ini diatur setelan useUnknownInCatchVariables, yang udah",
                    "termasuk di dalam strict.",
                    "",
                    "Tipe kembalian never pada fungsi gagal ternyata juga berguna. Fungsi",
                    "itu nggak pernah kembali, jadi compiler tahu kode sesudah",
                    "pemanggilannya nggak akan pernah dijalankan. Hasilnya, x di",
                    "`const x = a ?? gagal(...)` dijamin nggak null atau undefined, tanpa",
                    "perlu memaksa tipenya dengan as.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Promo di toko online sering berganti tiap minggu: potongan 10 persen,",
                    "potongan tetap 5000, dan seterusnya. Tim biasanya menyimpan tiap aturan",
                    "promo sebagai fungsi dengan tipe yang sama, sehingga kode kasir cukup",
                    "memanggil promo yang dipilih tanpa tahu isinya.",
                    "",
                    "Kasus kecil: total belanja 42000. Dengan promo persen10 hasilnya harus",
                    "37800, dengan potong5rb hasilnya 37000, dan tanpa promo tetap 42000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami bentuknya: setiap promo menerima total dan mengembalikan",
                    "     total baru. Tulis itu sebagai satu tipe fungsi:",
                    "      type Promo = (total: number) => number;",
                    "  2. Kumpulkan promonya di objek, seperti tabel operasi di contoh materi:",
                    "      const promo: Record<string, Promo> = {",
                    "        persen10: (t) => t * 0.9,",
                    "        potong5rb: (t) => Math.max(t - 5000, 0),",
                    "      };",
                    "  3. Tulis `bayar(total: number, namaPromo?: string)`. Kalau namaPromo",
                    "     kosong atau nggak ada di tabel, kembalikan total apa adanya.",
                    "  4. Periksa kasus pinggir: belanja 3000 dengan potong5rb. Tanpa",
                    "     Math.max hasilnya -2000, artinya kasir malah harus membayar",
                    "     pembeli. Dengan Math.max hasilnya 0.",
                    "",
                    "Jebakan: `t * 0.9` menghasilkan pecahan kalau totalnya bukan kelipatan",
                    "10, misalnya 33333 jadi 29999.7. Bulatkan dulu dengan Math.round sebelum",
                    "ditulis di struk.",
                ]
            },
        ],
    },
    {
        "title": "6. Generic",
        "sections": [
            {
                "body": [
                    "Generic bikin satu potong kode bisa dipakai untuk banyak tipe, tanpa",
                    "kehilangan informasi tipenya. Huruf T di contoh ini adalah parameter",
                    "tipe, semacam variabel yang isinya tipe:",
                    "",
                    "  function pertama<T>(daftar: T[]): T | undefined {",
                    "      return daftar[0];",
                    "  }",
                    "",
                    "  pertama([1, 2, 3])        -> number | undefined",
                    "  pertama([\"a\", \"b\"])       -> string | undefined",
                    "",
                    "Waktu dipanggil dengan array angka, T jadi number. Waktu dipanggil",
                    "dengan array teks, T jadi string. Bandingkan dengan versi any: dia juga",
                    "menerima apa aja, tapi hasilnya ikut jadi any, dan semua informasi",
                    "tipenya hilang sejak titik itu.",
                    "",
                    "Batasan dengan extends",
                    "",
                    "Kadang T nggak boleh sembarang tipe. Dengan extends, kamu bisa minta T",
                    "punya bentuk tertentu:",
                    "",
                    "  function panjang<T extends { length: number }>(x: T) {",
                    "      return x.length;",
                    "  }",
                    "",
                    "  panjang(\"halo\")      boleh",
                    "  panjang([1, 2])      boleh",
                    "  panjang(42)          ERROR: number tidak punya length",
                    "",
                    "keyof menghasilkan union dari nama-nama properti sebuah tipe:",
                    "",
                    "  type Kunci = keyof Murid;    \"nama\" | \"nilai\"",
                    "",
                    "  function ambil<T, K extends keyof T>(o: T, k: K): T[K] {",
                    "      return o[k];",
                    "  }",
                    "",
                    "  ambil(murid, \"nama\")    -> string, bukan any",
                    "  ambil(murid, \"xyz\")     -> error saat kompilasi",
                    "",
                    "T[K] artinya \"tipe properti K di dalam T\". Jadi tipe hasil ambil",
                    "ditentukan oleh nama properti yang kamu tulis waktu memanggilnya.",
                    "JavaScript biasa, yang nggak punya pemeriksaan tipe, nggak bisa ngasih",
                    "jaminan seperti ini sebelum programnya jalan.",
                    "",
                    "Utility type bawaan yang paling sering dipakai:",
                    "  Partial<T>        semua properti jadi opsional",
                    "  Required<T>       semua jadi wajib",
                    "  Readonly<T>       semua jadi readonly",
                    "  Pick<T, K>        ambil sebagian properti",
                    "  Omit<T, K>        buang sebagian properti",
                    "  Record<K, V>      objek berkunci K bernilai V",
                    "  Exclude<T, U>     buang anggota union",
                    "  Extract<T, U>     ambil anggota union",
                    "  NonNullable<T>    buang null dan undefined",
                    "  ReturnType<F>     tipe kembalian sebuah fungsi",
                    "  Parameters<F>     tuple parameter sebuah fungsi",
                    "  Awaited<P>        tipe di dalam sebuah Promise",
                    "",
                    "Semua utility type itu ditulis memakai fitur yang juga bisa kamu pakai",
                    "sendiri, yaitu mapped type dan conditional type. Keduanya dibahas di",
                    "materi Tipe Lanjut.",
                ]
            },
            {
                "heading": "Generic dan utility type",
                "code": """interface Murid {
  id: number;
  nama: string;
  nilai: number;
  catatan?: string;
}

// Generic dengan batasan keyof: tipe hasilnya bergantung argumennya
function ambil<T, K extends keyof T>(o: T, k: K): T[K] {
  return o[k];
}

// Generic dengan batasan bentuk
function terpanjang<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}

// Kelas generic
class Kotak<T> {
  private isi: T[] = [];

  constructor(private muat: number) {}

  get jumlah(): number {
    return this.isi.length;
  }

  masuk(x: T): boolean {
    if (this.isi.length >= this.muat) return false;
    this.isi.push(x);
    return true;
  }

  keluar(): T | undefined {
    return this.isi.shift();
  }

  toString(): string {
    return `[${this.isi.join(", ")}] ${this.jumlah}/${this.muat}`;
  }
}

const m: Murid = { id: 1, nama: "Andi", nilai: 88 };

console.log(`ambil nama : ${ambil(m, "nama")}`);
console.log(`ambil nilai: ${ambil(m, "nilai")}`);
// ambil(m, "xyz");            <- error saat kompilasi

console.log("---");
console.log(`terpanjang teks : ${terpanjang("pendek", "jauh lebih panjang")}`);
console.log(`terpanjang array: ${terpanjang([1, 2], [1, 2, 3]).join(",")}`);

console.log("---");
const angka = new Kotak<number>(3);
for (const n of [10, 20, 30, 40]) {
  console.log(`masuk ${n}: ${angka.masuk(n)}`);
}
console.log(String(angka));
console.log(`keluar: ${angka.keluar()}`);
console.log(String(angka));

console.log("---");
// Utility type
type MuridBaru = Omit<Murid, "id">;
type TambalMurid = Partial<Murid>;
type RingkasMurid = Pick<Murid, "nama" | "nilai">;

const baru: MuridBaru = { nama: "Budi", nilai: 72 };
const tambal: TambalMurid = { nilai: 75 };
const ringkas: RingkasMurid = { nama: "Cici", nilai: 95 };

function terapkan(asal: Murid, tambalan: TambalMurid): Murid {
  return { ...asal, ...tambalan };
}

console.log(`baru   : ${JSON.stringify(baru)}`);
console.log(`ringkas: ${JSON.stringify(ringkas)}`);
console.log(`tambal : ${JSON.stringify(terapkan(m, tambal))}`);"""
            },
            {
                "heading": "Hasil generic, spread, dan salinan dangkal",
                "body": [
                    "Keluaran:",
                    "  ambil nama : Andi",
                    "  ambil nilai: 88",
                    "  ---",
                    "  terpanjang teks : jauh lebih panjang",
                    "  terpanjang array: 1,2,3",
                    "  ---",
                    "  masuk 10: true",
                    "  masuk 20: true",
                    "  masuk 30: true",
                    "  masuk 40: false",
                    "  [10, 20, 30] 3/3",
                    "  keluar: 10",
                    "  [20, 30] 2/3",
                    "  ---",
                    "  baru   : {\"nama\":\"Budi\",\"nilai\":72}",
                    "  ringkas: {\"nama\":\"Cici\",\"nilai\":95}",
                    "  tambal : {\"id\":1,\"nama\":\"Andi\",\"nilai\":75}",
                    "",
                    "`ambil(m, \"nama\")` mengembalikan string, sedangkan `ambil(m, \"nilai\")`",
                    "mengembalikan number. Dua-duanya dari satu fungsi yang sama. Yang",
                    "menentukan tipenya adalah teks yang kamu tulis waktu memanggil.",
                    "",
                    "Fungsi seperti ini ada di mana-mana di kode nyata: pengambil nilai",
                    "konfigurasi, pembangun query database, dan pengurut berdasarkan nama",
                    "kolom. Tanpa generic, semuanya bakal mengembalikan any.",
                    "",
                    "`{ ...asal, ...tambalan }` disebut spread. Semua properti disalin, dan",
                    "properti yang ditulis belakangan menimpa yang di depan. Ini cara yang",
                    "lazim di JavaScript untuk bikin salinan objek sekaligus mengubah",
                    "sebagian isinya. Di Kotlin padanannya copy(), di C# padanannya with.",
                    "",
                    "Hasil spread adalah salinan dangkal. Properti yang isinya objek nggak",
                    "ikut digandakan, jadi salinan dan aslinya tetap menunjuk objek yang",
                    "sama. Untuk salinan dalam, pakai structuredClone(x), yang tersedia di",
                    "Node 17 ke atas dan di browser modern.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Fungsi pembantu di aplikasi sungguhan sering dipakai untuk banyak jenis",
                    "data: mengambil satu kolom dari daftar pelanggan, daftar pesanan, atau",
                    "daftar produk. Dengan generic dan keyof, satu fungsi itu tetap tahu tipe",
                    "hasilnya, dan nama kolom yang salah ketik ditolak sebelum program jalan.",
                    "",
                    "Kasus kecil: data pelanggan berisi Sari (1200 poin), Dodi (300 poin),",
                    "dan Rina (4500 poin), masing-masing dengan email. Bagian pemasaran minta",
                    "daftar email, bagian keuangan minta total poin, yaitu 6000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukan dan keluarannya: daftar objek dan satu nama kolom",
                    "     masuk, daftar isi kolom itu keluar. Tipe hasilnya harus ikut",
                    "     kolomnya, string[] untuk email dan number[] untuk poin.",
                    "  2. Pakai `K extends keyof T` supaya cuma nama kolom yang ada yang",
                    "     diterima, dan T[K] untuk tipe isinya:",
                    "      function kolom<T, K extends keyof T>(data: T[], k: K): T[K][] {",
                    "        return data.map((x) => x[k]);",
                    "      }",
                    "  3. Untuk pemasaran, tulis `kolom(pelanggan, \"email\").join(\", \")`.",
                    "     Untuk keuangan, `kolom(pelanggan, \"poin\")` langsung bisa dijumlah",
                    "     dengan reduce tanpa as, karena tipenya memang number[].",
                    "  4. Periksa daftar kosong. Dengan nilai awal 0, total poinnya 0. Tanpa",
                    "     nilai awal, reduce pada array kosong melempar TypeError.",
                    "",
                    "Ingat: `kolom(pelanggan, \"emial\")` gagal dikompilasi, karena \"emial\"",
                    "nggak termasuk keyof Pelanggan.",
                ]
            },
        ],
    },
    {
        "title": "7. Class & Modifier Akses",
        "sections": [
            {
                "body": [
                    "Class di TypeScript adalah class JavaScript biasa, ditambah anotasi",
                    "tipe dan modifier akses. Modifier akses adalah kata yang mengatur siapa",
                    "yang boleh memakai sebuah anggota class.",
                    "",
                    "  class Murid {",
                    "      constructor(",
                    "          public readonly nama: string,",
                    "          private nilai: number,",
                    "      ) {}",
                    "  }",
                    "",
                    "Contoh di atas memakai parameter property. Kalau kamu menulis public,",
                    "private, atau readonly di depan parameter constructor, propertinya",
                    "langsung dideklarasikan dan diisi sekaligus. Kamu nggak perlu menulis",
                    "`this.nama = nama` sendiri. Fitur ini cuma ada di TypeScript, nggak ada",
                    "di JavaScript.",
                    "",
                    "Modifier akses:",
                    "  public     bawaan; siapa pun boleh",
                    "  protected  class ini dan turunannya",
                    "  private    hanya class ini",
                    "  readonly   tidak bisa diubah sesudah constructor",
                    "",
                    "Jebakan: private milik TypeScript hilang waktu kompilasi. Dia cuma",
                    "pemeriksaan compiler. Di JavaScript hasilnya, properti itu jadi",
                    "properti biasa yang bisa diakses siapa aja.",
                    "",
                    "Kalau kamu butuh privasi yang tetap berlaku waktu program jalan, pakai",
                    "private field JavaScript, yang ditulis dengan tanda pagar:",
                    "",
                    "  class Murid {",
                    "      #nilai: number;          privat sungguhan",
                    "  }",
                    "",
                    "Mengakses #nilai dari luar class adalah error sintaks di JavaScript.",
                    "Yang menolak JavaScript-nya sendiri, jadi aturan ini tetap berlaku",
                    "sesudah kompilasi.",
                    "",
                    "Getter dan setter adalah method yang dipakai seperti properti:",
                    "  get grade(): string { ... }",
                    "  set nilai(n: number) { ... }",
                    "",
                    "Keduanya dipakai tanpa tanda kurung: m.grade, bukan m.grade().",
                    "",
                    "Pewarisan dan interface ditulis begini:",
                    "  class Kucing extends Hewan implements Berbunyi { }",
                    "",
                    "extends artinya Kucing mewarisi isi Hewan. implements artinya Kucing",
                    "berjanji memenuhi bentuk interface Berbunyi.",
                    "",
                    "abstract menandai class yang nggak bisa dibuat langsung dengan new,",
                    "dan method yang wajib diisi class turunannya.",
                    "",
                    "static dipakai untuk anggota milik class itu sendiri, bukan milik",
                    "objek-objeknya.",
                    "",
                    "override (ada sejak TypeScript 4.3) menandai method yang menimpa method",
                    "induknya. Kalau setelan noImplicitOverride dinyalakan, kata override",
                    "jadi wajib. Setelan ini layak dinyalakan. Tanpanya, salah ketik nama",
                    "method bikin method baru tanpa ketahuan, padahal maksudmu menimpa yang",
                    "lama.",
                ]
            },
            {
                "heading": "Class lengkap",
                "code": """interface Bangun {
  readonly nama: string;
  luas(): number;
}

abstract class BangunDasar implements Bangun {
  protected constructor(public readonly nama: string) {}

  abstract luas(): number;

  ringkas(): string {
    return `${this.nama.padEnd(16)}${this.luas().toFixed(2).padStart(8)}`;
  }
}

class Persegi extends BangunDasar {
  constructor(private readonly sisi: number) {
    super("Persegi");
  }

  luas(): number {
    return this.sisi * this.sisi;
  }
}

class Lingkaran extends BangunDasar {
  static readonly PI = 3.14159;

  constructor(private readonly jari: number) {
    super("Lingkaran");
  }

  luas(): number {
    return Lingkaran.PI * this.jari * this.jari;
  }

  override ringkas(): string {
    return `${super.ringkas()}  (r=${this.jari})`;
  }
}

class Rekening {
  static #urutan = 0;           // privat SUNGGUHAN, bertahan di runtime
  readonly nomor: string;
  #saldo: number;

  constructor(public readonly pemilik: string, saldoAwal = 0) {
    if (pemilik.trim() === "") throw new Error("pemilik wajib diisi");
    Rekening.#urutan += 1;
    this.nomor = `AC${String(Rekening.#urutan).padStart(4, "0")}`;
    this.#saldo = saldoAwal;
  }

  get saldo(): number {
    return this.#saldo;
  }

  get kosong(): boolean {
    return this.#saldo === 0;
  }

  setor(jumlah: number): this {
    if (jumlah <= 0) throw new Error("jumlah harus positif");
    this.#saldo += jumlah;
    return this;
  }

  tarik(jumlah: number): boolean {
    if (jumlah <= 0 || jumlah > this.#saldo) return false;
    this.#saldo -= jumlah;
    return true;
  }

  toString(): string {
    return `${this.nomor} ${this.pemilik.padEnd(8)}${String(this.#saldo).padStart(10)}`;
  }
}

const semua: Bangun[] = [new Persegi(4), new Lingkaran(3), new Persegi(2.5)];
for (const b of semua) {
  console.log(b instanceof BangunDasar ? b.ringkas() : b.nama);
}
console.log(`${"TOTAL".padEnd(16)}${semua.reduce((t, b) => t + b.luas(), 0).toFixed(2).padStart(8)}`);

console.log("---");
const a = new Rekening("Andi", 500000);
const b = new Rekening("Budi");

a.setor(250000);
console.log(`tarik 900rb: ${a.tarik(900000)}`);
console.log(`tarik 300rb: ${a.tarik(300000)}`);
b.setor(100000);

console.log(String(a));
console.log(String(b));
console.log(`b kosong? ${b.kosong}`);

try {
  new Rekening("   ");
} catch (e) {
  console.log(`Ditolak: ${e instanceof Error ? e.message : String(e)}`);
}"""
            },
            {
                "heading": "Private field, tipe this, dan setelan ketat",
                "body": [
                    "Dari contoh itu, ada empat hal yang perlu kamu lihat:",
                    "  1. #saldo dan static #urutan memakai private field JavaScript, bukan",
                    "     private TypeScript. Bedanya nyata: private hilang waktu kompilasi,",
                    "     sedangkan # tetap ada, dan mengaksesnya dari luar class adalah",
                    "     error sintaks.",
                    "  2. get saldo() ngasih akses baca tanpa ngasih akses ubah. Dipakai",
                    "     tanpa tanda kurung: a.saldo.",
                    "  3. setor mengembalikan this, dengan tipe this, bukan Rekening.",
                    "     Bedanya kerasa di pewarisan. Dengan tipe this, class turunan yang",
                    "     memanggil setor tetap dapat tipe turunannya sendiri, bukan tipe",
                    "     induknya.",
                    "  4. protected constructor mencegah new BangunDasar() dari luar, tapi",
                    "     class turunannya tetap boleh memanggil super().",
                    "",
                    "Setelan tsconfig yang layak dinyalakan bersama strict:",
                    "  - noImplicitOverride: mewajibkan kata override.",
                    "  - useDefineForClassFields: field class mengikuti aturan standar",
                    "    JavaScript.",
                    "  - exactOptionalPropertyTypes: membedakan properti yang nggak ada",
                    "    dari properti yang ada tapi isinya undefined.",
                    "  - noUncheckedIndexedAccess: arr[i] jadi bertipe T | undefined.",
                    "",
                    "Yang terakhir paling sering diabaikan, padahal paling berguna. Tanpa",
                    "setelan itu, arr[999] tetap bertipe T walaupun isinya undefined. Dari",
                    "situlah datang error yang paling sering muncul di JavaScript: \"Cannot",
                    "read properties of undefined\".",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Class dipakai untuk objek yang punya aturan yang harus selalu benar:",
                    "saldo dompet digital yang nggak boleh minus, stok barang, atau nomor",
                    "antrean di puskesmas. Aturannya ditaruh di method, dan datanya disimpan",
                    "di field privat supaya kode lain nggak bisa melompati aturan itu.",
                    "",
                    "Kasus kecil: mesin antrean puskesmas membagikan nomor A001, A002, A003,",
                    "dan seterusnya. Petugas memanggil pasien yang paling lama menunggu, dan",
                    "layar menampilkan berapa orang yang masih antre.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya dulu: nomor cuma naik, cuma lewat ambil(), dan yang",
                    "     dipanggil selalu yang terdepan. Simpan nomor terakhir dan daftar",
                    "     tunggu sebagai #nomor dan #menunggu, supaya tetap privat sesudah",
                    "     kompilasi.",
                    "  2. Method ambil() menaikkan nomor lalu memasukkannya ke daftar:",
                    "      ambil(): string {",
                    "        this.#nomor += 1;",
                    "        const n = `A${String(this.#nomor).padStart(3, \"0\")}`;",
                    "        this.#menunggu.push(n);",
                    "        return n;",
                    "      }",
                    "  3. panggil() mengambil yang terdepan dengan shift(), dan getter sisa",
                    "     mengembalikan panjang daftar tanpa membukanya. Tiga kali ambil lalu",
                    "     dua kali panggil menghasilkan A001, A002, dan sisa 1.",
                    "  4. Periksa antrean kosong. shift() mengembalikan undefined, jadi tipe",
                    "     kembalian panggil() adalah `string | undefined`, dan layar petugas",
                    "     harus menulis \"antrean kosong\" alih-alih kata undefined.",
                ]
            },
        ],
    },
    {
        "title": "8. Modul: import & export",
        "sections": [
            {
                "body": [
                    "TypeScript memakai sistem modul ES, yaitu cara standar JavaScript untuk",
                    "membagi kode ke beberapa berkas. Berkas yang menyediakan sesuatu",
                    "menandainya dengan export, dan berkas yang memakainya menulis import:",
                    "",
                    "  // murid.ts",
                    "  export interface Murid { nama: string; nilai: number }",
                    "  export function grade(n: number): string { ... }",
                    "  export const MAKS = 100;",
                    "  export default class Rapor { ... }",
                    "",
                    "  // main.ts",
                    "  import Rapor, { Murid, grade, MAKS } from \"./murid.js\";",
                    "  import * as murid from \"./murid.js\";",
                    "  import { grade as nilaiHuruf } from \"./murid.js\";",
                    "",
                    "Baris import kedua mengumpulkan semua isi murid.js ke dalam satu objek",
                    "bernama murid. Baris ketiga mengimpor grade dengan nama lain, yaitu",
                    "nilaiHuruf.",
                    "",
                    "Coba lihat ekstensi .js di dalam import, padahal berkasnya .ts. Itu",
                    "bukan salah ketik. Dengan modul ES, yang diimpor waktu program jalan",
                    "adalah berkas hasil kompilasi, dan TypeScript nggak mengubah tulisan",
                    "jalur di import. Aturan pastinya tergantung setelan moduleResolution,",
                    "dan bagian ini termasuk yang paling sering bikin bingung pendatang",
                    "baru.",
                    "",
                    "Untuk proyek Node yang baru, pakai ini:",
                    "  \"module\": \"nodenext\"",
                    "  \"moduleResolution\": \"nodenext\"",
                    "  tulis ekstensi .js di setiap import relatif",
                    "",
                    "Import relatif adalah import yang jalurnya diawali ./ atau ../.",
                    "",
                    "Import khusus tipe",
                    "",
                    "Kalau yang kamu impor cuma tipe, tandai dengan type:",
                    "",
                    "  import type { Murid } from \"./murid.js\";",
                    "  import { type Murid, grade } from \"./murid.js\";",
                    "",
                    "Import yang ditandai type dihapus seluruhnya waktu kompilasi. Tanpa",
                    "tanda itu, tergantung alat yang dipakai, bundler bisa ikut memasukkan",
                    "seluruh berkas cuma karena kamu mengimpor satu interface darinya.",
                    "",
                    "Setelan verbatimModuleSyntax memaksa kamu menulis import type di",
                    "tempat yang memerlukannya. Setelan ini layak dinyalakan.",
                    "",
                    "Ada dua jenis export. Named export punya nama tetap, seperti grade di",
                    "atas. Default export adalah satu ekspor utama per berkas,",
                    "seperti Rapor, dan pengimpornya bebas memberi nama apa aja. Mana yang",
                    "lebih baik?",
                    "  - Named export lebih baik untuk hampir semua kasus. Namanya sama di",
                    "    semua tempat, autocomplete jalan, dan kalau namanya diganti lewat",
                    "    refactor, semua tempat yang memakainya ikut berubah.",
                    "  - Default export membebaskan tiap berkas pengimpor memberi nama",
                    "    sendiri. Kebebasan itu justru bikin namanya nggak konsisten.",
                    "",
                    "Berkas deklarasi berakhiran .d.ts isinya tipe aja, tanpa isi kode.",
                    "Berkas ini dipakai untuk ngasih tipe ke pustaka JavaScript yang nggak",
                    "punya tipe sendiri. Sebagian besar pustaka populer punya paket",
                    "@types/nama di npm.",
                ]
            },
            {
                "heading": "Modul dan tsconfig",
                "code": """// ==== File: src/murid.ts ====
export interface Murid {
  readonly id: number;
  nama: string;
  nilai: number;
}

export const NILAI_MAKS = 100;

export function grade(n: number): string {
  if (n >= 85) return "A";
  if (n >= 75) return "B";
  if (n >= 60) return "C";
  return "D";
}

export function lulus(daftar: readonly Murid[]): string[] {
  return daftar.filter((m) => m.nilai >= 75).map((m) => m.nama).sort();
}

// ==== File: src/main.ts ====
import { NILAI_MAKS, grade, lulus } from "./murid.js";
import type { Murid } from "./murid.js";

const kelas: Murid[] = [
  { id: 1, nama: "Andi", nilai: 88 },
  { id: 2, nama: "Budi", nilai: 72 },
  { id: 3, nama: "Cici", nilai: 95 },
];

for (const m of kelas) {
  console.log(`${m.nama.padEnd(6)}${String(m.nilai).padStart(3)} ${grade(m.nilai)}`);
}

console.log(`lulus     : ${lulus(kelas).join(", ")}`);
console.log(`nilai maks: ${NILAI_MAKS}`);"""
            },
            {
                "heading": "tsconfig.json yang layak dipakai",
                "code": """{
  "compilerOptions": {
    "target": "es2022",
    "module": "nodenext",
    "moduleResolution": "nodenext",
    "lib": ["es2022"],

    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "exactOptionalPropertyTypes": true,
    "verbatimModuleSyntax": true,

    "outDir": "dist",
    "rootDir": "src",
    "sourceMap": true,
    "declaration": true,

    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}"""
            },
            {
                "heading": "Arti tiap setelan compilerOptions",
                "body": [
                    "Setelan yang paling menentukan, satu per satu:",
                    "  - strict: menyalakan semua pemeriksaan ketat sekaligus. Jumlahnya",
                    "    bertambah seiring versi; di TypeScript 5.6 ada sembilan setelan.",
                    "    Salah satunya strictNullChecks, yang mewajibkan kamu menyatakan",
                    "    kalau sebuah nilai boleh null. Tanpa strict, separuh manfaat",
                    "    TypeScript hilang.",
                    "  - noUncheckedIndexedAccess: arr[i] jadi bertipe T | undefined. Lebih",
                    "    jujur, dan menangkap bug yang berujung error \"Cannot read",
                    "    properties of undefined\".",
                    "  - target: versi JavaScript yang dihasilkan kompilasi. es2022 aman",
                    "    untuk Node 18 ke atas.",
                    "  - skipLibCheck: melewati pemeriksaan berkas .d.ts milik dependensi,",
                    "    yaitu pustaka yang dipakai proyekmu. Hampir semua proyek",
                    "    menyalakannya. Tanpa itu, satu dependensi yang tipenya bermasalah",
                    "    bisa menggagalkan seluruh build-mu.",
                    "  - declaration: menghasilkan berkas .d.ts. Wajib kalau kamu",
                    "    menerbitkan pustaka.",
                    "  - forceConsistentCasingInFileNames: menangkap import ./Murid yang",
                    "    berkasnya bernama murid. Import seperti itu jalan di macOS dan",
                    "    Windows, lalu gagal di server Linux.",
                    "",
                    "Yang sebaiknya nggak dipakai di proyek baru:",
                    "  \"noImplicitAny\": false     mematikan inti fiturnya",
                    "  \"allowJs\" tanpa alasan     mencampur berkas .js dan .ts",
                    "  \"const enum\"               bermasalah dengan bundler",
                    "",
                    "Tapi untuk proyek yang mewarisi kode JavaScript lama, allowJs bersama",
                    "checkJs justru jalan masuk yang bagus. TypeScript bisa memeriksa",
                    "berkas .js yang udah ada, sebelum kamu mengubahnya ke .ts satu per",
                    "satu.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi rapor atau toko online yang sungguhan terdiri dari puluhan",
                    "berkas. Konstanta dan fungsi yang dipakai di banyak halaman ditaruh di",
                    "satu modul lalu diimpor, supaya aturan yang sama nggak ditulis ulang di",
                    "tiga tempat dan melenceng satu per satu.",
                    "",
                    "Kasus kecil: halaman guru, halaman rapor, dan ekspor CSV masing-masing",
                    "menulis batas lulus 75 sendiri. Sekolah menaikkannya ke 78, satu berkas",
                    "lupa diubah, dan murid bernilai 76 tercatat lulus di layar guru tapi",
                    "nggak lulus di rapor.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari aturan yang diulang: angka batas dan perbandingannya. Dua hal",
                    "     itu yang dipindah ke satu modul.",
                    "  2. Tulis modulnya dengan named export, lalu impor dari setiap halaman:",
                    "      // src/nilai.ts",
                    "      export const BATAS_LULUS = 78;",
                    "      export const lulus = (n: number): boolean => n >= BATAS_LULUS;",
                    "      // src/rapor.ts",
                    "      import { BATAS_LULUS, lulus } from \"./nilai.js\";",
                    "  3. Hapus angka 75 yang tersisa di berkas lain dan ganti dengan",
                    "     `lulus(nilai)`. Perubahan berikutnya cukup di satu baris.",
                    "  4. Periksa jalur impornya. Ekstensinya .js walaupun berkasnya .ts, dan",
                    "     hurufnya harus sama persis: ./Nilai.js jalan di laptop Windows,",
                    "     lalu gagal di server Linux. forceConsistentCasingInFileNames",
                    "     menangkapnya lebih awal.",
                ]
            },
        ],
    },
    {
        "title": "9. Async, Promise & await",
        "sections": [
            {
                "body": [
                    "JavaScript berjalan di satu thread, artinya cuma bisa mengerjakan satu",
                    "hal dalam satu waktu. Karena itu pekerjaan yang harus menunggu, seperti",
                    "jaringan, berkas, dan timer, dikerjakan secara asinkron. Kalau ditunggu",
                    "dengan cara biasa, seluruh program bakal membeku selama menunggu.",
                    "",
                    "Promise adalah janji sebuah nilai yang belum ada sekarang, tapi bakal",
                    "datang nanti:",
                    "",
                    "  const p: Promise<string> = ambilData();",
                    "  p.then((x) => ...).catch((e) => ...).finally(() => ...);",
                    "",
                    "then dijalankan kalau janjinya terpenuhi, catch kalau janjinya gagal,",
                    "dan finally dijalankan apa pun hasilnya.",
                    "",
                    "async/await adalah cara menulis hal yang sama tanpa rantai then:",
                    "",
                    "  async function proses(): Promise<string> {",
                    "      const data = await ambilData();",
                    "      return data.toUpperCase();",
                    "  }",
                    "",
                    "Fungsi async selalu mengembalikan Promise, bahkan kalau kamu menulis",
                    "`return 5`. Tipe kembaliannya `Promise<number>`, bukan number.",
                    "",
                    "await cuma boleh dipakai di dalam fungsi async, atau di tingkat paling",
                    "atas sebuah modul ES. Yang kedua ini namanya top-level await.",
                    "",
                    "Berurutan atau bersamaan",
                    "",
                    "Misalkan ambilA dan ambilB masing-masing butuh 1 detik, dan keduanya",
                    "nggak saling bergantung. Bandingkan dua cara memanggilnya:",
                    "",
                    "  // BERURUTAN: 2 detik",
                    "  const a = await ambilA();",
                    "  const b = await ambilB();",
                    "",
                    "  // BERSAMAAN: 1 detik",
                    "  const [a, b] = await Promise.all([ambilA(), ambilB()]);",
                    "",
                    "await di tiap baris memaksa yang kedua menunggu yang pertama selesai.",
                    "Promise.all menjalankan keduanya bersamaan, lalu menunggu sampai",
                    "dua-duanya selesai. Salah pilih di sini bikin program lambat tanpa",
                    "alasan.",
                    "",
                    "Ada empat cara menggabungkan Promise, dan bedanya penting:",
                    "  Promise.all        semua berhasil; gagal kalau satu gagal",
                    "  Promise.allSettled semua selesai; laporkan masing-masing",
                    "  Promise.race       yang pertama selesai, berhasil atau gagal",
                    "  Promise.any        yang pertama berhasil",
                    "",
                    "Kalau kamu memanggil banyak layanan sekaligus, biasanya yang kamu mau",
                    "allSettled. Satu layanan yang mati nggak boleh membatalkan hasil",
                    "layanan lain.",
                    "",
                    "Error di dalam fungsi async ditangani dengan try/catch biasa:",
                    "  try { await f(); } catch (e) { ... }",
                    "",
                    "Jebakan: Promise yang gagal, padahal nggak di-await dan nggak di-catch,",
                    "menghasilkan unhandled rejection, yaitu kegagalan yang nggak ditangani",
                    "siapa pun. Di Node modern, itu bikin prosesnya berhenti. Kalau kamu",
                    "sengaja nggak menunggu sebuah Promise, pasang .catch() di situ.",
                    "",
                    "Kamu mungkin pernah lihat `void f()`. Penulisan itu cuma menandai",
                    "bahwa kamu sengaja nggak menunggu, misalnya supaya linter (alat",
                    "pemeriksa kebiasaan kode) diam. Kalau f() gagal, prosesnya tetap",
                    "berhenti.",
                ]
            },
            {
                "heading": "Berurutan versus bersamaan",
                "code": """function tunggu(ms: number): Promise<void> {
  return new Promise((selesai) => setTimeout(selesai, ms));
}

async function ambil(nama: string, ms: number): Promise<string> {
  await tunggu(ms);
  return `${nama} selesai (${ms}ms)`;
}

async function gagal(nama: string): Promise<string> {
  await tunggu(50);
  throw new Error(`${nama} gagal`);
}

async function main(): Promise<void> {
  // --- BERURUTAN ---
  let mulai = Date.now();
  console.log(await ambil("A", 200));
  console.log(await ambil("B", 200));
  console.log(`Berurutan ~${Math.round((Date.now() - mulai) / 100) * 100} ms`);

  console.log("---");

  // --- BERSAMAAN ---
  mulai = Date.now();
  const hasil = await Promise.all([ambil("C", 200), ambil("D", 200)]);
  hasil.forEach((h) => console.log(h));
  console.log(`Bersamaan ~${Math.round((Date.now() - mulai) / 100) * 100} ms`);

  console.log("---");

  // --- Promise.all GAGAL kalau satu gagal ---
  try {
    await Promise.all([ambil("E", 50), gagal("F")]);
  } catch (e) {
    console.log(`all   -> ${e instanceof Error ? e.message : String(e)}`);
  }

  // --- allSettled melaporkan masing-masing ---
  const semua = await Promise.allSettled([ambil("G", 50), gagal("H")]);
  for (const s of semua) {
    if (s.status === "fulfilled") {
      console.log(`allSettled -> berhasil: ${s.value}`);
    } else {
      const alasan = s.reason;
      console.log(`allSettled -> gagal  : ${alasan instanceof Error ? alasan.message : String(alasan)}`);
    }
  }

  console.log("---");

  // --- Memproses banyak item BERSAMAAN ---
  const nama = ["satu", "dua", "tiga", "empat"];
  mulai = Date.now();
  const panjang = await Promise.all(nama.map(async (n) => {
    await tunggu(100);
    return `${n}=${n.length}`;
  }));
  console.log(panjang.join(", "));
  console.log(`empat tugas ~${Math.round((Date.now() - mulai) / 100) * 100} ms`);
}

main();"""
            },
            {
                "heading": "Await dalam for lawan Promise.all",
                "body": [
                    "Keluaran:",
                    "  A selesai (200ms)",
                    "  B selesai (200ms)",
                    "  Berurutan ~400 ms",
                    "  ---",
                    "  C selesai (200ms)",
                    "  D selesai (200ms)",
                    "  Bersamaan ~200 ms",
                    "  ---",
                    "  all   -> F gagal",
                    "  allSettled -> berhasil: G selesai (50ms)",
                    "  allSettled -> gagal  : H gagal",
                    "  ---",
                    "  satu=4, dua=3, tiga=4, empat=5",
                    "  empat tugas ~100 ms",
                    "",
                    "Blok terakhir nunjukin pola yang paling sering salah di kode nyata:",
                    "",
                    "  // SALAH: 400 ms, satu per satu",
                    "  for (const n of nama) { await proses(n); }",
                    "",
                    "  // BENAR: 100 ms, semuanya bersamaan",
                    "  await Promise.all(nama.map((n) => proses(n)));",
                    "",
                    "Perulangan yang menunggu satu per satu kadang memang yang benar.",
                    "Misalnya kalau kamu sengaja membatasi beban ke server, atau kalau tiap",
                    "langkah butuh hasil langkah sebelumnya. Yang salah adalah memakainya",
                    "tanpa sadar.",
                    "",
                    "Kalau mau membatasi berapa tugas yang jalan bersamaan, pustaka seperti",
                    "p-limit bisa mengaturnya.",
                    "",
                    "`s.status === \"fulfilled\"` adalah discriminated union lagi. Di dalam",
                    "cabang itu, TypeScript tahu s.value tersedia. Di cabang lainnya, dia",
                    "tahu yang tersedia s.reason. Pola yang sama muncul di banyak API",
                    "modern.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman beranda aplikasi bank atau toko online biasanya memuat beberapa",
                    "hal dari layanan yang berbeda: profil, isi keranjang, dan promo. Kalau",
                    "semuanya ditunggu satu per satu, halaman terasa lambat. Kalau satu",
                    "layanan mati lalu seluruh halaman ikut kosong, pengguna nggak bisa",
                    "berbuat apa-apa.",
                    "",
                    "Kasus kecil: profil butuh 300 ms, keranjang 200 ms, dan promo 500 ms.",
                    "Menunggu satu per satu makan sekitar 1000 ms. Hari ini layanan promo",
                    "juga sedang mati, padahal profil dan keranjang tetap harus tampil.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami ketergantungannya: ketiga permintaan nggak saling butuh",
                    "     hasil, jadi boleh jalan bersamaan. Lama halaman jadi ditentukan",
                    "     yang paling lambat, sekitar 500 ms.",
                    "  2. Pilih alatnya. Promise.all gagal seluruhnya kalau satu gagal,",
                    "     sedangkan allSettled melaporkan masing-masing:",
                    "      const [profil, keranjang, promo] = await Promise.allSettled([",
                    "        ambilProfil(), ambilKeranjang(), ambilPromo(),",
                    "      ]);",
                    "  3. Cek `status === \"fulfilled\"` untuk tiap hasil. Bagian yang gagal",
                    "     diganti teks pengganti, misalnya \"promo belum bisa dimuat\".",
                    "  4. Periksa ketergantungan tersembunyi. Kalau keranjang butuh id dari",
                    "     profil, permintaan keranjang harus menunggu profil selesai, dan",
                    "     cuma promo yang dijalankan bersamaan.",
                ]
            },
        ],
    },
    {
        "title": "10. Tipe Lanjut",
        "sections": [
            {
                "body": [
                    "Bagian ini yang bikin sistem tipe TypeScript sering disebut salah satu",
                    "yang paling ekspresif di antara bahasa populer. Ekspresif artinya",
                    "banyak aturan yang bisa kamu tulis sebagai tipe.",
                    "",
                    "Conditional type: tipe yang bercabang",
                    "",
                    "  type Kalau<T> = T extends string ? \"teks\" : \"bukan\";",
                    "  Kalau<\"a\">     -> \"teks\"",
                    "  Kalau<5>       -> \"bukan\"",
                    "",
                    "  type Kupas<T> = T extends Array<infer U> ? U : T;",
                    "  Kupas<number[]>  -> number",
                    "",
                    "Bentuknya mirip `a ? b : c` di JavaScript. Kalau T cocok dengan string,",
                    "hasilnya \"teks\"; kalau nggak, hasilnya \"bukan\". infer U menangkap",
                    "sebagian dari tipenya supaya bisa dipakai di cabang benar. ReturnType",
                    "dan Awaited di pustaka standar dibuat dengan cara ini.",
                    "",
                    "Mapped type: mengubah setiap properti",
                    "",
                    "  type Semua<T> = { [K in keyof T]: T[K] };",
                    "  type Opsional<T> = { [K in keyof T]?: T[K] };",
                    "  type Beku<T> = { readonly [K in keyof T]: T[K] };",
                    "  type Buang<T> = { -readonly [K in keyof T]-?: T[K] };",
                    "",
                    "`[K in keyof T]` dibaca \"untuk setiap nama properti K di T\". Tanda",
                    "minus menghapus penanda: -? membuang opsional, dan -readonly membuang",
                    "readonly. Required bawaan TypeScript bekerja dengan -?. Tipe Mutable,",
                    "yang sering ditulis orang sendiri karena nggak tersedia bawaan, memakai",
                    "-readonly.",
                    "",
                    "Template literal type: menyusun tipe string",
                    "",
                    "  type Peristiwa = `on${Capitalize<\"klik\" | \"geser\">}`;",
                    "  // \"onKlik\" | \"onGeser\"",
                    "",
                    "  type Rute = `/api/${string}`;",
                    "",
                    "Rute menerima teks apa aja yang diawali /api/. Ada empat pembantu",
                    "bawaan untuk mengubah huruf: Uppercase, Lowercase, Capitalize, dan",
                    "Uncapitalize.",
                    "",
                    "satisfies (TypeScript 4.9): memeriksa tanpa melebarkan",
                    "",
                    "Melebar artinya tipe yang tadinya spesifik berubah jadi lebih umum,",
                    "misalnya dari \"#f00\" jadi string. satisfies ngecek apakah sebuah nilai",
                    "cocok dengan suatu tipe, tanpa melebarkan tipe nilai itu:",
                    "",
                    "  const warna = {",
                    "      merah: \"#f00\",",
                    "      biru: \"#00f\",",
                    "  } satisfies Record<string, `#${string}`>;",
                    "",
                    "  warna.merah      tipenya \"#f00\"",
                    "",
                    "Kalau ditulis dengan anotasi biasa, hasilnya lain:",
                    "",
                    "  const warna: Record<string, `#${string}`> = { ... };",
                    "  warna.merah      tipenya `#${string}`, literalnya hilang",
                    "",
                    "Literalnya cuma bertahan kalau tipe di belakang satisfies memang",
                    "memuat bentuk literal, seperti `#${string}` tadi. Dengan satisfies",
                    "Record<string, string>, warna.merah tetap bertipe string.",
                    "",
                    "Kebiasaan yang sehat soal semua fitur ini: jangan dipakai cuma karena",
                    "bisa. Tipe yang terlalu pintar sering menghasilkan pesan error yang",
                    "hampir mustahil dibaca. Pakai kalau dia memang menghapus pengulangan",
                    "atau menutup celah yang nyata.",
                ]
            },
            {
                "heading": "Tipe lanjut dalam praktik",
                "code": """// --- Mapped type dan modifier ---
interface Murid {
  readonly id: number;
  nama: string;
  nilai: number;
  catatan?: string;
}

type BisaDiubah<T> = { -readonly [K in keyof T]: T[K] };
type WajibSemua<T> = { [K in keyof T]-?: T[K] };
type Berawalan<T, P extends string> = {
  [K in keyof T as `${P}${Capitalize<string & K>}`]: T[K];
};

type MuridBisaDiubah = BisaDiubah<Murid>;
type MuridWajib = WajibSemua<Murid>;
type MuridBerawalan = Berawalan<Pick<Murid, "nama" | "nilai">, "get">;

const m1: MuridBisaDiubah = { id: 1, nama: "Andi", nilai: 88 };
m1.id = 2;                        // boleh: readonly sudah dibuang

const m2: MuridWajib = { id: 3, nama: "Budi", nilai: 72, catatan: "wajib" };
const m3: MuridBerawalan = { getNama: "Cici", getNilai: 95 };

console.log(`bisa diubah : ${JSON.stringify(m1)}`);
console.log(`wajib semua : ${JSON.stringify(m2)}`);
console.log(`berawalan   : ${JSON.stringify(m3)}`);

console.log("---");

// --- Conditional type dengan infer ---
type Kupas<T> = T extends Array<infer U> ? U : T;
type Kembalian<F> = F extends (...a: never[]) => infer R ? R : never;

function buatMurid(nama: string): Murid {
  return { id: 0, nama, nilai: 0 };
}

const satu: Kupas<number[]> = 42;
const teks: Kupas<string> = "bukan array";
const hasil: Kembalian<typeof buatMurid> = { id: 9, nama: "Dedi", nilai: 64 };

console.log(`kupas array : ${satu}`);
console.log(`kupas biasa : ${teks}`);
console.log(`kembalian   : ${hasil.nama}`);

console.log("---");

// --- Template literal type ---
type Aksi = "simpan" | "hapus";
type Peristiwa = `on${Capitalize<Aksi>}`;

const penangan: Record<Peristiwa, () => string> = {
  onSimpan: () => "menyimpan",
  onHapus: () => "menghapus",
};

for (const [nama, fn] of Object.entries(penangan)) {
  console.log(`${nama.padEnd(10)}-> ${fn()}`);
}

console.log("---");

// --- satisfies: memeriksa TANPA melebarkan ---
const warna = {
  merah: "#ff0000",
  biru: "#0000ff",
} satisfies Record<string, `#${string}`>;

// warna.merah bertipe "#ff0000", bukan string
const merah: "#ff0000" = warna.merah;
console.log(`satisfies   : ${merah}`);
console.log(`kunci       : ${Object.keys(warna).join(", ")}`);"""
            },
            {
                "heading": "Key remapping dan satisfies",
                "body": [
                    "Keluaran:",
                    "  bisa diubah : {\"id\":2,\"nama\":\"Andi\",\"nilai\":88}",
                    "  wajib semua : {\"id\":3,\"nama\":\"Budi\",\"nilai\":72,\"catatan\":\"wajib\"}",
                    "  berawalan   : {\"getNama\":\"Cici\",\"getNilai\":95}",
                    "  ---",
                    "  kupas array : 42",
                    "  kupas biasa : bukan array",
                    "  kembalian   : Dedi",
                    "  ---",
                    "  onSimpan  -> menyimpan",
                    "  onHapus   -> menghapus",
                    "  ---",
                    "  satisfies   : #ff0000",
                    "  kunci       : merah, biru",
                    "",
                    "`Berawalan<T, P>` memakai key remapping lewat klausa as. Setiap nama",
                    "properti diganti dengan nama baru yang disusun dari template literal.",
                    "Dari dua properti nama dan nilai, hasilnya getNama dan getNilai, dan",
                    "nggak ada satu nama pun yang diketik dua kali.",
                    "",
                    "Pola ini dipakai pustaka sungguhan untuk menghasilkan tipe getter,",
                    "tipe penangan event, dan tipe kolom database dari satu definisi.",
                    "",
                    "satisfies masih sering belum dikenal, padahal gunanya besar.",
                    "Bandingkan:",
                    "",
                    "  const a: Record<string, `#${string}`> = { merah: \"#f00\" };",
                    "  a.merah          -> `#${string}`   (melebar)",
                    "",
                    "  const b = { merah: \"#f00\" } satisfies Record<string, `#${string}`>;",
                    "  b.merah          -> \"#f00\"        (tetap sempit)",
                    "",
                    "Dua-duanya memeriksa kecocokan. Cuma yang kedua yang mempertahankan",
                    "informasi tipenya, dan itu sering persis yang kamu butuhkan untuk",
                    "konfigurasi dan konstanta.",
                    "",
                    "Peringatan yang perlu diulang: tipe seperti ini bikin pesan error jauh",
                    "lebih panjang kalau ada yang salah. Kalau sebuah tipe pintar menghemat",
                    "lima baris kode tapi pesan errornya jadi tiga puluh baris, belum tentu",
                    "itu pertukaran yang bagus.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Form pendaftaran, halaman pengaturan, dan filter pencarian di aplikasi",
                    "sungguhan punya banyak isian, dan tiap isian butuh pesan galatnya",
                    "sendiri. Dengan mapped type, tipe pesan galat diturunkan dari tipe form,",
                    "jadi isian baru otomatis ikut punya tempat untuk galatnya.",
                    "",
                    "Kasus kecil: form pendaftaran lomba berisi nama, email, dan umur.",
                    "Peserta minimal berumur 10 tahun. Kiriman dengan nama kosong, email",
                    "rina@contoh.id, dan umur 9 harus menghasilkan dua pesan, satu untuk nama",
                    "dan satu untuk umur.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami keluarannya: objek yang kuncinya sama dengan isian form, dan",
                    "     tiap kunci boleh kosong. Nilainya selalu teks pesan, apa pun tipe",
                    "     isiannya.",
                    "  2. Turunkan tipenya dengan mapped type, alih-alih mengetik ulang:",
                    "      type Form = { nama: string; email: string; umur: number };",
                    "      type GalatForm = { [K in keyof Form]?: string };",
                    "  3. Tulis `periksa(f: Form): GalatForm`. Mulai dari objek kosong, lalu",
                    "     isi galat.nama kalau nama kosong dan galat.umur kalau umurnya di",
                    "     bawah 10. Hasil untuk kiriman tadi berisi tepat dua kunci itu.",
                    "  4. Bandingkan dengan Partial<Form>. Di situ galat.umur bertipe number,",
                    "     jadi pesan teks ditolak. Mapped type di langkah 2 mengganti semua",
                    "     nilainya jadi string, apa pun tipe aslinya.",
                    "",
                    "Ingat: waktu Form dapat isian baru, misalnya sekolah, GalatForm ikut",
                    "punya kunci sekolah tanpa diubah, dan galat.emial ditolak compiler.",
                ]
            },
        ],
    },
    {
        "title": "11. Enum, const & Readonly",
        "sections": [
            {
                "body": [
                    "Enum adalah kumpulan nilai yang diberi nama. Enum termasuk sedikit",
                    "fitur TypeScript yang menghasilkan kode sungguhan di JavaScript. Hampir",
                    "semua fitur tipe lainnya hilang waktu kompilasi, enum nggak. Contoh",
                    "lainnya parameter property dari materi Class & Modifier Akses.",
                    "",
                    "  enum Arah { Utara, Timur, Selatan, Barat }",
                    "  enum Status { Draf = \"draf\", Terbit = \"terbit\" }",
                    "",
                    "Arah adalah enum numerik: Utara otomatis bernilai 0, Timur 1, dan",
                    "seterusnya. Status adalah enum string, karena tiap anggotanya diberi",
                    "teks.",
                    "",
                    "Enum numerik punya perilaku yang sering bikin kaget: dia reverse-mapped,",
                    "artinya bisa dibaca dari dua arah. Arah.Utara hasilnya 0, dan Arah[0]",
                    "hasilnya \"Utara\". Enum string nggak begitu.",
                    "",
                    "Dulu enum numerik juga menerima angka apa aja: `const a: Arah = 99`",
                    "diterima di TypeScript versi lama. Aturan itu udah diperketat, tapi",
                    "enum string tetap lebih aman.",
                    "",
                    "Kode modern lebih suka alternatif ini: union literal ditambah objek",
                    "as const.",
                    "",
                    "  const Arah = {",
                    "      Utara: \"utara\",",
                    "      Timur: \"timur\",",
                    "  } as const;",
                    "",
                    "  type Arah = typeof Arah[keyof typeof Arah];",
                    "",
                    "Kelebihannya: TypeScript nggak menambahkan kode apa pun di luar yang",
                    "kamu tulis, nilainya langsung cocok dengan string dari JSON, dan",
                    "bundler bisa membuangnya kalau nggak dipakai.",
                    "",
                    "as const disebut const assertion. Dia mengerjakan tiga hal sekaligus:",
                    "  - setiap properti jadi readonly",
                    "  - setiap nilai literal nggak melebar (\"a\" tetap \"a\", nggak berubah",
                    "    jadi string)",
                    "  - array jadi tuple yang readonly",
                    "",
                    "  const a = [1, 2, 3];              number[]",
                    "  const b = [1, 2, 3] as const;     readonly [1, 2, 3]",
                    "",
                    "Readonly bisa dipasang di berbagai tempat:",
                    "  readonly nama: string             properti",
                    "  readonly number[]                 array",
                    "  ReadonlyArray<number>             sama",
                    "  Readonly<T>                       seluruh objek",
                    "  ReadonlyMap / ReadonlySet",
                    "",
                    "Sama seperti private, semua readonly hilang waktu kompilasi. readonly",
                    "mencegah kamu menulis kode yang mengubah nilai, tapi nggak mencegah",
                    "perubahan waktu program jalan. Untuk itu ada Object.freeze(), yang",
                    "tetap bekerja waktu program jalan.",
                ]
            },
            {
                "heading": "Enum, as const, dan readonly",
                "code": """// --- Enum string: aman dan terbaca di log ---
enum Status {
  Draf = "draf",
  Ditinjau = "ditinjau",
  Terbit = "terbit",
}

// --- Alternatif tanpa enum: objek as const + union ---
const Taraf = {
  Info: "info",
  Peringatan: "peringatan",
  Galat: "galat",
} as const;

type Taraf = (typeof Taraf)[keyof typeof Taraf];

function warna(t: Taraf): string {
  switch (t) {
    case "info": return "biru";
    case "peringatan": return "kuning";
    case "galat": return "merah";
    default: {
      const _lengkap: never = t;
      throw new Error(`taraf belum ditangani: ${String(_lengkap)}`);
    }
  }
}

console.log("Status (enum):");
for (const s of Object.values(Status)) {
  console.log(`  ${s.padEnd(10)}panjang ${s.length}`);
}

console.log("Taraf (as const):");
for (const t of Object.values(Taraf)) {
  console.log(`  ${t.padEnd(12)}${warna(t)}`);
}

console.log("---");

// --- as const: literal tidak melebar ---
const biasa = { warna: "merah", ukuran: 14 };
const beku = { warna: "merah", ukuran: 14 } as const;

// biasa.warna bertipe string; beku.warna bertipe "merah"
const w: "merah" = beku.warna;
console.log(`as const  : ${w}`);
// beku.ukuran = 16;        <- error: readonly

biasa.warna = "biru";       // boleh
console.log(`tanpa const: ${biasa.warna}`);

console.log("---");

// --- readonly array ---
function total(angka: readonly number[]): number {
  // angka.push(1);          <- error: readonly
  return angka.reduce((a, b) => a + b, 0);
}

const nilai = [78, 92, 65] as const;
console.log(`total     : ${total(nilai)}`);
console.log(`tuple     : ${nilai.length} elemen, elemen pertama ${nilai[0]}`);

console.log("---");

// --- Object.freeze bekerja SUNGGUHAN di runtime ---
const setelan = Object.freeze({ tema: "gelap", ukuran: 18 });
try {
  // Dalam mode ketat ini melempar; di luar mode ketat ia diam saja
  (setelan as { tema: string }).tema = "terang";
} catch (e) {
  console.log(`freeze    : ${e instanceof Error ? e.constructor.name : "galat"}`);
}
console.log(`tema tetap: ${setelan.tema}`);"""
            },
            {
                "heading": "Beda readonly dan Object.freeze",
                "body": [
                    "Keluaran:",
                    "  Status (enum):",
                    "    draf      panjang 4",
                    "    ditinjau  panjang 8",
                    "    terbit    panjang 6",
                    "  Taraf (as const):",
                    "    info        biru",
                    "    peringatan  kuning",
                    "    galat       merah",
                    "  ---",
                    "  as const  : merah",
                    "  tanpa const: biru",
                    "  ---",
                    "  total     : 235",
                    "  tuple     : 3 elemen, elemen pertama 78",
                    "  ---",
                    "  freeze    : TypeError",
                    "  tema tetap: gelap",
                    "",
                    "Blok terakhir nunjukin perbedaan paling penting di materi ini:",
                    "readonly hilang waktu kompilasi, Object.freeze nggak. readonly",
                    "mencegah kamu menulis kode yang mengubah. Object.freeze mencegah",
                    "perubahannya terjadi waktu program jalan.",
                    "",
                    "Untuk data dari luar yang nggak boleh diubah siapa pun, yang kamu",
                    "butuhkan Object.freeze.",
                    "",
                    "`type Taraf = (typeof Taraf)[keyof typeof Taraf]` perlu dibaca",
                    "pelan-pelan:",
                    "  typeof Taraf            tipe objeknya",
                    "  keyof typeof Taraf      \"Info\"|\"Peringatan\"|\"Galat\"",
                    "  (typeof Taraf)[...]     nilai di kunci-kunci itu",
                    "                          -> \"info\"|\"peringatan\"|\"galat\"",
                    "",
                    "Pola ini lazim banget, jadi bentuknya layak dihafal. Daftar nilainya",
                    "cukup ditulis sekali, dan tipenya diturunkan dari situ. Kalau daftarnya",
                    "berubah, cuma ada satu tempat yang perlu diubah.",
                    "",
                    "Nama Taraf di sini dipakai untuk konstanta dan untuk tipe sekaligus.",
                    "TypeScript membolehkannya karena tipe dan nilai disimpan di ruang nama",
                    "yang terpisah. Kebiasaan ini dipakai luas, dan bikin kodenya lebih",
                    "ringkas.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi pengiriman menyimpan tabel tarif ongkir per kota yang dibaca",
                    "halaman checkout, halaman lacak paket, dan laporan. Tabel seperti itu",
                    "cuma boleh dibaca. as const membuatnya readonly sekaligus menjadikan",
                    "daftar kotanya tipe, dan Object.freeze menjaganya waktu program jalan.",
                    "",
                    "Kasus kecil: tarif ke Bogor 9000, Depok 10000, dan Bekasi 11000. Sebuah",
                    "fungsi promo mengubah tarif Bogor jadi 0 \"sementara\" lalu lupa",
                    "mengembalikannya, jadi semua pesanan ke Bogor sesudahnya gratis ongkir.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami pemakaiannya: tabelnya dibaca di banyak tempat dan nggak",
                    "     pernah perlu diubah sesudah aplikasi mulai.",
                    "  2. Tulis sekali dengan as const, lalu turunkan tipe kotanya:",
                    "      const tarif = { bogor: 9000, depok: 10000, bekasi: 11000 } as const;",
                    "      type Kota = keyof typeof tarif;",
                    "  3. Fungsi `ongkir(kota: Kota)` cuma menerima tiga nama itu, jadi",
                    "     \"Bogor\" berhuruf besar ditolak. Baris `tarif.bogor = 0` juga",
                    "     ditolak dengan pesan \"Cannot assign to 'bogor' because it is a",
                    "     read-only property\".",
                    "  4. Periksa celahnya: readonly hilang waktu kompilasi, dan kode yang",
                    "     memakai as masih bisa mengubah tabelnya. Bungkus objeknya dengan",
                    "     Object.freeze, supaya perubahan itu ditolak waktu program jalan.",
                ]
            },
        ],
    },
    {
        "title": "12. Data dari Luar: Tipe Bukan Jaminan",
        "sections": [
            {
                "body": [
                    "Materi ini yang paling penting di seluruh kurikulum TypeScript. Isinya",
                    "mengulang kalimat dari materi Pengenalan TypeScript & Instalasi: tipe",
                    "hilang waktu program jalan.",
                    "",
                    "Akibatnya biasanya baru kerasa sesudah ada bug di program yang udah",
                    "dipakai orang:",
                    "",
                    "  const data: Murid = await res.json();",
                    "",
                    "Baris itu nggak memeriksa apa pun. res.json() mengembalikan any, dan",
                    "anotasi `: Murid` cuma nyuruh compiler percaya sama kamu. Kalau server",
                    "mengirim bentuk data yang beda, program jalan terus sampai rusak di",
                    "tempat yang jauh dari penyebabnya.",
                    "",
                    "Hal yang sama berlaku untuk semua baris ini:",
                    "",
                    "  JSON.parse(teks) as Murid",
                    "  process.env.PORT as string",
                    "  JSON.parse(localStorage.getItem(\"setelan\") ?? \"{}\") as Setelan",
                    "",
                    "Begitu juga hasil query database. Semuanya cuma janji. Variabel",
                    "lingkungan di baris kedua, misalnya, bisa aja nggak diisi, dan isinya",
                    "jadi undefined.",
                    "",
                    "Ada tiga cara menanganinya, dari yang paling ringan:",
                    "  1. Type guard yang kamu tulis sendiri:",
                    "       function adalahMurid(x: unknown): x is Murid { ... }",
                    "  2. Assertion function:",
                    "       function pastikanMurid(x: unknown): asserts x is Murid",
                    "  3. Pustaka validasi skema: Zod, Valibot, ArkType, atau io-ts.",
                    "",
                    "Cara ketiga yang dipakai proyek sungguhan, dan alasannya kuat. Skema",
                    "adalah deskripsi bentuk data yang bisa dicek waktu program jalan. Skema",
                    "itu jadi satu-satunya sumber kebenaran: tipe TypeScript-nya diturunkan",
                    "dari skema, jadi keduanya nggak mungkin melenceng.",
                    "",
                    "  const Murid = z.object({",
                    "      nama: z.string().min(1),",
                    "      nilai: z.number().int().min(0).max(100),",
                    "  });",
                    "  type Murid = z.infer<typeof Murid>;",
                    "",
                    "  const hasil = Murid.safeParse(dataDariApi);",
                    "  if (!hasil.success) { ... }",
                    "",
                    "Aturan praktisnya: validasi di batas sistem. Begitu data masuk lewat",
                    "jaringan, berkas, atau ketikan pengguna, periksa sekali di situ.",
                    "Sesudah itu, seluruh kode di dalam program boleh mempercayai tipenya.",
                    "",
                    "Kata as (type assertion) juga bukan konversi. `x as Murid` nggak",
                    "mengubah apa pun waktu program jalan. Dia cuma membungkam keberatan",
                    "compiler. Setiap as adalah janji yang nggak diperiksa.",
                ]
            },
            {
                "heading": "Memvalidasi data dari luar tanpa pustaka",
                "code": """interface Murid {
  nama: string;
  kelas: string;
  nilai: number;
}

// --- 1. Type guard: mengembalikan boolean + mempersempit tipe ---
function adalahMurid(x: unknown): x is Murid {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return (
    typeof o.nama === "string" && o.nama.length > 0 &&
    typeof o.kelas === "string" &&
    typeof o.nilai === "number" && Number.isInteger(o.nilai) &&
    o.nilai >= 0 && o.nilai <= 100
  );
}

// --- 2. Assertion function: melempar, bukan mengembalikan ---
function pastikanMurid(x: unknown): asserts x is Murid {
  if (!adalahMurid(x)) {
    throw new TypeError(`bukan Murid yang sah: ${JSON.stringify(x)}`);
  }
}

// --- 3. Pengurai yang mengembalikan hasil bertanda ---
type Hasil<T> =
  | { ok: true; nilai: T }
  | { ok: false; pesan: string };

function uraikanMurid(teks: string): Hasil<Murid> {
  let mentah: unknown;
  try {
    mentah = JSON.parse(teks);
  } catch {
    return { ok: false, pesan: "JSON tidak bisa diurai" };
  }
  if (!adalahMurid(mentah)) {
    return { ok: false, pesan: "bentuk data tidak sesuai" };
  }
  return { ok: true, nilai: mentah };
}

const masukan = [
  '{"nama":"Andi","kelas":"A","nilai":88}',
  '{"nama":"Budi","kelas":"B"}',
  '{"nama":"Cici","kelas":"A","nilai":150}',
  '{"nama":"","kelas":"A","nilai":70}',
  "{rusak}",
];

for (const teks of masukan) {
  const h = uraikanMurid(teks);
  if (h.ok) {
    console.log(`OK    ${h.nilai.nama.padEnd(6)}${h.nilai.kelas} ${h.nilai.nilai}`);
  } else {
    console.log(`TOLAK ${h.pesan}`);
  }
}

console.log("---");

// Kenapa `as` BERBAHAYA: tidak memeriksa apa pun
const palsu = JSON.parse('{"nama":"Dedi"}') as Murid;
console.log(`as tanpa periksa -> nilai: ${palsu.nilai}`);
console.log("  (undefined, dan compiler tidak berkeberatan sama sekali)");

console.log("---");

// Assertion function: sesudah dipanggil, tipenya menyempit
const kandidat: unknown = { nama: "Euis", kelas: "B", nilai: 79 };
pastikanMurid(kandidat);
console.log(`sesudah assert   -> ${kandidat.nama} ${kandidat.nilai}`);"""
            },
            {
                "heading": "Bahaya as dan fungsi assertion",
                "body": [
                    "Keluaran:",
                    "  OK    Andi  A 88",
                    "  TOLAK bentuk data tidak sesuai",
                    "  TOLAK bentuk data tidak sesuai",
                    "  TOLAK bentuk data tidak sesuai",
                    "  TOLAK JSON tidak bisa diurai",
                    "  ---",
                    "  as tanpa periksa -> nilai: undefined",
                    "    (undefined, dan compiler tidak berkeberatan sama sekali)",
                    "  ---",
                    "  sesudah assert   -> Euis 79",
                    "",
                    "Baris \"as tanpa periksa\" itulah inti seluruh materi ini. Kodenya",
                    "dikompilasi tanpa satu keluhan pun, palsu bertipe Murid menurut",
                    "compiler, dan palsu.nilai ternyata undefined. Menurut TypeScript nggak",
                    "ada yang salah. Yang salah adalah janjinya.",
                    "",
                    "`asserts x is Murid` sebagai tipe kembalian artinya: \"kalau fungsi ini",
                    "selesai tanpa melempar error, anggap x sebagai Murid mulai dari titik",
                    "itu\". Karena itu kandidat.nama sesudah pemanggilan nggak ditolak lagi,",
                    "padahal kandidat dideklarasikan unknown.",
                    "",
                    "Assertion function punya syarat yang gampang terlupa: compiler harus",
                    "tahu tipe fungsinya dari yang kamu tulis, tanpa menebak. Fungsi yang",
                    "ditulis dengan kata function, seperti pastikanMurid, aman. Kalau",
                    "assertion function ditulis sebagai arrow function di dalam variabel,",
                    "variabel itu wajib dikasih anotasi tipe. Tanpa anotasi, compiler",
                    "menolak pemanggilannya dengan pesan \"Assertions require every name in",
                    "the call target to be declared with an explicit type annotation\".",
                    "",
                    "Di proyek nyata, tulis skemanya sekali dengan Zod, lalu turunkan",
                    "tipenya dari situ. Menulis type guard sendiri untuk sepuluh bentuk",
                    "data itu membosankan, dan gampang ketinggalan waktu bentuk datanya",
                    "berubah. Type guard yang ketinggalan lebih berbahaya daripada nggak ada",
                    "sama sekali, karena dia ngasih rasa aman yang palsu.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi toko online menerima data dari banyak pihak: notifikasi",
                    "pembayaran dari bank atau penyedia pembayaran, data ongkir dari jasa",
                    "kirim, dan berkas yang diunggah admin. Satu pihak bisa mengubah format",
                    "tanpa kabar, misalnya angka yang tiba-tiba dikirim sebagai teks.",
                    "",
                    "Kasus kecil: dua notifikasi pembayaran masuk. Yang pertama berisi",
                    "`\"jumlah\":150000`, yang kedua `\"jumlah\":\"75000\"` dengan tanda kutip.",
                    "Kode lama menulis `JSON.parse(teks) as Transaksi` lalu menjumlahkan,",
                    "dan total hari itu tercatat 15000075000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami batasnya: teks dari luar masuk, lalu keluar Transaksi yang",
                    "     pasti benar atau penolakan beserta alasannya. Transaksi di sini",
                    "     cukup punya id (teks) dan jumlah (angka).",
                    "  2. Simpan hasil JSON.parse sebagai unknown, lalu periksa tiap properti:",
                    "      function adalahTrx(x: unknown): x is Transaksi {",
                    "        if (typeof x !== \"object\" || x === null) return false;",
                    "        const o = x as Record<string, unknown>;",
                    "        return typeof o.id === \"string\" && typeof o.jumlah === \"number\";",
                    "      }",
                    "  3. Bungkus dalam pengurai yang mengembalikan Hasil<Transaksi>, seperti",
                    "     uraikanMurid di materi. Pemanggil wajib memeriksa ok sebelum",
                    "     menjumlahkan.",
                    "  4. Tentukan aturan untuk kasus pinggirnya: \"75000\" sebagai teks",
                    "     ditolak, dan teks aslinya dicatat di log supaya bisa ditanyakan ke",
                    "     pengirimnya. Hasilnya total 150000 dan satu penolakan yang jelas",
                    "     sebabnya.",
                ]
            },
        ],
    },
    {
        "title": "13. Pengujian",
        "sections": [
            {
                "body": [
                    "Kerangka tes, yaitu alat untuk menulis dan menjalankan tes otomatis,",
                    "yang lazim dipakai untuk TypeScript:",
                    "  - Vitest: paling umum di proyek baru. Cepat, dan langsung mengerti",
                    "    TypeScript tanpa konfigurasi tambahan.",
                    "  - Jest: matang dan ekosistemnya besar. Untuk TypeScript, Jest butuh",
                    "    ts-jest atau SWC.",
                    "  - node:test: bawaan Node 18 ke atas, tanpa dependensi apa pun.",
                    "",
                    "Bentuk tesnya hampir sama di ketiganya:",
                    "",
                    "  import { describe, it, expect } from \"vitest\";",
                    "",
                    "  describe(\"grade\", () => {",
                    "      it(\"memberi A tepat di 85\", () => {",
                    "          expect(grade(85)).toBe(\"A\");",
                    "      });",
                    "  });",
                    "",
                    "describe mengelompokkan tes, it berisi satu tes, dan expect(...)",
                    "memeriksa hasilnya.",
                    "",
                    "Matcher, yaitu cara membandingkan hasil, yang paling sering dipakai:",
                    "  toBe(x)                  sama persis (Object.is)",
                    "  toEqual(x)               sama isinya, sampai ke dalam",
                    "  toStrictEqual(x)         sama isinya dan tipenya",
                    "  toBeCloseTo(x, digit)    untuk pecahan",
                    "  toBeNull / toBeUndefined / toBeDefined",
                    "  toContain(x)             untuk array dan string",
                    "  toHaveLength(n)",
                    "  toThrow(/pola/)",
                    "  resolves / rejects       untuk Promise",
                    "",
                    "Aturan: toBe untuk primitif, toEqual untuk objek. toBe pada dua objek",
                    "yang berbeda selalu gagal walaupun isinya sama, karena toBe",
                    "membandingkan identitas: apakah keduanya objek yang sama di memori.",
                    "",
                    "Untuk pecahan, toBeCloseTo wajib dipakai. `0.1 + 0.2` nggak pernah",
                    "persis 0.3 di aritmetika IEEE 754, standar bilangan pecahan yang",
                    "dipakai JavaScript.",
                    "",
                    "Siklus hidup tes:",
                    "  beforeEach / afterEach   sebelum dan sesudah tiap tes",
                    "  beforeAll / afterAll     sekali untuk seluruh berkas",
                    "",
                    "beforeEach bikin tiap tes mulai dari keadaan yang sama. Tes yang",
                    "hasilnya bergantung pada urutan menjalankannya adalah tes yang suatu",
                    "hari gagal, padahal nggak ada yang mengubah apa pun.",
                    "",
                    "Kebiasaan yang paling berharga adalah menguji di batas. Uji 85 dan 84,",
                    "jangan 90 dan 50. Di batas itulah tanda >= sering salah ketik jadi >.",
                    "",
                    "Tipe juga bisa diuji, dan ini berguna untuk pustaka:",
                    "  expectTypeOf(f).returns.toEqualTypeOf<string>()",
                    "  // @ts-expect-error   menandai baris yang harus gagal",
                    "",
                    "Komentar @ts-expect-error bikin kompilasi gagal kalau baris di",
                    "bawahnya ternyata nggak error. Jadi kamu bisa memastikan kode yang",
                    "salah memang ditolak.",
                ]
            },
            {
                "heading": "Kode beserta tesnya",
                "code": """// ==== File: src/rapor.ts ====
export interface Murid {
  nama: string;
  nilai: number;
}

export function grade(n: number): string {
  if (!Number.isFinite(n) || n < 0 || n > 100) {
    throw new RangeError(`nilai ${n} di luar 0..100`);
  }
  if (n >= 85) return "A";
  if (n >= 75) return "B";
  if (n >= 60) return "C";
  return "D";
}

export function rataRata(daftar: readonly Murid[]): number | null {
  if (daftar.length === 0) return null;
  return daftar.reduce((t, m) => t + m.nilai, 0) / daftar.length;
}

export function lulus(daftar: readonly Murid[]): string[] {
  return daftar.filter((m) => m.nilai >= 75).map((m) => m.nama).sort();
}

// ==== File: src/rapor.test.ts ====
import { beforeEach, describe, expect, it } from "vitest";
import { grade, lulus, rataRata, type Murid } from "./rapor.js";

describe("grade", () => {
  // Di batas inilah perbandingan salah ketik
  it.each([
    [85, "A"], [84, "B"], [75, "B"],
    [74, "C"], [60, "C"], [59, "D"], [0, "D"],
  ])("nilai %i menghasilkan %s", (nilai, harap) => {
    expect(grade(nilai)).toBe(harap);
  });

  it("menolak nilai di luar rentang", () => {
    expect(() => grade(150)).toThrow(RangeError);
    expect(() => grade(-1)).toThrow(/di luar 0\\.\\.100/);
  });
});

describe("rataRata", () => {
  let kelas: Murid[];

  beforeEach(() => {
    kelas = [];          // tiap tes mulai dari nol
  });

  it("null saat kosong", () => {
    expect(rataRata(kelas)).toBeNull();
  });

  it("menghitung rata-rata", () => {
    kelas.push({ nama: "Andi", nilai: 80 }, { nama: "Budi", nilai: 90 });
    expect(rataRata(kelas)).toBeCloseTo(85, 5);
  });
});

describe("lulus", () => {
  it("terurut dan hanya yang lulus", () => {
    const kelas: Murid[] = [
      { nama: "Cici", nilai: 95 },
      { nama: "Budi", nilai: 64 },
      { nama: "Andi", nilai: 75 },
    ];
    expect(lulus(kelas)).toEqual(["Andi", "Cici"]);
  });

  it("array kosong untuk kelas kosong", () => {
    expect(lulus([])).toHaveLength(0);
  });
});"""
            },
            {
                "heading": "Matcher vitest dan cara menjalankannya",
                "body": [
                    "Lihat nilai yang dipilih: 85 dan 84, 75 dan 74, 60 dan 59. Menguji",
                    "tepat di batas jauh lebih berguna daripada menguji nilai di tengah",
                    "rentang, yang hampir nggak pernah menemukan bug.",
                    "",
                    "`it.each([...])` menjalankan tes yang sama dengan banyak data, dan nama",
                    "tiap tesnya ikut memuat datanya. Jadi kalau satu kasus gagal, kamu",
                    "langsung tahu yang mana.",
                    "",
                    "`toEqual(['Andi', 'Cici'])` membandingkan isi. Dengan toBe, tes ini",
                    "selalu gagal, karena dua array yang berbeda nggak pernah identik",
                    "walaupun isinya sama.",
                    "",
                    "`toBeCloseTo(85, 5)` memberi toleransi sampai lima angka di belakang",
                    "koma. Tanpa toleransi, selisih kecil dari pecahan biner bisa bikin",
                    "tesmu gagal walaupun hitungannya benar.",
                    "",
                    "`expect(() => grade(150)).toThrow(...)` membungkus pemanggilannya di",
                    "dalam fungsi. Kalau kamu menulis `expect(grade(150))` langsung, grade",
                    "melempar error sebelum expect sempat jalan, dan tesnya gagal dengan",
                    "pesan yang membingungkan.",
                    "",
                    "Menjalankan:",
                    "  npx vitest              mode tonton (jalan ulang tiap ada perubahan)",
                    "  npx vitest run          sekali jalan, untuk CI",
                    "  npx vitest run --coverage",
                    "  npx vitest -t \"grade\"   hanya tes yang namanya cocok",
                    "",
                    "CI adalah server yang menjalankan tes otomatis setiap ada perubahan",
                    "kode.",
                    "",
                    "Untuk proyek tanpa dependensi sama sekali, node:test bawaan Node udah",
                    "cukup untuk tes sederhana. Bentuknya mirip, dengan assert dari modul",
                    "node:assert/strict.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hitungan yang menyangkut uang, seperti diskon, ongkir, cicilan, atau",
                    "denda, biasanya dijaga tes otomatis. Tes itu jalan di CI setiap ada",
                    "perubahan kode, jadi tanda >= yang tertukar jadi > ketahuan sebelum ada",
                    "pengguna yang ditagih salah.",
                    "",
                    "Kasus kecil: perpustakaan sekolah mendenda 1000 rupiah per hari",
                    "keterlambatan, paling banyak 20000. Kamu diminta memastikan fungsi",
                    "denda(hari) benar, termasuk untuk masukan yang nggak masuk akal.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya sebagai tabel sampai ke batasnya: 0 hari denda 0,",
                    "     1 hari 1000, 20 hari 20000, dan 21 hari tetap 20000 karena atapnya.",
                    "  2. Pilih nilai di batas. Di 0 dan 1 denda mulai berlaku, di 20 dan 21",
                    "     atapnya mulai berlaku. Nilai di tengah seperti 10 jarang menemukan",
                    "     bug.",
                    "  3. Tulis tabel itu dengan it.each:",
                    "      it.each([",
                    "        [0, 0], [1, 1000], [20, 20000], [21, 20000],",
                    "      ])(\"terlambat %i hari, denda %i\", (hari, harap) => {",
                    "        expect(denda(hari)).toBe(harap);",
                    "      });",
                    "  4. Tambah satu tes untuk hari negatif, yaitu",
                    "     `expect(() => denda(-1)).toThrow(RangeError)`. Pemanggilannya wajib",
                    "     dibungkus fungsi, supaya error-nya sempat ditangkap expect.",
                ]
            },
        ],
    },
    {
        "title": "14. Bekerja dengan Data & Koleksi",
        "sections": [
            {
                "body": [
                    "TypeScript nggak menambah method koleksi apa pun. Semua yang dipakai",
                    "milik JavaScript. Yang ditambahkan TypeScript cuma satu: tipe hasilnya",
                    "jadi tepat.",
                    "",
                    "Method array yang paling sering dipakai:",
                    "  map filter reduce forEach find findIndex findLast",
                    "  some every includes indexOf",
                    "  slice splice concat join reverse sort",
                    "  flat flatMap fill at",
                    "  toSorted toReversed toSpliced with   (ES2023)",
                    "",
                    "Empat yang terakhir itu penting, tapi masih kurang dikenal. Keempatnya",
                    "mengembalikan salinan, dan array aslinya dibiarkan utuh. Sebaliknya,",
                    "arr.sort() mengubah array aslinya, dan ini sumber bug yang sering",
                    "banget terjadi. arr.toSorted() nggak begitu.",
                    "",
                    "  const urut = data.toSorted((a, b) => a - b);",
                    "  const ganti = data.with(0, 99);",
                    "",
                    "`data.with(0, 99)` menghasilkan salinan data dengan elemen pertama",
                    "diganti 99.",
                    "",
                    "Map dan Set sering terlupa, padahal sering lebih tepat:",
                    "  new Map<string, number>()",
                    "  m.get(k) / m.set(k, v) / m.has(k) / m.delete(k)",
                    "  m.size / [...m.entries()]",
                    "",
                    "  new Set<number>()",
                    "  s.add(x) / s.has(x) / s.delete(x) / s.size",
                    "",
                    "Map menyimpan pasangan kunci dan nilai. Set menyimpan kumpulan nilai",
                    "yang unik, jadi nilai yang sama nggak bisa masuk dua kali.",
                    "",
                    "Kapan Map lebih baik daripada objek biasa:",
                    "  - Kuncinya bukan string. Map menerima kunci bertipe apa aja.",
                    "  - Kuncinya datang dari luar. Objek biasa punya prototype, yaitu",
                    "    properti warisan bawaan, dan kunci seperti \"constructor\" bisa",
                    "    bertabrakan dengannya.",
                    "  - Urutannya harus dijamin.",
                    "  - Isinya sering ditambah dan dihapus.",
                    "",
                    "Untuk objek:",
                    "  Object.keys / values / entries / fromEntries",
                    "  Object.assign / freeze / groupBy (ES2024)",
                    "  { ...a, ...b }             spread, salinan dangkal",
                    "  structuredClone(x)         salinan dalam",
                    "",
                    "Jebakan tipe di Object.keys: hasilnya string[], bukan (keyof T)[]. Ini",
                    "disengaja dan benar. Sebuah objek bisa punya properti lebih banyak",
                    "daripada yang tertulis di tipenya, jadi TypeScript nggak bisa menjamin",
                    "semua kuncinya termasuk keyof T.",
                    "",
                    "Optional chaining dan nullish coalescing:",
                    "  a?.b?.c              berhenti di null/undefined pertama",
                    "  a?.[0]  f?.()        untuk indeks dan pemanggilan",
                    "  x ?? bawaan          hanya kalau null/undefined",
                    "  x ||= y   x ??= y    penugasan bersyarat",
                    "",
                    "a?.b artinya: kalau a null atau undefined, berhenti dan hasilkan",
                    "undefined. Kalau nggak, ambil a.b.",
                ]
            },
            {
                "heading": "Mengolah data",
                "code": """interface Transaksi {
  barang: string;
  kategori: string;
  jumlah: number;
  harga: number;
}

const data: Transaksi[] = [
  { barang: "Kopi", kategori: "Minuman", jumlah: 3, harga: 25000 },
  { barang: "Teh", kategori: "Minuman", jumlah: 5, harga: 15000 },
  { barang: "Roti", kategori: "Makanan", jumlah: 2, harga: 20000 },
  { barang: "Nasi", kategori: "Makanan", jumlah: 4, harga: 30000 },
  { barang: "Jus", kategori: "Minuman", jumlah: 1, harga: 35000 },
];

const sub = (t: Transaksi): number => t.jumlah * t.harga;

// toSorted: SALINAN terurut, tidak mengubah `data`
const terurut = data.toSorted(
  (a, b) => sub(b) - sub(a) || a.barang.localeCompare(b.barang),
);

for (const t of terurut) {
  console.log(
    `${t.barang.padEnd(11)}${t.kategori.padEnd(11)}` +
    `${String(t.jumlah).padStart(2)} x ${String(t.harga).padStart(6)} = ` +
    `${String(sub(t)).padStart(8)}`,
  );
}

console.log("---");
console.log(`Total     : ${data.reduce((t, x) => t + sub(x), 0)}`);

// Map untuk rekap: urutannya dijamin, kuncinya aman
const rekap = new Map<string, { total: number; n: number }>();
for (const t of data) {
  const lama = rekap.get(t.kategori) ?? { total: 0, n: 0 };
  rekap.set(t.kategori, { total: lama.total + sub(t), n: lama.n + 1 });
}

for (const [kategori, r] of [...rekap].toSorted((a, b) => a[0].localeCompare(b[0]))) {
  console.log(`${kategori.padEnd(10)}: ${r.total} (${r.n} transaksi)`);
}

const termahal = data.reduce((a, b) => (sub(b) > sub(a) ? b : a));
console.log(`${"Termahal".padEnd(10)}: ${termahal.barang}`);

console.log("---");
// data ASLI tidak berubah karena toSorted
console.log(`urutan asli: ${data.map((t) => t.barang).join(", ")}`);

console.log("---");
// Set: unik dan cepat
const kategori = new Set(data.map((t) => t.kategori));
console.log(`kategori   : ${[...kategori].toSorted().join(", ")}`);

// Optional chaining pada struktur bersarang
type Toko = { alamat?: { kota?: string } };
const toko: Toko[] = [{ alamat: { kota: "Bandung" } }, { alamat: {} }, {}];
for (const t of toko) {
  console.log(`kota       : ${t.alamat?.kota ?? "tidak diketahui"}`);
}"""
            },
            {
                "heading": "Pengurutan dua patokan dan Map.get",
                "body": [
                    "Keluaran:",
                    "  Nasi       Makanan     4 x  30000 =   120000",
                    "  Kopi       Minuman     3 x  25000 =    75000",
                    "  Teh        Minuman     5 x  15000 =    75000",
                    "  Roti       Makanan     2 x  20000 =    40000",
                    "  Jus        Minuman     1 x  35000 =    35000",
                    "  ---",
                    "  Total     : 345000",
                    "  Makanan   : 160000 (2 transaksi)",
                    "  Minuman   : 185000 (3 transaksi)",
                    "  Termahal  : Nasi",
                    "  ---",
                    "  urutan asli: Kopi, Teh, Roti, Nasi, Jus",
                    "  ---",
                    "  kategori   : Makanan, Minuman",
                    "  kota       : Bandung",
                    "  kota       : tidak diketahui",
                    "  kota       : tidak diketahui",
                    "",
                    "Baris \"urutan asli\" membuktikan toSorted nggak mengubah array aslinya.",
                    "Kalau pakai sort() biasa, baris itu bakal menampilkan urutan yang udah",
                    "ikut terurut. Bug seperti itu susah dilacak, karena penyebabnya satu",
                    "baris kode yang kelihatannya cuma membaca data.",
                    "",
                    "`sub(b) - sub(a) || a.barang.localeCompare(b.barang)` adalah cara",
                    "mengurutkan dengan dua patokan. Kalau selisih subtotalnya nol (falsy),",
                    "urutannya ditentukan nama barang.",
                    "",
                    "localeCompare membandingkan teks sesuai aturan bahasa, nggak cuma",
                    "membandingkan kode karakternya. Untuk teks yang dibaca manusia, ini",
                    "yang benar. Untuk kunci internal, perbandingan biasa lebih cepat dan",
                    "hasilnya lebih gampang ditebak.",
                    "",
                    "Lihat juga `rekap.get(t.kategori) ?? { total: 0, n: 0 }`. Map.get",
                    "mengembalikan `V | undefined`, dan TypeScript memaksa kamu menangani",
                    "kemungkinan undefined itu. Objek biasa dengan index signature nggak",
                    "ngasih peringatan yang sama, kecuali noUncheckedIndexedAccess",
                    "dinyalakan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pemilik warung atau UMKM yang memakai aplikasi kasir biasanya minta dua",
                    "laporan setiap malam: pendapatan per menu dan jumlah pelanggan yang",
                    "datang. Keduanya cuma pengolahan array transaksi hari itu dengan Map,",
                    "Set, dan toSorted.",
                    "",
                    "Kasus kecil: hari ini ada enam pesanan, yaitu Andi Kopi 18000, Budi",
                    "Teh 8000, \"andi \" Roti 12000, Cici Kopi 18000, Budi Kopi 18000, dan",
                    "Dewi Teh 8000. Laporannya harus berbunyi Kopi 54000, Teh 16000, Roti",
                    "12000, dan empat pelanggan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami keluarannya: satu baris per menu, terurut dari pendapatan",
                    "     terbesar, ditambah satu angka jumlah pelanggan.",
                    "  2. Jumlahkan per menu dengan Map, lalu urutkan salinannya:",
                    "      const perMenu = new Map<string, number>();",
                    "      for (const p of pesanan) {",
                    "        perMenu.set(p.menu, (perMenu.get(p.menu) ?? 0) + p.harga);",
                    "      }",
                    "      const urut = [...perMenu].toSorted((a, b) => b[1] - a[1]);",
                    "  3. Hitung pelanggan dengan Set dari nama mereka, lalu baca size-nya.",
                    "  4. Periksa data kotor: \"andi \" diketik kasir dengan huruf kecil dan",
                    "     spasi di belakang. Tanpa dirapikan, Set menghitung lima orang.",
                    "     Rapikan dulu dengan `p.pelanggan.trim().toLowerCase()`, dan",
                    "     hasilnya empat.",
                ]
            },
        ],
    },
    {
        "title": "15. TypeScript di Node & Browser",
        "sections": [
            {
                "body": [
                    "TypeScript sendiri nggak tahu apa-apa soal lingkungan tempat kodenya",
                    "bakal jalan, entah Node atau browser. API apa yang tersedia ditentukan",
                    "dua setelan:",
                    "",
                    "  \"lib\"    API bahasa dan lingkungan yang dikenali",
                    "  \"types\"  paket tipe global yang dimuat",
                    "",
                    "Untuk Node:",
                    "  npm install --save-dev @types/node",
                    "  \"lib\": [\"es2022\"]",
                    "",
                    "Tanpa @types/node, TypeScript nggak mengenali process, Buffer,",
                    "__dirname, dan semua modul `node:`. Pesan errornya diawali \"Cannot find",
                    "name 'process'\", yang sekilas mirip pesan salah ketik. Baca pesannya",
                    "sampai habis: biasanya TypeScript ikut menyarankan memasang",
                    "@types/node.",
                    "",
                    "  import { readFile } from \"node:fs/promises\";",
                    "  import path from \"node:path\";",
                    "",
                    "Awalan `node:` adalah bentuk yang disarankan sekarang. Dengan awalan",
                    "itu, jelas bahwa yang diimpor modul bawaan Node, bukan paket npm yang",
                    "kebetulan namanya sama.",
                    "",
                    "Untuk browser:",
                    "  \"lib\": [\"es2022\", \"dom\", \"dom.iterable\"]",
                    "",
                    "Kalau \"dom\" ada di lib, document, window, fetch, dan semua API browser",
                    "lainnya dikenali.",
                    "",
                    "Di browser, yang sering menjebak adalah ini:",
                    "",
                    "  const el = document.getElementById(\"tombol\");",
                    "  // bertipe HTMLElement | null",
                    "",
                    "TypeScript memaksa kamu menangani kemungkinan elemennya nggak ada. Itu",
                    "memang benar, karena elemen dengan id itu bisa aja nggak ada di",
                    "halaman. Untuk tipe yang lebih spesifik:",
                    "",
                    "  const el = document.querySelector<HTMLInputElement>(\"#nama\");",
                    "  if (!el) return;",
                    "  el.value;          sekarang dikenali",
                    "",
                    "HTMLInputElement adalah tipe untuk kotak isian <input>, dan value",
                    "adalah isinya.",
                    "",
                    "Menjalankan TypeScript di Node, tiga cara:",
                    "  tsc && node dist/main.js      klasik, paling aman",
                    "  npx tsx src/main.ts           cepat, untuk pengembangan",
                    "  node --experimental-strip-types src/main.ts",
                    "",
                    "Cara ketiga butuh Node 22.6 ke atas. Di Node yang lebih baru, misalnya",
                    "Node 24, opsinya udah nggak perlu: node src/main.ts langsung jalan.",
                    "",
                    "Hati-hati: cara ketiga cuma membuang anotasi tipe, tanpa memeriksanya",
                    "sama sekali. Memang cepat, tapi jangan sampai menggantikan",
                    "tsc --noEmit di CI. Perintah itu memeriksa tipe tanpa menghasilkan",
                    "berkas apa pun. Tanpa dia, nggak ada yang memeriksa tipemu.",
                ]
            },
            {
                "heading": "Node: berkas, argumen, dan lingkungan",
                "code": """// ==== File: package.json ====
// {
//   "type": "module",
//   "devDependencies": { "@types/node": "^22", "typescript": "^5.6" }
// }
//
// Tanpa @types/node, seluruh impor di bawah ditolak compiler dengan
// pesan "Cannot find name process" -- yang terdengar seperti salah ketik.

// ==== File: src/main.ts ====
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";

interface Murid {
  nama: string;
  kelas: string;
  nilai: number;
}

function keCsv(daftar: readonly Murid[]): string {
  const baris = daftar.map((m) => `${m.nama},${m.kelas},${m.nilai}`);
  return ["nama,kelas,nilai", ...baris].join("\\n") + "\\n";
}

function dariCsv(teks: string): Murid[] {
  const [, ...isi] = teks.trim().split("\\n");
  return isi.map((baris) => {
    const [nama, kelas, nilai] = baris.split(",");
    if (nama === undefined || kelas === undefined || nilai === undefined) {
      throw new Error(`baris tidak lengkap: ${baris}`);
    }
    return { nama, kelas, nilai: Number(nilai) };
  });
}

async function main(): Promise<void> {
  const folder = await mkdtemp(path.join(tmpdir(), "belajar-ts-"));
  const berkas = path.join(folder, "murid.csv");

  const data: Murid[] = [
    { nama: "Andi", kelas: "A", nilai: 88 },
    { nama: "Budi", kelas: "B", nilai: 72 },
    { nama: "Cici", kelas: "A", nilai: 95 },
  ];

  await writeFile(berkas, keCsv(data), "utf8");
  console.log(`ditulis   : ${path.basename(berkas)}`);

  const kembali = dariCsv(await readFile(berkas, "utf8"));
  for (const m of kembali.toSorted((a, b) => b.nilai - a.nilai)) {
    console.log(`  ${m.nama.padEnd(6)}${m.kelas} ${String(m.nilai).padStart(3)}`);
  }

  const rata = kembali.reduce((t, m) => t + m.nilai, 0) / kembali.length;
  console.log(`rata-rata : ${rata.toFixed(2)}`);

  console.log("---");
  // JSON: satu-satunya format bawaan yang punya pengurai
  const json = JSON.stringify(kembali[0], null, 2);
  console.log(json);

  console.log("---");
  console.log(`argumen   : ${process.argv.length >= 2 ? "ada" : "kosong"}`);
  console.log(`HOME ada? : ${process.env.HOME !== undefined}`);
  console.log(`platform  : ${typeof process.platform === "string"}`);

  await rm(folder, { recursive: true, force: true });
  console.log("---");
  console.log("folder sementara dibersihkan");
}

main().catch((e: unknown) => {
  console.error(e instanceof Error ? e.message : String(e));
  process.exitCode = 1;
});"""
            },
            {
                "heading": "Destructuring, catch, dan exitCode di Node",
                "body": [
                    "Keluaran:",
                    "  ditulis   : murid.csv",
                    "    Cici  A  95",
                    "    Andi  A  88",
                    "    Budi  B  72",
                    "  rata-rata : 85.00",
                    "  ---",
                    "  {",
                    "    \"nama\": \"Andi\",",
                    "    \"kelas\": \"A\",",
                    "    \"nilai\": 88",
                    "  }",
                    "  ---",
                    "  argumen   : ada",
                    "  HOME ada? : true",
                    "  platform  : true",
                    "  ---",
                    "  folder sementara dibersihkan",
                    "",
                    "Lihat pemeriksaan `if (nama === undefined || ...)`. Pemeriksaan itu",
                    "perlu karena split(\",\") mengembalikan array yang panjangnya nggak",
                    "dijamin. Kode itu membongkar isi array ke tiga variabel sekaligus",
                    "(namanya destructuring), dan dengan noUncheckedIndexedAccess, tiap",
                    "variabelnya bertipe `string | undefined`.",
                    "",
                    "Setelan ini memang terasa merepotkan, tapi dia menangkap bug yang",
                    "nyata. Baris CSV yang kurang kolom bakal menghasilkan undefined, dan di",
                    "tempat lain undefined itu berubah jadi teks \"undefined\" tanpa ada yang",
                    "sadar.",
                    "",
                    "`main().catch(...)` di akhir itu penting. Tanpa itu, Promise yang gagal",
                    "jadi unhandled rejection, dan di Node modern prosesnya langsung",
                    "berhenti.",
                    "",
                    "`process.exitCode = 1` lebih baik daripada `process.exit(1)`. Yang",
                    "pertama ngebiarin Node menyelesaikan penulisan keluaran yang masih",
                    "tertunda. Yang kedua langsung memotongnya, jadi pesan terakhirmu bisa",
                    "hilang.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di kantor, TypeScript di Node sering dipakai untuk skrip kecil: merekap",
                    "ekspor CSV dari aplikasi kasir, memindahkan data, atau mengirim",
                    "pengingat. Skrip seperti itu membaca nama berkas dari argumen perintah",
                    "dan harus memberi pesan yang jelas kalau dipakai dengan salah.",
                    "",
                    "Kasus kecil: aplikasi kasir mengekspor penjualan harian ke berkas CSV",
                    "berkolom tanggal dan total. Pemilik toko ingin satu perintah yang",
                    "mencetak total sebulan, yaitu `node dist/rekap.js oktober.csv`.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukannya: process.argv[0] berisi jalur program node, [1]",
                    "     jalur skripnya, dan nama berkasnya ada di process.argv[2].",
                    "     Keluarannya satu angka total, atau pesan pemakaian.",
                    "  2. Periksa argumennya di awal main(), sebelum membaca berkas:",
                    "      const berkas = process.argv[2];",
                    "      if (berkas === undefined) {",
                    "        console.error(\"pakai: node dist/rekap.js <berkas.csv>\");",
                    "        process.exitCode = 1;",
                    "        return;",
                    "      }",
                    "  3. Baca isinya dengan readFile dari node:fs/promises, buang baris",
                    "     judul seperti dariCsv di materi, lalu jumlahkan Number dari kolom",
                    "     kedua tiap baris.",
                    "  4. Periksa format angkanya. `Number(\"1.250.000\")` hasilnya NaN, jadi",
                    "     baris itu bisa ditolak. Yang lebih licin `Number(\"150.000\")`, yang",
                    "     hasilnya 150 tanpa error, karena titik dibaca sebagai pemisah",
                    "     desimal. Minta ekspornya ditulis tanpa titik ribuan.",
                ]
            },
        ],
    },
    {
        "title": "16. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan interface, discriminated union,",
                    "generic, koleksi, dan pemisahan tanggung jawab dalam satu program utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang. Fiturnya sendiri nggak",
                    "penting. Yang penting cara bagian-bagiannya dipisah.",
                    "",
                    "Ada tiga lapisan, dan arah ketergantungannya cuma satu:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  - Model: interface Barang, union Gerak, dan union galat. Bagian ini",
                    "    nggak tahu apa-apa soal layar.",
                    "  - Layanan: class Gudang beserta semua aturannya. Bagian ini nggak",
                    "    pernah memanggil console.log.",
                    "  - Antarmuka: memanggil layanan, lalu mencetak hasilnya.",
                    "",
                    "Antarmuka memakai Layanan, dan Layanan memakai Model. Arah sebaliknya",
                    "nggak pernah terjadi.",
                    "",
                    "Yang khas TypeScript di sini: kegagalan dikembalikan sebagai",
                    "discriminated union. Kegagalan nggak dilempar sebagai exception, yaitu",
                    "error yang dilempar dengan throw.",
                    "",
                    "Bedanya terasa:",
                    "  - Tanda tangan fungsinya sendiri menyatakan bahwa dia bisa gagal,",
                    "    dan seperti apa bentuk kegagalannya.",
                    "  - Pemanggil harus mempersempit union dulu sebelum bisa memakai",
                    "    hasilnya. Compiler yang memaksanya.",
                    "  - Kalau ada jenis galat baru, setiap switch yang belum lengkap",
                    "    langsung gagal di pemeriksaan never.",
                    "",
                    "Pola ini sama dengan sealed class di Kotlin dan Result di Rust, dan di",
                    "TypeScript dia bisa dipakai tanpa fitur tambahan apa pun.",
                ]
            },
            {
                "heading": "Program lengkap",
                "code": """// ---------------------------------------------------------------- MODEL
interface Barang {
  readonly kode: string;
  readonly nama: string;
  readonly stok: number;
  readonly harga: number;
}

type Gerak = "masuk" | "keluar";

type GalatGudang =
  | { jenis: "kodeSudahAda"; kode: string }
  | { jenis: "kodeTidakDikenal"; kode: string }
  | { jenis: "jumlahTidakSah"; jumlah: number }
  | { jenis: "stokTidakCukup"; punya: number; diminta: number };

type Hasil<T> =
  | { ok: true; nilai: T }
  | { ok: false; galat: GalatGudang };

function pesanGalat(g: GalatGudang): string {
  switch (g.jenis) {
    case "kodeSudahAda":
      return `kode ${g.kode} sudah ada`;
    case "kodeTidakDikenal":
      return `kode ${g.kode} tidak dikenal`;
    case "jumlahTidakSah":
      return `jumlah ${g.jumlah} tidak sah`;
    case "stokTidakCukup":
      return `stok cuma ${g.punya}, diminta ${g.diminta}`;
    default: {
      const _lengkap: never = g;
      throw new Error(`galat belum ditangani: ${JSON.stringify(_lengkap)}`);
    }
  }
}

const subtotal = (b: Barang): number => b.stok * b.harga;

function barisTabel(b: Barang): string {
  return (
    b.kode.padEnd(5) +
    b.nama.padEnd(12) +
    String(b.stok).padStart(2) +
    String(b.harga).padStart(10) +
    String(subtotal(b)).padStart(12)
  );
}

// -------------------------------------------------------------- LAYANAN
class Gudang {
  readonly #isi = new Map<string, Barang>();

  daftar(b: Barang): Hasil<Barang> {
    if (this.#isi.has(b.kode)) {
      return { ok: false, galat: { jenis: "kodeSudahAda", kode: b.kode } };
    }
    this.#isi.set(b.kode, b);
    return { ok: true, nilai: b };
  }

  catat(kode: string, gerak: Gerak, jumlah: number): Hasil<number> {
    const b = this.#isi.get(kode);
    if (b === undefined) {
      return { ok: false, galat: { jenis: "kodeTidakDikenal", kode } };
    }
    if (!Number.isInteger(jumlah) || jumlah <= 0) {
      return { ok: false, galat: { jenis: "jumlahTidakSah", jumlah } };
    }

    const baru = gerak === "masuk" ? b.stok + jumlah : b.stok - jumlah;
    if (baru < 0) {
      return {
        ok: false,
        galat: { jenis: "stokTidakCukup", punya: b.stok, diminta: jumlah },
      };
    }

    this.#isi.set(kode, { ...b, stok: baru });
    return { ok: true, nilai: baru };
  }

  semua(): Barang[] {
    return [...this.#isi.values()].toSorted((a, b) => a.kode.localeCompare(b.kode));
  }

  nilaiPersediaan(): number {
    return [...this.#isi.values()].reduce((t, b) => t + subtotal(b), 0);
  }

  stokMenipis(batas: number): Barang[] {
    return [...this.#isi.values()]
      .filter((b) => b.stok < batas)
      .toSorted((a, b) => a.stok - b.stok || a.kode.localeCompare(b.kode));
  }
}

// ------------------------------------------------------------ ANTARMUKA
const gudang = new Gudang();

for (const b of [
  { kode: "B01", nama: "Kabel", stok: 10, harga: 15000 },
  { kode: "B02", nama: "Adaptor", stok: 4, harga: 85000 },
  { kode: "B03", nama: "Mouse", stok: 25, harga: 120000 },
] satisfies Barang[]) {
  gudang.daftar(b);
}

const langkah: Array<[string, Gerak, number]> = [
  ["B01", "masuk", 15],
  ["B02", "keluar", 10],
  ["B03", "keluar", 5],
  ["B09", "masuk", 1],
  ["B03", "keluar", 0],
];

for (const [kode, gerak, jumlah] of langkah) {
  const aksi = gerak.charAt(0).toUpperCase() + gerak.slice(1);
  const label = `${aksi} ${kode} ${jumlah}`;
  const hasil = gudang.catat(kode, gerak, jumlah);
  console.log(
    hasil.ok
      ? `${label} -> stok ${hasil.nilai}`
      : `${label} -> DITOLAK: ${pesanGalat(hasil.galat)}`,
  );
}

console.log("---");
for (const b of gudang.semua()) console.log(barisTabel(b));

console.log("---");
console.log(`nilai persediaan: ${gudang.nilaiPersediaan()}`);

const menipis = gudang
  .stokMenipis(10)
  .map((b) => `${b.kode} ${b.nama} (${b.stok})`)
  .join(", ");
console.log(`stok menipis (<10): ${menipis}`);"""
            },
            {
                "heading": "Lima keputusan desain dan satisfies",
                "body": [
                    "Lima keputusan yang layak ditiru:",
                    "  1. Kegagalan dikembalikan lewat discriminated union. Pemanggil nggak",
                    "     bisa membaca hasil.nilai sebelum memeriksa hasil.ok, dan compiler",
                    "     yang memaksanya.",
                    "  2. Barang seluruhnya readonly. Perubahan stok dibuat lewat",
                    "     `{ ...b, stok: baru }`, yang menghasilkan objek baru. Jadi nggak",
                    "     ada bagian lain yang bisa memegang sebuah Barang lalu mengubahnya",
                    "     tanpa ketahuan.",
                    "  3. #isi memakai private field JavaScript, bukan private TypeScript.",
                    "     Privasinya tetap berlaku waktu program jalan.",
                    "  4. semua() dan stokMenipis() mengurutkan hasilnya sebelum",
                    "     dikembalikan, dan memakai toSorted, jadi Map aslinya nggak",
                    "     tersentuh.",
                    "  5. Gudang nggak memanggil console.log sama sekali. Karena itu seluruh",
                    "     aturannya bisa diuji tanpa membaca layar.",
                    "",
                    "`satisfies Barang[]` pada daftar awal memeriksa tiap objek terhadap",
                    "bentuk Barang. Properti yang lupa ditulis, atau properti asing yang",
                    "nggak ada di Barang, langsung ketahuan. Dengan `as Barang[]`, dua",
                    "kesalahan itu lolos tanpa keluhan, karena as cuma protes kalau dua",
                    "bentuknya sama sekali nggak cocok.",
                    "",
                    "Kalau kamu mau melanjutkannya:",
                    "  - Validasi data yang masuk dengan Zod di batas sistem.",
                    "  - Simpan ke berkas JSON lewat node:fs/promises.",
                    "  - Sembunyikan penyimpanan di balik sebuah interface, supaya Gudang",
                    "    nggak tahu datanya disimpan di berkas, di database, atau cuma di",
                    "    memori waktu tes.",
                    "  - Tulis tes Vitest untuk Gudang. Ini bisa langsung dikerjakan tanpa",
                    "    mengubah satu baris pun, berkat keputusan nomor 5.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi sungguhan jarang selesai sekali tulis, karena pemilik toko",
                    "terus minta fitur baru. Susunan berlapis seperti Gudang membuat fitur",
                    "itu bisa ditambah tanpa membongkar layar. Aturannya masuk ke Layanan,",
                    "jenis galatnya ke Model, dan pesannya ke Antarmuka.",
                    "",
                    "Kasus kecil: pemilik minta fitur ubah harga. Harga baru harus bilangan",
                    "bulat positif, dan kenaikan lebih dari 50 persen sekaligus ditolak,",
                    "karena biasanya itu salah ketik, misalnya Adaptor 85000 jadi 850000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan lapisannya. Model dapat satu anggota baru di GalatGudang:",
                    "      | { jenis: \"hargaTidakWajar\"; lama: number; baru: number }",
                    "  2. Jalankan tsc. Baris `const _lengkap: never = g` di pesanGalat",
                    "     langsung gagal, dan itulah daftar tugasmu: tulis case",
                    "     \"hargaTidakWajar\" di sana.",
                    "  3. Tambah method ubahHarga(kode, baru) di Gudang yang mengembalikan",
                    "     Hasil<Barang>. Aturan 50 persennya ditulis begini:",
                    "      if (baru > b.harga * 1.5) {",
                    "        return {",
                    "          ok: false,",
                    "          galat: { jenis: \"hargaTidakWajar\", lama: b.harga, baru },",
                    "        };",
                    "      }",
                    "     Kalau lolos, simpan objek baru `{ ...b, harga: baru }`, karena",
                    "     Barang seluruhnya readonly.",
                    "  4. Uji tepat di batasnya: 85000 ke 127500 diterima, 127501 ditolak.",
                    "     Gudang nggak memanggil console.log, jadi tes ini bisa ditulis",
                    "     langsung tanpa membaca layar.",
                ]
            },
        ],
    },
]
