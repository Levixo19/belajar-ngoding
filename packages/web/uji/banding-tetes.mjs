/* Memeriksa fisika tetes kaca cair (`komponen/tetes-teks.ts`) dan shader-nya
 * (`komponen/tetes-shader.ts`).
 *
 * Tidak ada JS lama untuk diadu (komponennya baru) dan tidak ada sisi Python
 * untuk direkam, jadi yang ditagih adalah SIFAT yang dijanjikan komentar kepala
 * modulnya, atas skenario tangan yang angkanya DIUKUR lebih dulu dari fisika
 * sungguhan (bukan ditebak) ditambah ratusan skenario acak berbenih tetap:
 *
 *   [kontrak]   angka yang menjamin bentuk gerak (ambang pecah, umur riak, ...)
 *   [sasaran]   tetes menutupi PERSIS kotak butirnya
 *   [tempat]    berdiri langsung atau berangkat; pemimpin = ujung terdekat
 *   [tunda]     ujung penyusul tertunda lalu menyusul (itu yang merenggang)
 *   [pecah]     jauh = pecah jadi tiga satelit, dekat = tidak pernah
 *   [pegas]     pemimpin sampai cepat; semuanya diam dalam batas waktu
 *   [pipih]     tetes menggepeng saat melaju, dan tidak pernah gepeng terlalu jauh
 *   [riak]      riak lahir saat berhenti, umurnya terbatas, jumlahnya terbatas
 *   [tembok]    ujung tidak pernah menembus dinding bilah
 *   [halus]     tanpa pantulan, tanpa satelit, tanpa riak, dua ujung selalu sama
 *   [mati]      satu langkah dan sudah berdiri
 *   [muncul]    hilang dan muncul lagi tidak terbang dari tempat yang sudah tiada
 *   [kursor]    hanya tingkat penuh yang menyalakan gelombang kursor
 *   [bingkai]   kapan bingkai berikutnya perlu digambar
 *   [uniform]   data shader: urutan, jumlah, pergeseran TEPI
 *   [cadangan]  tetes CSS tanpa WebGL
 *   [tema]      dukungan pembiasan, kaca mati di kontras, palet gelap/terang
 *   [shader]    tiap uniform dideklarasikan dan dipakai, ukuran larik cocok
 *   [acak]      ratusan skenario: sifat tetap benar di setiap langkah
 *
 *     node --experimental-strip-types uji/banding-tetes.mjs
 */

import {
  AMBANG_PECAH, FAKTOR_TUNDA, MAKS_KAPSUL, MAKS_RIAK, MAKS_SATELIT, TEMBOK, TEPI, TUNDA_MS,
  UMUR_RIAK,
  acakBerbenih, arahkan, bacaUniform, buatTetes, celah, dukungBias, gayaCadangan, kacaAktif,
  langkah, nilaiGelap, perluBingkai, pindahLangsung, sasaranDariKotak, tambahRiak,
  tampilSeketika, tunjuk, ukuranBilah,
} from "../src/komponen/tetes-teks.ts";
import { NAMA_UNIFORM, SUMBER_FRAGMEN, SUMBER_VERTEKS } from "../src/komponen/tetes-shader.ts";

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
const hingga = (...n) => n.every((v) => Number.isFinite(v));

const R = acakBerbenih(20261028);
const antara = (a, b) => a + R() * (b - a);

const DT = 1 / 60;
const LEBAR = 920;
const TINGGI = 52;
const kotak = (x, lebar = 84) => ({ kiri: x - lebar / 2, atas: 7, lebar, tinggi: 38 });
const sasaran = (x, lebar = 84) => sasaranDariKotak(kotak(x, lebar));

/** Tetes yang sudah berdiri di `dari`, tampak penuh, siap diarahkan. */
function mulaiDi(dari, lebar = 84, w = LEBAR) {
  const t = buatTetes();
  ukuranBilah(t, w, TINGGI);
  pindahLangsung(t, sasaran(dari, lebar));
  tampilSeketika(t);
  return t;
}

/** Jalankan sampai berhenti bergerak atau `maks` bingkai. Memanggil `tiap(t, i)`
 *  sesudah tiap langkah. Mengembalikan jumlah langkah yang dipakai. */
function jalan(t, mode, benih, maks = 900, tiap = null, dt = DT) {
  const rng = acakBerbenih(benih);
  let now = 0;
  for (let i = 0; i < maks; i++) {
    now += dt * 1000;
    langkah(t, dt, now, mode, rng);
    if (tiap) tiap(t, i);
    if (!t.bergerak && t.satelit.length === 0 && i > 0) return i + 1;
  }
  return maks;
}

/* ------------------------------------------------------------------ kontrak */
{
  adu("kontrak", "tepi kanvas 2 piksel", TEPI === 2, TEPI);
  adu("kontrak", "ambang pecah -6", AMBANG_PECAH === -6, AMBANG_PECAH);
  adu("kontrak", "umur riak 2,4 detik", UMUR_RIAK === 2.4, UMUR_RIAK);
  adu("kontrak", "enam riak", MAKS_RIAK === 6, MAKS_RIAK);
  adu("kontrak", "enam kapsul: dua utama + empat satelit", MAKS_KAPSUL === 6 && MAKS_SATELIT === 4, [MAKS_KAPSUL, MAKS_SATELIT]);
  adu("kontrak", "jeda penyusul 70 ms, lamban 0,08", TUNDA_MS === 70 && FAKTOR_TUNDA === 0.08, [TUNDA_MS, FAKTOR_TUNDA]);
  adu("kontrak", "jarak aman tembok 6", TEMBOK === 6, TEMBOK);
}

