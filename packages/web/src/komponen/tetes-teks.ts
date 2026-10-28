/* Fisika "tetes air" untuk kaca cair di bilah atas. BAGIAN MURNI: tidak ada
 * DOM, tidak ada WebGL, tidak ada `Math.random()` telanjang. Pembangkit angka
 * acak masuk lewat parameter, jadi satu benih memberi satu riwayat gerak yang
 * sama persis, dan pembanding Node bisa mengadunya.
 *
 * Gagasan mekanismenya dari komponen "Liquid Glass Navbar" milik Guglielmo
 * Giannattasio (@gughigug, 21st.dev, lisensi MIT). Yang dipakai dari sana
 * hanya CARA KERJANYA, dibaca dari kodenya: dua ujung tetes pada pegas
 * berbeda sehingga tetes MERENGGANG, tetes pecah jadi satelit kalau
 * rentangnya melewati ambang, dan riak keluar saat semuanya diam. Selebihnya
 * ditulis ulang di sini: nama, tingkat gerak, batas, dan pembagian murni dan
 * komponen. Teks izin MIT ada di `TetesKaca.tsx`.
 *
 * Semua koordinat dalam piksel, terhadap TEPI KIRI-ATAS bilah (kotak berbatas
 * penuh), BUKAN terhadap kanvas. Kanvas lebih besar `TEPI` di tiap sisi;
 * selisih itu ditambahkan satu kali, di `bacaUniform`, supaya tidak ada
 * rumus lain yang perlu ingat ada dua sistem koordinat.
 *
 * Tiga tingkat gerak (`tingkatGerak()` yang memutuskan, bukan modul ini):
 *  - penuh: pegas, merenggang, pecah jadi satelit, riak, gelombang kursor.
 *  - halus: meluncur cepat tanpa pantulan, tanpa satelit, riak, atau kursor.
 *    Yang padam hanya yang bergerak SENDIRI; berpindah butir karena diklik
 *    tetap dijawab.
 *  - mati: langsung berdiri di tempat baru.
 */

export type Mode = "penuh" | "halus" | "mati";

/** Lebar tepi kanvas di luar bilah, dalam piksel. Cukup untuk anti-alias tepi
 *  bilah; tetes dan satelit dijepit di dalam bilah, jadi tidak perlu lebih. */
export const TEPI = 2;
/** Berapa banyak riak yang dipertahankan, dan berapa lama satu riak hidup. */
export const MAKS_RIAK = 6;
export const UMUR_RIAK = 2.4;
/** Tetes utama (dua ujung) + satelit. Shader membaca enam kapsul. */
export const MAKS_KAPSUL = 6;
export const MAKS_SATELIT = MAKS_KAPSUL - 2;
/** Jeda ujung penyusul dan kelambanannya selama jeda itu. */
export const TUNDA_MS = 70;
export const FAKTOR_TUNDA = 0.08;
/** Jarak aman dinding bilah (piksel) yang dijaga ujung tetes. */
export const TEMBOK = 6;
/** Ambang pecah: celah antara dua ujung sesudah dikurangi panjang kapsulnya. */
export const AMBANG_PECAH = -6;

const PEGAS_PEMIMPIN = { k: 210, c: 25 } as const;
const PEGAS_PENYUSUL = { k: 72, c: 13 } as const;
/** Teredam kritis (c = 2 sqrt k): tanpa pantulan, untuk tingkat halus. */
const PEGAS_HALUS = { k: 210, c: 2 * Math.sqrt(210) } as const;

export interface Sasaran {
  /** Pusat butir (x), pusat vertikal (cy), setengah panjang batang (q),
   *  jari-jari ujung (r). Lebar butir = 2 (q + r), tingginya 2 r. */
  x: number;
  cy: number;
  q: number;
  r: number;
}
export interface Ujung { x: number; v: number }
export interface Satelit { x: number; y: number; vx: number; vy: number; r: number; k: number }
export interface Riak { x: number; y: number; umur: number; amp: number }
export interface Kursor { x: number; y: number; s: number; nyala: boolean }

