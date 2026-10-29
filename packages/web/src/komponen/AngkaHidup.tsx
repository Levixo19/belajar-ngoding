/* Angka yang menghitung naik saat dasbor tampil. Gagasannya dari "Count Up" (unlumen, 21st.dev);
 * kodenya ditulis ulang di atas tingkat gerak aplikasi ini, tanpa pustaka.
 *
 * Aturan yang gampang terbalik tanpa satu pun error:
 *  - Keadaan alaminya adalah angka AKHIR. Animasi hanya berangkat dari nol; gerak yang
 *    dimatikan, tab yang tidak terlihat, atau efek yang tidak pernah jalan berarti angka
 *    yang benar tetap tertulis. Angka di luar layar saat dipasang tidak dianimasikan sama
 *    sekali (menganimasikannya begitu tergulir ke sana adalah kedipan di depan mata
 *    orang yang sedang membaca).
 *  - Hanya tingkat gerak penuh (`useGerakPenuh`): menghitung naik adalah gerak yang jalan
 *    SENDIRI, dan `prefers-reduced-motion` selalu menang.
 *  - Pembaca layar membaca angka akhirnya saja (`.ds-sr`); yang berubah-ubah `aria-hidden`.
 *    Teksnya ditulis lewat ref, bukan anak React: React memegang simpul teksnya sendiri,
 *    dan menimpa `textContent` di bawahnya meninggalkan simpul yatim.
 *  - Perubahan nilai sesudah pertama kali (XP bertambah) berangkat dari angka sebelumnya,
 *    bukan dari nol.
 */

import { useEffect, useLayoutEffect, useRef } from "react";

import { angka } from "../util.ts";
import { durasiAngka, tahapAngka } from "./angka-hidup-teks.ts";
import { useGerakPenuh } from "./gerak-penuh.ts";

export function AngkaHidup({ nilai, kelas }: { nilai: number; kelas?: string }) {
  const hidup = useRef<HTMLSpanElement>(null);
  /** Nilai yang terakhir DITULIS; null = belum pernah. */
  const terakhir = useRef<number | null>(null);
  const penuh = useGerakPenuh();

  // Sebelum cat pertama: tidak ada bingkai kosong, dan tidak ada kedipan angka akhir lalu nol.
  useLayoutEffect(() => {
    const el = hidup.current;
    if (!el) return;
    const akhir = angka(nilai);
    const sebelum = terakhir.current;
    terakhir.current = nilai;
    if (!penuh || sebelum === nilai) {
      el.textContent = akhir;
      return;
    }
    let dari = sebelum ?? 0;
    if (sebelum === null) {
      const k = el.getBoundingClientRect();
      if (k.bottom < 0 || k.top > window.innerHeight) {
        el.textContent = akhir;
        return;
      }
    }
    if (dari === nilai) dari = 0;
    el.textContent = angka(dari);
    const mulai = performance.now();
    const lama = durasiAngka(dari, nilai);
    let id = 0;
    const langkah = (t: number) => {
      el.textContent = angka(tahapAngka(dari, nilai, (t - mulai) / lama));
      if (t - mulai < lama) id = requestAnimationFrame(langkah);
    };
    id = requestAnimationFrame(langkah);
    return () => {
      cancelAnimationFrame(id);
      el.textContent = akhir;
    };
  }, [nilai, penuh]);

  // Cadangan: tab yang baru terlihat tidak menahan angka di tengah jalan.
  useEffect(() => {
    const el = hidup.current;
    if (!el) return;
    const kembali = () => {
      if (!document.hidden) return;
      el.textContent = angka(nilai);
    };
    document.addEventListener("visibilitychange", kembali);
    return () => document.removeEventListener("visibilitychange", kembali);
  }, [nilai]);

  return (
    <span className={"angka-hidup" + (kelas ? " " + kelas : "")}>
      <span ref={hidup} aria-hidden="true" />
      <span className="ds-sr">{angka(nilai)}</span>
    </span>
  );
}
