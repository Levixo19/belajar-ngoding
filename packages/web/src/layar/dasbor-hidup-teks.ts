/* Isi murni "dasbor hidup": susunan baru Dasbor yang tidak lagi tumpukan kotak sama rupa
 * (`Dasbor.tsx`, `MejaKerja`). Tidak ada DOM dan tidak ada React.
 *
 * Gagasannya dari katalog 21st.dev: rel panel yang meluas saat disorot ("Hover Expand",
 * "Expanding Cards") dan angka yang menghitung naik ("Count Up"). Tidak ada kodenya yang
 * disalin; yang diambil hanya pola interaksinya, dengan isi data sungguhan.
 *
 * Yang dijaga di sini, semuanya soal ISI bukan gaya:
 *  - Rel bahasa hanya memuat bahasa yang SUDAH dijalani (persen > 0); langit yang seluruhnya
 *    redup tidak menjawab apa pun. Bahasa tempat posisi sekarang berada selalu pertama
 *    (itu yang terbuka sejak awal), sisanya menurut persen terbesar.
 *  - Teks persen dan materi sama dengan baris lama (`BarisBahasaMeja`): "43% selesai",
 *    "14/23 materi". Persennya ikut menghitung kuis dan latihan, jadi bukan "materi".
 *  - Tiga angka hari ini (XP, streak, level) datang dari `DataDasbor` yang sama dengan
 *    kartu lama; tidak ada definisi kedua.
 */

import { angka } from "../util.ts";
import {
  bandingHarian, celahBelajar,
  type BahasaDasbor, type DataDasbor,
} from "./dasbor-teks.ts";

/** Paling banyak berapa panel di rel. */
export const MAKS_REL = 6;

/** Bahasa untuk rel: yang dijalani, posisi sekarang di depan, sisanya menurut persen. */
export function urutRel(
  bahasa: BahasaDasbor[],
  kunciPosisi: string | null | undefined,
  maks: number = MAKS_REL,
): BahasaDasbor[] {
  const urut = bahasa.filter((b) => b.persen > 0).sort((a, b) => b.persen - a.persen);
  const awal = kunciPosisi ? urut.filter((b) => b.key === kunciPosisi) : [];
  const sisa = kunciPosisi ? urut.filter((b) => b.key !== kunciPosisi) : urut;
  return [...awal, ...sisa].slice(0, maks);
}

/** Tulisan satu panel rel. `isi` adalah lebar bilah (0..100). */
export function teksRel(b: BahasaDasbor): { persen: string; materi: string; isi: number } {
  return {
    persen: `${Math.round(b.persen)}% selesai`,
    materi: `${b.materi}/${b.total_materi} materi`,
    isi: Math.max(0, Math.min(100, b.persen)),
  };
}

export interface StatHidup {
  kunci: "hari" | "streak" | "level";
  nilai: number;
  satuan: string;
  ket: string;
  /** Lebar bilah di bawah angka, 0..100; -1 = tanpa bilah. */
  isi: number;
  capai: boolean;
}

/** Tiga angka di atas: XP hari ini, streak, dan level. */
export function statHariIni(d: DataDasbor): StatHidup[] {
  const kurang = Math.max(0, d.target_harian - d.xp_hari_ini);
  const celah = d.streak ? null : celahBelajar(d);
  return [
    {
      kunci: "hari",
      nilai: d.xp_hari_ini,
      satuan: kurang ? `dari ${angka(d.target_harian)} XP hari ini` : `XP hari ini · target ${angka(d.target_harian)} tercapai`,
      ket: bandingHarian(d).teks,
      isi: Math.min(100, (d.xp_hari_ini / Math.max(1, d.target_harian)) * 100),
      capai: kurang === 0,
    },
    {
      kunci: "streak",
      nilai: d.streak,
      satuan: d.streak ? "hari berturut-turut" : "belum ada hari berurutan",
      ket: celah ? `Terakhir belajar ${celah.tanggal}, ${angka(celah.selisih)} hari lalu` : "",
      isi: -1,
      capai: false,
    },
    {
      kunci: "level",
      nilai: d.level,
      satuan: d.gelar,
      ket: `${angka(d.xp)} XP, ${angka(d.di_level)} dari ${angka(d.butuh_level)} menuju level ${angka(d.level + 1)}`,
      isi: Math.min(100, (d.di_level / Math.max(1, d.butuh_level)) * 100),
      capai: false,
    },
  ];
}

/** Lencana yang dimiliki, "4/22". */
export function teksLencana(d: DataDasbor): string {
  return `${d.badge_dimiliki}/${d.badge_total}`;
}
