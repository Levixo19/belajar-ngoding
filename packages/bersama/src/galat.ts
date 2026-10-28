/* Menerjemahkan pesan error compiler/runtime. Port dari `inti/galat.py`.
 *
 * Tabel polanya TIDAK ditulis di sini: seluruhnya dihasilkan
 * `alat/ekspor_bersama.py` ke `../data/pola-galat.json`. Setiap pola yang
 * diketik ulang adalah satu kesempatan lagi untuk menyimpang, dan
 * menyimpangnya tidak menimbulkan error -- cuma satu pesan error yang kembali
 * tampil mentah kepada orang yang justru paling tidak bisa membacanya.
 *
 * Yang tetap ditulis di sini cuma ALGORITMANYA, dan satu hal yang harus
 * diketahui saat menambah pola BARU di `inti/galat.py`: `\w` di Python
 * mencakup huruf Unicode, di JavaScript cuma ASCII. Pola yang ada hari ini
 * memakainya untuk nama pengenal dan nama tag -- semuanya ASCII -- jadi
 * hasilnya sama. Pola baru yang perlu mencocokkan huruf berdiakritik tidak
 * boleh mengandalkan `\w`.
 */

import tabel from "../data/pola-galat.json" with { type: "json" };

interface PolaMentah {
  pola: string;
  ganti: string;
}

const BENDERA = tabel.bendera as string;

/* Dikompilasi sekali. `RegExp` tanpa bendera `g` berarti `exec` tidak menyimpan
 * `lastIndex`, jadi objek yang sama aman dipakai ulang lintas pemanggilan --
 * dengan `g` ia akan melanjutkan dari posisi terakhir dan melewatkan kecocokan
 * pada pesan berikutnya, dan gejalanya penjelasan yang muncul atau hilang
 * tergantung pesan mana yang diterjemahkan sebelumnya. */
const TERKOMPILASI: Array<{ re: RegExp; ganti: string }> = (
  tabel.pola as PolaMentah[]
).map((p) => ({ re: new RegExp(p.pola, BENDERA), ganti: p.ganti }));

/**
 * Daftar penjelasan berbahasa Indonesia untuk sebuah pesan error.
 *
 * Kosong kalau tidak ada pola yang cocok -- pemanggil TETAP wajib menampilkan
 * pesan aslinya. Menebak-nebak lebih berbahaya daripada diam.
 */
export function terjemahkan(galat: string | null | undefined, maks = 3): string[] {
  if (!galat || !galat.trim()) return [];

  const keluar: string[] = [];
  for (const { re, ganti } of TERKOMPILASI) {
    const cocok = re.exec(galat);
    if (!cocok) continue;
    // Penggantinya dikenakan pada TEKS YANG COCOK, bukan pada seluruh pesan:
    // itu yang membuat `$1` menunjuk grup di dalam kecocokan itu, dan yang
    // membuat satu pesan panjang tidak ikut terbawa ke dalam penjelasannya.
    const teks = cocok[0].replace(re, ganti).trim().split(/\s+/).join(" ");
    if (!keluar.includes(teks)) keluar.push(teks);
    if (keluar.length >= maks) break;
  }
  return keluar;
}

const RAPIKAN = tabel.rapikan as {
  path: string;
  baris_berkas: string;
  kata_line: string;
};

/* Ketiganya `g`: `re.sub` di Python mengganti SEMUA kecocokan, dan sebuah
 * pesan kompiler biasanya menyebut jalurnya lebih dari sekali. */
const RE_PATH = new RegExp(RAPIKAN.path, "g");
const RE_BARIS_BERKAS = new RegExp(RAPIKAN.baris_berkas, "g");
const RE_KATA_LINE = new RegExp(RAPIKAN.kata_line, "g");

/**
 * Bersihkan pesan error mentah supaya cocok dengan berkas milik pelajar.
 *
 * Jalur direktori sementara diganti nama berkas kerjanya, dan nomor baris
 * digeser mundur sebanyak baris `setup` yang ditempel runner -- sehingga
 * "baris 15" menunjuk baris 1 di berkas pelajar yang isinya memang cuma satu
 * baris. Tanpa itu, pesan error menunjuk ke tempat yang tidak ada di layarnya.
 */
export function rapikan(
  galat: string | null | undefined,
  namaBerkas = "",
  barisSetup = 0,
): string {
  if (!galat) return galat ?? "";

  let teks = galat.replace(RE_PATH, (_cocok, g1: string) => namaBerkas || g1);
  if (barisSetup <= 0) return teks;

  const geser = (_cocok: string, g1: string, g2: string) => {
    const baru = parseInt(g2, 10) - barisSetup;
    if (baru < 1) return `${g1}[bagian KONDISI AWAL]`;
    return `${g1}${baru}`;
  };

  teks = teks.replace(RE_BARIS_BERKAS, geser);
  return teks.replace(RE_KATA_LINE, geser);
}

/** Ambil bagian paling berguna dari pesan error yang panjang. */
export function ringkas(galat: string | null | undefined, maksBaris = 12): string[] {
  // `str.splitlines()` Python memecah pada lebih banyak pemisah daripada ini
  // (form feed, U+2028, ...). Keluaran compiler dan runtime tidak pernah
  // memakainya, dan menirukan daftar lengkapnya berarti menyalin tabel yang
  // tidak ada yang bisa mengujinya.
  const baris = (galat ?? "").split(/\r\n|\r|\n/).filter((b) => b.trim());
  if (baris.length <= maksBaris) return baris;
  // Traceback Python paling berguna di bagian AKHIR; keluaran kompiler di AWAL.
  if (baris.slice(0, 3).some((b) => b.includes("Traceback"))) {
    return ["...(bagian awal disingkat)", ...baris.slice(-(maksBaris - 1))];
  }
  return [
    ...baris.slice(0, maksBaris - 1),
    `...(${baris.length - maksBaris + 1} baris lagi)`,
  ];
}
