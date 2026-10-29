/* Isi penutup dasbor ("Cakrawala"): layar terakhir yang tersingkap saat dasbor
 * digulir sampai habis (`PenutupDasbor.tsx`). BAGIAN MURNI: tidak ada DOM, tidak
 * ada React, dan tidak ada angka yang diketik. Semua yang tampil di strip dan
 * judulnya dihitung dari `DataDasbor`, jadi angkanya persis angka yang sudah ada
 * di dasbor, dan kalimat pembukanya persis `kalimatPembuka` (satu rumusan, bukan
 * dua yang bisa melenceng).
 *
 * Gagasan layarnya dari komponen "Motion Footer" (21st.dev; penulis Hossain
 * Jahed, bidang lisensinya KOSONG): footer yang diam di bawah konten dan
 * tersingkap saat digulir, strip teks miring yang berjalan, kata raksasa
 * tembus pandang, dan pil kaca yang mengikuti kursor. Tidak ada kodenya yang
 * disalin; semuanya ditulis ulang di atas mesin gerak repo ini.
 *
 * Dua aturan isi yang gampang terbalik tanpa satu pun error:
 *  - Strip memuat hanya yang BERARTI. "0 hari berturut-turut" dan "0 lencana"
 *    adalah katalog kegagalan yang bahkan belum sempat dilakukan, dan di layar
 *    yang berjalan sendiri (marquee) kalimat seperti itu terbaca sebagai
 *    teguran yang tak bisa dihentikan. Yang nol atau satu dibuang, bukan
 *    ditulis "0".
 *  - Tautannya sama dengan tujuan di bilah atas, tidak ada yang baru. Satu
 *    layar satu tombol utama: penutup tidak punya tombol beraksen kedua; yang
 *    utama tetap kartu Lanjutkan di atas, dan tombol "ke atas" mengembalikan
 *    orang ke sana. */

import { angka } from "../util.ts";
import { kalimatPembuka, type DataDasbor } from "./dasbor-teks.ts";

/** Kata raksasa di latar. Bagian dari penampilan, bukan isi: `aria-hidden`. */
export const KATA_RAKSASA = "belajar";

export interface TautanPenutup {
  label: string;
  href: string;
  /** Nama ikon di `komponen/ikon-bentuk.ts`. */
  ikon: string;
}

/** Dua pil besar. Tujuan yang paling sering dibuka sesudah dasbor. */
export const TAUTAN_UTAMA: readonly TautanPenutup[] = [
  { label: "Peta Langit", href: "#/langit", ikon: "bintang" },
  { label: "Ruang Coba", href: "#/coba", ikon: "latihan" },
];

/** Empat pil kecil, tujuan sisanya di bilah atas. */
export const TAUTAN_KECIL: readonly TautanPenutup[] = [
  { label: "Pustaka", href: "#/pustaka", ikon: "pustaka" },
  { label: "Peta Karier", href: "#/karier", ikon: "karier" },
  { label: "Statistik", href: "#/statistik", ikon: "statistik" },
  { label: "Pengaturan", href: "#/atur", ikon: "atur" },
];

/** Butir strip yang berjalan. Selalu ada dua yang pertama; selebihnya hanya
 *  bila bernilai. Urutannya tetap: yang paling stabil di depan. */
export function butirStrip(d: DataDasbor): string[] {
  // Dihitung LANGSUNG dari data, bukan dari `dijalaniDasbor`: yang itu dipotong di enam untuk
  // bento, jadi orang yang menjalani sepuluh kurikulum akan dibaca "6 kurikulum dijalani".
  const dijalani = d.bahasa.filter((b) => b.persen > 0);
  const materi = d.bahasa.reduce((a, b) => a + b.materi, 0);
  const total = d.bahasa.reduce((a, b) => a + b.total_materi, 0);
  const butir = [`Level ${angka(d.level)}, ${d.gelar}`, `${angka(d.xp)} XP`];
  if (materi > 0 && total > 0) butir.push(`${angka(materi)} dari ${angka(total)} materi dibaca`);
  if (d.streak >= 2) butir.push(`${angka(d.streak)} hari berturut-turut`);
  if (d.badge_dimiliki > 0) butir.push(`${angka(d.badge_dimiliki)} dari ${angka(d.badge_total)} lencana`);
  if (dijalani.length > 0) butir.push(`${angka(dijalani.length)} kurikulum dijalani`);
  if (d.kuis_jatuh_tempo > 0) butir.push(`${angka(d.kuis_jatuh_tempo)} kuis menunggu diulang`);
  return butir;
}

/** Penanda kecil di atas judul: kemajuan hari ini, dari angka yang sama dengan kartu Bara. */
export function alisPenutup(d: DataDasbor): string {
  return `Hari ini: ${angka(d.xp_hari_ini)} dari ${angka(d.target_harian)} XP`;
}

/** Judul penutup = kalimat pembuka dasbor, kata demi kata. */
export function judulPenutup(d: DataDasbor): string {
  return kalimatPembuka(d);
}

/** Kalimat yang dibacakan pembaca layar untuk strip yang `aria-hidden`. */
export function ringkasStrip(d: DataDasbor): string {
  return butirStrip(d).join(", ") + ".";
}
