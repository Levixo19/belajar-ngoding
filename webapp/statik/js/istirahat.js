/* =========================================================================
 * Jeda mata — pengingat 20-20-20 untuk sesi belajar yang panjang.
 *
 * Aturan 20-20-20: setiap 20 menit menatap layar, pandang sesuatu sejauh
 * kira-kira 6 meter (20 kaki) selama 20 detik. Mata yang terus memfokus pada
 * jarak dekat itulah yang lelah, bukan mata yang membaca; dua puluh detik
 * melihat jauh sudah cukup untuk melemaskan otot fokusnya.
 *
 * Yang dihitung WAKTU AKTIF, bukan waktu sejak halaman dibuka:
 *
 *   · Tab yang tidak terlihat tidak dihitung. Orang yang pindah ke jendela
 *     lain tidak sedang menatap aplikasi ini.
 *   · Tanpa interaksi dua menit, detaknya berhenti. Diam selama itu bisa
 *     berarti membaca satu blok panjang, jadi waktunya tidak dibuang — cuma
 *     tidak ditambah.
 *   · Diam lima menit dianggap sudah beristirahat: hitungannya kembali ke nol.
 *     Mengingatkan orang yang baru kembali dari istirahat untuk beristirahat
 *     adalah cara tercepat membuat pengingat ini dimatikan.
 *
 * Pengingatnya satu pemberitahuan tenang yang bertahan DUA PULUH detik —
 * selama itulah jedanya, jadi pemberitahuan itu sendiri yang jadi penghitung
 * waktunya. Tidak ada dialog yang harus ditutup, tidak ada bunyi, dan tidak
 * ada yang menghentikan pekerjaan: menekan Jalankan di tengah jeda tetap
 * menjalankan kode.
 *
 * Bawaannya NYALA, dan saklarnya di Pengaturan > Tampilan. Disimpan di
 * browser ini saja, seperti tema: ini soal kenyamanan layar, bukan capaian
 * belajar.
 * ========================================================================= */

import { sorak, simpanLokal, ambilLokal } from "./inti.js";

const KUNCI = "jeda_mata";
const SELANG_MS = 20 * 60 * 1000;
const DETAK_MS = 30 * 1000;
const DIAM_MS = 2 * 60 * 1000;
const ISTIRAHAT_MS = 5 * 60 * 1000;

export function bacaJedaMata() {
  return ambilLokal(KUNCI, true) !== false;
}

export function setelJedaMata(nyala) {
  simpanLokal(KUNCI, Boolean(nyala));
}

export function pasangJedaMata() {
  let aktif = 0;
  let sentuhTerakhir = Date.now();
  const tandai = () => { sentuhTerakhir = Date.now(); };

  // `scroll` tidak menggelembung, jadi didengar di fase tangkap: gulir di
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
