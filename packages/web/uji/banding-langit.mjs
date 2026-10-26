/* Adu bagian MURNI peta langit dengan `langit.js` yang masih melayani
 * antarmuka lama.
 *
 * Jenisnya sama dengan `banding-rasi.mjs`: bukan melawan rekaman, melainkan
 * melawan implementasi JS yang masih hidup -- keduanya JavaScript dan
 * fungsinya murni, jadi tidak ada sisi Python yang perlu direkam.
 *
 * Yang dijaganya: letak SETIAP bintang deterministik dari benih tetap (1801).
 * Satu bit yang meleset di `prng` menggeser seluruh langit, dan yang terlihat
 * tetap "langit berbintang" -- cuma langit yang berbeda, tanpa satu pun error.
 * Itu kelas kerusakan yang hanya pembanding bisa menangkap.
 *
 * `langit.js` mengimpor `gerak.js` dan menyentuh DOM di `nyalakanLangit()`,
 * jadi yang diambil POTONGAN sumbernya -- `prng`, `jariMag`, dan badan
 * `bangkitkan()` -- bukan modulnya. Potongan yang tidak ketemu membuat alat
 * ini MENOLAK, bukan membandingkan nol fungsi.
 */

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

import { bangkitkanBintang, bintangTerang, jariMag, prng }
  from "../src/langit-bentuk.ts";

const SINI = dirname(fileURLToPath(import.meta.url));
const AKAR = resolve(SINI, "../../..");
const sumber = readFileSync(
  resolve(AKAR, "webapp/statik/js/langit.js"), "utf-8");

function potong(pola, nama) {
  const m = sumber.match(pola);
  if (!m) {
    console.error(`GAGAL: potongan \`${nama}\` tidak ketemu di langit.js. `
      + "Pembanding yang kehilangan acuannya MENOLAK, bukan membandingkan "
      + "nol fungsi.");
    process.exit(1);
  }
  return m[0];
}

const kodeAcuan = [
  potong(/function prng\(benih\) \{[\s\S]*?\n\}/, "prng"),
  potong(/const jariMag = [^;]+;/, "jariMag"),
  `
  function bangkitkanAcuan(lebar, tinggi) {
    ${potong(/const acak = prng\(1801\);[\s\S]*?terang = bintang\.filter\([^;]+;/,
             "badan bangkitkan()")
      .replace(/^\s*bintang = \[\];/m, "let bintang = [];")
      .replace(/let bintang = \[\];/, "let bintang = [];")
      .replace(/terang = bintang\.filter/, "const terang = bintang.filter")}
    return { bintang, terang };
  }
  export { prng, jariMag, bangkitkanAcuan };
  `,
].join("\n");

const acuan = await import(
  "data:text/javascript," + encodeURIComponent(kodeAcuan));

let cacah = 0, beda = 0;
const adu = (nama, a, b) => {
  cacah += 1;
  if (JSON.stringify(a) !== JSON.stringify(b)) {
    beda += 1;
    if (beda <= 5) {
      console.error(`BEDA ${nama}\n  js: ${JSON.stringify(a)?.slice(0, 120)}`
        + `\n  ts: ${JSON.stringify(b)?.slice(0, 120)}`);
    }
  }
};

/* --------------------------------------------------------------- prng */
for (const benih of [1801, 1610, 0, 1, -1, 2 ** 31 - 1, -(2 ** 31), 123456789]) {
  const a = acuan.prng(benih), b = prng(benih);
  const kiri = [], kanan = [];
  for (let i = 0; i < 200; i++) { kiri.push(a()); kanan.push(b()); }
  adu(`prng(${benih})`, kiri, kanan);
}

/* ------------------------------------------------------------ jariMag */
for (let mag = -2; mag <= 8; mag++) {
  adu(`jariMag(${mag})`, acuan.jariMag(mag), jariMag(mag));
}

/* ------------------------------------------------- sebaran bintangnya */
const UKURAN = [
  [1472, 932], [1952, 1112], [1312, 800], [392, 700], [2592, 1472],
  [1000, 1000], [1, 1], [5000, 3000],
];
for (const [w, h] of UKURAN) {
  const a = acuan.bangkitkanAcuan(w, h);
  const bintang = bangkitkanBintang(w, h);
  adu(`bintang ${w}x${h}`, a.bintang, bintang);
  adu(`terang ${w}x${h}`, a.terang, bintangTerang(bintang));
}

const jml = bangkitkanBintang(1472, 932).length;
console.log(`${cacah} perbandingan, ${jml} bintang pada 1472x932`);
if (beda) {
  console.error(`BEDA: ${beda} dari ${cacah}.`);
  process.exit(1);
}
console.log("COCOK: peta langit TypeScript identik dengan langit.js.");
