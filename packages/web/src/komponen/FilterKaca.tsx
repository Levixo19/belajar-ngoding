/* Filter SVG untuk tombol kaca (`.tbl-kaca` di gaya.css). Dipasang SEKALI oleh
 * `Cangkang.tsx`; yang memakainya CSS lewat `backdrop-filter: url(#tbl-kaca)`.
 *
 * Mekanismenya dari komponen "Liquid Glass Button" milik `designali-in` di
 * 21st.dev (dibaca dari bundelnya lewat REA): derau fraktal berfrekuensi rendah
 * dihaluskan, dipakai sebagai peta pergeseran atas isi di belakang tombol, lalu
 * hasilnya diburamkan sedikit. Hasilnya tombol tampak seperti kaca tebal yang
 * membelokkan apa pun di belakangnya. Selebihnya ditulis ulang di sini: yang asli
 * berupa kelas Tailwind dan memuat satu filter per tombol; di sini satu filter
 * untuk semua tombol, dan pergeserannya jauh lebih kecil karena tombolnya
 * setinggi 44 sampai 52 piksel (yang asli 70, untuk tombol yang lebih besar dan
 * latar yang berupa gambar).
 *
 * Aturan yang gampang terbalik:
 *  - `width="0" height="0"` dengan posisi absolut, BUKAN `display: none`: filter di
 *    dalam elemen yang tidak digambar tidak terpakai oleh peramban.
 *  - `x`, `y`, `width`, `height` filter dalam persen kotak elemen yang
 *    memakainya, jadi satu filter cocok untuk tombol selebar apa pun.
 *  - Komponen ini TIDAK punya logika dan tidak membaca tingkat gerak: filternya
 *    statis. Yang bergerak (skala saat disorot) ada di CSS dan tunduk pada
 *    `prefers-reduced-motion` di sana.
 *
 * Pembiasan latar hanya jalan di Chromium. CSS memasangnya di balik
 * `@supports (backdrop-filter: url(#a))`, jadi peramban lain mendapat tombol
 * bertinta tanpa pembiasan, bukan deklarasi yang gugur dan menyeret tintanya.
 *
 * LISENSI, dan ini beda dari komponen navbar: halaman komponen asalnya di
 * 21st.dev mencantumkan penulis (Ali Imam, `designali-in`) tetapi bidang
 * lisensinya KOSONG. Tanpa lisensi tertulis kodenya tidak boleh disalin, jadi
 * TIDAK ada satu baris pun yang disalin: yang dipakai hanya teknik umum (rantai
 * filter derau, pergeseran, blur; tumpukan bayangan dalam untuk tepi kaca),
 * ditulis ulang dengan nilai dan susunan sendiri. Komponen navbar yang
 * berlisensi MIT punya kredit dan teks izinnya di `TetesKaca.tsx`. */

/** Seberapa jauh isi di belakang tombol digeser (piksel). */
const GESER = 26;

export function FilterKaca() {
  return (
    <svg className="tbl-kaca-filter" width="0" height="0" aria-hidden="true" focusable="false">
      <filter id="tbl-kaca" x="0" y="0" width="100%" height="100%" colorInterpolationFilters="sRGB">
        <feTurbulence type="fractalNoise" baseFrequency="0.05 0.05" numOctaves={1} seed={1} result="derau" />
        <feGaussianBlur in="derau" stdDeviation="2" result="derauHalus" />
        <feDisplacementMap
          in="SourceGraphic" in2="derauHalus" scale={GESER}
          xChannelSelector="R" yChannelSelector="B" result="bergeser"
        />
        <feGaussianBlur in="bergeser" stdDeviation="2" />
      </filter>
    </svg>
  );
}
