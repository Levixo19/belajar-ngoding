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

/* ------------------------------------------------- tata letak peta rasi */

/** Satu bab seperti yang dikirim `/api/bahasa`: nomor, judul, indeks materi. */
export interface BabRasi {
  nomor: number;
  judul: string;
  materi: number[];
}

/** Masukan `tataPetaRasi`. Padanan `dariBahasa()` di `rasi.js`. */
export interface DataPeta {
  key: string;
  label: string;
  materi: MateriBintang[];
  bab?: BabRasi[];
}

/**
 * Satu anak sebuah rasi, dalam URUTAN GAMBAR.
 *
 * Urutannya bagian dari kontrak, bukan kebetulan: versi JS menempelkan garis
 * ke-j SEBELUM bintang ke-j, jadi garisnya tergambar di atas bintang
 * sebelumnya dan di bawah bintang sesudahnya. Mengurutkan ulang jadi "semua
 * garis dulu, lalu semua bintang" tidak menimbulkan error dan hampir tidak
 * terlihat -- tapi `--i` (penunda animasi per anak) ikut bergeser, dan
 * koreografi garis-tergambar yang tadinya mengalir dari bintang pertama ke
 * terakhir berubah jadi dua gelombang.
 */
export type ItemPeta =
  | {
      jenis: "garis";
      a: Titik;
      b: Titik;
      ra: number;
      rb: number;
      terang: boolean;
      urut: number;
    }
  | { jenis: "bintang"; indeks: number; x: number; y: number; r: number; urut: number };

/** Label satu bab di tepi petanya. */
export interface LabelPeta {
  x: number;
  y: number;
  jangkar: "start" | "middle" | "end";
  /** Angka Romawi plus DUA spasi, persis seperti versi JS-nya. */
  nomor: string;
  judul: string;
}

/** Jalur putus-putus antara bintang terakhir sebuah bab dan bintang pertama
 *  bab berikutnya. */
export interface JalurPeta {
  a: Titik;
  b: Titik;
  ra: number;
  rb: number;
}

export interface TataPeta {
  W: number;
  H: number;
  kelompok: ItemPeta[][];
  label: LabelPeta[];
  jalur: JalurPeta[];
  reticle: { x: number; y: number; r: number } | null;
  ringkasan: string;
}

/**
 * Tata letak peta rasi satu kurikulum. Port bagian murni `petaRasi()`.
 *
 * Satu bab = satu rasi, diletakkan berderet dari kiri ke kanan dengan pusat
 * yang naik-turun mengikuti sinus berbenih `hash(key)`. Benih itulah yang
 * membuat peta Python selalu berbentuk sama, dan kenapa fungsi ini diadu
 * dengan `rasi.js` alih-alih dipercaya: satu bit yang meleset menggeser
 * SELURUH peta tanpa satu pun error.
 *
 * Bahasa tanpa pembagian bab tetap dapat petanya -- satu rasi berisi semua
 * materinya, dilabeli nama bahasanya. Itu jalur cadangan yang sengaja ada,
 * sama dengan jalur cadangan `data/bab.py`.
 */
