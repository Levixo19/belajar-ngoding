/* Sampul: karya visual SVG yang dibangkitkan dari sebuah teks.
 *
 * Pemilik meminta gambar ("no one wants to see website full tulisan"), dan
 * aplikasi ini wajib utuh tanpa internet, jadi gambarnya tidak diambil dari
 * mana pun: tiap bahasa, bab, dan profesi mendapat komposisi geometris yang
 * DIBANGKITKAN dari namanya sendiri. Teks yang sama selalu menghasilkan
 * gambar yang sama (PRNG berbenih), jadi sampul HTML hari ini sama dengan
 * sampul HTML bulan depan, dan dua bab yang bertetangga tetap berbeda.
 *
 * Warna: satu warna identitas per bahasa (diredam: saturasi rendah, supaya
 * tenang di sesi panjang) ditemani aksen aplikasi (--nyala) dan latar kartu.
 * Warna tema dibaca lewat style="fill: var(--...)", jadi sampul ikut berganti
 * saat tema diganti tanpa digambar ulang.
 *
 * Gambar ini HIASAN: aria-hidden, tidak bisa difokus, dan tidak pernah jadi
 * satu-satunya pembawa informasi.
 *
 * Importir: layar-belajar.js, beranda.js, layar-karier.js, layar-pustaka.js,
 * layar-lain.js, layar-kerja.js.
 */

import { h } from "./inti.js";

const NS = "http://www.w3.org/2000/svg";

/* Rona identitas per kunci bahasa (derajat HSL). Bahasa yang tidak ada di sini
   mendapat rona dari hash namanya. */
const RONA = {
  html: 16, css: 205, javascript: 46, typescript: 212, python: 52, java: 14,
  c: 222, cpp: 232, go: 190, rust: 22, php: 245, ruby: 352, kotlin: 268,
  sql: 196, bash: 135, git: 10, fedora: 214, aplikasi: 32, csharp: 275, vb: 238,
};

/* Tanda: akhiran berkas atau isyarat pendek tiap kurikulum, digambar besar
   dan samar di sudut sampul. Inilah yang membuat sampul Python terbaca
   "Python" sebelum namanya dibaca. */
const TANDA = {
  html: "</>", css: "{ }", javascript: ".js", typescript: ".ts", python: ".py",
  java: ".java", c: ".c", cpp: ".cpp", go: ".go", rust: ".rs", php: ".php",
  ruby: ".rb", kotlin: ".kt", sql: ".sql", bash: ".sh", git: "git", fedora: "$_",
  aplikasi: "app", csharp: ".cs", vb: ".vb",
};

/* Saturasi & kecerahan dibaca dari CSS (--sampul-s, --sampul-l), supaya tema
   terang bisa menggelapkan warnanya tanpa menggambar ulang sampul. */
const warnaRona = (rona) => `hsl(${rona} var(--sampul-s, 44%) var(--sampul-l, 58%))`;

