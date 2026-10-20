/* Menggambar kode tersorot. Pengganti `keFragmen`/`praKode` di sorot.js.
 *
 * Perbedaan yang disengaja: `sorot.js` menempel `DocumentFragment` dengan
 * tangan karena ia harus menyorot ulang setiap ketikan. Di React token digambar
 * sebagai elemen biasa, jadi tidak ada penulis DOM imperatif di sini sama
 * sekali -- dan karena itu komponen ini bisa diuji tanpa shim DOM.
 *
 * DUA sumber token, dan bedanya penting:
 *
 * * Halaman materi menerima token yang sudah DIHITUNG server
 *   (`isi.token_kode`), jadi browser tidak memindai ulang ratusan blok kode
 *   saat halaman dibuka. Untuk itu pakai `<Kode token={...} />`.
 * * Editor harus menyorot ulang tiap ketikan, dan menempuh jaringan untuk itu
 *   -- meski cuma ke localhost -- membuat kursor terasa berat. Untuk itu pakai
 *   `<Kode kode={...} bahasa={...} />`, yang memindai di sisi klien lewat
 *   `@belajar/bersama`.
 *
 * Keduanya menghasilkan token yang identik; itu yang dijaga rekaman golden di
 * `packages/bersama/golden/sorot.json`.
 */

import { token as pindai, type Token } from "../../../bersama/src/sorot.ts";

interface Props {
  /** Token yang sudah dihitung server. Dipakai halaman materi. */
  token?: Token[];
  /** Kode mentah, dipindai di sisi klien. Dipakai editor dan ruang coba. */
  kode?: string;
  /** Nama penyorot. Wajib kalau `kode` diberikan. */
  bahasa?: string;
  /** Kelas tambahan pada `<pre>`. */
  kelas?: string;
}

/**
 * `<pre class="kode">` berisi kode tersorot.
 *
 * Token berjenis `"teks"` digambar sebagai teks biasa, bukan `<span>`. Itu
 * bukan penghematan kosmetik: sebuah blok kode normal lebih dari separuh
 * isinya teks biasa, dan membungkus tiap potongnya berarti ribuan elemen yang
 * tampilannya sama persis dengan tanpa elemen.
 */
export function Kode({ token, kode, bahasa, kelas }: Props) {
  const daftar: Token[] =
    token ?? (kode !== undefined ? pindai(kode, bahasa ?? "") : []);
  return (
    <pre className={"kode" + (kelas ? " " + kelas : "")}>
      <code>
        {daftar.map(([jenis, teks], i) =>
          jenis === "teks" ? (
            teks
          ) : (
            <span key={i} className={"tk-" + jenis}>
              {teks}
            </span>
          ),
        )}
      </code>
    </pre>
  );
}
