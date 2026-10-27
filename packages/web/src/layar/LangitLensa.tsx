/* Lensa layar Langit: satu rasi, diperbesar sampai tiap bintang bisa ditunjuk.
 *
 * Ini TAMPILAN LAIN atas data yang sama, bukan fitur baru: bentuk rasinya
 * sama dengan di ikhtisar (benih dan `bentukRasi` yang sama), cuma
 * diskalakan 4,5 kali (median jarak tetangga 39 px, lawan 8,65 px di
 * ikhtisar). Di ukuran itu setiap bintang bisa berbentuk per status, berlabel
 * nomor, dan dipilih dengan mouse maupun papan ketik, dan panel di sampingnya
 * terhubung ke bintang yang dipilih lewat garis penunjuk.
 *
 * Model papan ketik: satu perhentian Tab untuk seluruh daftar bintang (pola
 * listbox dengan roving tabindex). Panah memindahkan fokus sepanjang urutan
 * baca (= urutan indeks = garis rasi), Home/End ke ujung, PageUp/PageDown
 * antar-bab, Enter atau Spasi memilih, Escape keluar dari lensa. Tombol yang
 * dipegang bersama Alt, Ctrl, atau Meta bukan milik daftar ini: Alt+Panah
 * adalah Mundur/Maju peramban. Bintang terkunci TETAP bisa difokus dan dipilih:
 * alasannya harus bisa dibaca, dan aturan "bab yang terkunci tetap
 * ditampilkan" berlaku juga untuk papan ketik. Karena ia memang bisa
 * dioperasikan, ia TIDAK diberi `aria-disabled` (itu menyuruh pembaca layar
 * mengumumkan "tidak tersedia" pada butir yang paling perlu dipilih pelajar
 * baru); statusnya ada di namanya ("masih terkunci").
 *
 * Memilih TIDAK membuka materi. Membuka layar materi menulis progres (materi
 * berstatus baru ditandai "sebagian" dan menggerakkan kartu Lanjutkan), jadi
 * itu selalu tindakan eksplisit lewat tombol di panel.
 *
 * Fokus tidak boleh jatuh ke BODY: panel tidak dibongkar-pasang tiap pilihan
 * (kuncinya per rasi, bukan per bintang), dan tombol yang memang mengganti jenis
 * panel mengembalikan fokus ke bintangnya. Esc didengar di tingkat dokumen
 * karena fokus BODY keadaan yang sah (alamat yang baru dimuat, klik ruang
 * kosong).
 */

import { memo, useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";

import { adaGerak, tingkatGerak } from "../gerak.ts";
import { Ikon } from "../komponen/Ikon.tsx";
import { KELAS_GLIF } from "../komponen/Glif.tsx";
import {
  bagianGlif,
  bangunLensa,
  bintangDiBawahKartu,
  CELAH_GULIR,
  deltaGulirPanel,
  deltaGulirTampak,
  jalurPenunjuk,
  pilihSorotLensa,
  KATA_STATUS_BINTANG,
  langkahTombol,
  pathBraket,
  romawi,
  RUANG_TERPILIH,
  sasaranLensa,
  tempatTip,
  type BahasaLangit,
  type BintangLensa,
} from "../komponen/lensa-geometri.ts";
import { kalimatDipilih, labelBintang } from "../komponen/lensa-teks.ts";
import { type MateriBintang } from "../komponen/rasi-geometri.ts";
import { tanpaNomor } from "../util.tsx";
import { Legenda } from "./LangitIkhtisar.tsx";
import { PanelBintang, PanelRasi, useDataB, useDataM, type Berkas } from "./LangitPanel.tsx";
import { TATA, type Profesi } from "./langit-data.ts";

interface Ukuran {
  w: number;
  h: number;
}

function useUkuran<T extends HTMLElement>() {
  const ref = useRef<T>(null);
  const [u, setU] = useState<Ukuran>({ w: 0, h: 0 });
  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) return;
    setU({ w: el.clientWidth, h: el.clientHeight });
    const amat = new ResizeObserver((e) => {
      const r = e[0]?.contentRect;
      if (!r) return;
      setU((lama) =>
        Math.abs(lama.w - r.width) < 0.5 && Math.abs(lama.h - r.height) < 0.5
          ? lama
          : { w: r.width, h: r.height },
      );
    });
    amat.observe(el);
    return () => amat.disconnect();
  }, []);
  return { ref, ...u };
}

