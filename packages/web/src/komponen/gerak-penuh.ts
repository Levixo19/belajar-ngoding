/* Hook `useGerakPenuh`: apakah gerak sedang di tingkat "penuh", dan tetap
 * benar bila tingkatnya berubah di tengah jalan (tombol di pil atas, Ctrl+J,
 * Pengaturan, atau setelan sistem `prefers-reduced-motion`).
 *
 * Yang memutuskan tetap `gerakPenuh()` di `gerak.ts`; hook ini hanya
 * mendengarkan kapan harus bertanya lagi. Komponen yang membaca
 * `data-gerak` sendiri akan salah untuk orang yang menyalakan setelan sistem,
 * karena setelan sistem selalu menang di sana.
 */

import { useEffect, useState } from "react";

import { gerakPenuh } from "../gerak.ts";

export function useGerakPenuh(): boolean {
  const [penuh, setPenuh] = useState<boolean>(gerakPenuh);
  useEffect(() => {
    const segarkan = () => setPenuh(gerakPenuh());
    document.addEventListener("tampilan-berubah", segarkan);
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    mq.addEventListener("change", segarkan);
    segarkan();
    return () => {
      document.removeEventListener("tampilan-berubah", segarkan);
      mq.removeEventListener("change", segarkan);
    };
  }, []);
  return penuh;
}
