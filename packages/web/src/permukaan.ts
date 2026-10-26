/** Permukaan -- cahaya kecil yang menjawab tangan.
 *
 *  Port `webapp/statik/js/permukaan.js`. Isinya satu hal: sorot di bawah
 *  kursor. Baris daftar, kartu, dan kartu Lanjutkan menyala samar tepat di
 *  bawah penunjuk. CSS-nya ada di bagian "permukaan" `gaya.css`; yang
 *  dikerjakan di sini cuma menyetel dua properti kustom (`--kx`, `--ky`)
 *  pada SATU elemen, yaitu yang sedang disentuh.
 *
 *  Tiga hal yang disengaja:
 *
 *  * **Hanya penunjuk halus.** Di layar sentuh tidak ada "di bawah kursor" --
 *    yang ada jari yang menutupi tempat itu sendiri.
 *  * **Paling banyak satu tulisan per frame.** `pointermove` bisa datang jauh
 *    lebih sering daripada layar menggambar; menulis gaya di setiap peristiwa
 *    berarti membayar hitung-ulang gaya yang tidak pernah terlihat.
 *  * **Elemen yang ditinggal DIBERSIHKAN.** Properti yang tersisa di elemen
 *    lama akan membekukan cahayanya di tempat terakhir kursor
 *    meninggalkannya.
 *
 *  Ini BUKAN gerak: tidak ada yang beranimasi sendiri, dan tidak ada yang
 *  berpindah tanpa tangan yang memindahkannya. Karena itu ia TIDAK lewat
 *  `tingkatGerak()` -- mematikan gerak tidak berarti mematikan cahaya, sama
 *  seperti mematikan gerak tidak mematikan warna hover.
 *
 *  Properti kustom disetel lewat `setProperty`, bukan `Object.assign` ke
 *  `style`: yang terakhir diam-diam MEMBUANG properti `--*`, dan itu bug yang
 *  sudah pernah terjadi di repo ini (pendar `--panas` yang alfanya nol
 *  selamanya).
 */

const SASARAN = ".senarai > .baris, .kartu, .lanjutkan";

/** Pasang sorot. Mengembalikan pelepasnya. */
export function pasangSorot(akar: Document | HTMLElement = document): () => void {
  let kini: HTMLElement | null = null;
  let x = 0;
  let y = 0;
  let antre = false;

  function lukis() {
    antre = false;
    if (!kini || !kini.isConnected) return;
    const r = kini.getBoundingClientRect();
    kini.style.setProperty("--kx", `${Math.round(x - r.left)}px`);
    kini.style.setProperty("--ky", `${Math.round(y - r.top)}px`);
  }

  function tinggalkan() {
    if (!kini) return;
    kini.style.removeProperty("--kx");
    kini.style.removeProperty("--ky");
    kini = null;
  }

  const saatGerak = (e: Event) => {
    const p = e as PointerEvent;
    if (p.pointerType !== "mouse") return;
    const el = p.target instanceof Element
      ? (p.target.closest(SASARAN) as HTMLElement | null)
      : null;
    if (el !== kini) tinggalkan();
    if (!el) return;
    kini = el;
    x = p.clientX;
    y = p.clientY;
    if (!antre) {
      antre = true;
      requestAnimationFrame(lukis);
    }
  };

  akar.addEventListener("pointermove", saatGerak, { passive: true });
  // Kursor keluar jendela, atau layar berganti di bawah kursor yang DIAM:
  // keduanya meninggalkan cahaya di elemen yang tidak lagi disentuh.
  document.documentElement.addEventListener("pointerleave", tinggalkan);
  window.addEventListener("hashchange", tinggalkan);

  return () => {
    akar.removeEventListener("pointermove", saatGerak);
    document.documentElement.removeEventListener("pointerleave", tinggalkan);
    window.removeEventListener("hashchange", tinggalkan);
    tinggalkan();
  };
}
