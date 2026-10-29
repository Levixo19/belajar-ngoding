/* Orbit bekal: kurikulum yang dibutuhkan satu profesi, berputar mengelilingi
 * profesi itu. Dipakai di panel profesi Peta Karier.
 *
 * Padanan `RadialOrbitalTimeline` yang ditempel pemilik, ditulis ulang tanpa
 * lucide, shadcn, maupun Tailwind, dan dengan data sungguhan (lihat
 * `orbit-teks.ts` untuk apa yang dikodekan tiap bagian).
 *
 * Yang sengaja berbeda dari aslinya, masing-masing dengan sebabnya:
 *  - Putaran hanya pada gerak penuh, dan BERHENTI saat penunjuk ada di atas
 *    papan, saat satu simpul difokus, dan saat ada simpul terpilih. Asli:
 *    berhenti hanya saat simpul dibuka, jadi mengklik simpul yang sedang
 *    bergerak sulit. Ada juga tombol Jeda yang terlihat (WCAG 2.2.2: gerak yang
 *    jalan sendiri lebih dari lima detik harus bisa dihentikan).
 *  - Sudutnya ditulis ke DOM lewat ref (`--or-sudut`), tidak jadi state React:
 *    aslinya me-render ulang seluruh komponen tiap 50 ms.
 *  - Rincian simpul tampil di panel di samping papan, bukan kartu yang melayang
 *    di atas simpul. Kartu yang ikut bergeser menutupi simpul tetangganya, dan
 *    tidak punya tempat tetap untuk dibaca pembaca layar (`aria-live`).
 *  - Simpul adalah tombol sungguhan dengan nama lengkap (kurikulum, cincin,
 *    persen, status), bisa dijangkau Tab dan panah, dan Esc melepas pilihan.
 *  - Tidak ada peredupan `opacity` untuk memberi kesan kedalaman: teks yang
 *    diredupkan jatuh di bawah 4,5:1.
 * Daftar bekal di bawahnya (`.kr-bekal`) tetap ada: ia jalur kanonik untuk
 * pembaca layar dan angka persisnya.
 */

import {
  useEffect, useMemo, useRef, useState,
  type CSSProperties, type KeyboardEvent as TekanEvent, type ReactNode,
} from "react";

import { useGerakPenuh } from "./gerak-penuh.ts";
import {
  JARI, KECEPATAN, STATUS_TEKS, bangunNode, labelNode, langkahFokus, ringkasOrbit, sudutBerikut,
  type KelompokOrbit, type KurOrbit,
} from "./orbit-teks.ts";

const KELILING = 2 * Math.PI * 17;