export interface Tetes {
  a: Ujung;
  b: Ujung;
  /** Peregangan vertikal (1 = bulat). Pegas sendiri, mengikuti ujung pemimpin. */
  sy: { s: number; v: number };
  pemimpin: 0 | 1;
  tertinggalSampai: number;
  satelit: Satelit[];
  riak: Riak[];
  sasaran: Sasaran;
  /** Setengah panjang batang yang dihaluskan menuju `sasaran.q`. */
  q: number;
  bergerak: boolean;
  pecah: boolean;
  /** Sudah pernah diberi tempat berdiri. */
  siap: boolean;
  /** Ada butir yang sedang ditandai. Tanpa itu tetes mengecil dan hilang. */
  hadir: boolean;
  /** 0 sampai 1, mengikuti `hadir`. Mengalikan jari-jari kapsul. */
  muncul: number;
  lebar: number;
  tinggi: number;
  waktu: number;
  kursor: Kursor;
}

export function buatTetes(): Tetes {
  return {
    a: { x: 0, v: 0 },
    b: { x: 0, v: 0 },
    sy: { s: 1, v: 0 },
    pemimpin: 0,
    tertinggalSampai: 0,
    satelit: [],
    riak: [],
    sasaran: { x: 0, cy: 0, q: 0, r: 0 },
    q: 0,
    bergerak: false,
    pecah: false,
    siap: false,
    hadir: false,
    muncul: 0,
    lebar: 0,
    tinggi: 0,
    waktu: 0,
    kursor: { x: 0, y: 0, s: 0, nyala: false },
  };
}

export interface Kotak { kiri: number; atas: number; lebar: number; tinggi: number }

/** Tetes menutupi PERSIS kotak butirnya: tingginya tinggi butir, lebarnya
 *  lebar butir. Kapsul = batang setengah panjang `q` berujung bulat `r`. */
export function sasaranDariKotak(k: Kotak): Sasaran {
  const r = k.tinggi / 2;
  return {
    x: k.kiri + k.lebar / 2,
    cy: k.atas + k.tinggi / 2,
    q: Math.max(0, k.lebar / 2 - r),
    r,
  };
}

export function ukuranBilah(t: Tetes, lebar: number, tinggi: number): void {
  t.lebar = lebar;
  t.tinggi = tinggi;
}

function berdiri(t: Tetes, s: Sasaran): void {
  t.a.x = t.b.x = s.x;
  t.a.v = t.b.v = 0;
  t.sy.s = 1;
  t.sy.v = 0;
  t.satelit = [];
  t.bergerak = false;
  t.pecah = false;
}

/** Berdiri di tempat baru TANPA gerak: ukuran bilah berubah (huruf selesai
 *  dimuat, jendela diubah), jadi jarak lama tidak berarti lagi. `null` =
 *  tidak ada butir yang ditandai. */
export function pindahLangsung(t: Tetes, s: Sasaran | null): void {
  if (s === null) {
    t.hadir = false;
    return;
  }
  t.sasaran = s;
  t.q = s.q;
  t.siap = true;
  t.hadir = true;
  berdiri(t, s);
}

/** Butir yang ditandai berganti. Tetes berangkat dari tempatnya sekarang,
 *  kecuali ia belum pernah berdiri atau sedang tersembunyi: yang baru muncul
 *  tidak terbang dari tempat yang sudah tidak ada. */
export function arahkan(t: Tetes, s: Sasaran | null, sekarangMs: number, mode: Mode): void {
  if (s === null) {
    t.hadir = false;
    return;
  }
  const lama = t.sasaran;
  const sudahBerdiri = t.hadir && t.siap;
  if (!sudahBerdiri || mode === "mati") {
    pindahLangsung(t, s);
    if (mode === "mati") t.muncul = 1;
    return;
  }
  t.sasaran = s;
  if (Math.abs(s.x - lama.x) > 0.5) {
    // Ujung yang lebih dekat ke tujuan memimpin; yang satunya tertinggal.
    t.pemimpin = Math.abs(s.x - t.a.x) <= Math.abs(s.x - t.b.x) ? 0 : 1;
    t.tertinggalSampai = sekarangMs + TUNDA_MS;
    t.bergerak = true;
    t.pecah = false;
  }
}

/** Tetes yang baru pertama kali berdiri langsung tampak penuh. Tanpa ini ia
 *  tumbuh dari titik selama sepertiga detik, padahal penanda lama di butir itu
 *  sudah dimatikan: butir aktif berkedip tanpa penanda sama sekali. */
export function tampilSeketika(t: Tetes): void {
  t.muncul = t.hadir ? 1 : 0;
}

