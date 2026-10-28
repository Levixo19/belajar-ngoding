/* Memeriksa logika cakrawala bara (`komponen/skyline-teks.ts`).
 *
 * Tidak ada JS lama untuk diadu (komponennya baru) dan tidak ada sisi Python
 * untuk direkam, jadi yang ditagih adalah SIFAT yang dijanjikan komentar kepala
 * modulnya. Tiap sifat dibandingkan dengan oracle yang ditulis sendiri di sini
 * (hitungan lurus, bukan salinan rumusnya), atas kasus tangan ditambah ribuan
 * kasus acak berbenih tetap:
 *
 *   [kontrak]  angka yang menjamin urutan gambar dan bentuk gambar
 *   [kolom]    hari ke-i jatuh di kolom dan baris yang benar
 *   [puncak]   pembagi tinggi: target atau hari terbaik, mana yang lebih besar
 *   [tinggi]   linear, berlantai untuk hari ber-XP, berpuncak, nol untuk nol
 *   [titik]    proyeksi afin, tinggi mengangkat ke atas layar
 *   [urutan]   urutan batang = urutan gambar: tidak ada yang digambar sebelum yang lebih belakang
 *   [bangun]   geometri: ukuran, batas, tiga permukaan, garis luar, label
 *   [bulan]    label bulan: tiap tanggal 1, tanpa yang berdesakan
 *   [langkah]  navigasi papan ketik: dijepit, tidak menyeberang minggu
 *   [ringkas]  total, hari ber-XP, tersibuk, rentetan, lawan hitungan lurus
 *   [teks]     kalimat yang dibaca pembaca layar
 *
 *     node uji/banding-skyline.mjs
 */

import {
  BARIS_LABEL, HARI, HARI_PER_MINGGU, INSET, JARAK_BULAN, MINGGU, NAMA_BULAN, NAMA_HARI, PAD,
  RUANG_LABEL, SKALA, TINGGI_MAKS, TINGGI_MIN,
  bangunSkyline, kolomBaris, labelBulan, labelGrup, langkahSel, puncakXp, ringkasSkyline,
  teksHari, teksRentetan, teksTersibuk, tinggiBatang, titik,
} from "../src/komponen/skyline-teks.ts";

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