/* ------------------------------------------------------------------ sasaran */
for (let i = 0; i < 400; i++) {
  const k = { kiri: antara(0, 800), atas: antara(0, 20), lebar: antara(30, 160), tinggi: antara(20, 50) };
  const s = sasaranDariKotak(k);
  adu("sasaran", "pusat x di tengah kotak", dekat(s.x, k.kiri + k.lebar / 2), [k, s]);
  adu("sasaran", "pusat y di tengah kotak", dekat(s.cy, k.atas + k.tinggi / 2), [k, s]);
  adu("sasaran", "jari-jari setengah tinggi", dekat(s.r, k.tinggi / 2), [k, s]);
  adu("sasaran", "lebar kapsul = lebar kotak kecuali butir lebih sempit dari tingginya",
    dekat(2 * (s.q + s.r), Math.max(k.lebar, k.tinggi)), [k, s]);
  adu("sasaran", "setengah panjang batang tidak negatif", s.q >= 0, s);
}

/* ------------------------------------------------------------------- tempat */
{
  const t = buatTetes();
  ukuranBilah(t, LEBAR, TINGGI);
  adu("tempat", "tetes baru belum siap dan belum hadir", !t.siap && !t.hadir && t.muncul === 0 && !perluBingkai(t));
  arahkan(t, sasaran(200), 0, "penuh");
  adu("tempat", "arah pertama berdiri langsung di tempatnya", t.a.x === 200 && t.b.x === 200 && t.siap && t.hadir && !t.bergerak);
  adu("tempat", "arah pertama TIDAK langsung penuh (tumbuh dari kecil)", t.muncul === 0 && perluBingkai(t));
  tampilSeketika(t);
  adu("tempat", "tampilSeketika memenuhi muncul", t.muncul === 1 && !perluBingkai(t));
  arahkan(t, sasaran(200.3), 100, "penuh");
  adu("tempat", "geser di bawah 0,5 piksel tidak memulai gerak", !t.bergerak);
  arahkan(t, sasaran(500), 100, "penuh");
  adu("tempat", "butir lain memulai gerak, belum pecah", t.bergerak && !t.pecah);
  adu("tempat", "ujung yang lebih dekat ke tujuan memimpin",
    (t.pemimpin === 0) === (Math.abs(500 - t.a.x) <= Math.abs(500 - t.b.x)));
  adu("tempat", "jeda penyusul 70 ms dari sekarang", t.tertinggalSampai === 100 + TUNDA_MS, t.tertinggalSampai);

  // Pemimpin jatuh ke ujung yang lebih dekat, di kedua arah.
  const k = buatTetes();
  ukuranBilah(k, LEBAR, TINGGI);
  pindahLangsung(k, sasaran(300));
  tampilSeketika(k);
  k.a.x = 290; k.b.x = 312; // ujung kiri dan kanan berbeda
  arahkan(k, sasaran(700), 0, "penuh");
  adu("tempat", "tujuan di kanan: ujung kanan (b) memimpin", k.pemimpin === 1, k.pemimpin);
  arahkan(k, sasaran(100), 0, "penuh");
  adu("tempat", "tujuan di kiri: ujung kiri (a) memimpin", k.pemimpin === 0, k.pemimpin);

  // Butir hilang lalu muncul lagi: tidak terbang dari tempat yang sudah tiada.
  const h = mulaiDi(200);
  arahkan(h, null, 0, "penuh");
  adu("tempat", "null menyembunyikan (hadir false)", !h.hadir);
  arahkan(h, sasaran(800), 5, "penuh");
  adu("tempat", "muncul lagi berdiri LANGSUNG di tujuan, tanpa gerak",
    h.hadir && h.a.x === 800 && h.b.x === 800 && !h.bergerak, [h.a.x, h.bergerak]);
  // Mode mati: berdiri langsung walau sudah berdiri sebelumnya.
  const m = mulaiDi(200);
  arahkan(m, sasaran(700), 0, "mati");
  adu("mati", "arah di tingkat mati langsung berdiri", m.a.x === 700 && m.b.x === 700 && !m.bergerak && m.muncul === 1);
  // Menunjuk null tidak mengubah apa pun selain hadir.
  const n = mulaiDi(200);
  const sebelum = JSON.stringify([n.a, n.b, n.sasaran]);
  arahkan(n, null, 0, "penuh");
  adu("tempat", "null tidak menyentuh posisi", JSON.stringify([n.a, n.b, n.sasaran]) === sebelum);
}

