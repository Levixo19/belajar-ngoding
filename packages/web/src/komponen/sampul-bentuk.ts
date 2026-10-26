/** Bagian MURNI sampul: komposisi geometris yang dibangkitkan dari sebuah teks.
 *
 *  Port `webapp/statik/js/sampul.js`. Pemilik meminta gambar ("no one wants to
 *  see website full tulisan"), dan aplikasi ini wajib utuh tanpa internet --
 *  jadi gambarnya tidak diambil dari mana pun: tiap bahasa, bab, dan profesi
 *  mendapat komposisi yang dibangkitkan dari namanya sendiri. Teks yang sama
 *  selalu memberi gambar yang sama, jadi sampul HTML hari ini sama dengan
 *  sampul HTML bulan depan.
 *
 *  Yang dikembalikan DESKRIPTOR (`{tag, sifat}`), bukan elemen DOM. Dua
 *  sebabnya: komponennya bisa merendernya sebagai JSX tanpa menyentuh
 *  `document`, dan pembandingnya bisa mengadu bentuknya dengan `sampul.js`
 *  tanpa memuat satu pun DOM sungguhan. Di sinilah kerusakan paling sulit
 *  dilihat bisa terjadi -- satu bit meleset di `benih` mengubah SETIAP sampul,
 *  dan yang terlihat tetap "gambar geometris", cuma gambar yang lain.
 *
 *  Gambar ini HIASAN: `aria-hidden`, tidak bisa difokus, dan tidak pernah jadi
 *  satu-satunya pembawa informasi.
 */

export interface Bentuk {
  tag: string;
  sifat: Record<string, string | number>;
  teks?: string;
}

/* Rona identitas per kunci bahasa (derajat HSL). Bahasa yang tidak ada di
   sini mendapat rona dari hash namanya. */
const RONA: Record<string, number> = {
  html: 16, css: 205, javascript: 46, typescript: 212, python: 52, java: 14,
  c: 222, cpp: 232, go: 190, rust: 22, php: 245, ruby: 352, kotlin: 268,
  sql: 196, bash: 135, git: 10, fedora: 214, aplikasi: 32, csharp: 275,
  vb: 238,
};

/* Akhiran berkas atau isyarat pendek tiap kurikulum, digambar besar dan samar
   di sudut. Inilah yang membuat sampul Python terbaca "Python" sebelum
   namanya dibaca. */
const TANDA: Record<string, string> = {
  html: "</>", css: "{ }", javascript: ".js", typescript: ".ts", python: ".py",
  java: ".java", c: ".c", cpp: ".cpp", go: ".go", rust: ".rs", php: ".php",
  ruby: ".rb", kotlin: ".kt", sql: ".sql", bash: ".sh", git: "git",
  fedora: "$_", aplikasi: "app", csharp: ".cs", vb: ".vb",
};

/* Saturasi & kecerahan dibaca dari CSS supaya tema terang bisa menggelapkan
   warnanya tanpa menggambar ulang sampulnya. */
const warnaRona = (rona: number) =>
  `hsl(${rona} var(--sampul-s, 44%) var(--sampul-l, 58%))`;