/** Bawah pil atas yang melayang (`#rel`): batas atas ruang yang benar-benar
 *  terlihat. 0 bila tidak ada. */
function bawahPilAtas(): number {
  return document.getElementById("rel")?.getBoundingClientRect().bottom ?? 0;
}

/** Gulir jendela (bukan `scrollIntoView`: ia menggulir SEMUA leluhur) sampai
 *  benda ini tampak penuh. `focus({ preventScroll: true })` dipakai di seluruh
 *  lensa, jadi inilah satu-satunya yang menjaga bintang berfokus tetap
 *  terlihat pada zum 125 persen ke atas dan jendela pendek. */
function tampakkan(el: Element) {
  const r = el.getBoundingClientRect();
  const d = deltaGulirTampak(r.top, r.bottom, window.innerHeight, bawahPilAtas());
  if (d !== 0) window.scrollTo({ top: window.scrollY + d, behavior: adaGerak() ? "smooth" : "auto" });
}

/** Faktor ukuran huruf aplikasi (setelan "Ukuran huruf" menggeser `rem`,
 *  bukan piksel): 1 pada 16 px, 1,25 pada 20 px. Dibaca sekali per lensa. */
export function skalaTeksAplikasi(): number {
  try {
    const px = parseFloat(getComputedStyle(document.documentElement).fontSize);
    return Math.min(2, Math.max(1, (Number.isFinite(px) ? px : 16) / 16));
  } catch {
    return 1;
  }
}

/** Satu bintang di daftar. `memo`: pindah fokus mengubah dua opsi saja (yang
 *  lama dan yang baru), bukan seluruh 56. */
const Opsi = memo(function Opsi({
  i, s, judul, berikutnya, fokus, terpilih, cocok, konsepNama, pasangRef, onFokus,
}: {
  i: number;
  s: BintangLensa;
  judul: string;
  berikutnya: boolean;
  fokus: boolean;
  terpilih: boolean;
  cocok: boolean;
  konsepNama: string | null;
  pasangRef: (i: number, el: SVGGElement | null) => void;
  onFokus: (i: number) => void;
}) {
  const bg = bagianGlif(s.status, s.x, s.y, s.r);
  return (
    <g
      ref={(el) => pasangRef(i, el)}
      role="option"
      tabIndex={fokus ? 0 : -1}
      aria-selected={terpilih}
      aria-label={labelBintang({
        indeks: i,
        judul,
        status: s.status,
        berikutnya,
        konsepCocok: cocok ? konsepNama : null,
      })}
      className="lt-opsi"
      onFocus={() => onFokus(i)}
    >
      <circle className="lt-fokus" cx={s.x.toFixed(1)} cy={s.y.toFixed(1)} r={s.r + 12} />
      {cocok ? <circle className="lt-ik-cocok" cx={s.x.toFixed(1)} cy={s.y.toFixed(1)} r={s.r + 4.5} /> : null}
      {bg.isi ? <path className={`${KELAS_GLIF[s.status]} lt-gl-isi`} d={bg.isi} /> : null}
      {bg.tepi ? <path className={`${KELAS_GLIF[s.status]} lt-gl-tepi lt-gl-tebal`} d={bg.tepi} /> : null}
      <text
        className="lt-ln-nomor"
        x={s.label.x.toFixed(1)}
        y={s.label.y.toFixed(1)}
        textAnchor={s.label.jangkar}
        dominantBaseline="central"
        aria-hidden="true"
      >
        {i + 1}
      </text>
    </g>
  );
});

interface Props {
  data: { bahasa: BahasaLangit[]; profesi: Profesi[] };
  kunci: string;
  /** Memindahkan fokus ke daftar bintang begitu lensa tergambar. `false` pada
   *  pemuatan dokumen pertama (jangan merebut fokus dari pelajar yang baru
   *  menempel alamat). */
  fokusAwal: boolean;
  indeks: number | null;
  berkas: Berkas;
  keluarga: string;
  cocok: (m: MateriBintang) => boolean;
  adaKonsep: boolean;
  konsepNama: string | null;
  profesiNama: string | null;
  sebelum: { key: string; label: string } | null;
  sesudah: { key: string; label: string } | null;
  onPilih: (i: number | null) => void;
  onTutup: () => void;
  onKeRasi: (key: string) => void;
  onLepasKonsep: () => void;
  onLepasProfesi: () => void;
}

