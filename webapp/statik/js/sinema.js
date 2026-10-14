/* =========================================================================
 * Sinema — judul yang tiba kata demi kata, lewat GSAP + SplitText.
 *
 * GSAP disimpan LOKAL di statik/vendor/gsap/ (3.15.0, lisensi standar tanpa
 * biaya, gsap.com/standard-license) dan dimuat index.html sebagai skrip
 * `defer` sebelum modul ini. Aplikasi ini harus utuh tanpa internet, jadi
 * tidak ada satu pun permintaan ke CDN — dan kalau berkasnya gagal dimuat,
 * modul ini diam saja: judulnya sudah ada di halaman sejak awal.
 *
 * KAPAN, dan terutama kapan TIDAK:
 *
 *   · Hanya di layar "pintu" — dasbor, halaman bahasa, statistik, dan
 *     teman-temannya. Materi, latihan, dan kuis dibuka ratusan kali dalam
 *     satu sesi panjang; gerak yang menyenangkan di kunjungan pertama jadi
 *     penghalang di kunjungan keempat puluh. Pemanggilnya yang memilih layar.
 *   · Hanya di tingkat gerak "penuh". Yang memutuskan tingkat itu cuma
 *     tingkatGerak() lewat gerakPenuh() — prefers-reduced-motion selalu
 *     menang di sana, jadi tidak ada gsap.matchMedia kedua yang bisa berbeda
 *     pendapat dengannya.
 *   · Hanya transform dan opacity, pada SPAN kata yang dibuat SplitText —
 *     bukan pada h1-nya. h1 itu anak blok yang sedang dimasukkan
 *     masukBerurut() lewat WAAPI; satu properti, satu mesin, dan mesinnya
 *     beda elemen.
 *
 * Keadaan akhir = keadaan alami: `gsap.from` berangkat dari bawah dan pudar,
 * lalu berhenti tepat di tempat kata itu memang berdiri. Begitu selesai,
 * split.revert() mengembalikan h1 ke teks polosnya — tidak ada span yang
 * tertinggal untuk dibaca pembaca layar kata per kata. Pembersih yang
 * dikembalikan melakukan hal yang sama kalau layarnya ditinggal di tengah
 * jalan.
 * ========================================================================= */

import { gerakPenuh } from "./gerak.js";

let terdaftar = false;

function gsapSiap() {
  const g = window.gsap;
  if (!g || !window.SplitText) return null;
  if (!terdaftar) {
    g.registerPlugin(window.SplitText);
    terdaftar = true;
  }
  return g;
}

const TANPA_APA_APA = () => {};

/** Ungkap h1 pertama di `akar` kata demi kata. Mengembalikan pembersih. */
export function ungkapJudul(akar) {
  const g = gsapSiap();
  const h1 = akar && akar.querySelector("h1");
  if (!g || !h1 || !gerakPenuh()) return TANPA_APA_APA;

  let split = null;
  let tween = null;
  let batal = false;

  const mulai = () => {
    if (batal || !h1.isConnected) return;
    split = window.SplitText.create(h1, { type: "words", aria: "auto" });
    tween = g.from(split.words, {
      yPercent: 55,
      opacity: 0,
      duration: 0.62,
      ease: "expo.out",
      stagger: 0.04,
      onComplete: () => {
        if (split) split.revert();
        split = null;
      },
    });
  };

  // Memecah sebelum huruf selesai dimuat berarti mengukur kata dengan huruf
  // cadangan, lalu kata-kata itu bergeser sendiri begitu huruf aslinya tiba.
  if (document.fonts && document.fonts.status !== "loaded") {
    document.fonts.ready.then(mulai);
  } else {
    mulai();
  }

  return () => {
    batal = true;
    if (tween) tween.kill();
    if (split) split.revert();
    split = null;
  };
}
