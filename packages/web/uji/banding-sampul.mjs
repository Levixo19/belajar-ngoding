/* Adu geometri sampul dengan `sampul.js` yang masih melayani antarmuka lama.
 *
 * `sampul.js` membangun SVG lewat `document.createElementNS`, jadi yang
 * dipasang di sini shim DOM minimal yang MEREKAM apa yang digambar. Itu lebih
 * jujur daripada mengadu dua tabel: yang dibandingkan benar-benar hasil
 * pemanggilan fungsinya, bukan niat penulisnya.
 *
 * Yang dijaganya: satu bit yang meleset di `benih` atau `acak` mengubah
 * SETIAP sampul di aplikasi, dan yang terlihat tetap "gambar geometris" --
 * cuma gambar yang lain. Tidak ada error di mana pun.
 */

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

import { benih, acak, rencanaSampul, setelNomorSampul }
  from "../src/komponen/sampul-bentuk.ts";

const SINI = dirname(fileURLToPath(import.meta.url));
const AKAR = resolve(SINI, "../../..");

/* --------------------------------------------------- shim DOM perekam --- */
class ElPalsu {
  constructor(tag) { this.tag = tag; this.sifat = {}; this.anak = []; }
  setAttribute(k, v) { this.sifat[k] = v; }
  append(...a) { this.anak.push(...a); }
}
globalThis.document = {
  createElementNS: (_ns, tag) => new ElPalsu(tag),
  createTextNode: (t) => ({ tag: "#teks", teks: t }),
};
// `sampul.js` mengimpor `h` dari inti.js, dan inti.js menyentuh banyak DOM
// saat diimpor. Yang dipakai cuma `kepalaBersampul`, yang TIDAK diuji di
// sini, jadi modulnya dialihkan ke stub lewat penulisan ulang impor.
const sumber = readFileSync(resolve(AKAR, "webapp/statik/js/sampul.js"), "utf-8")
  .replace('import { h } from "./inti.js";',
           "const h = () => { throw new Error('h tidak dipakai di sini'); };");
const acuan = await import(
  "data:text/javascript," + encodeURIComponent(sumber));

/* ------------------------------------------------------------- adu ------ */
let cacah = 0, beda = 0;
/* `setAttribute` memaksa SEMUA nilai jadi string, sementara deskriptor di
 * sisi TS menyimpan angka apa adanya. Jadi yang diadu bentuk ter-STRING-kan
 * di kedua sisi -- penyetaraan itu milik pembandingnya, bukan sumbernya:
 * memaksa lapisan geometri menyimpan string akan membuatnya membawa jejak
 * DOM yang tidak ada hubungannya dengan geometri. Jebakan yang sama pernah
 * memberi 198 "beda" palsu di `banding-rasi.mjs`. */
const keString = (x) => {
  if (Array.isArray(x)) return x.map(keString);
  if (x && typeof x === "object") {
    return Object.fromEntries(
      Object.entries(x).map(([k, v]) => [k, keString(v)]));
  }
  return typeof x === "number" ? String(x) : x;
};

const adu = (nama, a, b) => {
  cacah += 1;
  const ka = JSON.stringify(keString(a)), kb = JSON.stringify(keString(b));
  if (ka !== kb) {
    beda += 1;
    if (beda <= 4) {
      console.error(`BEDA ${nama}\n  js: ${ka?.slice(0, 160)}\n  ts: ${kb?.slice(0, 160)}`);
    }
  }
};

/* Yang diadu BENTUKNYA, bukan id gradiennya: `idg` memuat penomor global yang
   memang sengaja berbeda tiap pemanggilan, dan menuntutnya sama berarti
   menuntut dua modul berbagi satu penghitung. */
function bentukDariSvg(svg) {
  return svg.anak
    .filter((e) => e instanceof ElPalsu
      && ["circle", "rect", "path"].includes(e.tag)
      // dua rect pertama (latar + gradien) dan rect terakhir (grain) bukan
      // bagian komposisinya
      && !("filter" in e.sifat) && !(e.sifat.fill || "").startsWith("url(")
      && e.sifat.style !== "fill: var(--kartu)")
    .map((e) => ({ tag: e.tag, sifat: e.sifat }));
}

const BENIH = [
  "python", "html", "css", "javascript", "go", "rust", "bab-1", "bab-12",
  "python/bab-3", "karier/backend", "", "a", "Proyek Akhir", "ruby",
  "kurikulum yang namanya sangat panjang sekali untuk menguji hash",
];
const UKURAN = [[640, 360], [560, 400], [960, 200], [320, 180]];
const BAHASA = [null, "python", "html", "tidak-ada-di-tabel"];

/* `benih` dan `acak` TIDAK diekspor `sampul.js`, jadi acuannya DIPOTONG dari
 * sumbernya -- bukan disalin ke sini. Versi pertama pembanding ini menyalin
 * rumus FNV-nya ke dalam berkas ini lalu mengadu salinan itu dengan port:
 * fikstur yang menyalin predikatnya tidak membuktikan apa pun tentang
 * acuannya, dan ia akan tetap hijau kalau `sampul.js` yang bergeser.
 * Baterai mutasi yang menangkapnya -- dua sel merah dengan alasan yang salah.
 */
function potong(pola, nama) {
  const m = sumber.match(pola);
  if (!m) {
    console.error(`GAGAL: potongan \`${nama}\` tidak ketemu di sampul.js.`);
    process.exit(1);
  }
  return m[0];
}
const inti = await import("data:text/javascript," + encodeURIComponent([
  potong(/function benih\(teks\) \{[\s\S]*?\n\}/, "benih"),
  potong(/function acak\(benihAwal\) \{[\s\S]*?\n\}/, "acak"),
  "export { benih, acak };",
].join("\n")));

for (const t of BENIH) {
  adu(`benih(${JSON.stringify(t)})`, inti.benih(t), benih(t));
}

for (const b of [1, 0, 7919, 2 ** 31 - 1, -(2 ** 31), 123456789]) {
  const ja = inti.acak(b), ts = acak(b);
  const kiri = [], kanan = [];
  for (let i = 0; i < 60; i++) { kiri.push(ja()); kanan.push(ts()); }
  adu(`acak(${b})`, kiri, kanan);
}

for (const t of BENIH) {
  for (const [w, h] of UKURAN) {
    for (const bhs of BAHASA) {
      const opsi = { lebar: w, tinggi: h, bahasa: bhs, tanda: true };
      const svg = acuan.sampul(t, opsi);
      setelNomorSampul(0);
      const r = rencanaSampul(t, opsi);
      adu(`bentuk ${JSON.stringify(t)} ${w}x${h} ${bhs}`,
          bentukDariSvg(svg), r.bentuk);
      adu(`ragam ${JSON.stringify(t)} ${w}x${h} ${bhs}`,
          svg.sifat["data-ragam"], r.ragam);
      const teksJs = svg.anak.find((e) => e instanceof ElPalsu && e.tag === "text");
      adu(`tanda ${JSON.stringify(t)} ${bhs}`,
          teksJs ? teksJs.anak[0].teks : null, r.tanda);
    }
  }
}

console.log(`${cacah} perbandingan atas ${BENIH.length} benih x ${UKURAN.length} ukuran`);
if (beda) {
  console.error(`BEDA: ${beda} dari ${cacah}.`);
  process.exit(1);
}
console.log("COCOK: geometri sampul TypeScript identik dengan sampul.js.");
