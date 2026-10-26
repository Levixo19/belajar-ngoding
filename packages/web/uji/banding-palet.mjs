/* Adu pencocok palet perintah dengan `webapp/statik/js/aplikasi.js`.
 *
 * Yang dikerjakan palet adalah MENGURUTKAN, dan urutan yang salah tidak pernah
 * menimbulkan error -- ia cuma menaruh hal yang dicari orang di baris kedua
 * belas. Pagar ini karena itu mengadu URUTAN penuh, bukan sekadar keanggotaan:
 * dua daftar yang isinya sama tapi tersusun lain adalah dua palet yang
 * berbeda.
 *
 * Empat lapisan diadu:
 *
 * * `skorBerurutan` -- angka mentahnya, bukan cuma cocok/tidak. Bonus batas
 *   kata (8), bonus awal teks (4), dan bobot huruf (2) menentukan siapa menang
 *   di antara kandidat yang sama-sama cocok.
 * * `diBatasKata` -- dibaca pada teks ASLI, jadi transisi kecil->besar
 *   (`scrollTop`) ikut terhitung batas kata.
 * * `saringPerintah` -- urutan hasilnya, termasuk stabilitas `sort` untuk
 *   baris berskor sama dan efek bonus riwayat.
 * * `riwayatPotong` / `riwayatNaikkan` -- umur 14 hari dan "satu alamat satu
 *   butir".
 *
 *     node uji/banding-palet.mjs
 */

import { mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  diBatasKata, GRUP_PALET, kelompokkan, riwayatNaikkan, riwayatPotong,
  saringPerintah, skorBerurutan,
} from "../src/komponen/palet-cari.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "aplikasi.js");
const KONTEN = path.join(AKAR, "packages", "konten", "kurikulum");

const teks = readFileSync(SUMBER, "utf-8");

function potong(pola, nama) {
  const cocok = teks.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. aplikasi.js mungkin ditulis ulang. ` +
        `Perbarui polanya di uji/banding-palet.mjs, JANGAN biarkan pagar ini ` +
        `membandingkan nol fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const bagian = [
  potong(/const SKOR_GAGAL = -1;/, "SKOR_GAGAL"),
  potong(/const BOBOT_HURUF = \d+;/, "BOBOT_HURUF"),
  potong(/const BONUS_BATAS = \d+;/, "BONUS_BATAS"),
  potong(/const BONUS_AWAL = \d+;/, "BONUS_AWAL"),
  potong(/const BONUS_RIWAYAT = \d+;/, "BONUS_RIWAYAT"),
  potong(/const HARI_MS = \d+;/, "HARI_MS"),
  potong(/function diBatasKata\(teks, i\) \{[\s\S]*?\n\}/, "diBatasKata"),
  potong(/function skorBerurutan\(teks, kata\) \{[\s\S]*?\n\}/, "skorBerurutan"),
  potong(/function saringPerintah\(daftar, kata, riwayat = \[\]\) \{[\s\S]*?\n\}/,
         "saringPerintah"),
  potong(/function riwayatPotong\(riwayat, sekarang, batasHari = 14\) \{[\s\S]*?\n\}/,
         "riwayatPotong"),
  potong(/function riwayatNaikkan\(riwayat, k, sekarang\) \{[\s\S]*?\n\}/,
         "riwayatNaikkan"),
  potong(/const GRUP_PALET = \[[\s\S]*?\n\];/, "GRUP_PALET"),
];

const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-palet-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  bagian.join("\n") +
    `
export { diBatasKata, skorBerurutan, saringPerintah, riwayatPotong,
         riwayatNaikkan, GRUP_PALET, SKOR_GAGAL };
`,
);
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

/* ----------------------------------------------------------------- korpus

   Teksnya diambil dari isi aplikasi yang SUNGGUHAN -- label perintah, nama
   kurikulum, dan judul materi -- bukan dikarang: yang dicari orang di palet
   ini persis itu, dan bentuk nama di kurikulum ini (camelCase, garis bawah,
   titik) justru kelas yang paling menentukan di `diBatasKata`. */

import { readdirSync } from "node:fs";

