/** Sinema -- judul yang tiba kata demi kata, lewat GSAP + SplitText.
 *
 *  Port `webapp/statik/js/sinema.js`. GSAP disimpan LOKAL di
 *  `webapp/statik/vendor/gsap/` (3.15.0, lisensi standar tanpa biaya,
 *  gsap.com/standard-license) dan dilayani server Python apa adanya.
 *  Aplikasi ini harus utuh tanpa internet, jadi tidak ada satu pun
 *  permintaan ke CDN -- dan kalau berkasnya gagal dimuat, modul ini DIAM
 *  saja: judulnya sudah ada di halaman sejak awal.
 *
 *  Kapan, dan terutama kapan TIDAK:
 *
 *  * **Hanya di layar "pintu"** -- dasbor, halaman bahasa, statistik, dan
 *    teman-temannya. Materi, latihan, dan kuis dibuka ratusan kali dalam satu
 *    sesi panjang; gerak yang menyenangkan di kunjungan pertama jadi
 *    penghalang di kunjungan keempat puluh. Pemanggilnya yang memilih layar.
 *  * **Hanya di tingkat gerak "penuh"**, dan yang memutuskan cuma
 *    `gerakPenuh()` -- `prefers-reduced-motion` selalu menang di sana, jadi
 *    tidak ada `gsap.matchMedia` kedua yang bisa berbeda pendapat.
 *  * **Hanya transform dan opacity, pada SPAN kata** yang dibuat SplitText --
 *    bukan pada `h1`-nya. `h1` itu anak blok yang sedang dimasukkan WAAPI;
 *    satu properti, satu mesin, dan mesinnya beda elemen.
 *
 *  Keadaan akhir = keadaan alami: `gsap.from` berangkat dari bawah dan pudar,
 *  lalu berhenti tepat di tempat kata itu memang berdiri. Begitu selesai,
 *  `split.revert()` mengembalikan `h1` ke teks polosnya -- tidak ada span
 *  yang tertinggal untuk dibaca pembaca layar kata per kata.
 */

import { gerakPenuh } from "./gerak.ts";

interface Split { words: Element[]; revert(): void }
interface Tween { kill(): void }
interface Gsap {
  registerPlugin(p: unknown): void;
  from(s: unknown, v: Record<string, unknown>): Tween;
}
interface SplitTextStatis {
  create(el: Element, o: Record<string, unknown>): Split;
}

let terdaftar = false;

function gsapSiap(): Gsap | null {
  const w = globalThis as unknown as { gsap?: Gsap; SplitText?: SplitTextStatis };
  const g = w.gsap;
  if (!g || !w.SplitText) return null;
  if (!terdaftar) {
    g.registerPlugin(w.SplitText);
    terdaftar = true;
  }
  return g;
}

const TANPA_APA_APA = () => {};

/** Ungkap `h1` pertama di `akar` kata demi kata. Mengembalikan pembersih. */
export function ungkapJudul(akar: Element | null): () => void {
  const g = gsapSiap();
  const h1 = akar?.querySelector("h1");
  const w = globalThis as unknown as { SplitText?: SplitTextStatis };
  if (!g || !h1 || !w.SplitText || !gerakPenuh()) return TANPA_APA_APA;

  let split: Split | null = null;
  let tween: Tween | null = null;
  let batal = false;

  const mulai = () => {
    if (batal || !h1.isConnected) return;
    split = w.SplitText!.create(h1, { type: "words", aria: "auto" });
    tween = g.from(split.words, {
      yPercent: 55,
      opacity: 0,
      duration: 0.62,
      ease: "expo.out",
      stagger: 0.04,
      onComplete: () => {
        split?.revert();
        split = null;
      },
    });
  };

  // Memecah SEBELUM huruf selesai dimuat berarti mengukur kata dengan huruf
  // cadangan, lalu kata-kata itu bergeser sendiri begitu huruf aslinya tiba.
  if (document.fonts && document.fonts.status !== "loaded") {
    void document.fonts.ready.then(mulai);
  } else {
    mulai();
  }

  return () => {
    batal = true;
    tween?.kill();
    split?.revert();
    split = null;
  };
}

/** Sama dengan `ungkapJudul`, tapi MENUNGGU `h1`-nya tiba.
 *
 *  Beda struktural dari sisi JS, dan satu-satunya alasan fungsi ini ada: di
 *  `aplikasi.js` router MENUNGGU data layarnya sebelum menempelkannya, jadi
 *  `ungkapJudul()` selalu mengukur halaman yang sudah penuh. Di React
 *  cangkangnya digambar LEBIH DULU -- saat efeknya jalan, `#layar` masih
 *  sebuah pusaran, dan `querySelector("h1")` mengembalikan null. Terukur
 *  sebelum pengamat ini ada: nol kata terpecah di SELURUH delapan layar
 *  pintu, tanpa satu pun galat di konsol. Ini kembaran dari pengamat ukuran
 *  di bilah kemajuan baca, dengan sebab yang sama.
 *
 *  Batas waktunya bukan kehati-hatian: layar yang memang tidak punya `h1`
 *  (atau permintaan yang gagal) akan meninggalkan pengamat hidup di belakang
 *  layar berikutnya. Yang mengikat sama dengan `pinKeHariIni()`: pengamatnya
 *  WAJIB lepas, dan ia lepas pada kejadian pertama yang menjawabnya. */
const TUNGGU_JUDUL_MS = 4000;

export function ungkapJudulSaatTiba(akar: Element | null): () => void {
  if (!akar) return TANPA_APA_APA;
  if (akar.querySelector("h1")) return ungkapJudul(akar);
  if (!gsapSiap() || !gerakPenuh()) return TANPA_APA_APA;

  let lepasUngkap: (() => void) | null = null;
  const pengamat = new MutationObserver(() => {
    if (!akar.querySelector("h1")) return;
    selesai();
    lepasUngkap = ungkapJudul(akar);
  });
  const jam = setTimeout(selesai, TUNGGU_JUDUL_MS);
  pengamat.observe(akar, { childList: true, subtree: true });

  function selesai() {
    pengamat.disconnect();
    clearTimeout(jam);
  }

  return () => {
    selesai();
    lepasUngkap?.();
  };
}
