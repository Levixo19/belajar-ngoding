/* Logika murni orbit bekal (panel profesi di Peta Karier). Tanpa DOM, tanpa
 * React: hanya bagian ini yang bisa diadu di Node (`uji/banding-orbit.mjs`).
 *
 * Padanan komponen `RadialOrbitalTimeline` yang ditempel pemilik, dengan
 * semua yang dikodekan diganti data sungguhan, bukan angka demo:
 *   pusat           profesi yang sedang dibuka, dengan kesiapannya
 *   cincin dalam    bekal: tiap kurikulum dari tiap kelompok bekal
 *   cincin luar     pelengkap
 *   cincin progres  persen kurikulum itu, dari `progress.statistik_bahasa`
 *                   (angka yang sama dengan halaman bahasa)
 *   "terhubung"     alternatif SETARA dalam satu kelompok bekal ("salah satu
 *                   dari Python atau JavaScript"), bukan keterkaitan karangan
 *
 * Aturan yang masing-masing ada sebabnya:
 *  - Semua alternatif sebuah kelompok jadi simpul sendiri, tetapi hanya satu
 *    (`wakil`) yang dihitung ke kesiapan. Menyembunyikan sisanya membuat
 *    orang yang justru belajar JavaScript melihat bekal itu "belum disentuh".
 *  - Pelengkap yang sudah ada di cincin dalam tidak digambar dua kali.
 *  - Sudut dasar dibagi rata di tiap cincin, dan cincin luar digeser setengah
 *    langkah supaya simpul dua cincin tidak berbaris lurus dari pusat.
 *  - Kemajuan sudut dijepit (`dtMs` paling banyak 100): tab yang baru
 *    kembali dari latar tidak boleh membuat orbit melompat.
 */

export type StatusOrbit = "selesai" | "jalan" | "belum";
export type Lingkar = "dalam" | "luar";

export interface KelompokOrbit {
  pilihan: string[];
  wakil: string;
  persen: number;
}

export type KurOrbit = Record<string, { label: string; persen: number }>;

export interface NodeOrbit {
  /** `"<lingkar>:<kunci kurikulum>"`, unik di satu orbit. */
  id: string;
  kunci: string;
  label: string;
  /** 0..100. */
  persen: number;
  status: StatusOrbit;
  lingkar: Lingkar;
  /** Derajat dasar: -90 = di puncak, bertambah searah jarum jam (arah `rotate` CSS). */
  sudut: number;
  /** Alternatif yang dihitung ke kesiapan (cincin dalam). */
  wakil: boolean;
  /** Indeks kelompok bekal, `null` untuk pelengkap. */
  kelompok: number | null;
  /** Id simpul alternatif setara dalam kelompok yang sama. */
  setara: string[];
}

/** Jari-jari tiap cincin dalam satuan `cqw` (lebar papan). Dipakai CSS juga. */
export const JARI: Record<Lingkar, number> = { dalam: 30, luar: 44 };
/** Pengali kecepatan putar tiap cincin: yang dalam lebih cepat. */
export const KECEPATAN: Record<Lingkar, number> = { dalam: 1, luar: 0.6 };
/** Derajat per detik pada pengali 1. */
export const LAJU = 6;
/** Batas selisih waktu satu bingkai, milidetik. */
export const DT_MAKS = 100;

export const STATUS_TEKS: Record<StatusOrbit, string> = {
  selesai: "selesai",
  jalan: "sedang dikerjakan",
  belum: "belum dimulai",
};

const jepit = (n: number): number => Math.min(100, Math.max(0, Number.isFinite(n) ? n : 0));

export function statusDari(persen: number): StatusOrbit {
  const p = jepit(persen);
  return p >= 100 ? "selesai" : p > 0 ? "jalan" : "belum";
}

/** Sudut dasar simpul ke-`i` dari `n` di satu cincin; `geser` dalam satuan langkah. */
export function sudutDasar(i: number, n: number, geser = 0): number {
  return n <= 0 ? -90 : -90 + ((i + geser) / n) * 360;
}

export function bangunNode(
  kelompok: KelompokOrbit[],
  pelengkap: string[],
  kur: KurOrbit,
): NodeOrbit[] {
  const dalam: Array<{ kunci: string; kelompok: number; wakil: boolean; cadangan: number }> = [];
  const lihat = new Set<string>();
  kelompok.forEach((k, gi) => {
    for (const x of k.pilihan) {
      if (lihat.has(x)) continue;
      lihat.add(x);
      dalam.push({ kunci: x, kelompok: gi, wakil: x === k.wakil, cadangan: x === k.wakil ? k.persen : 0 });
    }
  });
  const luar = pelengkap.filter((x) => {
    if (lihat.has(x)) return false;
    lihat.add(x);
    return true;
  });

  const buat = (
    kunci: string, lingkar: Lingkar, sudut: number, wakil: boolean, gi: number | null, cadangan: number,
  ): NodeOrbit => {
    const persen = jepit(kur[kunci]?.persen ?? cadangan);
    return {
      id: `${lingkar}:${kunci}`, kunci, label: kur[kunci]?.label ?? kunci, persen,
      status: statusDari(persen), lingkar, sudut, wakil, kelompok: gi, setara: [],
    };
  };
  const simpul = [
    ...dalam.map((d, i) => buat(d.kunci, "dalam", sudutDasar(i, dalam.length), d.wakil, d.kelompok, d.cadangan)),
    ...luar.map((x, j) => buat(x, "luar", sudutDasar(j, luar.length, 0.5), false, null, 0)),
  ];
  for (const n of simpul) {
    if (n.kelompok === null) continue;
    n.setara = simpul.filter((m) => m.kelompok === n.kelompok && m.id !== n.id).map((m) => m.id);
  }
  return simpul;
}

/** Sudut putar berikutnya (derajat, 0..360) sesudah `dtMs` milidetik. */
export function sudutBerikut(sudut: number, dtMs: number, laju = LAJU): number {
  const dt = Math.min(Math.max(Number.isFinite(dtMs) ? dtMs : 0, 0), DT_MAKS);
  const n = (sudut + (laju * dt) / 1000) % 360;
  return n < 0 ? n + 360 : n;
}

/** Indeks tujuan fokus untuk tombol navigasi, atau `null` bila bukan milik orbit. */
export function langkahFokus(key: string, i: number, n: number): number | null {
  if (n <= 0) return null;
  switch (key) {
    case "ArrowRight":
    case "ArrowDown":
      return (i + 1) % n;
    case "ArrowLeft":
    case "ArrowUp":
      return (i - 1 + n) % n;
    case "Home":
      return 0;
    case "End":
      return n - 1;
    default:
      return null;
  }
}

export function labelNode(n: NodeOrbit): string {
  return `${n.label}, ${n.lingkar === "dalam" ? "bekal" : "pelengkap"}, ${Math.round(n.persen)} persen, ${STATUS_TEKS[n.status]}`;
}

/** Satu kalimat untuk keadaan tanpa simpul terpilih. */
export function ringkasOrbit(simpul: NodeOrbit[]): string {
  if (simpul.length === 0) return "Profesi ini belum punya kurikulum di aplikasi ini.";
  const selesai = simpul.filter((n) => n.status === "selesai").length;
  const jalan = simpul.filter((n) => n.status === "jalan").length;
  return `${selesai} dari ${simpul.length} kurikulum di orbit sudah selesai, ${jalan} sedang dikerjakan.`;
}