/* -------------------------------------------------- tunda, pecah, pegas, pipih */
{
  // [tunda] 48 ms pertama: ujung penyusul nyaris diam, pemimpin sudah bergerak.
  for (const [dari, ke] of [[150, 500], [700, 250], [150, 760]]) {
    const t = mulaiDi(dari);
    arahkan(t, sasaran(ke), 0, "penuh");
    const rng = acakBerbenih(1);
    let now = 0;
    for (let i = 0; i < 3; i++) { now += 16; langkah(t, 0.016, now, "penuh", rng); }
    const arah = Math.sign(ke - dari);
    const lead = (t.pemimpin === 0 ? t.a : t.b);
    const tail = (t.pemimpin === 0 ? t.b : t.a);
    const geserLead = (lead.x - dari) * arah;
    const geserTail = (tail.x - dari) * arah;
    adu("tunda", `${dari}->${ke}: pemimpin sudah melaju di 48 ms`, geserLead > 1, [geserLead, geserTail]);
    adu("tunda", `${dari}->${ke}: penyusul tertinggal jauh (di bawah 25 persen pemimpin)`, geserTail < geserLead * 0.25, [geserLead, geserTail]);
    // Setelah jeda habis penyusul menyusul: celah antar ujung mengecil lagi.
    jalan(t, "penuh", 1, 900);
    adu("tunda", `${dari}->${ke}: akhirnya kedua ujung bertemu di tujuan`, t.a.x === ke && t.b.x === ke, [t.a.x, t.b.x]);
  }

  // [pecah] angka hasil ukuran: <=110 piksel tak pernah pecah, >=270 selalu.
  for (const [dari, ke, harusPecah] of [[150, 170, false], [150, 200, false], [150, 260, false],
      [150, 420, true], [150, 760, true], [760, 150, true]]) {
    for (const benih of [1, 2, 3]) {
      const t = mulaiDi(dari);
      arahkan(t, sasaran(ke), 0, "penuh");
      let pecahSekali = false;
      let maksSat = 0;
      let minSy = 1;
      let riakSaatBerhenti = null;
      let selesaiPada = -1;
      let galatSebelum = Infinity;
      let galatSyPeregangan = Infinity;
      let lompatan = null;
      let lompatanSy = null;
      const langkahan = jalan(t, "penuh", benih, 900, (x, i) => {
        if (x.pecah) pecahSekali = true;
        maksSat = Math.max(maksSat, x.satelit.length);
        minSy = Math.min(minSy, x.sy.s);
        if (selesaiPada < 0 && !x.bergerak) {
          selesaiPada = i;
          riakSaatBerhenti = x.riak.map((r) => r.amp);
          lompatan = galatSebelum; // seberapa jauh ujung dari tujuan TEPAT sebelum dinyatakan diam
          lompatanSy = galatSyPeregangan; // dan seberapa jauh peregangan vertikal dari bulat
        }
        galatSebelum = Math.max(Math.abs(ke - x.a.x), Math.abs(ke - x.b.x));
        galatSyPeregangan = Math.abs(1 - x.sy.s);
      });
      const nama = `${dari}->${ke} benih ${benih}`;
      adu("pegas", `${nama}: dinyatakan diam hanya bila ujung sudah dalam 0,6 px (tidak melompat)`, lompatan !== null && lompatan <= 0.6, lompatan);
      adu("pegas", `${nama}: dan hanya bila peregangan vertikal sudah bulat (tidak melompat)`, lompatanSy !== null && lompatanSy <= 0.01, lompatanSy);
      adu("pecah", `${nama}: ${harusPecah ? "pecah" : "tidak pecah"}`, pecahSekali === harusPecah, pecahSekali);
      adu("pecah", `${nama}: satelit ${harusPecah ? "tiga" : "nol"}`, maksSat === (harusPecah ? 3 : 0), maksSat);
      adu("pecah", `${nama}: berhenti dengan riak berukuran ${harusPecah ? "1,2" : "0,7"}`,
        riakSaatBerhenti !== null && riakSaatBerhenti.length === 1 && riakSaatBerhenti[0] === (harusPecah ? 1.2 : 0.7), riakSaatBerhenti);
      adu("pegas", `${nama}: diam dalam 1,3 detik`, langkahan * DT <= 1.3, langkahan * DT);
      adu("pegas", `${nama}: kedua ujung tepat di tujuan`, t.a.x === ke && t.b.x === ke && t.a.v === 0 && t.b.v === 0);
      adu("pegas", `${nama}: tidak lagi bergerak dan tanpa satelit`, !t.bergerak && t.satelit.length === 0);
      if (harusPecah && Math.abs(ke - dari) >= 600) {
        adu("pipih", `${nama}: menggepeng saat melaju jauh (0,65 sampai 0,85)`, minSy >= 0.65 && minSy <= 0.85, minSy);
      }
      if (Math.abs(ke - dari) <= 25) {
        adu("pipih", `${nama}: gerak pendek nyaris tidak menggepeng`, minSy > 0.97, minSy);
      }
    }
  }

  // [pegas] pemimpin sampai cepat: dalam 0,4 detik sudah dalam 6 piksel dari tujuan.
  for (const [dari, ke] of [[150, 760], [760, 150], [150, 420]]) {
    const t = mulaiDi(dari);
    arahkan(t, sasaran(ke), 0, "penuh");
    jalan(t, "penuh", 1, 18);
    // Pegas penyusul LEBIH LEMBUT: pada 0,3 detik galatnya sekitar delapan kali galat
    // pemimpin (terukur 8,3). Jeda 70 ms saja hanya memberi sekitar 2,4 kali, jadi
    // penyusul yang sekeras pemimpin tidak lolos dari sini.
    const pemimpin = t.pemimpin === 0 ? t.a : t.b;
    const penyusul = t.pemimpin === 0 ? t.b : t.a;
    const galatPemimpin = Math.abs(ke - pemimpin.x);
    const galatPenyusul = Math.abs(ke - penyusul.x);
    adu("pegas", `${dari}->${ke}: penyusul jauh lebih lambat dari pemimpin pada 0,3 detik`, galatPenyusul >= 5 * galatPemimpin, [galatPemimpin, galatPenyusul]);
    jalan(t, "penuh", 1, 6);
    const lead = t.pemimpin === 0 ? t.a : t.b;
    adu("pegas", `${dari}->${ke}: pemimpin dalam 6 px dalam 0,4 detik`, Math.abs(ke - lead.x) <= 6, Math.abs(ke - lead.x));
  }

  // [pecah] satelit nyata: tiga, di antara dua ujung, jari-jari dan kekakuan dalam rentang.
  {
    const t = mulaiDi(150);
    arahkan(t, sasaran(760), 0, "penuh");
    const rng = acakBerbenih(7);
    let now = 0;
    let dilihat = false;
    for (let i = 0; i < 60 && !dilihat; i++) {
      now += 16;
      langkah(t, 0.016, now, "penuh", rng);
      if (t.pecah) {
        dilihat = true;
        adu("pecah", "tepat tiga satelit lahir", t.satelit.length === 3, t.satelit.length);
        adu("pecah", "tiap satelit: jari-jari di (0,6; 8], kekakuan 70..160, di dalam bilah",
          t.satelit.every((m) => m.r > 0.6 && m.r <= 8 && m.k >= 70 && m.k <= 160 && m.x > 0 && m.x < LEBAR));
        adu("pecah", "celah sudah melewati ambang pada saat pecah", celah(t) > AMBANG_PECAH, celah(t));
      }
    }
    adu("pecah", "perjalanan jauh akhirnya pecah dalam satu detik", dilihat);
  }
}

