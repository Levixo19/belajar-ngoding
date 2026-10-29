/* Memeriksa logika orbit bekal (`komponen/orbit-teks.ts`).
 *
 * Tidak ada JS lama untuk diadu (komponennya baru) dan tidak ada sisi Python
 * untuk direkam, jadi yang ditagih adalah SIFAT yang dijanjikan komentar kepala
 * modulnya, atas kasus tangan ditambah ribuan kasus acak berbenih tetap:
 *
 *   [kontrak]  angka yang juga dipakai CSS dan skrip peramban
 *   [status]   batas selesai, sedang, belum; persen dijepit 0..100
 *   [sudut]    sudut dasar dibagi rata; cincin luar bergeser setengah langkah
 *   [bangun]   simpul untuk tiap alternatif bekal dan pelengkap, tanpa kembar
 *   [wakil]    tepat satu wakil per kelompok, dan itu yang ditunjuk server
 *   [setara]   alternatif saling setara, tidak pernah dengan dirinya sendiri
 *   [putar]    kemajuan sudut: lurus, melingkar 0..360, dan dijepit per bingkai
 *   [fokus]    navigasi panah berputar di ujung daftar
 *   [label] [ringkas]  teks yang dibaca pembaca layar
 *
 *     node uji/banding-orbit.mjs
 */

import {
  DT_MAKS, JARI, KECEPATAN, LAJU, STATUS_TEKS,
  bangunNode, labelNode, langkahFokus, ringkasOrbit, statusDari, sudutBerikut, sudutDasar,
} from "../src/komponen/orbit-teks.ts";

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

/* ------------------------------------------------------------------ kontrak */
adu("kontrak", "jari cincin dalam 30 dan luar 44 cqw", JARI.dalam === 30 && JARI.luar === 44, JARI);
adu("kontrak", "cincin dalam berputar lebih cepat (1) daripada luar (0,6)", KECEPATAN.dalam === 1 && KECEPATAN.luar === 0.6, KECEPATAN);
adu("kontrak", "laju dasar 6 derajat per detik dan jepitan bingkai 100 ms", LAJU === 6 && DT_MAKS === 100, { LAJU, DT_MAKS });
adu("kontrak", "teks status", STATUS_TEKS.selesai === "selesai" && STATUS_TEKS.jalan === "sedang dikerjakan" && STATUS_TEKS.belum === "belum dimulai", STATUS_TEKS);

/* ------------------------------------------------------------------- status */
for (const [p, harap] of [[0, "belum"], [0.01, "jalan"], [1, "jalan"], [50, "jalan"], [99.9, "jalan"], [100, "selesai"], [150, "selesai"], [-5, "belum"], [NaN, "belum"]]) {
  adu("status", `statusDari(${p}) = ${harap}`, statusDari(p) === harap, statusDari(p));
}

/* -------------------------------------------------------------------- sudut */
for (let n = 1; n <= 12; n++) {
  for (let i = 0; i < n; i++) {
    adu("sudut", `sudutDasar(${i}, ${n}) membagi lingkaran rata dari puncak`, dekat(sudutDasar(i, n), -90 + (360 * i) / n));
    adu("sudut", `sudutDasar(${i}, ${n}, 0,5) bergeser setengah langkah`, dekat(sudutDasar(i, n, 0.5), -90 + (360 * (i + 0.5)) / n));
  }
}
adu("sudut", "tanpa simpul: sudut di puncak", sudutDasar(0, 0) === -90);

/* ------------------------------------------------------------------- bangun */
const KUR = {
  html: { label: "HTML", persen: 100 }, css: { label: "CSS", persen: 62 }, python: { label: "Python", persen: 40 },
  javascript: { label: "JavaScript", persen: 80 }, go: { label: "Go", persen: 0 }, git: { label: "Git", persen: 100 },
};
const k1 = bangunNode([{ pilihan: ["html"], wakil: "html", persen: 100 }, { pilihan: ["python", "javascript"], wakil: "javascript", persen: 80 }], ["css", "git"], KUR);
adu("bangun", "tiap alternatif jadi simpul, bekal lebih dulu", k1.map((n) => n.id).join() === "dalam:html,dalam:python,dalam:javascript,luar:css,luar:git", k1.map((n) => n.id));
adu("bangun", "persen dan label dari kurikulum", k1[0].label === "HTML" && k1[0].persen === 100 && k1[1].persen === 40 && k1[3].persen === 62, k1.map((n) => [n.label, n.persen]));
adu("bangun", "status mengikuti persen", k1.map((n) => n.status).join() === "selesai,jalan,jalan,jalan,selesai", k1.map((n) => n.status));
adu("bangun", "cincin dalam untuk bekal, luar untuk pelengkap", k1.map((n) => n.lingkar).join() === "dalam,dalam,dalam,luar,luar");
adu("bangun", "indeks kelompok: bekal 0..n, pelengkap null", k1.map((n) => n.kelompok).join() === "0,1,1,,", k1.map((n) => n.kelompok));
adu("bangun", "cincin dalam dibagi rata dari puncak", dekat(k1[0].sudut, -90) && dekat(k1[1].sudut, 30) && dekat(k1[2].sudut, 150), k1.map((n) => n.sudut));
adu("bangun", "cincin luar bergeser setengah langkah (tidak berbaris dengan simpul dalam)", dekat(k1[3].sudut, -90 + 90) && dekat(k1[4].sudut, -90 + 270), k1.map((n) => n.sudut));
adu("wakil", "satu wakil per kelompok, yang ditunjuk", k1[0].wakil && !k1[1].wakil && k1[2].wakil && !k1[3].wakil && !k1[4].wakil, k1.map((n) => n.wakil));
adu("setara", "alternatif saling setara; yang sendirian tidak punya setara",
  k1[0].setara.length === 0 && k1[1].setara.join() === "dalam:javascript" && k1[2].setara.join() === "dalam:python" && k1[3].setara.length === 0, k1.map((n) => n.setara));