export function tambahRiak(t: Tetes, x: number, y: number, amp: number): void {
  t.riak.push({ x, y, umur: 0, amp });
  while (t.riak.length > MAKS_RIAK) t.riak.shift();
}

/** Penunjuk mouse di atas bilah (koordinat bilah). `null` = pergi. */
export function tunjuk(t: Tetes, x: number | null, y = 0): void {
  if (x === null) {
    t.kursor.nyala = false;
    return;
  }
  t.kursor.x = x;
  t.kursor.y = y;
  t.kursor.nyala = true;
}

/** Celah antara dua ujung sesudah panjang kapsul keduanya dikurangkan. Nilai
 *  mendekati nol artinya kapsul nyaris terlepas; lewat `AMBANG_PECAH`, jembatan
 *  di antaranya putus. */
export function celah(t: Tetes): number {
  const s = t.sasaran;
  const jarak = Math.abs(t.a.x - t.b.x);
  const z = Math.min(jarak / (2 * (s.q + s.r) || 1), 1);
  const jariAkhir = s.r * (1 - 0.3 * z);
  return jarak - 2 * s.q - 2 * jariAkhir;
}

function pegasUjung(
  u: Ujung, tujuan: number, k: number, c: number, faktor: number, dt: number,
): void {
  u.v += (k * (tujuan - u.x) - c * u.v) * dt * faktor;
  u.x += u.v * dt;
}

/** Satu langkah waktu `dtMentah` detik. `sekarangMs` dari jam yang sama dengan
 *  `arahkan` (menentukan kapan jeda ujung penyusul habis).
 *
 *  Waktu TIDAK PERNAH mundur: `dt` negatif dianggap nol. Ini bukan kehati-hatian
 *  berlebihan. Cap waktu `requestAnimationFrame` adalah AWAL bingkai, dan bisa
 *  lebih awal daripada `performance.now()` yang dicatat saat bingkai diminta;
 *  bingkai pertama sesudah diam karena itu bisa berdurasi negatif. Untuk gelombang
 *  kursor itu membuat `kursor.s` negatif, `perluBingkai` salah, dan putaran
 *  berhenti sesudah dua bingkai padahal penunjuk masih di atas bilah. Ditemukan
 *  di peramban, bukan di pembanding: semua `dt` di pembanding positif. */
