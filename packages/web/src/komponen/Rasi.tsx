/* Penggambar SVG peta rasi. Port bagian berbau-DOM dari `rasi.js`.
 *
 * Geometrinya tinggal di `rasi-geometri.ts` dan sudah dibuktikan identik
 * dengan `rasi.js` (`uji/banding-rasi.mjs`). Yang di sini cuma bentuk
 * elemennya, jadi perubahan di berkas ini tidak bisa menggeser letak bintang
 * mana pun -- dan itu memang maksud pemisahannya.
 *
 * Kelas CSS-nya TIDAK diubah namanya (`rasi-titik`, `rasi-cahaya`,
 * `rasi-sasaran`, `rasi-garis`, `rasi-reticle`, ...). Semuanya sudah ada di
 * `gaya.css` beserta animasi garis-tergambar dan aturan tingkat geraknya;
 * mengganti namanya berarti menulis ulang gaya yang sudah bekerja.
 */

import { useCallback, useMemo, useRef, useState, type CSSProperties, type PointerEvent, type RefObject } from "react";

import { tingkatGerak } from "../gerak.ts";
import {
  jariBintang,
  KATA_STATUS,
  kelasBintang,
  labelBintang,
  magStatus,
  ruasAntara,
  tataPetaRasi,
  type DataPeta,
  type MateriBintang,
  type Titik,
} from "./rasi-geometri.ts";

/** Satu bintang: titik, cahaya, dan sasaran klik.
 *
 *  Sasaran kliknya SENGAJA lebih besar daripada titiknya. Bintang redup
 *  berjari-jari satu piksel mustahil dikenai mouse, dan materi yang belum
 *  dibaca justru yang paling redup -- jadi tanpa sasaran besar, yang paling
 *  sulit diklik adalah yang paling perlu dibuka. */
export function Bintang({
  materi,
  x,
  y,
  r,
  href,
  dataKey,
  indeks,
  urut,
  kelasEkstra,
  onTunjuk,
}: {
  materi: MateriBintang;
  x: number;
  y: number;
  r: number;
  href?: string;
  dataKey?: string;
  indeks?: number;
  /** Mengisi `--i`, penunda animasi per bintang. */
  urut?: number;
  kelasEkstra?: string;
  onTunjuk?: (el: Element, materi: MateriBintang) => void;
}) {
  const kelas = kelasBintang(materi);
  const isi = (
    <>
      {materi.status === "selesai" && !materi.terkunci ? (
        <circle
          className="rasi-cahaya"
          cx={x.toFixed(1)}
          cy={y.toFixed(1)}
          r={(r * 3.2).toFixed(1)}
        />
      ) : null}
      <circle
        className={"rasi-titik " + kelas}
        cx={x.toFixed(1)}
        cy={y.toFixed(1)}
        r={r.toFixed(2)}
      />
      <circle className="rasi-sasaran" cx={x.toFixed(1)} cy={y.toFixed(1)} r={10} />
    </>
  );

  const sifat = {
    className:
      "rasi-bintang" +
      (materi.terkunci || !href ? " rasi-bintang-kunci" : "") +
      (kelasEkstra ? " " + kelasEkstra : ""),
    "aria-label": labelBintang(materi),
    "data-key": dataKey,
    "data-indeks": indeks,
    style:
      urut === undefined ? undefined : ({ "--i": urut } as CSSProperties),
    // Parameternya `Element`, bukan `SVGElement`: React memetakan `<a>` ke
    // `HTMLAnchorElement` bahkan di dalam SVG, jadi handler yang menuntut
    // `SVGElement` tidak bisa dipasang di keduanya. Yang dibutuhkan `onTunjuk`
    // cuma `getBoundingClientRect`, yang ada di `Element`.
    onPointerOver: onTunjuk
      ? (e: PointerEvent<Element>) => onTunjuk(e.currentTarget, materi)
      : undefined,
  };

  // Yang terkunci bukan tautan: ia tetap DIGAMBAR beserta alasannya di
  // `aria-label`, tapi tidak mengantar ke mana pun. Tombol yang berujung
  // penolakan adalah tombol yang membuat sebuah fitur terasa rusak.
  return materi.terkunci || !href ? (
    <g {...sifat}>{isi}</g>
  ) : (
    <a {...sifat} href={href} tabIndex={-1}>
      {isi}
    </a>
  );
}

