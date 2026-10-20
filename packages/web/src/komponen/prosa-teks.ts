/* Bagian MURNI prosa: kata mana di tengah kalimat dikotaki sebagai kode.
 *
 * Dipisahkan dari `Prosa.tsx` karena Node melucuti TIPE dari `.ts` tapi tidak
 * melucuti JSX dari `.tsx` -- jadi hanya berkas ini yang bisa diimpor
 * `uji/banding-prosa.mjs` dan diadu dengan `berkode` di `layar-belajar.js`.
 * Pola yang sama dengan `editor-teks.ts`, `pratinjau-css.ts`,
 * `visual-bentuk.ts`, `jejak-teks.ts`, dan `kerja-beda.ts`.
 */

/* Kata yang DIKOTAKI sebagai kode di tengah prosa.
 *
 * Polanya sengaja cuma yang MUSTAHIL jadi kata Indonesia biasa: kurung sudut,
 * tanda kurung kosong, tanda sama dengan berkutip, akhiran berkas, dan `kode`.
 * Properti CSS telanjang seperti `color` atau `grid` TIDAK ikut -- kata-kata
 * itu muncul sebagai kata biasa di kalimat Indonesia, dan menandainya sebagai
 * kode berarti menaruh kotak di tengah kalimat yang bukan kode.
 *
 * Hasilnya 1.123 chip di seluruh kurikulum, dan 87% blok prosa tidak
 * memilikinya sama sekali. Itu yang membuatnya jadi penanda: kalau setiap
 * paragraf punya, tidak ada yang punya. */
const POLA_KODE = new RegExp(
  "`[^`]+`|</?[a-zA-Z][\\w-]*\\s*/?>"             // `kode` <tag> </tag> <br/>
  + "|\\b[a-zA-Z_][\\w.]*\\(\\)"                    // fungsi()
  + "|\\b[a-zA-Z-]+=\"[^\"]{1,30}\""              // atribut="nilai"
  + "|\\b[\\w-]+\\.(?:py|js|java|c|cpp|h|css|html|sql|sh|go|json|txt|md)\\b",
  "g");

/** Potongan teks prosa: teks biasa, atau sebuah chip kode. */
export type SegmenProsa = string | { kode: true; teks: string };

/**
 * Teks -> potongan, dengan bagian yang jadi `<code>` ditandai.
 *
 * Backtick DIBUANG dari isi chip-nya: terminal memakai backtick sebagai
 * penanda, web memakai kotak, dan isinya sama.
 *
 * `lastIndex` disetel nol di tiap panggilan. Untuk bentuk loop yang SEKARANG
 * ia tidak pernah mengubah apa pun: loopnya selalu jalan sampai `exec`
 * mengembalikan `null`, dan di situ mesin regex sudah menyetel `lastIndex`
 * kembali ke nol sendiri. Diukur, bukan diduga -- baterai mutasi yang
 * menemukannya, lewat sel yang mencabut reset ini dan tetap hijau atas 153.959
 * baris prosa.
 *
 * Ia DIPERTAHANKAN karena yang dijaganya bentuk loop BERIKUTNYA: polanya
 * ber-bendera `g` dan dibagi antar panggilan, jadi satu `break` yang
 * ditambahkan di tengah loop -- misalnya atap jumlah chip per paragraf --
 * langsung membuat hasilnya bergantung pada teks yang dipindai SEBELUMNYA.
 * Paragraf yang sama akan dikotaki berbeda tergantung urutan rendernya, dan
 * tidak ada error di mana pun.
 */
export function segmenKode(teks: string): SegmenProsa[] {
  const keluar: SegmenProsa[] = [];
  let akhir = 0;
  POLA_KODE.lastIndex = 0;
  let m: RegExpExecArray | null;
  while ((m = POLA_KODE.exec(teks)) !== null) {
    if (m.index > akhir) keluar.push(teks.slice(akhir, m.index));
    const cocok = m[0];
    keluar.push({
      kode: true,
      teks: cocok.charAt(0) === "`" ? cocok.slice(1, -1) : cocok,
    });
    akhir = m.index + cocok.length;
  }
  if (!keluar.length) return [teks];
  if (akhir < teks.length) keluar.push(teks.slice(akhir));
  return keluar;
}
