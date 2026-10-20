/* Adu bagian murni pratinjau versi TypeScript dengan `webapp/statik/js/pratinjau.js`.
 *
 * Yang dijaganya bukan "warnanya sama" melainkan HALAMAN YANG DIKARANG.
 * `halamanDariCss` menurunkan markup dari pemilih CSS pelajar, dan satu
 * perbedaan kecil di penguraiannya menghasilkan halaman tempat aturannya
 * TIDAK berlaku -- lalu yang dilihat pelajar adalah CSS-nya seolah tidak
 * bekerja, pada kode yang sebenarnya benar. Tidak ada error di mana pun.
 *
 * Korpusnya SELURUH blok kode kurikulum, dan tiap blok dilewatkan sebagai
 * `html` MAUPUN `css` tanpa peduli bahasa aslinya. Itu bukan kelalaian: yang
 * diuji penguraiannya, bukan klasifikasinya, dan memaksa setiap blok melewati
 * jalur CSS memberi `pemilihDi` ribuan masukan yang tidak ada seorang pun akan
 * memikirkannya sebagai lembar gaya.
 *
 * Pelapor tinggi (`PELAPOR`) diadu sebagai TEKS antara `pratinjau.js` dan
 * `Pratinjau.tsx` -- ia skrip yang dijalankan di dalam bingkai ber-asal buram,
 * jadi tidak ada cara mengujinya dari sini; yang bisa dijamin cuma bahwa
 * keduanya byte yang sama.
 *
 *     node uji/banding-pratinjau.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  adaMarkup,
  bisaDipratinjau,
  dokumenPratinjau,
  halamanDariCss,
  halamanDikarang,
} from "../src/komponen/pratinjau-css.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "pratinjau.js");
const KOMPONEN = path.join(SINI, "..", "src", "komponen", "Pratinjau.tsx");
const KONTEN = path.join(AKAR, "packages", "konten");

const teks = readFileSync(SUMBER, "utf-8");

function potong(pola, nama, dari = teks) {
  const cocok = dari.match(pola);
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
  potong(/const INDUK_WAJIB = \{[\s\S]*?\n\};/, "INDUK_WAJIB"),
  potong(/const TEKS_CONTOH = \{[\s\S]*?\n\};/, "TEKS_CONTOH"),
  potong(/const TEKS_BAWAAN = "[^"]*";/, "TEKS_BAWAAN"),
  potong(/const KOSONG = new Set\(\[[\s\S]*?\]\);/, "KOSONG"),
  potong(/const MAKS_CONTOH = \d+;/, "MAKS_CONTOH"),
  potong(/function tanpaKomentar\(css\) \{[\s\S]*?\n\}/, "tanpaKomentar"),
  potong(/function pemilihDi\(css\) \{[\s\S]*?\n\}/, "pemilihDi"),
  potong(/function uraiSederhana\(bagian\) \{[\s\S]*?\n\}/, "uraiSederhana"),
  potong(/function contohUntuk\(pemilih\) \{[\s\S]*?\n\}/, "contohUntuk"),
  potong(/export function halamanDariCss\(css\) \{[\s\S]*?\n\}/, "halamanDariCss"),
  potong(/export function adaMarkup\(kode\) \{[\s\S]*?\n\}/, "adaMarkup"),
  potong(/export function bisaDipratinjau\(runner\) \{[\s\S]*?\n\}/, "bisaDipratinjau"),
  potong(/export function dokumenPratinjau\(runner, kode\) \{[\s\S]*?\n\}/,
         "dokumenPratinjau"),
  potong(/export function halamanDikarang\(runner, kode\) \{[\s\S]*?\n\}/,
         "halamanDikarang"),
];

const kode = bagian.join("\n").replace(/^export /gm, "");
const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-pratinjau-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  kode +
    "\nexport {halamanDariCss, adaMarkup, bisaDipratinjau, dokumenPratinjau," +
    " halamanDikarang};\n",
);
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
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

/* ------------------------------------------- pelapor tinggi, byte demi byte */

const POLA_PELAPOR = /const PELAPOR = `[\s\S]*?`;/;
const pelaporJs = potong(POLA_PELAPOR, "PELAPOR di pratinjau.js");
const pelaporTs = potong(
  POLA_PELAPOR, "PELAPOR di Pratinjau.tsx", readFileSync(KOMPONEN, "utf-8"),
);
let pelaporBeda = 0;
if (pelaporJs !== pelaporTs) {
  pelaporBeda = 1;
  console.error(
    "PELAPOR BERBEDA. Skrip pengukur tinggi di dalam bingkai tidak sama " +
      "antara pratinjau.js dan Pratinjau.tsx. Ia jalan di asal buram, jadi " +
      "tidak ada cara lain mengujinya selain menuntut byte yang sama.",
  );
}

/* ---------------------------------------------------- korpus kode kurikulum */

const blok = [];
for (const nama of readdirSync(path.join(KONTEN, "kurikulum")).sort()) {
  const lang = JSON.parse(
    readFileSync(path.join(KONTEN, "kurikulum", nama), "utf-8"),
  );
  for (const m of lang.materi) {
    m.sections.forEach((s) => {
      if (s.code) blok.push({ nama: `${lang.key}/${m.title}`, kode: s.code });
    });
  }
  for (const x of lang.latihan) {
    if (x.solution) {
      blok.push({ nama: `${lang.key}/${x.title}`, kode: x.solution });
    }
  }
}

for (const b of blok) {
  adu(`adaMarkup ${b.nama}`, acuan.adaMarkup(b.kode), adaMarkup(b.kode));
  adu(`halamanDariCss ${b.nama}`,
      acuan.halamanDariCss(b.kode), halamanDariCss(b.kode));
  for (const runner of ["html", "css", "python"]) {
    adu(`dokumenPratinjau ${runner} ${b.nama}`,
        acuan.dokumenPratinjau(runner, b.kode),
        dokumenPratinjau(runner, b.kode));
    adu(`halamanDikarang ${runner} ${b.nama}`,
        acuan.halamanDikarang(runner, b.kode),
        halamanDikarang(runner, b.kode));
  }
}

/* --------------------------------------------------------- bisaDipratinjau */

for (const runner of ["html", "css", "python", "javascript", "", "HTML",
                      "terminal", "teks", "fedora", "git"]) {
  adu(`bisaDipratinjau ${runner || "(kosong)"}`,
      acuan.bisaDipratinjau(runner), bisaDipratinjau(runner));
}

console.log(`${blok.length} blok kode x 8 pemeriksaan, 10 nama runner`);
if (gagal || pelaporBeda) {
  if (gagal) console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: bagian murni pratinjau TypeScript identik dengan pratinjau.js.");
