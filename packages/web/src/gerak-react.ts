/** Kait React untuk mesin gerak.
 *
 *  Berkas TERPISAH dari `gerak.ts`, dan itu bukan selera: `gerak.ts` diimpor
 *  pembandingnya di Node (`uji/banding-gerak.mjs`), dan modul yang mengimpor
 *  React akan menyeret seluruh React ke dalam pembanding matematika pegas.
 *  Jadi yang murni tetap murni; yang tahu soal React tinggal di sini.
 */

import { useEffect, useRef } from "react";
import type { RefObject } from "react";
import { adaGerak, ungkap } from "./gerak.ts";
import type { OpsiAnimasi, OpsiTampak, OpsiUrut } from "./gerak.ts";

type OpsiUngkap = OpsiAnimasi & OpsiUrut & OpsiTampak & { pilih?: string };

/** Ungkap anak-anak sebuah wadah saat ia tergulir ke layar.
 *
 *  `kunci` menentukan kapan dipasang ULANG: daftar yang isinya berganti
 *  (saringan bab, hasil cari) butuh pengungkapan baru, sementara daftar yang
 *  cuma digambar ulang dengan isi yang sama tidak -- memasangnya ulang di
 *  situ berarti isinya disembunyikan lagi lalu dimunculkan lagi, tepat di
 *  bawah mata orang yang sedang membaca.
 *
 *  Pelepasnya dipakai: `ungkap()` memasang `IntersectionObserver` plus satu
 *  pengaman waktu, dan keduanya hidup terus di belakang layar berikutnya
 *  kalau tidak dicabut.
 */
export function useUngkap<T extends HTMLElement>(
  opsi: OpsiUngkap = {}, kunci: unknown[] = [],
): RefObject<T | null> {
  const ref = useRef<T>(null);
  useEffect(() => {
    if (!ref.current || !adaGerak()) return;
    return ungkap(ref.current, opsi);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, kunci);
  return ref;
}
