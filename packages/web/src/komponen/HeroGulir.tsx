/* Hero yang membuka saat digulir (layar Pengantar): sebuah gambar kecil
 * mengembang sampai memenuhi pelatnya, judulnya terbelah ke kiri dan kanan,
 * latarnya memudar, lalu isi di bawahnya muncul.
 *
 * Padanan komponen `ScrollExpandMedia` yang ditempel pemilik (framer-motion +
 * Tailwind + Next), ditulis ulang tanpa satu pun pustaka: seluruh geraknya satu
 * angka `--hg-p` (0..1) yang dibaca CSS di `gaya.css` (blok "hero gulir").
 * Logika isyaratnya di `hero-gulir-teks.ts`, murni dan diuji di Node.
 *
 * Yang sengaja berbeda dari aslinya, masing-masing dengan sebabnya:
 *  - Gerak penuh saja yang membajak gulir. Pada "halus", "mati", dan
 *    `prefers-reduced-motion` hero tampil SUDAH terbuka: membajak roda adalah
 *    gerak akibat interaksi (WCAG 2.3.3), dan orang yang memintanya padam tidak
 *    boleh dipaksa menggulir untuk melihat isi.
 *  - Papan ketik punya jalan sendiri (Spasi, PageDown, panah, End) dan ada
 *    tombol "Lewati pengantar" yang terlihat. Aslinya hanya roda dan sentuh.
 *  - Isi di bawah hero TIDAK dirender selama hero tertutup, jadi tidak ada
 *    tautan tersembunyi yang bisa difokuskan lewat Tab.
 *  - Angka `p` ditulis ke DOM lewat ref, tidak jadi state React: ia berubah
 *    tiap bingkai, sedangkan React hanya perlu tahu "terbuka atau belum".
 *  - Tidak ada `scrollTo(0, 0)` tiap peristiwa gulir (aslinya begitu). Isi yang
 *    belum dirender membuat halaman pendek, jadi tidak ada yang perlu dikunci.
 */

import { useEffect, useRef, useState, type ReactNode } from "react";

import { adaGerak, gerakPenuh } from "../gerak.ts";
import { umumkan } from "../sorak.tsx";
import {
  AMBANG_TERBUKA, PEMILIK_TOMBOL, pikselRoda, susul, terapkanIsyarat,
} from "./hero-gulir-teks.ts";

interface Kendali {
  ke: (p: number, langsung?: boolean) => void;
}

