/** Bagian MURNI peta langit: benih, magnitudo, dan letak bintangnya.
 *
 *  Dipisah dari penggambarnya karena di sinilah kerusakan yang paling sulit
 *  dilihat bisa terjadi: satu bit yang meleset di `prng` menggeser SETIAP
 *  bintang, dan yang terlihat tetap "langit berbintang" -- cuma langit yang
 *  berbeda, tanpa satu pun error. Alasan yang sama membuat `rasi-geometri.ts`
 *  dipisah dari `Rasi.tsx`, dan pembandingnya mengadu bagian ini dengan
 *  `langit.js` yang masih melayani antarmuka lama.
 *
 *  Benihnya tetap (1801, tahun Uranographia), jadi langitnya SAMA setiap kali
 *  dibuka. Itu bukan detail: langit yang diacak ulang tiap pemuatan terbaca
 *  sebagai semburan titik baru, bukan sebagai tempat yang sama.
 */

export interface Bintang {
  x: number;
  y: number;
  mag: number;
  fase: number;
  hangat: boolean;
}

/** mulberry32. Disalin apa adanya dari `langit.js`; angkanya kontrak. */
export function prng(benih: number): () => number {
  let b = benih;
  return () => {
    b |= 0;
    b = (b + 0x6d2b79f5) | 0;
    let t = Math.imul(b ^ (b >>> 15), 1 | b);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** Rumus ukuran d3-celestial: bintang terang jarang, yang redup banyak. */
export const jariMag = (mag: number): number => 7 * Math.exp(-0.28 * (mag + 2));

/** Sebaran bintang untuk kanvas selebar `lebar` x `tinggi`.
 *
 *  Distribusi magnitudonya condong ke redup -- kelas 6 paling banyak --
 *  karena itulah yang terjadi di langit sungguhan, dan langit yang
 *  magnitudonya rata terbaca sebagai kisi titik.
 */
export function bangkitkanBintang(lebar: number, tinggi: number): Bintang[] {
  const acak = prng(1801);
  const jumlah = Math.round((lebar * tinggi) / 5200);
  const bintang: Bintang[] = [];
  for (let i = 0; i < jumlah; i++) {
    const u = acak();
    const mag = u < 0.02 ? 1
      : u < 0.06 ? 2
      : u < 0.14 ? 3
      : u < 0.30 ? 4
      : u < 0.58 ? 5
      : 6;
    bintang.push({
      x: acak() * lebar,
      y: acak() * tinggi,
      mag,
      fase: acak() * Math.PI * 2,
      hangat: acak() < 0.18,
    });
  }
  return bintang;
}

/** Tiga puluh bintang paling terang: yang berkelip, dan hanya itu. */
export const bintangTerang = (bintang: Bintang[]): Bintang[] =>
  bintang.filter((b) => b.mag <= 2).slice(0, 30);