/* ----------------------------------------------------- tembok, riak, bingkai */
{
  // [tembok] tujuan persis di batas kiri: pegas yang sedikit melampaui dijepit.
  const q = 0; // kapsul bulat: butir selebar tingginya
  const r = 19;
  const kiri = TEMBOK + q + r - 3;
  const t = mulaiDi(700, 38);
  arahkan(t, sasaran(kiri, 38), 0, "penuh");
  let minX = 1e9;
  jalan(t, "penuh", 1, 900, (x) => { minX = Math.min(minX, x.a.x, x.b.x); });
  adu("tembok", "tidak ada ujung yang menembus dinding kiri", minX >= kiri - 1e-9, [minX, kiri]);
  const w = mulaiDi(200, 38);
  const kanan = LEBAR - TEMBOK - q - r + 3;
  arahkan(w, sasaran(kanan, 38), 0, "penuh");
  let maksX = -1e9;
  jalan(w, "penuh", 1, 900, (x) => { maksX = Math.max(maksX, x.a.x, x.b.x); });
  adu("tembok", "tidak ada ujung yang menembus dinding kanan", maksX <= kanan + 1e-9, [maksX, kanan]);

  // [riak] umur terbatas, jumlah terbatas, tambah menggeser yang tertua.
  const p = mulaiDi(300);
  for (let i = 0; i < 9; i++) tambahRiak(p, i, 0, 1);
  adu("riak", "paling banyak enam riak, yang tertua tergeser", p.riak.length === MAKS_RIAK && p.riak[0].x === 3, p.riak.map((x) => x.x));
  const rng = acakBerbenih(1);
  let now = 0;
  for (let i = 0; i < Math.ceil((UMUR_RIAK - 0.1) / DT); i++) { now += 16; langkah(p, DT, now, "penuh", rng); }
  adu("riak", "riak masih ada sebelum 2,3 detik", p.riak.length === MAKS_RIAK && perluBingkai(p), p.riak.length);
  for (let i = 0; i < Math.ceil(0.3 / DT); i++) { now += 16; langkah(p, DT, now, "penuh", rng); }
  adu("riak", "semua riak lenyap sesudah 2,4 detik", p.riak.length === 0 && !perluBingkai(p), p.riak.length);
  adu("riak", "umur bertambah sebesar dt", (() => {
    const z = mulaiDi(100);
    tambahRiak(z, 0, 0, 1);
    langkah(z, 0.5, 0, "penuh", rng);
    return dekat(z.riak[0].umur, 0.5);
  })());

  // [bingkai] diam = tidak perlu bingkai; bergerak = perlu.
  const d = mulaiDi(300);
  adu("bingkai", "tetes diam tidak meminta bingkai", !perluBingkai(d));
  arahkan(d, sasaran(600), 0, "penuh");
  adu("bingkai", "tetes bergerak meminta bingkai", perluBingkai(d));
  jalan(d, "penuh", 1, 900);
  adu("bingkai", "riak sesudah berhenti masih meminta bingkai", d.riak.length === 1 && perluBingkai(d));
}

/* ------------------------------------------------- waktu tidak pernah mundur */
{
  // Bingkai pertama sesudah diam bisa berdurasi negatif (cap waktu rAF = awal bingkai, lebih
  // awal dari performance.now() saat bingkai diminta). Ditemukan di peramban: kursor.s menjadi
  // negatif, perluBingkai salah, dan putaran berhenti padahal penunjuk masih di atas bilah.
  for (const mode of ["penuh", "halus", "mati"]) {
    const bandingkan = (dt) => {
      const t = mulaiDi(150);
      tunjuk(t, 300, 20);
      arahkan(t, sasaran(500), 0, mode);
      langkah(t, dt, 16, mode, acakBerbenih(1));
      return JSON.stringify(t);
    };
    adu("bingkai", `${mode}: dt negatif sama dengan dt nol (waktu tidak mundur)`, bandingkan(-0.05) === bandingkan(0), mode);
  }
  const t = mulaiDi(300);
  tunjuk(t, 400, 20);
  langkah(t, -0.02, 0, "penuh", acakBerbenih(1));
  adu("bingkai", "bingkai pertama berdurasi negatif tidak membuat kursor.s negatif", t.kursor.s >= 0, t.kursor.s);
  // Bingkai pertama berdurasi nol: kursor.s masih nol, tetapi penunjuk jelas di atas bilah.
  // Dulu perluBingkai hanya membaca kursor.s, dan putaran berhenti sebelum gelombang naik.
  adu("kursor", "kursor menyala tetap meminta bingkai walau bingkai pertama berdurasi nol (kursor.s masih nol)",
    t.kursor.s === 0 && perluBingkai(t, "penuh"), t.kursor.s);
  adu("kursor", "di tingkat selain penuh, kursor yang tertinggal menyala tidak menahan putaran",
    !perluBingkai(t, "halus") && !perluBingkai(t, "mati"));
  langkah(t, DT, 16, "penuh", acakBerbenih(1));
  adu("bingkai", "kursor tetap meminta bingkai sesudah bingkai berdurasi negatif", perluBingkai(t), t.kursor.s);
  // dt nol: tidak mengubah dinamika (dipakai komponen untuk menerapkan tingkat gerak baru).
  const n = mulaiDi(150);
  arahkan(n, sasaran(500), 0, "penuh");
  const sebelum = JSON.stringify([n.a, n.b, n.sy, n.satelit]);
  langkah(n, 0, 0, "penuh", acakBerbenih(1));
  adu("bingkai", "dt nol tidak menggerakkan apa pun", JSON.stringify([n.a, n.b, n.sy, n.satelit]) === sebelum);
}