export function tataPetaRasi(data: DataPeta, tinggi = 250): TataPeta {
  const W = 1000;
  const H = tinggi;
  const bab: BabRasi[] =
    data.bab && data.bab.length
      ? data.bab
      : [{ nomor: 1, judul: data.label, materi: data.materi.map((_m, i) => i) }];
  const berikut = berikutDari(data.materi);
  const lebarRasi = W / bab.length;
  // Label bergantian atas-bawah, jadi tiap label boleh selebar DUA rasi.
  const batasLabel = Math.max(10, Math.min(30, Math.floor((lebarRasi * 2) / 6.8)));

  const posisi: Array<{ p: Titik; r: number } | undefined> = [];
  const pasangan: Array<[number, number]> = [];
  const kelompok: ItemPeta[][] = [];
  const label: LabelPeta[] = [];
  let urutan = 0;

  bab.forEach((b, i) => {
    const cx = (i + 0.5) * lebarRasi;
    const cy = H * 0.46 + Math.sin(i * 1.7 + (hash(data.key) % 7)) * H * 0.13;
    const kotakW = Math.min(lebarRasi * 0.74, 150);
    const kotakH = H * 0.42;
    const titik = bentukRasi(
      b.materi.length,
      data.key + "·" + b.judul,
      kotakW,
      kotakH,
    ).map(([x, y]) => [cx + x, cy + y] as Titik);

    const isi: ItemPeta[] = [];
    b.materi.forEach((idx, j) => {
      const m = data.materi[idx];
      if (!m) return;
      const p = titik[j] as Titik;
      const r = jariBintang(magStatus(m), 0.9);
      posisi[idx] = { p, r };
      const sebelum = j > 0 ? posisi[b.materi[j - 1] as number] : undefined;
      if (sebelum) {
        const kiri = data.materi[b.materi[j - 1] as number] as MateriBintang;
        // Garis yang terlalu pendek DIBUANG, dan `urut` tidak ikut terpakai --
        // itu yang dilakukan `ruas()` yang mengembalikan null di versi JS.
        if (ruasAntara(sebelum.p, p, sebelum.r, r)) {
          isi.push({
            jenis: "garis",
            a: sebelum.p,
            b: p,
            ra: sebelum.r,
            rb: r,
            terang: kiri.status === "selesai" && m.status === "selesai",
            urut: urutan,
          });
        }
      }
      isi.push({ jenis: "bintang", indeks: idx, x: p[0], y: p[1], r, urut: urutan++ });
    });
    kelompok.push(isi);

    const bawah = i % 2 === 0;
    // Label di ujung kiri/kanan dijangkarkan ke dalam supaya tidak terpotong.
    const jangkar: LabelPeta["jangkar"] =
      bab.length > 2 && i === 0
        ? "start"
        : bab.length > 2 && i === bab.length - 1
          ? "end"
          : "middle";
    label.push({
      x: jangkar === "start" ? 6 : jangkar === "end" ? W - 6 : cx,
      y: bawah ? cy + kotakH / 2 + 24 : cy - kotakH / 2 - 14,
      jangkar,
      nomor: (ROMAWI[b.nomor] || String(b.nomor)) + "  ",
      judul:
        b.judul.length > batasLabel
          ? b.judul.slice(0, batasLabel - 1) + "…"
          : b.judul,
    });

    const lanjut = bab[i + 1];
    if (lanjut && b.materi.length && lanjut.materi.length) {
      pasangan.push([
        b.materi[b.materi.length - 1] as number,
        lanjut.materi[0] as number,
      ]);
    }
  });

  const jalur: JalurPeta[] = [];
  for (const [a, b] of pasangan) {
    const pa = posisi[a];
    const pb = posisi[b];
    if (!pa || !pb) continue;
    if (!ruasAntara(pa.p, pb.p, pa.r, pb.r)) continue;
    jalur.push({ a: pa.p, b: pb.p, ra: pa.r, rb: pb.r });
  }

  const sasaran = berikut !== null ? posisi[berikut] : undefined;
  const selesai = data.materi.filter((m) => m.status === "selesai").length;

  return {
    W,
    H,
    kelompok,
    label,
    jalur,
    reticle: sasaran ? { x: sasaran.p[0], y: sasaran.p[1], r: sasaran.r } : null,
    ringkasan:
      `Peta langit ${data.label}: ${selesai} dari ${data.materi.length} ` +
      "bintang menyala." +
      (berikut !== null
        ? ` Berikutnya: ${(data.materi[berikut] as MateriBintang).judul}.`
        : ""),
  };
}

/** `/api/bahasa` -> masukan `tataPetaRasi`. Port `dariBahasa()`. */
export function dariBahasa(b: {
  key: string;
  label: string;
  materi: Array<{ judul: string; status: string; terkunci?: boolean }>;
  bab?: Array<{ nomor: number; judul: string; materi: number[] }>;
}): DataPeta {
  return {
    key: b.key,
    label: b.label,
    materi: b.materi.map((m) => ({
      judul: m.judul,
      status: m.status,
      terkunci: m.terkunci,
    })),
    bab: (b.bab || []).map((x) => ({
      nomor: x.nomor,
      judul: x.judul,
      materi: x.materi,
    })),
  };
}