export function OrbitBekal({
  nama,
  kelompok,
  pelengkap,
  kur,
  pusat,
}: {
  nama: string;
  kelompok: KelompokOrbit[];
  pelengkap: string[];
  kur: KurOrbit;
  /** Isi pusat orbit: biasanya cincin kesiapan profesi. */
  pusat: ReactNode;
}) {
  const simpul = useMemo(() => bangunNode(kelompok, pelengkap, kur), [kelompok, pelengkap, kur]);
  const penuh = useGerakPenuh();
  const [aktif, setAktif] = useState<string | null>(null);
  const [jeda, setJeda] = useState(false);
  const [hover, setHover] = useState(false);
  const [fokus, setFokus] = useState(false);
  const papan = useRef<HTMLDivElement>(null);
  const sudut = useRef(0);

  const dipilih = simpul.find((n) => n.id === aktif) ?? null;
  const berkaitan = new Set(dipilih?.setara ?? []);
  const berputar = penuh && !jeda && !hover && !fokus && dipilih === null;

  useEffect(() => {
    if (!berputar) return;
    let raf = 0;
    let t0 = performance.now();
    const bingkai = (t: number) => {
      sudut.current = sudutBerikut(sudut.current, t - t0);
      t0 = t;
      papan.current?.style.setProperty("--or-sudut", `${sudut.current.toFixed(3)}deg`);
      raf = requestAnimationFrame(bingkai);
    };
    raf = requestAnimationFrame(bingkai);
    return () => cancelAnimationFrame(raf);
  }, [berputar]);

  if (simpul.length === 0) return <p className="kr-catatan">{ringkasOrbit(simpul)}</p>;

  const tombol = (e: TekanEvent<HTMLDivElement>) => {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.key === "Escape" && dipilih) {
      e.preventDefault();
      e.stopPropagation();
      setAktif(null);
      return;
    }
    const daftar = [...e.currentTarget.querySelectorAll<HTMLButtonElement>(".or-node")];
    const i = daftar.indexOf(e.target as HTMLButtonElement);
    if (i < 0) return;
    const ke = langkahFokus(e.key, i, daftar.length);
    if (ke !== null) {
      e.preventDefault();
      daftar[ke]?.focus();
    }
  };
  const setaraDengan = dipilih ? simpul.filter((n) => berkaitan.has(n.id)) : [];
  const wakil = dipilih ? simpul.find((n) => n.kelompok === dipilih.kelompok && n.wakil) : undefined;

  return (
    <div className="or-wadah" onKeyDown={tombol}>
      <div className="or-kolom">
        <div
          className="or-papan"
          ref={papan}
          role="group"
          aria-label={`Orbit bekal ${nama}`}
          style={{ "--jd": `${JARI.dalam}cqw`, "--jl": `${JARI.luar}cqw` } as CSSProperties}
          onPointerEnter={() => setHover(true)}
          onPointerLeave={() => setHover(false)}
          onFocus={() => setFokus(true)}
          onBlur={(e) => {
            if (!e.currentTarget.contains(e.relatedTarget as Node | null)) setFokus(false);
          }}
          onClick={(e) => {
            if (e.target === e.currentTarget) setAktif(null);
          }}
        >
          <span className="or-lintasan or-lintasan-dalam" aria-hidden="true" />
          {simpul.some((n) => n.lingkar === "luar") ? (
            <span className="or-lintasan or-lintasan-luar" aria-hidden="true" />
          ) : null}
          <div className="or-pusat">{pusat}</div>
          {simpul.map((n) => (
            <button
              key={n.id}
              type="button"
              className={
                "or-node" + (n.id === dipilih?.id ? " aktif" : "") + (berkaitan.has(n.id) ? " berkaitan" : "")
              }
              data-status={n.status}
              data-lingkar={n.lingkar}
              style={{ "--dasar": `${n.sudut}deg`, "--laju": KECEPATAN[n.lingkar] } as CSSProperties}
              aria-pressed={n.id === dipilih?.id}
              aria-label={labelNode(n)}
              onClick={() => setAktif(n.id === dipilih?.id ? null : n.id)}
            >
              <svg className="or-ring" viewBox="0 0 40 40" aria-hidden="true">
                <circle className="or-ring-jalur" cx="20" cy="20" r="17" />
                {n.persen > 0 ? (
                  <circle
                    className="or-ring-isi"
                    cx="20"
                    cy="20"
                    r="17"
                    strokeDasharray={`${((KELILING * n.persen) / 100).toFixed(2)} ${KELILING.toFixed(2)}`}
                  />
                ) : null}
              </svg>
              <span className="or-persen" aria-hidden="true">{Math.round(n.persen)}%</span>
              <span className="or-nama" aria-hidden="true">{n.label}</span>
            </button>
          ))}
        </div>
        {penuh ? (
          <div className="or-alat">
            <button
              type="button"
              className="tbl tbl-kecil tbl-hantu or-jeda"
              aria-pressed={jeda}
              onClick={() => setJeda(!jeda)}
            >
              {jeda ? "Putar lagi" : "Jeda putaran"}
            </button>
          </div>
        ) : null}
      </div>

      <div className="or-rinci" aria-live="polite" data-status={dipilih?.status}>
        {dipilih ? (
          <>
            <div className="or-rinci-kepala">
              <h4>{dipilih.label}</h4>
              <span className="pil">{STATUS_TEKS[dipilih.status]}</span>
            </div>
            <div className="kr-bekal-bilah" role="img" aria-label={`${Math.round(dipilih.persen)} persen`}>
              <i style={{ width: `${dipilih.persen}%` }} />
            </div>
            <p className="or-rinci-ket">
              {dipilih.lingkar === "luar"
                ? `Pelengkap: membantu ${nama}, tapi tidak dihitung ke kesiapannya.`
                : dipilih.wakil
                  ? `Bekal. Yang terdepan di kelompoknya, jadi inilah yang dihitung ke kesiapan ${nama}.`
                  : `Bekal setara dengan ${wakil?.label ?? "yang lain"}, yang sekarang terdepan dan dihitung ke kesiapan.`}
            </p>
            {setaraDengan.length ? (
              <p className="or-rinci-ket">
                {"Cukup salah satu. Setara dengan "}
                {setaraDengan.map((n, i) => (
                  <span key={n.id}>
                    {i ? ", " : ""}
                    <button type="button" className="or-tautan" onClick={() => setAktif(n.id)}>
                      {`${n.label} (${Math.round(n.persen)}%)`}
                    </button>
                  </span>
                ))}
                .
              </p>
            ) : null}
            <a className="tbl tbl-kecil or-buka" href={"#/bahasa/" + dipilih.kunci}>
              Buka kurikulum
            </a>
          </>
        ) : (
          <>
            <p className="or-rinci-ket">{ringkasOrbit(simpul)}</p>
            <p className="or-rinci-ket">
              Cincin dalam adalah bekal, cincin luar pelengkap. Cincin di tiap simpul menunjukkan
              seberapa banyak kurikulumnya sudah kamu selesaikan. Pilih satu simpul untuk melihat rinciannya.
            </p>
          </>
        )}
      </div>
    </div>
  );
}