export function benih(teks: string): number {
  let h = 2166136261;
  for (let i = 0; i < teks.length; i++) {
    h ^= teks.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/** mulberry32: PRNG kecil berbenih, cukup untuk tata letak hiasan. */
export function acak(benihAwal: number): () => number {
  let a = benihAwal || 1;
  return () => {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const r1 = (n: number) => Math.round(n * 10) / 10;

interface Warna { utama: string }
type Ragam = (rng: () => number, w: number, h: number, c: Warna) => Bentuk[];

/* Empat ragam komposisi, masing-masing memakai SEDIKIT bentuk besar: sampul
   yang ramai berhenti terbaca sebagai satu benda. */
const RAGAM: Record<string, Ragam> = {
  orbit(rng, w, h, c) {
    const cx = w * (0.55 + rng() * 0.3);
    const cy = h * (0.35 + rng() * 0.4);
    const out: Bentuk[] = [];
    const n = 4 + Math.floor(rng() * 3);
    for (let i = n; i >= 1; i--) {
      const r = (Math.min(w, h) * 0.17) * i;
      out.push({ tag: "circle", sifat: {
        cx: r1(cx), cy: r1(cy), r: r1(r), fill: "none",
        style: `stroke: ${i === 2 ? "var(--nyala)" : c.utama}`,
        "stroke-width": i === 2 ? 2 : 1.2,
        opacity: r1(0.25 + 0.6 * (1 - i / n)),
      } });
    }
    out.push({ tag: "circle", sifat: {
      cx: r1(cx), cy: r1(cy), r: r1(Math.min(w, h) * 0.09),
      style: `fill: ${c.utama}`,
    } });
    for (let i = 0; i < 5; i++) {
      const a = rng() * Math.PI * 2;
      const r = Math.min(w, h) * 0.17 * (1 + Math.floor(rng() * n));
      out.push({ tag: "circle", sifat: {
        cx: r1(cx + Math.cos(a) * r), cy: r1(cy + Math.sin(a) * r),
        r: r1(3 + rng() * 5), style: "fill: var(--nyala)",
      } });
    }
    return out;
  },

  kisi(rng, w, h, c) {
    const out: Bentuk[] = [];
    const kolom = 7 + Math.floor(rng() * 4);
    const s = w / kolom;
    const baris = Math.ceil(h / s);
    for (let y = 0; y < baris; y++) {
      for (let x = 0; x < kolom; x++) {
        const p = rng();
        if (p < 0.55) continue;
        const isi = p > 0.93 ? "var(--nyala)" : c.utama;
        out.push({ tag: "rect", sifat: {
          x: r1(x * s + s * 0.12), y: r1(y * s + s * 0.12),
          width: r1(s * 0.76), height: r1(s * 0.76),
          rx: r1(s * (p > 0.8 ? 0.38 : 0.16)),
          style: `fill: ${isi}`,
          opacity: r1(p > 0.93 ? 0.95 : 0.18 + (p - 0.55) * 1.4),
        } });
      }
    }
    return out;
  },

  gelombang(rng, w, h, c) {
    const out: Bentuk[] = [];
    const lapis = 4 + Math.floor(rng() * 3);
    for (let i = 0; i < lapis; i++) {
      const dasar = h * (0.3 + (i / lapis) * 0.75);
      const amp = h * (0.06 + rng() * 0.08);
      const fase = rng() * Math.PI * 2;
      let d = `M0,${r1(dasar)}`;
      for (let x = 0; x <= w; x += w / 24) {
        d += ` L${r1(x)},${r1(dasar + Math.sin(x / w * Math.PI * 2 + fase) * amp)}`;
      }
      d += ` L${w},${h} L0,${h} Z`;
      out.push({ tag: "path", sifat: {
        d, style: `fill: ${i === lapis - 2 ? "var(--nyala)" : c.utama}`,
        opacity: r1(i === lapis - 2 ? 0.55 : 0.12 + i * 0.1),
      } });
    }
    return out;
  },

  pecahan(rng, w, h, c) {
    const out: Bentuk[] = [];
    const n = 5 + Math.floor(rng() * 3);
    for (let i = 0; i < n; i++) {
      const pw = w * (0.18 + rng() * 0.35);
      const ph = h * (0.25 + rng() * 0.5);
      const x = rng() * (w - pw * 0.5);
      const y = rng() * (h - ph * 0.5);
      const sudut = Math.round((rng() - 0.5) * 50);
      const aksen = i === n - 1;
      out.push({ tag: "rect", sifat: {
        x: r1(x), y: r1(y), width: r1(pw), height: r1(ph),
        rx: r1(Math.min(pw, ph) * 0.18),
        transform: `rotate(${sudut} ${r1(x + pw / 2)} ${r1(y + ph / 2)})`,
        style: `fill: ${aksen ? "var(--nyala)" : c.utama}`,
        opacity: r1(aksen ? 0.85 : 0.2 + rng() * 0.38),
      } });
    }
    return out;
  },
};

const NAMA_RAGAM = Object.keys(RAGAM);

export interface OpsiSampul {
  lebar?: number;
  tinggi?: number;
  bahasa?: string | null;
  ragam?: string;
  kelas?: string;
  tanda?: boolean;
}

export interface RencanaSampul {
  w: number;
  h: number;
  rona: number;
  ragam: string;
  kelas: string;
  idg: string;
  bentuk: Bentuk[];
  tanda: string | null;
  warnaUtama: string;
}

/* Penomor id gradien/filter. Benih yang sama bisa muncul dua kali di satu
   halaman, dan `url(#id)` yang kembar selalu menunjuk definisi PERTAMA di
   dokumen -- yang bisa saja sudah dilepas bersama layar sebelumnya.
   Gambarnya tetap ditentukan benih; yang dibuat unik cuma alamat definisinya. */
let nomorSampul = 0;

/** Hanya untuk pembanding: samakan penomor supaya `idg` bisa diadu. */
export function setelNomorSampul(n: number): void {
  nomorSampul = n;
}

/** Rencana satu sampul: semua yang dibutuhkan untuk menggambarnya. */
export function rencanaSampul(teks: string, opsi: OpsiSampul = {}): RencanaSampul {
  const { lebar: w = 640, tinggi: tg = 360, bahasa = null, kelas = "",
          tanda = false } = opsi;
  const s = benih(String(teks));
  const rng = acak(s);
  const rona = bahasa && RONA[bahasa] !== undefined ? RONA[bahasa]! : s % 360;
  const warna = { utama: warnaRona(rona) };
  const teksTanda = tanda && bahasa ? (TANDA[bahasa] ?? null) : null;
  const ragam = opsi.ragam && RAGAM[opsi.ragam]
    ? opsi.ragam
    : NAMA_RAGAM[s % NAMA_RAGAM.length]!;
  const idg = "sg" + s.toString(36) + "-" + (++nomorSampul).toString(36);
  return {
    w, h: tg, rona, ragam, kelas, idg,
    bentuk: RAGAM[ragam]!(rng, w, tg, warna),
    tanda: teksTanda,
    warnaUtama: warna.utama,
  };
}
