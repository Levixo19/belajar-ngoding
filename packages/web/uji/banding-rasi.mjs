/* Adu geometri rasi versi TypeScript dengan `webapp/statik/js/rasi.js`.
 *
 * Bentuk tiap rasi deterministik dari benihnya (nama kurikulum), jadi satu bit
 * yang meleset di `hash` atau `prng` mengubah SETIAP rasi -- tanpa satu pun
 * error, cuma peta langit yang tidak lagi sama dengan yang dilihat pelajar
 * kemarin. Itu jenis pergeseran yang tidak akan ada yang laporkan sebagai bug.
 *
 * Versi JS mengimpor `inti.js` yang butuh DOM, jadi fungsi murninya tidak bisa
 * diimpor langsung di Node. Yang dilakukan di sini: AMBIL potongan sumbernya
 * dengan regex lalu evaluasi. Itu rapuh terhadap penulisan ulang -- karena itu
 * ia MENOLAK kalau salah satu potongan tidak ketemu, alih-alih diam-diam
 * membandingkan nol fungsi.
 *
 *     node uji/banding-rasi.mjs
 */

import { mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  bentukRasi,
  hash,
  jariBintang,
  magStatus,
  berikutDari,
  ruasAntara,
} from "../src/komponen/rasi-geometri.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "rasi.js");

const teks = readFileSync(SUMBER, "utf-8");

/** Ambil satu deklarasi tingkat-atas dari sumber JS, apa adanya. */
function potong(pola, nama) {
  const cocok = teks.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. Sumber rasi.js mungkin ditulis ulang. ` +
        `Perbarui polanya di uji/banding-rasi.mjs, JANGAN biarkan pagar ini ` +
        `membandingkan nol fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const bagian = [
  potong(/export function hash\(teks\) \{[\s\S]*?\n\}/, "hash"),
  potong(/function prng\(benih\) \{[\s\S]*?\n\}/, "prng"),
  potong(/export const jariBintang = [^;]+;/, "jariBintang"),
  potong(/const MAG = \{[^}]*\};/, "MAG"),
  potong(/export const magStatus = [^;]+;/, "magStatus"),
  potong(/export function bentukRasi\(n, benih, w, h\) \{[\s\S]*?\n\}/, "bentukRasi"),
  potong(/export function berikutDari\(materi\) \{[\s\S]*?\n\}/, "berikutDari"),
];

/* Potongannya ditulis ke berkas sementara lalu DIIMPOR, bukan dijalankan
 * lewat `new Function`. Dua alasan, dan yang kedua yang praktis:
 *
 * * `new Function` atas string yang disusun program adalah bentuk yang sama
 *   dengan injeksi kode. Di sini sumbernya berkas repo sendiri, jadi batas
 *   percayanya sama dengan mengimpor modul repo mana pun -- tapi bentuk yang
 *   tidak perlu dibela lebih baik daripada bentuk yang perlu.
 * * Galat sintaks di dalam `new Function` dilaporkan tanpa nomor baris yang
 *   berguna. Sebagai modul, Node menunjuk barisnya.
 */
const kode = bagian.join("\n").replace(/^export /gm, "");
const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-rasi-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  kode + "\nexport {hash, prng, jariBintang, magStatus, bentukRasi, berikutDari};\n",
);
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
const adu = (nama, a, b) => {
  const sa = JSON.stringify(a);
  const sb = JSON.stringify(b);
  if (sa !== sb) {
    gagal += 1;
    console.error(`  ${nama}\n    JS: ${sa}\n    TS: ${sb}`);
  }
};

// Benih nyata: kunci kurikulum yang dipakai aplikasi, plus bentuk pinggiran.
const BENIH = [
  "python", "java", "javascript", "c", "cpp", "sql", "bash", "html", "css",
  "go", "git", "fedora", "aplikasi", "techstack", "frontend", "backend",
  "database", "mobile", "game", "iot", "devops", "keamanan", "data", "ai",
  "bahasalain", "", "a", "kurikulum-yang-namanya-sangat-panjang-sekali",
];

for (const benih of BENIH) {
  adu(`hash(${JSON.stringify(benih)})`, acuan.hash(benih), hash(benih));
  for (const n of [0, 1, 2, 3, 7, 12, 44, 83]) {
    adu(
      `bentukRasi(${n}, ${JSON.stringify(benih)})`,
      acuan.bentukRasi(n, benih, 1000, 250),
      bentukRasi(n, benih, 1000, 250),
    );
  }
}

for (const mag of [0, 1, 1.5, 3, 5, 6, 12]) {
  for (const skala of [1, 0.5, 2.25]) {
    adu(
      `jariBintang(${mag}, ${skala})`,
      acuan.jariBintang(mag, skala),
      jariBintang(mag, skala),
    );
  }
}

const CONTOH = [
  { judul: "a", status: "selesai" },
  { judul: "b", status: "sebagian" },
  { judul: "c", status: "baru" },
  { judul: "d", status: "baru", terkunci: true },
  { judul: "e", status: "entah-apa" },
];
for (const m of CONTOH) {
  adu(`magStatus(${m.judul})`, acuan.magStatus(m), magStatus(m));
}
adu("berikutDari(contoh)", acuan.berikutDari(CONTOH), berikutDari(CONTOH));
adu(
  "berikutDari(semua selesai)",
  acuan.berikutDari([{ judul: "x", status: "selesai" }]),
  berikutDari([{ judul: "x", status: "selesai" }]),
);

// `ruas` versi JS menghasilkan elemen SVG, jadi yang diadu KOORDINATNYA:
// nilai yang sama yang dipasang ke atribut x1/y1/x2/y2 di sana.
const PASANG = [
  [[0, 0], [100, 0], 3, 3],
  [[0, 0], [5, 0], 3, 3],
  [[10, 20], [-30, 44], 1.1, 5.2],
  [[0, 0], [0, 0], 1, 1],
];
for (const [a, b, ra, rb] of PASANG) {
  const d = Math.hypot(b[0] - a[0], b[1] - a[1]);
  const harap =
    d < ra + rb + 4
      ? null
      : {
          x1: Number((a[0] + ((b[0] - a[0]) / d) * (ra + 3)).toFixed(1)),
          y1: Number((a[1] + ((b[1] - a[1]) / d) * (ra + 3)).toFixed(1)),
          x2: Number((b[0] - ((b[0] - a[0]) / d) * (rb + 3)).toFixed(1)),
          y2: Number((b[1] - ((b[1] - a[1]) / d) * (rb + 3)).toFixed(1)),
        };
  const nyata = ruasAntara(a, b, ra, rb);
  const bulat =
    nyata === null
      ? null
      : {
          x1: Number(nyata.x1.toFixed(1)),
          y1: Number(nyata.y1.toFixed(1)),
          x2: Number(nyata.x2.toFixed(1)),
          y2: Number(nyata.y2.toFixed(1)),
        };
  adu(`ruasAntara(${JSON.stringify([a, b, ra, rb])})`, harap, bulat);
}

const cacah = BENIH.length * 9 + 21 + CONTOH.length + 2 + PASANG.length;
console.log(`${cacah} perbandingan atas ${BENIH.length} benih`);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: geometri rasi TypeScript identik dengan rasi.js.");
