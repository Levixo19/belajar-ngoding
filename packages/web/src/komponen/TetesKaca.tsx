/* Kaca cair di bilah atas: satu tetes air yang berpindah ke butir navigasi
 * yang sedang dibuka, merenggang di perjalanan, pecah jadi tetes kecil kalau
 * jaraknya jauh, lalu meninggalkan riak.
 *
 * Komponen ini TIDAK menggambar bilahnya. Bilah tetap `<nav id="rel">` milik
 * `Cangkang.tsx`, dengan tautan dan `aria-current` yang sama; yang ditambahkan
 * hanya tiga hal di dalamnya: sebuah kanvas WebGL (tetes + kilap tepi kaca),
 * sebuah tetes CSS cadangan, dan definisi filter SVG untuk pembiasan latar.
 * Ketiganya `aria-hidden` dan tidak menangkap penunjuk. Seluruh tampilannya
 * dikendalikan atribut yang dipasang di sini pada bilah:
 *   data-kaca = "cair" | "polos"  (polos = tema kontras: bilah padat lama)
 *   data-tk   = "gl" | "css"      (WebGL jalan, atau tetes cadangan)
 *   data-bias = "on" | "off"      (pembiasan latar, hanya Chromium)
 * Mencabut komponen ini (atau blok CSS "kaca cair" di ujung gaya.css)
 * mengembalikan bilah yang lama sepenuhnya.
 *
 * Aturan yang gampang terbalik, semuanya tanpa satu pun error kalau salah:
 *  - Tetes mengikuti butir yang AKTIF (nama dari `Cangkang`), bukan klik.
 *    Rute berubah dari palet perintah, tautan di halaman, atau tombol
 *    Kembali, dan tetesnya harus ikut. Butir di panel "Lainnya" menandai
 *    pemicunya; rute tanpa butir (halaman bahasa, materi) menyembunyikan
 *    tetesnya, jadi `aktif` boleh null.
 *  - Penanda lama (`a.kini`) baru dimatikan CSS sesudah atribut `data-tk`
 *    terpasang, dan atribut itu dipasang sebelum cat pertama (`useLayoutEffect`).
 *  - Gerak lewat `tingkatGerak()`, dibaca tiap langkah: mengganti tingkat di
 *    tengah jalan langsung berlaku, tanpa memasang ulang apa pun.
 *  - Bingkai hanya berjalan selama ada yang bergerak (`perluBingkai`). Kanvas
 *    menahan bingkai terakhirnya, jadi tetes yang diam tidak memakan GPU.
 *  - Pemasangan WAJIB bisa dibatalkan: `StrictMode` menjalankannya dua kali.
 *
 * Teknik dan mekanismenya mengikuti komponen "Liquid Glass Navbar" oleh
 * Guglielmo Giannattasio (@gughigug), dibagikan di 21st.dev dengan lisensi
 * MIT. Kodenya ditulis ulang (fisika di `tetes-teks.ts`, shader di
 * `tetes-shader.ts`), tetapi gagasannya milik pembuat aslinya, dan
 * syarat lisensi mewajibkan teks ini ikut:
 *
 *   MIT License. Copyright (c) Guglielmo Giannattasio (@gughigug).
 *   (Tahun tidak tertulis di sumbernya.)
 *
 *   Permission is hereby granted, free of charge, to any person obtaining a
 *   copy of this software and associated documentation files (the
 *   "Software"), to deal in the Software without restriction, including
 *   without limitation the rights to use, copy, modify, merge, publish,
 *   distribute, sublicense, and/or sell copies of the Software, and to
 *   permit persons to whom the Software is furnished to do so, subject to
 *   the following conditions:
 *
 *   The above copyright notice and this permission notice shall be included
 *   in all copies or substantial portions of the Software.
 *
 *   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 *   OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 *   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 *   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
 *   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 *   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 *   SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

import { useLayoutEffect, useRef } from "react";

import { tingkatGerak } from "../gerak.ts";
import { NAMA_UNIFORM, SUMBER_FRAGMEN, SUMBER_VERTEKS } from "./tetes-shader.ts";
import {
  TEPI, arahkan, bacaUniform, buatTetes, dukungBias, gayaCadangan, kacaAktif, langkah,
  nilaiGelap, perluBingkai, pindahLangsung, sasaranDariKotak, tambahRiak, tampilSeketika,
  tunjuk, ukuranBilah, type Sasaran,
} from "./tetes-teks.ts";

/** Seberapa jauh pembiasan menggeser isi di balik kaca (piksel). */
const GESER_BIAS = 36;