adu("bangun", "tanpa bekal dan pelengkap: kosong", bangunNode([], [], KUR).length === 0);
const dup = bangunNode([{ pilihan: ["python", "go"], wakil: "python", persen: 40 }, { pilihan: ["go", "git"], wakil: "git", persen: 100 }], ["python", "css", "css"], KUR);
adu("bangun", "kunci yang muncul dua kali hanya digambar sekali (bekal, bekal lain, pelengkap)", dup.map((n) => n.id).join() === "dalam:python,dalam:go,dalam:git,luar:css", dup.map((n) => n.id));
adu("bangun", "alternatif yang sudah ada di kelompok pertama tidak ikut kelompok kedua", dup.find((n) => n.id === "dalam:go").kelompok === 0 && dup.find((n) => n.id === "dalam:git").setara.length === 0, dup.map((n) => [n.id, n.kelompok, n.setara]));
const hilang = bangunNode([{ pilihan: ["entah", "lain"], wakil: "entah", persen: 33 }], ["tak-ada"], {});
adu("bangun", "tanpa data kurikulum: label jatuh ke kunci, wakil jatuh ke persen kelompok, lainnya 0",
  hilang[0].label === "entah" && hilang[0].persen === 33 && hilang[1].persen === 0 && hilang[2].persen === 0 && hilang[2].label === "tak-ada", hilang.map((n) => [n.label, n.persen]));
const jepitan = bangunNode([{ pilihan: ["a", "b", "c"], wakil: "a", persen: 0 }], [], { a: { label: "A", persen: 150 }, b: { label: "B", persen: -5 }, c: { label: "C", persen: NaN } });
adu("status", "persen di luar jangkauan dijepit 0..100", jepitan.map((n) => n.persen).join() === "100,0,0", jepitan.map((n) => n.persen));

/* ---- kasus acak berbenih (benih tetap: perubahan benih = korpus lain) */
let benih = 20261028;
const acak = () => { benih = (benih * 1664525 + 1013904223) >>> 0; return benih / 2 ** 32; };
const KUNCI = Array.from({ length: 14 }, (_, i) => `k${i}`);
const kurAcak = Object.fromEntries(KUNCI.map((k, i) => [k, { label: `Kurikulum ${i}`, persen: [0, 12, 40, 62, 100, 100, 7][i % 7] }]));
for (let t = 0; t < 600; t++) {
  const kel = [];
  const pakai = new Set();
  const jumlahKel = 1 + Math.floor(acak() * 5);
  for (let g = 0; g < jumlahKel; g++) {
    const ukuran = 1 + Math.floor(acak() * 3);
    const pil = [];
    while (pil.length < ukuran) { const x = KUNCI[Math.floor(acak() * KUNCI.length)]; if (!pil.includes(x)) pil.push(x); }
    const wakil = pil.reduce((a, x) => (kurAcak[x].persen > kurAcak[a].persen ? x : a), pil[0]);
    kel.push({ pilihan: pil, wakil, persen: kurAcak[wakil].persen });
    pil.forEach((x) => pakai.add(x));
  }
  const pel = Array.from({ length: Math.floor(acak() * 5) }, () => KUNCI[Math.floor(acak() * KUNCI.length)]);
  const n = bangunNode(kel, pel, kurAcak);
  const ids = n.map((x) => x.id);
  adu("bangun", `acak ${t}: id unik`, new Set(ids).size === ids.length, ids);
  adu("bangun", `acak ${t}: tiap alternatif bekal punya simpul dalam`, [...pakai].every((k) => ids.includes(`dalam:${k}`)));
  adu("bangun", `acak ${t}: pelengkap tanpa kembar bekal punya simpul luar, yang kembar tidak`,
    pel.every((k) => (pakai.has(k) ? !ids.includes(`luar:${k}`) : ids.includes(`luar:${k}`))));
  adu("bangun", `acak ${t}: sudut dalam [-90, 270) dan menaik di tiap cincin`,
    ["dalam", "luar"].every((l) => { const s = n.filter((x) => x.lingkar === l).map((x) => x.sudut); return s.every((v, i) => v >= -90 && v < 270 && (i === 0 || v > s[i - 1])); }));
  const dalam = n.filter((x) => x.lingkar === "dalam");
  adu("wakil", `acak ${t}: tepat satu wakil per kelompok, sesuai wakil dari server`,
    kel.every((g, gi) => { const w = dalam.filter((x) => x.kelompok === gi && x.wakil); return w.length <= 1 && (w.length === 0 ? kel.slice(0, gi).some((h) => h.pilihan.includes(g.wakil)) : w[0].kunci === g.wakil); }));
  adu("setara", `acak ${t}: setara simetris dan tidak memuat diri sendiri`,
    n.every((a) => !a.setara.includes(a.id) && a.setara.every((id) => n.find((b) => b.id === id).setara.includes(a.id) && n.find((b) => b.id === id).kelompok === a.kelompok)));
  adu("setara", `acak ${t}: pelengkap tidak punya setara`, n.filter((x) => x.lingkar === "luar").every((x) => x.setara.length === 0));
}

