/* Bilah kemajuan. Port `bilah()` dari `inti.js`.
 *
 * Dua invarian bertemu di komponen sekecil ini, dan keduanya ada di AGENTS.md:
 *
 * 1. **Animasi tidak boleh jadi satu-satunya cara sebuah elemen terlihat.**
 *    Lebar akhirnya dipasang di gaya inline -- keadaan ALAMI elemennya -- dan
 *    animasinya cuma berangkat dari `0%`. Kalau polanya dibalik (`fill:
 *    "forwards"` menuju keadaan yang benar), maka gerak yang dimatikan,
 *    animasi yang dibatalkan saat layar berganti, atau pengamat yang tidak
 *    pernah menyala berarti bilahnya KOSONG selamanya.
 * 2. **Satu properti, satu mesin.** Yang menganimasikan `width` di sini WAAPI,
 *    jadi `.bilah > i` di `gaya.css` sengaja TIDAK punya `transition: width`.
 *    Dua mesin untuk satu properti saling mengejar dan menghasilkan gerakan
 *    tersendat yang sangat sulit didiagnosis.
 */

import { useEffect, useRef } from "react";

import { tingkatGerak } from "../gerak.ts";

const jepit = (n: number, a: number, b: number) => Math.min(b, Math.max(a, n));

export function Bilah({
  persen,
  kelas,
  diam = false,
  label,
}: {
  persen: number;
  kelas?: string;
  /** `true` untuk bilah yang digambar ulang tiap pergantian layar.
   *
   *  Strip konteks memakainya: bilah yang mengisi dari nol pada SETIAP
   *  perpindahan bukan lagi umpan balik melainkan kedipan. */
  diam?: boolean;
  label?: string;
}) {
  const isiRef = useRef<HTMLElement>(null);
  const p = jepit(Number(persen) || 0, 0, 100);
  const sebelumnya = useRef<number | null>(null);

  useEffect(() => {
    const isi = isiRef.current;
    if (!isi) return;
    const lama = sebelumnya.current;
    sebelumnya.current = p;
    if (diam || tingkatGerak() === "mati") return;
    // Muatan pertama berangkat dari nol; perubahan berikutnya dari nilai
    // sebelumnya, supaya bilah yang naik 40 -> 45 tidak jatuh dulu ke nol.
    const dari = (lama === null ? 0 : lama) + "%";
    isi.animate(
      { width: [dari, p + "%"] },
      { duration: 520, easing: "cubic-bezier(.32,.72,.36,1)" },
    );
  }, [p, diam]);

  return (
    <div
      className={"bilah" + (kelas ? " " + kelas : "")}
      role="progressbar"
      aria-valuenow={Math.round(p)}
      aria-valuemin={0}
      aria-valuemax={100}
      aria-label={label}
    >
      {/* Lebar akhir di gaya inline: inilah keadaan alaminya. */}
      <i ref={isiRef} style={{ width: p + "%" }} />
    </div>
  );
}
