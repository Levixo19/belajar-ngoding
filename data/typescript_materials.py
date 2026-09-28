TYPESCRIPT_MATERIALS = [
    {
        "title": "1. Pengenalan TypeScript & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu TypeScript?",
                    "  - Dibuat Microsoft, dirilis 2012.",
                    "  - Dirancang Anders Hejlsberg, orang yang sama di balik",
                    "    Turbo Pascal, Delphi, dan C#.",
                    "  - SUPERSET dari JavaScript: setiap berkas .js yang sah",
                    "    juga berkas .ts yang sah.",
                    "  - Menambahkan SATU hal: sistem tipe statis.",
                    "",
                    "KALIMAT TERPENTING DI SELURUH MATERI INI, dan ia harus",
                    "ditanam sejak sekarang:",
                    "",
                    "  TIPE HILANG SAAT PROGRAM JALAN.",
                    "",
                    "TypeScript dikompilasi jadi JavaScript biasa, dan seluruh",
                    "anotasi tipenya DIHAPUS. Tidak ada satu pun pemeriksaan",
                    "tipe yang tersisa di hasil akhirnya. Yang kamu dapat",
                    "adalah pemeriksaan saat MENULIS, bukan saat menjalankan.",
                    "",
                    "Akibatnya yang sering mengejutkan:",
                    "  - Data dari API, JSON, atau berkas TIDAK diperiksa",
                    "    sama sekali. `as Murid` cuma janji, bukan jaminan.",
                    "  - Tipe tidak bisa diperiksa dengan `typeof` untuk",
                    "    interface buatanmu sendiri.",
                    "  - Untuk memvalidasi data dari luar, kamu butuh",
                    "    pustaka seperti Zod atau menulis pemeriksa sendiri.",
                    "",
                    "Apa yang didapat sebagai gantinya:",
                    "  - Salah ketik nama properti ketahuan saat mengetik.",
                    "  - Autocomplete yang benar-benar tahu isi objekmu.",
                    "  - Refactor yang aman: mengganti nama menyentuh semua",
                    "    tempat yang benar.",
                    "  - Dokumentasi yang tidak bisa basi, karena ia diperiksa.",
                    "",
                    "Instalasi:",
                    "  npm install -g typescript        global",
                    "  npm install --save-dev typescript  per proyek (lebih baik)",
                    "  tsc --version",
                    "",
                    "Menjalankan:",
                    "  tsc berkas.ts && node berkas.js",
                    "  tsc --watch                      kompilasi otomatis",
                    "  npx tsx berkas.ts                jalankan langsung",
                    "  node --experimental-strip-types berkas.ts   Node 22+",
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
                "body": [
                    "Yang berbeda dari JavaScript hanya satu: ANOTASI TIPE",
                    "sesudah tanda titik dua.",
                    "",
                    "  const nama: string = \"Andi\";",
                    "  function sapa(orang: string): string { ... }",
                    "",
                    "Buang semua anotasinya, dan yang tersisa JavaScript yang",
                    "sah. Itulah yang dilakukan compiler.",
                    "",
                    "INFERENSI membuat sebagian besar anotasi tidak perlu:",
                    "",
                    "  const nama = \"Andi\";      TypeScript tahu ini string",
                    "  const umur = 20;          tahu ini number",
                    "",
                    "Aturan praktis yang dipakai kode TypeScript yang baik:",
                    "  - JANGAN tulis tipe kalau sudah jelas dari nilainya.",
                    "  - TULIS tipe di batas: parameter fungsi, nilai",
                    "    kembalian fungsi publik, dan bentuk data dari luar.",
                    "",
                    "Menulis `const nama: string = \"Andi\"` bukan salah, cuma",
                    "berlebihan — dan berlebihan itu ongkos, karena setiap",
                    "anotasi harus ikut diperbarui saat kodenya berubah.",
                    "",
                    "Berkas konfigurasi `tsconfig.json` mengatur seluruh",
                    "perilaku compiler. Satu setelan jauh lebih penting",
                    "daripada yang lain:",
                    "",
                    "  { \"compilerOptions\": { \"strict\": true } }",
                    "",
                    "Tanpa `strict`, separuh gunanya TypeScript hilang: null",
                    "diterima di mana-mana dan parameter yang tidak beranotasi",
                    "diam-diam jadi `any`. Selalu nyalakan, sejak berkas",
                    "pertama.",
                ]
            },
        ],
    },
    {
        "title": "2. Tipe Dasar",
        "sections": [
            {
                "body": [
                    "Tipe primitif, semuanya HURUF KECIL:",
                    "  string   number   boolean",
                    "  bigint   symbol",
                    "  null     undefined",
                    "",
                    "PERINGATAN: `String`, `Number`, dan `Boolean` dengan",
                    "huruf besar adalah tipe OBJEK pembungkus, dan hampir",
                    "tidak pernah yang kamu maksud. Pakai yang huruf kecil.",
                    "",
                    "TypeScript cuma punya SATU tipe angka: `number`, yang",
                    "berupa pecahan 64-bit. Tidak ada int, long, atau float",
                    "terpisah. Untuk bilangan bulat sangat besar ada `bigint`",
                    "yang ditulis `123n`.",
                    "",
                    "Array, dua bentuk yang identik:",
                    "  const a: number[] = [1, 2, 3];",
                    "  const a: Array<number> = [1, 2, 3];",
                    "",
                    "TUPLE — array berukuran tetap dengan tipe per posisi:",
                    "  const titik: [number, number] = [3, 4];",
                    "  const pasangan: [string, number] = [\"umur\", 20];",
                    "  const opsional: [string, number?] = [\"a\"];",
                    "  const sisanya: [string, ...number[]] = [\"a\", 1, 2];",
                    "",
                    "OBJEK ditulis dengan bentuknya:",
                    "  const murid: { nama: string; nilai: number } = {",
                    "      nama: \"Andi\", nilai: 88,",
                    "  };",
                    "",
                    "Penanda tambahan pada properti:",
                    "  nama?: string       OPSIONAL, boleh tidak ada",
                    "  readonly id: number tidak bisa diubah sesudah dibuat",
                    "",
                    "TIGA TIPE KHUSUS yang wajib dibedakan:",
                    "",
                    "  any      MATIKAN pemeriksaan. Apa pun boleh masuk dan",
                    "           keluar. Ini pintu keluar darurat, bukan alat",
                    "           sehari-hari.",
                    "  unknown  'aku belum tahu tipenya'. Apa pun boleh MASUK,",
                    "           tapi tidak ada yang boleh DILAKUKAN padanya",
                    "           sampai kamu memeriksanya.",
                    "  never    tidak punya satu pun nilai. Tipe kembalian",
                    "           fungsi yang selalu melempar atau tidak pernah",
                    "           selesai.",
                    "",
                    "`unknown` hampir selalu lebih baik daripada `any` untuk",
                    "data yang datang dari luar: ia MEMAKSA kamu memeriksanya",
                    "sebelum memakainya.",
                    "",
                    "  void     tidak mengembalikan apa-apa (fungsi)",
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
                    "Fungsi `jelaskan` menunjukkan kenapa `unknown` lebih baik",
                    "daripada `any`. Dengan `any`, `x.length` diterima tanpa",
                    "keberatan apa pun — dan meledak saat x ternyata angka.",
                    "Dengan `unknown`, compiler MENOLAK setiap pemakaian",
                    "sampai kamu mempersempitnya lebih dulu.",
                    "",
                    "Proses mempersempit itu disebut NARROWING, dan alatnya:",
                    "  typeof x === \"string\"",
                    "  Array.isArray(x)",
                    "  x === null",
                    "  x instanceof Kelas",
                    "  \"nama\" in x",
                    "",
                    "Perhatikan `typeof null` memberi `\"object\"` — bug",
                    "JavaScript yang berumur tiga puluh tahun dan tidak bisa",
                    "diperbaiki tanpa merusak internet. Itu sebabnya",
                    "pemeriksaan `x === null` ditulis terpisah.",
                    "",
                    "`??` (nullish coalescing) memberi nilai cadangan HANYA",
                    "kalau kirinya null atau undefined. Bedanya dengan `||`",
                    "penting: `0 || 5` memberi 5, sedangkan `0 ?? 5` memberi",
                    "0 — dan untuk angka, yang kedua hampir selalu yang kamu",
                    "maksud.",
                ]
            },
        ],
    },
    {
        "title": "3. Union, Literal & Narrowing",
        "sections": [
            {
                "body": [
                    "UNION TYPE adalah gagasan paling khas TypeScript:",
                    "sebuah nilai boleh bertipe A ATAU B.",
                    "",
                    "  let id: string | number;",
                    "  let mungkin: string | null;",
                    "  let hasil: Sukses | Gagal;",
                    "",
                    "Selama sebuah nilai masih union, kamu hanya boleh",
                    "memakai anggota yang dimiliki SEMUA anggotanya. Untuk",
                    "sisanya, kamu harus MEMPERSEMPITNYA lebih dulu.",
                    "",
                    "LITERAL TYPE — tipe yang isinya satu nilai tertentu:",
                    "",
                    "  let arah: \"utara\" | \"timur\" | \"selatan\" | \"barat\";",
                    "  let kode: 200 | 404 | 500;",
                    "  let saklar: true;",
                    "",
                    "Gabungan literal union ini menggantikan enum di sebagian",
                    "besar kasus, dan ia lebih ringan: ia HILANG sepenuhnya",
                    "saat kompilasi, sedangkan enum menghasilkan objek",
                    "sungguhan di JavaScript.",
                    "",
                    "NARROWING — cara mempersempit union:",
                    "",
                    "  typeof x === \"string\"        untuk primitif",
                    "  Array.isArray(x)             untuk array",
                    "  x === null / x == null       null dan undefined",
                    "  x instanceof Kelas           untuk class",
                    "  \"nama\" in x                  untuk properti",
                    "  x.jenis === \"lingkaran\"      DISCRIMINATED UNION",
                    "",
                    "DISCRIMINATED UNION adalah pola terpenting di daftar ini,",
                    "dan ia setara sealed class di Kotlin atau enum berdata",
                    "di Rust:",
                    "",
                    "  type Bentuk =",
                    "      | { jenis: \"lingkaran\"; jari: number }",
                    "      | { jenis: \"persegi\"; sisi: number };",
                    "",
                    "Properti `jenis` yang sama namanya di semua anggota",
                    "disebut DISKRIMINAN. Memeriksanya mempersempit tipenya",
                    "secara otomatis, dan compiler tahu properti apa yang",
                    "tersedia di tiap cabang.",
                    "",
                    "EXHAUSTIVENESS CHECK memastikan tidak ada cabang yang",
                    "terlewat:",
                    "",
                    "  default: {",
                    "      const _lengkap: never = bentuk;",
                    "      throw new Error(`belum ditangani: ${_lengkap}`);",
                    "  }",
                    "",
                    "Kalau nanti ada anggota union baru, baris itu GAGAL",
                    "DIKOMPILASI — compiler menunjukkan persis tempat yang",
                    "perlu diperbarui.",
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
                    "Di dalam `case \"lingkaran\"`, TypeScript TAHU bahwa `b`",
                    "punya properti `jari` dan TIDAK punya `sisi`. Menulis",
                    "`b.sisi` di situ adalah error kompilasi. Itulah yang",
                    "membuat discriminated union jauh lebih aman daripada",
                    "objek dengan properti opsional di mana-mana.",
                    "",
                    "Blok `default` dengan `const _lengkap: never = b;` adalah",
                    "idiom yang layak dihafal. Ia bekerja karena: kalau semua",
                    "cabang sudah tertangani, tipe `b` di situ menyempit jadi",
                    "`never`, dan `never` boleh ditugaskan ke `never`. Begitu",
                    "ada anggota baru, tipenya bukan `never` lagi dan",
                    "penugasannya ditolak.",
                    "",
                    "`Record<Taraf, string>` menuntut SEMUA anggota union",
                    "punya entri. Melupakan satu adalah error kompilasi —",
                    "cara lain mendapat kelengkapan yang diperiksa.",
                    "",
                    "Kapan memakai literal union dan kapan enum:",
                    "  literal union   hampir selalu. Ia hilang saat",
                    "                  kompilasi dan langsung cocok dengan",
                    "                  string dari JSON.",
                    "  enum            kalau kamu butuh nilainya ada di",
                    "                  runtime atau perlu penomoran otomatis.",
                    "  const enum      HINDARI: ia bermasalah dengan bundler",
                    "                  dan isolatedModules.",
                ]
            },
        ],
    },
    {
        "title": "4. Interface & Type Alias",
        "sections": [
            {
                "body": [
                    "Dua cara menamai bentuk, dan keduanya hampir sama:",
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
                    "PERBEDAAN yang benar-benar berarti:",
                    "",
                    "  interface  bisa DIGABUNG: dua deklarasi dengan nama",
                    "             sama otomatis menyatu. Ini yang membuat",
                    "             pustaka bisa memperluas tipe bawaan.",
                    "  type       bisa menamai APA PUN: union, tuple,",
                    "             primitif, tipe terhitung. Interface tidak.",
                    "",
                    "Aturan praktis yang dipakai banyak proyek:",
                    "  - Pakai `interface` untuk bentuk objek dan kontrak",
                    "    yang mungkin diperluas.",
                    "  - Pakai `type` untuk union, tuple, dan apa pun yang",
                    "    bukan objek polos.",
                    "  - Jangan habiskan waktu memperdebatkannya; yang",
                    "    penting konsisten dalam satu proyek.",
                    "",
                    "MEMPERLUAS:",
                    "  interface Guru extends Murid { mapel: string }",
                    "  type Guru = Murid & { mapel: string };",
                    "",
                    "Tanda `&` disebut INTERSECTION: gabungan semua",
                    "propertinya sekaligus.",
                    "",
                    "Interface juga bisa mendeskripsikan FUNGSI dan INDEKS:",
                    "",
                    "  interface Pembanding {",
                    "      (a: number, b: number): number;    dipanggil",
                    "  }",
                    "",
                    "  interface Kamus {",
                    "      [kunci: string]: number;           index signature",
                    "  }",
                    "",
                    "EXCESS PROPERTY CHECK — jebakan yang sering bikin",
                    "bingung: OBJEK LITERAL yang langsung ditugaskan ditolak",
                    "kalau punya properti tambahan, tapi objek lewat variabel",
                    "TIDAK ditolak:",
                    "",
                    "  const m: Murid = { nama: \"a\", nilai: 1, x: 2 };  ERROR",
                    "  const t = { nama: \"a\", nilai: 1, x: 2 };",
                    "  const m: Murid = t;                             lolos",
                    "",
                    "Ini disengaja: pemeriksaan ketat pada literal menangkap",
                    "salah ketik nama properti, sementara sisanya memakai",
                    "aturan kecocokan bentuk yang lebih longgar.",
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
                    "`function adalahGuru(o: Orang): o is Guru` memakai",
                    "PREDIKAT TIPE. Tipe kembaliannya bukan `boolean`",
                    "melainkan `o is Guru`, dan itu memberi tahu compiler:",
                    "'kalau fungsi ini mengembalikan true, perlakukan o",
                    "sebagai Guru sejak titik itu'.",
                    "",
                    "Tanpa predikat tipe, `adalahGuru(o)` cuma mengembalikan",
                    "boolean dan `o.mapel` sesudahnya tetap ditolak compiler.",
                    "",
                    "PERINGATAN: predikat tipe adalah JANJI yang TIDAK",
                    "diperiksa. Kalau isinya salah — misalnya selalu",
                    "mengembalikan true — compiler akan mempercayainya dan",
                    "kamu kehilangan seluruh jaminannya. Tulis isinya dengan",
                    "hati-hati.",
                    "",
                    "`b[1] - a[1] || a[0].localeCompare(b[0])` adalah idiom",
                    "pengurutan dua tingkat di JavaScript: kalau selisih",
                    "pertamanya nol (falsy), pakai pembanding kedua.",
                    "",
                    "Satu catatan tentang index signature: dengan setelan",
                    "`noUncheckedIndexedAccess` dinyalakan, `hitung[k]`",
                    "bertipe `number | undefined` — yang lebih jujur, karena",
                    "kuncinya memang mungkin tidak ada. Setelan itu tidak",
                    "termasuk `strict` dan layak dinyalakan sendiri.",
                ]
            },
        ],
    },
    {
        "title": "5. Fungsi & Tipe Fungsi",
        "sections": [
            {
                "body": [
                    "Bentuk fungsi:",
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
                    "Bentuk ketiga menunjukkan TIPE FUNGSI: `(a: A, b: B) => C`.",
                    "Perhatikan panahnya — di posisi tipe, panah berarti",
                    "'mengembalikan', bukan arrow function.",
                    "",
                    "Parameter:",
                    "  a: number            wajib",
                    "  b?: number           OPSIONAL, bertipe number|undefined",
                    "  c: number = 10       bawaan; otomatis opsional",
                    "  ...sisa: number[]    rest, harus yang terakhir",
                    "",
                    "Parameter opsional HARUS sesudah yang wajib.",
                    "",
                    "TIPE KEMBALIAN biasanya boleh disimpulkan, TAPI",
                    "menuliskannya di fungsi publik punya nilai: ia menangkap",
                    "kesalahan DI DALAM fungsinya alih-alih di tempat",
                    "pemakaiannya, dan pesan errornya jauh lebih jelas.",
                    "",
                    "  void    tidak mengembalikan apa-apa",
                    "  never   tidak pernah selesai normal (selalu melempar",
                    "          atau perulangan abadi)",
                    "",
                    "OVERLOAD — satu implementasi, beberapa tanda tangan:",
                    "",
                    "  function cari(id: number): Murid | undefined;",
                    "  function cari(nama: string): Murid[] ;",
                    "  function cari(x: number | string): unknown { ... }",
                    "",
                    "Tanda tangan implementasinya TIDAK ikut terlihat dari",
                    "luar. Dalam praktik, union sering lebih sederhana",
                    "daripada overload — pakai overload hanya kalau tipe",
                    "kembaliannya benar-benar bergantung tipe masukannya.",
                    "",
                    "`this` di dalam fungsi bisa diberi tipe lewat parameter",
                    "pertama semu bernama `this`, yang dihapus saat kompilasi:",
                    "  function f(this: HTMLElement, x: number) { ... }",
                    "",
                    "Arrow function TIDAK punya `this` sendiri — ia memakai",
                    "`this` dari lingkungan tempat ia ditulis. Itu sebabnya",
                    "arrow function jauh lebih aman untuk callback.",
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
                    "Bagian yang paling penting di contoh itu adalah blok",
                    "terakhir:",
                    "",
                    "  catch (e) {",
                    "      e instanceof Error ? e.message : String(e)",
                    "  }",
                    "",
                    "Di TypeScript modern, variabel di `catch` bertipe",
                    "`unknown`, BUKAN `Error`. Alasannya jujur: di JavaScript,",
                    "`throw` boleh melempar APA PUN — angka, string, objek",
                    "polos. Tidak ada jaminan bahwa yang tertangkap punya",
                    "properti `.message`.",
                    "",
                    "Karena itu setiap blok catch di TypeScript ketat harus",
                    "memeriksa dulu sebelum membaca pesannya. Ini terasa",
                    "merepotkan di awal, dan ia menangkap kelas bug yang",
                    "nyata.",
                    "",
                    "(Setelan `useUnknownInCatchVariables` mengendalikannya,",
                    "dan ia sudah termasuk di dalam `strict`.)",
                    "",
                    "`never` sebagai tipe kembalian `gagal` juga berguna di",
                    "luar dugaan: karena fungsi itu tidak pernah kembali,",
                    "compiler tahu kode sesudah pemanggilannya tidak akan",
                    "pernah tercapai. Itu membuat `const x = a ?? gagal(...)`",
                    "bertipe non-null tanpa cast apa pun.",
                ]
            },
        ],
    },
    {
        "title": "6. Generic",
        "sections": [
            {
                "body": [
                    "Generic membuat satu potong kode bekerja untuk banyak",
                    "tipe tanpa kehilangan informasi tipenya.",
                    "",
                    "  function pertama<T>(daftar: T[]): T | undefined {",
                    "      return daftar[0];",
                    "  }",
                    "",
                    "  pertama([1, 2, 3])        -> number | undefined",
                    "  pertama([\"a\", \"b\"])       -> string | undefined",
                    "",
                    "Bandingkan dengan versi `any`: ia juga menerima apa pun,",
                    "tapi hasilnya `any` juga — dan seluruh informasi tipenya",
                    "hilang sejak saat itu.",
                    "",
                    "BATASAN dengan `extends`:",
                    "",
                    "  function panjang<T extends { length: number }>(x: T) {",
                    "      return x.length;",
                    "  }",
                    "",
                    "  panjang(\"halo\")      boleh",
                    "  panjang([1, 2])      boleh",
                    "  panjang(42)          ERROR: number tidak punya length",
                    "",
                    "`keyof` menghasilkan union dari nama-nama propertinya:",
                    "",
                    "  type Kunci = keyof Murid;    \"nama\" | \"nilai\"",
                    "",
                    "  function ambil<T, K extends keyof T>(o: T, k: K): T[K] {",
                    "      return o[k];",
                    "  }",
                    "",
                    "  ambil(murid, \"nama\")    -> string, BUKAN any",
                    "  ambil(murid, \"xyz\")     -> ERROR saat kompilasi",
                    "",
                    "Ini salah satu hal yang tidak bisa ditiru bahasa dinamis",
                    "mana pun: tipe hasilnya BERGANTUNG pada nilai argumen",
                    "yang kamu tulis.",
                    "",
                    "UTILITY TYPE bawaan yang paling sering dipakai:",
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
                    "Semuanya ditulis memakai fitur yang sama yang tersedia",
                    "untukmu: mapped type dan conditional type.",
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
                    "`ambil(m, \"nama\")` mengembalikan `string`, sedangkan",
                    "`ambil(m, \"nilai\")` mengembalikan `number` — dari SATU",
                    "fungsi yang sama. Yang menentukannya adalah literal",
                    "string yang kamu tulis di pemanggilan.",
                    "",
                    "Ini bukan kecanggihan tanpa guna. Fungsi seperti ini",
                    "ada di mana-mana di kode nyata: pengambil konfigurasi,",
                    "pembangun query, dan pengurut berdasarkan nama kolom.",
                    "Tanpa generic, semuanya akan mengembalikan `any`.",
                    "",
                    "`{ ...asal, ...tambalan }` adalah SPREAD: menyalin semua",
                    "properti, dengan yang belakangan menimpa yang di depan.",
                    "Ini cara idiomatis membuat salinan-dengan-perubahan di",
                    "JavaScript, setara `copy()` di Kotlin dan `with` di C#.",
                    "",
                    "Perhatikan ia SALINAN DANGKAL: properti yang berupa",
                    "objek tetap ditunjuk bersama. Untuk salinan dalam,",
                    "`structuredClone(x)` tersedia di Node 17+ dan browser",
                    "modern.",
                ]
            },
        ],
    },
    {
        "title": "7. Class & Modifier Akses",
        "sections": [
            {
                "body": [
                    "Class di TypeScript adalah class JavaScript ditambah",
                    "anotasi tipe dan modifier akses.",
                    "",
                    "  class Murid {",
                    "      constructor(",
                    "          public readonly nama: string,",
                    "          private nilai: number,",
                    "      ) {}",
                    "  }",
                    "",
                    "PARAMETER PROPERTY: menulis `public`, `private`, atau",
                    "`readonly` di parameter constructor sekaligus",
                    "MENDEKLARASIKAN dan MENGISI propertinya. Ini fitur",
                    "TypeScript, bukan JavaScript.",
                    "",
                    "Modifier akses:",
                    "  public     bawaan; siapa pun boleh",
                    "  protected  class ini dan turunannya",
                    "  private    hanya class ini",
                    "  readonly   tidak bisa diubah sesudah constructor",
                    "",
                    "PERINGATAN PENTING: `private` di TypeScript HILANG saat",
                    "kompilasi. Ia cuma pemeriksaan compiler; di JavaScript",
                    "hasilnya properti biasa yang bisa diakses siapa pun.",
                    "",
                    "Untuk privasi SUNGGUHAN yang bertahan di runtime, pakai",
                    "PRIVATE FIELD JavaScript dengan tanda pagar:",
                    "",
                    "  class Murid {",
                    "      #nilai: number;          benar-benar privat",
                    "  }",
                    "",
                    "Mengaksesnya dari luar adalah error SINTAKS di",
                    "JavaScript, bukan sekadar keberatan compiler.",
                    "",
                    "GETTER dan SETTER:",
                    "  get grade(): string { ... }",
                    "  set nilai(n: number) { ... }",
                    "",
                    "Keduanya dipakai TANPA tanda kurung: `m.grade`.",
                    "",
                    "PEWARISAN dan INTERFACE:",
                    "  class Kucing extends Hewan implements Berbunyi { }",
                    "",
                    "`abstract` menandai class yang tidak bisa di-new dan",
                    "method yang wajib diisi turunannya.",
                    "",
                    "`static` untuk anggota milik class, bukan objek.",
                    "",
                    "`override` (sejak TS 4.3) menandai method yang menimpa",
                    "induknya. Dengan setelan `noImplicitOverride`, ia jadi",
                    "WAJIB — dan itu layak dinyalakan, karena tanpa itu",
                    "salah ketik nama method diam-diam membuat method baru",
                    "alih-alih menimpa yang lama.",
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
                "body": [
                    "Empat hal yang layak diperhatikan:",
                    "",
                    "  1. `#saldo` dan `static #urutan` memakai private field",
                    "     JavaScript, bukan `private` TypeScript. Bedanya",
                    "     nyata: `private` hilang saat kompilasi, sedangkan",
                    "     `#` bertahan dan mengaksesnya dari luar adalah",
                    "     error sintaks.",
                    "",
                    "  2. `get saldo()` memberi akses BACA tanpa memberi",
                    "     akses ubah. Dipakai tanpa tanda kurung: `a.saldo`.",
                    "",
                    "  3. `setor` mengembalikan `this` dengan tipe `this`,",
                    "     bukan `Rekening`. Bedanya penting untuk pewarisan:",
                    "     dengan tipe `this`, turunan yang memanggil `setor`",
                    "     tetap mendapat tipe turunannya, bukan induknya.",
                    "",
                    "  4. `protected constructor` mencegah `new BangunDasar()`",
                    "     dari luar, tapi tetap memperbolehkan turunannya",
                    "     memanggil `super()`.",
                    "",
                    "Setelan tsconfig yang layak dinyalakan bersama `strict`:",
                    "",
                    "  noImplicitOverride            wajibkan kata `override`",
                    "  useDefineForClassFields       semantik field standar",
                    "  exactOptionalPropertyTypes    bedakan 'tidak ada' dari",
                    "                                'ada tapi undefined'",
                    "  noUncheckedIndexedAccess      arr[i] jadi T | undefined",
                    "",
                    "Yang terakhir itu paling sering diabaikan padahal paling",
                    "berguna: tanpa itu, `arr[999]` bertipe `T` padahal",
                    "nilainya `undefined` — dan itu persis sumber kesalahan",
                    "'cannot read property of undefined' yang paling sering",
                    "di JavaScript.",
                ]
            },
        ],
    },
    {
        "title": "8. Modul: import & export",
        "sections": [
            {
                "body": [
                    "TypeScript memakai sistem modul ES:",
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
                    "PERHATIKAN `.js` di dalam import, padahal berkasnya",
                    "`.ts`. Itu bukan salah ketik: dengan modul ES, yang",
                    "diimpor adalah berkas HASIL kompilasi. Aturannya",
                    "bergantung setelan `moduleResolution`, dan ini salah",
                    "satu sumber kebingungan terbesar bagi pendatang baru.",
                    "",
                    "Aturan praktis untuk proyek baru di Node:",
                    "  \"module\": \"nodenext\"",
                    "  \"moduleResolution\": \"nodenext\"",
                    "  tulis ekstensi `.js` di setiap import relatif",
                    "",
                    "IMPORT KHUSUS TIPE — penting dan sering dilupakan:",
                    "",
                    "  import type { Murid } from \"./murid.js\";",
                    "  import { type Murid, grade } from \"./murid.js\";",
                    "",
                    "Impor bertanda `type` DIHAPUS sepenuhnya saat kompilasi.",
                    "Tanpa itu, bundler bisa menyertakan seluruh berkas hanya",
                    "karena kamu mengimpor sebuah interface darinya.",
                    "",
                    "Setelan `verbatimModuleSyntax` memaksa pemakaian",
                    "`import type` di tempat yang memerlukannya, dan itu",
                    "layak dinyalakan.",
                    "",
                    "EXPORT DEFAULT versus NAMED:",
                    "  - Named export lebih baik untuk hampir semua kasus:",
                    "    namanya konsisten, autocomplete bekerja, dan refactor",
                    "    rename menyentuh semua tempat.",
                    "  - Default export membuat setiap pengimpor bebas",
                    "    menamainya sendiri, dan itu justru sumber",
                    "    ketidakkonsistenan.",
                    "",
                    "BERKAS DEKLARASI `.d.ts` berisi tipe TANPA implementasi.",
                    "Ia dipakai untuk memberi tipe pada pustaka JavaScript",
                    "yang tidak punya tipe sendiri. Sebagian besar pustaka",
                    "populer punya paket `@types/nama` di npm.",
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
                "body": [
                    "Setelan yang paling menentukan, satu per satu:",
                    "",
                    "  strict          Menyalakan tujuh pemeriksaan sekaligus,",
                    "                  termasuk strictNullChecks yang membuat",
                    "                  null harus dinyatakan. TANPA INI,",
                    "                  separuh gunanya TypeScript hilang.",
                    "",
                    "  noUncheckedIndexedAccess",
                    "                  `arr[i]` jadi `T | undefined`. Lebih",
                    "                  jujur, dan menangkap kelas bug 'cannot",
                    "                  read property of undefined'.",
                    "",
                    "  target          Versi JavaScript hasil kompilasi.",
                    "                  es2022 aman untuk Node 18+.",
                    "",
                    "  skipLibCheck    Melewati pemeriksaan berkas .d.ts milik",
                    "                  dependensi. Hampir semua proyek",
                    "                  menyalakannya: tanpa itu, satu",
                    "                  dependensi yang tipenya bermasalah",
                    "                  menggagalkan seluruh build-mu.",
                    "",
                    "  declaration     Menghasilkan berkas .d.ts. Wajib kalau",
                    "                  kamu menerbitkan pustaka.",
                    "",
                    "  forceConsistentCasingInFileNames",
                    "                  Menangkap `./Murid` versus `./murid`,",
                    "                  yang jalan di macOS dan Windows lalu",
                    "                  gagal di server Linux.",
                    "",
                    "Yang SEBAIKNYA TIDAK dipakai di proyek baru:",
                    "  \"noImplicitAny\": false     mematikan inti fiturnya",
                    "  \"allowJs\" tanpa alasan     mencampur dua dunia",
                    "  \"const enum\"               bermasalah dengan bundler",
                    "",
                    "Untuk proyek yang mewarisi kode JavaScript lama,",
                    "`allowJs` beserta `checkJs` justru jalan masuk yang",
                    "baik: TypeScript bisa memeriksa berkas .js yang ada",
                    "sebelum kamu mengonversinya satu per satu.",
                ]
            },
        ],
    },
    {
        "title": "9. Async, Promise & await",
        "sections": [
            {
                "body": [
                    "JavaScript berjalan di SATU thread. Semua pekerjaan yang",
                    "menunggu — jaringan, berkas, timer — harus asinkron,",
                    "kalau tidak seluruh program membeku.",
                    "",
                    "PROMISE adalah janji sebuah nilai yang belum ada:",
                    "",
                    "  const p: Promise<string> = ambilData();",
                    "  p.then((x) => ...).catch((e) => ...).finally(() => ...);",
                    "",
                    "ASYNC/AWAIT adalah cara menulis yang sama tanpa rantai:",
                    "",
                    "  async function proses(): Promise<string> {",
                    "      const data = await ambilData();",
                    "      return data.toUpperCase();",
                    "  }",
                    "",
                    "Fungsi `async` SELALU mengembalikan Promise, bahkan",
                    "kalau kamu menulis `return 5`. Tipe kembaliannya",
                    "`Promise<number>`, bukan `number`.",
                    "",
                    "`await` hanya boleh di dalam fungsi async — atau di",
                    "level atas modul ES (top-level await).",
                    "",
                    "BERURUTAN versus BERSAMAAN — kesalahan paling mahal:",
                    "",
                    "  // BERURUTAN: 2 detik",
                    "  const a = await ambilA();",
                    "  const b = await ambilB();",
                    "",
                    "  // BERSAMAAN: 1 detik",
                    "  const [a, b] = await Promise.all([ambilA(), ambilB()]);",
                    "",
                    "Kuncinya: `await` di setiap baris memaksa yang kedua",
                    "menunggu yang pertama selesai, padahal keduanya tidak",
                    "saling bergantung.",
                    "",
                    "Empat penggabung Promise, dan bedanya penting:",
                    "  Promise.all        semua berhasil; GAGAL kalau satu gagal",
                    "  Promise.allSettled semua selesai; laporkan masing-masing",
                    "  Promise.race       yang PERTAMA selesai, berhasil atau gagal",
                    "  Promise.any        yang pertama BERHASIL",
                    "",
                    "`allSettled` yang biasanya kamu mau saat memanggil",
                    "banyak layanan: satu yang mati tidak boleh membatalkan",
                    "hasil yang lain.",
                    "",
                    "PENANGANAN GALAT memakai try/catch biasa:",
                    "  try { await f(); } catch (e) { ... }",
                    "",
                    "PERINGATAN: Promise yang tidak di-await dan tidak",
                    "di-catch menghasilkan unhandled rejection. Di Node",
                    "modern, itu MENJATUHKAN proses. Kalau kamu sengaja",
                    "tidak menunggu, tulis `void f()` atau pasang `.catch()`.",
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
                    "Blok terakhir menunjukkan pola yang paling sering salah",
                    "di kode nyata:",
                    "",
                    "  // SALAH: 400 ms, satu per satu",
                    "  for (const n of nama) { await proses(n); }",
                    "",
                    "  // BENAR: 100 ms, semuanya bersamaan",
                    "  await Promise.all(nama.map((n) => proses(n)));",
                    "",
                    "Perulangan `for await` memang kadang BENAR — misalnya",
                    "saat kamu sengaja membatasi beban ke server, atau saat",
                    "tiap langkah bergantung pada hasil sebelumnya. Yang",
                    "salah adalah memakainya tanpa sadar.",
                    "",
                    "Untuk membatasi berapa yang berjalan bersamaan, pustaka",
                    "seperti `p-limit` menyediakan kolam terbatas.",
                    "",
                    "`s.status === \"fulfilled\"` adalah discriminated union",
                    "lagi: di dalam cabang itu, TypeScript tahu `s.value`",
                    "tersedia; di cabang lain ia tahu yang tersedia `s.reason`.",
                    "Pola yang sama muncul di seluruh API modern.",
                ]
            },
        ],
    },
    {
        "title": "10. Tipe Lanjut",
        "sections": [
            {
                "body": [
                    "Bagian ini yang membuat sistem tipe TypeScript disebut",
                    "salah satu yang paling ekspresif di antara bahasa arus",
                    "utama.",
                    "",
                    "CONDITIONAL TYPE — tipe yang bercabang:",
                    "",
                    "  type Kalau<T> = T extends string ? \"teks\" : \"bukan\";",
                    "  Kalau<\"a\">     -> \"teks\"",
                    "  Kalau<5>       -> \"bukan\"",
                    "",
                    "  type Kupas<T> = T extends Array<infer U> ? U : T;",
                    "  Kupas<number[]>  -> number",
                    "",
                    "`infer U` menangkap bagian dari tipenya untuk dipakai",
                    "di cabang benarnya. Inilah yang dipakai `ReturnType` dan",
                    "`Awaited` di pustaka standar.",
                    "",
                    "MAPPED TYPE — mengubah setiap properti:",
                    "",
                    "  type Semua<T> = { [K in keyof T]: T[K] };",
                    "  type Opsional<T> = { [K in keyof T]?: T[K] };",
                    "  type Beku<T> = { readonly [K in keyof T]: T[K] };",
                    "  type Buang<T> = { -readonly [K in keyof T]-?: T[K] };",
                    "",
                    "Tanda minus MENGHAPUS penanda. `-?` membuang opsional,",
                    "`-readonly` membuang readonly. Itulah cara `Required`",
                    "dan salah satu bagian `Mutable` bekerja.",
                    "",
                    "TEMPLATE LITERAL TYPE — menyusun tipe string:",
                    "",
                    "  type Peristiwa = `on${Capitalize<\"klik\" | \"geser\">}`;",
                    "  // \"onKlik\" | \"onGeser\"",
                    "",
                    "  type Rute = `/api/${string}`;",
                    "",
                    "Ada empat pembantu bawaan: Uppercase, Lowercase,",
                    "Capitalize, Uncapitalize.",
                    "",
                    "SATISFIES (TS 4.9) — memeriksa TANPA melebarkan:",
                    "",
                    "  const warna = {",
                    "      merah: \"#f00\",",
                    "      biru: \"#00f\",",
                    "  } satisfies Record<string, string>;",
                    "",
                    "  warna.merah      tipenya \"#f00\", bukan string",
                    "",
                    "Dengan anotasi `: Record<string, string>` biasa, tipe",
                    "tiap nilainya melebar jadi `string` dan kamu kehilangan",
                    "literalnya. `satisfies` memeriksa kecocokan sambil",
                    "MEMPERTAHANKAN tipe sempitnya.",
                    "",
                    "Aturan praktis soal semua ini: jangan memakainya karena",
                    "bisa. Tipe yang sangat pintar sering jadi tipe yang",
                    "pesan errornya mustahil dibaca. Pakai saat ia benar-benar",
                    "menghapus pengulangan atau menutup celah nyata.",
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
                    "`Berawalan<T, P>` memakai KEY REMAPPING dengan klausa",
                    "`as`: setiap nama properti diubah jadi nama baru yang",
                    "disusun dari template literal. Dari dua properti `nama`",
                    "dan `nilai`, ia menghasilkan `getNama` dan `getNilai` —",
                    "tanpa satu pun nama diketik dua kali.",
                    "",
                    "Pola ini dipakai pustaka sungguhan untuk menghasilkan",
                    "tipe getter, tipe event handler, dan tipe kolom",
                    "database dari satu definisi.",
                    "",
                    "`satisfies` adalah tambahan yang sangat berguna dan",
                    "sering belum dikenal. Bandingkan:",
                    "",
                    "  const a: Record<string, string> = { merah: \"#f00\" };",
                    "  a.merah          -> string        (melebar)",
                    "",
                    "  const b = { merah: \"#f00\" } satisfies Record<string, string>;",
                    "  b.merah          -> \"#f00\"        (tetap sempit)",
                    "",
                    "Keduanya memeriksa kecocokan. Hanya yang kedua yang",
                    "mempertahankan informasi tipenya, dan itu sering persis",
                    "yang kamu butuhkan untuk konfigurasi dan konstanta.",
                    "",
                    "Peringatan yang layak diulang: tipe seperti ini membuat",
                    "pesan error jadi jauh lebih panjang saat ada yang salah.",
                    "Kalau sebuah tipe pintar menghemat lima baris tapi",
                    "membuat pesan errornya tiga puluh baris, ia belum tentu",
                    "menang.",
                ]
            },
        ],
    },
    {
        "title": "11. Enum, const & Readonly",
        "sections": [
            {
                "body": [
                    "ENUM adalah satu-satunya fitur TypeScript yang",
                    "menghasilkan KODE SUNGGUHAN di JavaScript. Semua fitur",
                    "tipe lainnya hilang saat kompilasi; enum tidak.",
                    "",
                    "  enum Arah { Utara, Timur, Selatan, Barat }",
                    "  enum Status { Draf = \"draf\", Terbit = \"terbit\" }",
                    "",
                    "Enum numerik punya perilaku yang sering mengejutkan:",
                    "ia REVERSE-MAPPED, artinya `Arah[0]` memberi `\"Utara\"`.",
                    "Enum string tidak begitu.",
                    "",
                    "Enum numerik juga menerima angka apa pun secara historis",
                    "— `const a: Arah = 99` diterima di TypeScript lama.",
                    "Itu sudah diperketat, tapi enum string tetap lebih aman.",
                    "",
                    "ALTERNATIF yang lebih disukai kode modern: union literal",
                    "plus objek `as const`.",
                    "",
                    "  const Arah = {",
                    "      Utara: \"utara\",",
                    "      Timur: \"timur\",",
                    "  } as const;",
                    "",
                    "  type Arah = typeof Arah[keyof typeof Arah];",
                    "",
                    "Keunggulannya: tidak ada kode yang dihasilkan, nilainya",
                    "langsung cocok dengan string dari JSON, dan bundler",
                    "bisa membuangnya kalau tidak dipakai.",
                    "",
                    "`as const` disebut CONST ASSERTION, dan ia melakukan",
                    "tiga hal sekaligus:",
                    "  - setiap properti jadi `readonly`",
                    "  - setiap nilai literal TIDAK melebar (\"a\" tetap \"a\",",
                    "    bukan string)",
                    "  - array jadi readonly tuple",
                    "",
                    "  const a = [1, 2, 3];              number[]",
                    "  const b = [1, 2, 3] as const;     readonly [1, 2, 3]",
                    "",
                    "READONLY di berbagai tempat:",
                    "  readonly nama: string             properti",
                    "  readonly number[]                 array",
                    "  ReadonlyArray<number>             sama",
                    "  Readonly<T>                       seluruh objek",
                    "  ReadonlyMap / ReadonlySet",
                    "",
                    "Sama seperti `private`, semua `readonly` HILANG saat",
                    "kompilasi. Ia mencegah kamu menulis kode yang mengubah,",
                    "bukan mencegah perubahan saat program jalan. Untuk itu",
                    "ada `Object.freeze()`, yang bekerja sungguhan.",
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
                    "Blok terakhir menunjukkan perbedaan yang paling penting",
                    "di materi ini: `readonly` hilang saat kompilasi,",
                    "`Object.freeze` tidak. Yang pertama mencegah kamu",
                    "MENULIS kode yang mengubah; yang kedua mencegah",
                    "perubahannya BENAR-BENAR terjadi.",
                    "",
                    "Untuk data yang datang dari luar dan tidak boleh diubah",
                    "siapa pun, `Object.freeze` yang kamu butuhkan.",
                    "",
                    "`type Taraf = (typeof Taraf)[keyof typeof Taraf]` layak",
                    "dibaca pelan-pelan:",
                    "  typeof Taraf            tipe OBJEKNYA",
                    "  keyof typeof Taraf      \"Info\"|\"Peringatan\"|\"Galat\"",
                    "  (typeof Taraf)[...]     nilai di kunci-kunci itu",
                    "                          -> \"info\"|\"peringatan\"|\"galat\"",
                    "",
                    "Pola ini sangat lazim dan layak dihafal bentuknya. Ia",
                    "memberi kamu satu sumber kebenaran: daftar nilainya",
                    "ditulis SEKALI, dan tipenya diturunkan darinya.",
                    "",
                    "Perhatikan juga nama `Taraf` dipakai untuk KONSTANTA dan",
                    "TIPE sekaligus. TypeScript memperbolehkannya karena tipe",
                    "dan nilai hidup di ruang nama yang terpisah — kebiasaan",
                    "yang dipakai luas dan membuat kodenya lebih ringkas.",
                ]
            },
        ],
    },
    {
        "title": "12. Data dari Luar: Tipe Bukan Jaminan",
        "sections": [
            {
                "body": [
                    "Ini materi terpenting di seluruh kurikulum TypeScript,",
                    "dan ia mengulang kalimat dari materi pertama:",
                    "",
                    "  TIPE HILANG SAAT PROGRAM JALAN.",
                    "",
                    "Akibat praktisnya, dan ini sering baru disadari setelah",
                    "sebuah bug produksi:",
                    "",
                    "  const data: Murid = await res.json();",
                    "",
                    "Baris itu TIDAK MEMERIKSA APA PUN. `res.json()`",
                    "mengembalikan `any`, dan anotasi `: Murid` cuma",
                    "memberitahu compiler untuk mempercayaimu. Kalau server",
                    "mengirim bentuk yang berbeda, program berjalan terus",
                    "sampai meledak di tempat yang jauh dari penyebabnya.",
                    "",
                    "Hal yang sama berlaku untuk:",
                    "  JSON.parse(teks) as Murid",
                    "  process.env.PORT as number",
                    "  localStorage.getItem(...) as Setelan",
                    "  hasil query database",
                    "",
                    "TIGA CARA menanganinya, dari yang paling ringan:",
                    "",
                    "  1. TYPE GUARD tulis tangan",
                    "     function adalahMurid(x: unknown): x is Murid { ... }",
                    "",
                    "  2. ASSERTION FUNCTION",
                    "     function pastikanMurid(x: unknown): asserts x is Murid",
                    "",
                    "  3. PUSTAKA VALIDASI SKEMA",
                    "     Zod, Valibot, ArkType, io-ts",
                    "",
                    "Yang ketiga yang dipakai proyek sungguhan, dan alasannya",
                    "kuat: skemanya menjadi SATU sumber kebenaran — tipe",
                    "TypeScript-nya diturunkan dari skema itu, sehingga",
                    "keduanya mustahil melenceng.",
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
                    "ATURAN PRAKTIS: validasi di BATAS sistem. Begitu data",
                    "masuk lewat jaringan, berkas, atau masukan pengguna,",
                    "periksa sekali di situ. Sesudah itu seluruh kode di",
                    "dalam boleh mempercayai tipenya.",
                    "",
                    "`as` (type assertion) juga bukan konversi. `x as Murid`",
                    "tidak mengubah apa pun saat program jalan; ia cuma",
                    "mematikan keberatan compiler. Setiap `as` adalah janji",
                    "yang tidak diperiksa.",
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
                    "Baris `as tanpa periksa` adalah seluruh inti materi ini.",
                    "Kodenya dikompilasi tanpa satu pun keluhan, `palsu`",
                    "bertipe `Murid` menurut compiler, dan `palsu.nilai`",
                    "ternyata `undefined`. Tidak ada yang salah menurut",
                    "TypeScript; yang salah adalah janjinya.",
                    "",
                    "Perhatikan `asserts x is Murid` sebagai tipe kembalian:",
                    "ia memberi tahu compiler 'kalau fungsi ini kembali tanpa",
                    "melempar, perlakukan x sebagai Murid sejak titik itu'.",
                    "Itu sebabnya `kandidat.nama` sesudah pemanggilan tidak",
                    "lagi ditolak, padahal `kandidat` dideklarasikan",
                    "`unknown`.",
                    "",
                    "Assertion function punya satu syarat yang mudah",
                    "terlupa: variabelnya harus dideklarasikan dengan tipe",
                    "eksplisit atau `const`, dan fungsinya harus dirujuk",
                    "lewat nama — bukan lewat properti objek.",
                    "",
                    "Di proyek nyata, tulis skemanya SEKALI dengan Zod lalu",
                    "turunkan tipenya. Menulis type guard tangan untuk",
                    "sepuluh bentuk data adalah pekerjaan yang membosankan",
                    "dan gampang tertinggal saat bentuknya berubah — dan",
                    "type guard yang tertinggal jauh lebih berbahaya daripada",
                    "tidak ada sama sekali, karena ia memberi rasa aman palsu.",
                ]
            },
        ],
    },
    {
        "title": "13. Pengujian",
        "sections": [
            {
                "body": [
                    "Kerangka tes yang lazim untuk TypeScript:",
                    "",
                    "  Vitest    paling umum di proyek baru; cepat, mengerti",
                    "            TypeScript tanpa konfigurasi tambahan",
                    "  Jest      matang, ekosistem besar, butuh ts-jest atau",
                    "            SWC untuk TypeScript",
                    "  node:test Bawaan Node 18+, tanpa dependensi apa pun",
                    "",
                    "Bentuk tesnya hampir identik di ketiganya:",
                    "",
                    "  import { describe, it, expect } from \"vitest\";",
                    "",
                    "  describe(\"grade\", () => {",
                    "      it(\"memberi A tepat di 85\", () => {",
                    "          expect(grade(85)).toBe(\"A\");",
                    "      });",
                    "  });",
                    "",
                    "Matcher yang paling sering dipakai:",
                    "  toBe(x)                  sama persis (Object.is)",
                    "  toEqual(x)               sama isinya, dalam",
                    "  toStrictEqual(x)         sama isinya DAN tipenya",
                    "  toBeCloseTo(x, digit)    untuk pecahan",
                    "  toBeNull / toBeUndefined / toBeDefined",
                    "  toContain(x)             untuk array dan string",
                    "  toHaveLength(n)",
                    "  toThrow(/pola/)",
                    "  resolves / rejects       untuk Promise",
                    "",
                    "PILIH toBe UNTUK PRIMITIF, toEqual UNTUK OBJEK.",
                    "`toBe` pada dua objek berbeda selalu gagal meski isinya",
                    "sama, karena ia membandingkan identitas.",
                    "",
                    "Untuk pecahan, `toBeCloseTo` wajib: `0.1 + 0.2` tidak",
                    "pernah persis `0.3` di aritmetika IEEE 754.",
                    "",
                    "Siklus hidup:",
                    "  beforeEach / afterEach   sebelum dan sesudah TIAP tes",
                    "  beforeAll / afterAll     sekali untuk seluruh berkas",
                    "",
                    "`beforeEach` penting: ia membuat tiap tes mulai dari",
                    "keadaan yang sama. Tes yang bergantung pada urutan",
                    "menjalankannya adalah tes yang suatu hari gagal tanpa",
                    "ada yang mengubah apa pun.",
                    "",
                    "MENGUJI DI BATAS adalah kebiasaan paling berharga: uji",
                    "85 dan 84, bukan 90 dan 50. Di batas itulah",
                    "lebih-besar-sama-dengan salah ketik.",
                    "",
                    "MENGUJI TIPE juga mungkin, dan berguna untuk pustaka:",
                    "  expectTypeOf(f).returns.toEqualTypeOf<string>()",
                    "  // @ts-expect-error   menandai baris yang HARUS gagal",
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
                "body": [
                    "Perhatikan nilai yang dipilih: 85 dan 84, 75 dan 74,",
                    "60 dan 59. Menguji tepat di batas jauh lebih berharga",
                    "daripada menguji nilai di tengah rentang, yang hampir",
                    "tidak pernah menemukan bug.",
                    "",
                    "`it.each([...])` menjalankan tes yang sama dengan banyak",
                    "data, dan nama tesnya ikut berisi datanya — sehingga",
                    "saat satu kasus gagal, kamu langsung tahu yang mana.",
                    "",
                    "`toEqual(['Andi', 'Cici'])` memakai perbandingan ISI.",
                    "Dengan `toBe`, tesnya selalu gagal karena dua array",
                    "berbeda tidak pernah identik meski isinya sama.",
                    "",
                    "`toBeCloseTo(85, 5)` memakai toleransi lima angka di",
                    "belakang koma. Tanpa itu, pecahan biner yang tidak",
                    "pernah persis akan membuat tesmu gagal secara acak.",
                    "",
                    "`expect(() => grade(150)).toThrow(...)` membungkus",
                    "pemanggilannya dalam fungsi. Menulis `expect(grade(150))`",
                    "langsung akan melempar SEBELUM expect sempat berjalan,",
                    "dan tesnya gagal dengan pesan yang membingungkan.",
                    "",
                    "Menjalankan:",
                    "  npx vitest              mode tonton",
                    "  npx vitest run          sekali jalan, untuk CI",
                    "  npx vitest run --coverage",
                    "  npx vitest -t \"grade\"   hanya yang namanya cocok",
                    "",
                    "Untuk proyek tanpa dependensi sama sekali, `node:test`",
                    "bawaan Node sudah cukup untuk tes sederhana — bentuknya",
                    "mirip, dengan `assert` dari modul `node:assert/strict`.",
                ]
            },
        ],
    },
    {
        "title": "14. Bekerja dengan Data & Koleksi",
        "sections": [
            {
                "body": [
                    "TypeScript tidak menambah method koleksi apa pun — yang",
                    "dipakai adalah milik JavaScript. Yang ditambahkannya:",
                    "tipe hasilnya jadi tepat.",
                    "",
                    "ARRAY, yang paling sering dipakai:",
                    "  map filter reduce forEach find findIndex findLast",
                    "  some every includes indexOf",
                    "  slice splice concat join reverse sort",
                    "  flat flatMap fill at",
                    "  toSorted toReversed toSpliced with   (ES2023)",
                    "",
                    "Empat yang terakhir itu penting dan masih kurang",
                    "dikenal: mereka mengembalikan SALINAN alih-alih mengubah",
                    "di tempat. `arr.sort()` mengubah array aslinya —",
                    "sumber bug yang sangat sering — sedangkan",
                    "`arr.toSorted()` tidak.",
                    "",
                    "  const urut = data.toSorted((a, b) => a - b);",
                    "  const ganti = data.with(0, 99);",
                    "",
                    "MAP dan SET, sering terlupa padahal lebih tepat:",
                    "  new Map<string, number>()",
                    "  m.get(k) / m.set(k, v) / m.has(k) / m.delete(k)",
                    "  m.size / [...m.entries()]",
                    "",
                    "  new Set<number>()",
                    "  s.add(x) / s.has(x) / s.delete(x) / s.size",
                    "",
                    "Kapan Map lebih baik daripada objek polos:",
                    "  - kuncinya bukan string (Map menerima apa pun)",
                    "  - kuncinya datang dari luar (objek polos punya",
                    "    prototype yang bisa ditabrak, misalnya kunci",
                    "    bernama \"constructor\")",
                    "  - urutannya harus dijamin",
                    "  - sering ditambah dan dihapus",
                    "",
                    "OBJEK:",
                    "  Object.keys / values / entries / fromEntries",
                    "  Object.assign / freeze / groupBy (ES2024)",
                    "  { ...a, ...b }             spread, salinan dangkal",
                    "  structuredClone(x)         salinan DALAM",
                    "",
                    "PERINGATAN tipe pada `Object.keys`: ia mengembalikan",
                    "`string[]`, BUKAN `(keyof T)[]`. Itu disengaja dan",
                    "benar — sebuah objek bisa punya properti lebih banyak",
                    "daripada yang tertulis di tipenya.",
                    "",
                    "OPTIONAL CHAINING dan NULLISH COALESCING:",
                    "  a?.b?.c              berhenti di null pertama",
                    "  a?.[0]  f?.()        untuk indeks dan pemanggilan",
                    "  x ?? bawaan          hanya kalau null/undefined",
                    "  x ||= y   x ??= y    penugasan bersyarat",
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
                    "Baris 'urutan asli' membuktikan `toSorted` tidak",
                    "mengubah array aslinya. Dengan `sort()` biasa, baris itu",
                    "akan menampilkan urutan yang sudah teracak — dan bug",
                    "seperti itu sangat sulit dilacak karena penyebabnya",
                    "sebaris kode yang terlihat cuma 'membaca'.",
                    "",
                    "`sub(b) - sub(a) || a.barang.localeCompare(b.barang)`",
                    "adalah idiom pengurutan dua tingkat: kalau selisih",
                    "pertamanya nol (falsy), pakai pembanding kedua.",
                    "",
                    "`localeCompare` membandingkan teks sesuai aturan bahasa,",
                    "bukan sekadar nilai kode karakternya. Untuk teks yang",
                    "dilihat manusia, ini yang benar — meski untuk kunci",
                    "internal, perbandingan biasa lebih cepat dan lebih",
                    "mudah diprediksi.",
                    "",
                    "Perhatikan `rekap.get(t.kategori) ?? { total: 0, n: 0 }`:",
                    "`Map.get` mengembalikan `V | undefined`, dan TypeScript",
                    "MEMAKSA kamu menanganinya. Objek polos dengan index",
                    "signature tidak memberimu peringatan itu kecuali",
                    "`noUncheckedIndexedAccess` dinyalakan.",
                ]
            },
        ],
    },
    {
        "title": "15. TypeScript di Node & Browser",
        "sections": [
            {
                "body": [
                    "TypeScript sendiri tidak tahu apa-apa tentang lingkungan",
                    "tempat kodenya akan berjalan. Yang menentukan API apa",
                    "yang tersedia adalah dua setelan:",
                    "",
                    "  \"lib\"    API bahasa dan lingkungan yang dikenali",
                    "  \"types\"  paket tipe global yang dimuat",
                    "",
                    "UNTUK NODE:",
                    "  npm install --save-dev @types/node",
                    "  \"lib\": [\"es2022\"]",
                    "",
                    "Tanpa `@types/node`, `process`, `Buffer`, `__dirname`,",
                    "dan seluruh modul `node:` tidak dikenali — dan pesannya",
                    "berupa 'Cannot find name process', yang terdengar",
                    "seperti salah ketik.",
                    "",
                    "  import { readFile } from \"node:fs/promises\";",
                    "  import path from \"node:path\";",
                    "",
                    "Awalan `node:` adalah bentuk yang disarankan sekarang:",
                    "ia membuat jelas bahwa yang diimpor modul bawaan, bukan",
                    "paket npm bernama sama.",
                    "",
                    "UNTUK BROWSER:",
                    "  \"lib\": [\"es2022\", \"dom\", \"dom.iterable\"]",
                    "",
                    "Dengan `dom`, `document`, `window`, `fetch`, dan seluruh",
                    "API browser dikenali.",
                    "",
                    "Satu hal yang sering menjebak di browser:",
                    "",
                    "  const el = document.getElementById(\"tombol\");",
                    "  // bertipe HTMLElement | null",
                    "",
                    "TypeScript memaksa kamu menangani kemungkinan elemennya",
                    "tidak ada — dan itu benar, karena memang mungkin.",
                    "Untuk tipe yang lebih spesifik:",
                    "",
                    "  const el = document.querySelector<HTMLInputElement>(\"#nama\");",
                    "  if (!el) return;",
                    "  el.value;          sekarang dikenali",
                    "",
                    "MENJALANKAN TypeScript di Node, tiga cara:",
                    "  tsc && node dist/main.js      klasik, paling aman",
                    "  npx tsx src/main.ts           cepat, untuk pengembangan",
                    "  node --experimental-strip-types src/main.ts",
                    "",
                    "Yang ketiga (Node 22+) MENGHAPUS anotasi tipe tanpa",
                    "memeriksanya sama sekali. Ia cepat, tapi jangan sampai",
                    "menggantikan `tsc --noEmit` di CI — tanpa itu, tidak ada",
                    "yang benar-benar memeriksa tipemu.",
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
                    "Perhatikan pemeriksaan `if (nama === undefined || ...)`.",
                    "Itu diperlukan karena `split(\",\")` mengembalikan array",
                    "yang panjangnya tidak dijamin, dan dengan",
                    "`noUncheckedIndexedAccess` setiap elemennya bertipe",
                    "`string | undefined`.",
                    "",
                    "Ini contoh bagus dari setelan yang terasa merepotkan",
                    "tapi menangkap bug nyata: baris CSV yang kurang kolom",
                    "akan menghasilkan `undefined` yang diam-diam jadi",
                    "string \"undefined\" di tempat lain.",
                    "",
                    "`main().catch(...)` di akhir penting: tanpa itu, sebuah",
                    "Promise yang gagal menghasilkan unhandled rejection yang",
                    "di Node modern MENJATUHKAN proses dengan pesan yang",
                    "tidak membantu.",
                    "",
                    "`process.exitCode = 1` lebih baik daripada",
                    "`process.exit(1)`: yang pertama membiarkan Node",
                    "menyelesaikan penulisan keluaran yang tertunda, yang",
                    "kedua memotongnya seketika — dan pesan terakhirmu bisa",
                    "hilang.",
                ]
            },
        ],
    },
    {
        "title": "16. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan interface,",
                    "discriminated union, generic, koleksi, dan pemisahan",
                    "tanggung jawab dalam satu program utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang. Yang penting",
                    "bukan fiturnya melainkan CARA bagiannya dipisah.",
                    "",
                    "Tiga lapisan, panah ketergantungan satu arah:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  MODEL     interface Barang, union Gerak, dan union",
                    "            galat. Tidak tahu apa-apa tentang layar.",
                    "  LAYANAN   class Gudang dengan seluruh aturannya. TIDAK",
                    "            PERNAH memanggil console.log.",
                    "  ANTARMUKA memanggil layanan, mencetak hasilnya.",
                    "",
                    "Yang khas TypeScript di sini: kegagalan dikembalikan",
                    "sebagai DISCRIMINATED UNION, bukan dilempar sebagai",
                    "exception.",
                    "",
                    "Bedanya nyata:",
                    "  - Tanda tangan fungsinya MENYATAKAN bahwa ia bisa",
                    "    gagal, dan bagaimana bentuk kegagalannya.",
                    "  - Pemanggil harus mempersempit union sebelum bisa",
                    "    memakai hasilnya — compiler yang memaksanya.",
                    "  - Menambah jenis galat baru langsung membuat setiap",
                    "    `switch` yang belum lengkap gagal di pemeriksaan",
                    "    `never`.",
                    "",
                    "Ini pola yang sama dengan sealed class di Kotlin dan",
                    "Result di Rust, dan ia tersedia di TypeScript tanpa",
                    "fitur tambahan apa pun.",
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
                "body": [
                    "Lima keputusan yang layak ditiru:",
                    "",
                    "  1. Kegagalan dikembalikan lewat discriminated union.",
                    "     Pemanggil tidak bisa membaca `hasil.nilai` sebelum",
                    "     memeriksa `hasil.ok` — compiler yang memaksanya.",
                    "",
                    "  2. `Barang` seluruhnya `readonly`. Perubahan stok",
                    "     dilakukan dengan `{ ...b, stok: baru }`, menghasilkan",
                    "     objek baru. Tidak ada tempat lain yang bisa memegang",
                    "     Barang lalu mengubahnya diam-diam.",
                    "",
                    "  3. `#isi` memakai private field JavaScript, bukan",
                    "     `private` TypeScript. Privasinya bertahan di runtime.",
                    "",
                    "  4. `semua()` dan `stokMenipis()` MENGURUTKAN sebelum",
                    "     mengembalikan, dan memakai `toSorted` sehingga peta",
                    "     aslinya tidak tersentuh.",
                    "",
                    "  5. Gudang tidak memanggil console.log sama sekali. Itu",
                    "     yang membuat seluruh aturannya bisa diuji tanpa",
                    "     membaca layar.",
                    "",
                    "`satisfies Barang[]` pada daftar awal memeriksa bentuknya",
                    "tanpa melebarkan tipe literalnya — dan ia menangkap",
                    "salah ketik nama properti yang dengan `as Barang[]`",
                    "akan lolos diam-diam.",
                    "",
                    "Langkah berikutnya kalau kamu ingin melanjutkannya:",
                    "  - Validasi data masuk dengan Zod di batas sistem.",
                    "  - Simpan ke berkas JSON lewat node:fs/promises.",
                    "  - Sembunyikan penyimpanan di balik sebuah interface,",
                    "    sehingga Gudang tidak tahu datanya di berkas, di",
                    "    database, atau cuma di memori saat tes.",
                    "  - Tulis tes Vitest untuk Gudang — perhatikan ini",
                    "    langsung bisa dilakukan tanpa mengubah satu baris",
                    "    pun, justru karena keputusan nomor 5.",
                ]
            },
        ],
    },
]
