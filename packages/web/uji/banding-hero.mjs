/* Memeriksa logika isyarat hero gulir-membuka (`komponen/hero-gulir-teks.ts`).
 *
 * Tidak ada JS lama untuk diadu (hero ini baru, bukan port), dan tidak ada sisi
 * Python untuk direkam, jadi yang ditagih adalah SIFAT yang dijanjikan
 * komentar kepala modulnya, atas kisi masukan:
 *
 *   [kontrak]  angka yang dipatok di komentar dan di CSS
 *   [roda]     selama tertutup roda dimakan, dua arah, dan p terjepit 0..1
 *   [buka]     sesudah terbuka roda turun milik halaman; naik menutup hanya
 *              di puncak yang sudah diam
 *   [tombol]   papan ketik punya jalan sendiri; tombol yang ditahan tidak menutup
 *   [ambang]   di mana "terbuka" mulai
 *   [susul]    pelicinan mendekat, tidak melewati, dan berhenti tepat
 *   [pikselRoda] [pemilik]  satuan roda dan elemen yang tombolnya tidak dicuri
 *
 *     node uji/banding-hero.mjs
 */

import {
  AMBANG_TERBUKA, JARAK_RODA, JEDA_TUTUP, LANGKAH_TOMBOL, PEMILIK_TOMBOL,
  arahTombol, pikselRoda, susul, terapkanIsyarat,
} from "../src/komponen/hero-gulir-teks.ts";

let cacah = 0;
let gagal = 0;
function adu(kategori, nama, ok, rinci = "") {
  cacah += 1;
  if (!ok) {
    gagal += 1;
    console.error(`[${kategori}] ${nama}${rinci === "" ? "" : "  " + JSON.stringify(rinci)}`);
  }
}
const dekat = (a, b, t = 1e-9) => Math.abs(a - b) <= t;
const jepit = (x) => Math.min(1, Math.max(0, x));
const roda = (delta) => ({ jenis: "roda", delta });
const tombol = (key, { shift = false, ulang = false } = {}) => ({ jenis: "tombol", key, shift, ulang });
const keadaan = (p, gulirY = 0, sejakGulir = Infinity) => ({ p, gulirY, sejakGulir });

/* ------------------------------------------------------------------ kontrak */
adu("kontrak", "JARAK_RODA = 1100 px untuk membuka seluruhnya", JARAK_RODA === 1100, JARAK_RODA);
adu("kontrak", "LANGKAH_TOMBOL = 0,34 (tiga tekan membuka)", LANGKAH_TOMBOL === 0.34 && 3 * LANGKAH_TOMBOL >= 1, LANGKAH_TOMBOL);
adu("kontrak", "JEDA_TUTUP = 350 ms", JEDA_TUTUP === 350, JEDA_TUTUP);
adu("kontrak", "AMBANG_TERBUKA = 0,999", AMBANG_TERBUKA === 0.999, AMBANG_TERBUKA);

/* -------------------------------------------------------------------- roda */
const GRID_P = [];
for (let i = 0; i <= 19; i++) GRID_P.push(i / 20);
GRID_P.push(0.998);
for (const p of GRID_P) {
  for (const d of [-1500, -300, -50, -1, 1, 50, 300, 1500]) {
    for (const [gulirY, sejak] of [[0, Infinity], [400, 0], [0, 0]]) {
      const h = terapkanIsyarat(roda(d), keadaan(p, gulirY, sejak));
      const harap = jepit(p + d / JARAK_RODA);
      adu("roda", `tertutup p=${p} delta=${d}: p baru terjepit`, dekat(h.p, harap), { p: h.p, harap });
      adu("roda", `tertutup p=${p} delta=${d}: dimakan hero (gulirY=${gulirY}, sejak=${sejak})`, h.cegah === true);
      adu("roda", `tertutup p=${p} delta=${d}: arah mengikuti tanda delta`, d > 0 ? h.p >= p : h.p <= p);
    }
  }
  const nol = terapkanIsyarat(roda(0), keadaan(p));
  adu("roda", `tertutup p=${p} delta 0 tidak dimakan`, nol.cegah === false && nol.p === p);
}

