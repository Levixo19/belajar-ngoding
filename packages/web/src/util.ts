/* Pembantu murni yang dipakai beberapa layar, TANPA JSX.
 *
 * Pemisahannya dari `util.tsx` punya sebab teknis, bukan selera: Node melucuti
 * TIPE dari `.ts` tapi tidak melucuti JSX dari `.tsx`. Pembanding `.mjs`
 * karena itu cuma bisa mengimpor berkas `.ts` -- dan bagian murni yang mereka
 * adu (`dasbor-teks.ts`, `bahasa-teks.ts`, ...) butuh `angka()`. Sebelum ini
 * ia tinggal di `util.tsx` bersama `tandai()` yang memang mengembalikan JSX,
 * jadi satu fungsi berisi satu `toLocaleString` menyeret seluruh React ke
 * dalam pembanding yang tidak pernah merender apa pun.
 *
 * `util.tsx` meneruskan ketiganya, jadi tidak ada satu pun impor lama yang
 * perlu diubah.
 */

/** Angka dengan pemisah ribuan Indonesia. */
export function angka(n: number | string | null | undefined): string {
  return (Number(n) || 0).toLocaleString("id-ID");
}

/**
 * URL yang boleh dipasang sebagai `href`. `null` kalau tidak.
 *
 * Ini PAGAR, bukan pembersih kosmetik, dan harus tetap seketat versi JS-nya.
 * Tautan Pustaka datang dari berkas data hasil panen, dan satu `javascript:`
 * yang lolos ke `href` berarti kode asing berjalan di halaman yang memegang
 * token API aplikasi ini. Yang diizinkan hanya http dan https.
 */
export function urlAman(u: unknown): string | null {
  return typeof u === "string" && /^https?:\/\//i.test(u.trim()) ? u : null;
}

/** Buang awalan nomor dari judul materi ("12. Variabel" -> "Variabel"). */
export function tanpaNomor(t: string): string {
  return t.replace(/^\s*\d+\.\s*/, "");
}
