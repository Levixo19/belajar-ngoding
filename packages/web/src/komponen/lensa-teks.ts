/* Teks panel bintang: ringkasan paragraf pembuka dan kata aksi. Murni.
 *
 * `ringkasPembuka` TIDAK mengarang deskripsi. Ia memangkas paragraf pembuka
 * yang memang sudah ditulis di materi (`bagian[0]` dari `/api/materi`), dengan
 * aturan yang diukur atas SELURUH 1.062 materi: hasilnya selalu ada, median 190
 * karakter, dan tidak pernah berakhir titik dua. Aturan naifnya (blok pertama
 * apa adanya) menghasilkan 17 persen kalimat yang menggantung ("Ketiganya
 * dibedakan dari artinya:") karena blok pertama sering cuma pengantar daftar
 * atau kode.
 */

import { tanpaNomor } from "../util.ts";
import { KATA_STATUS_BINTANG, type StatusBintang } from "./lensa-geometri.ts";

/** Satu blok prosa dari `/api/materi` (hanya medan yang dibaca di sini). */
export interface BlokPembuka {
  jenis: string;
  teks?: string;
  peran?: string;
}

export interface BagianPembuka {
  jenis: string;
  blok?: BlokPembuka[] | null;
}

const SINGKATAN = /\b(?:dll|dsb|dst|mis|yg|dgn|tsb|no|vs|bdk|cth|spt|hlm|ket)\.$/i;
const AKHIR = /[.!?]$/;
const MAKS_KALIMAT = 3;
const MAKS_KARAKTER = 260;
/** Blok kedua dst. ikut hanya bila sepanjang ini dan berakhir tanda baca:
 *  label kecil seperti "Keamanan" atau "Pemilih dasar:" bukan kalimat. */
const MIN_LANJUTAN = 30;

