/* Data layar Langit: bentuk jawaban API, letak rasi, daftar konsep, dan
 * tembolok yang hidup selama layar ini terbuka.
 *
 * Tembolok sengaja BUKAN variabel modul. Status bintang berubah setiap kali
 * pelajar membaca sebuah materi, dan itu hanya mungkin sesudah meninggalkan
 * layar ini; tembolok modul akan memperlihatkan menit dan status yang basi.
 * Yang disimpan adalah Promise-nya, bukan hasilnya, supaya dua pilihan
 * beruntun di kurikulum yang sama tidak menembakkan dua permintaan.
 */

import type { BahasaLangit, TataRasi } from "../komponen/lensa-geometri.ts";

export interface Profesi {
  id: string;
  nama: string;
  /** Tiap kelompok = "salah satu dari". */
  bekal: string[][];
}

export interface Jawaban {
  bahasa: BahasaLangit[];
  profesi: Profesi[];
  tujuan?: string;
}

const adaTeks = (v: unknown): v is string => typeof v === "string";
const adaDaftar = (v: unknown): v is unknown[] => Array.isArray(v);
const adaObjek = (v: unknown): v is Record<string, unknown> =>
  typeof v === "object" && v !== null && !Array.isArray(v);

/** Apakah jawaban `/api/langit` berbentuk yang dibaca layar ini? Server
 *  sungguhan selalu mengirimnya, tetapi `200 {}` (proksi yang salah, versi
 *  server yang tidak cocok) lolos `ambil` dan melempar di tengah render:
 *  tidak ada error boundary, jadi seluruh pohon React kosong. Yang dicek
 *  hanya medan yang dibaca layar Langit; medan lain boleh bertambah. */
export function bentukJawabanSah(d: unknown): d is Jawaban {
  if (!adaObjek(d) || !adaDaftar(d.bahasa) || !adaDaftar(d.profesi)) return false;
  const bab = (x: unknown) =>
    adaObjek(x) && typeof x.nomor === "number" && adaTeks(x.judul) && adaDaftar(x.materi) &&
    x.materi.every((i) => typeof i === "number");
  const bahasa = (x: unknown) =>
    adaObjek(x) && adaTeks(x.key) && adaTeks(x.label) && adaDaftar(x.materi) &&
    x.materi.every((m) => adaObjek(m) && adaTeks(m.judul) && adaTeks(m.status)) &&
    (x.bab === undefined || (adaDaftar(x.bab) && x.bab.every(bab)));
  const profesi = (x: unknown) =>
    adaObjek(x) && adaTeks(x.id) && adaTeks(x.nama) && adaDaftar(x.bekal) &&
    x.bekal.every((g) => adaDaftar(g) && g.every(adaTeks));
  return d.bahasa.every(bahasa) && d.profesi.every(profesi) && (d.tujuan === undefined || adaTeks(d.tujuan));
}

/** Pusat tiap rasi dan keluarganya. Tidak berubah dari layar lama: pelajar
 *  yang hafal letak "HTML" di pojok kiri atas tetap menemukannya di sana.
 *  Kurikulum yang belum terdaftar tetap muncul di baris cadangan. */
export const TATA: TataRasi = {
  html: [170, 200, "web"], css: [330, 140, "web"], javascript: [300, 330, "web"],
  typescript: [470, 260, "web"], php: [150, 420, "web"],
  c: [700, 150, "sistem"], cpp: [860, 210, "sistem"], rust: [760, 350, "sistem"],
  go: [930, 380, "sistem"],
  java: [1090, 150, "jvm"], kotlin: [1270, 220, "jvm"], aplikasi: [1060, 350, "jvm"],
  csharp: [1270, 420, "jvm"], vb: [1120, 540, "jvm"],
  python: [430, 560, "skrip"], ruby: [250, 640, "skrip"], bash: [570, 700, "skrip"],
  git: [790, 600, "perkakas"], fedora: [980, 680, "perkakas"], sql: [1290, 680, "perkakas"],
  techstack: [150, 980, "tech"], frontend: [390, 1055, "tech"], backend: [630, 975, "tech"],
  database: [870, 1050, "tech"], devops: [1110, 975, "tech"], keamanan: [1310, 1065, "tech"],
  mobile: [150, 1235, "tech"], game: [390, 1300, "tech"], iot: [630, 1230, "tech"],
  data: [870, 1300, "tech"], ai: [1110, 1230, "tech"], bahasalain: [1310, 1310, "tech"],
};