/* ------------------------------------------------------------------- halus */
for (const [dari, ke] of [[150, 760], [760, 150], [200, 330]]) {
  const t = mulaiDi(dari);
  arahkan(t, sasaran(ke), 0, "halus");
  const arah = Math.sign(ke - dari);
  let sama = true;
  let lewat = 0;
  let adaSat = false;
  let adaRiak = false;
  let sy = 1;
  const langkahan = jalan(t, "halus", 1, 900, (x) => {
    if (x.a.x !== x.b.x) sama = false;
    lewat = Math.max(lewat, (x.a.x - ke) * arah);
    if (x.satelit.length) adaSat = true;
    if (x.riak.length) adaRiak = true;
    sy = Math.min(sy, x.sy.s);
  });
  adu("halus", `${dari}->${ke}: dua ujung selalu sama (tidak merenggang)`, sama);
  adu("halus", `${dari}->${ke}: tidak melampaui tujuan (teredam kritis)`, lewat <= 0.01, lewat);
  adu("halus", `${dari}->${ke}: tanpa satelit, tanpa riak, tidak menggepeng`, !adaSat && !adaRiak && sy === 1);
  adu("halus", `${dari}->${ke}: berhenti dalam 1,2 detik, tepat di tujuan`, langkahan * DT <= 1.2 && t.a.x === ke && t.b.x === ke, langkahan * DT);
  adu("halus", `${dari}->${ke}: tidak pernah pecah`, !t.pecah);
}
{
  const t = mulaiDi(200);
  tunjuk(t, 300, 20);
  arahkan(t, sasaran(500), 0, "halus");
  jalan(t, "halus", 1, 60);
  adu("halus", "kursor tidak menyalakan gelombang", t.kursor.s < 0.01, t.kursor.s);
}

/* -------------------------------------------------------------------- mati */
{
  const t = mulaiDi(150);
  t.satelit.push({ x: 300, y: 26, vx: 1, vy: 1, r: 5, k: 100 });
  tambahRiak(t, 100, 20, 1);
  arahkan(t, sasaran(760), 0, "penuh");
  langkah(t, DT, 16, "mati", acakBerbenih(1));
  adu("mati", "satu langkah: berdiri di tujuan tanpa satelit dan tanpa riak",
    t.a.x === 760 && t.b.x === 760 && t.satelit.length === 0 && t.riak.length === 0 && !t.bergerak, [t.a.x, t.satelit.length, t.riak.length]);
  adu("mati", "tidak lagi meminta bingkai", !perluBingkai(t));
}

/* ------------------------------------------------------------------ muncul */
{
  const t = mulaiDi(300);
  arahkan(t, null, 0, "penuh");
  adu("muncul", "sesudah disembunyikan, bingkai masih diminta sampai lenyap", perluBingkai(t));
  const rng = acakBerbenih(1);
  let now = 0;
  let i = 0;
  while (perluBingkai(t) && i < 200) { now += 16; langkah(t, DT, now, "penuh", rng); i++; }
  adu("muncul", "lenyap dalam 0,8 detik", i * DT <= 0.8 && t.muncul === 0, [i * DT, t.muncul]);
  const u = bacaUniform(t);
  adu("muncul", "tetes lenyap = jari-jari kapsul utama nol (shader membuangnya)", u.kapsul[3] === 0 && u.kapsul[7] === 0, [u.kapsul[3], u.kapsul[7]]);
  adu("muncul", "sesudah lenyap tidak ada lagi yang meminta bingkai", !perluBingkai(t));
  arahkan(t, sasaran(500), 0, "penuh");
  i = 0;
  while (perluBingkai(t) && i < 200) { now += 16; langkah(t, DT, now, "penuh", rng); i++; }
  adu("muncul", "muncul lagi penuh dalam 0,8 detik", t.muncul === 1 && i * DT <= 0.8, [t.muncul, i * DT]);
}

/* ------------------------------------------------------------------ kursor */
{
  const t = mulaiDi(300);
  tunjuk(t, 400, 20);
  const rng = acakBerbenih(1);
  for (let i = 0; i < 60; i++) langkah(t, DT, i * 16, "penuh", rng);
  adu("kursor", "tingkat penuh: gelombang menyala mendekati 1", t.kursor.s > 0.95, t.kursor.s);
  adu("kursor", "selama menyala bingkai terus diminta", perluBingkai(t));
  tunjuk(t, null);
  // Penunjuk sudah pergi tetapi gelombang belum habis: bingkai masih diminta sampai ia luruh.
  adu("kursor", "penunjuk baru pergi: gelombang masih luruh, bingkai tetap diminta", t.kursor.s > 0.9 && perluBingkai(t, "penuh"), t.kursor.s);
  for (let i = 0; i < 90; i++) langkah(t, DT, i * 16, "penuh", rng);
  adu("kursor", "sesudah pergi, luruh dan berhenti meminta bingkai", t.kursor.s < 0.01 && !perluBingkai(t), t.kursor.s);
  const h = mulaiDi(300);
  tunjuk(h, 400, 20);
  for (let i = 0; i < 60; i++) langkah(h, DT, i * 16, "halus", rng);
  adu("kursor", "tingkat halus: tidak menyala", h.kursor.s < 0.01, h.kursor.s);
  const m = mulaiDi(300);
  tunjuk(m, 400, 20);
  for (let i = 0; i < 60; i++) langkah(m, DT, i * 16, "mati", rng);
  adu("kursor", "tingkat mati: tidak menyala", m.kursor.s < 0.01, m.kursor.s);
  const u = bacaUniform((() => { const z = mulaiDi(300); tunjuk(z, 50, 10); return z; })());
  adu("kursor", "kursor di uniform digeser TEPI", u.kursor[0] === 50 + TEPI && u.kursor[1] === 10 + TEPI);
}

