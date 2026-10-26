/* Adu matematika pegas dengan `gerak.js` yang masih melayani antarmuka lama.
 *
 * `gerak.js` berpenjaga DOM (`ADA_DOM`), jadi ia bisa diimpor apa adanya di
 * Node -- tidak perlu shim. Yang diadu bagian MURNI-nya: jepit, antara,
 * petakan, paramPegas, tauSampai, jalurPegas, kurvaPegas, berurut.
 *
 * Kenapa justru bagian ini. Kurva pegas menentukan BENTUK setiap gerakan di
 * aplikasi: satu digit meleset di `tauSampai` atau di solver tertutupnya
 * membuat semua animasi sedikit lebih lamban atau sedikit lebih memantul --
 * perubahan yang tidak melempar apa pun, tidak terlihat di satu animasi, dan
 * baru terasa sebagai "entah kenapa sekarang terasa berat". Rekaman byte
 * easing-nya yang menangkap itu.
 */

import * as ts from "../src/gerak.ts";

const js = await import(
  "../../../webapp/statik/js/gerak.js");

let cacah = 0, beda = 0;
const adu = (nama, a, b) => {
  cacah += 1;
  const ka = JSON.stringify(a), kb = JSON.stringify(b);
  if (ka !== kb) {
    beda += 1;
    if (beda <= 5) {
      console.error(`BEDA ${nama}\n  js: ${ka?.slice(0, 150)}\n  ts: ${kb?.slice(0, 150)}`);
    }
  }
};

/* ------------------------------------------------------------- aritmetika */
const ANGKA = [-3, -1, -0.5, 0, 0.001, 0.5, 1, 1.5, 7, 1e6, NaN];
for (const n of ANGKA) {
  adu(`jepit(${n})`, js.jepit(n), ts.jepit(n));
  adu(`jepit(${n},-2,9)`, js.jepit(n, -2, 9), ts.jepit(n, -2, 9));
}
for (const t of [0, 0.25, 0.5, 1, 2, -1]) {
  adu(`antara(3,11,${t})`, js.antara(3, 11, t), ts.antara(3, 11, t));
}
const PETA = [
  [50, [0, 100], [0, 1]], [150, [0, 100], [0, 1]], [-20, [0, 100], [0, 1]],
  [0, [0, 0], [5, 9]], [30, [0, 400], [1, 0]], [400, [0, 400], [1, 0]],
];
for (const [n, dari, ke] of PETA) {
  adu(`petakan(${n})`, js.petakan(n, dari, ke), ts.petakan(n, dari, ke));
  adu(`petakan(${n}) tanpa jepit`,
      js.petakan(n, dari, ke, { jepitHasil: false }),
      ts.petakan(n, dari, ke, { jepitHasil: false }));
}

/* ------------------------------------------------------------------ pegas */
adu("daftar PEGAS", js.PEGAS, ts.PEGAS);

for (const z of [0.05, 0.2, 0.5, 0.74, 0.94, 0.99, 1]) {
  adu(`tauSampai(${z})`, js.tauSampai(z), ts.tauSampai(z));
  adu(`tauSampai(${z}, .95)`, js.tauSampai(z, 0.95), ts.tauSampai(z, 0.95));
}

const PERIAN = [
  {}, { pantul: 0 }, { pantul: 0.26 }, { pantul: 0.6 },
  { durasiTampak: 0.19, pantul: 0.05 }, { durasiTampak: 0.6, pantul: 0.03 },
  { durasiTampak: 1.2, pantul: 0.4 }, { kekakuan: 170, redaman: 26 },
  { kekakuan: 300 }, { redaman: 12 }, { massa: 2, pantul: 0.1 },
  { durasiTampak: 0.28, pantul: 0, kecepatan: 4 },
  ...Object.values(js.PEGAS),
];
for (const p of PERIAN) {
  const nama = JSON.stringify(p);
  adu(`paramPegas ${nama}`, js.paramPegas(p), ts.paramPegas(p));
  // Kurvanya diadu SELURUH titiknya, bukan cuma durasinya: durasi yang sama
  // dengan bentuk yang berbeda adalah persis kerusakan yang tidak terlihat.
  const kj = js.kurvaPegas(p), kt = ts.kurvaPegas(p);
  adu(`kurvaPegas.durasi ${nama}`, kj.durasi, kt.durasi);
  adu(`kurvaPegas.easing ${nama}`, kj.easing, kt.easing);
  adu(`kurvaPegas.titik ${nama}`, kj.titik, kt.titik);

  const fj = js.jalurPegas(js.paramPegas(p));
  const ft = ts.jalurPegas(ts.paramPegas(p));
  const kiri = [], kanan = [];
  for (let t = 0; t <= 2; t += 0.01) {
    kiri.push(Math.round(fj(t) * 1e9) / 1e9);
    kanan.push(Math.round(ft(t) * 1e9) / 1e9);
  }
  adu(`jalurPegas ${nama}`, kiri, kanan);
}

/* ----------------------------------------------------------------- urutan */
const URUT = [
  [1, {}], [5, {}], [60, {}], [12, { dari: "akhir" }],
  [12, { dari: "tengah" }], [12, { dari: 3 }], [9, { per: 80, maks: 120 }],
  [30, { mulai: 40, per: 20 }], [0, {}],
];
for (const [n, o] of URUT) {
  const dj = js.berurut(n, o), dt = ts.berurut(n, o);
  const kiri = [], kanan = [];
  for (let i = 0; i < Math.max(1, n); i++) { kiri.push(dj(i)); kanan.push(dt(i)); }
  adu(`berurut(${n}, ${JSON.stringify(o)})`, kiri, kanan);
}

/* ------------------------------------------------------------- konstanta */
adu("MULUS", js.MULUS, ts.MULUS);
adu("KELUAR", js.KELUAR, ts.KELUAR);
adu("DETIK", js.DETIK, ts.DETIK);

console.log(`${cacah} perbandingan atas ${PERIAN.length} pemerian pegas`);
if (beda) {
  console.error(`BEDA: ${beda} dari ${cacah}.`);
  process.exit(1);
}
console.log("COCOK: mesin gerak TypeScript identik dengan gerak.js.");
