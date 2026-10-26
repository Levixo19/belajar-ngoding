/* Tingkat gerak. Port `tingkatGerak()` dari `webapp/statik/js/gerak.js`.
 *
 * Satu aturan yang mengikat seluruh aplikasi, dan ia sudah mengikat di sisi
 * JS: **ini SATU-SATUNYA tempat yang berhak memutuskan tingkat gerak.** Jangan
 * membaca `data-gerak` langsung dari komponen mana pun.
 *
 * Alasannya bukan kerapian. `prefers-reduced-motion` di sistem operasi SELALU
 * menang atas saklar di halaman: kalau pemakainya sudah bilang ke sistemnya
 * bahwa ia ingin gerak dikurangi, tidak ada setelan di aplikasi ini yang
 * berhak membantahnya. Begitu ada tempat kedua yang menyimpulkannya sendiri,
 * satu permukaan akan tetap bergerak sementara yang lain berhenti -- dan yang
 * terlihat bukan error melainkan aplikasi yang setengah menghormati pilihan
 * orang.
 */

export type TingkatGerak = "penuh" | "halus" | "mati";

const ADA_DOM = typeof document !== "undefined";
const kurangiGerak =
  ADA_DOM && typeof matchMedia === "function"
    ? matchMedia("(prefers-reduced-motion: reduce)")
    : null;

/** `"penuh"` | `"halus"` | `"mati"`. Setelan sistem menang atas apa pun. */
export function tingkatGerak(): TingkatGerak {
  if (!ADA_DOM) return "mati";
  if (kurangiGerak?.matches) return "mati";
  const d = document.documentElement.dataset.gerak;
  if (d === "mati") return "mati";
  if (d === "halus") return "halus";
  return "penuh";
}

export const adaGerak = (): boolean => tingkatGerak() !== "mati";
export const gerakPenuh = (): boolean => tingkatGerak() === "penuh";

/** Panggil `fn` saat `prefers-reduced-motion` SISTEM berubah.
 *
 *  Padanan fungsi bernama sama di `gerak.js`. Saklar `data-gerak` di aplikasi
 *  TIDAK lewat sini -- yang mengamatinya `MutationObserver` di pemakainya,
 *  karena ia atribut, bukan media query. Keduanya perlu: orang bisa mengubah
 *  setelan sistemnya tanpa menyentuh aplikasi ini.
 */
export function saatGerakBerubah(fn: (tingkat: TingkatGerak) => void): () => void {
  if (typeof matchMedia !== "function") return () => {};
  const mq = matchMedia("(prefers-reduced-motion: reduce)");
  const bungkus = () => fn(tingkatGerak());
  mq.addEventListener("change", bungkus);
  return () => mq.removeEventListener("change", bungkus);
}