/** Pecah jadi kalimat; singkatan ("dll.", "mis.") tidak dianggap akhir kalimat. */
export function pecahKalimat(teks: string): string[] {
  const mentah = teks
    .trim()
    .split(/(?<=[.!?])\s+(?=[A-Z0-9"“(<`'])/)
    .filter((k) => k.length > 0);
  const keluar: string[] = [];
  for (const k of mentah) {
    const akhir = keluar.length - 1;
    if (akhir >= 0 && SINGKATAN.test(keluar[akhir] as string)) {
      keluar[akhir] += " " + k;
    } else {
      keluar.push(k);
    }
  }
  return keluar;
}

function rakit(kalimat: string[]): string {
  let hasil = "";
  for (const k of kalimat.slice(0, MAKS_KALIMAT)) {
    if (hasil && hasil.length + 1 + k.length > MAKS_KARAKTER) break;
    hasil = (hasil + " " + k).trim();
  }
  // Satu-satunya jalan hasil melewati batas: kalimat PERTAMA yang sendirian
  // lebih panjang daripada 260 karakter (kalimat berikutnya hanya ikut kalau
  // muat). Tidak ada contohnya di 1.062 materi sekarang, tapi materi baru bisa;
  // dipotong di spasi terakhir, tanpa koma atau titik dua yang menggantung.
  if (hasil.length > MAKS_KARAKTER) {
    const potong = hasil.slice(0, MAKS_KARAKTER);
    const spasi = potong.lastIndexOf(" ");
    return (spasi > 0 ? potong.slice(0, spasi) : potong).replace(/[,;:]+$/, "") + "\u2026";
  }
  return hasil;
}

/**
 * Paragraf pembuka sebuah materi, dipangkas jadi paling banyak tiga kalimat
 * dan 260 karakter. `null` kalau materinya tidak berawal dengan prosa
 * (tidak pernah terjadi di data sekarang, tapi data baru bisa).
 *
 * Kalimat pengantar yang berakhir ":" dibuang; kalau SEMUA kalimat pengantar,
 * titik duanya diganti titik pada kalimat pertama saja.
 */
export function ringkasPembuka(
  bagian: readonly BagianPembuka[] | null | undefined,
): string | null {
  const b0 = bagian?.[0];
  if (!b0 || b0.jenis !== "prosa" || !b0.blok || b0.blok.length === 0) return null;
  const teks: string[] = [];
  for (const [j, x] of b0.blok.entries()) {
    if (x.jenis !== "teks" || x.peran === "jebakan") break;
    const t = (x.teks ?? "").trim();
    if (j > 0 && !(x.peran === "" || x.peran === undefined)) break;
    if (j > 0 && !(t.length >= MIN_LANJUTAN && AKHIR.test(t))) break;
    teks.push(t);
  }
  if (teks.length === 0) return null;
  const kalimat = pecahKalimat(teks.join(" "));
  // Blok pembuka kosong atau hanya spasi: tidak ada kalimat untuk diringkas.
  // Tanpa ini `kalimat[0]` di bawah `undefined` dan satu materi baru dengan
  // paragraf pembuka kosong melempar di tengah render (tidak ada error
  // boundary: seluruh pohon React kosong sampai muat ulang).
  if (kalimat.length === 0) return null;
  const utuh = kalimat.filter((k) => !k.endsWith(":"));
  if (utuh.length > 0 && utuh.length === kalimat.length) return rakit(kalimat);
  if (utuh.length > 0) return rakit(utuh);
  const k0 = (kalimat[0] as string).slice(0, -1).trimEnd() + ".";
  return rakit([k0]);
}

/** Kata tombol aksi utama. Bergantung status; terkunci tidak punya aksi baca. */
export function kataAksiBaca(status: StatusBintang): string | null {
  switch (status) {
    case "selesai":
      return "Baca lagi";
    case "sebagian":
      return "Lanjutkan membaca";
    case "baru":
      return "Mulai membaca";
    case "terkunci":
      return null;
  }
}

/** Kata kapsul penanda saran di peta dan Daftar, diturunkan dari status bintang
 *  sasarannya: yang pernah dibuka sebagian = "Lanjutkan di sini", yang lain
 *  (belum dibaca) = "Mulai di sini". Dulu kata itu diturunkan dari XP, sehingga
 *  pelajar ber-XP yang saran berikutnya sebuah materi baru melihat "Lanjutkan"
 *  untuk bintang yang belum pernah ia buka. Kapsul tidak pernah menunjuk
 *  bintang terkunci. */
export function kataMulai(status: StatusBintang): string {
  return status === "sebagian" ? "Lanjutkan di sini" : "Mulai di sini";
}

/** "1 dari 3 materi di bab ini sudah dibaca": dihitung dari status bintang di
 *  `/api/langit` (sebagian TIDAK dihitung selesai, sama dengan `pelajar/bab.py`). */
export function hitungBab(
  materi: ReadonlyArray<{ status: string }>,
  anggota: readonly number[],
): { selesai: number; jumlah: number; persen: number } {
  const jumlah = anggota.length;
  const selesai = anggota.filter((i) => materi[i]?.status === "selesai").length;
  return { selesai, jumlah, persen: jumlah ? Math.round((100 * selesai) / jumlah) : 0 };
}

/**
 * Nama aksesibel satu bintang di lensa: nomor, judul, status, lalu penanda
 * yang di layar HANYA visual ("berikutnya" = braket dan lencana, "cocok
 * dengan X" = cincin). Penanda yang tidak masuk nama tidak ada bagi pembaca
 * layar. Kurikulum dan bab TIDAK diulang di tiap nama: ia datang dari
 * `listbox` ("Bintang HTML: 23 materi") dan `group` bab di atasnya, dan
 * diumumkan sekali saat fokus masuk.
 */
export function labelBintang(o: {
  indeks: number;
  judul: string;
  status: StatusBintang;
  berikutnya: boolean;
  konsepCocok: string | null;
}): string {
  return (
    `${o.indeks + 1}. ${tanpaNomor(o.judul)}, ${KATA_STATUS_BINTANG[o.status]}` +
    (o.berikutnya ? ", berikutnya" : "") +
    (o.konsepCocok ? `, cocok dengan ${o.konsepCocok}` : "")
  );
}

/**
 * Nama aksesibel tautan rasi di ikhtisar (dan baris di Daftar). Dua hal yang
 * di layar hanya VISUAL harus masuk nama: cincin konsep ("N materi cocok
 * dengan X") dan jalur profesi ("bagian bekal Y"). Tanpa keduanya hasil
 * saringan konsep dan profesi tidak ada bagi pembaca layar: tiga puluh dua
 * nama yang sama sebelum dan sesudah saringan menyala. Nama diawali teks yang
 * terlihat ("Python 0/44") supaya kontrol suara yang menyebut label itu
 * menemukannya (WCAG 2.5.3). Konsep tanpa satu pun kecocokan di rasi ini tidak
 * disebut: cincinnya juga tidak digambar.
 */
export function labelRasi(o: {
  label: string;
  selesai: number;
  jumlah: number;
  konsep: string | null;
  cocok: number;
  profesi: string | null;
  bekal: boolean;
}): string {
  return (
    `${o.label} ${o.selesai}/${o.jumlah}: ${o.selesai} dari ${o.jumlah} materi sudah dibaca` +
    (o.konsep && o.cocok > 0 ? `, ${o.cocok} materi cocok dengan ${o.konsep}` : "") +
    (o.profesi && o.bekal ? `, bagian bekal ${o.profesi}` : "") +
    ". Perbesar rasi."
  );
}

/**
 * Kalimat `role=status` ketika sebuah bintang dipilih. Untuk bintang terkunci
 * kalimat alasan milik server (`pelajar/bab.py`) ikut dibacakan bila sudah
 * tiba: alasannya satu-satunya hal yang bisa dilakukan pelajar atas bintang
 * itu, dan dulu hanya ada di paragraf panel yang bukan perhentian Tab.
 */
export function kalimatDipilih(o: {
  judul: string;
  status: StatusBintang;
  alasan?: string | null;
}): string {
  return (
    `Dipilih: ${tanpaNomor(o.judul)}, ${KATA_STATUS_BINTANG[o.status]}.` +
    (o.status === "terkunci" && o.alasan ? ` ${o.alasan}` : "")
  );
}

/** Pecah satu baris prosa di tanda `\`` jadi bagian biasa dan bagian kode,
 *  tanpa tanda itu sendiri. Pembaca materi menggambar `kode` sebagai
 *  <code>; panel yang mencetak teks mentah menampilkan backtick (6 dari 1.062
 *  paragraf pembuka). Tanda yang tidak berpasangan dibuang, bukan dicetak. */
export function pecahKode(teks: string): Array<{ teks: string; kode: boolean }> {
  const bagian = teks.split("`");
  const keluar: Array<{ teks: string; kode: boolean }> = [];
  bagian.forEach((b, i) => {
    if (b === "") return;
    // Bagian ganjil di antara sepasang tanda adalah kode; bagian terakhir
    // pada jumlah tanda ganjil tidak punya penutup, jadi tetap biasa.
    const kode = i % 2 === 1 && i < bagian.length - 1;
    keluar.push({ teks: b, kode });
  });
  return keluar;
}

/** Penunjuk sebuah alamat Langit: `#/langit/html/13` -> `{ key: "html",
 *  indeks: 13 }`. `null` untuk alamat yang bukan Langit, dan untuk alamat
 *  dengan persen-sandi rusak (`#/langit/%`): `decodeURIComponent` melempar
 *  `URIError`, dan tanpa penjaga satu fragmen yang terpotong dari chat
 *  mengosongkan SELURUH pohon React (tidak ada error boundary). Kunci
 *  kurikulum hanya `[a-z0-9]`, jadi alamat rusak diperlakukan seperti kunci
 *  yang tak dikenal. Nomor bintang hanya bilangan bulat tak negatif utuh:
 *  `/1.5` dan `/1e3` dulu membuka bintang 2 (`\d+` menelan angka depannya),
 *  sekarang ekor itu diabaikan seperti `/abc`. */
export function bacaAlamat(hash: string): { key: string; indeks: number | null } | null {
  const m = /^#\/langit\/([^/?#]+)(?:\/(\d+)(?![\w.]))?/.exec(hash);
  if (!m) return null;
  let key = m[1] as string;
  try {
    key = decodeURIComponent(key);
  } catch {
    return null;
  }
  return { key, indeks: m[2] === undefined ? null : Number(m[2]) };
}
