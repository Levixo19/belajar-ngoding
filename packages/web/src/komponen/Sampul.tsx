/** Sampul SVG generatif: hiasan yang mengodekan namanya sendiri.
 *
 *  Geometrinya di `sampul-bentuk.ts`; berkas ini cuma merendernya. Pembagian
 *  itu punya sebab teknis, bukan selera: Node melucuti TIPE dari `.ts` tapi
 *  tidak melucuti JSX dari `.tsx`, jadi hanya berkas `.ts` yang bisa diimpor
 *  pembandingnya.
 *
 *  `aria-hidden` dan `focusable="false"` SELALU, tanpa opsi untuk
 *  mematikannya: gambar ini tidak pernah jadi satu-satunya pembawa
 *  informasi, dan sampul yang bisa difokus papan ketik adalah satu
 *  perhentian tab yang tidak mengantar ke mana pun.
 */

import { useMemo } from "react";
import { rencanaSampul, type OpsiSampul } from "./sampul-bentuk.ts";

export function Sampul({ teks, ...opsi }: { teks: string } & OpsiSampul) {
  // Dihitung sekali per (teks, opsi): `rencanaSampul` menaikkan penomor id
  // tiap kali dipanggil, jadi menghitungnya di tiap render akan membuat
  // `url(#id)` berubah pada setiap render -- dan gradiennya berkedip.
  const r = useMemo(
    () => rencanaSampul(teks, opsi),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [teks, opsi.lebar, opsi.tinggi, opsi.bahasa, opsi.ragam, opsi.kelas,
     opsi.tanda]);

  return (
    <svg
      viewBox={`0 0 ${r.w} ${r.h}`}
      preserveAspectRatio="xMidYMid slice"
      className={("sampul " + r.kelas).trim()}
      aria-hidden="true"
      focusable="false"
      data-ragam={r.ragam}
    >
      <defs>
        <linearGradient id={r.idg + "l"} x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" style={{
            stopColor: `hsl(${r.rona} 30% 50%)`, stopOpacity: 0.22 }} />
          <stop offset="1" style={{
            stopColor: "var(--nyala)", stopOpacity: 0.10 }} />
        </linearGradient>
        <filter id={r.idg + "b"} x="0" y="0" width="100%" height="100%">
          <feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2"
                        stitchTiles="stitch" />
          <feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .09 0" />
        </filter>
      </defs>
      <rect width={r.w} height={r.h} style={{ fill: "var(--kartu)" }} />
      <rect width={r.w} height={r.h} fill={`url(#${r.idg}l)`} />
      {r.bentuk.map((b, i) => {
        const { style, ...sisa } = b.sifat as Record<string, string | number>;
        const props: Record<string, unknown> = { key: i, ...sisa };
        // `style` di sini STRING CSS (dari sumber aslinya), sementara React
        // menuntut objek. Diurai di sini, bukan di lapisan geometri: lapisan
        // itu diadu byte-per-byte dengan `sampul.js`, dan mengubah bentuknya
        // jadi objek akan membuat pembandingnya membandingkan dua bahasa.
        if (typeof style === "string") {
          props.style = Object.fromEntries(
            style.split(";").filter(Boolean).map((d) => {
              const [k, ...v] = d.split(":");
              return [
                k!.trim().replace(/-([a-z])/g, (_, c: string) => c.toUpperCase()),
                v.join(":").trim(),
              ];
            }));
        }
        if (b.tag === "circle") return <circle {...props} />;
        if (b.tag === "rect") return <rect {...props} />;
        if (b.tag === "path") return <path {...props} />;
        return null;
      })}
      {r.tanda ? (
        <text
          x={Math.round(r.w * 0.06 * 10) / 10}
          y={Math.round(r.h * 0.9 * 10) / 10}
          className="sampul-tanda"
          fontSize={Math.round(r.h * 0.34 * 10) / 10}
          style={{ fill: "var(--teks)" }}
        >
          {r.tanda}
        </text>
      ) : null}
      <rect width={r.w} height={r.h} filter={`url(#${r.idg}b)`} />
    </svg>
  );
}