const JUDUL = [];
const BAHASA = [];
for (const nama of readdirSync(KONTEN).sort()) {
  const k = JSON.parse(readFileSync(path.join(KONTEN, nama), "utf-8"));
  BAHASA.push({
    key: k.key,
    label: k.label,
    materi: k.materi.length,
    kuis: (k.kuis_mentah || []).length,
    latihan: (k.latihan || []).length,
  });
  for (const m of k.materi.slice(0, 6)) JUDUL.push(m.title);
}

const TEKS_UJI = [
  ...BAHASA.map((b) => b.label),
  ...JUDUL,
  "Dasbor", "Ruang Coba", "Catatanku", "Bookmark", "Statistik", "Pengaturan",
  "Pustaka", "Peta Karier", "Langit", "Cari",
  // Bentuk yang menguji `diBatasKata` secara langsung.
  "scrollTop", "tipeData", "satu_dua", "satu-dua", "satu/dua", "satu dua",
  "ABC", "aBc", "", "a", "  spasi di depan", "AWAL besar", "x1y2z3",
];

const KUERI = [
  "", "a", "p", "py", "python", "stk", "kts", "bh", "ds", "db",
  "cat", "catatanku", "ruang", "rc", "xp", "materi", "kuis", "latihan",
  "SCROLL", "scrolltop", "sT", "td", "satu", "dua", "/", "_", "-", " ",
  "zzz", "pengaturanx", "lang", "lgt", "karier", "kr", "pst",
];

for (const t of TEKS_UJI) {
  for (const k of KUERI) {
    adu(`skorBerurutan(${JSON.stringify(t)}, ${JSON.stringify(k)})`,
        acuan.skorBerurutan(t, k), skorBerurutan(t, k));
  }
  for (let i = 0; i < Math.min(t.length, 12); i++) {
    adu(`diBatasKata(${JSON.stringify(t)}, ${i})`,
        acuan.diBatasKata(t, i), diBatasKata(t, i));
  }
}

/* ------------------------------------------------- saringPerintah berurut

   Daftar perintahnya DISUSUN ulang di sini, bukan diiris dari `daftarPerintah`
   di `aplikasi.js`: fungsi itu membaca `ctx.awal`, dan menirukan `ctx` berarti
   membandingkan tiruan dengan tiruan. Yang penting bentuk butirnya -- `label`,
   `ket`, `href`, `tipe` -- dan itu dibangun sama di kedua sisi di bawah. */

const PERINTAH = [
  { label: "Dasbor", ket: "Ringkasan dan langkah berikutnya", href: "#/dasbor" },
  { label: "Ruang Coba", ket: "Jalankan kode apa saja", href: "#/coba" },
  { label: "Catatanku", ket: "Semua catatan pribadimu", href: "#/catatan" },
  { label: "Bookmark", ket: "Halaman yang kamu tandai", href: "#/bookmark" },
  { label: "Statistik", ket: "XP, badge, toolchain", href: "#/statistik" },
  { label: "Pengaturan", ket: "Tema, target harian, data", href: "#/atur" },
  { label: "Pustaka", ket: "Buku, kursus, proyek, dan API gratis", href: "#/pustaka" },
  { label: "Peta Karier", ket: "21 profesi, kesiapan, dan jalur pindah", href: "#/karier" },
  { label: "Langit", ket: "Seluruh kurikulum sebagai peta bintang", href: "#/langit" },
  ...BAHASA.map((b) => ({
    label: b.label,
    ket: `${b.materi} materi · ${b.kuis} kuis · ${b.latihan} latihan`,
    href: "#/bahasa/" + b.key,
    tipe: "bahasa",
  })),
];

/* Riwayat: kosong, satu butir, beberapa butir, dan butir yang TIDAK cocok
   dengan kuerinya -- yang terakhir membuktikan bahwa riwayat menaikkan
   kecocokan yang sudah ada dan tidak pernah menciptakannya. */
const RIWAYAT = [
  [],
  [{ k: "#/statistik", u: 0 }],
  [{ k: "#/bahasa/python", u: 0 }, { k: "#/atur", u: 0 }],
  [{ k: "#/tidak-ada", u: 0 }],
  BAHASA.map((b) => ({ k: "#/bahasa/" + b.key, u: 0 })),
];

