/** Jeda mata -- pengingat 20-20-20 untuk sesi belajar yang panjang.
 *
 *  Port `webapp/statik/js/istirahat.js`. Aturan 20-20-20: setiap 20 menit
 *  menatap layar, pandang sesuatu sejauh kira-kira 6 meter selama 20 detik.
 *  Mata yang terus memfokus pada jarak dekat itulah yang lelah.
 *
 *  Yang dihitung WAKTU AKTIF, bukan waktu sejak halaman dibuka:
 *
 *    - Tab yang tidak terlihat tidak dihitung. Orang yang pindah ke jendela
 *      lain tidak sedang menatap aplikasi ini.
 *    - Tanpa interaksi dua menit, detaknya berhenti. Diam selama itu bisa
 *      berarti membaca satu blok panjang, jadi waktunya tidak dibuang --
 *      cuma tidak ditambah.
 *    - Diam lima menit dianggap sudah beristirahat: hitungannya kembali ke
 *      nol. Mengingatkan orang yang baru kembali dari istirahat untuk
 *      beristirahat adalah cara tercepat membuat pengingat ini dimatikan.
 *
 *  Pengingatnya satu pemberitahuan tenang yang bertahan DUA PULUH detik --
 *  selama itulah jedanya, jadi pemberitahuan itu sendiri yang jadi penghitung
 *  waktunya. Tidak ada dialog yang harus ditutup dan tidak ada yang
 *  menghentikan pekerjaan.
 *
 *  Kuncinya `jeda_mata`, DIBAGI dengan antarmuka lama lewat awalan `belajar.`
 *  dan penyandian JSON yang sama (`lokal.ts` dan `inti.js` identik di situ).
 *  Bawaannya NYALA, dan bawaan itu ditulis sebagai `!== false` persis seperti
 *  aslinya: nilai rusak atau nilai yang belum pernah ada harus jatuh ke
 *  keadaan yang SAMA di kedua antarmuka. Pembaca kedua yang bawaannya
 *  berbeda berarti saklar yang menyala di satu halaman dan mati di halaman
 *  lain, tanpa satu pun error.
 */

import { ambilLokal, simpanLokal } from "./lokal.ts";
import { sorak } from "./sorak.tsx";

const KUNCI = "jeda_mata";
const SELANG_MS = 20 * 60 * 1000;
const DETAK_MS = 30 * 1000;
const DIAM_MS = 2 * 60 * 1000;
const ISTIRAHAT_MS = 5 * 60 * 1000;

export function bacaJedaMata(): boolean {
  return ambilLokal<boolean>(KUNCI, true) !== false;
}

export function setelJedaMata(nyala: boolean): void {
  simpanLokal(KUNCI, Boolean(nyala));
}

let terpasang = false;

/** Dipasang SEKALI per muatan halaman, dari luar React.
 *
 *  Penjaga `terpasang` ada karena `StrictMode` memanggil efek dua kali di
 *  pengembangan; dua pendengar dan dua interval akan menghitung waktu aktif
 *  dua kali lipat, dan pengingatnya datang tiap sepuluh menit alih-alih dua
 *  puluh. Dipanggil dari `main.tsx` di tingkat modul, sejajar dengan
 *  `terapkanTampilan()`.
 */
export function pasangJedaMata(): void {
  if (terpasang) return;
  terpasang = true;

  let aktif = 0;
  let sentuhTerakhir = Date.now();
  const tandai = () => { sentuhTerakhir = Date.now(); };

  // `scroll` tidak menggelembung, jadi didengar di fase TANGKAP: gulir di
  // panel keluaran atau di jalur materi juga tanda orangnya masih di sini.
  for (const jenis of ["pointerdown", "keydown", "wheel", "scroll"]) {
    window.addEventListener(jenis, tandai, { passive: true, capture: true });
  }

  setInterval(() => {
    if (document.visibilityState !== "visible") return;
    const diam = Date.now() - sentuhTerakhir;
    if (diam > ISTIRAHAT_MS) { aktif = 0; return; }
    if (diam > DIAM_MS) return;
    aktif += DETAK_MS;
    if (aktif < SELANG_MS) return;
    aktif = 0;
    if (!bacaJedaMata()) return;
    sorak("Sudah 20 menit. Pandang sesuatu sejauh 6 meter selama 20 detik, "
      + "lalu lanjutkan.", "", 20);
  }, DETAK_MS);
}
