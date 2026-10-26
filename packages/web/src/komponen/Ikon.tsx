/* Komponen ikon. Jalurnya tinggal di `ikon-bentuk.ts` dan sudah diadu dengan
 * `webapp/statik/js/ikon.js` (`uji/banding-ikon.mjs`), jadi tidak ada
 * koordinat yang bisa bergeser dari berkas ini.
 *
 * Semuanya mewarisi `currentColor`, jadi ikon otomatis ikut warna teks di
 * sekitarnya di keempat tema tanpa satu baris CSS tambahan.
 *
 * `aria-hidden` SELALU, dan itu bukan kelalaian aksesibilitas melainkan
 * sebaliknya: ikon di aplikasi ini selalu mendampingi teks yang sudah
 * menyampaikan artinya, jadi membiarkannya terbaca pembaca layar cuma
 * menghasilkan pengumuman ganda. Ikon yang berdiri SENDIRI sebagai satu-satunya
 * pembawa arti tidak boleh dibuat dengan komponen ini -- tombolnya yang perlu
 * `aria-label`, bukan ikonnya.
 */

import { isiJalur, jalurIkon } from "./ikon-bentuk.ts";

export function Ikon({
  nama,
  ukuran = 20,
  tebal = 1.7,
  kelas,
}: {
  nama: string;
  ukuran?: number;
  tebal?: number;
  kelas?: string;
}) {
  const jalur = jalurIkon(nama);
  if (!jalur) return null;
  return (
    <svg
      viewBox="0 0 24 24"
      width={ukuran}
      height={ukuran}
      fill="none"
      stroke="currentColor"
      strokeWidth={tebal}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      focusable="false"
      className={kelas}
      // `flex: none` di gaya inline, sama dengan versi JS: ikon di dalam baris
      // flex yang boleh menyusut akan terjepit jadi beberapa piksel di layar
      // sempit, dan yang terlihat bukan "ikonnya kecil" melainkan satu goresan
      // yang tidak bisa dikenali sebagai apa pun.
      style={{ flex: "none" }}
    >
      {jalur.map((d, i) => (
        <path key={i} d={d} {...(isiJalur(nama, i) ? { fill: "currentColor" } : {})} />
      ))}
    </svg>
  );
}
