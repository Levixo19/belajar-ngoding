/* Pembantu kecil yang dipakai beberapa layar. Padanan sebagian `inti.js`.
 *
 * Yang masuk ke sini cuma yang sudah dipakai LEBIH DARI SATU layar, atau yang
 * memuat sebuah aturan. `inti.js` 803 baris sebagian karena ia jadi tempat
 * singgah apa pun yang belum punya rumah; folder ini tidak perlu mengulanginya.
 *
 * Yang TIDAK memakai JSX tinggal di `util.ts` dan diteruskan dari sini, supaya
 * pembanding `.mjs` bisa mengimpornya tanpa menyeret React. Alasan lengkapnya
 * ada di kepala berkas itu.
 */

import type { ReactNode } from "react";

export { angka, tanpaNomor, urlAman } from "./util.ts";

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

