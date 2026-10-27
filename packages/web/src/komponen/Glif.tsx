/* Glif bintang: satu penggambar untuk legenda, kepala panel, dan tip.
 *
 * Bentuknya datang dari `bagianGlif` (murni, diuji). Komponen ini cuma
 * membungkusnya jadi SVG kecil. Peta (ikhtisar dan lensa) menggambar path
 * yang sama langsung, tanpa komponen ini, karena di sana ratusan glif
 * digabung jadi beberapa atribut `d`.
 *
 * Kelasnya berawalan `lt-` dan ditulis literal (lihat `KELAS_GLIF`).
 */

import { bagianGlif, type StatusBintang } from "./lensa-geometri.ts";

/** Nama kelas ditulis LITERAL, bukan dirangkai dari awalan plus nama status: rangkaian membuat
 *  `TestKontrakKelasHidup` menganggap SETIAP `.lt-gl-*` hidup (kelas yatim lolos). */
export const KELAS_GLIF: Record<StatusBintang, string> = {
  selesai: "lt-gl-selesai",
  sebagian: "lt-gl-sebagian",
  baru: "lt-gl-baru",
  terkunci: "lt-gl-terkunci",
};

/** Selalu dekoratif (`aria-hidden`): statusnya sudah ditulis sebagai teks di
 *  sebelahnya (legenda, pil, kepala panel). */
export function Glif({
  status,
  r,
  ukuran,
}: {
  status: StatusBintang;
  r: number;
  ukuran: number;
}) {
  const bagian = bagianGlif(status, 0, 0, r);
  const setengah = ukuran / 2;
  return (
    <svg
      className="lt-glif"
      viewBox={`${-setengah} ${-setengah} ${ukuran} ${ukuran}`}
      width={ukuran}
      height={ukuran}
      focusable="false"
      aria-hidden="true"
    >
      {bagian.isi ? (
        <path className={`${KELAS_GLIF[status]} lt-gl-isi`} d={bagian.isi} />
      ) : null}
      {bagian.tepi ? (
        <path className={`${KELAS_GLIF[status]} lt-gl-tepi`} d={bagian.tepi} />
      ) : null}
    </svg>
  );
}