/* ----------------------------------------------------------------- uniform */
{
  // Diam: kedua kapsul utama sama, di pusat butir, digeser TEPI.
  const s = sasaran(300, 90);
  const t = mulaiDi(300, 90);
  const u = bacaUniform(t);
  adu("uniform", "enam kapsul x empat angka, enam sy, enam riak x empat",
    u.kapsul.length === 24 && u.sy.length === 6 && u.riak.length === 24);
  adu("uniform", "kapsul pertama di pusat butir, digeser TEPI",
    dekat(u.kapsul[0], 300 + TEPI, 1e-4) && dekat(u.kapsul[1], s.cy + TEPI, 1e-4), [u.kapsul[0], u.kapsul[1]]);
  adu("uniform", "kapsul pertama: setengah panjang q dan jari-jari r (diam)",
    dekat(u.kapsul[2], s.q, 1e-4) && dekat(u.kapsul[3], s.r, 1e-4), [u.kapsul[2], u.kapsul[3], s.q, s.r]);
  adu("uniform", "kapsul kedua sama dengan yang pertama saat diam",
    dekat(u.kapsul[4], u.kapsul[0], 1e-4) && dekat(u.kapsul[6], u.kapsul[2], 1e-4) && dekat(u.kapsul[7], u.kapsul[3], 1e-4));
  adu("uniform", "tanpa satelit: kapsul 3 sampai 6 kosong (jari-jari 0)",
    [11, 15, 19, 23].every((i) => u.kapsul[i] === 0) && [8, 9, 10, 12, 16, 20].every((i) => u.kapsul[i] === 0));
  adu("uniform", "sy semua 1 saat diam", Array.from(u.sy).every((v) => v === 1));
  adu("uniform", "tanpa riak: seluruhnya nol", Array.from(u.riak).every((v) => v === 0));

  // Bergerak: pemimpin dulu; satelit; riak digeser TEPI; sy untuk dua kapsul pertama.
  const g = mulaiDi(150);
  arahkan(g, sasaran(760), 0, "penuh");
  const rng = acakBerbenih(3);
  let now = 0;
  for (let i = 0; i < 6; i++) { now += 16; langkah(g, DT, now, "penuh", rng); }
  tambahRiak(g, 77, 13, 0.9);
  const v = bacaUniform(g);
  const lead = g.pemimpin === 0 ? g.a : g.b;
  const tail = g.pemimpin === 0 ? g.b : g.a;
  adu("uniform", "kapsul pertama = ujung pemimpin", dekat(v.kapsul[0], lead.x + TEPI, 1e-3), [v.kapsul[0], lead.x]);
  adu("uniform", "kapsul kedua = ujung penyusul", dekat(v.kapsul[4], tail.x + TEPI, 1e-3), [v.kapsul[4], tail.x]);
  adu("uniform", "pemimpin dan penyusul berbeda saat melaju", Math.abs(v.kapsul[0] - v.kapsul[4]) > 5);
  adu("uniform", "sy dua kapsul pertama = sy tetes, sisanya 1",
    dekat(v.sy[0], g.sy.s, 1e-5) && dekat(v.sy[1], g.sy.s, 1e-5) && [2, 3, 4, 5].every((i) => v.sy[i] === 1));
  g.satelit.slice(0, 4).forEach((m, i) => {
    adu("uniform", `satelit ${i} di slot kapsul ${i + 2}: x, y digeser TEPI, jari-jari`,
      dekat(v.kapsul[8 + i * 4], m.x + TEPI, 1e-3) && dekat(v.kapsul[9 + i * 4], m.y + TEPI, 1e-3)
      && v.kapsul[10 + i * 4] === 0 && dekat(v.kapsul[11 + i * 4], m.r, 1e-4));
  });
  const terakhir = g.riak[g.riak.length - 1];
  adu("uniform", "riak terbaru ada di uniform, digeser TEPI",
    Array.from({ length: 6 }, (_, i) => i).some((i) => dekat(v.riak[i * 4], terakhir.x + TEPI, 1e-3)
      && dekat(v.riak[i * 4 + 1], terakhir.y + TEPI, 1e-3) && dekat(v.riak[i * 4 + 3], 0.9, 1e-5)));

  // Banyak satelit: dipotong di empat; banyak riak: dipotong di enam.
  const b = mulaiDi(300);
  for (let i = 0; i < 7; i++) b.satelit.push({ x: 200 + i, y: 26, vx: 0, vy: 0, r: 5, k: 90 });
  const ub = bacaUniform(b);
  adu("uniform", "satelit lebih dari empat dipotong, bukan menimpa kapsul utama",
    ub.kapsul.length === 24 && dekat(ub.kapsul[0], 300 + TEPI, 1e-4) && dekat(ub.kapsul[8], 200 + TEPI, 1e-4) && dekat(ub.kapsul[20], 203 + TEPI, 1e-4));
  // Tetes setengah tampak: jari-jari kapsul utama dikali muncul.
  const sm = mulaiDi(300);
  sm.muncul = 0.5;
  const us = bacaUniform(sm);
  adu("uniform", "muncul 0,5 memangkas jari-jari kapsul utama jadi setengah", dekat(us.kapsul[3], sm.sasaran.r * 0.5, 1e-4), us.kapsul[3]);
}