export function HeroGulir({
  judul,
  gambarLatar,
  gambarMedia,
  altMedia,
  petunjuk,
  children,
}: {
  /** Dua baris judul: yang pertama bergeser ke kiri, yang kedua ke kanan. */
  judul: [string, string];
  /** Dekoratif (`alt` kosong): memudar sepenuhnya saat hero terbuka. */
  gambarLatar: string;
  gambarMedia: string;
  altMedia: string;
  /** Petunjuk di kaki hero selama belum terbuka. */
  petunjuk: string;
  children: ReactNode;
}) {
  const [penuh, setPenuh] = useState<boolean>(gerakPenuh);
  const [terbuka, setTerbuka] = useState<boolean>(() => !gerakPenuh());
  const akar = useRef<HTMLElement>(null);
  const isi = useRef<HTMLDivElement>(null);
  const kendali = useRef<Kendali | null>(null);
  const pTergambar = useRef(0);
  const terbukaRef = useRef(terbuka);
  const terakhirGulir = useRef(-Infinity);
  const fokusKeIsi = useRef(false);
  const lewatiBerfokus = useRef(false);
  const sudahTertutup = useRef(false);

  const tulis = (p: number) => {
    pTergambar.current = p;
    akar.current?.style.setProperty("--hg-p", String(p));
  };

  // Tingkat gerak bisa berubah di tengah jalan: tombol di pil atas, Ctrl+J,
  // Pengaturan, atau setelan sistem.
  useEffect(() => {
    const segarkan = () => setPenuh(gerakPenuh());
    document.addEventListener("tampilan-berubah", segarkan);
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    mq.addEventListener("change", segarkan);
    return () => {
      document.removeEventListener("tampilan-berubah", segarkan);
      mq.removeEventListener("change", segarkan);
    };
  }, []);

  // Tanpa gerak penuh hero langsung terbuka.
  useEffect(() => {
    if (penuh) return;
    tulis(1);
    terbukaRef.current = true;
    setTerbuka(true);
  }, [penuh]);

  // Gerak penuh: roda dan papan ketik menggeser `p`, lalu `p` menyusul.
  useEffect(() => {
    if (!penuh || !akar.current) return;
    let target = terbukaRef.current ? 1 : pTergambar.current;
    let kini = target;
    let raf = 0;

    const bingkai = () => {
      raf = 0;
      kini = susul(kini, target);
      tulis(kini);
      const buka = kini >= AMBANG_TERBUKA;
      if (buka !== terbukaRef.current) {
        terbukaRef.current = buka;
        setTerbuka(buka);
      }
      if (kini !== target) raf = requestAnimationFrame(bingkai);
    };
    const dorong = (p: number, langsung = false) => {
      target = p;
      if (langsung) kini = p;
      if (!raf) raf = requestAnimationFrame(bingkai);
    };
    kendali.current = { ke: dorong };

    const keadaan = () => ({
      p: target,
      gulirY: window.scrollY,
      sejakGulir: performance.now() - terakhirGulir.current,
    });
    const roda = (e: WheelEvent) => {
      if (e.ctrlKey || (e.target as Element | null)?.closest?.("#tirai")) return;
      const h = terapkanIsyarat(
        { jenis: "roda", delta: pikselRoda(e.deltaY, e.deltaMode, window.innerHeight) },
        keadaan(),
      );
      if (h.cegah) { e.preventDefault(); dorong(h.p); }
    };
    const tombol = (e: KeyboardEvent) => {
      if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
      if ((e.target as Element | null)?.closest?.(PEMILIK_TOMBOL)) return;
      const h = terapkanIsyarat(
        { jenis: "tombol", key: e.key, shift: e.shiftKey, ulang: e.repeat },
        keadaan(),
      );
      if (h.cegah) { e.preventDefault(); dorong(h.p); }
    };
    const gulir = () => { terakhirGulir.current = performance.now(); };

    window.addEventListener("wheel", roda, { passive: false });
    window.addEventListener("keydown", tombol);
    window.addEventListener("scroll", gulir, { passive: true });
    return () => {
      window.removeEventListener("wheel", roda);
      window.removeEventListener("keydown", tombol);
      window.removeEventListener("scroll", gulir);
      if (raf) cancelAnimationFrame(raf);
      kendali.current = null;
    };
  }, [penuh]);

  // Yang mengumumkan dan memindahkan fokus saat isi muncul. Fokus tidak boleh
  // jatuh ke <body> ketika tombol "Lewati" yang sedang berfokus ikut hilang.
  useEffect(() => {
    if (!terbuka) { sudahTertutup.current = true; return; }
    if (fokusKeIsi.current || lewatiBerfokus.current) {
      fokusKeIsi.current = false;
      lewatiBerfokus.current = false;
      const el = isi.current;
      if (el) {
        el.focus({ preventScroll: true });
        window.scrollTo({ top: Math.max(0, el.offsetTop - 96), behavior: adaGerak() ? "smooth" : "auto" });
      }
    }
    if (sudahTertutup.current) umumkan("Pengantar terbuka. Isinya ada di bawah judul.");
  }, [terbuka]);

  const lewati = () => {
    fokusKeIsi.current = true;
    kendali.current?.ke(1, true);
  };

  return (
    <section
      className="hg"
      ref={akar}
      data-terbuka={terbuka ? "true" : "false"}
      data-penuh={penuh ? "true" : "false"}
    >
      <div className="hg-pelat">
        <img className="hg-latar" src={gambarLatar} alt="" decoding="async" />
        <div className="hg-media">
          <img src={gambarMedia} alt={altMedia} decoding="async" />
          <div className="hg-scrim" aria-hidden="true" />
        </div>
        <h1 className="hg-judul">
          <span className="hg-kiri">{judul[0]}</span>{" "}
          <span className="hg-kanan">{judul[1]}</span>
        </h1>
        {!terbuka ? <p className="hg-petunjuk">{petunjuk}</p> : null}
        {penuh && !terbuka ? (
          <button
            type="button"
            className="tbl tbl-kecil tbl-hantu hg-lewati"
            onClick={lewati}
            onFocus={() => { lewatiBerfokus.current = true; }}
            onBlur={() => { lewatiBerfokus.current = false; }}
          >
            Lewati pengantar
          </button>
        ) : null}
      </div>
      {terbuka ? (
        <div className="hg-isi" ref={isi} tabIndex={-1}>
          {children}
        </div>
      ) : null}
    </section>
  );
}