/* -------------------------------------------------------------------- buka */
for (const gulirY of [0, 1, 400]) {
  for (const sejak of [0, 349, 349.9, 350, 5000, Infinity]) {
    const turun = terapkanIsyarat(roda(300), keadaan(1, gulirY, sejak));
    adu("buka", `terbuka: roda turun milik halaman (gulirY=${gulirY}, sejak=${sejak})`, turun.cegah === false && turun.p === 1, turun);
    const naik = terapkanIsyarat(roda(-300), keadaan(1, gulirY, sejak));
    const boleh = gulirY <= 0 && sejak >= 350;
    adu("buka", `terbuka: roda naik menutup hanya di puncak yang diam (gulirY=${gulirY}, sejak=${sejak})`,
      boleh ? naik.cegah === true && dekat(naik.p, 1 - 300 / JARAK_RODA) : naik.cegah === false && naik.p === 1, naik);
  }
}
const mantul = terapkanIsyarat(roda(-300), keadaan(1, -0.5, 1000));
adu("buka", "puncak dengan gulir negatif (pantulan) tetap puncak", mantul.cegah === true, mantul);

/* ------------------------------------------------------------------ tombol */
const ARAH = [
  ["ArrowDown", false, 1], ["ArrowRight", false, 1], ["PageDown", false, 1], [" ", false, 1], ["Spacebar", false, 1],
  ["ArrowUp", false, -1], ["ArrowLeft", false, -1], ["PageUp", false, -1], [" ", true, -1], ["Spacebar", true, -1],
  ["End", false, 2], ["Home", false, -2],
  ["Tab", false, 0], ["Enter", false, 0], ["a", false, 0], ["Escape", false, 0], ["ArrowDown", true, 1], ["F5", false, 0],
];
for (const [key, shift, arah] of ARAH) {
  adu("tombol", `arahTombol(${JSON.stringify(key)}, shift=${shift})`, arahTombol(key, shift) === arah, arahTombol(key, shift));
}
for (const ulang of [false, true]) {
  const maju = terapkanIsyarat(tombol(" ", { ulang }), keadaan(0.5));
  adu("tombol", `tertutup: Spasi menambah satu langkah (ulang=${ulang}: ditahan tetap maju)`, dekat(maju.p, 0.5 + LANGKAH_TOMBOL) && maju.cegah, maju);
  const mundur = terapkanIsyarat(tombol(" ", { shift: true, ulang }), keadaan(0.5));
  adu("tombol", `tertutup: Shift+Spasi mundur satu langkah (ulang=${ulang})`, dekat(mundur.p, 0.5 - LANGKAH_TOMBOL) && mundur.cegah, mundur);
}
adu("tombol", "tertutup: End membuka seluruhnya", terapkanIsyarat(tombol("End"), keadaan(0.2)).p === 1);
adu("tombol", "tertutup: Home menutup seluruhnya", terapkanIsyarat(tombol("Home"), keadaan(0.7)).p === 0);
adu("tombol", "tertutup: PageDown dekat ujung terjepit di 1", terapkanIsyarat(tombol("PageDown"), keadaan(0.9)).p === 1);
adu("tombol", "tertutup: panah atas di 0 terjepit di 0", terapkanIsyarat(tombol("ArrowUp"), keadaan(0)).p === 0);
for (const key of ["Tab", "Enter", "a", "Escape"]) {
  const h = terapkanIsyarat(tombol(key), keadaan(0.5));
  adu("tombol", `tertutup: ${key} bukan milik hero`, h.cegah === false && h.p === 0.5, h);
}
// Terbuka.
for (const key of ["ArrowDown", "PageDown", " ", "End"]) {
  const h = terapkanIsyarat(tombol(key), keadaan(1, 0, Infinity));
  adu("tombol", `terbuka: ${JSON.stringify(key)} milik halaman`, h.cegah === false && h.p === 1, h);
}
for (const key of ["ArrowUp", "PageUp"]) {
  const h = terapkanIsyarat(tombol(key), keadaan(1, 0, Infinity));
  adu("tombol", `terbuka: ${key} sekali tekan di puncak yang diam mundur satu langkah`, dekat(h.p, 1 - LANGKAH_TOMBOL) && h.cegah === true, h);
  const tahan = terapkanIsyarat(tombol(key, { ulang: true }), keadaan(1, 0, Infinity));
  adu("tombol ulang", `terbuka: ${key} yang DITAHAN tidak menutup`, tahan.cegah === false && tahan.p === 1, tahan);
  const gerak = terapkanIsyarat(tombol(key), keadaan(1, 0, 100));
  adu("tombol", `terbuka: ${key} sebelum halaman diam tidak menutup`, gerak.cegah === false && gerak.p === 1, gerak);
  const tengah = terapkanIsyarat(tombol(key), keadaan(1, 300, Infinity));
  adu("tombol", `terbuka: ${key} di tengah halaman menggulir halaman`, tengah.cegah === false && tengah.p === 1, tengah);
}
const rumah = terapkanIsyarat(tombol("Home"), keadaan(1, 0, Infinity));
adu("tombol", "terbuka: Home di puncak yang diam menutup seluruhnya", rumah.p === 0 && rumah.cegah === true, rumah);
adu("tombol", "terbuka: Shift+Spasi di puncak yang diam mundur satu langkah",
  dekat(terapkanIsyarat(tombol(" ", { shift: true }), keadaan(1, 0, Infinity)).p, 1 - LANGKAH_TOMBOL));

