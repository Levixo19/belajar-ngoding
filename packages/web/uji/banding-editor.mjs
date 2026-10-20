/* Adu bagian murni editor versi TypeScript dengan `webapp/statik/js/editor.js`.
 *
 * Ketiga fungsi ini punya kontrak yang keras: GABUNGAN seluruh `teks`
 * keluarannya wajib identik byte-per-byte dengan gabungan masukannya, karena
 * lapisan sorot duduk persis di bawah textarea yang transparan. Satu karakter
 * selisih membuat kursor mendarat di huruf yang salah pada baris panjang --
 * tanpa satu pun error di mana pun.
 *
 * Korpusnya SELURUH kode kurikulum, dibaca dari `packages/konten/`, bukan
 * contoh yang ditulis tangan. Dari 40.287 token operator ber-kurung di
 * kurikulum ini, 9.045 rengket dengan karakter lain -- bentuk yang mustahil
 * ditebak dan justru yang paling mudah salah.
 *
 *     node uji/banding-editor.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { bahasaDikenal, namaPenyorot, token } from "../../bersama/src/sorot.ts";
import {
  pisahInden,
  pisahKurung,
  posisiPita,
} from "../src/komponen/editor-teks.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "editor.js");
const KONTEN = path.join(AKAR, "packages", "konten");

const teks = readFileSync(SUMBER, "utf-8");

function potong(pola, nama) {
  const cocok = teks.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. Sumber editor.js mungkin ditulis ` +
        `ulang. Perbarui polanya, JANGAN biarkan pagar ini membandingkan nol ` +
        `fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const bagian = [
  // `[^}]*` tidak bisa dipakai di sini: nilai PASANGAN sendiri memuat `}`
  // (pasangan kurung kurawal), jadi polanya berhenti di tengah. Ia satu baris,
  // jadi `.*` tanpa bendera `s` justru yang benar.
  potong(/const PASANGAN = \{.*\};/, "PASANGAN"),
  potong(/const TUTUP_DARI = \{\};[\s\S]*?\n\}/, "TUTUP_DARI/BUKA_DARI"),
  potong(/const WARNA_KURUNG = \d+;/, "WARNA_KURUNG"),
  potong(/const YATIM = "[^"]*";/, "YATIM"),
  potong(/export function pisahKurung\(daftar\) \{[\s\S]*?\n\}/, "pisahKurung"),
  potong(/export function posisiPita\(\{[\s\S]*?\n\}/, "posisiPita"),
  potong(/export function pisahInden\(daftar\) \{[\s\S]*?\n\}/, "pisahInden"),
];

const kode = bagian.join("\n").replace(/^export /gm, "");
const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-editor-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  kode + "\nexport {pisahKurung, pisahInden, posisiPita};\n",
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
        `  ${nama}\n    JS: ${sa.slice(0, 160)}\n    TS: ${sb.slice(0, 160)}`,
      );
    }
  }
};

/* ---------------------------------------------------- korpus kode kurikulum */

function bahasaSorot(lang) {
  return bahasaDikenal(lang.key) ? lang.key : lang.runner;
}

const blok = [];
for (const nama of readdirSync(path.join(KONTEN, "kurikulum")).sort()) {
  const lang = JSON.parse(
    readFileSync(path.join(KONTEN, "kurikulum", nama), "utf-8"),
  );
  for (const m of lang.materi) {
    m.sections.forEach((s) => {
      if (s.code) {
        blok.push({
          nama: `${lang.key}/${m.title}`,
          bahasa: s.bahasa ? namaPenyorot(s.bahasa) : bahasaSorot(lang),
          kode: s.code,
        });
      }
    });
  }
  const bhs = bahasaSorot(lang);
  for (const x of lang.latihan) {
    if (x.solution) {
      blok.push({ nama: `${lang.key}/${x.title}`, bahasa: bhs, kode: x.solution });
    }
  }
}

for (const b of blok) {
  const t = token(b.kode, b.bahasa);
  const jsKurung = acuan.pisahKurung(t);
  const tsKurung = pisahKurung(t);
  adu(`pisahKurung ${b.nama}`, jsKurung, tsKurung);

  const jsInden = acuan.pisahInden(jsKurung);
  const tsInden = pisahInden(tsKurung);
  adu(`pisahInden ${b.nama}`, jsInden, tsInden);

  // Kontrak identitas-byte diperiksa sendiri, bukan cuma lewat perbandingan:
  // kedua sisi bisa konsisten salah, dan hasil yang cocok tidak akan memberi
  // tahu apa pun soal itu.
  if (tsInden.map((p) => p[1]).join("") !== b.kode) takUtuh += 1;
}

/* ------------------------------------------------------------- posisiPita */

for (const baris of [0, 1, 2, 40, 400]) {
  for (const tinggiBaris of [0, 21, 21.6]) {
    for (const paddingAtas of [0, 12]) {
      for (const scrollTop of [0, 828]) {
        const arg = { baris, tinggiBaris, paddingAtas, scrollTop };
        adu(
          `posisiPita ${JSON.stringify(arg)}`,
          acuan.posisiPita(arg),
          posisiPita(arg),
        );
      }
    }
  }
}

console.log(`${blok.length} blok kode, 60 kasus posisiPita`);
if (takUtuh) {
  console.error(
    `IDENTITAS BYTE RUSAK: ${takUtuh} blok. Gabungan teks keluaran tidak sama ` +
      `dengan masukannya; kursor akan mendarat di huruf yang salah.`,
  );
}
if (gagal || takUtuh) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: bagian murni editor TypeScript identik dengan editor.js.");