/** Braket sudut yang mengunci bintang berikutnya. "Ini sasaranmu". */
export function Reticle({ x, y, r }: { x: number; y: number; r: number }) {
  const R = r + 7;
  // Dua lapis: luar memegang POSISI (atribut transform), dalam boleh diputar
  // CSS. Memutar lapis luar lewat CSS akan menimpa translate-nya.
  return (
    <g
      className="rasi-reticle"
      transform={`translate(${x.toFixed(1)},${y.toFixed(1)})`}
    >
      <g className="rasi-reticle-putar">
        <circle r={R} fill="none" />
        {[0, 90, 180, 270].map((d) => (
          <line
            key={d}
            x1={0}
            y1={-R - 5}
            x2={0}
            y2={-R + 1}
            transform={`rotate(${d})`}
          />
        ))}
      </g>
    </g>
  );
}

/** Garis antara dua bintang. `null` kalau keduanya terlalu dekat. */
export function GarisRasi({
  a,
  b,
  ra,
  rb,
  terang,
  jalur,
  urut,
}: {
  a: Titik;
  b: Titik;
  ra: number;
  rb: number;
  terang?: boolean;
  /** Garis antar-BAB: putus-putus, dan tanpa `pathLength`. */
  jalur?: boolean;
  /** Mengisi `--i`, penunda animasi per anak. */
  urut?: number;
}) {
  const u = ruasAntara(a, b, ra, rb);
  if (!u) return null;
  return (
    <line
      className={
        "rasi-garis" +
        (terang ? " rasi-garis-terang" : "") +
        (jalur ? " rasi-garis-jalur" : "")
      }
      x1={u.x1.toFixed(1)}
      y1={u.y1.toFixed(1)}
      x2={u.x2.toFixed(1)}
      y2={u.y2.toFixed(1)}
      // Garis jalur putus-putus tidak memakai pathLength; lihat visual.js.
      // Ia digambar DASHED oleh CSS, dan `pathLength: 1` menormalkan panjang
      // jalurnya jadi satu satuan -- yang membuat pola putus-putusnya hilang.
      pathLength={jalur ? undefined : 1}
      style={urut === undefined ? undefined : ({ "--i": urut } as CSSProperties)}
    />
  );
}

export interface Tip {
  judul: string;
  ket: string;
  kiri: number;
  atas: number;
}

/**
 * Tip melayang yang dipakai bersama seluruh bintang dalam satu peta.
 *
 * Versi JS menempel satu `<div>` ke wadahnya lalu menggeser `style.left`
 * langsung (`pasangTip`). Di sini posisinya jadi state, tapi pengukurannya
 * tetap dari `getBoundingClientRect` -- satu-satunya cara tahu di mana sebuah
 * bintang SVG berada di layar setelah `viewBox` menskalakannya.
 */
export function useTip(wadahRef: RefObject<HTMLElement | null>) {
  const [tip, setTip] = useState<Tip | null>(null);

  const tunjuk = useCallback(
    (el: Element, judul: string, ket: string) => {
      const wadah = wadahRef.current;
      if (!wadah) return;
      const kotak = wadah.getBoundingClientRect();
      const r = el.getBoundingClientRect();
      setTip({
        judul,
        ket,
        // Dipatok ke dalam wadahnya: tip di bintang paling kanan akan
        // menggantung di luar peta dan memicu gulir horizontal.
        kiri: Math.min(kotak.width - 260, Math.max(0, r.left - kotak.left - 24)),
        atas: r.bottom - kotak.top + 10,
      });
    },
    [wadahRef],
  );

  const sembunyi = useCallback(() => setTip(null), []);

  const elemen = (
    <div
      className={"rasi-tip" + (tip ? " rasi-tip-tampil" : "")}
      style={tip ? { left: tip.kiri + "px", top: tip.atas + "px" } : undefined}
    >
      {tip ? (
        <>
          <b>{tip.judul}</b>
          {tip.ket ? <span>{tip.ket}</span> : null}
        </>
      ) : null}
    </div>
  );

  return { tunjuk, sembunyi, elemen };
}

