/* Satu blok prosa (teks, daftar, pra, catatan) -> simpul.
 *
 * Port `blokProsa`, `senarai`, dan `berkode` dari
 * `webapp/statik/js/layar-belajar.js`. Ia komponen BERSAMA, bukan salinan per
 * layar, dan itu aturan yang ditulis di AGENTS.md: soal latihan lewat pengurai
 * yang sama dengan badan materi, karena contoh keluaran berkolom di dalam soal
 * butuh perlakuan yang persis sama dengan tabel di dalam materi. Menuliskannya
 * dua kali berarti suatu hari keduanya berbeda tanpa ada yang menyadarinya.
 *
 * Blok-bloknya datang dari `isi.blok_badan` di server; aturan penguraiannya
 * tinggal di sana, dan berkas ini tidak memutuskan apa pun soal itu.
 */

import type { ReactNode } from "react";

import { segmenKode } from "./prosa-teks.ts";

export { segmenKode } from "./prosa-teks.ts";
export type { SegmenProsa } from "./prosa-teks.ts";

/** Potongan -> simpul. Teks biasa tetap string, bukan `<span>`. */
export function Berkode({ teks }: { teks: string }): ReactNode {
  return segmenKode(teks).map((s, i) =>
    (typeof s === "string" ? s : <code key={i}>{s.teks}</code>));
}

export interface ButirDaftar {
  teks: string;
  blok?: { jenis: string; teks: string }[];
  anak?: DaftarProsa | null;
}
export interface DaftarProsa {
  urut: boolean;
  mulai?: number;
  butir: ButirDaftar[];
}

/**
 * Daftar butir materi.
 *
 * Sebuah butir bukan cuma sebaris teks: ia boleh membawa contoh kode kecil
 * miliknya sendiri dan boleh punya daftar anak. Ketiganya digambar DALAM `<li>`
 * yang sama supaya hubungannya terbaca -- contoh yang diletakkan sebagai
 * saudara di luar butirnya berdiri sejajar dengan butir berikutnya, dan pembaca
 * layar mengumumkannya sebagai isi yang tidak dimiliki siapa pun.
 *
 * `start` cuma dipasang kalau nomornya BUKAN satu. Butir bernomor yang dipotong
 * contoh kode atau baris kosong pecah jadi beberapa blok; tanpa nomor awal,
 * tiap potongan digambar sebagai `<ol>` baru dan web menampilkan 1, 1, 1
 * padahal sumbernya menulis 1, 2, 3.
 */
export function Senarai({ d }: { d: DaftarProsa }) {
  const isi = d.butir.map((x, i) => (
    <li key={i}>
      <Berkode teks={x.teks} />
      {(x.blok || []).map((sub, j) => (sub.jenis === "pra"
        ? <div key={j} className="pra pra-butir">{sub.teks}</div>
        : <div key={j} className="par par-butir"><Berkode teks={sub.teks} /></div>))}
      {x.anak ? <Senarai d={x.anak} /> : null}
    </li>
  ));
  const mulai = d.mulai && d.mulai > 1 ? d.mulai : undefined;
  return d.urut ? <ol start={mulai}>{isi}</ol> : <ul>{isi}</ul>;
}

export interface Blok {
  jenis: string;
  teks?: string;
  peran?: string;
  urut?: boolean;
  mulai?: number;
  butir?: ButirDaftar[];
}

/** Satu blok prosa -> simpul. */
export function BlokProsa({ blk }: { blk: Blok }) {
  if (blk.jenis === "pra") return <div className="pra">{blk.teks}</div>;
  if (blk.jenis === "daftar") {
    return <Senarai d={{ urut: !!blk.urut, mulai: blk.mulai, butir: blk.butir || [] }} />;
  }
  // Blok berperan ("Jebakan: ...", "Aturan ...") diberi kotaknya sendiri.
  // Kelas dasarnya tetap yang lama, jadi blok tanpa peran tidak berubah.
  const dasar = blk.jenis === "catatan" ? "catatan-prosa" : "par";
  const kelas = blk.peran ? `${dasar} peran peran-${blk.peran}` : dasar;
  return <div className={kelas}><Berkode teks={blk.teks || ""} /></div>;
}