interface GL {
  gl: WebGLRenderingContext;
  u: Record<string, WebGLUniformLocation | null>;
}

function nyalakanGL(kanvas: HTMLCanvasElement): GL | null {
  const gl = kanvas.getContext("webgl", { premultipliedAlpha: true, alpha: true, antialias: false });
  if (!gl) return null;
  const buat = (jenis: number, sumber: string): WebGLShader | null => {
    const s = gl.createShader(jenis);
    if (!s) return null;
    gl.shaderSource(s, sumber);
    gl.compileShader(s);
    return gl.getShaderParameter(s, gl.COMPILE_STATUS) ? s : null;
  };
  const verteks = buat(gl.VERTEX_SHADER, SUMBER_VERTEKS);
  const fragmen = buat(gl.FRAGMENT_SHADER, SUMBER_FRAGMEN);
  if (!verteks || !fragmen) return null;
  const program = gl.createProgram();
  if (!program) return null;
  gl.attachShader(program, verteks);
  gl.attachShader(program, fragmen);
  gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) return null;
  gl.useProgram(program);
  const penyangga = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, penyangga);
  // Satu segitiga yang menutupi layar: lebih murah dari dua segitiga.
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  const atribut = gl.getAttribLocation(program, "a");
  gl.enableVertexAttribArray(atribut);
  gl.vertexAttribPointer(atribut, 2, gl.FLOAT, false, 0, 0);
  const u: Record<string, WebGLUniformLocation | null> = {};
  for (const nama of NAMA_UNIFORM) u[nama] = gl.getUniformLocation(program, nama);
  return { gl, u };
}

function ukurSasaran(nav: HTMLElement, nama: string | null): Sasaran | null {
  if (!nama) return null;
  const el = nav.querySelector<HTMLElement>(`[data-rel="${nama}"]`);
  if (!el) return null;
  const n = nav.getBoundingClientRect();
  const e = el.getBoundingClientRect();
  // Butir tersembunyi (layar sempit melipat bilah) tidak punya ukuran.
  if (e.width < 1 || e.height < 1) return null;
  return sasaranDariKotak({
    kiri: e.left - n.left, atas: e.top - n.top, lebar: e.width, tinggi: e.height,
  });
}