function benih(teks) {
  let h = 2166136261;
  for (let i = 0; i < teks.length; i++) {
    h ^= teks.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/** mulberry32: PRNG kecil berbenih, cukup untuk tata letak hiasan. */
function acak(benihAwal) {
  let a = benihAwal || 1;
  return () => {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function el(tag, sifat = {}, ...anak) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(sifat)) {
    if (v !== null && v !== undefined) e.setAttribute(k, String(v));
  }
  for (const a of anak) if (a) e.append(a);
  return e;
}

const r1 = (n) => Math.round(n * 10) / 10;

/* Empat ragam komposisi. Masing-masing menerima (rng, w, h, warna) dan
   mengembalikan daftar elemen. Semuanya memakai sedikit bentuk besar --
   sampul yang ramai berhenti terbaca sebagai satu benda. */
const RAGAM = {
  orbit(rng, w, h, c) {
    const cx = w * (0.55 + rng() * 0.3);
    const cy = h * (0.35 + rng() * 0.4);
    const out = [];
    const n = 4 + Math.floor(rng() * 3);
    for (let i = n; i >= 1; i--) {
      const r = (Math.min(w, h) * 0.17) * i;
      out.push(el("circle", {
        cx: r1(cx), cy: r1(cy), r: r1(r), fill: "none",
        style: `stroke: ${i === 2 ? "var(--nyala)" : c.utama}`,
        "stroke-width": i === 2 ? 2 : 1.2, opacity: r1(0.25 + 0.6 * (1 - i / n)),
      }));
    }
    out.push(el("circle", { cx: r1(cx), cy: r1(cy), r: r1(Math.min(w, h) * 0.09),
                            style: `fill: ${c.utama}` }));
    for (let i = 0; i < 5; i++) {
      const a = rng() * Math.PI * 2;
      const r = Math.min(w, h) * 0.17 * (1 + Math.floor(rng() * n));
      out.push(el("circle", { cx: r1(cx + Math.cos(a) * r), cy: r1(cy + Math.sin(a) * r),
                              r: r1(3 + rng() * 5), style: "fill: var(--nyala)" }));
    }
    return out;
  },

  kisi(rng, w, h, c) {
    const out = [];
    const kolom = 7 + Math.floor(rng() * 4);
    const s = w / kolom;
    const baris = Math.ceil(h / s);
    for (let y = 0; y < baris; y++) {
      for (let x = 0; x < kolom; x++) {
        const p = rng();
        if (p < 0.55) continue;
        const isi = p > 0.93 ? "var(--nyala)" : c.utama;
        out.push(el("rect", {
          x: r1(x * s + s * 0.12), y: r1(y * s + s * 0.12),
          width: r1(s * 0.76), height: r1(s * 0.76), rx: r1(s * (p > 0.8 ? 0.38 : 0.16)),
          style: `fill: ${isi}`, opacity: r1(p > 0.93 ? 0.95 : 0.18 + (p - 0.55) * 1.4),
        }));
      }
    }
    return out;
  },

  gelombang(rng, w, h, c) {
    const out = [];
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
      out.push(el("path", { d, style: `fill: ${i === lapis - 2 ? "var(--nyala)" : c.utama}`,
                            opacity: r1(i === lapis - 2 ? 0.55 : 0.12 + i * 0.1) }));
    }
    return out;
  },

  pecahan(rng, w, h, c) {
    const out = [];
    const n = 5 + Math.floor(rng() * 3);
    for (let i = 0; i < n; i++) {
      const pw = w * (0.18 + rng() * 0.35);
      const ph = h * (0.25 + rng() * 0.5);
      const x = rng() * (w - pw * 0.5);
      const y = rng() * (h - ph * 0.5);
      const sudut = Math.round((rng() - 0.5) * 50);
      const aksen = i === n - 1;
      out.push(el("rect", {
        x: r1(x), y: r1(y), width: r1(pw), height: r1(ph), rx: r1(Math.min(pw, ph) * 0.18),
        transform: `rotate(${sudut} ${r1(x + pw / 2)} ${r1(y + ph / 2)})`,
        style: `fill: ${aksen ? "var(--nyala)" : c.utama}`,
        opacity: r1(aksen ? 0.85 : 0.2 + rng() * 0.38),
      }));
    }
    return out;
  },
};

const NAMA_RAGAM = Object.keys(RAGAM);

/* Penomor id gradien/filter. Benih yang sama bisa muncul dua kali di satu
   halaman (akordeon dan marquee sama-sama menggambar "python"), dan url(#id)
   yang kembar selalu menunjuk ke definisi PERTAMA di dokumen -- yang bisa saja
   sudah dilepas bersama layar sebelumnya. Gambarnya tetap ditentukan benih;
   yang dibuat unik cuma alamat definisinya. */
let nomorSampul = 0;

/**
 * Bangun satu sampul.
 *
 * @param teks   benih gambar, mis. "python" atau "python/bab-3"
 * @param opsi   { lebar = 640, tinggi = 360, bahasa, ragam, kelas, tanda }
 *               `bahasa` memilih rona identitas; `ragam` memaksa komposisi;
 *               `tanda` menggambar isyarat bahasanya (".py") di sudut.
 * @returns SVGElement yang mengisi wadahnya (preserveAspectRatio slice).
 */
export function sampul(teks, opsi = {}) {
  const { lebar: w = 640, tinggi: tg = 360, bahasa = null, kelas = "", tanda = false } = opsi;
  const s = benih(String(teks));
  const rng = acak(s);
  const rona = bahasa && RONA[bahasa] !== undefined ? RONA[bahasa] : s % 360;
  const warna = { utama: warnaRona(rona) };
  const teksTanda = tanda && bahasa ? TANDA[bahasa] : null;
  const ragam = opsi.ragam && RAGAM[opsi.ragam] ? opsi.ragam
    : NAMA_RAGAM[s % NAMA_RAGAM.length];
  const idg = "sg" + s.toString(36) + "-" + (++nomorSampul).toString(36);

  return el("svg", {
    viewBox: `0 0 ${w} ${tg}`, preserveAspectRatio: "xMidYMid slice",
    class: ("sampul " + kelas).trim(), "aria-hidden": "true", focusable: "false",
    "data-ragam": ragam,
  },
    el("defs", {},
      el("linearGradient", { id: idg + "l", x1: "0", y1: "0", x2: "1", y2: "1" },
        el("stop", { offset: "0", style: `stop-color: hsl(${rona} 30% 50%); stop-opacity: .22` }),
        el("stop", { offset: "1", style: "stop-color: var(--nyala); stop-opacity: .10" })),
      el("filter", { id: idg + "b", x: "0", y: "0", width: "100%", height: "100%" },
        el("feTurbulence", { type: "fractalNoise", baseFrequency: ".85", numOctaves: "2",
                             stitchTiles: "stitch" }),
        el("feColorMatrix", { values: "0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .09 0" }))),
    el("rect", { width: w, height: tg, style: "fill: var(--kartu)" }),
    el("rect", { width: w, height: tg, fill: `url(#${idg}l)` }),
    ...RAGAM[ragam](rng, w, tg, warna),
    teksTanda ? el("text", {
      x: r1(w * 0.06), y: r1(tg * 0.9), class: "sampul-tanda",
      "font-size": r1(tg * 0.34), style: "fill: var(--teks)",
    }, document.createTextNode(teksTanda)) : null,
    el("rect", { width: w, height: tg, filter: `url(#${idg}b)` }));
}

/** Kepala halaman bersampul: teks di kiri, sampul di kanan.
 *
 *  Argumen sesudah `opsi` adalah ISI kepala, persis yang dulu diberikan ke
 *  h("header.kepala-besar", {}, ...). Jadi mengubah sebuah layar cukup
 *  mengganti pembukanya; kurung penutup dan isinya tidak disentuh, dan
 *  susunan teks di kiri tetap sama dengan versi tanpa sampul. */
export function kepalaBersampul(benih, opsi, ...isi) {
  // `pita`: untuk layar yang kolomnya sempit (kuis, sekitar 720 px). Di sana
  // sampul di samping memeras judul jadi lima baris; sebagai pita melebar di
  // ATAS judul, judulnya kembali ke dua baris.
  const { pita = false, ...sisa } = opsi;
  return h("header.kepala-besar.kepala-bersampul", { kelas: pita ? "kepala-berpita" : "" },
    h("div.kepala-teks", {}, ...isi),
    h("div.kepala-sampul", {},
      sampul(benih, pita ? { lebar: 960, tinggi: 200, ...sisa } : { lebar: 560, tinggi: 400, ...sisa })));
}