/* ------------------------------------------------------------------- putar */
adu("putar", "satu bingkai penuh (100 ms) pada laju 6 menambah 0,6 derajat", dekat(sudutBerikut(0, 100), 0.6), sudutBerikut(0, 100));
adu("putar", "dua puluh bingkai 50 ms pada laju 6 menambah 6 derajat (satu detik)", dekat(Array.from({ length: 20 }).reduce((a) => sudutBerikut(a, 50), 0), 6, 1e-6));
adu("putar", "melingkar di 360", dekat(sudutBerikut(359.7, 100), 0.3, 1e-9), sudutBerikut(359.7, 100));
adu("putar", "satu bingkai dijepit 100 ms (tab yang kembali dari latar tidak melompat)", dekat(sudutBerikut(0, 5000), 0.6), sudutBerikut(0, 5000));
adu("putar", "selisih waktu negatif atau bukan angka tidak menggeser", sudutBerikut(10, -50) === 10 && sudutBerikut(10, NaN) === 10);
adu("putar", "laju khusus dipakai", dekat(sudutBerikut(0, 100, 36), 3.6), sudutBerikut(0, 100, 36));
for (let t = 0; t < 400; t++) {
  const a = acak() * 360; const dt = acak() * 400;
  const b = sudutBerikut(a, dt);
  adu("putar", `acak ${t}: hasil di [0, 360) dan maju tidak lebih dari jepitan`, b >= 0 && b < 360 && ((b - a + 720) % 360) <= (LAJU * DT_MAKS) / 1000 + 1e-9, { a, dt, b });
}

/* ------------------------------------------------------------------- fokus */
for (const [key, i, n, harap] of [
  ["ArrowRight", 0, 5, 1], ["ArrowDown", 2, 5, 3], ["ArrowRight", 4, 5, 0], ["ArrowLeft", 3, 5, 2], ["ArrowUp", 1, 5, 0], ["ArrowLeft", 0, 5, 4],
  ["Home", 3, 5, 0], ["End", 1, 5, 4], ["ArrowRight", 0, 1, 0], ["ArrowLeft", 0, 1, 0], ["a", 0, 5, null], ["Tab", 1, 5, null], ["Enter", 1, 5, null], ["ArrowRight", 0, 0, null],
]) {
  adu("fokus", `langkahFokus(${JSON.stringify(key)}, ${i}, ${n})`, langkahFokus(key, i, n) === harap, langkahFokus(key, i, n));
}

/* ------------------------------------------------------------ label, ringkas */
const contoh = (o) => ({ id: "dalam:x", kunci: "x", label: "Python", persen: 62, status: "jalan", lingkar: "dalam", sudut: 0, wakil: true, kelompok: 0, setara: [], ...o });
adu("label", "nama aksesibel bekal", labelNode(contoh({})) === "Python, bekal, 62 persen, sedang dikerjakan", labelNode(contoh({})));
adu("label", "nama aksesibel pelengkap", labelNode(contoh({ lingkar: "luar", persen: 100, status: "selesai" })) === "Python, pelengkap, 100 persen, selesai");
adu("label", "persen dibulatkan", labelNode(contoh({ persen: 62.5 })).includes("63 persen") && labelNode(contoh({ persen: 99.6, status: "jalan" })).includes("100 persen"));
adu("ringkas", "tanpa simpul", ringkasOrbit([]) === "Profesi ini belum punya kurikulum di aplikasi ini.");
adu("ringkas", "menghitung yang selesai dan yang sedang dikerjakan", ringkasOrbit(k1) === "2 dari 5 kurikulum di orbit sudah selesai, 3 sedang dikerjakan.", ringkasOrbit(k1));

console.log(`${cacah} perbandingan atas logika orbit bekal`);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: logika orbit bekal memenuhi semua sifat yang dijanjikan.");
