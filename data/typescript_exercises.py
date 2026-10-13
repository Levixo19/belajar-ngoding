TYPESCRIPT_EXERCISES = [
    {
        "title": "Latihan 1: Perkenalan Diri",
        "difficulty": "Mudah",
        "question": [
            "Buat program TypeScript yang menampilkan tepat tiga baris.",
            "Simpan nama, bahasa, dan tahun sebagai variabel BERTIPE.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar TypeScript.",
            "  Tipe hilang saat program jalan.",
        ],
        "hints": [
            "Anotasi tipe ditulis sesudah titik dua: const nama: string = ...",
            "console.log() mencetak lalu pindah baris.",
            "Template literal memakai backtick dan ${...}.",
        ],
        "solution": """const nama: string = "Andi";
const bahasa: string = "TypeScript";

console.log(`Halo, namaku ${nama}!`);
console.log(`Aku sedang belajar ${bahasa}.`);
console.log("Tipe hilang saat program jalan.");""",
    },
    {
        "title": "Latihan 2: Kalkulator Dua Bilangan",
        "difficulty": "Mudah",
        "question": [
            "Buat dua variabel a = 17 dan b = 5, lalu tampilkan:",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  17 + 5 = 22",
            "  17 - 5 = 12",
            "  17 * 5 = 85",
            "  17 / 5 = 3.4",
            "  17 % 5 = 2",
            "  17 ** 2 = 289",
            "  17 / 5 = 3 (dibulatkan ke bawah)",
        ],
        "hints": [
            "TypeScript cuma punya satu tipe angka: number, berupa pecahan.",
            "Pembagian TIDAK memotong: 17 / 5 langsung memberi 3.4.",
            "Untuk membulatkan ke bawah, pakai Math.floor atau Math.trunc.",
            "Operator pangkat adalah **.",
        ],
        "solution": """const a: number = 17;
const b: number = 5;

console.log(`${a} + ${b} = ${a + b}`);
console.log(`${a} - ${b} = ${a - b}`);
console.log(`${a} * ${b} = ${a * b}`);
console.log(`${a} / ${b} = ${a / b}`);
console.log(`${a} % ${b} = ${a % b}`);
console.log(`${a} ** 2 = ${a ** 2}`);
console.log(`${a} / ${b} = ${Math.floor(a / b)} (dibulatkan ke bawah)`);""",
    },
    {
        "title": "Latihan 3: Konversi Suhu",
        "difficulty": "Mudah",
        "question": [
            "Buat fungsi konversi(c: number) yang mencetak tiga baris,",
            "lalu panggil dengan 25, 0, dan -40.",
            "",
            "Rumus:",
            "  F = C * 9 / 5 + 32",
            "  K = C + 273.15",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Celsius    : 25.00",
            "  Fahrenheit : 77.00",
            "  Kelvin     : 298.15",
            "  ---",
            "  Celsius    : 0.00",
            "  Fahrenheit : 32.00",
            "  Kelvin     : 273.15",
            "  ---",
            "  Celsius    : -40.00",
            "  Fahrenheit : -40.00",
            "  Kelvin     : 233.15",
        ],
        "hints": [
            "toFixed(2) mengubah angka jadi teks dengan dua desimal.",
            "Tulis tipe di parameter dan kembalian: (c: number): void",
            "Cetak pemisah --- di antara pemanggilan, bukan sesudah yang terakhir.",
            "Perhatikan -40 adalah titik di mana Celsius dan Fahrenheit bertemu.",
        ],
        "solution": """function konversi(c: number): void {
  const f = c * 9 / 5 + 32;
  const k = c + 273.15;

  console.log(`Celsius    : ${c.toFixed(2)}`);
  console.log(`Fahrenheit : ${f.toFixed(2)}`);
  console.log(`Kelvin     : ${k.toFixed(2)}`);
}

const suhu: number[] = [25, 0, -40];
suhu.forEach((c, i) => {
  if (i > 0) console.log("---");
  konversi(c);
});""",
    },
    {
        "title": "Latihan 4: Grade & Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Buat fungsi grade(n: number) yang mengembalikan union literal",
            "\"A\" | \"B\" | \"C\" | \"D\" | \"E\" sesuai aturan:",
            "  >= 85 : A, >= 75 : B, >= 60 : C, >= 40 : D, sisanya E",
            "",
            "Buat juga fungsi kelulusan(n: number): \"Lulus\" | \"Tidak Lulus\"",
            "dengan batas 75.",
            "",
            "Uji dengan nilai 92, 78, 65, 45, dan 12.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "   92 -> A  Lulus",
            "   78 -> B  Lulus",
            "   65 -> C  Tidak Lulus",
            "   45 -> D  Tidak Lulus",
            "   12 -> E  Tidak Lulus",
            "",
            "Nilai dicetak rata kanan selebar 3.",
        ],
        "hints": [
            "Tipe kembalian union literal: \"A\" | \"B\" | ...",
            "String(n).padStart(3) meratakan ke kanan.",
            "Union literal lebih ringan daripada enum: ia hilang saat kompilasi.",
            "JANGAN menamainya `status`: itu variabel GLOBAL milik lib.dom, "
            "dan mendeklarasikannya ulang menghasilkan Duplicate identifier.",
        ],
        "solution": """type Grade = "A" | "B" | "C" | "D" | "E";
type Kelulusan = "Lulus" | "Tidak Lulus";

function grade(n: number): Grade {
  if (n >= 85) return "A";
  if (n >= 75) return "B";
  if (n >= 60) return "C";
  if (n >= 40) return "D";
  return "E";
}

function kelulusan(n: number): Kelulusan {
  return n >= 75 ? "Lulus" : "Tidak Lulus";
}

const nilai: number[] = [92, 78, 65, 45, 12];
for (const n of nilai) {
  console.log(`${String(n).padStart(3)} -> ${grade(n)}  ${kelulusan(n)}`);
}""",
    },
    {
        "title": "Latihan 5: Tabel Perkalian",
        "difficulty": "Mudah",
        "question": [
            "Tampilkan tabel perkalian 1 sampai 5.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  1 x 1 =  1   1 x 2 =  2   1 x 3 =  3   1 x 4 =  4   1 x 5 =  5",
            "  2 x 1 =  2   2 x 2 =  4   2 x 3 =  6   2 x 4 =  8   2 x 5 = 10",
            "  3 x 1 =  3   3 x 2 =  6   3 x 3 =  9   3 x 4 = 12   3 x 5 = 15",
            "  4 x 1 =  4   4 x 2 =  8   4 x 3 = 12   4 x 4 = 16   4 x 5 = 20",
            "  5 x 1 =  5   5 x 2 = 10   5 x 3 = 15   5 x 4 = 20   5 x 5 = 25",
            "",
            "Tiap baris diawali dua spasi. Hasil perkaliannya rata kanan",
            "selebar 2 karakter, dan tiap sel dipisah tiga spasi.",
        ],
        "hints": [
            "Array.from({ length: 5 }, (_, i) => i + 1) membuat [1..5].",
            "map lalu join(\"   \") menyusun satu baris.",
            "padStart(2) meratakan hasil perkaliannya.",
            "Tanda garis bawah dipakai untuk parameter yang tidak terpakai.",
        ],
        "solution": """const angka: number[] = Array.from({ length: 5 }, (_, i) => i + 1);

for (const b of angka) {
  const sel = angka.map((k) => `${b} x ${k} = ${String(b * k).padStart(2)}`);
  console.log("  " + sel.join("   "));
}""",
    },
    {
        "title": "Latihan 6: Statistik Nilai",
        "difficulty": "Menengah",
        "question": [
            "Diberikan array nilai berikut di dalam kodemu:",
            "  78, 92, 65, 88, 71, 95, 59, 83",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
            "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
            "  Jumlah    : 8",
            "  Total     : 631",
            "  Rata-rata : 78.88",
            "  Tertinggi : 95",
            "  Terendah  : 59",
            "  Di atas rata-rata: 92, 88, 95, 83",
            "  ---",
            "  Data ASLI tetap: 78, 92, 65, 88, 71, 95, 59, 83",
        ],
        "hints": [
            "Pakai toSorted(), BUKAN sort() — sort mengubah array aslinya.",
            "Math.max(...arr) dan Math.min(...arr) memakai spread.",
            "reduce((a, b) => a + b, 0) menjumlahkan.",
            "Baris terakhir membuktikan toSorted tidak merusak data aslinya.",
        ],
        "solution": """const nilai: number[] = [78, 92, 65, 88, 71, 95, 59, 83];

const total = nilai.reduce((a, b) => a + b, 0);
const rata = total / nilai.length;

console.log(`Data      : ${nilai.join(", ")}`);
console.log(`Terurut   : ${nilai.toSorted((a, b) => a - b).join(", ")}`);
console.log(`Jumlah    : ${nilai.length}`);
console.log(`Total     : ${total}`);
console.log(`Rata-rata : ${rata.toFixed(2)}`);
console.log(`Tertinggi : ${Math.max(...nilai)}`);
console.log(`Terendah  : ${Math.min(...nilai)}`);
console.log(`Di atas rata-rata: ${nilai.filter((n) => n > rata).join(", ")}`);
console.log("---");
console.log(`Data ASLI tetap: ${nilai.join(", ")}`);""",
    },
    {
        "title": "Latihan 7: Balik Teks & Palindrom",
        "difficulty": "Menengah",
        "question": [
            "Buat fungsi periksa(teks: string) yang mencetak empat baris:",
            "  Asli    : teks aslinya",
            "  Dibalik : teksnya dibalik",
            "  Huruf   : jumlah huruf tanpa spasi",
            "  Palindrom: ya / bukan (abaikan spasi dan besar-kecil huruf)",
            "",
            "Uji dengan 'Kasur ini rusak', 'Belajar TypeScript', dan 'Ini'.",
            "Cetak --- di antara tiap pemeriksaan.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Asli    : Kasur ini rusak",
            "  Dibalik : kasur ini rusaK",
            "  Huruf   : 13",
            "  Palindrom: ya",
            "  ---",
            "  Asli    : Belajar TypeScript",
            "  Dibalik : tpircSepyT rajaleB",
            "  Huruf   : 17",
            "  Palindrom: bukan",
            "  ---",
            "  Asli    : Ini",
            "  Dibalik : inI",
            "  Huruf   : 3",
            "  Palindrom: ya",
        ],
        "hints": [
            "Membalik: [...teks].reverse().join(\"\") atau split(\"\").reverse().join(\"\")",
            "replaceAll(\" \", \"\") membuang spasi.",
            "toLowerCase() untuk mengabaikan besar-kecil huruf.",
            "Cetak pemisah hanya DI ANTARA, bukan sesudah yang terakhir.",
        ],
        "solution": """function balik(s: string): string {
  return [...s].reverse().join("");
}

function periksa(teks: string): void {
  const rapat = teks.replaceAll(" ", "");
  const bersih = rapat.toLowerCase();

  console.log(`Asli    : ${teks}`);
  console.log(`Dibalik : ${balik(teks)}`);
  console.log(`Huruf   : ${rapat.length}`);
  console.log(`Palindrom: ${bersih === balik(bersih) ? "ya" : "bukan"}`);
}

const contoh: string[] = ["Kasur ini rusak", "Belajar TypeScript", "Ini"];
contoh.forEach((t, i) => {
  if (i > 0) console.log("---");
  periksa(t);
});""",
    },
    {
        "title": "Latihan 8: Menghitung Frekuensi Kata",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat berikut di dalam kodemu:",
            "  \"kucing makan ikan kucing tidur ikan kucing\"",
            "",
            "Hitung frekuensi tiap kata memakai Map<string, number>,",
            "lalu tampilkan terurut dari yang paling sering. Kalau",
            "jumlahnya sama, urutkan berdasarkan abjad.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  kucing : 3",
            "  ikan   : 2",
            "  makan  : 1",
            "  tidur  : 1",
            "  ---",
            "  Kata unik  : 4",
            "  Total kata : 7",
            "",
            "Nama kata rata kiri selebar 7 karakter.",
        ],
        "hints": [
            "Map.get mengembalikan V | undefined — tangani dengan ?? 0.",
            "[...peta] mengubah Map jadi array pasangan [kunci, nilai].",
            "Dua kunci urutan: b[1] - a[1] || a[0].localeCompare(b[0])",
            "padEnd(7) meratakan ke kiri.",
        ],
        "solution": """const kalimat = "kucing makan ikan kucing tidur ikan kucing";
const kata: string[] = kalimat.split(" ");

const hitung = new Map<string, number>();
for (const k of kata) {
  hitung.set(k, (hitung.get(k) ?? 0) + 1);
}

const terurut = [...hitung].toSorted(
  (a, b) => b[1] - a[1] || a[0].localeCompare(b[0]),
);

for (const [k, n] of terurut) {
  console.log(`${k.padEnd(7)}: ${n}`);
}

console.log("---");
console.log(`Kata unik  : ${hitung.size}`);
console.log(`Total kata : ${kata.length}`);""",
    },
    {
        "title": "Latihan 9: Interface & Type Guard",
        "difficulty": "Menengah",
        "question": [
            "Buat interface Murid { readonly id: number; nama: string;",
            "nilai: number } dan interface Guru extends Murid",
            "{ mapel: string }.",
            "",
            "Buat type Orang = Murid | Guru, lalu type guard",
            "adalahGuru(o: Orang): o is Guru yang memeriksa properti mapel.",
            "",
            "Buat fungsi ringkas(o: Orang): string berformat",
            "\"<nama rata kiri 8><peran rata kiri 7><nilai rata kanan 3>\"",
            "ditambah \" (<mapel>)\" kalau ia guru.",
            "",
            "Isi: Andi 88 (murid), Budi 72 mapel Matematika, Cici 95 (murid).",
            "Urutkan nilai MENURUN lalu cetak.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Cici    murid   95",
            "  Andi    murid   88",
            "  Budi    guru    72 (Matematika)",
        ],
        "hints": [
            "Predikat tipe ditulis sebagai tipe kembalian: o is Guru",
            "\"mapel\" in o mempersempit union berdasarkan properti.",
            "Sesudah type guard, o.mapel boleh diakses tanpa cast.",
            "toSorted((a, b) => b.nilai - a.nilai) untuk urutan menurun.",
        ],
        "solution": """interface Murid {
  readonly id: number;
  nama: string;
  nilai: number;
}

interface Guru extends Murid {
  mapel: string;
}

type Orang = Murid | Guru;

function adalahGuru(o: Orang): o is Guru {
  return "mapel" in o;
}

function ringkas(o: Orang): string {
  const peran = adalahGuru(o) ? "guru" : "murid";
  const tambahan = adalahGuru(o) ? ` (${o.mapel})` : "";
  return (
    o.nama.padEnd(8) +
    peran.padEnd(7) +
    String(o.nilai).padStart(3) +
    tambahan
  );
}

const semua: Orang[] = [
  { id: 1, nama: "Andi", nilai: 88 },
  { id: 2, nama: "Budi", nilai: 72, mapel: "Matematika" },
  { id: 3, nama: "Cici", nilai: 95 },
];

for (const o of semua.toSorted((a, b) => b.nilai - a.nilai)) {
  console.log(ringkas(o));
}""",
    },
    {
        "title": "Latihan 10: Discriminated Union",
        "difficulty": "Lanjut",
        "question": [
            "Buat type Bentuk sebagai discriminated union dengan properti",
            "penanda `jenis`:",
            "  { jenis: \"lingkaran\"; jari: number }",
            "  { jenis: \"persegi\"; sisi: number }",
            "  { jenis: \"persegiPanjang\"; panjang: number; lebar: number }",
            "",
            "Buat fungsi luas(b: Bentuk): number memakai switch atas",
            "`jenis`, dengan cabang default yang memakai pemeriksaan never.",
            "Pakai PI = 3.14159.",
            "",
            "Buat juga fungsi nama(b: Bentuk): string yang menghasilkan",
            "\"Lingkaran\", \"Persegi\", atau \"PersegiPanjang\".",
            "",
            "Isi dengan persegi(4), lingkaran(3), persegiPanjang(6, 3),",
            "lalu cetak tabelnya dan totalnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Persegi            16.00",
            "  Lingkaran          28.27",
            "  PersegiPanjang     18.00",
            "  TOTAL              62.27",
            "",
            "Nama rata kiri 16, luas rata kanan 8 dengan dua desimal.",
        ],
        "hints": [
            "Di dalam tiap case, TypeScript tahu properti apa yang tersedia.",
            "const _lengkap: never = b; di default memastikan kelengkapannya.",
            "padEnd(16) dan toFixed(2).padStart(8) untuk kolomnya.",
            "reduce untuk menjumlahkan luas seluruh bentuk.",
        ],
        "solution": """type Bentuk =
  | { jenis: "lingkaran"; jari: number }
  | { jenis: "persegi"; sisi: number }
  | { jenis: "persegiPanjang"; panjang: number; lebar: number };

const PI = 3.14159;

function luas(b: Bentuk): number {
  switch (b.jenis) {
    case "lingkaran":
      return PI * b.jari * b.jari;
    case "persegi":
      return b.sisi * b.sisi;
    case "persegiPanjang":
      return b.panjang * b.lebar;
    default: {
      const _lengkap: never = b;
      throw new Error(`bentuk belum ditangani: ${JSON.stringify(_lengkap)}`);
    }
  }
}

function nama(b: Bentuk): string {
  return b.jenis === "persegiPanjang"
    ? "PersegiPanjang"
    : b.jenis.charAt(0).toUpperCase() + b.jenis.slice(1);
}

const semua: Bentuk[] = [
  { jenis: "persegi", sisi: 4 },
  { jenis: "lingkaran", jari: 3 },
  { jenis: "persegiPanjang", panjang: 6, lebar: 3 },
];

for (const b of semua) {
  console.log(nama(b).padEnd(16) + luas(b).toFixed(2).padStart(8));
}

const total = semua.reduce((t, b) => t + luas(b), 0);
console.log("TOTAL".padEnd(16) + total.toFixed(2).padStart(8));""",
    },
    {
        "title": "Latihan 11: Generic & keyof",
        "difficulty": "Lanjut",
        "question": [
            "Buat fungsi generic berikut:",
            "  ambil<T, K extends keyof T>(o: T, k: K): T[K]",
            "  terpanjang<T extends { length: number }>(a: T, b: T): T",
            "  kelompokkan<T, K extends string>(d: T[], kunci: (x: T) => K):",
            "      Map<K, T[]>",
            "",
            "Buat interface Murid { id, nama, kelas, nilai } lalu:",
            "  1. Ambil nama dan nilai dari satu murid",
            "  2. Bandingkan dua teks dan dua array dengan terpanjang",
            "  3. Kelompokkan lima murid berdasarkan kelas, cetak terurut",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  ambil nama : Andi",
            "  ambil nilai: 88",
            "  ---",
            "  teks  : jauh lebih panjang",
            "  array : 1,2,3",
            "  ---",
            "  Kelas A: Andi, Cici, Euis (rata-rata 87.3)",
            "  Kelas B: Budi, Dedi (rata-rata 68.0)",
        ],
        "hints": [
            "keyof T menghasilkan union dari nama-nama propertinya.",
            "T[K] adalah tipe properti K di dalam T — indexed access type.",
            "Map.get mengembalikan V | undefined; pakai ?? [] saat mengelompokkan.",
            "toFixed(1) untuk rata-rata dengan satu desimal.",
        ],
        "solution": """interface Murid {
  id: number;
  nama: string;
  kelas: string;
  nilai: number;
}

function ambil<T, K extends keyof T>(o: T, k: K): T[K] {
  return o[k];
}

function terpanjang<T extends { length: number }>(a: T, b: T): T {
  return a.length >= b.length ? a : b;
}

function kelompokkan<T, K extends string>(
  data: T[],
  kunci: (x: T) => K,
): Map<K, T[]> {
  const hasil = new Map<K, T[]>();
  for (const x of data) {
    const k = kunci(x);
    hasil.set(k, [...(hasil.get(k) ?? []), x]);
  }
  return hasil;
}

const kelas: Murid[] = [
  { id: 1, nama: "Andi", kelas: "A", nilai: 88 },
  { id: 2, nama: "Budi", kelas: "B", nilai: 72 },
  { id: 3, nama: "Cici", kelas: "A", nilai: 95 },
  { id: 4, nama: "Dedi", kelas: "B", nilai: 64 },
  { id: 5, nama: "Euis", kelas: "A", nilai: 79 },
];

const pertama = kelas[0]!;
console.log(`ambil nama : ${ambil(pertama, "nama")}`);
console.log(`ambil nilai: ${ambil(pertama, "nilai")}`);

console.log("---");
console.log(`teks  : ${terpanjang("pendek", "jauh lebih panjang")}`);
console.log(`array : ${terpanjang([1, 2], [1, 2, 3]).join(",")}`);

console.log("---");
const per = kelompokkan(kelas, (m) => m.kelas);
for (const [k, anggota] of [...per].toSorted((a, b) => a[0].localeCompare(b[0]))) {
  const rata = anggota.reduce((t, m) => t + m.nilai, 0) / anggota.length;
  const nama = anggota.map((m) => m.nama).join(", ");
  console.log(`Kelas ${k}: ${nama} (rata-rata ${rata.toFixed(1)})`);
}""",
    },
    {
        "title": "Latihan 12: Validasi Data dari Luar",
        "difficulty": "Lanjut",
        "question": [
            "Buat interface Murid { nama: string; kelas: string; nilai: number }.",
            "",
            "Buat type guard adalahMurid(x: unknown): x is Murid yang",
            "memeriksa: nama string tidak kosong, kelas string, dan nilai",
            "bilangan BULAT 0..100.",
            "",
            "Buat type Hasil<T> = { ok: true; nilai: T } | { ok: false; pesan: string }",
            "dan fungsi uraikan(teks: string): Hasil<Murid> yang menangani",
            "JSON rusak DAN bentuk yang tidak sesuai secara terpisah.",
            "",
            "Uji dengan lima masukan:",
            "  '{\"nama\":\"Andi\",\"kelas\":\"A\",\"nilai\":88}'",
            "  '{\"nama\":\"Budi\",\"kelas\":\"B\"}'",
            "  '{\"nama\":\"Cici\",\"kelas\":\"A\",\"nilai\":150}'",
            "  '{\"nama\":\"\",\"kelas\":\"A\",\"nilai\":70}'",
            "  '{rusak}'",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  OK    Andi  A 88",
            "  TOLAK bentuk data tidak sesuai",
            "  TOLAK bentuk data tidak sesuai",
            "  TOLAK bentuk data tidak sesuai",
            "  TOLAK JSON tidak bisa diurai",
        ],
        "hints": [
            "JSON.parse mengembalikan any — tampung ke variabel bertipe unknown.",
            "Cast ke Record<string, unknown> untuk memeriksa propertinya.",
            "Number.isInteger memeriksa bilangan bulat sekaligus menolak NaN.",
            "try/catch di sekitar JSON.parse, bukan di sekitar seluruh fungsi.",
        ],
        "solution": """interface Murid {
  nama: string;
  kelas: string;
  nilai: number;
}

type Hasil<T> =
  | { ok: true; nilai: T }
  | { ok: false; pesan: string };

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

function uraikan(teks: string): Hasil<Murid> {
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

const masukan: string[] = [
  '{"nama":"Andi","kelas":"A","nilai":88}',
  '{"nama":"Budi","kelas":"B"}',
  '{"nama":"Cici","kelas":"A","nilai":150}',
  '{"nama":"","kelas":"A","nilai":70}',
  "{rusak}",
];

for (const teks of masukan) {
  const h = uraikan(teks);
  if (h.ok) {
    console.log(`OK    ${h.nilai.nama.padEnd(6)}${h.nilai.kelas} ${h.nilai.nilai}`);
  } else {
    console.log(`TOLAK ${h.pesan}`);
  }
}""",
    },
    {
        "title": "Latihan 13: Laporan Penjualan",
        "difficulty": "Lanjut",
        "question": [
            "Buat interface Transaksi { barang, kategori, jumlah, harga }",
            "dan fungsi sub(t) yang menghitung subtotal.",
            "",
            "Isi dengan:",
            "  Kopi  Minuman  3  25000",
            "  Teh   Minuman  5  15000",
            "  Roti  Makanan  2  20000",
            "  Nasi  Makanan  4  30000",
            "  Jus   Minuman  1  35000",
            "",
            "Tampilkan semua terurut subtotal MENURUN; kalau sama, nama",
            "barang MENAIK. Lalu total, rekap per kategori terurut abjad,",
            "dan barang termahal. Data aslinya TIDAK boleh berubah.",
            "",
            "Keluaran yang diharapkan:",
            "",
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
            "",
            "Kolom: barang rata kiri 11, kategori rata kiri 11, jumlah rata",
            "kanan 2, harga rata kanan 6, subtotal rata kanan 8.",
        ],
        "hints": [
            "toSorted menjaga array aslinya tetap utuh.",
            "Dua kunci urutan: sub(b) - sub(a) || a.barang.localeCompare(b.barang)",
            "Map untuk rekap, lalu urutkan kuncinya sebelum mencetak.",
            "reduce dengan pembanding untuk mencari yang termahal.",
        ],
        "solution": """interface Transaksi {
  barang: string;
  kategori: string;
  jumlah: number;
  harga: number;
}

const sub = (t: Transaksi): number => t.jumlah * t.harga;

const data: Transaksi[] = [
  { barang: "Kopi", kategori: "Minuman", jumlah: 3, harga: 25000 },
  { barang: "Teh", kategori: "Minuman", jumlah: 5, harga: 15000 },
  { barang: "Roti", kategori: "Makanan", jumlah: 2, harga: 20000 },
  { barang: "Nasi", kategori: "Makanan", jumlah: 4, harga: 30000 },
  { barang: "Jus", kategori: "Minuman", jumlah: 1, harga: 35000 },
];

const terurut = data.toSorted(
  (a, b) => sub(b) - sub(a) || a.barang.localeCompare(b.barang),
);

for (const t of terurut) {
  console.log(
    t.barang.padEnd(11) +
      t.kategori.padEnd(11) +
      String(t.jumlah).padStart(2) +
      " x " +
      String(t.harga).padStart(6) +
      " = " +
      String(sub(t)).padStart(8),
  );
}

console.log("---");
console.log(`${"Total".padEnd(10)}: ${data.reduce((x, t) => x + sub(t), 0)}`);

const rekap = new Map<string, { total: number; n: number }>();
for (const t of data) {
  const lama = rekap.get(t.kategori) ?? { total: 0, n: 0 };
  rekap.set(t.kategori, { total: lama.total + sub(t), n: lama.n + 1 });
}

for (const [k, r] of [...rekap].toSorted((a, b) => a[0].localeCompare(b[0]))) {
  console.log(`${k.padEnd(10)}: ${r.total} (${r.n} transaksi)`);
}

const termahal = data.reduce((a, b) => (sub(b) > sub(a) ? b : a));
console.log(`${"Termahal".padEnd(10)}: ${termahal.barang}`);""",
    },
    {
        "title": "Latihan 14: Utility Type & Mapped Type",
        "difficulty": "Sulit",
        "question": [
            "Buat interface Murid { readonly id: number; nama: string;",
            "nilai: number; catatan?: string }.",
            "",
            "Buat tipe turunan berikut TANPA menuliskan ulang propertinya:",
            "  MuridBaru      = Murid tanpa id",
            "  TambalMurid    = semua properti Murid jadi opsional",
            "  RingkasMurid   = hanya nama dan nilai",
            "  BisaDiubah     = mapped type yang membuang readonly",
            "  WajibSemua     = mapped type yang membuang opsional",
            "",
            "Buat fungsi terapkan(asal: Murid, tambalan: TambalMurid): Murid",
            "yang menggabungkan keduanya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  asal    : {\"id\":1,\"nama\":\"Andi\",\"nilai\":88}",
            "  baru    : {\"nama\":\"Budi\",\"nilai\":72}",
            "  ringkas : {\"nama\":\"Cici\",\"nilai\":95}",
            "  tambal  : {\"id\":1,\"nama\":\"Andi\",\"nilai\":75}",
            "  diubah  : {\"id\":9,\"nama\":\"Dedi\",\"nilai\":64}",
            "  wajib   : {\"id\":3,\"nama\":\"Euis\",\"nilai\":79,\"catatan\":\"ada\"}",
        ],
        "hints": [
            "Omit<T, K>, Partial<T>, dan Pick<T, K> sudah tersedia.",
            "Mapped type: { -readonly [K in keyof T]: T[K] }",
            "Tanda minus MENGHAPUS penanda; -? membuang opsional.",
            "Spread { ...asal, ...tambalan } menimpa dengan yang belakangan.",
        ],
        "solution": """interface Murid {
  readonly id: number;
  nama: string;
  nilai: number;
  catatan?: string;
}

type MuridBaru = Omit<Murid, "id">;
type TambalMurid = Partial<Murid>;
type RingkasMurid = Pick<Murid, "nama" | "nilai">;
type BisaDiubah<T> = { -readonly [K in keyof T]: T[K] };
type WajibSemua<T> = { [K in keyof T]-?: T[K] };

function terapkan(asal: Murid, tambalan: TambalMurid): Murid {
  return { ...asal, ...tambalan };
}

const asal: Murid = { id: 1, nama: "Andi", nilai: 88 };
const baru: MuridBaru = { nama: "Budi", nilai: 72 };
const ringkas: RingkasMurid = { nama: "Cici", nilai: 95 };

const diubah: BisaDiubah<Murid> = { id: 8, nama: "Dedi", nilai: 64 };
diubah.id = 9;                       // boleh: readonly sudah dibuang

const wajib: WajibSemua<Murid> = {
  id: 3,
  nama: "Euis",
  nilai: 79,
  catatan: "ada",
};

console.log(`asal    : ${JSON.stringify(asal)}`);
console.log(`baru    : ${JSON.stringify(baru)}`);
console.log(`ringkas : ${JSON.stringify(ringkas)}`);
console.log(`tambal  : ${JSON.stringify(terapkan(asal, { nilai: 75 }))}`);
console.log(`diubah  : ${JSON.stringify(diubah)}`);
console.log(`wajib   : ${JSON.stringify(wajib)}`);""",
    },
    {
        "title": "Latihan 15: Async & Promise",
        "difficulty": "Sulit",
        "question": [
            "Buat fungsi tunggu(ms) yang mengembalikan Promise<void>,",
            "fungsi async ambil(nama, ms): Promise<string> yang",
            "mengembalikan \"<nama> selesai\", dan fungsi async",
            "gagal(nama): Promise<string> yang melempar \"<nama> gagal\".",
            "",
            "Di fungsi main async, tunjukkan berurutan:",
            "  1. Promise.all pada dua ambil yang berhasil",
            "  2. Promise.all yang GAGAL karena satu anggotanya gagal",
            "  3. Promise.allSettled yang melaporkan keduanya",
            "  4. Memproses empat nama BERSAMAAN dengan map + Promise.all",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  all       : A selesai, B selesai",
            "  all gagal : C gagal",
            "  settled   : berhasil D selesai",
            "  settled   : gagal   E gagal",
            "  bersamaan : satu=4, dua=3, tiga=4, empat=5",
        ],
        "hints": [
            "new Promise<void>((selesai) => setTimeout(selesai, ms))",
            "Variabel di blok catch bertipe unknown — periksa instanceof Error.",
            "allSettled memberi { status, value } atau { status, reason }.",
            "map dengan async callback menghasilkan array Promise.",
        ],
        "solution": """function tunggu(ms: number): Promise<void> {
  return new Promise<void>((selesai) => setTimeout(selesai, ms));
}

async function ambil(nama: string, ms: number): Promise<string> {
  await tunggu(ms);
  return `${nama} selesai`;
}

async function gagal(nama: string): Promise<string> {
  await tunggu(10);
  throw new Error(`${nama} gagal`);
}

function pesan(e: unknown): string {
  return e instanceof Error ? e.message : String(e);
}

async function main(): Promise<void> {
  const berhasil = await Promise.all([ambil("A", 20), ambil("B", 20)]);
  console.log(`all       : ${berhasil.join(", ")}`);

  try {
    await Promise.all([ambil("X", 20), gagal("C")]);
  } catch (e) {
    console.log(`all gagal : ${pesan(e)}`);
  }

  const settled = await Promise.allSettled([ambil("D", 20), gagal("E")]);
  for (const s of settled) {
    if (s.status === "fulfilled") {
      console.log(`settled   : berhasil ${s.value}`);
    } else {
      console.log(`settled   : gagal   ${pesan(s.reason)}`);
    }
  }

  const nama = ["satu", "dua", "tiga", "empat"];
  const panjang = await Promise.all(
    nama.map(async (n) => {
      await tunggu(20);
      return `${n}=${n.length}`;
    }),
  );
  console.log(`bersamaan : ${panjang.join(", ")}`);
}

main().catch((e: unknown) => {
  console.error(pesan(e));
});""",
    },
    {
        "title": "Latihan 16: Proyek Akhir - Inventaris Gudang",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Bangun sistem inventaris yang MEMISAHKAN tiga lapisan:",
            "model (data), layanan (aturan), dan antarmuka (cetak).",
            "",
            "MODEL",
            "  interface Barang dengan SEMUA properti readonly:",
            "    kode, nama, stok, harga",
            "  type Gerak = \"masuk\" | \"keluar\"",
            "  type GalatGudang sebagai discriminated union berpenanda",
            "  `jenis` dengan empat anggota: kodeSudahAda, kodeTidakDikenal,",
            "  jumlahTidakSah, stokTidakCukup.",
            "  type Hasil<T> = { ok: true; nilai: T } | { ok: false; galat }",
            "  Fungsi pesanGalat(g) memakai switch + pemeriksaan never.",
            "  Pesannya:",
            "    \"kode B01 sudah ada\"",
            "    \"kode B09 tidak dikenal\"",
            "    \"jumlah 0 tidak sah\"",
            "    \"stok cuma 4, diminta 10\"",
            "",
            "LAYANAN  class Gudang dengan private field #isi berupa Map",
            "  - daftar(b): Hasil<Barang>",
            "  - catat(kode, gerak, jumlah): Hasil<number>",
            "    urutan periksa: kode dulu, lalu jumlah, baru kecukupan stok",
            "  - semua(): Barang[] terurut kode",
            "  - nilaiPersediaan(): number",
            "  - stokMenipis(batas): Barang[] terurut stok naik lalu kode",
            "  Gudang TIDAK BOLEH memanggil console.log sama sekali.",
            "",
            "ANTARMUKA",
            "  Daftarkan B01 Kabel 10 15000, B02 Adaptor 4 85000,",
            "            B03 Mouse 25 120000",
            "  Jalankan: masuk B01 15, keluar B02 10, keluar B03 5,",
            "            masuk B09 1, keluar B03 0",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Masuk B01 15 -> stok 25",
            "  Keluar B02 10 -> DITOLAK: stok cuma 4, diminta 10",
            "  Keluar B03 5 -> stok 20",
            "  Masuk B09 1 -> DITOLAK: kode B09 tidak dikenal",
            "  Keluar B03 0 -> DITOLAK: jumlah 0 tidak sah",
            "  ---",
            "  B01  Kabel       25     15000      375000",
            "  B02  Adaptor      4     85000      340000",
            "  B03  Mouse       20    120000     2400000",
            "  ---",
            "  nilai persediaan: 3115000",
            "  stok menipis (<10): B02 Adaptor (4)",
            "",
            "Kolom tabel: kode rata kiri 5, nama rata kiri 12, stok rata",
            "kanan 2, harga rata kanan 10, subtotal rata kanan 12.",
        ],
        "hints": [
            "Barang readonly seluruhnya: perbarui dengan { ...b, stok: baru }.",
            "#isi dengan tanda pagar adalah private field JavaScript — ia "
            "bertahan di runtime, berbeda dari `private` TypeScript.",
            "Map.get mengembalikan Barang | undefined; periksa === undefined.",
            "Pemanggil TIDAK BISA membaca hasil.nilai sebelum memeriksa "
            "hasil.ok — compiler yang memaksanya, dan itu seluruh gunanya.",
            "Number.isInteger sekaligus menolak NaN dan pecahan.",
        ],
        "solution": """// ---------------------------------------------------------------- MODEL
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
    return [...this.#isi.values()].toSorted((a, b) =>
      a.kode.localeCompare(b.kode),
    );
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

const awal: Barang[] = [
  { kode: "B01", nama: "Kabel", stok: 10, harga: 15000 },
  { kode: "B02", nama: "Adaptor", stok: 4, harga: 85000 },
  { kode: "B03", nama: "Mouse", stok: 25, harga: 120000 },
];
for (const b of awal) gudang.daftar(b);

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
console.log(`stok menipis (<10): ${menipis}`);""",
    },
]