/** Nama keluarga dan letak judulnya (satuan dasar 1400 x 1420). Titiknya
 *  adalah SUDUT KIRI-BAWAH blok judul. Judul tiga keluarga terakhir DIPINDAH
 *  dari letak lama (di bawah kelompoknya, sehingga terbaca sebagai judul
 *  kelompok sesudahnya) ke ruang kosong di dekat rasi pertama kelompoknya;
 *  `uji/banding-lensa.mjs` memeriksa tidak ada judul yang menimpa rasi. */
export const KELUARGA: Record<string, [string, number, number]> = {
  web: ["Web", 60, 72], sistem: ["Sistem", 640, 72], jvm: ["JVM & .NET", 1080, 72],
  skrip: ["Skrip", 60, 651], perkakas: ["Perkakas & data", 818, 611],
  tech: ["Tech stack", 60, 921],
};
export const URUTAN_KELUARGA = ["web", "sistem", "jvm", "skrip", "perkakas", "tech"];

/** Konsep yang muncul di banyak kurikulum. Polanya mencocokkan JUDUL materi,
 *  bukan isinya: mencocokkan isi akan menyalakan hampir semua bintang untuk
 *  hampir semua konsep. Disalin apa adanya dari layar lama. */
export const KONSEP: Array<[string, RegExp]> = [
  ["Variabel & tipe", /variabel|tipe data|\bval\b|\bvar\b|konstanta/i],
  ["Percabangan", /percabangan|kendali alur|\bif\b|switch|\bwhen\b|select case|\bcase\b/i],
  ["Perulangan", /perulangan|loop|\bfor\b|while|iterasi|iterator/i],
  ["Fungsi", /fungsi|function|method|\bsub\b|prosedur|closure|lambda/i],
  ["Koleksi", /array|\blist\b|slice|koleksi|collection|\bmap\b|dict|hash|\bset\b|\bvec\b|tuple|stl/i],
  ["Teks & regex", /string|teks|regex|ekspresi reguler/i],
  ["Objek & class", /class|objek|oop|struct|record|interface|trait|pewarisan|inheritance|polymorph/i],
  ["Galat", /exception|galat|error|panic|\bresult\b/i],
  ["Berkas & I/O", /berkas|\bfile\b|i\/o|input|output|json|csv/i],
  ["Pengujian", /pengujian|\btest|\buji|debug/i],
  ["Konkurensi", /konkurensi|thread|goroutine|async|await|paralel|bersamaan|coroutine|race/i],
  ["Algoritma", /rekursi|algoritma|big-o|sorting|pengurutan|pencarian|kompleksitas/i],
  ["Modul & paket", /modul|paket|package|import|namespace|crate|dependensi|maven|gradle/i],
  ["Database", /database|\bsql\b|query|join|tabel|jdbc|pdo|transaksi/i],
];

/* ---------------------------------------------------- jawaban /api/bahasa */

export interface BabB {
  nomor: number;
  judul: string;
  ket: string;
  tingkat: string;
  label_tingkat: string;
  materi: number[];
  selesai: number;
  jumlah: number;
  status: string;
  alasan: string;
}

export interface MateriB {
  indeks: number;
  judul: string;
  menit: number;
  bagian: number;
  tingkat: string;
  bab: number;
}

export interface DataB {
  key: string;
  label: string;
  materi: MateriB[];
  bab: BabB[];
  kuis: Array<{ indeks: number; judul: string }>;
  latihan: Array<{ indeks: number; judul: string }>;
  tebak: number;
}

/** Hanya medan `/api/materi` yang dibaca panel. */
export interface DataM {
  judul: string;
  bagian: Array<{ jenis: string; blok?: Array<{ jenis: string; teks?: string; peran?: string }> | null }>;
}

/** Satu langkah dari `/api/dasbor`: dipakai untuk satu penanda "mulai di sini". */
export type { Langkah } from "./dasbor-teks.ts";

export interface Saran {
  bahasa: string;
  indeks: number;
  alasan: string;
}

/** Tembolok Promise per layar. */
export class Tembolok<T> {
  private peta = new Map<string, Promise<T>>();

  ambil(kunci: string, buat: () => Promise<T>): Promise<T> {
    const ada = this.peta.get(kunci);
    if (ada) return ada;
    const p = buat().catch((e: unknown) => {
      // Penolakan tidak boleh ditembolok: percobaan berikutnya harus bisa
      // berhasil kalau servernya sempat tersendat.
      this.peta.delete(kunci);
      throw e;
    });
    this.peta.set(kunci, p);
    return p;
  }
}