export function langkah(
  t: Tetes, dtMentah: number, sekarangMs: number, mode: Mode, rng: () => number,
): void {
  const dt = dtMentah > 0 ? dtMentah : 0;
  t.waktu += dt;
  const s = t.sasaran;
  const tujuanMuncul = t.hadir ? 1 : 0;
  if (mode === "mati") {
    t.muncul = tujuanMuncul;
    t.q = s.q;
  } else {
    t.muncul += (tujuanMuncul - t.muncul) * Math.min(1, dt * 10);
    if (Math.abs(t.muncul - tujuanMuncul) < 0.01) t.muncul = tujuanMuncul;
    t.q += (s.q - t.q) * Math.min(1, dt * 12);
  }

  // Kursor hanya hidup di tingkat penuh; di tingkat lain ia luruh ke nol.
  const mauKursor = mode === "penuh" && t.kursor.nyala ? 1 : 0;
  t.kursor.s += (mauKursor - t.kursor.s) * Math.min(1, dt * 7);

  if (mode === "mati") {
    berdiri(t, s);
    t.riak = [];
    return;
  }

  if (mode === "halus") {
    pegasUjung(t.a, s.x, PEGAS_HALUS.k, PEGAS_HALUS.c, 1, dt);
    pegasUjung(t.b, s.x, PEGAS_HALUS.k, PEGAS_HALUS.c, 1, dt);
    t.sy.s = 1;
    t.sy.v = 0;
    t.satelit = [];
    t.riak = [];
    const diam = Math.abs(s.x - t.a.x) <= 0.3 && Math.abs(s.x - t.b.x) <= 0.3
      && Math.abs(t.a.v) <= 3 && Math.abs(t.b.v) <= 3;
    if (t.bergerak && diam) berdiri(t, s);
    return;
  }

  // ---- penuh
  let diam = true;
  const ujung = [t.a, t.b];
  ujung.forEach((u, i) => {
    const memimpin = i === t.pemimpin;
    const peg = memimpin ? PEGAS_PEMIMPIN : PEGAS_PENYUSUL;
    const faktor = !memimpin && sekarangMs < t.tertinggalSampai ? FAKTOR_TUNDA : 1;
    pegasUjung(u, s.x, peg.k, peg.c, faktor, dt);
    const kiri = TEMBOK + t.q + s.r - 3;
    const kanan = t.lebar - TEMBOK - t.q - s.r + 3;
    if (u.x < kiri || u.x > kanan) {
      // Menabrak dinding: tetes gepeng sedikit lalu memantul lemah.
      t.sy.v -= Math.min(Math.abs(u.v), 900) * 0.0016;
      u.x = Math.max(kiri, Math.min(kanan, u.x));
      u.v *= -0.25;
    }
    if (Math.abs(s.x - u.x) > 0.3 || Math.abs(u.v) > 3) diam = false;
  });

  const pemimpin = ujung[t.pemimpin]!;
  const sasaranSy = 1 - 0.2 * Math.min(Math.abs(pemimpin.v) / 1500, 1);
  t.sy.v += (280 * (sasaranSy - t.sy.s) - 9 * t.sy.v) * dt;
  t.sy.s += t.sy.v * dt;
  if (Math.abs(t.sy.s - 1) > 0.002 || Math.abs(t.sy.v) > 0.02) diam = false;

  if (!t.pecah && t.bergerak && celah(t) > AMBANG_PECAH) {
    t.pecah = true;
    const tertinggal = ujung[1 - t.pemimpin]!;
    [0.3, 0.5, 0.72].forEach((f, i) => {
      t.satelit.push({
        x: tertinggal.x + (pemimpin.x - tertinggal.x) * f + (rng() - 0.5) * 6,
        y: s.cy + (rng() - 0.5) * 10,
        vx: (tertinggal.v + pemimpin.v) * 0.45,
        vy: (rng() - 0.5) * 60,
        r: 5 + rng() * 3 - i * 0.5,
        k: 70 + rng() * 90,
      });
    });
  }

  t.satelit = t.satelit.filter((m) => {
    m.vx += (m.k * (s.x - m.x) - 9 * m.vx) * dt;
    m.vy += (90 * (s.cy - m.y) - 7 * m.vy) * dt;
    m.x += m.vx * dt;
    m.y += m.vy * dt;
    m.x = Math.max(8 + m.r, Math.min(t.lebar - 8 - m.r, m.x));
    m.y = Math.max(s.cy - s.r + m.r, Math.min(s.cy + s.r - m.r, m.y));
    // Satelit yang sudah mendarat di tetes induk larut ke dalamnya.
    if (Math.abs(s.x - m.x) < t.q + s.r * 0.5) m.r -= dt * 26;
    return m.r > 0.6;
  });
  if (t.satelit.length > 0) diam = false;

  if (t.bergerak && diam) {
    const pecah = t.pecah;
    berdiri(t, s);
    tambahRiak(t, s.x, s.cy, pecah ? 1.2 : 0.7);
  }

  t.riak.forEach((m) => { m.umur += dt; });
  t.riak = t.riak.filter((m) => m.umur < UMUR_RIAK);
}

/** Perlukah bingkai berikutnya digambar. Tetap benar selama ada yang masih
 *  bergerak, dan berhenti begitu semuanya diam: kanvas menahan bingkai
 *  terakhirnya sendiri, jadi tetes yang diam tidak memakan satu bingkai pun.
 *
 *  Kursor dibaca dari `nyala` (di tingkat penuh), BUKAN hanya dari `kursor.s`:
 *  `s` hasil integrasi, dan bingkai pertama bisa berdurasi nol sehingga `s`
 *  masih nol padahal penunjuk jelas di atas bilah; putarannya dinyatakan
 *  selesai sebelum gelombang sempat naik. Di tingkat lain `nyala` tidak
 *  menahan apa pun (ia bisa tertinggal bila tingkat gerak diganti saat
 *  menunjuk), dan yang tersisa hanya `s` yang luruh. */
export function perluBingkai(t: Tetes, mode: Mode = "penuh"): boolean {
  return t.bergerak
    || t.satelit.length > 0
    || t.riak.length > 0
    || t.kursor.s > 0.01
    || (mode === "penuh" && t.kursor.nyala)
    || t.muncul !== (t.hadir ? 1 : 0);
}