export function Lensa({
  data, kunci, fokusAwal, indeks, berkas, keluarga, cocok, adaKonsep, konsepNama, profesiNama,
  sebelum, sesudah, onPilih, onTutup, onKeRasi, onLepasKonsep, onLepasProfesi,
}: Props) {
  const b = data.bahasa.find((x) => x.key === kunci) as BahasaLangit;
  const akar = useUkuran<HTMLElement>();
  const kanvas = useUkuran<HTMLElement>();
  // Panel di KANAN atau di BAWAH kanvas: diputuskan CSS (`@container panggung`),
  // dan di sini cuma dibaca dari tata letak yang sungguh terjadi. Angka ambang
  // yang ditulis di dua tempat adalah angka yang suatu hari meleset di salah
  // satunya, dan gejalanya garis penunjuk yang menuju ke ruang kosong.
  const panelRef = useRef<HTMLElement>(null);
  const [dua, setDua] = useState(false);
  useLayoutEffect(() => {
    const k = kanvas.ref.current;
    const p = panelRef.current;
    if (!k || !p) return;
    setDua(p.getBoundingClientRect().left >= k.getBoundingClientRect().right - 1);
  }, [akar.w, kanvas.w, kanvas.ref]);
  const mode = dua ? "kanan" : "bawah";
  const babList = b.bab ?? [];
  const n = b.materi.length;

  const [hidup] = useState(() => tingkatGerak() === "penuh");
  const [skalaTeks] = useState(skalaTeksAplikasi);
  const [hov, setHov] = useState<number | null>(null);
  const [babSorot, setBabSorot] = useState<number | null>(null);
  const berikut = useMemo(() => {
    const i = b.materi.findIndex((m) => m.status !== "selesai" && !m.terkunci);
    return i < 0 ? null : i;
  }, [b]);
  const [fokusI, setFokusI] = useState<number>(indeks ?? berikut ?? 0);
  const [fokusDalam, setFokusDalam] = useState(false);
  // WCAG 1.4.13: kartu judul yang muncul karena hover atau fokus harus bisa
  // ditutup tanpa memindahkan penunjuk atau fokus. Escape pertama menutup
  // kartunya; Escape berikutnya baru keluar dari lensa.
  const [tipTutup, setTipTutup] = useState(false);
  const opsiRef = useRef(new Map<number, SVGGElement>());
  const tipRef = useRef<HTMLDivElement>(null);
  const pasangRef = useCallback((i: number, el: SVGGElement | null) => {
    if (el) opsiRef.current.set(i, el);
    else opsiRef.current.delete(i);
  }, []);

  useEffect(() => {
    if (indeks !== null) setFokusI(indeks);
  }, [indeks]);
  useEffect(() => {
    setTipTutup(false);
  }, [hov, fokusI]);

  const lensa = useMemo(
    () =>
      kanvas.w > 40 && kanvas.h > 40
        ? bangunLensa(b.materi, babList, b.key, {
            lebar: kanvas.w,
            tinggi: kanvas.h,
            tepiX: kanvas.w > 600 ? 72 : 30,
            tepiY: 54,
            skalaTeks,
          })
        : null,
    [b, babList, kanvas.w, kanvas.h, skalaTeks],
  );

  // Fokus masuk ke daftar bintang begitu lensanya selesai digambar (sekali),
  // supaya pembaca papan ketik yang baru menekan Enter pada nama rasi bisa
  // langsung memakai panah. Bintang awalnya: yang dipilih, lalu yang berikutnya.
  const sudahFokus = useRef(false);
  useEffect(() => {
    if (!lensa || sudahFokus.current) return;
    sudahFokus.current = true;
    if (!fokusAwal) return;
    const el = opsiRef.current.get(fokusI);
    el?.focus({ preventScroll: true });
    if (el) tampakkan(el);
  }, [lensa, fokusI, fokusAwal]);

  const babDari = useMemo(() => {
    const x: number[] = Array.from({ length: n }, () => -1);
    babList.forEach((bb, k) => bb.materi.forEach((i) => { x[i] = k; }));
    return x;
  }, [babList, n]);
  const awalBab = useMemo(() => babList.map((bb) => bb.materi[0] ?? -1), [babList]);

  const { data: dataB, galat: galatB } = useDataB(berkas, kunci);
  const mTerpilih = indeks !== null ? b.materi[indeks] : undefined;
  const { data: dataM, galat: galatM } = useDataM(berkas, kunci, indeks, !!mTerpilih?.terkunci);

  // Fokus papan ketik: pindah, lalu pastikan terlihat (gulir jendela, bukan
  // `scrollIntoView`).
  const fokusKe = useCallback((i: number) => {
    setFokusI(i);
    const el = opsiRef.current.get(i);
    el?.focus({ preventScroll: true });
    if (el) tampakkan(el);
  }, []);

  const pilih = useCallback((i: number | null) => {
    onPilih(i);
    if (i !== null) {
      setFokusI(i);
    }
  }, [onPilih]);

  /** Pilih dari panel (bukan dari daftar) lalu kembalikan fokus ke bintangnya:
   *  tombol yang mengganti jenis panel membongkar dirinya, dan fokus yang
   *  hilang jatuh ke BODY. */
  const pilihDariPanel = useCallback((i: number) => {
    pilih(i);
    opsiRef.current.get(i)?.focus({ preventScroll: true });
  }, [pilih]);

  const sasaran = (e: { clientX: number; clientY: number; currentTarget: Element }): BintangLensa | null => {
    if (!lensa) return null;
    const k = e.currentTarget.getBoundingClientRect();
    return sasaranLensa(lensa, e.clientX - k.left, e.clientY - k.top);
  };

  /** Bintang lain yang glifnya ada di bawah penunjuk yang sedang di atas
   *  kartu judul. Kartu hover menangkap penunjuk (WCAG 1.4.13), jadi tanpa ini
   *  bintang yang pusatnya tertutup kartu tetangganya tidak bisa disorot atau
   *  diklik. */
  const dibawahKartu = (e: { clientX: number; clientY: number }): BintangLensa | null => {
    const k = kanvas.ref.current?.getBoundingClientRect();
    if (!lensa || !k || hov === null) return null;
    return bintangDiBawahKartu(lensa, hov, e.clientX - k.left, e.clientY - k.top);
  };

  const terpilihB = lensa && indeks !== null ? lensa.bintang[indeks] : undefined;
  const penunjuk = lensa && terpilihB ? jalurPenunjuk(terpilihB, lensa.lebar, lensa.tinggi, mode) : null;
  const babAktif = babSorot ?? (terpilihB ? terpilihB.bab : -1);
  const tipI = tipTutup ? null : (hov ?? (fokusDalam && fokusI !== indeks ? fokusI : null));
  const tipB = lensa && tipI !== null ? lensa.bintang[tipI] : undefined;
  const bintangBerikut = lensa && berikut !== null ? lensa.bintang[berikut] : undefined;

  const selesai = b.materi.filter((m) => m.status === "selesai").length;
  const jumlahCocok = adaKonsep ? b.materi.filter((m) => cocok(m)).length : 0;
  const nomorBabTerpilih = indeks !== null ? babDari[indeks] ?? -1 : -1;
  const alasan = nomorBabTerpilih >= 0 ? dataB?.bab[nomorBabTerpilih]?.alasan : undefined;
  const pengumuman =
    indeks !== null && mTerpilih
      ? kalimatDipilih({
          judul: mTerpilih.judul,
          status: mTerpilih.terkunci ? "terkunci" : (mTerpilih.status as "selesai" | "sebagian" | "baru"),
          alasan,
        })
      : "";

  // Escape didengar di tingkat DOKUMEN: sesudah klik ruang kosong, klik teks
  // panel, atau muat alamat langsung, fokus ada di BODY dan `onKeyDown` pada
  // <section> tidak pernah menerima tombolnya. Refnya selalu menunjuk logika
  // terbaru, jadi pendengarnya dipasang sekali.
  const escRef = useRef<() => void>(() => {});
  escRef.current = () => {
    if (tipB) {
      setTipTutup(true);
      return;
    }
    if (indeks !== null) {
      onPilih(null);
      const el = opsiRef.current.get(indeks);
      el?.focus({ preventScroll: true });
      if (el) tampakkan(el);
      // Fokus kembali ke bintang yang baru dilepas dan memunculkan kartunya
      // lagi; tanpa ini Esc berikutnya hanya menyembunyikan kartu itu dan
      // keluar dari lensa butuh tiga tekan, padahal kaki lensa menjanjikan
      // satu.
      setTipTutup(true);
      return;
    }
    onTutup();
  };
  useEffect(() => {
    const dengar = (e: KeyboardEvent) => {
      if (e.key !== "Escape" || e.defaultPrevented) return;
      // Dialog global (bantuan, palet) dan menu "Lainnya" cangkang punya
      // Escape-nya sendiri; pendengar dokumen ini jalan lebih dulu daripada
      // pendengar jendela milik menu itu, jadi tanpa pemeriksaan ini satu
      // tekan menutup menu sekaligus melepas pilihan bintang.
      if (document.querySelector(".jendela, #cangkang.rel-buka")) return;
      e.preventDefault();
      escRef.current();
    };
    document.addEventListener("keydown", dengar);
    return () => document.removeEventListener("keydown", dengar);
  }, []);

  // Mode panel-di-bawah: sesudah sebuah bintang DIPILIH, panelnya ada di
  // bawah kanvas dan sering di luar layar. Gulir sampai judulnya tampak.
  // Hanya pada PERUBAHAN pilihan sesudah lensa tergambar (alamat yang baru
  // dimuat tidak menggulir halaman di bawah pembacanya).
  const indeksLama = useRef<number | null>(indeks);
  const lensaRef = useRef(lensa);
  lensaRef.current = lensa;
  useEffect(() => {
    const lama = indeksLama.current;
    indeksLama.current = indeks;
    if (indeks === null || indeks === lama || mode !== "bawah") return;
    const p = panelRef.current;
    const h = p?.querySelector(".lt-panel-kepala h3");
    if (!p || !h) return;
    // Kanvas ada di atas panel: tepi atas penanda bintang terpilih ikut
    // membatasi gulir, supaya bintang di bagian atas kanvas tidak terdorong ke
    // bawah pil atas tepat saat dipilih.
    const sb = lensaRef.current?.bintang[indeks];
    const kanvasAtas = kanvas.ref.current?.getBoundingClientRect().top;
    const d = deltaGulirPanel(
      p.getBoundingClientRect().top,
      h.getBoundingClientRect().bottom,
      window.innerHeight,
      bawahPilAtas(),
      CELAH_GULIR,
      sb && kanvasAtas !== undefined ? kanvasAtas + sb.y - sb.r - RUANG_TERPILIH : undefined,
    );
    if (d !== 0) window.scrollTo({ top: window.scrollY + d, behavior: adaGerak() ? "smooth" : "auto" });
  }, [indeks, mode]);

  const dipanah = (e: React.KeyboardEvent) => {
    // Alt+Panah = Mundur/Maju peramban, Ctrl atau Meta + Home/End = gulir
    // dokumen: bukan milik daftar bintang.
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    const ke = langkahTombol(e.key, fokusI, n, babDari, awalBab, {
      alt: e.altKey, ctrl: e.ctrlKey, meta: e.metaKey,
    });
    if (ke !== null) {
      e.preventDefault();
      fokusKe(ke);
    } else if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      pilih(fokusI);
    }
  };

  return (
    <section
      ref={akar.ref}
      className={"lt-lensa" + (hidup ? " lt-lensa-hidup" : "")}
      aria-labelledby="lt-lensa-judul"
      style={{ "--lt-skala": skalaTeks } as React.CSSProperties}
    >
      <header className="lt-lensa-kepala">
        <button type="button" className="tbl tbl-kecil tbl-hantu lt-lensa-balik" onClick={onTutup}>
          <Ikon nama="kembali" ukuran={15} />
          Semua rasi
        </button>
        <div className="lt-lensa-judul">
          <h2 id="lt-lensa-judul">{b.label}</h2>
          <span className="mata">{keluarga}</span>
          <p>{`${selesai} dari ${n} materi sudah dibaca`}</p>
        </div>
        <div className="lt-lensa-alat">
          {konsepNama ? (
            <button type="button" className="tbl tbl-kecil tbl-pilih" onClick={onLepasKonsep}>
              {`Konsep: ${konsepNama} · ${jumlahCocok} cocok`}
              <span aria-hidden="true"> ×</span>
              <span className="lt-sr"> (lepas)</span>
            </button>
          ) : null}
          {profesiNama ? (
            <button type="button" className="tbl tbl-kecil tbl-pilih" onClick={onLepasProfesi}>
              {`Profesi: ${profesiNama}`}
              <span aria-hidden="true"> ×</span>
              <span className="lt-sr"> (lepas)</span>
            </button>
          ) : null}
          {sebelum ? (
            <button type="button" className="tbl tbl-kecil tbl-hantu" onClick={() => onKeRasi(sebelum.key)}>
              <Ikon nama="kembali" ukuran={14} />
              {sebelum.label}
            </button>
          ) : null}
          {sesudah ? (
            <button type="button" className="tbl tbl-kecil tbl-hantu" onClick={() => onKeRasi(sesudah.key)}>
              {sesudah.label}
              <Ikon nama="lanjut" ukuran={14} />
            </button>
          ) : null}
        </div>
      </header>

      <div className="lt-lensa-isi" data-mode={mode}>
        <figure className="lt-lensa-kanvas" ref={kanvas.ref} data-kel={TATA[kunci]?.[2] ?? "tech"}>
          {lensa ? (
            <svg
              className="lt-ln-svg"
              width={lensa.lebar}
              height={lensa.tinggi}
              viewBox={`0 0 ${lensa.lebar} ${lensa.tinggi}`}
              style={{ cursor: hov !== null ? "pointer" : undefined }}
              onPointerMove={(e) => {
                if (e.pointerType === "touch") return;
                const s = sasaran(e);
                const k = e.currentTarget.getBoundingClientRect();
                const dipilih = lensa
                  ? pilihSorotLensa(
                      hov !== null ? (lensa.bintang[hov] ?? null) : null, s,
                      e.clientX - k.left, e.clientY - k.top, lensa.lebar, lensa.tinggi,
                    )
                  : s;
                setHov(dipilih ? dipilih.i : null);
              }}
              onPointerLeave={(e) => {
                // Pindah ke kartu judul bukan meninggalkan bintangnya.
                if (tipRef.current && tipRef.current.contains(e.relatedTarget as Node | null)) return;
                setHov(null);
              }}
              onClick={(e) => {
                const s = sasaran(e);
                if (s) {
                  pilih(s.i);
                  opsiRef.current.get(s.i)?.focus({ preventScroll: true });
                } else if (indeks !== null) {
                  onPilih(null);
                }
              }}
            >
              <defs>
                <radialGradient id="rasi-ln-halo-gradien">
                  <stop offset="0" className="lt-ln-henti-a" />
                  <stop offset="1" className="lt-ln-henti-b" />
                </radialGradient>
              </defs>
              <g aria-hidden="true">
                {lensa.bintang.map((s) =>
                  s.status === "selesai" ? (
                    <circle
                      key={"h" + s.i}
                      className="lt-ln-halo"
                      cx={s.x.toFixed(1)}
                      cy={s.y.toFixed(1)}
                      r={(s.r * 3.4).toFixed(1)}
                    />
                  ) : null,
                )}
                {lensa.garis.map((g) => {
                  const a = lensa.bintang[g.dari] as BintangLensa;
                  const c = lensa.bintang[g.ke] as BintangLensa;
                  const tuntas = a.status === "selesai" && c.status === "selesai";
                  return (
                    <line
                      key={g.dari}
                      className={
                        "lt-ln-garis" +
                        (tuntas ? " lt-ln-garis-tuntas" : "") +
                        (g.bab === babAktif ? " lt-ln-garis-aktif" : "")
                      }
                      x1={g.x1.toFixed(1)}
                      y1={g.y1.toFixed(1)}
                      x2={g.x2.toFixed(1)}
                      y2={g.y2.toFixed(1)}
                    />
                  );
                })}
                {penunjuk && terpilihB ? (
                  <>
                    <path className="lt-ln-penunjuk" d={penunjuk.d} />
                    <circle className="lt-ln-ujung" cx={penunjuk.ujungX} cy={penunjuk.ujungY} r={3.5} />
                  </>
                ) : null}
                {lensa.bab.map((lb, k) =>
                  lb.awal < 0 ? null : (
                    <g
                      key={lb.nomor}
                      className={"lt-ln-bab" + (k === babAktif ? " lt-ln-bab-aktif" : "")}
                    >
                      <rect
                        x={(lb.x - lb.w / 2).toFixed(1)}
                        y={(lb.y - lb.h / 2).toFixed(1)}
                        width={lb.w}
                        height={lb.h}
                        rx={lb.h / 2}
                      />
                      <text x={lb.x.toFixed(1)} y={lb.y.toFixed(1)} textAnchor="middle" dominantBaseline="central">
                        {romawi(lb.nomor)}
                      </text>
                    </g>
                  ),
                )}
                {bintangBerikut ? (
                  <path
                    className="lt-ln-braket"
                    d={pathBraket(bintangBerikut.x, bintangBerikut.y, bintangBerikut.r + 9, 7)}
                  />
                ) : null}
                {lensa.berikut ? (
                  <g className="lt-ln-berikut">
                    <rect
                      x={(lensa.berikut.x - lensa.berikut.w / 2).toFixed(1)}
                      y={(lensa.berikut.y - lensa.berikut.h / 2).toFixed(1)}
                      width={lensa.berikut.w}
                      height={lensa.berikut.h}
                      rx={lensa.berikut.h / 2}
                    />
                    <text
                      x={lensa.berikut.x.toFixed(1)}
                      y={lensa.berikut.y.toFixed(1)}
                      textAnchor="middle"
                      dominantBaseline="central"
                    >
                      berikutnya
                    </text>
                  </g>
                ) : null}
                {terpilihB ? (
                  <g
                    className="lt-ln-terpilih"
                    style={{ transform: `translate(${terpilihB.x.toFixed(1)}px, ${terpilihB.y.toFixed(1)}px)` }}
                  >
                    <circle className="lt-ln-terpilih-isi" r={terpilihB.r + RUANG_TERPILIH} />
                    <circle className="lt-ln-terpilih-cincin" r={terpilihB.r + 6} />
                  </g>
                ) : null}
                {hov !== null && hov !== indeks && lensa.bintang[hov] ? (
                  <circle
                    className="lt-ln-sorot"
                    cx={(lensa.bintang[hov] as BintangLensa).x.toFixed(1)}
                    cy={(lensa.bintang[hov] as BintangLensa).y.toFixed(1)}
                    r={(lensa.bintang[hov] as BintangLensa).r + 5}
                  />
                ) : null}
              </g>

              <g
                role="listbox"
                aria-label={`Bintang ${b.label}: ${n} materi`}
                onKeyDown={dipanah}
                onFocus={(e) => {
                  // Tip fokus hanya untuk fokus PAPAN KETIK. Fokus yang diberikan
                  // program sesudah klik tetikus (`:focus-visible` salah) tidak
                  // boleh memunculkan kartu judul di atas bintang yang baru
                  // dilihat.
                  let tampak = false;
                  try {
                    tampak = (e.target as Element).matches(":focus-visible");
                  } catch {
                    tampak = false;
                  }
                  setFokusDalam(tampak);
                }}
                onBlur={(e) => {
                  if (!e.currentTarget.contains(e.relatedTarget as Node | null)) setFokusDalam(false);
                }}
              >
                {(babList.length ? babList : [{ nomor: 0, judul: b.label, materi: b.materi.map((_m, i) => i) }]).map((bb) => (
                  <g
                    key={bb.nomor}
                    role="group"
                    aria-label={babList.length ? `Bab ${romawi(bb.nomor)}: ${bb.judul}` : b.label}
                  >
                    {bb.materi.map((i) => {
                      const m = b.materi[i] as MateriBintang;
                      return (
                        <Opsi
                          key={i}
                          i={i}
                          s={lensa.bintang[i] as BintangLensa}
                          judul={m.judul}
                          berikutnya={i === berikut}
                          fokus={fokusI === i}
                          terpilih={indeks === i}
                          cocok={adaKonsep && cocok(m)}
                          konsepNama={konsepNama}
                          pasangRef={pasangRef}
                          onFokus={setFokusI}
                        />
                      );
                    })}
                  </g>
                ))}
              </g>
            </svg>
          ) : null}
          {lensa && tipB && b.materi[tipB.i] ? (
            (() => {
              const t = tempatTip(tipB, lensa.lebar, lensa.tinggi);
              if (!t) return null;
              return (
                <div
                  ref={tipRef}
                  className="lt-ln-tip"
                  data-sisi={t.sisi}
                  // Hanya kartu HOVER yang bisa dilayangi. Kartu fokus papan ketik
                  // menetap di bintangnya dan, kalau menangkap penunjuk, menutup
                  // hover bintang-bintang di bawahnya.
                  data-hover={hov !== null ? "ya" : undefined}
                  aria-hidden="true"
                  style={{ left: t.kiri + "px", top: t.atas + "px" }}
                  // Kartu hover menangkap penunjuk, jadi bintang yang pusatnya
                  // di bawahnya hanya bisa dicapai kalau kartu meneruskan sorot
                  // dan klik ke bintang itu (terukur: 21 sampai 28 persen
                  // perpindahan antar-bintang salah sebelum ini).
                  onPointerMove={(e) => {
                    if (e.pointerType === "touch") return;
                    const o = dibawahKartu(e);
                    if (o) setHov(o.i);
                  }}
                  onClick={(e) => {
                    const o = dibawahKartu(e);
                    if (!o) return;
                    pilih(o.i);
                    opsiRef.current.get(o.i)?.focus({ preventScroll: true });
                  }}
                  onPointerLeave={(e) => {
                    // Kembali ke svg = masih bintang itu; ke mana pun lainnya, selesai.
                    if (!(e.relatedTarget instanceof Element && e.relatedTarget.closest(".lt-ln-svg"))) setHov(null);
                  }}
                >
                  <b>{tanpaNomor((b.materi[tipB.i] as MateriBintang).judul)}</b>
                  <span>
                    {`Materi ${tipB.i + 1} · ${tipB.status === "terkunci" ? "masih terkunci" : KATA_STATUS_BINTANG[tipB.status]}`}
                  </span>
                </div>
              );
            })()
          ) : null}
        </figure>

        <aside
          ref={panelRef}
          className="lt-panel"
          aria-label={indeks !== null ? "Detail bintang" : `Ringkasan rasi ${b.label}`}
          style={
            penunjuk
              ? ({
                  "--ujung-y": `${penunjuk.ujungY.toFixed(0)}px`,
                  "--ujung-x": `${penunjuk.ujungX.toFixed(0)}px`,
                } as React.CSSProperties)
              : undefined
          }
          data-ada-ujung={penunjuk ? "ya" : undefined}
        >
          {indeks !== null && mTerpilih ? (
            // Kuncinya per RASI, bukan per bintang: panel tidak punya state,
            // dan memasangnya ulang tiap pilihan membuang tombol yang sedang
            // berfokus (Sebelumnya, Sesudahnya) ke BODY.
            <PanelBintang
              key={kunci}
              b={b}
              i={indeks}
              dataB={dataB}
              galatB={galatB}
              deskripsi={dataM}
              galatDeskripsi={galatM}
              memuatDeskripsi={!mTerpilih.terkunci && dataM === null && galatM === null}
              profesi={data.profesi}
              berikut={berikut}
              onPilih={pilih}
              onKosong={() => {
                onPilih(null);
                opsiRef.current.get(indeks as number)?.focus({ preventScroll: true });
              }}
            />
          ) : (
            <PanelRasi
              b={b}
              dataB={dataB}
              berikut={berikut}
              babSorot={babSorot}
              onPilih={pilihDariPanel}
              onSorotBab={setBabSorot}
              keluarga={keluarga}
            />
          )}
        </aside>
      </div>

      <div className="lt-lensa-kaki">
        <Legenda />
        <p className="lt-bantuan">
          Panah pindah bintang, Enter memilih, PageUp dan PageDown pindah bab, Esc kembali ke peta.
        </p>
      </div>
      <p className="lt-sr" role="status">
        {pengumuman}
      </p>
    </section>
  );
}
