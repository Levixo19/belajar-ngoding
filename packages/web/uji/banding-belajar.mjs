/* Adu bagian murni pembaca materi dengan `webapp/statik/js/layar-belajar.js`.
 *
 * `labelPeta` memutuskan apa yang terbaca di peta bagian -- permukaan yang
 * dipakai untuk MELIRIK, bukan untuk membaca. Ia rusak dengan cara yang tidak
 * kelihatan: potongan yang jatuh di tempat salah tetap terlihat sebagai label
 * yang wajar, cuma berhenti memberi tahu isi di baliknya. Tiga ambangnya (8,
 * 52, 44) dan dua jalur potongnya (batas kalimat, batas kata) saling tumpang
 * tindih, dan yang menemukan kombinasi yang salah bukan contoh yang ditulis
 * tangan.
 *
 * Korpusnya tiap baris `body` kurikulum, disintesis jadi satu blok prosa. Itu
 * bukan bentuk yang sampai ke `labelPeta` di aplikasi -- di sana bloknya sudah
 * lewat `isi.blok_badan` di server -- tapi yang diuji FUNGSINYA atas teks,
 * dan teks itulah teks yang sama. Bentuk yang hanya ada di server ditambahkan
 * sebagai kasus pinggiran di bawah.
 *
 *     node uji/banding-belajar.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { labelPeta, potong } from "../src/layar/belajar-teks.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "layar-belajar.js");
const KONTEN = path.join(AKAR, "packages", "konten", "kurikulum");

const teks = readFileSync(SUMBER, "utf-8");

function potongSumber(pola, nama) {
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
  potongSumber(/function potong\(t, n\) \{[\s\S]*?\n\}/, "potong"),
  potongSumber(/function labelPeta\(bg\) \{[\s\S]*?\n\}/, "labelPeta"),
];

const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-belajar-")),
  "acuan.mjs",
);
writeFileSync(jalurTemp, bagian.join("\n") + "\nexport {potong, labelPeta};\n");
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
const adu = (nama, a, b) => {
  // `String(JSON.stringify(...))`, bukan hasil mentahnya: `JSON.stringify`
  // mengembalikan `undefined` (nilai, bukan string) untuk masukan `undefined`,
  // dan `.slice` di atasnya melempar TypeError. Pagar yang MELEMPAR alih-alih
  // melapor tetap merah, tapi pesannya menunjuk berkas ini -- bukan ke
  // selisih yang baru saja ditemukannya.
  const sa = String(JSON.stringify(a));
  const sb = String(JSON.stringify(b));
  if (sa !== sb) {
    gagal += 1;
    if (gagal <= 5) {
      console.error(
        `  ${nama}\n    JS: ${sa.slice(0, 160)}\n    TS: ${sb.slice(0, 160)}`,
      );
    }
  }
};

/* --------------------------------------------------------------- korpus */

const baris = [];
const judul = [];
for (const nama of readdirSync(KONTEN).sort()) {
  const lang = JSON.parse(readFileSync(path.join(KONTEN, nama), "utf-8"));
  for (const m of lang.materi) {
    judul.push(m.title);
    for (const s of m.sections) {
      for (const b of s.body || []) baris.push(b);
    }
  }
  for (const x of lang.latihan) judul.push(x.title);
}

for (const t of baris) {
  adu(`labelPeta ${JSON.stringify(t).slice(0, 50)}`,
      acuan.labelPeta({ blok: [{ jenis: "teks", teks: t }] }),
      labelPeta({ blok: [{ jenis: "teks", teks: t }] }));
}

/* Judul materi dan latihan lewat `potong` di empat panjang yang benar-benar
   dipakai layar ini: 22 dan 26 di kaki pembaca, dan dua di sekitarnya supaya
   batas elipsisnya ikut teruji dari kedua sisi. */
for (const t of judul) {
  for (const n of [21, 22, 25, 26]) {
    adu(`potong(${n}) ${JSON.stringify(t).slice(0, 40)}`,
        acuan.potong(t, n), potong(t, n));
  }
}

/* --------------------------------------------------------- kasus pinggiran */

const PINGGIR = [
  { blok: [] },
  {},
  { blok: [{ jenis: "pra", teks: "kolom   kolom" }] },
  // `pra` dilewati, blok berikutnya yang dipakai.
  { blok: [{ jenis: "pra", teks: "tabel" }, { jenis: "teks", teks: "Prosanya." }] },
  { blok: [{ jenis: "teks", teks: "" }] },
  { blok: [{ jenis: "teks", teks: "   " }] },
  { blok: [{ jenis: "daftar", butir: [{ teks: "Butir pertama." }] }] },
  { blok: [{ jenis: "daftar", butir: [] }, { jenis: "teks", teks: "Sesudahnya." }] },
  // Titik tepat di batas 8 dan 52: keduanya ambang eksklusif.
  { blok: [{ jenis: "teks", teks: "12345678. sesudah titik" }] },
  { blok: [{ jenis: "teks", teks: "123456789. sesudah titik" }] },
  { blok: [{ jenis: "teks", teks: "a".repeat(51) + ". ekor" }] },
  { blok: [{ jenis: "teks", teks: "a".repeat(52) + ". ekor" }] },
  // Lewat 44 tanpa spasi sama sekali: batas kata tidak ketemu, dipotong keras.
  { blok: [{ jenis: "teks", teks: "x".repeat(60) }] },
  // Spasi ada tapi terlalu awal (<= 20): juga dipotong keras di 44.
  { blok: [{ jenis: "teks", teks: "ab " + "y".repeat(60) }] },
  { blok: [{ jenis: "teks", teks: "kata ".repeat(20) }] },
  // Spasi ganda dan baris baru diruntuhkan jadi satu spasi.
  { blok: [{ jenis: "teks", teks: "dua   spasi\ndan\tbaris baru." }] },
  { blok: [{ jenis: "teks", teks: "Tanya? lalu sisanya" }] },
  { blok: [{ jenis: "teks", teks: "Seru! lalu sisanya" }] },
  { blok: [{ jenis: "teks", teks: "Titik dua: lalu sisanya" }] },
  // Tanda baca di ujung TANPA spasi sesudahnya ikut cocok (`(\s|$)`).
  { blok: [{ jenis: "teks", teks: "Selesai di ujung." }] },
];
PINGGIR.forEach((bg, i) => {
  adu(`labelPeta pinggiran #${i}`, acuan.labelPeta(bg), labelPeta(bg));
});

const PINGGIR_POTONG = [
  [null, 10], [undefined, 10], ["", 10], ["abc", 0], ["abc", 1], ["abc", 3],
  ["abcd", 3], ["…", 1], ["halo dunia", 10], ["halo dunia", 9],
];
PINGGIR_POTONG.forEach(([t, n], i) => {
  adu(`potong pinggiran #${i}`, acuan.potong(t, n), potong(t, n));
});

console.log(`${baris.length} baris prosa, ${judul.length} judul x 4 panjang, ` +
            `${PINGGIR.length + PINGGIR_POTONG.length} pinggiran`);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: bagian murni pembaca materi identik dengan layar-belajar.js.");
