/* Bagian murni panel "Lihat jalannya": token per baris, dan kalimat langkah.
 *
 * Port bagian non-DOM `webapp/statik/js/jejak.js`. Bentuk datanya dari
 * `inti/jejak.py` lewat `POST /api/jejak`; tipe di bawah mendokumentasikan
 * jawaban itu, bukan memvalidasinya.
 *
 * `tokenPerBaris` punya kontrak yang keras dan satu arah: menyambung kembali
 * teks tiap barisnya dengan "\n" WAJIB menghasilkan kode aslinya. Panel ini
 * menomori barisnya sendiri lalu menyorot baris yang akan dijalankan dari
 * nomor yang dikirim pelacak Python -- jadi satu baris yang hilang atau satu
 * baris tambahan membuat sorotnya menunjuk baris yang salah di SELURUH sisa
 * rekaman, dan yang dipelajari orang jadi urutan eksekusi yang tidak pernah
 * terjadi. Pagarnya `uji/banding-jejak.mjs`.
 */

/** Token dari server: `[jenis, teks]`. */
export type Token = [string, string];

export interface NilaiJejak { r: string; t: string; id?: number }
export interface Bingkai {
  nama: string;
  baris: number;
  isi: Record<string, NilaiJejak>;
}
export interface Langkah {
  baris: number;
  /** `"baris"` | `"panggil"` | `"kembali"` | `"galat"` */
  p: string;
  tumpukan: Bingkai[];
  /** Panjang keluaran sejauh langkah ini, dalam karakter. */
  keluar: number;
  nilai?: NilaiJejak | null;
  galat?: string;
}
export interface Rekaman {
  langkah: Langkah[];
  keluaran: string;
  galat?: string | null;
  baris_galat?: number | null;
  terpotong?: boolean;
  timeout?: boolean;
}

/** Token server dipecah per baris. Baris kosong jadi larik kosong. */
export function tokenPerBaris(token: Token[] | null | undefined): Token[][] {
  const baris: Token[][] = [[]];
  for (const [jenis, teks] of token || []) {
    String(teks).split("\n").forEach((p, i) => {
      if (i > 0) baris.push([]);
      if (p) (baris[baris.length - 1] as Token[]).push([jenis, p]);
    });
  }
  return baris;
}

/** Kalimat yang menerangkan satu langkah, dalam bahasa manusia. */
export function kalimat(l: Langkah, adaBerikut: boolean): string {
  const atas = l.tumpukan[l.tumpukan.length - 1] || { nama: "", isi: {} };
  if (l.p === "panggil") {
    const arg = Object.entries(atas.isi).map(([k, v]) => `${k}=${v.r}`).join(", ");
    return `Masuk ke fungsi ${atas.nama}(${arg}).`;
  }
  if (l.p === "kembali") {
    return `${atas.nama} selesai dan mengembalikan ${l.nilai ? l.nilai.r : "None"}.`;
  }
  if (l.p === "galat") return `Galat di baris ${l.baris}: ${l.galat}.`;
  return `Baris ${l.baris} akan dijalankan.`
    + (adaBerikut ? "" : " Ini langkah terakhir yang tercatat.");
}