export interface Uniform {
  /** 6 kapsul x (x, y, setengah panjang, jari-jari). Jari-jari 0 = tidak ada. */
  kapsul: Float32Array;
  sy: Float32Array;
  /** 6 riak x (x, y, umur, amplitudo). */
  riak: Float32Array;
  kursor: [number, number, number];
}

/** Susun data untuk shader: dua kapsul utama (pemimpin dulu), satelit, lalu
 *  nol. Koordinat bilah digeser `TEPI` jadi koordinat kanvas di SINI. */
export function bacaUniform(t: Tetes): Uniform {
  const s = t.sasaran;
  const jarak = Math.abs(t.a.x - t.b.x);
  const z = Math.min(jarak / (2 * (t.q + s.r) || 1), 1);
  const pemimpin = t.pemimpin === 0 ? t.a : t.b;
  const tertinggal = t.pemimpin === 0 ? t.b : t.a;
  const kapsul = new Float32Array(MAKS_KAPSUL * 4);
  const sy = new Float32Array(MAKS_KAPSUL).fill(1);
  const m = t.muncul;
  kapsul.set([
    pemimpin.x + TEPI, s.cy + TEPI, t.q * (1 - 0.25 * z) * m, s.r * (1 - 0.12 * z) * m,
    tertinggal.x + TEPI, s.cy + TEPI, t.q * (1 - 0.8 * z) * m, s.r * (1 - 0.5 * z) * m,
  ], 0);
  sy[0] = sy[1] = t.sy.s;
  t.satelit.slice(0, MAKS_SATELIT).forEach((p, i) => {
    kapsul.set([p.x + TEPI, p.y + TEPI, 0, p.r], 8 + i * 4);
  });
  const riak = new Float32Array(MAKS_RIAK * 4);
  t.riak.slice(-MAKS_RIAK).forEach((p, i) => {
    riak.set([p.x + TEPI, p.y + TEPI, p.umur, p.amp], i * 4);
  });
  return { kapsul, sy, riak, kursor: [t.kursor.x + TEPI, t.kursor.y + TEPI, t.kursor.s] };
}

export interface GayaCadangan {
  lebar: number;
  geser: number;
  skalaY: number;
  atas: number;
  tinggi: number;
  tampak: boolean;
}

/** Tetes cadangan tanpa WebGL: satu kapsul CSS dari ujung ke ujung. Tidak ada
 *  satelit dan riak di sini; yang dijaga cuma gerak rentang dan tempatnya. */
export function gayaCadangan(t: Tetes): GayaCadangan {
  const s = t.sasaran;
  const jarak = Math.abs(t.a.x - t.b.x);
  const z = Math.min(jarak / (2 * (t.q + s.r) || 1), 1);
  const w = s.r * (1 - 0.3 * z);
  return {
    lebar: jarak + 2 * (t.q + w),
    geser: Math.min(t.a.x, t.b.x) - t.q - w,
    skalaY: t.sy.s,
    atas: s.cy - s.r,
    tinggi: 2 * s.r,
    tampak: t.muncul > 0.02,
  };
}

/** Pembiasan latar (`backdrop-filter: url(#...)`) hanya jalan di Chromium. Di
 *  Firefox dan Safari deklarasinya membuat SELURUH `backdrop-filter` gugur,
 *  jadi kacanya tidak buram sama sekali; karena itu ditanya dua kali: ke
 *  nama peramban, lalu ke CSS sendiri. */
export function dukungBias(userAgent: string, cssBisa: boolean): boolean {
  return /Chrome\/|Chromium\/|Edg\//.test(userAgent) && !/Firefox\//.test(userAgent) && cssBisa;
}

/** Kaca cair mati di tema kontras tinggi: latar tembus pandang dan sorot putih
 *  justru yang dihindari orang yang memilih tema itu. Kembali ke bilah padat
 *  dan penanda butir lama. */
export function kacaAktif(tema: string | undefined): boolean {
  return tema !== "kontras";
}

/** Tetes lebih tua (gelap) lawan lebih muda (terang): dua palet shader. */
export function nilaiGelap(tema: string | undefined): 0 | 1 {
  return tema === "terang" ? 0 : 1;
}

/** Pembangkit acak berbenih (mulberry32) untuk uji dan pembanding. */
export function acakBerbenih(benih: number): () => number {
  let a = benih >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
