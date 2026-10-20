/* Bagian MURNI pembaca materi: pemotong label, dan label peta bagian.
 *
 * Port bagian non-DOM `webapp/statik/js/layar-belajar.js`. Keduanya memutuskan
 * APA YANG TERBACA di permukaan yang dipakai untuk memilih, bukan untuk
 * membaca -- dan permukaan seperti itu rusak dengan cara yang tidak kelihatan:
 * potongan yang jatuh di tempat salah tetap terlihat sebagai label yang wajar,
 * cuma berhenti memberi tahu isi di baliknya.
 *
 * Pagarnya `uji/banding-belajar.mjs`.
 */

/**
 * Potong di `n` karakter dengan elipsis. Tidak menyentuh batas kata.
 *
 * Nilai kosong dikembalikan APA ADANYA, bukan ditukar jadi string kosong, dan
 * tipenya mengakui itu. Versi pertama port ini "merapikannya" jadi `string`
 * dengan `?? ""` -- dan pembandingnya langsung menolak. Di tempat render
 * keduanya memang sama (React mengabaikan `null` maupun `""`), tapi selisih
 * yang tidak terlihat di satu pemanggil adalah selisih yang menunggu pemanggil
 * berikutnya: `potong(x, 26) || "Daftar materi"` berperilaku berbeda untuk
 * `""` dan `null` hanya kalau salah satunya pernah muncul.
 */
export function potong<T extends string | null | undefined>(
  t: T, n: number,
): T | string {
  return t && t.length > n ? t.slice(0, n - 1) + "…" : t;
}

export interface BlokRingkas {
  jenis: string;
  teks?: string;
  butir?: { teks: string }[];
}

/**
 * Label peta halaman untuk sebuah bagian prosa.
 *
 * Sebagian besar bagian di kurikulum ini tidak punya judul sendiri --
 * penulisnya memang menulis mengalir, bukan berjudul-judul. Kalimat pertamanya
 * dipakai sebagai gantinya, TAPI dipotong di batas KATA dan jauh lebih pendek
 * daripada judul biasa. Alasannya: peta yang berisi kalimat setengah jadi
 * ("Di aplikasi ini HTML tidak digambar seperti d…") lebih lambat dipindai
 * daripada peta berisi frasa pendek. Peta dibaca dengan MELIRIK, bukan dengan
 * membaca -- dan potongan di tengah kata memaksa mata berhenti untuk menebak
 * kata apa yang terpotong.
 *
 * Blok `pra` dilewati: ia tabel atau contoh berkolom, dan baris pertamanya
 * hampir selalu kepala kolom yang tidak berarti apa-apa di luar tabelnya.
 */
export function labelPeta(bg: { blok?: BlokRingkas[] }): string {
  const blok = (bg.blok || []).find(
    (x) => x.jenis !== "pra" && (x.teks || (x.butir && x.butir.length)));
  if (!blok) return "";
  const teks = String(blok.teks
    || (blok.butir && blok.butir[0] && blok.butir[0].teks) || "")
    .replace(/\s+/g, " ").trim();
  if (!teks) return "";
  /* Berhenti di tanda baca akhir kalimat pertama kalau ada dan cukup pendek;
     kalau tidak, potong di batas kata -- tidak pernah di tengah kata.

     Ambang 52 cuma menanggung beban dari BAWAH, dan itu diukur: menaikkannya
     ke 62 tidak mengubah satu pun dari 8.475 baris kurikulum yang titiknya
     jatuh di [52, 62). Sebabnya aritmetik -- apa pun yang lolos 44 dipotong
     ULANG di batas kata di dalam 44 karakter pertama, dan kedua sisi berbagi
     karakter-karakter itu. Jadi setiap nilai >= 45 berperilaku sama.
     Menurunkannya yang berarti: 22.564 baris titiknya jatuh di [30, 52), dan
     semuanya akan pindah dari jalur "potong di kalimat" ke jalur "potong di
     kata". Baterai mutasi yang menemukannya, lewat sel yang menaikkan
     ambangnya dan tetap hijau. */
  const titik = teks.search(/[.!?:](\s|$)/);
  let awal = titik > 8 && titik < 52 ? teks.slice(0, titik) : teks;
  if (awal.length > 44) {
    const batas = awal.lastIndexOf(" ", 44);
    awal = awal.slice(0, batas > 20 ? batas : 44) + "…";
  }
  return awal;
}