/* ---------------------------------------------------------------- cadangan */
{
  const s = sasaran(300, 90);
  const t = mulaiDi(300, 90);
  const g = gayaCadangan(t);
  adu("cadangan", "diam: lebar = lebar butir, geser = tepi kiri butir",
    dekat(g.lebar, 90, 1e-9) && dekat(g.geser, 255, 1e-9), g);
  adu("cadangan", "diam: tinggi dan atas = kotak butir, tanpa skala", dekat(g.tinggi, 38) && dekat(g.atas, s.cy - 19) && g.skalaY === 1, g);
  adu("cadangan", "tampak saat muncul penuh, tidak saat tersembunyi", g.tampak && !gayaCadangan((() => { const z = mulaiDi(300); z.muncul = 0.01; return z; })()).tampak);
  const m = mulaiDi(150, 90);
  arahkan(m, sasaran(760, 90), 0, "penuh");
  const rng = acakBerbenih(1);
  let now = 0;
  for (let i = 0; i < 8; i++) { now += 16; langkah(m, DT, now, "penuh", rng); }
  const gm = gayaCadangan(m);
  adu("cadangan", "melaju: lebih lebar dari butir (merenggang), skala vertikal di bawah 1",
    gm.lebar > 100 && gm.skalaY < 1, gm);
  adu("cadangan", "melaju: tepi kiri = ujung paling kiri dikurangi jari-jari",
    gm.geser < Math.min(m.a.x, m.b.x), [gm.geser, m.a.x, m.b.x]);
}

/* -------------------------------------------------------------------- tema */
{
  const CHROME = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36";
  const EDGE = CHROME + " Edg/155.0.0.0";
  const FIREFOX = "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0";
  const SAFARI = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15";
  adu("tema", "Chrome yang mendukung url() di backdrop-filter: bias nyala", dukungBias(CHROME, true) === true);
  adu("tema", "Edge: bias nyala", dukungBias(EDGE, true) === true);
  adu("tema", "Firefox: bias mati walau CSS mengaku bisa", dukungBias(FIREFOX, true) === false);
  adu("tema", "Safari: bias mati", dukungBias(SAFARI, true) === false);
  // UA Firefox sungguhan tidak memuat "Chrome/", jadi pengecualian Firefox hanya
  // bergigi untuk UA hibrida (peramban turunan yang menyamar). Tanpa kasus ini
  // pengecualiannya bisa dihapus dan tidak ada yang memerah.
  adu("tema", "UA hibrida Chrome + Firefox: bias mati", dukungBias(CHROME + " Firefox/140.0", true) === false);
  adu("tema", "Chrome tanpa dukungan CSS: bias mati", dukungBias(CHROME, false) === false);
  adu("tema", "kaca mati hanya di kontras", ["gelap", "malam", "terang", undefined].every((x) => kacaAktif(x)) && kacaAktif("kontras") === false);
  adu("tema", "palet: terang 0, selebihnya 1", nilaiGelap("terang") === 0 && ["gelap", "malam", "kontras", undefined].every((x) => nilaiGelap(x) === 1));
  const a = acakBerbenih(5);
  const b = acakBerbenih(5);
  let sama = true;
  let dalam = true;
  for (let i = 0; i < 200; i++) { const x = a(); if (x !== b()) sama = false; if (!(x >= 0 && x < 1)) dalam = false; }
  adu("tema", "pembangkit berbenih: benih sama = deret sama, di [0,1)", sama && dalam);
  adu("tema", "benih berbeda = deret berbeda", acakBerbenih(5)() !== acakBerbenih(6)());
}

/* ------------------------------------------------------------------ shader */
{
  const deklarasi = [...SUMBER_FRAGMEN.matchAll(/^uniform\s+\w+\s+(\w+)(\[(\d+)\])?\s*;/gm)];
  const nama = deklarasi.map((m) => m[1]);
  adu("shader", "tiap nama di NAMA_UNIFORM dideklarasikan di GLSL", NAMA_UNIFORM.every((n) => nama.includes(n)),
    NAMA_UNIFORM.filter((n) => !nama.includes(n)));
  adu("shader", "tiap uniform di GLSL terdaftar di NAMA_UNIFORM", nama.every((n) => NAMA_UNIFORM.includes(n)),
    nama.filter((n) => !NAMA_UNIFORM.includes(n)));
  adu("shader", "tanpa nama ganda", new Set(NAMA_UNIFORM).size === NAMA_UNIFORM.length);
  const ukuran = Object.fromEntries(deklarasi.map((m) => [m[1], m[3] ? Number(m[3]) : 1]));
  adu("shader", "larik kapsul dan sy seukuran MAKS_KAPSUL", ukuran.uKapsul === MAKS_KAPSUL && ukuran.uSy === MAKS_KAPSUL, ukuran);
  adu("shader", "larik riak seukuran MAKS_RIAK", ukuran.uRiak === MAKS_RIAK, ukuran);
  adu("shader", "setiap perulangan atas larik berbatas enam", (SUMBER_FRAGMEN.match(/i < 6/g) ?? []).length === 2);
  adu("shader", "satu main, satu gl_FragColor", (SUMBER_FRAGMEN.match(/void main\(\)/g) ?? []).length === 1 && (SUMBER_FRAGMEN.match(/gl_FragColor/g) ?? []).length === 1);
  adu("shader", "kurung kurawal dan kurung biasa seimbang", (() => {
    const hitung = (a, b) => (SUMBER_FRAGMEN.match(new RegExp("\\" + a, "g")) ?? []).length === (SUMBER_FRAGMEN.match(new RegExp("\\" + b, "g")) ?? []).length;
    return hitung("{", "}") && hitung("(", ")") && hitung("[", "]");
  })());
  adu("shader", "presisi float diumumkan", /precision (high|medium)p float;/.test(SUMBER_FRAGMEN));
  adu("shader", "ambang kapsul ada (jari-jari > 0,5 = tampak)", SUMBER_FRAGMEN.includes("uKapsul[i].w > .5"));
  adu("shader", "gabungan halus tetes 13 dan topeng bilah menjepit tetes ke dalam bilah",
    SUMBER_FRAGMEN.includes("13.)") && SUMBER_FRAGMEN.includes("smoothstep(1., -2., dp)"));
  adu("shader", "keluaran alfa terkali-dulu: warna dan alfa ditulis bersama", /gl_FragColor = vec4\(c, a\);/.test(SUMBER_FRAGMEN));
  adu("shader", "verteks: satu atribut a, satu segitiga layar penuh", SUMBER_VERTEKS.includes("attribute vec2 a;") && SUMBER_VERTEKS.includes("gl_Position"));
}

