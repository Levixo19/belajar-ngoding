/* Logika murni hero gulir-membuka (layar Pengantar). Tanpa DOM, tanpa React:
 * hanya bagian ini yang bisa diadu di Node (`uji/banding-hero.mjs`).
 *
 * Satu angka, `p` dari 0 (tertutup) sampai 1 (terbuka), menggerakkan seluruh
 * hero lewat CSS (`--hg-p`). Roda dan papan ketik hanya menggesernya; yang
 * memutuskan bahwa sebuah isyarat dimakan hero atau dibiarkan menggulir
 * halaman adalah `terapkanIsyarat`.
 *
 * Aturan yang masing-masing ada sebabnya:
 *  - Selama belum terbuka, hero memakan roda DAN tombol gulir, dua arah. Kalau
 *    ia hanya memakan roda, pengguna papan ketik tidak punya jalan membukanya.
 *  - Sesudah terbuka, halaman menggulir seperti biasa. Hero baru menutup lagi
 *    kalau halaman sudah DIAM di puncak (`JEDA_TUTUP`) dan isyaratnya naik:
 *    tanpa jeda itu, gulir berinersia yang baru sampai di puncak ikut
 *    menutupnya, tepat saat orang selesai membaca ke atas.
 *  - Tombol yang ditahan (`ulang`) tidak pernah menutup, dengan alasan yang
 *    sama.
 */

/** Jarak gulir roda, piksel, yang membuka hero seluruhnya. */
export const JARAK_RODA = 1100;
/** Sekali tekan Spasi, PageDown, atau panah bawah maju sejauh ini. */
export const LANGKAH_TOMBOL = 0.34;
/** Halaman harus diam di puncak sekian milidetik sebelum gulir naik menutup hero. */
export const JEDA_TUTUP = 350;
/** `p` di atas ini dianggap terbuka (isi muncul). Ambang, bukan 1, karena
 *  pelicinan menuju 1 hanya mendekat. */
export const AMBANG_TERBUKA = 0.999;

export type Isyarat =
  | { jenis: "roda"; delta: number }
  | { jenis: "tombol"; key: string; shift: boolean; ulang: boolean };

export interface KeadaanGulir {
  /** Kemajuan sekarang (target, bukan yang tergambar), 0..1. */
  p: number;
  /** `scrollY` dokumen. */
  gulirY: number;
  /** Milidetik sejak peristiwa `scroll` terakhir. */
  sejakGulir: number;
}

export interface Hasil {
  p: number;
  /** `true` bila isyarat dimakan hero dan `preventDefault` wajib dipanggil. */
  cegah: boolean;
}

const MAJU = new Set(["ArrowDown", "ArrowRight", "PageDown", " ", "Spacebar"]);
const MUNDUR = new Set(["ArrowUp", "ArrowLeft", "PageUp"]);

const jepit = (x: number): number => Math.min(1, Math.max(0, x));

/** Arah satu tombol: 1 maju, -1 mundur, 2 langsung buka (End), -2 langsung
 *  tutup (Home), 0 bukan milik hero. */
export function arahTombol(key: string, shift: boolean): number {
  if (key === "End") return 2;
  if (key === "Home") return -2;
  if ((key === " " || key === "Spacebar") && shift) return -1;
  if (MAJU.has(key)) return 1;
  if (MUNDUR.has(key)) return -1;
  return 0;
}

/** Roda yang dilaporkan dalam baris atau halaman diubah jadi piksel. */
export function pikselRoda(delta: number, mode: number, tinggiJendela: number): number {
  if (mode === 1) return delta * 16;
  if (mode === 2) return delta * tinggiJendela;
  return delta;
}

export function terapkanIsyarat(i: Isyarat, k: KeadaanGulir): Hasil {
  const tak = { p: k.p, cegah: false };
  const terbuka = k.p >= AMBANG_TERBUKA;
  const bolehTutup = k.gulirY <= 0 && k.sejakGulir >= JEDA_TUTUP;

  if (i.jenis === "roda") {
    if (i.delta === 0) return tak;
    if (terbuka && !(i.delta < 0 && bolehTutup)) return tak;
    return { p: jepit(k.p + i.delta / JARAK_RODA), cegah: true };
  }

  const arah = arahTombol(i.key, i.shift);
  if (arah === 0) return tak;
  if (terbuka) {
    // Terbuka: hanya tombol naik, sekali tekan, di puncak yang sudah diam.
    if (arah > 0 || i.ulang || !bolehTutup) return tak;
    return { p: arah === -2 ? 0 : jepit(k.p - LANGKAH_TOMBOL), cegah: true };
  }
  if (arah === 2) return { p: 1, cegah: true };
  if (arah === -2) return { p: 0, cegah: true };
  return { p: jepit(k.p + arah * LANGKAH_TOMBOL), cegah: true };
}

/** Sasaran pelicinan: `p` menyusul `target` sejauh `laju` per bingkai, dan
 *  berhenti tepat di target begitu selisihnya di bawah `ambang`. */
export function susul(p: number, target: number, laju = 0.18, ambang = 0.0008): number {
  const n = p + (target - p) * laju;
  return Math.abs(target - n) < ambang ? target : n;
}

/** Elemen yang memakai Spasi dan panah untuk dirinya sendiri: hero tidak boleh
 *  mencuri tombol dari mereka. */
export const PEMILIK_TOMBOL =
  'input, textarea, select, button, a[href], summary, [contenteditable=""], [contenteditable="true"], [role="combobox"], [role="listbox"], [role="textbox"], #tirai';
