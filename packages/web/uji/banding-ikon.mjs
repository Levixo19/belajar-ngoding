/* Adu ikon versi TypeScript dengan `webapp/statik/js/ikon.js`.
 *
 * Tabel jalurnya DISALIN, bukan diimpor -- dan salinan adalah hal yang paling
 * mudah melenceng tanpa tanda. Satu koordinat yang salah ketik menghasilkan
 * ikon yang tetap tergambar, tetap tanpa error di konsol, dan cuma terlihat
 * sedikit aneh. Yang dibandingkan di sini SETIAP atribut setiap `<path>`, plus
 * atribut `<svg>` pembungkusnya, untuk ke-26 ikon pada empat ukuran.
 *
 * Satu cabang diuji khusus: `fill: currentColor` dipasang berdasarkan INDEKS,
 * bukan bentuk jalurnya. Penjaga lama di sisi JS memeriksa `d.endsWith("18Z")`
 * dan KEDUA jalur ikon "sedang" kebetulan berakhir begitu, jadi separuh
 * lingkarannya tidak pernah terisi dan ikon "sedang dikerjakan" tak bisa
 * dibedakan dari "belum". Pagar ini menagih keadaan sesudah perbaikan itu.
 *
 *     node uji/banding-ikon.mjs
 */

import { mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  ikonTipe,
  isiJalur,
  jalurIkon,
  NAMA_IKON,
} from "../src/komponen/ikon-bentuk.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "ikon.js");

/* ------------------------------------------------------------- shim DOM */

class Elemen {
  constructor(tag) {
    this.tag = tag;
    this.sifat = {};
    this.anak = [];
    this.gaya = {};
    this.style = new Proxy(this.gaya, {
      set: (o, k, v) => { o[k] = String(v); return true; },
    });
  }
  setAttribute(k, v) { this.sifat[k] = String(v); }
  appendChild(n) { this.anak.push(n); return n; }
}
globalThis.document = { createElementNS: (_ns, tag) => new Elemen(tag) };

/* --------------------------------------------- muat ikon.js apa adanya

   Tidak ada irisan regex di sini: `ikon.js` tidak mengimpor apa pun, jadi ia
   bisa dimuat utuh begitu `document.createElementNS` ada. Yang diubah cuma
   `.js` -> berkas sementara, supaya resolusi modulnya tidak bergantung pada
   di mana pembanding ini dijalankan. */
const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-ikon-")),
  "acuan.mjs",
);
writeFileSync(jalurTemp, readFileSync(SUMBER, "utf-8"));
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
let cacah = 0;
const adu = (nama, a, b) => {
  cacah += 1;
  const sa = JSON.stringify(a);
  const sb = JSON.stringify(b);
  if (sa !== sb) {
    gagal += 1;
    console.error(`  ${nama}\n    JS: ${sa}\n    TS: ${sb}`);
  }
};

/* Daftar nama diadu LEBIH DULU: pembanding yang mengulang nol ikon akan
   melaporkan "cocok" dengan sempurna, dan itu kegagalan yang paling mahal di
   sini karena ia terbaca seperti keberhasilan. */
adu("NAMA_IKON", acuan.NAMA_IKON, NAMA_IKON);
if (NAMA_IKON.length < 20) {
  console.error(`KORPUS TERLALU KECIL: ${NAMA_IKON.length} ikon.`);
  process.exit(1);
}

/** Bentuk `<svg>` versi TS, meniru `Ikon.tsx` -- atribut yang sama, urutan
 *  yang sama. Batasnya sama dengan `banding-visual.mjs`: yang dibuktikan
 *  identik LAPISAN MURNI-nya, dan komponennya memang dijaga tipis. */
function dariTs(nama, ukuran, tebal, kelas) {
  const jalur = jalurIkon(nama);
  if (!jalur) return null;
  return {
    tag: "svg",
    sifat: {
      viewBox: "0 0 24 24",
      width: String(ukuran),
      height: String(ukuran),
      fill: "none",
      stroke: "currentColor",
      "stroke-width": String(tebal),
      "stroke-linecap": "round",
      "stroke-linejoin": "round",
      "aria-hidden": "true",
      focusable: "false",
      ...(kelas ? { class: kelas } : {}),
    },
    gaya: { flex: "none" },
    anak: jalur.map((d, i) => ({
      tag: "path",
      sifat: { d, ...(isiJalur(nama, i) ? { fill: "currentColor" } : {}) },
    })),
  };
}

/** Elemen shim -> bentuk yang sama. */
function dariJs(el) {
  if (!el) return null;
  return {
    tag: el.tag,
    sifat: el.sifat,
    gaya: el.gaya,
    anak: el.anak.map((a) => ({ tag: a.tag, sifat: a.sifat })),
  };
}

const UKURAN = [
  [20, 1.7, ""], [13, 2, ""], [17, 1.7, ""], [14, 1.9, "pil-ikon"],
];

for (const nama of NAMA_IKON) {
  for (const [ukuran, tebal, kelas] of UKURAN) {
    const opsi = { ukuran, tebal, ...(kelas ? { kelas } : {}) };
    adu(
      `ikon(${nama}, ${ukuran}/${tebal}${kelas ? "/" + kelas : ""})`,
      dariJs(acuan.ikon(nama, opsi)),
      dariTs(nama, ukuran, tebal, kelas),
    );
  }
}

/* Bawaan tanpa opsi, dan nama yang TIDAK ada: keduanya cabang sendiri. */
adu("ikon(materi) bawaan", dariJs(acuan.ikon("materi")), dariTs("materi", 20, 1.7, ""));
adu("ikon(tidak-ada)", dariJs(acuan.ikon("tidak-ada")), dariTs("tidak-ada", 20, 1.7, ""));

for (const tipe of ["materi", "kuis", "latihan", "bacaan", "", "entah"]) {
  adu(`ikonTipe(${JSON.stringify(tipe)})`, acuan.ikonTipe(tipe), ikonTipe(tipe));
}

console.log(`${cacah} perbandingan atas ${NAMA_IKON.length} ikon`);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: ikon TypeScript identik dengan ikon.js.");
