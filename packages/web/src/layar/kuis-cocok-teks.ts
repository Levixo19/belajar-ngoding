/* Hitungan dan kalimat murni kuis kecocokan Peta Karier. Nol rujukan ke
 * `document` atau React, supaya bisa dites langsung lewat pelucut tipe Node.
 *
 * Yang dikunci di sini adalah keputusan yang membuat kuis ini tidak
 * membingungkan, masing-masing dengan sebabnya:
 *
 * 1. SATU tombol maju yang jujur. Kuis lama menampilkan enam soal sekaligus dan
 *    satu tombol yang mati sampai tiga soal terjawab, tanpa menyebut sebabnya.
 *    Di sini tombol majunya berganti arti menurut keadaan (lewati, lanjut,
 *    lihat hasil, atau pergi ke soal yang belum dijawab), dan tidak pernah ada
 *    tombol yang berujung penolakan.
 * 2. Syarat minimum disebut dengan angkanya ("Jawab 2 soal lagi"), bukan
 *    disembunyikan di balik tombol yang mati.
 * 3. Kalimat "makin banyak soal terjawab, makin jelas arahnya" memang benar:
 *    skor tiap profesi adalah jumlah bobot jawaban, jadi sedikit jawaban
 *    memberi banyak profesi yang berimbang. Ia bukan dorongan untuk
 *    menyelesaikan kuis.
 */

/** Jawaban minimum sebelum hasil ditawarkan. Di bawah ini hasilnya lebih mirip
 *  tebakan daripada saran. */
export const MIN_JAWABAN = 3;

export type Jawaban = ReadonlyArray<number | null>;

export function jumlahDijawab(j: Jawaban): number {
  return j.filter((x) => x !== null).length;
}

/** Berapa soal lagi sebelum hasil bisa dilihat; 0 bila sudah cukup. */
export function sisaJawaban(j: Jawaban): number {
  return Math.max(0, MIN_JAWABAN - jumlahDijawab(j));
}

/** Indeks soal pertama yang belum dijawab, mulai dari `dari` lalu berputar ke
 *  awal. `null` bila semuanya sudah dijawab. */
export function soalBelumDijawab(j: Jawaban, dari = 0): number | null {
  const n = j.length;
  for (let k = 0; k < n; k++) {
    const i = (((dari + k) % n) + n) % n;
    if (j[i] === null) return i;
  }
  return null;
}

/** Kalimat di bawah daftar jawaban. */
export function kalimatSisa(j: Jawaban): string {
  const sisa = sisaJawaban(j);
  if (sisa > 0) return `Jawab ${sisa} soal lagi untuk melihat yang cocok.`;
  if (jumlahDijawab(j) < j.length) return "Makin banyak soal terjawab, makin jelas arahnya.";
  return "Semua soal sudah terjawab.";
}

export type AksiMaju =
  | { jenis: "lewati" }
  | { jenis: "lanjut" }
  | { jenis: "hasil" }
  | { jenis: "belum"; ke: number };

/** Apa yang dilakukan tombol maju di soal `aktif`. Di soal terakhir tombol ini
 *  menawarkan hasil bila jawabannya cukup, dan kalau belum cukup mengantar ke
 *  soal yang belum dijawab: tidak pernah buntu. */
export function aksiMaju(j: Jawaban, aktif: number): AksiMaju {
  if (aktif < j.length - 1) {
    return j[aktif] === null ? { jenis: "lewati" } : { jenis: "lanjut" };
  }
  if (sisaJawaban(j) === 0) return { jenis: "hasil" };
  const ke = soalBelumDijawab(j, 0);
  return ke === null ? { jenis: "hasil" } : { jenis: "belum", ke };
}

export function labelAksiMaju(a: AksiMaju): string {
  switch (a.jenis) {
    case "lewati": return "Lewati soal ini";
    case "lanjut": return "Lanjut";
    case "hasil": return "Lihat yang cocok";
    case "belum": return `Ke soal ${a.ke + 1} yang belum dijawab`;
  }
}

/** "01", "02", ...: nomor soal di judul dan daftar jawaban. */
export function nomorSoal(i: number): string {
  return String(i + 1).padStart(2, "0");
}

/** Nilai kueri `pilihan` untuk `GET /api/karier/kuis`: kosong = dilewati. */
export function parameterPilihan(j: Jawaban): string {
  return j.map((x) => (x === null ? "" : String(x))).join(",");
}

/** Nama keahlian untuk dibaca orang; id yang tidak dikenal tampil apa adanya
 *  (lebih baik terbaca ganjil daripada hilang). */
export function namaKeahlian(ids: readonly string[], peta: Readonly<Record<string, string>>): string {
  return ids.map((k) => peta[k] ?? k).join(", ");
}

const BILANGAN = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan", "Sepuluh"];

/** Bilangan 1 sampai 10 sebagai kata berhuruf kapital awal; di luar itu angka.
 *  Jumlah soal dihitung dari data, bukan diketik, jadi kalimatnya ikut benar
 *  kalau kuisnya bertambah. */
export function bilanganKata(n: number): string {
  return BILANGAN[n] && n >= 1 ? (BILANGAN[n] as string) : String(n);
}

/** Judul hasil menurut banyaknya profesi yang dikembalikan server. */
export function judulHasil(banyak: number): string {
  if (banyak <= 0) return "Belum ada arah yang jelas";
  return `${bilanganKata(Math.min(banyak, 3))} arah yang paling dekat dengan jawabanmu`;
}
