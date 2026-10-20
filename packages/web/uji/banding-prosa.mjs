/* Adu `segmenKode` dengan `berkode` di `webapp/statik/js/layar-belajar.js`.
 *
 * Yang diputuskan fungsi ini: kata mana di tengah prosa DIKOTAKI sebagai kode.
 * Terlalu sedikit, dan `<p>` terbaca sebagai kata biasa di tengah kalimat
 * Indonesia -- satu-satunya cara mengenalinya jadi sudah tahu lebih dulu.
 * Terlalu banyak, dan penandanya berhenti menandai apa pun: kalau setiap
 * paragraf punya chip, tidak ada yang punya.
 *
 * Korpusnya SELURUH teks prosa kurikulum: tiap baris `body` materi, tiap baris
 * soal latihan, dan tiap petunjuk. Itu ratusan ribu baris, dan memang itu
 * gunanya -- polanya memuat lima alternatif yang saling tumpang tindih, dan
 * yang menemukan tumpang tindih yang salah bukan contoh yang ditulis tangan.
 *
 * Sisi JS dijalankan dengan `h` DI-SHIM jadi satu baris. `berkode` memanggil
 * `h` hanya untuk membungkus `<code>`, jadi shim itu membuatnya mengembalikan
 * bentuk data yang sama persis dengan `segmenKode` -- tanpa memuat `inti.js`
 * dan tanpa DOM sama sekali.
 *
 *     node uji/banding-prosa.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { segmenKode } from "../src/komponen/prosa-teks.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "layar-belajar.js");
const KONTEN = path.join(AKAR, "packages", "konten", "kurikulum");

const teks = readFileSync(SUMBER, "utf-8");

function potong(pola, nama) {
  const cocok = teks.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. Sumbernya mungkin ditulis ulang. ` +
        `Perbarui polanya, JANGAN biarkan pagar ini membandingkan nol fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const bagian = [
  potong(/const POLA_KODE = new RegExp\([\s\S]*?"g"\);/, "POLA_KODE"),
  potong(/export function berkode\(teks\) \{[\s\S]*?\n\}/, "berkode"),
];

const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-prosa-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  "const h = (_tag, _sifat, teks) => ({ kode: true, teks });\n"
    + bagian.join("\n").replace(/^export /gm, "")
    + "\nexport {berkode};\n",
);
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
let takUtuh = 0;
const adu = (nama, a, b) => {
  const sa = JSON.stringify(a);
  const sb = JSON.stringify(b);
  if (sa !== sb) {
    gagal += 1;
    if (gagal <= 5) {
      console.error(
        `  ${nama}\n    JS: ${sa.slice(0, 200)}\n    TS: ${sb.slice(0, 200)}`,
      );
    }
  }
};

/* ------------------------------------------------- korpus prosa kurikulum */

const baris = [];
for (const nama of readdirSync(KONTEN).sort()) {
  const lang = JSON.parse(readFileSync(path.join(KONTEN, nama), "utf-8"));
  for (const m of lang.materi) {
    for (const s of m.sections) {
      for (const b of s.body || []) baris.push(b);
    }
  }
  for (const x of lang.latihan) {
    for (const q of x.question || []) baris.push(q);
    for (const t of x.hints || []) baris.push(t);
  }
}

for (const t of baris) {
  const js = acuan.berkode(t);
  const ts = segmenKode(t);
  adu(`segmenKode ${JSON.stringify(t).slice(0, 60)}`, js, ts);

  /* Kontrak penyambungan ulang, ditagih SENDIRI: potongan yang disambung
     kembali harus memberi teks aslinya -- dengan backtick dikembalikan, karena
     chip memang membuangnya. Kedua sisi bisa konsisten salah, dan hasil yang
     cocok tidak akan memberi tahu apa pun soal itu. Satu karakter yang hilang
     di sini berarti kalimat materi yang tampil berbeda dari yang ditulis. */
  const susun = ts.map((s) => (typeof s === "string" ? s : s.teks)).join("");
  const tanpaBacktick = t.replace(/`([^`]+)`/g, "$1");
  if (susun !== tanpaBacktick) takUtuh += 1;
}

/* --------------------------------------------------------- kasus pinggiran */

const PINGGIR = [
  "",
  "`",
  "``",
  "`kode`",
  "`a``b`",
  "<p> tidak boleh memuat <div>",
  "<br/>",
  "<br />",
  "</div>",
  "fungsi()",
  "obj.metode()",
  "_pribadi()",
  'class="kartu"',
  'data-gerak="penuh"',
  'alt="ini keterangan yang panjang sekali sampai lewat tiga puluh huruf"',
  "jawab.py",
  "Main.java",
  "gaya.css dan inti.js",
  "warna color grid flex",            // properti telanjang: TIDAK dikotaki
  "halo.txt halo.md halo.json",
  "1.py",
  "a-b.py",
  "teks `di tengah` kalimat",
  "`di awal` lalu teks",
  "teks lalu `di akhir`",
  '<a href="x">tautan</a>',
  "e.target.value",
  "print() dan input()",
];
PINGGIR.forEach((t, i) => {
  adu(`segmenKode pinggiran #${i}`, acuan.berkode(t), segmenKode(t));
});

console.log(`${baris.length} baris prosa, ${PINGGIR.length} pinggiran`);
if (takUtuh) {
  console.error(
    `PENYAMBUNGAN RUSAK: ${takUtuh} baris. Potongan yang disambung kembali ` +
      `tidak sama dengan teks aslinya, jadi kalimat materi akan tampil ` +
      `berbeda dari yang ditulis.`,
  );
}
if (gagal || takUtuh) {
  if (gagal) console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: segmenKode TypeScript identik dengan berkode di layar-belajar.js.");
