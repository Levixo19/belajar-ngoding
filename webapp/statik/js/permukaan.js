/* =========================================================================
 * Permukaan — cahaya kecil yang menjawab tangan.
 *
 * Satu-satunya isi modul ini sorot di bawah kursor: baris daftar, kartu, dan
 * kartu Lanjutkan menyala samar tepat di bawah penunjuk. CSS-nya ada di
 * bagian "permukaan" gaya.css; yang dikerjakan di sini cuma menyetel dua
 * properti kustom (--kx, --ky) pada SATU elemen, yaitu yang sedang disentuh.
 *
 * Tiga hal yang disengaja:
 *
 *   · Hanya penunjuk halus. Di layar sentuh tidak ada "di bawah kursor" —
 *     yang ada jari yang menutupi tempat itu sendiri — jadi pointerType
 *     selain "mouse" diabaikan sejak awal.
 *   · Paling banyak satu tulisan per frame. Peristiwa pointermove bisa datang
 *     jauh lebih sering daripada layar menggambar; menulis gaya di setiap
 *     peristiwa berarti membayar hitung-ulang gaya yang tidak pernah terlihat.
 *   · Elemen yang ditinggal DIBERSIHKAN. Properti yang tersisa di elemen lama
 *     akan membekukan cahayanya di tempat terakhir kursor meninggalkannya.
 *
 * Ini bukan gerak: tidak ada yang beranimasi sendiri, dan tidak ada yang
 * berpindah tanpa tangan yang memindahkannya. Karena itu ia tidak lewat
 * tingkatGerak() — mematikan gerak tidak berarti mematikan cahaya, sama
 * seperti mematikan gerak tidak mematikan warna hover.
 * ========================================================================= */

const SASARAN = ".senarai > .baris, .kartu, .lanjutkan";

export function pasangSorot(akar = document) {
  let kini = null;
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

  akar.addEventListener("pointermove", (e) => {
    if (e.pointerType !== "mouse") return;
    const el = e.target instanceof Element ? e.target.closest(SASARAN) : null;
    if (el !== kini) tinggalkan();
    if (!el) return;
    kini = el;
    x = e.clientX;
    y = e.clientY;
    if (!antre) {
      antre = true;
      requestAnimationFrame(lukis);
    }
  }, { passive: true });

  // Kursor keluar jendela, atau layar berganti di bawah kursor yang diam:
  // keduanya meninggalkan cahaya di elemen yang tidak lagi disentuh.
  document.documentElement.addEventListener("pointerleave", tinggalkan);
  window.addEventListener("hashchange", tinggalkan);
}