/* Pembangkit acak berbenih (mulberry32): kasus yang sama di setiap mesin. */
function acak(benih) {
  let a = benih >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const R = acak(20261028);
const bulat = (n) => Math.floor(R() * n);

const iso = (t) =>
  `${t.getFullYear()}-${String(t.getMonth() + 1).padStart(2, "0")}-${String(t.getDate()).padStart(2, "0")}`;

/** Daftar hari berurutan dari `mulai` (Date lokal tengah malam), xp dari `xpDari(i)`. */
function deret(mulai, n, xpDari, target = 60) {
  const hari = [];
  for (let i = 0; i < n; i++) {
    const t = new Date(mulai.getFullYear(), mulai.getMonth(), mulai.getDate() + i);
    const xp = xpDari(i);
    hari.push({
      tanggal: iso(t),
      xp,
      tingkat: xp <= 0 ? 0 : xp < target * 0.5 ? 1 : xp < target ? 2 : 3,
      kini: i === n - 1,
      judul: `${iso(t)}: ${xp} XP`,
    });
  }
  return { hari, kosong: (mulai.getDay() + 6) % 7 };
}

/* ------------------------------------------------------------------ kontrak */
adu("kontrak", "satu minggu tujuh hari", HARI_PER_MINGGU === 7, HARI_PER_MINGGU);
adu("kontrak", "kedua langkah layar turun (koefisien y positif): syarat urutan gambar",
  MINGGU.y > 0 && HARI.y > 0, { MINGGU, HARI });
adu("kontrak", "minggu ke kanan, hari ke kiri bawah", MINGGU.x > 0 && HARI.x < 0, { MINGGU, HARI });
adu("kontrak", "jarak batang ke tepi petak di dalam (0, 0,5)", INSET > 0 && INSET < 0.5, INSET);
adu("kontrak", "lantai tinggi di bawah puncak tinggi", TINGGI_MIN > 0 && TINGGI_MIN < TINGGI_MAKS, { TINGGI_MIN, TINGGI_MAKS });
// Batang setinggi lebih dari tiga satuan menutupi lebih dari lima baris di belakangnya.
adu("kontrak", "tinggi puncak antara satu dan tiga satuan", TINGGI_MAKS >= 1 && TINGGI_MAKS <= 3, TINGGI_MAKS);
adu("kontrak", "label bulan digantung di bawah baris Minggu dan punya ruang tulis",
  BARIS_LABEL > 7 && BARIS_LABEL < 8 && RUANG_LABEL >= 0.5, { BARIS_LABEL, RUANG_LABEL });
adu("kontrak", "jarak label bulan tiga kolom", JARAK_BULAN === 3, JARAK_BULAN);
adu("kontrak", "nama bulan dan hari lengkap", NAMA_BULAN.length === 12 && NAMA_HARI.length === 7);
adu("kontrak", "skala dan ruang tepi positif", SKALA > 0 && PAD > 0, { SKALA, PAD });

/* -------------------------------------------------------------------- kolom */
for (let kosong = 0; kosong < 7; kosong++) {
  for (let i = 0; i < 200; i++) {
    const { kolom, baris } = kolomBaris(i, kosong);
    adu("kolom", `kolom*7+baris = kosong+i (${i}, ${kosong})`, kolom * 7 + baris === kosong + i, { kolom, baris });
    adu("kolom", `baris 0..6 (${i}, ${kosong})`, baris >= 0 && baris <= 6 && Number.isInteger(kolom), { kolom, baris });
  }
  adu("kolom", `hari pertama jatuh di baris = kosong (${kosong})`, kolomBaris(0, kosong).baris === kosong && kolomBaris(0, kosong).kolom === 0);
}
adu("kolom", "minggu berikutnya satu kolom ke kanan, baris sama",
  kolomBaris(10, 3).kolom + 1 === kolomBaris(17, 3).kolom && kolomBaris(10, 3).baris === kolomBaris(17, 3).baris);

/* ------------------------------------------------------------------- puncak */
adu("puncak", "tanpa hari: target", puncakXp([], 60) === 60);
adu("puncak", "target nol: dasar 1", puncakXp([], 0) === 1 && puncakXp([{ xp: 0 }], -5) === 1);
adu("puncak", "hari terbaik di atas target menang", puncakXp([{ xp: 10 }, { xp: 200 }], 60) === 200);
adu("puncak", "target di atas hari terbaik menang", puncakXp([{ xp: 10 }, { xp: 20 }], 60) === 60);
for (let k = 0; k < 300; k++) {
  const xs = Array.from({ length: bulat(40) }, () => bulat(400));
  const target = bulat(150);
  const p = puncakXp(xs.map((xp) => ({ xp })), target);
  const harap = Math.max(target > 0 ? target : 1, ...xs);
  adu("puncak", "sama dengan maksimum lurus", p === harap, { p, harap });
}

/* ------------------------------------------------------------------- tinggi */
adu("tinggi", "nol XP: nol", tinggiBatang(0, 60) === 0);
adu("tinggi", "XP negatif atau bukan angka: nol", tinggiBatang(-4, 60) === 0 && tinggiBatang(NaN, 60) === 0);
adu("tinggi", "puncak tidak sah: nol", tinggiBatang(10, 0) === 0 && tinggiBatang(10, -1) === 0);
adu("tinggi", "satu XP di puncak besar: lantai", tinggiBatang(1, 100000) === TINGGI_MIN, tinggiBatang(1, 100000));
adu("tinggi", "XP di puncak: tinggi puncak", tinggiBatang(60, 60) === TINGGI_MAKS);
adu("tinggi", "XP di atas puncak dijepit", tinggiBatang(600, 60) === TINGGI_MAKS);
{
  let sebelum = -1;
  let naik = true;
  for (let xp = 0; xp <= 200; xp++) {
    const t = tinggiBatang(xp, 120);
    if (t < sebelum) naik = false;
    sebelum = t;
    if (xp > 0 && t < TINGGI_MIN) adu("tinggi", `hari ber-XP tak pernah di bawah lantai (${xp})`, false, t);
    if (t > TINGGI_MAKS) adu("tinggi", `tak pernah di atas puncak (${xp})`, false, t);
  }
  adu("tinggi", "tidak pernah turun saat XP naik", naik);
}
for (let k = 0; k < 200; k++) {
  const puncak = 50 + bulat(500);
  const xp = 1 + bulat(Math.floor(puncak / 2));
  const t1 = tinggiBatang(xp, puncak);
  const t2 = tinggiBatang(2 * xp, puncak);
  if (t1 > TINGGI_MIN && t2 < TINGGI_MAKS) {
    adu("tinggi", "linear: dua kali XP dua kali tinggi", dekat(t2, 2 * t1, 1e-9), { xp, puncak, t1, t2 });
  }
}

/* -------------------------------------------------------------------- titik */
for (let k = 0; k < 200; k++) {
  const c = R() * 30;
  const r = R() * 8;
  const naik = R() * 3;
  const [x, y] = titik(c, r, naik);
  adu("titik", "kombinasi linear dua langkah dikurangi tinggi",
    dekat(x, c * MINGGU.x + r * HARI.x) && dekat(y, c * MINGGU.y + r * HARI.y - naik), { c, r, naik, x, y });
}
adu("titik", "tinggi mengangkat ke atas layar (y mengecil)", titik(3, 3, 1)[1] < titik(3, 3, 0)[1]);
adu("titik", "tanpa tinggi: tinggi 0", titik(2, 2)[1] === titik(2, 2, 0)[1]);

/* ------------------------------------------------------------------- urutan */
// Urutan `batang` ADALAH urutan gambar (algoritma pelukis): tidak ada batang yang digambar sebelum
// batang yang lebih belakang darinya, dan urutannya sama dengan urutan hari.
for (const [n, kosong] of [[1, 0], [7, 0], [8, 6], [50, 3], [182, 0], [182, 2], [183, 4], [190, 6]]) {
  const { hari } = deret(new Date(2026, 0, 1), n, () => 5);
  const t = bangunSkyline(hari, kosong, 60);
  const pos = t.batang.map((bt) => kolomBaris(bt.i, kosong));
  let salah = "";
  if (t.batang.some((bt, i) => bt.i !== i)) salah = "batang tidak berurutan seperti harinya";
  for (let i = 0; i < n && !salah; i++) {
    for (let j = i + 1; j < n; j++) {
      // i digambar lebih dulu dari j: j tidak boleh lebih belakang dari i pada kedua sumbu.
      if (pos[j].kolom <= pos[i].kolom && pos[j].baris <= pos[i].baris) {
        salah = `(${pos[j].kolom},${pos[j].baris}) digambar sesudah (${pos[i].kolom},${pos[i].baris}) padahal tidak lebih depan`;
        break;
      }
    }
  }
  adu("urutan", `n=${n} kosong=${kosong}: tidak ada batang digambar sebelum yang lebih belakang`, salah === "", salah);
}

/* ------------------------------------------------------------------- bangun */
const titikDari = (s) => (s === "" ? [] : s.split(" ").map((p) => p.split(",").map(Number)));
const titikPath = (s) => s.slice(1, -1).split("L").map((p) => p.split(",").map(Number));
{
  const e = bangunSkyline([], 0, 60);
  adu("bangun", "tanpa hari: ukuran terhingga dan tanpa batang",
    Number.isFinite(e.lebar) && Number.isFinite(e.tinggi) && e.batang.length === 0 && e.bulan.length === 0, e);
}
for (let k = 0; k < 40; k++) {
  const n = 1 + bulat(190);
  const mulai = new Date(2026, bulat(12), 1 + bulat(28));
  const { hari, kosong } = deret(mulai, n, () => (bulat(4) === 0 ? 0 : 1 + bulat(300)));
  const t = bangunSkyline(hari, kosong, 60);
  const nama = `n=${n} kosong=${kosong}`;
  adu("bangun", `${nama}: satu batang per hari, penanda i = posisinya`,
    t.batang.length === n && t.batang.every((bt, i) => bt.i === i));
  adu("bangun", `${nama}: deterministik`, JSON.stringify(t) === JSON.stringify(bangunSkyline(hari, kosong, 60)));

  let minX = Infinity;
  let minY = Infinity;
  let maxX = -Infinity;
  let maxY = -Infinity;
  let rusak = "";
  t.batang.forEach((b, i) => {
    const h = hari[i];
    const atas = titikDari(b.atas);
    const muka = titikDari(b.muka);
    const sisi = titikDari(b.sisi);
    const garis = titikPath(b.siluet);
    if (atas.length !== 4) rusak = `atas ${i}`;
    if (garis.length !== 6) rusak = `siluet ${i}`;
    if (h.xp > 0 && (muka.length !== 4 || sisi.length !== 4)) rusak = `permukaan samping ${i}`;
    if (h.xp <= 0 && (b.muka !== "" || b.sisi !== "" || b.tinggi !== 0)) rusak = `hari kosong ${i} berdinding`;
    if (b.i !== i || b.tingkat !== h.tingkat || b.kini !== h.kini) rusak = `penanda ${i}`;
    // Tinggi di layar: puncak sisi depan terhadap alasnya = tinggi * SKALA.
    // Oracle-nya `tinggiBatang` yang belum dibulatkan: `b.tinggi` dibulatkan
    // ke 0,01 satuan (0,34 piksel), terlalu kasar untuk toleransi koordinat.
    if (h.xp > 0) {
      const naikLayar = muka[3][1] - muka[0][1];
      const harap = tinggiBatang(h.xp, t.puncak) * SKALA;
      if (!dekat(naikLayar, harap, 0.03)) rusak = `tinggi layar ${i}: ${naikLayar} vs ${harap}`;
      if (!dekat(b.tinggi, tinggiBatang(h.xp, t.puncak), 0.0051)) rusak = `tinggi tercatat ${i}: ${b.tinggi}`;
    }
    // Bentuk: tiga permukaan saling menempel di tepi yang sama. Urutan titik:
    // atas = [A, B, C, D] puncak; muka = [D, C, alas C, alas D];
    // sisi = [B, C, alas C, alas B]; siluet = [A, B, alas B, alas C, alas D, D].
    const sama = (p, q) => dekat(p[0], q[0], 0.02) && dekat(p[1], q[1], 0.02);
    if (!sama(garis[0], atas[0]) || !sama(garis[1], atas[1]) || !sama(garis[5], atas[3])) rusak = `siluet tak mengikuti puncak ${i}`;
    if (h.xp > 0) {
      if (!sama(muka[0], atas[3]) || !sama(muka[1], atas[2])) rusak = `muka tak menempel di puncak ${i}`;
      if (!sama(sisi[0], atas[1]) || !sama(sisi[1], atas[2])) rusak = `sisi tak menempel di puncak ${i}`;
      if (!dekat(muka[2][0], muka[1][0], 0.02) || !dekat(muka[3][0], muka[0][0], 0.02)) rusak = `muka tidak tegak ${i}`;
      if (!dekat(sisi[2][0], sisi[1][0], 0.02) || !dekat(sisi[3][0], sisi[0][0], 0.02)) rusak = `sisi tidak tegak ${i}`;
      if (!sama(sisi[2], muka[2])) rusak = `muka dan sisi tak berbagi alas depan ${i}`;
      if (!sama(garis[2], sisi[3]) || !sama(garis[3], muka[2]) || !sama(garis[4], muka[3])) rusak = `siluet tak mengikuti alas ${i}`;
    }
    for (const [x, y] of [...atas, ...muka, ...sisi, ...garis]) {
      if (x < minX) minX = x;
      if (x > maxX) maxX = x;
      if (y < minY) minY = y;
      if (y > maxY) maxY = y;
    }
  });
  adu("bangun", `${nama}: bentuk tiap batang`, rusak === "", rusak);
  adu("bangun", `${nama}: tepi kiri dan atas tepat satu ruang tepi`,
    dekat(minX, PAD * SKALA, 0.02) && minY >= PAD * SKALA - 0.02 && dekat(minY, PAD * SKALA, 0.02), { minX, minY });
  adu("bangun", `${nama}: batang tidak keluar gambar`, maxX <= t.lebar + 0.02 && maxY <= t.tinggi + 0.02, { maxX, maxY, lebar: t.lebar, tinggi: t.tinggi });
  adu("bangun", `${nama}: ada ruang tepi di kanan`, t.lebar - maxX >= PAD * SKALA - 0.05, { maxX, lebar: t.lebar });
  for (const b of t.bulan) {
    adu("bangun", `${nama}: label ${b.teks} di dalam gambar dengan ruang tulis`,
      b.x >= 0 && b.x <= 1 && b.y >= 0 && b.y <= 1 && b.y * t.tinggi + 0.5 * SKALA <= t.tinggi + 0.05, b);
    // Ruang di bawah jangkar: ruang tulis ditambah ruang tepi. Teks label
    // mengikuti rem, jadi setelan "Ukuran huruf" yang besar butuh lebih dari
    // ruang tepi saja.
    adu("bangun", `${nama}: label ${b.teks} punya ruang tulis di bawah jangkarnya`,
      (1 - b.y) * t.tinggi >= (PAD + RUANG_LABEL) * SKALA - 0.05, { sisa: (1 - b.y) * t.tinggi, butuh: (PAD + RUANG_LABEL) * SKALA });
    // Jangkar di bawah alas terdepan batang sekolomnya: label tidak menimpa batang.
    let alasTerdepan = -Infinity;
    t.batang.forEach((bt) => {
      if (bt.kolom !== b.kolom) return;
      for (const p of [...titikDari(bt.atas), ...titikDari(bt.muka), ...titikDari(bt.sisi)]) alasTerdepan = Math.max(alasTerdepan, p[1]);
    });
    adu("bangun", `${nama}: label ${b.teks} di bawah batang sekolomnya`, b.y * t.tinggi >= alasTerdepan + 4, { jangkar: b.y * t.tinggi, alasTerdepan });
  }
  adu("bangun", `${nama}: puncak tinggi sama dengan pembagi`, t.puncak === puncakXp(hari, 60));
}

/* -------------------------------------------------------------------- bulan */
{
  /** Oracle: cacah kolom tiap tanggal 1, ditambah hari pertama, tanpa penyaringan. */
  const lurus = (hari, kosong) => {
    const hasil = [];
    hari.forEach((h, i) => {
      const t = new Date(Number(h.tanggal.slice(0, 4)), Number(h.tanggal.slice(5, 7)) - 1, Number(h.tanggal.slice(8, 10)));
      if (i === 0 || t.getDate() === 1) {
        hasil.push({ kolom: Math.floor((kosong + i) / 7), bulan: t.getMonth() });
      }
    });
    return hasil;
  };
  for (let k = 0; k < 120; k++) {
    const mulai = new Date(2026, bulat(12), 1 + bulat(28));
    const n = 7 + bulat(190);
    const { hari, kosong } = deret(mulai, n, () => 5);
    const got = labelBulan(hari, kosong);
    const calon = lurus(hari, kosong);
    if (calon.length >= 2 && calon[1].kolom - calon[0].kolom < JARAK_BULAN) calon.shift();
    const harap = [];
    for (const c of calon) {
      const t = harap[harap.length - 1];
      if (!t || c.kolom - t.kolom >= JARAK_BULAN) harap.push(c);
    }
    adu("bulan", `mulai ${iso(mulai)} n=${n}: sama dengan hitungan lurus`,
      JSON.stringify(got.map((g) => [g.kolom, g.teks])) === JSON.stringify(harap.map((c) => [c.kolom, NAMA_BULAN[c.bulan]])), { got, harap });
    let rapat = true;
    for (let j = 1; j < got.length; j++) if (got[j].kolom - got[j - 1].kolom < JARAK_BULAN) rapat = false;
    adu("bulan", `mulai ${iso(mulai)} n=${n}: tak ada yang berdesakan, kolom menaik`, rapat);
  }
  // Tepat tiga kolom masih cukup: bulan pembuka dan bulan berikutnya sama-sama diberi label.
  {
    const { hari, kosong } = deret(new Date(2026, 3, 8), 60, () => 5);
    const got = labelBulan(hari, kosong);
    adu("bulan", "jarak tepat tiga kolom: dua label",
      got.length >= 2 && got[0].teks === "Apr" && got[1].teks === "Mei" && got[1].kolom - got[0].kolom === 3, got);
  }
  // Bulan pembuka yang tinggal dua hari tidak memakan label bulan berikutnya.
  {
    const { hari, kosong } = deret(new Date(2026, 3, 29), 60, () => 5);
    const got = labelBulan(hari, kosong);
    adu("bulan", "bulan pembuka yang tinggal sebentar dibuang", got[0].teks === "Mei" && got[0].kolom === 0, got);
  }
  adu("bulan", "tanggal tak terbaca dilewati, bukan melempar", labelBulan([{ tanggal: "bukan-tanggal" }], 0).length === 0);
}

/* ------------------------------------------------------------------- langkah */
{
  adu("langkah", "tanpa hari: bukan milik hamparan", langkahSel(0, "ArrowRight", 0, 0) === null);
  adu("langkah", "tombol lain: null", langkahSel(5, "a", 0, 100) === null && langkahSel(5, "Tab", 0, 100) === null && langkahSel(5, "Enter", 0, 100) === null);
  adu("langkah", "kanan satu minggu", langkahSel(10, "ArrowRight", 0, 182) === 17);
  adu("langkah", "kiri satu minggu", langkahSel(10, "ArrowLeft", 0, 182) === 3);
  adu("langkah", "kanan di minggu terakhir: hari ini", langkahSel(178, "ArrowRight", 0, 182) === 181);
  adu("langkah", "kiri di minggu pertama: hari pertama", langkahSel(3, "ArrowLeft", 0, 182) === 0);
  adu("langkah", "bawah satu hari", langkahSel(10, "ArrowDown", 0, 182) === 11);
  adu("langkah", "atas satu hari", langkahSel(10, "ArrowUp", 0, 182) === 9);
  adu("langkah", "bawah dari Minggu tetap", langkahSel(6, "ArrowDown", 0, 182) === 6 && langkahSel(13, "ArrowDown", 0, 182) === 13);
  adu("langkah", "atas dari Senin tetap", langkahSel(7, "ArrowUp", 0, 182) === 7 && langkahSel(0, "ArrowUp", 0, 182) === 0);
  // Dengan 4 sel kosong pembuka: i=0 Jumat, i=2 Minggu, i=3 Senin minggu berikutnya.
  adu("langkah", "kosong pembuka menggeser barisnya: Minggu dan Senin jatuh di i=2 dan i=3",
    langkahSel(2, "ArrowDown", 4, 182) === 2 && langkahSel(3, "ArrowUp", 4, 182) === 3 &&
      langkahSel(3, "ArrowDown", 4, 182) === 4 && langkahSel(4, "ArrowUp", 4, 182) === 3);
  adu("langkah", "hari ini tak melampaui akhir ke bawah", langkahSel(181, "ArrowDown", 0, 182) === 181);
  adu("langkah", "Home dan End", langkahSel(50, "Home", 0, 182) === 0 && langkahSel(50, "End", 0, 182) === 181);
  adu("langkah", "PageDown empat minggu, dijepit", langkahSel(10, "PageDown", 0, 182) === 38 && langkahSel(170, "PageDown", 0, 182) === 181);
  adu("langkah", "PageUp empat minggu, dijepit", langkahSel(40, "PageUp", 0, 182) === 12 && langkahSel(5, "PageUp", 0, 182) === 0);
  for (let k = 0; k < 400; k++) {
    const jumlah = 1 + bulat(190);
    const kosong = bulat(7);
    const i = bulat(jumlah);
    for (const tombol of ["ArrowRight", "ArrowLeft", "ArrowDown", "ArrowUp", "PageDown", "PageUp", "Home", "End"]) {
      const ke = langkahSel(i, tombol, kosong, jumlah);
      adu("langkah", `${tombol} (${i}/${jumlah}) tetap di dalam hamparan`, Number.isInteger(ke) && ke >= 0 && ke < jumlah, ke);
      if (tombol === "ArrowDown" || tombol === "ArrowUp") {
        adu("langkah", `${tombol} tidak menyeberang minggu`, kolomBaris(ke, kosong).kolom === kolomBaris(i, kosong).kolom, { i, ke, kosong });
      }
      if (tombol === "ArrowRight" && i + 7 < jumlah) adu("langkah", "kanan: baris sama", kolomBaris(ke, kosong).baris === kolomBaris(i, kosong).baris);
    }
  }
}

/* ------------------------------------------------------------------ ringkas */
{
  const lurus = (hari) => {
    let total = 0;
    let aktif = 0;
    let tersibuk = null;
    let panjang = 0;
    let akhir = "";
    for (let a = 0; a < hari.length; a++) {
      if (hari[a].xp > 0) {
        total += hari[a].xp;
        aktif += 1;
        if (tersibuk === null || hari[a].xp >= hari[tersibuk].xp) tersibuk = a;
        let b = a;
        while (b + 1 < hari.length && hari[b + 1].xp > 0) b++;
        const p = b - a + 1;
        if (a === 0 || hari[a - 1].xp <= 0) {
          if (p >= panjang) {
            panjang = p;
            akhir = hari[b].tanggal;
          }
        }
      }
    }
    return { total, aktif, tersibuk: tersibuk === null ? null : hari[tersibuk].tanggal, rentetan: panjang > 0 ? { panjang, akhir } : null };
  };
  for (let k = 0; k < 400; k++) {
    const n = bulat(60);
    const rapat = bulat(3);
    const { hari } = deret(new Date(2026, 5, 1), n, () => (bulat(3) < rapat ? 0 : 1 + bulat(4) * 10));
    const r = ringkasSkyline(hari);
    const h = lurus(hari);
    adu("ringkas", `n=${n}: total, aktif, tersibuk, rentetan sama dengan hitungan lurus`,
      r.total === h.total && r.aktif === h.aktif && (r.tersibuk ? r.tersibuk.tanggal : null) === h.tersibuk &&
        JSON.stringify(r.rentetan) === JSON.stringify(h.rentetan), { r, h });
  }
  const hz = deret(new Date(2026, 5, 1), 5, () => 0).hari;
  const kosongR = ringkasSkyline(hz);
  adu("ringkas", "tanpa XP: nol dan tanpa tersibuk atau rentetan", kosongR.total === 0 && kosongR.aktif === 0 && kosongR.tersibuk === null && kosongR.rentetan === null);
  adu("ringkas", "tanpa hari", ringkasSkyline([]).aktif === 0);
  const seri = deret(new Date(2026, 5, 1), 6, (i) => [50, 0, 50, 0, 50, 0][i]).hari;
  adu("ringkas", "tersibuk seri: yang terbaru", ringkasSkyline(seri).tersibuk.tanggal === seri[4].tanggal);
  const dua = deret(new Date(2026, 5, 1), 7, (i) => [5, 5, 0, 5, 5, 0, 0][i]).hari;
  adu("ringkas", "rentetan seri: yang terbaru", ringkasSkyline(dua).rentetan.akhir === dua[4].tanggal && ringkasSkyline(dua).rentetan.panjang === 2);
  const putus = deret(new Date(2026, 5, 1), 7, (i) => [5, 5, 5, 0, 5, 5, 0][i]).hari;
  adu("ringkas", "rentetan putus oleh hari kosong", ringkasSkyline(putus).rentetan.panjang === 3 && ringkasSkyline(putus).aktif === 5);
  const ber = deret(new Date(2026, 5, 1), 4, (i) => [1, 2, 3, 4][i]).hari;
  adu("ringkas", "rentetan penuh", ringkasSkyline(ber).rentetan.panjang === 4 && ringkasSkyline(ber).rentetan.akhir === ber[3].tanggal);
}

/* --------------------------------------------------------------------- teks */
{
  const hari = deret(new Date(2026, 9, 26), 3, (i) => [0, 40, 0][i]).hari;
  for (let b = 0; b < 7; b++) {
    adu("teks", `nama hari baris ${b}`, teksHari(hari[0], b).startsWith(NAMA_HARI[b] + ", "), teksHari(hari[0], b));
  }
  adu("teks", "hari ini diberi penanda, yang lain tidak",
    teksHari(hari[2], 2).endsWith(", hari ini") && !teksHari(hari[1], 1).includes("hari ini"));
  adu("teks", "memuat judul hamparan datar (isi sama di dua tampilan)", teksHari(hari[1], 1).includes(hari[1].judul));
  const r = ringkasSkyline(hari);
  adu("teks", "label grup menyebut hari ber-XP, total, dan cara menjelajah",
    labelGrup(r).includes("1 hari ber-XP, total 40 XP") && labelGrup(r).includes("Panah") && labelGrup(r).includes("Home dan End"), labelGrup(r));
  adu("teks", "label grup tanpa XP", labelGrup(ringkasSkyline([])).includes("belum ada hari ber-XP"));
  adu("teks", "hari tersibuk memuat XP-nya", teksTersibuk(r).includes("40 XP"), teksTersibuk(r));
  adu("teks", "tanpa XP: belum ada", teksTersibuk(ringkasSkyline([])) === "belum ada" && teksRentetan(ringkasSkyline([])) === "belum ada");
  adu("teks", "rentetan menyebut hari", teksRentetan(r) === "1 hari", teksRentetan(r));
  for (const s of [labelGrup(r), teksHari(hari[2], 2), teksTersibuk(r), teksRentetan(r)]) {
    // Escape Unicode, bukan karakternya: berkas ini sendiri diperiksa tes "tanpa dash".
    adu("teks", "tanpa dash", !s.includes("\u2014") && !s.includes("\u2013"), s);
  }
}

console.log(gagal ? `GAGAL: ${gagal} dari ${cacah} perbandingan` : `COCOK: ${cacah} perbandingan, cakrawala sesuai janji kepala modulnya`);
process.exit(gagal ? 1 : 0);
