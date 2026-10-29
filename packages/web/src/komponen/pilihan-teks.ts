/* Logika murni `Pilihan` (select-only combobox): tombol navigasi dan pencarian
 * awalan. Nol rujukan ke `document` atau React, supaya bisa dites langsung
 * lewat pelucut tipe Node.
 *
 * Kenapa komponen ini ada: popup `<select>` bawaan peramban adalah jendela
 * terpisah yang tidak bisa dikendalikan halaman. Di Wayland ia bisa menutup
 * sendiri begitu klik dilepas dan baru bertahan kalau tombol mouse ditahan
 * (dilaporkan pemilik di Perencana Peta Karier). Daftar yang digambar di dalam
 * halaman tidak punya jalur kegagalan itu: ia terbuka saat diklik, tetap
 * terbuka sampai ada yang memilih atau menutupnya, dan memilih cukup satu klik
 * cepat.
 */

export interface OpsiPilihan {
  id: string;
  nama: string;
}

/** Berapa baris yang dilompati PageUp/PageDown. */
export const LOMPAT_HALAMAN = 10;

/** Indeks aktif sesudah sebuah tombol navigasi, atau `null` bila tombol itu
 *  bukan navigasi (pemanggil lalu memeriksa tombol lain, mis. Enter). */
export function geserAktif(tombol: string, aktif: number, jumlah: number): number | null {
  if (jumlah <= 0) return null;
  const batas = (i: number) => Math.max(0, Math.min(jumlah - 1, i));
  switch (tombol) {
    case "ArrowDown": return batas(aktif + 1);
    case "ArrowUp": return batas(aktif - 1);
    case "Home": return 0;
    case "End": return jumlah - 1;
    case "PageDown": return batas(aktif + LOMPAT_HALAMAN);
    case "PageUp": return batas(aktif - LOMPAT_HALAMAN);
    default: return null;
  }
}

/** Indeks opsi yang namanya diawali `awalan` (huruf besar-kecil tidak
 *  dibedakan), dicari mulai dari `dari` dan berputar ke awal. Satu huruf
 *  mencari mulai SESUDAH `dari` supaya menekan huruf yang sama berulang
 *  menggilir opsi berawalan itu; beberapa huruf (kata yang sedang diketik)
 *  boleh tetap di opsi sekarang. -1 bila tidak ada. */
export function cariAwalan(
  opsi: readonly OpsiPilihan[], awalan: string, dari: number,
): number {
  const n = opsi.length;
  const kunci = awalan.trim().toLocaleLowerCase("id");
  if (n === 0 || kunci === "") return -1;
  const mulai = kunci.length === 1 ? dari + 1 : dari;
  for (let k = 0; k < n; k++) {
    const i = (((mulai + k) % n) + n) % n;
    if ((opsi[i] as OpsiPilihan).nama.toLocaleLowerCase("id").startsWith(kunci)) return i;
  }
  return -1;
}

/** Sambungkan huruf yang baru diketik ke yang sebelumnya bila jedanya masih
 *  pendek; kalau tidak, mulai kata baru. */
export const JEDA_KETIK_MS = 700;

export function sambungAwalan(lalu: string, tLalu: number, huruf: string, t: number): string {
  return t - tLalu <= JEDA_KETIK_MS ? lalu + huruf : huruf;
}
