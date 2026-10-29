/* Pilihan: select-only combobox (pola APG) yang daftarnya digambar DI DALAM
 * halaman, pengganti `<select>` di seluruh aplikasi.
 *
 * Alasannya, terukur 2026-10-28: popup `<select>` bawaan peramban adalah jendela
 * terpisah. Di Chrome kami uji apa yang menutupnya, dan tidak ada kode
 * aplikasi di antaranya (render ulang, penulisan opsi, gulir, blur, dan
 * pointer tidak menutupnya; hanya ubah ukuran jendela dan elemen yang dipasang
 * ulang). Gejala yang dilaporkan pemilik, menutup sendiri begitu klik dilepas
 * dan baru bertahan kalau tombol ditahan, berasal dari popup native (Wayland)
 * dan tidak bisa dibetulkan dari halaman. Penyebab persisnya TIDAK terbukti;
 * yang terbukti hanya bahwa daftar yang digambar sendiri tidak punya jalur
 * kegagalan itu: ia terbuka saat diklik, tetap terbuka, dan memilih cukup satu
 * klik cepat.
 *
 * Yang sengaja dijaga, masing-masing dengan sebabnya:
 *  - Fokus TETAP di tombol (`aria-activedescendant`), dan `pointerdown` pada
 *    opsi di-`preventDefault`. Kalau fokus pindah ke daftar, `blur` menutup
 *    daftar sebelum `click` sempat memilih, dan kesalahan itu persis gejala
 *    yang mau dihilangkan.
 *  - Opsi disorot lewat `pointermove`, bukan `pointerenter`: peramban
 *    mengirim `pointerenter` palsu ke elemen yang tergulir ke bawah kursor
 *    diam. Dan daftar hanya menggulir ke opsi aktif bila PAPAN KETIK yang
 *    menggesernya: menggulir di bawah penunjuk menggeser baris yang sedang
 *    diklik dan kliknya mengenai tetangganya.
 *  - Daftar digambar lewat portal dengan posisi `fixed`, ke `#tirai` bila
 *    tombolnya di dalam dialog, kalau tidak ke `<body>`. `.jendela` ber-
 *    `overflow: hidden`, jadi daftar yang menempel di dalamnya terpotong.
 *  - Escape pada tombol yang terbukanya hanya menutup daftar: dialog
 *    (`fokus-dialog.ts`, `Jendela.tsx`) melewati Escape yang ditujukan ke
 *    `.pil-pemicu[aria-expanded="true"]`, dan di sini `stopPropagation`
 *    mencegah pendengar dokumen lain (mis. Langit) ikut bereaksi.
 *  - Nama aksesibelnya dari `<label htmlFor>` di luar daftar, atau
 *    `namaTombol` bila tidak ada label. Label yang MEMBUNGKUS daftar
 *    meneruskan klik pada opsi ke tombol dan membukanya lagi sesudah memilih
 *    (dengan portal, daftar memang di luar label).
 */

import {
  useEffect, useId, useRef, useState,
  type CSSProperties, type KeyboardEvent as TekanEvent,
} from "react";
import { createPortal } from "react-dom";

import { Ikon } from "./Ikon.tsx";
import { cariAwalan, geserAktif, sambungAwalan, type OpsiPilihan } from "./pilihan-teks.ts";

/** Ruang di bawah tombol yang dianggap cukup untuk daftar menurun, piksel. */
const RUANG_DAFTAR = 288;

interface Posisi {
  left: number;
  width: number;
  top?: number;
  bottom?: number;
  maks: number;
  naik: boolean;
}