/* ------------------------------------------------------------------ ambang */
const tepat = terapkanIsyarat(roda(300), keadaan(AMBANG_TERBUKA));
adu("ambang", "p tepat di ambang sudah terbuka (roda turun milik halaman)", tepat.cegah === false, tepat);
const bawah = terapkanIsyarat(roda(300), keadaan(AMBANG_TERBUKA - 1e-4));
adu("ambang", "sedikit di bawah ambang masih tertutup (roda dimakan)", bawah.cegah === true, bawah);

/* ------------------------------------------------------------------ susul */
for (const [dari, ke] of [[0, 1], [1, 0], [0.2, 0.7], [0.9, 0.1], [0.5, 0.5]]) {
  let p = dari, langkah = 0, naik = true, lewat = false;
  while (p !== ke && langkah < 200) {
    const n = susul(p, ke);
    if (ke > dari ? n < p : n > p) naik = false;
    if (ke > dari ? n > ke : n < ke) lewat = true;
    p = n; langkah += 1;
  }
  adu("susul", `${dari} -> ${ke}: berhenti TEPAT di target dalam < 60 bingkai`, p === ke && langkah < 60, { langkah, p });
  adu("susul", `${dari} -> ${ke}: mendekat terus dan tidak melewati target`, naik && !lewat);
}
adu("susul", "satu langkah menempuh 18 persen jarak", dekat(susul(0, 1), 0.18), susul(0, 1));
adu("susul", "selisih di bawah ambang langsung menempel ke target", susul(0.9995, 1) === 1 && susul(0.0005, 0) === 0);
adu("susul", "selisih di atas ambang belum menempel", susul(0.99, 1) !== 1);

/* ------------------------------------------------------- pikselRoda, pemilik */
adu("pikselRoda", "mode piksel apa adanya", pikselRoda(120, 0, 800) === 120);
adu("pikselRoda", "mode baris: 16 piksel per baris", pikselRoda(3, 1, 800) === 48);
adu("pikselRoda", "mode halaman: satu tinggi jendela per halaman", pikselRoda(2, 2, 800) === 1600);
adu("pikselRoda", "mode tak dikenal diperlakukan sebagai piksel", pikselRoda(7, 9, 800) === 7);
for (const bagian of ["input", "textarea", "select", "button", "a[href]", "summary", '[role="combobox"]', '[role="textbox"]', "#tirai"]) {
  adu("pemilik", `${bagian} tombolnya tidak dicuri hero`, PEMILIK_TOMBOL.split(",").map((s) => s.trim()).includes(bagian), bagian);
}

console.log(`${cacah} perbandingan atas isyarat hero gulir`);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: logika hero gulir memenuhi semua sifat yang dijanjikan.");
