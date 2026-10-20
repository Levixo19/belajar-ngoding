/* Pembantu kecil yang dipakai beberapa layar. Padanan sebagian `inti.js`.
 *
 * Yang masuk ke sini cuma yang sudah dipakai LEBIH DARI SATU layar, atau yang
 * memuat sebuah aturan. `inti.js` 803 baris sebagian karena ia jadi tempat
 * singgah apa pun yang belum punya rumah; folder ini tidak perlu mengulanginya.
 */

import type { ReactNode } from "react";

/** Angka dengan pemisah ribuan Indonesia. */
export function angka(n: number | string | null | undefined): string {
  return (Number(n) || 0).toLocaleString("id-ID");
}

/**
 * URL yang boleh dipasang sebagai `href`. `null` kalau tidak.
 *
 * Ini PAGAR, bukan pembersih kosmetik, dan harus tetap seketat versi JS-nya.
 * Tautan Pustaka datang dari berkas data hasil panen, dan satu `javascript:`
 * yang lolos ke `href` berarti kode asing berjalan di halaman yang memegang
 * token API aplikasi ini. Yang diizinkan hanya http dan https.
 */
export function urlAman(u: unknown): string | null {
  return typeof u === "string" && /^https?:\/\//i.test(u.trim()) ? u : null;
}

/**
 * Tandai kemunculan `kata` di dalam `teks` dengan `<mark>`.
 *
 * Pencocokannya tanpa membedakan huruf besar-kecil, tapi yang DITAMPILKAN
 * selalu potongan asli `teks` -- bukan `kata` yang diketik pelajar. Kalau yang
 * digambar `kata`, judul "JavaScript" yang dicari dengan "javascript" akan
 * tampil dengan kapital yang salah, dan yang terlihat seperti data yang rusak.
 */
export function tandai(teks: string, kata?: string): ReactNode {
  if (!kata) return teks;
  const rendah = teks.toLowerCase();
  const cari = kata.toLowerCase();
  const bagian: ReactNode[] = [];
  let i = 0;
  for (;;) {
    const pos = rendah.indexOf(cari, i);
    if (pos < 0) break;
    if (pos > i) bagian.push(teks.slice(i, pos));
    bagian.push(<mark key={pos}>{teks.slice(pos, pos + cari.length)}</mark>);
    i = pos + cari.length;
  }
  bagian.push(teks.slice(i));
  return bagian;
}

/** Buang awalan nomor dari judul materi ("12. Variabel" -> "Variabel"). */
export function tanpaNomor(t: string): string {
  return t.replace(/^\s*\d+\.\s*/, "");
}