for (const k of KUERI) {
  for (const [i, r] of RIWAYAT.entries()) {
    adu(
      `saringPerintah(${JSON.stringify(k)}, riwayat ${i})`,
      acuan.saringPerintah(PERINTAH, k, r).map((d) => d.href),
      saringPerintah(PERINTAH, k, r).map((d) => d.href),
    );
  }
  // Bentuk DUA argumen: harus berarti persis seperti sebelum riwayat ada.
  adu(
    `saringPerintah(${JSON.stringify(k)}, tanpa riwayat)`,
    acuan.saringPerintah(PERINTAH, k).map((d) => d.href),
    saringPerintah(PERINTAH, k).map((d) => d.href),
  );
}

/* --------------------------------------------------------------- riwayat */

const SEKARANG = 1_800_000_000_000;
const HARI = 86400000;
const RIWAYAT_UJI = [
  [],
  [{ k: "#/a", u: SEKARANG }],
  [{ k: "#/a", u: SEKARANG - 13 * HARI }],
  [{ k: "#/a", u: SEKARANG - 14 * HARI }],
  [{ k: "#/a", u: SEKARANG - 14 * HARI + 1 }],
  [{ k: "#/a", u: SEKARANG - 15 * HARI }],
  [{ k: "#/a", u: SEKARANG }, { k: "#/b", u: SEKARANG - 20 * HARI },
   { k: "#/c", u: SEKARANG - 1 }],
  [{ k: "#/a", u: 0 }],
];
for (const [i, r] of RIWAYAT_UJI.entries()) {
  for (const hari of [14, 1, 0, 365]) {
    adu(`riwayatPotong(${i}, ${hari} hari)`,
        acuan.riwayatPotong(r, SEKARANG, hari), riwayatPotong(r, SEKARANG, hari));
  }
  adu(`riwayatPotong(${i}, bawaan)`,
      acuan.riwayatPotong(r, SEKARANG), riwayatPotong(r, SEKARANG));
  for (const k of ["#/a", "#/b", "#/baru"]) {
    adu(`riwayatNaikkan(${i}, ${k})`,
        acuan.riwayatNaikkan(r, k, SEKARANG), riwayatNaikkan(r, k, SEKARANG));
  }
}

/* -------------------------------------------------------- pengelompokan */

const ISI = [
  { label: "C · 15. Pointer Dasar", ket: "cuplikan", tipe: "materi", href: "#/materi/c/14" },
  { label: "Python · Kuis 1", ket: "cuplikan", tipe: "kuis", href: "#/kuis/python/0" },
  { label: "Go · Latihan 2", ket: "cuplikan", tipe: "latihan", href: "#/latihan/go/1" },
  // Tipe yang BELUM ada hari ini: ia wajib masuk ke rombongan "Isi", bukan
  // hilang. Itu seluruh alasan predikat terakhir `() => true`.
  { label: "Sesuatu · baru", ket: "", tipe: "proyek", href: "#/proyek/x/0" },
];
const SET_GABUNG = [
  [],
  PERINTAH,
  ISI,
  [...PERINTAH, ...ISI],
  [...ISI, ...PERINTAH],
  PERINTAH.filter((d) => d.tipe === "bahasa"),
];
for (const [i, set] of SET_GABUNG.entries()) {
  // Sisi JS mengelompokkan di dalam `gambar()`, yang menggambar DOM. Yang
  // diadu di sini partisinya, disusun dari `GRUP_PALET` acuan -- jadi kalau
  // predikat atau urutannya bergeser di `aplikasi.js`, angkanya ikut bergeser.
  const isiGrup = acuan.GRUP_PALET.map(() => []);
  for (const d of set) {
    isiGrup[acuan.GRUP_PALET.findIndex((g) => g.punya(d))].push(d);
  }
  const harap = acuan.GRUP_PALET
    .map((g, j) => ({ label: g.label, isi: isiGrup[j].map((d) => d.href) }))
    .filter((r) => r.isi.length);
  adu(
    `kelompokkan(set ${i})`,
    harap,
    kelompokkan(set).map((r) => ({ label: r.label, isi: r.isi.map((d) => d.href) })),
  );
}

adu("GRUP_PALET label", acuan.GRUP_PALET.map((g) => g.label),
    GRUP_PALET.map((g) => g.label));

console.log(
  `${cacah} perbandingan atas ${TEKS_UJI.length} teks x ${KUERI.length} kueri, ` +
    `${PERINTAH.length} perintah, ${RIWAYAT_UJI.length} riwayat`,
);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: pencocok palet TypeScript identik dengan aplikasi.js.");
