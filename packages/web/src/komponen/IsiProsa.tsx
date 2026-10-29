/* Isi satu bagian prosa, dengan satu pengecualian: "Cara memecahkannya" di bagian "Di dunia nyata"
 * terlipat sampai pembaca membukanya.
 *
 * Kenapa terlipat: mengambil kembali (mencoba dulu, baru melihat jawaban) lebih awet daripada membaca
 * ulang, dan bagian ini sudah ada di SEMUA materi (judul "Cara memecahkannya:" diikuti daftar langkah),
 * jadi tidak butuh satu kata konten baru. Tidak ada yang disembunyikan selamanya: satu klik, dan cetak
 * membukanya. Tombolnya tombol asli (`aria-expanded`, `aria-controls`); isinya memakai atribut `hidden`,
 * bukan `<details>`, karena `hidden` cukup ditimpa `display: block` di cetak tanpa `!important`.
 *
 * Tidak memengaruhi indeks: semuanya terjadi DI DALAM `<section>` bagian itu, bukan di antara anak
 * `<article>` (anak ke-i artikel = bagian ke-i dipakai peta, pintasan, dan Ruang Coba).
 */

import { useId, useState } from "react";

import { BlokProsa, type Blok } from "./Prosa.tsx";

/** Indeks blok "Cara memecahkannya" bila sesudahnya masih ada isi; -1 bila tidak ada yang bisa dilipat. */
export function cariPecahkan(blok: Blok[]): number {
  const k = blok.findIndex((b) => b.jenis !== "pra" && b.jenis !== "daftar"
    && /^Cara memecahkannya\b/.test(b.teks ?? ""));
  return k >= 0 && k < blok.length - 1 ? k : -1;
}

export function IsiProsa({ blok, lipat }: { blok: Blok[]; lipat: boolean }) {
  const k = lipat ? cariPecahkan(blok) : -1;
  const [buka, setBuka] = useState(false);
  const id = useId();
  if (k < 0) return <>{blok.map((b, j) => <BlokProsa key={j} blk={b} />)}</>;
  return (
    <>
      {blok.slice(0, k).map((b, j) => <BlokProsa key={j} blk={b} />)}
      <div className="pecahkan">
        <button
          type="button"
          className="pecahkan-tombol"
          aria-expanded={buka}
          aria-controls={id}
          onClick={() => setBuka(!buka)}
        >
          <span>Cara memecahkannya</span>
          <span className="pecahkan-saran">{buka ? "tutup" : "coba dulu sendiri, lalu buka"}</span>
        </button>
        <div id={id} className="pecahkan-isi" hidden={!buka}>
          {blok.slice(k + 1).map((b, j) => <BlokProsa key={k + 1 + j} blk={b} />)}
        </div>
      </div>
    </>
  );
}
