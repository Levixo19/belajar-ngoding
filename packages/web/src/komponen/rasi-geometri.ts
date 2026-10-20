/* Geometri peta rasi. Port bagian MURNI dari `webapp/statik/js/rasi.js`.
 *
 * Dipisahkan dari penggambarnya karena satu alasan yang bisa diukur: bentuk
 * tiap rasi DETERMINISTIK dari benihnya (nama kurikulum). Kalau `hash` atau
 * `prng` di sini meleset satu bit dari versi JS-nya, SETIAP rasi berubah
 * bentuk -- dan tidak ada error di mana pun, cuma peta langit yang tidak lagi
 * sama dengan yang dilihat pelajar kemarin.
 *
 * Karena murni, keduanya bisa diadu langsung: `uji/banding-rasi.mjs`
 * menjalankan versi JS dan versi TS atas benih yang sama lalu menuntut
 * titiknya identik. Itu pagar yang sama gunanya dengan rekaman golden untuk
 * `sorot`, dengan ongkos jauh lebih kecil karena tidak ada sisi Python.
 */

/** Angka Romawi untuk nomor bab. Indeks 0 sengaja kosong. */
export const ROMAWI = [
  "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI",
  "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
];

/** Magnitudo per status. Makin kecil, makin terang. */
const MAG: Record<string, number> = { selesai: 1, sebagian: 3, baru: 5 };

export const KATA_STATUS: Record<string, string> = {
  selesai: "sudah dibaca",
  sebagian: "dibaca sebagian",
  baru: "belum dibaca",
};

/** Materi sebagai bintang. Bentuknya datang dari `/api/langit`. */
export interface MateriBintang {
  judul: string;
  status: string;
  terkunci?: boolean;
}

/**
 * FNV-1a 32-bit. `Math.imul` WAJIB, bukan `*`.
 *
 * Perkalian biasa di JavaScript memakai float 64-bit, jadi hasil di atas
 * 2^53 kehilangan presisi dan hash-nya berbeda dari yang dimaksud. `Math.imul`
 * mengalikan sebagai int32 persis seperti implementasi acuannya.
 */
export function hash(teks: string): number {
  let x = 2166136261;
  for (const c of String(teks)) {
    x = Math.imul(x ^ (c.codePointAt(0) ?? 0), 16777619);
  }
  return x >>> 0;
}

/** PRNG mulberry32. Deterministik dari benihnya. */
function prng(benih: number): () => number {
  let b = benih;
  return () => {
    b |= 0;
    b = (b + 0x6d2b79f5) | 0;
    let t = Math.imul(b ^ (b >>> 15), 1 | b);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** Jari-jari bintang dari magnitudonya. Rumus ukuran ala d3-celestial. */
export const jariBintang = (mag: number, skala = 1): number =>
  Math.max(1.1, 7 * Math.exp(-0.28 * (mag + 2)) * skala);

/** Magnitudo sebuah materi. Yang terkunci paling redup. */
export const magStatus = (m: MateriBintang): number =>
  m.terkunci ? 6 : (MAG[m.status] ?? 5);

export type Titik = [number, number];

/** Titik-titik sebuah rasi berisi `n` bintang, dinormalkan ke kotak w x h. */
export function bentukRasi(
  n: number,
  benih: string,
  w: number,
  h: number,
): Titik[] {
  if (n <= 1) return [[0, 0]];
  const acak = prng(hash(benih));
  const titik: Titik[] = [[0, 0]];
  let sudut = acak() * Math.PI * 2;
  for (let i = 1; i < n; i++) {
    // Belokan tajam dan langkah tak seragam: rasi sungguhan bukan garis
    // berkelok rata, ia gugus yang jaraknya berselang-seling.
    sudut += (acak() - 0.5) * 2.7;
    const langkah = 0.45 + acak() * 1.05;
    const [x, y] = titik[i - 1] as Titik;
    titik.push([x + Math.cos(sudut) * langkah, y + Math.sin(sudut) * langkah]);
  }
  const xs = titik.map((p) => p[0]);
  const ys = titik.map((p) => p[1]);
  const x0 = Math.min(...xs);
  const x1 = Math.max(...xs);
  const y0 = Math.min(...ys);
  const y1 = Math.max(...ys);
  const skala = Math.min(
    w / Math.max(0.001, x1 - x0),
    h / Math.max(0.001, y1 - y0),
  );
  const cx = (x0 + x1) / 2;
  const cy = (y0 + y1) / 2;
  return titik.map(([x, y]) => [(x - cx) * skala, (y - cy) * skala] as Titik);
}

/** Indeks materi berikutnya yang layak dikerjakan. `null` kalau tidak ada. */
export function berikutDari(materi: MateriBintang[]): number | null {
  const i = materi.findIndex((m) => m.status !== "selesai" && !m.terkunci);
  return i < 0 ? null : i;
}

/** Kelas CSS titik bintang untuk sebuah materi. */
export function kelasBintang(m: MateriBintang): string {
  if (m.terkunci) return "rasi-terkunci";
  return "rasi-" + (MAG[m.status] ? m.status : "baru");
}

/** Label pembaca layar sebuah bintang. */
export function labelBintang(m: MateriBintang): string {
  const keadaan = m.terkunci ? "masih terkunci" : (KATA_STATUS[m.status] ?? "");
  return `${m.judul}, ${keadaan}`;
}

/**
 * Ujung-ujung garis antara dua bintang, berhenti sebelum menyentuh keduanya.
 *
 * `null` kalau keduanya terlalu dekat: garis yang lebih pendek daripada kedua
 * jari-jarinya akan tergambar sebagai coretan di dalam bintangnya sendiri.
 */
export function ruasAntara(
  a: Titik,
  b: Titik,
  ra: number,
  rb: number,
): { x1: number; y1: number; x2: number; y2: number } | null {
  const dx = b[0] - a[0];
  const dy = b[1] - a[1];
  const d = Math.hypot(dx, dy);
  if (d < ra + rb + 4) return null;
  const ux = dx / d;
  const uy = dy / d;
  return {
    x1: a[0] + ux * (ra + 3),
    y1: a[1] + uy * (ra + 3),
    x2: b[0] - ux * (rb + 3),
    y2: b[1] - uy * (rb + 3),
  };
}
