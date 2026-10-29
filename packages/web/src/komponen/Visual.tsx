/* Gambar konsep di halaman materi: pohon dari `visual-bentuk.ts` -> SVG React.
 *
 * Port `gambarVisual` dan `hidupkan` dari `webapp/statik/js/visual.js`.
 * Geometrinya tidak ada di sini sama sekali -- ia tinggal di `visual-bentuk.ts`
 * dan sudah diadu simpul demi simpul dengan versi JS-nya atas 1.356
 * spesifikasi gambar (`uji/banding-visual.mjs`). Yang tinggal di berkas ini
 * cuma dua hal yang memang butuh peramban: mengubah pohon jadi simpul, dan
 * animasi garis-tergambar.
 */

import { useEffect, useRef, useState, type ReactNode } from "react";

import { tingkatGerak } from "../gerak.ts";
import { bentukVisual, type Simpul, type SpekUmum } from "./visual-bentuk.ts";

/* `class` dipetakan ke `className`; sisanya diteruskan apa adanya.
 *
 * Atribut SVG bertanda hubung (`dominant-baseline`, `text-anchor`) memang
 * ditulis begitu di React, jadi tidak ada yang perlu diterjemahkan selain
 * `class` -- dan `class` WAJIB diterjemahkan, karena React menolaknya dengan
 * peringatan lalu tetap merender elemen tanpa kelasnya. Yang terlihat gambar
 * tanpa satu pun warna, di keempat tema, tanpa error. */
function keSimpul(n: Simpul | string, kunci: number): ReactNode {
  if (typeof n === "string") return n;
  const { class: kelas, ...sisa } = n.sifat;
  const Tag = n.tag as "g";
  return (
    <Tag key={kunci} className={kelas} {...sisa}>
      {n.anak.map(keSimpul)}
    </Tag>
  );
}

export function Visual({ spek }: { spek: SpekUmum }) {
  const akarRef = useRef<HTMLElement>(null);
  const [hidup, setHidup] = useState(false);

  const hasil = bentukVisual(spek);

  /* Garisnya tergambar saat gambar pertama kali tergulir ke layar, hanya di
   * tingkat gerak penuh. Keadaan alaminya TERGAMBAR UTUH: kelas `v-hidup`
   * cuma memasang animasi yang berangkat dari kosong, jadi kalau pengamatnya
   * tidak pernah menyala, gambarnya tetap lengkap. Itu bentuk yang dituntut
   * AGENTS.md ("animasi tidak boleh jadi satu-satunya cara sebuah elemen
   * terlihat"), dan di sini ia gratis: `hidup` cuma MENAMBAH kelas. */
  useEffect(() => {
    if (tingkatGerak() !== "penuh") return;
    if (typeof IntersectionObserver === "undefined") return;
    const el = akarRef.current;
    if (!el) return;
    const pengamat = new IntersectionObserver((entri) => {
      for (const e of entri) {
        if (!e.isIntersecting) continue;
        pengamat.unobserve(e.target);
        // Dipicu SEBELUM masuk layar (rootMargin bawah). Gambar yang sudah
        // terlihat saat pertama diamati tidak dianimasikan: mengosongkan garis
        // yang sedang dibaca lalu menggambarnya ulang adalah kedipan.
        if (e.boundingClientRect.top < globalThis.innerHeight) continue;
        setHidup(true);
      }
    }, { rootMargin: "0px 0px 25% 0px", threshold: 0 });
    pengamat.observe(el);
    return () => pengamat.disconnect();
  }, []);

  // Jenis yang tak dikenal atau data yang menjatuhkan penggambarnya tidak
  // boleh menjatuhkan seluruh halaman materi. `tests/test_visual.py` yang
  // wajib menangkapnya lebih dulu; kalau sampai ke sini, pagar itu bocor.
  if (!hasil) return null;

  const w = Math.ceil(hasil.w), t = Math.ceil(hasil.h);
  return (
    <figure
      ref={akarRef}
      className={"visual" + (hidup ? " v-hidup" : "")}
      data-jenis={spek.jenis}
    >
      <div className="visual-kanvas">
        <svg
          viewBox={`0 0 ${w} ${t}`}
          width={w}
          role="img"
          aria-label={spek.judul}
          className="visual-svg"
          preserveAspectRatio="xMinYMin meet"
          style={{ width: "100%", maxWidth: Math.round(w * 1.3) + "px" }}
        >
          {hasil.simpul.map(keSimpul)}
        </svg>
      </div>
      <figcaption className="visual-judul">
        <span className="visual-nomor">{"Gambar " + (spek.nomor || "")}</span>
        <span className="visual-teks">{spek.judul}</span>
        {spek.ket ? <span className="visual-ket">{spek.ket}</span> : null}
      </figcaption>
    </figure>
  );
}