export function TetesKaca({ aktif }: { aktif: string | null }) {
  const kanvasRef = useRef<HTMLCanvasElement>(null);
  const cadanganRef = useRef<HTMLSpanElement>(null);
  const aktifRef = useRef(aktif);
  aktifRef.current = aktif;
  const ke = useRef<((nama: string | null) => void) | null>(null);

  /* Dipasang SEKALI, dan dideklarasikan lebih dulu dari efek `aktif` di
     bawahnya: efek tata letak berjalan menurut urutan deklarasi, dan efek
     kedua memanggil `ke.current` yang baru ada sesudah efek ini. */
  useLayoutEffect(() => {
    const kanvas = kanvasRef.current;
    const cadangan = cadanganRef.current;
    const nav = kanvas?.closest<HTMLElement>("#rel") ?? null;
    if (!kanvas || !cadangan || !nav) return;

    const t = buatTetes();
    const doc = document.documentElement;
    let glc = nyalakanGL(kanvas);
    let dpr = 1;
    let raf = 0;
    let terakhir = 0;
    let tema = doc.dataset.tema;
    let mauKaca = kacaAktif(tema);

    nav.dataset.bias = dukungBias(
      navigator.userAgent,
      typeof CSS !== "undefined" && CSS.supports("backdrop-filter", "url(#a)"),
    ) ? "on" : "off";

    const pasangAtribut = () => {
      nav.dataset.kaca = mauKaca ? "cair" : "polos";
      if (mauKaca) nav.dataset.tk = glc ? "gl" : "css";
      else delete nav.dataset.tk;
    };

    const ukurBilah = () => {
      const r = nav.getBoundingClientRect();
      ukuranBilah(t, r.width, r.height);
      if (!glc) return;
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      const w = r.width + TEPI * 2;
      const h = r.height + TEPI * 2;
      const pw = Math.round(w * dpr);
      const ph = Math.round(h * dpr);
      if (kanvas.width !== pw || kanvas.height !== ph) {
        kanvas.width = pw;
        kanvas.height = ph;
      }
      kanvas.style.width = `${w}px`;
      kanvas.style.height = `${h}px`;
      // Kanvas berdiri di tepi LUAR bilah, bukan tepi dalamnya: batas bilah
      // (1 sampai 2 piksel) ikut terhitung.
      kanvas.style.left = `${-TEPI - nav.clientLeft}px`;
      kanvas.style.top = `${-TEPI - nav.clientTop}px`;
    };

    const gambar = () => {
      if (!mauKaca || t.lebar === 0) return;
      if (glc) {
        const { gl, u } = glc;
        const d = bacaUniform(t);
        gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
        gl.uniform2f(u.uRes!, kanvas.width / dpr, kanvas.height / dpr);
        gl.uniform1f(u.uDpr!, dpr);
        gl.uniform1f(u.uWaktu!, t.waktu);
        gl.uniform4f(u.uBilah!, TEPI, TEPI, t.lebar, t.tinggi);
        gl.uniform4fv(u.uKapsul!, d.kapsul);
        gl.uniform1fv(u.uSy!, d.sy);
        gl.uniform4fv(u.uRiak!, d.riak);
        gl.uniform3f(u.uKursor!, d.kursor[0], d.kursor[1], d.kursor[2]);
        gl.uniform1f(u.uGelap!, nilaiGelap(tema));
        gl.uniform1f(u.uAmbien!, tingkatGerak() === "penuh" ? 1 : 0);
        gl.clearColor(0, 0, 0, 0);
        gl.clear(gl.COLOR_BUFFER_BIT);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
      } else {
        const g = gayaCadangan(t);
        cadangan.style.width = `${g.lebar}px`;
        cadangan.style.height = `${g.tinggi}px`;
        // Koordinat tetes terhadap tepi LUAR bilah, sedangkan `absolute` mengukur
        // dari tepi DALAMnya: batas bilah (1 sampai 2 piksel) harus dikurangkan.
        cadangan.style.top = `${g.atas - nav.clientTop}px`;
        cadangan.style.transform = `translateX(${g.geser - nav.clientLeft}px) scaleY(${g.skalaY})`;
        cadangan.style.opacity = g.tampak ? "1" : "0";
      }
    };

    const bingkai = (ts: number) => {
      raf = 0;
      const dt = Math.min((ts - terakhir) / 1000, 1 / 30);
      terakhir = ts;
      langkah(t, dt, ts, tingkatGerak(), Math.random);
      gambar();
      if (perluBingkai(t, tingkatGerak()) && !document.hidden) raf = requestAnimationFrame(bingkai);
    };
    const mulai = () => {
      if (raf || !mauKaca || document.hidden) return;
      terakhir = performance.now();
      raf = requestAnimationFrame(bingkai);
    };
    /** Gambar keadaan sekarang sekali (langkah nol detik menerapkan tingkat
     *  gerak yang baru, mis. "mati" langsung berdiri), lalu jalan kalau perlu. */
    const segarkan = () => {
      langkah(t, 0, performance.now(), tingkatGerak(), Math.random);
      gambar();
      if (perluBingkai(t, tingkatGerak())) mulai();
    };

    const arahkanKe = (nama: string | null) => {
      if (!mauKaca) return;
      ukurBilah();
      arahkan(t, ukurSasaran(nav, nama), performance.now(), tingkatGerak());
      segarkan();
    };
    ke.current = arahkanKe;

    pasangAtribut();
    if (mauKaca) {
      ukurBilah();
      arahkan(t, ukurSasaran(nav, aktifRef.current), performance.now(), tingkatGerak());
      tampilSeketika(t);
      segarkan();
    }

    // Ukuran bilah berubah (huruf selesai dimuat, jendela diubah, bilah
    // melipat di layar sempit): jarak lama tidak berarti lagi, berdiri langsung.
    const awal = nav.getBoundingClientRect();
    let lebarTerukur = awal.width;
    let tinggiTerukur = awal.height;
    const pengamat = new ResizeObserver(() => {
      const r = nav.getBoundingClientRect();
      if (Math.abs(r.width - lebarTerukur) < 0.5 && Math.abs(r.height - tinggiTerukur) < 0.5) return;
      lebarTerukur = r.width;
      tinggiTerukur = r.height;
      if (!mauKaca) return;
      ukurBilah();
      pindahLangsung(t, ukurSasaran(nav, aktifRef.current));
      segarkan();
    });
    pengamat.observe(nav);

    const koordinat = (e: PointerEvent) => {
      const r = nav.getBoundingClientRect();
      return { x: e.clientX - r.left, y: e.clientY - r.top };
    };
    const saatGerak = (e: PointerEvent) => {
      if (e.pointerType !== "mouse" || !mauKaca || tingkatGerak() !== "penuh") return;
      const p = koordinat(e);
      tunjuk(t, p.x, p.y);
      mulai();
    };
    const saatPergi = () => {
      tunjuk(t, null);
      mulai();
    };
    const saatTekan = (e: PointerEvent) => {
      if (!mauKaca || tingkatGerak() !== "penuh") return;
      const p = koordinat(e);
      tambahRiak(t, p.x, p.y, 0.8);
      mulai();
    };
    nav.addEventListener("pointermove", saatGerak);
    nav.addEventListener("pointerleave", saatPergi);
    nav.addEventListener("pointerdown", saatTekan);

    // Tema dan tingkat gerak berganti dari luar komponen (Pengaturan, tombol
    // tema, Ctrl+J, setelan sistem).
    const saatTampilan = () => {
      tema = doc.dataset.tema;
      const dulu = mauKaca;
      mauKaca = kacaAktif(tema);
      pasangAtribut();
      if (!mauKaca) {
        if (raf) cancelAnimationFrame(raf);
        raf = 0;
        return;
      }
      if (!dulu) {
        ukurBilah();
        pindahLangsung(t, ukurSasaran(nav, aktifRef.current));
        tampilSeketika(t);
      }
      segarkan();
    };
    document.addEventListener("tampilan-berubah", saatTampilan);
    const kurangiGerak = window.matchMedia("(prefers-reduced-motion: reduce)");
    kurangiGerak.addEventListener("change", saatTampilan);

    const saatLihat = () => {
      if (document.hidden) return;
      terakhir = performance.now();
      if (perluBingkai(t, tingkatGerak())) mulai();
    };
    document.addEventListener("visibilitychange", saatLihat);

    // Konteks WebGL bisa dicabut peramban kapan saja (kartu grafis diganti,
    // terlalu banyak konteks). Pindah ke tetes cadangan, jangan menggantung.
    const saatHilang = (e: Event) => {
      e.preventDefault();
      glc = null;
      pasangAtribut();
      if (mauKaca) {
        ukurBilah();
        segarkan();
      }
    };
    kanvas.addEventListener("webglcontextlost", saatHilang);

    return () => {
      if (raf) cancelAnimationFrame(raf);
      raf = 0;
      ke.current = null;
      pengamat.disconnect();
      nav.removeEventListener("pointermove", saatGerak);
      nav.removeEventListener("pointerleave", saatPergi);
      nav.removeEventListener("pointerdown", saatTekan);
      document.removeEventListener("tampilan-berubah", saatTampilan);
      kurangiGerak.removeEventListener("change", saatTampilan);
      document.removeEventListener("visibilitychange", saatLihat);
      kanvas.removeEventListener("webglcontextlost", saatHilang);
      delete nav.dataset.kaca;
      delete nav.dataset.tk;
      delete nav.dataset.bias;
    };
  }, []);

  useLayoutEffect(() => {
    ke.current?.(aktif);
  }, [aktif]);

  return (
    <>
      <svg className="tk-bias" width="0" height="0" aria-hidden="true" focusable="false">
        <filter id="tk-bias" x="0" y="0" width="100%" height="100%" colorInterpolationFilters="sRGB">
          <feTurbulence type="fractalNoise" baseFrequency="0.006 0.02" numOctaves={2} seed={7} result="derau" />
          <feGaussianBlur in="derau" stdDeviation="2" result="halus" />
          <feDisplacementMap
            in="SourceGraphic" in2="halus" scale={GESER_BIAS}
            xChannelSelector="R" yChannelSelector="G"
          />
        </filter>
      </svg>
      <canvas ref={kanvasRef} className="tk-kanvas" aria-hidden="true" />
      <span ref={cadanganRef} className="tk-cadangan" aria-hidden="true" />
    </>
  );
}