/* ------------------------------------------------------------------- acak */
{
  const SKENARIO = 260;
  for (let n = 0; n < SKENARIO; n++) {
    const w = Math.round(antara(700, 1100));
    const lebarButir = Math.round(antara(60, 130));
    const kiri = TEMBOK + lebarButir / 2 + 3;
    const kanan = w - TEMBOK - lebarButir / 2 - 3;
    const dari = antara(kiri, kanan);
    const ke = antara(kiri, kanan);
    const mode = ["penuh", "penuh", "penuh", "halus", "mati"][Math.floor(R() * 5)];
    const t = mulaiDi(dari, lebarButir, w);
    arahkan(t, sasaran(ke, lebarButir), 0, mode);
    const sasaranKedua = R() < 0.35 ? antara(kiri, kanan) : null;
    const gantiMode = R() < 0.15 ? "mati" : null;
    const rng = acakBerbenih(1000 + n);
    let now = 0;
    for (let i = 0; i < 1000; i++) {
      now += 16;
      if (i === 12 && sasaranKedua !== null) arahkan(t, sasaran(sasaranKedua, lebarButir), now, mode);
      const m = i === 40 && gantiMode ? gantiMode : mode;
      langkah(t, DT, now, m, rng);
      const dasar = `acak #${n} ${mode} langkah ${i}`;
      const angka = hingga(t.a.x, t.a.v, t.b.x, t.b.v, t.sy.s, t.sy.v, t.q, t.muncul, t.waktu);
      if (!angka) { adu("acak", `${dasar}: semua bilangan terhingga`, false); break; }
      const kiriW = TEMBOK + t.q + t.sasaran.r - 3;
      const kananW = w - TEMBOK - t.q - t.sasaran.r + 3;
      if (m === "penuh") {
        adu("acak", `${dasar}: ujung di dalam dinding`, t.a.x >= kiriW - 1e-6 && t.a.x <= kananW + 1e-6 && t.b.x >= kiriW - 1e-6 && t.b.x <= kananW + 1e-6, [t.a.x, t.b.x, kiriW, kananW]);
        adu("acak", `${dasar}: sy dalam rentang wajar`, t.sy.s > 0.3 && t.sy.s < 1.7, t.sy.s);
        adu("acak", `${dasar}: pecah dinyatakan begitu celah melewati ambang`, !(t.bergerak && !t.pecah && celah(t) > AMBANG_PECAH), celah(t));
        adu("acak", `${dasar}: satelit sehat`, t.satelit.every((s) => hingga(s.x, s.y, s.r) && s.r > 0.6 && s.x >= 0 && s.x <= w), t.satelit.length);
      }
      adu("acak", `${dasar}: riak terbatas jumlah dan umur`, t.riak.length <= MAKS_RIAK && t.riak.every((r) => r.umur < UMUR_RIAK + 1e-9));
      const u = bacaUniform(t);
      adu("acak", `${dasar}: uniform berukuran tetap dan terhingga`, u.kapsul.length === 24 && u.sy.length === 6 && u.riak.length === 24
        && Array.from(u.kapsul).every(Number.isFinite) && Array.from(u.riak).every(Number.isFinite));
      if (m === "mati") {
        adu("acak", `${dasar}: tingkat mati berdiri di tujuan`, t.a.x === t.sasaran.x && t.b.x === t.sasaran.x && !t.bergerak);
      }
      if (!perluBingkai(t) && !t.bergerak) {
        adu("acak", `${dasar}: yang berhenti meminta bingkai berdiri di tujuan`, t.a.x === t.sasaran.x && t.b.x === t.sasaran.x && t.satelit.length === 0, [t.a.x, t.sasaran.x]);
        break;
      }
    }
    adu("acak", `acak #${n} ${mode}: tidak menggantung (berhenti meminta bingkai dalam 16 detik)`, !perluBingkai(t) || t.kursor.nyala, [mode, t.bergerak, t.satelit.length, t.riak.length]);
  }

  // Determinisme: benih sama = riwayat sama sampai ke satelit; benih lain = satelit lain.
  const jejak = (benih) => {
    const t = mulaiDi(150);
    arahkan(t, sasaran(760), 0, "penuh");
    const rng = acakBerbenih(benih);
    const hasil = [];
    let now = 0;
    for (let i = 0; i < 80; i++) { now += 16; langkah(t, DT, now, "penuh", rng); hasil.push(JSON.stringify([t.a, t.b, t.sy, t.satelit, t.riak])); }
    return hasil;
  };
  const a = jejak(11), b = jejak(11), c = jejak(12);
  adu("acak", "benih sama = riwayat gerak identik", a.every((x, i) => x === b[i]));
  adu("acak", "benih berbeda = satelit berbeda", a.some((x, i) => x !== c[i]));
  adu("acak", "tanpa pecah, benih tidak berpengaruh", (() => {
    const k = (benih) => { const t = mulaiDi(150); arahkan(t, sasaran(200), 0, "penuh"); const rng = acakBerbenih(benih); let now = 0; for (let i = 0; i < 60; i++) { now += 16; langkah(t, DT, now, "penuh", rng); } return JSON.stringify([t.a, t.b, t.sy]); };
    return k(1) === k(2);
  })());
}

console.log(gagal ? `GAGAL: ${gagal} dari ${cacah} perbandingan` : `COCOK: ${cacah} perbandingan, tetes kaca cair sesuai janji kepala modulnya`);
process.exit(gagal ? 1 : 0);