/** Jari-jari tiap bintang sebuah kurikulum, pada skala tertentu. */
export function jariSemua(materi: MateriBintang[], skala: number): number[] {
  return materi.map((m) => jariBintang(magStatus(m), skala));
}

/** Ref wadah peta, untuk `useTip`. Sekadar gula supaya tipenya tidak diulang. */
export function useWadahPeta() {
  return useRef<HTMLDivElement>(null);
}

/**
 * Peta rasi satu kurikulum. Port `petaRasi()` dari `rasi.js`.
 *
 * Tata letaknya tinggal di `tataPetaRasi()` dan sudah diadu dengan `rasi.js`
 * (`uji/banding-rasi.mjs`), jadi tidak ada koordinat yang bisa bergeser dari
 * berkas ini.
 *
 * Sorot kelompok jadi TURUNAN state, bukan `classList.add` seperti versi JS.
 * Bedanya nyata: versi imperatif harus ingat melepas `.rasi-sorot` dari
 * kelompok sebelumnya pada setiap `pointerover`, dan satu cabang yang lupa
 * melakukannya meninggalkan dua rasi menyala bersamaan -- tanpa satu pun
 * error. Di sini keadaan itu cuma satu angka.
 *
 * Peta ini PELENGKAP: daftar materi di bawahnya tetap jalan utama, bintangnya
 * ber-`tabindex -1`, dan ringkasan teksnya menyampaikan isi yang sama.
 */
export function PetaRasi({ data, tinggi = 250 }: { data: DataPeta; tinggi?: number }) {
  const wadahRef = useWadahPeta();
  const tip = useTip(wadahRef);
  const [sorot, setSorot] = useState<number | null>(null);
  const tata = useMemo(() => tataPetaRasi(data, tinggi), [data, tinggi]);

  const lepas = () => {
    tip.sembunyi();
    setSorot(null);
  };

  return (
    <div
      ref={wadahRef}
      className={"rasi" + (tingkatGerak() === "penuh" ? " rasi-hidup" : "")}
    >
      <p className="rasi-ringkasan">{tata.ringkasan}</p>
      <svg
        viewBox={`0 0 ${tata.W} ${tata.H}`}
        className="rasi-svg"
        preserveAspectRatio="xMidYMid meet"
        onPointerLeave={lepas}
      >
        {/* Jalur antar rasi digambar PALING DULU supaya ia di bawah
            bintangnya -- urutan lapis yang sama dengan versi JS. */}
        <g>
          {tata.jalur.map((j, i) => (
            <GarisRasi key={i} a={j.a} b={j.b} ra={j.ra} rb={j.rb} jalur />
          ))}
        </g>

        <g>
          {tata.kelompok.map((isi, ik) => (
            <g
              key={ik}
              className={"rasi-kelompok" + (sorot === ik ? " rasi-sorot" : "")}
            >
              {isi.map((x, i) =>
                x.jenis === "garis" ? (
                  <GarisRasi
                    key={i}
                    a={x.a}
                    b={x.b}
                    ra={x.ra}
                    rb={x.rb}
                    terang={x.terang}
                    urut={x.urut}
                  />
                ) : (
                  <Bintang
                    key={i}
                    materi={data.materi[x.indeks] as MateriBintang}
                    x={x.x}
                    y={x.y}
                    r={x.r}
                    href={`#/materi/${data.key}/${x.indeks}`}
                    indeks={x.indeks}
                    urut={x.urut}
                    onTunjuk={(el, m) => {
                      setSorot(ik);
                      tip.tunjuk(
                        el,
                        m.judul,
                        m.terkunci ? "Masih terkunci" : (KATA_STATUS[m.status] ?? ""),
                      );
                    }}
                  />
                ),
              )}
            </g>
          ))}
        </g>

        <g>
          {tata.label.map((l, i) => (
            <text
              key={i}
              className="rasi-label-bab"
              x={l.x.toFixed(1)}
              y={l.y.toFixed(1)}
              textAnchor={l.jangkar}
            >
              <tspan className="rasi-nomor">{l.nomor}</tspan>
              {l.judul}
            </text>
          ))}
          {tata.reticle ? (
            <Reticle x={tata.reticle.x} y={tata.reticle.y} r={tata.reticle.r} />
          ) : null}
        </g>
      </svg>
      {tip.elemen}
    </div>
  );
}
