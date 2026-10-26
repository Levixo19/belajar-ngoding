/* Tabel pintasan papan ketik. Port `PINTASAN_G` dari `aplikasi.js` dan
 * `PINTASAN` dari `layar-lain.js`.
 *
 * Dipisahkan dari `Pintasan.tsx` karena DUA pembaca memerlukannya dan salah
 * satunya murni: penangan papan ketik beserta dialognya (`.tsx`), dan palet
 * perintah yang menitipkan label `<kbd>` ke tiap butirnya (`palet-cari.ts`,
 * yang diadu pembanding `.mjs` -- dan `.mjs` tidak bisa mengimpor `.tsx`).
 *
 * **Ini SATU definisi untuk ketiga pembaca itu.** Di sisi JS huruf-huruf itu
 * pernah ditulis di tiga tempat (penangan, palet, dan tabel prosa), dan akibat
 * rumusan yang melenceng bisa disebut: huruf yang dipindah di satu tempat
 * membuat tempat lain menjanjikan halaman yang berbeda, tanpa satu pun tes
 * gagal.
 */

/** Huruf `G lalu <huruf>` dan alamat yang dibukanya. SATU definisi. */
export const PINTASAN_G: Record<string, string> = {
  d: "#/dasbor",
  c: "#/coba",
  s: "#/statistik",
  b: "#/bookmark",
  n: "#/catatan",
  p: "#/atur",
};

/** Daftar lengkap untuk dialog bantuan. */
export const PINTASAN: Array<[string, string]> = [
  ["Ctrl K", "Palet perintah: lompat ke mana saja"],
  ["Ctrl B", "Buka / tutup menu"],
  ["Ctrl J", "Ganti tema"],
  ["G lalu D", "Ke dasbor"],
  ["G lalu C", "Ke ruang coba"],
  ["G lalu S", "Ke statistik"],
  ["G lalu B", "Ke bookmark"],
  ["G lalu N", "Ke catatanku"],
  ["G lalu P", "Ke pengaturan"],
  ["?", "Tampilkan daftar ini"],
  ["Esc", "Tutup dialog"],
  ["1-9 atau A-J", "Menjawab soal kuis"],
  ["Ctrl ⏎", "Jalankan kode di editor"],
  ["Ctrl ⇧ ⏎", "Periksa jawaban latihan"],
  ["Ctrl S", "Simpan kode"],
  ["Ctrl /", "Komentari baris di editor"],
  ["Tab atau ⇧ Tab", "Tambah atau kurangi indentasi"],
  ["j", "Blok kode berikutnya (di halaman materi)"],
  ["k", "Blok kode sebelumnya (di halaman materi)"],
  ["]", "Bagian berikutnya (di halaman materi)"],
  ["[", "Bagian sebelumnya (di halaman materi)"],
  ["f", "Mode fokus (di halaman materi)"],
  ["⏎", "Jalankan blok kode yang sedang difokus"],
];

/**
 * Label pintasan untuk `href`, atau `null` kalau tujuan itu tidak punya.
 *
 * Pencariannya lewat ALAMAT, bukan lewat urutan daftar dan bukan lewat label.
 * Keduanya justru satu-satunya dua hal yang TIDAK menentukan ke mana sebuah
 * butir membawa orang: urutan daftar perintah boleh berubah dan labelnya boleh
 * ditulis ulang tanpa satu pun pintasan berpindah.
 *
 * Rumusannya ("G lalu D") sengaja sama persis dengan ruas tombol di tabel
 * `PINTASAN` di atas. Dua permukaan yang menyebut pintasan yang sama dengan
 * dua rumusan adalah dua permukaan yang suatu hari berbeda, dan yang
 * membacanya tidak punya cara tahu mana yang benar.
 *
 * Yang tidak ada di peta mengembalikan `null`, dan itu keadaan WAJAR, bukan
 * cacat: "Catatanku" punya pintasan, tiga puluh dua bahasa tidak, dan hasil
 * pencarian juga tidak. Butir tanpa pintasan cuma tidak menggambar `<kbd>`.
 */
export function labelPintasan(href: string): string | null {
  for (const huruf of Object.keys(PINTASAN_G)) {
    if (PINTASAN_G[huruf] === href) return "G lalu " + huruf.toUpperCase();
  }
  return null;
}