export function Pilihan({
  id,
  label,
  namaTombol,
  nilai,
  opsi,
  onUbah,
  kelas,
  kelasPemicu,
  gaya,
}: {
  /** `id` tombol: diacu `<label htmlFor>` di pemanggilnya. Bawaan: dibuatkan. */
  id?: string;
  /** Nama daftar untuk pembaca layar. */
  label: string;
  /** Nama tombolnya bila tidak ada `<label htmlFor>` yang menamainya. */
  namaTombol?: string;
  nilai: string;
  opsi: readonly OpsiPilihan[];
  onUbah: (id: string) => void;
  /** Kelas tambahan untuk pembungkus (`.pil-kotak`). */
  kelas?: string;
  /** Kelas tambahan untuk tombolnya (mis. gaya `<select>` lama sebuah layar). */
  kelasPemicu?: string;
  /** Gaya pembungkus: lebar otomatis, `flex`, dan sebagainya. */
  gaya?: CSSProperties;
}) {
  const kunci = useId();
  const idTombol = id ?? `${kunci}-tombol`;
  const idDaftar = `${kunci}-daftar`;
  const idOpsi = (i: number) => `${kunci}-o${i}`;
  const [buka, setBuka] = useState(false);
  const [aktif, setAktif] = useState(0);
  const [pos, setPos] = useState<Posisi | null>(null);
  const [wadah, setWadah] = useState<Element | null>(null);
  const akar = useRef<HTMLDivElement>(null);
  const pemicu = useRef<HTMLButtonElement>(null);
  const daftar = useRef<HTMLUListElement>(null);
  const ketik = useRef({ teks: "", t: 0 });
  // Siapa yang terakhir menggeser opsi aktif (lihat catatan kepala berkas).
  const gulirKeAktif = useRef(true);
  const terpilih = Math.max(0, opsi.findIndex((o) => o.id === nilai));

  function ukurPos(): Posisi | null {
    const r = pemicu.current?.getBoundingClientRect();
    if (!r) return null;
    const bawah = innerHeight - r.bottom;
    // Menurun kalau muat; kalau tidak, naik asalkan di atas lebih lapang.
    const naik = bawah < RUANG_DAFTAR && r.top > bawah;
    const maks = Math.max(120, Math.min(320, (naik ? r.top : bawah) - 12));
    return naik
      ? { left: r.left, width: r.width, bottom: innerHeight - r.top + 4, maks, naik }
      : { left: r.left, width: r.width, top: r.bottom + 4, maks, naik };
  }

  function bukaDaftar(mulai: number = terpilih) {
    setWadah(pemicu.current?.closest("#tirai") ?? document.body);
    setPos(ukurPos());
    gulirKeAktif.current = true;
    setAktif(mulai);
    setBuka(true);
  }

  function geserKe(i: number) {
    gulirKeAktif.current = true;
    setAktif(i);
  }

  function pilih(i: number) {
    const o = opsi[i];
    if (!o) return;
    if (o.id !== nilai) onUbah(o.id);
    setBuka(false);
  }

  // Klik di luar menutup. `pointerdown`, bukan `click`: hasilnya sama bagi
  // klik cepat, tapi tidak menunggu tombol dilepas. Daftar ada di luar
  // `.pil-kotak` (portal), jadi ia dihitung sebagai "di dalam" juga.
  useEffect(() => {
    if (!buka) return;
    const luar = (e: PointerEvent) => {
      const t = e.target;
      if (t instanceof Node && !akar.current?.contains(t) && !daftar.current?.contains(t)) setBuka(false);
    };
    document.addEventListener("pointerdown", luar);
    return () => document.removeEventListener("pointerdown", luar);
  }, [buka]);

  // Daftar mengikuti tombolnya saat halaman atau wadah apa pun menggulir, dan
  // saat jendela berubah ukuran.
  useEffect(() => {
    if (!buka) return;
    const ulang = () => setPos(ukurPos());
    window.addEventListener("scroll", ulang, true);
    window.addEventListener("resize", ulang);
    return () => {
      window.removeEventListener("scroll", ulang, true);
      window.removeEventListener("resize", ulang);
    };
  }, [buka]);

  // Opsi aktif selalu terlihat di dalam daftar. Menggulir `scrollTop` daftar
  // sendiri, bukan `scrollIntoView`, yang ikut menggulir halaman.
  useEffect(() => {
    if (!buka || !gulirKeAktif.current) return;
    const d = daftar.current;
    const li = d?.children[aktif] as HTMLElement | undefined;
    if (!d || !li) return;
    if (li.offsetTop < d.scrollTop) d.scrollTop = li.offsetTop - 4;
    else if (li.offsetTop + li.offsetHeight > d.scrollTop + d.clientHeight) {
      d.scrollTop = li.offsetTop + li.offsetHeight - d.clientHeight + 4;
    }
  }, [buka, aktif, pos]);

  function tombol(e: TekanEvent<HTMLButtonElement>) {
    if (e.ctrlKey || e.metaKey) return;
    if (e.altKey) {
      if (e.key === "ArrowDown") { e.preventDefault(); if (!buka) bukaDaftar(); }
      return;
    }
    if (e.key === "Enter" || e.key === " ") {
      // `preventDefault` mencegah tombol menembakkan `click` sendiri, yang
      // akan membuka lalu menutup daftar dalam satu tekanan.
      e.preventDefault();
      if (buka) pilih(aktif); else bukaDaftar();
      return;
    }
    if (e.key === "Escape") {
      if (buka) { e.preventDefault(); e.stopPropagation(); setBuka(false); }
      return;
    }
    if (e.key === "Tab") {
      // Seperti pilihan bawaan dan pola APG: Tab menetapkan opsi aktif.
      if (buka) pilih(aktif);
      return;
    }
    const n = geserAktif(e.key, buka ? aktif : terpilih, opsi.length);
    if (n !== null) {
      e.preventDefault();
      if (buka) geserKe(n); else bukaDaftar(e.key === "Home" || e.key === "End" ? n : terpilih);
      return;
    }
    if (e.key.length === 1 && /\S/.test(e.key)) {
      const t = performance.now();
      const teks = sambungAwalan(ketik.current.teks, ketik.current.t, e.key, t);
      ketik.current = { teks, t };
      const i = cariAwalan(opsi, teks, buka ? aktif : terpilih);
      if (i >= 0) {
        e.preventDefault();
        if (buka) geserKe(i); else bukaDaftar(i);
      }
    }
  }

  return (
    <div
      className={"pil-kotak" + (kelas ? " " + kelas : "")}
      style={gaya}
      ref={akar}
      // Fokus meninggalkan komponen (Tab, atau klik di luar yang memindahkan
      // fokus): tutup. Fokus yang tetap di tombol saat opsi diklik tidak lewat sini.
      onBlur={(e) => {
        if (!akar.current?.contains(e.relatedTarget as Node | null)) setBuka(false);
      }}
    >
      <button
        type="button"
        id={idTombol}
        ref={pemicu}
        role="combobox"
        className={"pil-pemicu" + (kelasPemicu ? " " + kelasPemicu : "")}
        aria-label={namaTombol}
        aria-haspopup="listbox"
        aria-expanded={buka}
        aria-controls={buka ? idDaftar : undefined}
        aria-activedescendant={buka ? idOpsi(aktif) : undefined}
        onClick={() => (buka ? setBuka(false) : bukaDaftar())}
        onKeyDown={tombol}
      >
        <span className="pil-nilai">{opsi[terpilih]?.nama ?? ""}</span>
        <span className="pil-panah" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor"
               strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M6 9l6 6 6-6" />
          </svg>
        </span>
      </button>
      {buka && pos && wadah
        ? createPortal(
          <ul
            ref={daftar}
            id={idDaftar}
            role="listbox"
            aria-label={label}
            className="pil-daftar"
            data-atas={pos.naik ? "" : undefined}
            style={{ left: pos.left, width: pos.width, top: pos.top, bottom: pos.bottom, maxHeight: pos.maks }}
            // Fokus tidak boleh pindah ke daftar: lihat catatan kepala berkas.
            onPointerDown={(e) => e.preventDefault()}
          >
            {opsi.map((o, i) => (
              <li
                key={o.id}
                id={idOpsi(i)}
                role="option"
                aria-selected={o.id === nilai}
                data-aktif={i === aktif ? "" : undefined}
                onPointerMove={() => {
                  if (i === aktif) return;
                  gulirKeAktif.current = false;
                  setAktif(i);
                }}
                onClick={() => pilih(i)}
              >
                <span>{o.nama}</span>
                {o.id === nilai ? <Ikon nama="selesai" ukuran={16} /> : null}
              </li>
            ))}
          </ul>,
          wadah,
        )
        : null}
    </div>
  );
}
