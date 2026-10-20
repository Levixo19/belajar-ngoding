/* Adu bagian murni panel "Lihat jalannya" dengan `webapp/statik/js/jejak.js`.
 *
 * Dua fungsi, dua jenis risiko yang berbeda:
 *
 * `tokenPerBaris` memecah token server jadi baris. Panel menomori barisnya
 * sendiri dari hasil itu, lalu menyorot baris yang akan dijalankan dari nomor
 * yang dikirim pelacak Python. Satu baris yang hilang menggeser SELURUH sisa
 * sorotnya, dan tidak ada error di mana pun -- yang dipelajari orang jadi
 * urutan eksekusi yang tidak pernah terjadi. Karena itu kontrak penyambungan
 * ulangnya ditagih TERPISAH dari perbandingan: kedua sisi bisa konsisten
 * salah.
 *
 * `kalimat` cuma teks, tapi keempat cabangnya adalah satu-satunya penjelasan
 * yang dibaca pelajar tentang apa yang baru terjadi. Ia diadu atas kasus yang
 * disintesis di sini, karena menjalankan pelacak sungguhan butuh server --
 * dan korpusnya memang kecil dan bisa ditulis habis.
 *
 *     node uji/banding-jejak.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { bahasaDikenal, namaPenyorot, token } from "../../bersama/src/sorot.ts";
import { kalimat, tokenPerBaris } from "../src/komponen/jejak-teks.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "jejak.js");
const KONTEN = path.join(AKAR, "packages", "konten");

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
  potong(/function tokenPerBaris\(token\) \{[\s\S]*?\n\}/, "tokenPerBaris"),
  potong(/function kalimat\(l, adaBerikut\) \{[\s\S]*?\n\}/, "kalimat"),
];

const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-jejak-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  bagian.join("\n") + "\nexport {tokenPerBaris, kalimat};\n",
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
        `  ${nama}\n    JS: ${sa.slice(0, 180)}\n    TS: ${sb.slice(0, 180)}`,
      );
    }
  }
};

/* ------------------------------------- tokenPerBaris atas kode kurikulum */

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
}

for (const b of blok) {
  const t = token(b.kode, b.bahasa);
  const js = acuan.tokenPerBaris(t);
  const ts = tokenPerBaris(t);
  adu(`tokenPerBaris ${b.nama}`, js, ts);

  // Kontrak penyambungan ulang, ditagih sendiri: jumlah barisnya harus sama
  // dengan `split("\n")` kodenya, dan menyambungnya kembali harus memberi
  // kode yang sama. Kedua sisi bisa konsisten salah, dan hasil yang cocok
  // tidak akan memberi tahu apa pun soal itu.
  const susun = ts.map((l) => l.map((p) => p[1]).join("")).join("\n");
  if (susun !== b.kode || ts.length !== b.kode.split("\n").length) takUtuh += 1;
}

/* ----------------------------------- tokenPerBaris atas masukan pinggiran */

const PINGGIR = [
  null,
  undefined,
  [],
  [["teks", ""]],
  [["teks", "\n"]],
  [["teks", "\n\n\n"]],
  [["kunci", "def"], ["teks", " f():\n    "], ["kunci", "pass"]],
  [["teks", "a\nb"], ["teks", "c\nd"]],
  [["string", '"""\nbaris\n"""'], ["teks", "\n"]],
  [["teks", "akhir\n"]],
];
PINGGIR.forEach((t, i) => {
  adu(`tokenPerBaris pinggiran #${i}`, acuan.tokenPerBaris(t), tokenPerBaris(t));
});

/* ------------------------------------------------------- kalimat, 4 cabang */

const BINGKAI_KOSONG = { nama: "program utama", baris: 1, isi: {} };
const BINGKAI_ISI = {
  nama: "hitung", baris: 7,
  isi: { n: { r: "3", t: "int" }, data: { r: "[1, 2]", t: "list", id: 2 } },
};
const LANGKAH = [
  { baris: 1, p: "baris", tumpukan: [BINGKAI_KOSONG], keluar: 0 },
  { baris: 9, p: "baris", tumpukan: [], keluar: 0 },
  { baris: 7, p: "panggil", tumpukan: [BINGKAI_KOSONG, BINGKAI_ISI], keluar: 0 },
  { baris: 7, p: "panggil", tumpukan: [BINGKAI_KOSONG], keluar: 0 },
  { baris: 7, p: "panggil", tumpukan: [], keluar: 0 },
  { baris: 8, p: "kembali", tumpukan: [BINGKAI_ISI], keluar: 4,
    nilai: { r: "6", t: "int" } },
  { baris: 8, p: "kembali", tumpukan: [BINGKAI_ISI], keluar: 4, nilai: null },
  { baris: 8, p: "kembali", tumpukan: [], keluar: 4 },
  { baris: 3, p: "galat", tumpukan: [BINGKAI_KOSONG], keluar: 0,
    galat: "ZeroDivisionError: division by zero" },
  { baris: 3, p: "galat", tumpukan: [], keluar: 0 },
  { baris: 5, p: "jenis-yang-tidak-ada", tumpukan: [BINGKAI_ISI], keluar: 1 },
];
let kasusKalimat = 0;
for (const l of LANGKAH) {
  for (const ada of [true, false]) {
    kasusKalimat += 1;
    adu(`kalimat ${l.p} ${l.tumpukan.length} ${ada}`,
        acuan.kalimat(l, ada), kalimat(l, ada));
  }
}

console.log(`${blok.length} blok kode, ${PINGGIR.length} masukan pinggiran, ` +
            `${kasusKalimat} kasus kalimat`);
if (takUtuh) {
  console.error(
    `PENYAMBUNGAN RUSAK: ${takUtuh} blok. Baris hasil tokenPerBaris tidak ` +
      `menyusun kembali kodenya, jadi nomor baris di panel akan menunjuk ` +
      `baris yang salah.`,
  );
}
if (gagal || takUtuh) {
  if (gagal) console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: bagian murni jejak TypeScript identik dengan jejak.js.");
