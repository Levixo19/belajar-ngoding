/* Ikhtisar layar Langit: 32 rasi sebagai SATU peta, dibaca dari jauh.
 *
 * Pekerjaannya sempit dan sengaja begitu: menjawab "kurikulum mana, dan sudah
 * sejauh apa". Bintang satu per satu tidak dipilih di sini; memilih sebuah
 * rasi membuka lensa (`LangitLensa`), tempat tiap bintang cukup besar untuk
 * ditunjuk. Pembagian itu menjawab dua hal yang tidak terjawab oleh peta
 * 1.062 bintang yang masing-masing bisa diklik:
 *
 * * Kepadatan. Jarak tetangga median cuma 8,65 px di 1905 dan 6,49 px di 1440,
 *   jadi glif berbentuk per status tidak muat di sini. Di sini status dibaca
 *   dari ukuran dan terang (pola), dan bentuk per status baru dipakai di lensa.
 * * Salah sasaran. Sasaran klik lama r=10 saling tumpang dan 66 persen klik
 *   tepat di pusat bintang mengenai TETANGGANYA, yang lalu membuka materi lain
 *   dan menandainya "sebagian" di catatan belajar. Di sini klik hanya membuka
 *   lensa, dan membuka materi sungguhan selalu tindakan eksplisit di panel.
 *
 * Anggaran gerak: tidak ada animasi tak berhingga dan tidak ada animasi per
 * bintang. Lapis statis dibungkus `memo` supaya hover tidak merender ulang
 * 1.062 bintang, dan hover cuma menyentuh lapis sorot yang berisi paling
 * banyak tiga simpul.
 */

import {
  Fragment,
  memo,
  useCallback,
  useEffect,
  useLayoutEffect,
  useMemo,
  useRef,
  useState,
} from "react";

import { tingkatGerak } from "../gerak.ts";
import { tanpaNomor } from "../util.tsx";
import { Glif, KELAS_GLIF } from "../komponen/Glif.tsx";
import {
  bagianGlif,
  bangunIkhtisar,
  KATA_STATUS_BINTANG,
  lingkaran,
  pathBraket,
  padWilayah,
  pathWilayah,
  ruasIkhtisar,
  sasaranIkhtisar,
  LEBAR_PETA,
  TINGGI_PETA,
  URUTAN_STATUS,
  type BintangPeta,
  type Ikhtisar,
} from "../komponen/lensa-geometri.ts";
import type { MateriBintang, Titik } from "../komponen/rasi-geometri.ts";
import { kataMulai, labelRasi } from "../komponen/lensa-teks.ts";
import { KELUARGA, TATA, URUTAN_KELUARGA, type Jawaban, type Saran } from "./langit-data.ts";

interface Sorot {
  rasi: number;
  /** Bintang yang ditunjuk persis (dalam jangkauan), atau `null`. */
  bintang: BintangPeta | null;
}

interface Props {
  data: Jawaban;
  saran: Saran | null;
  cocok: (m: MateriBintang) => boolean;
  adaKonsep: boolean;
  konsepNama: string | null;
  /** Jumlah materi yang cocok dengan konsep, per kunci kurikulum. */
  cocokPer: Readonly<Record<string, number>>;
  bekal: ReadonlySet<string>;
  adaProfesi: boolean;
  profesiNama: string | null;
  kelompok: string[][];
  onBuka: (key: string, indeks: number | null) => void;
  /** Lebar akar layar (px): lebar awal wadah saat ia masih `hidden`. */
  lebarAkar: number;
}

/** Lebar wadah, diukur sesudah tata letak dan setiap ia berubah.
 *
 *  `lebarAwal` dipakai selama wadah belum bisa diukur (lebar nol): ikhtisar
 *  dibuka PERTAMA kali saat lensa sudah terbuka (Kembali dari materi, alamat
 *  `#/langit/<key>`), jadi ia tergambar di dalam wadah `hidden`. Tanpa nilai
 *  awal itu tautan nama rasi belum ada ketika lensa ditutup, dan fokus tidak
 *  punya tempat kembali (terukur: fokus jatuh ke BODY). Wadahnya selebar
 *  min(akar layar, 1800), jadi pemanggil bisa menghitungnya dari akar. */
export function useLebar<T extends HTMLElement>(lebarAwal = 0) {
  const ref = useRef<T>(null);
  const [lebar, setLebar] = useState(lebarAwal);
  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) return;
    setLebar(el.clientWidth || lebarAwal);
    const amat = new ResizeObserver((e) => {
      const w = e[0]?.contentRect.width ?? 0;
      // Lebar nol = wadahnya disembunyikan (`hidden` saat lensa terbuka),
      // bukan berubah ukuran. Menuruti angka itu membuang seluruh peta, dan
      // saat lensa ditutup petanya baru tergambar SESUDAH efek pemulihan
      // fokus berjalan.
      if (w === 0) return;
      setLebar((lama) => (Math.abs(lama - w) < 0.5 ? lama : w));
    });
    amat.observe(el);
    return () => amat.disconnect();
  }, []);
  return { ref, lebar };
}

/** Posisi sebuah rasi dalam urutan peta (`TATA`); yang tak terdaftar di akhir. */
const urutPeta = (key: string): number => {
  const i = Object.keys(TATA).indexOf(key);
  return i < 0 ? 1e6 : i;
};

const persen = (v: number, total: number): string => `${((100 * v) / total).toFixed(3)}%`;

/** Lapis statis: lintang, cahaya, garis, dan bintang tiap rasi. `memo`, dan
 *  semua propsnya stabil antar hover. */
const Statis = memo(function Statis({
  ik,
  cocok,
  adaKonsep,
  data,
}: {
  ik: Ikhtisar;
  cocok: (m: MateriBintang) => boolean;
  adaKonsep: boolean;
  data: Jawaban;
}) {
  return (
    <g>
      {ik.rasi.map((r, ri) => {
        const bahasa = data.bahasa[ri];
        const dBiasa: string[] = [];
        const dTuntas: string[] = [];
        for (let i = 1; i < r.bintang.length; i++) {
          if (r.awalBab.has(i)) continue;
          const a = r.bintang[i - 1] as BintangPeta;
          const b = r.bintang[i] as BintangPeta;
          const u = ruasIkhtisar([a.x, a.y], [b.x, b.y], a.r, b.r);
          if (!u) continue;
          const d = `M${u.x1.toFixed(1)},${u.y1.toFixed(1)}L${u.x2.toFixed(1)},${u.y2.toFixed(1)}`;
          (a.status === "selesai" && b.status === "selesai" ? dTuntas : dBiasa).push(d);
        }
        // Satu path per status. Saringan konsep MENAMBAH sebuah cincin pada
        // bintang yang cocok; bintang yang tidak cocok tidak diredupkan:
        // bintang samar di atas latar terang (nomor dan cincin fokus ikut
        // pudar) justru yang dilarang brief.
        const grup = new Map<string, { isi: string[]; tepi: string[] }>();
        const cincin: string[] = [];
        r.bintang.forEach((b) => {
          const m = bahasa?.materi[b.i] as MateriBintang;
          const g = grup.get(b.status) ?? { isi: [], tepi: [] };
          const bg = bagianGlif(b.status, b.x, b.y, b.r);
          if (bg.isi) g.isi.push(bg.isi);
          if (bg.tepi) g.tepi.push(bg.tepi);
          grup.set(b.status, g);
          if (adaKonsep && cocok(m)) cincin.push(lingkaran(b.x, b.y, b.r + 3.6));
        });
        return (
          <g key={r.key}>
            {dBiasa.length ? <path className="lt-ik-garis" d={dBiasa.join("")} /> : null}
            {dTuntas.length ? (
              <path className="lt-ik-garis lt-ik-garis-tuntas" d={dTuntas.join("")} />
            ) : null}
            {URUTAN_STATUS.map((st) => {
              const g = grup.get(st);
              if (!g) return null;
              return [
                g.isi.length ? (
                  <path key={st + "i"} className={`${KELAS_GLIF[st]} lt-gl-isi`} d={g.isi.join("")} />
                ) : null,
                g.tepi.length ? (
                  <path key={st + "t"} className={`${KELAS_GLIF[st]} lt-gl-tepi`} d={g.tepi.join("")} />
                ) : null,
              ];
            })}
            {cincin.length ? <path className="lt-ik-cocok" d={cincin.join("")} /> : null}
          </g>
        );
      })}
    </g>
  );
});

/** Cahaya tiap rasi: SATU elemen dengan banyak `radial-gradient` sebagai latar,
 *  DI BELAKANG svg. Warna dasarnya warna KELUARGA (mengodekan kelompok yang
 *  benar), inti hijau di atasnya sebanding kemajuan membaca (mengodekan hal
 *  yang benar; nol di profil baru). Di dalam svg, 32 lingkaran bergradien itu
 *  ikut digambar ulang setiap kali sorot berpindah (sekitar 0,6 ms per gerakan
 *  pada CPU 4x); sebagai latar elemen sendiri ia digambar sekali. */
const Cahaya = memo(function Cahaya({
  ik,
  bekal,
  adaProfesi,
}: {
  ik: Ikhtisar;
  bekal: ReadonlySet<string>;
  adaProfesi: boolean;
}) {
  const jari = 112 * ik.skala;
  const lapis: string[] = [];
  const ukuran: string[] = [];
  const letak: string[] = [];
  // Tiap gradien dibatasi ke kotaknya sendiri (2 x jari-jari). Tanpa itu
  // 64 lapis menggambar seluruh kotak 1800x1826 padahal di luar jari-jarinya
  // transparan, dan satu langkah ubah ukuran jendela menahan 2 sampai 6 detik
  // di Chrome headless (sekitar 60 ms tanpa latar ini). Sekarang sekitar 60 ms
  // dengan latar. Tampilannya sama dengan mata; piksel tidak identik byte demi
  // byte (selisih paling besar 8 dari 255, hampir semuanya 1 sampai 2), karena
  // gradien kini dirasterisasi per kotak kecil.
  const tambah = (gradien: (pusat: string) => string, r: { cx: number; cy: number }) => {
    const sisi = `${(2 * jari).toFixed(1)}px`;
    lapis.push(gradien(`${jari.toFixed(1)}px ${jari.toFixed(1)}px`));
    ukuran.push(`${sisi} ${sisi}`);
    letak.push(`${(r.cx - jari).toFixed(1)}px ${(r.cy - jari).toFixed(1)}px`);
  };
  for (const r of ik.rasi) {
    const frak = r.jumlah ? r.selesai / r.jumlah : 0;
    if (frak > 0) {
      const f = (0.3 + 0.7 * frak).toFixed(3);
      tambah(
        (pos) =>
          `radial-gradient(circle ${jari.toFixed(1)}px at ${pos}, color-mix(in srgb, var(--lg-selesai) calc(var(--lt-maju) * ${f}${adaProfesi && !bekal.has(r.key) ? " * 0.34" : ""}), transparent), transparent)`,
        r,
      );
    }
    // Rasi di luar bekal profesi: yang diredupkan CAHAYANYA (dekoratif),
    // bukan bintang, garis, atau namanya. Peredupan lewat `opacity` pada
    // teks dan glif menurunkan nama rasi ke 2,1-2,9:1 dan nomor bintang ke
    // 1,6:1, dan itu tautan dan bintang yang masih bisa dipakai.
    const redup = adaProfesi && !bekal.has(r.key) ? " * 0.34" : "";
    tambah(
      (pos) =>
        `radial-gradient(circle ${jari.toFixed(1)}px at ${pos}, color-mix(in srgb, var(--lt-kel-${r.keluarga}) calc(var(--lt-cahaya)${redup}), transparent), transparent)`,
      r,
    );
  }
  return (
    <div
      className="lt-ik-cahaya"
      aria-hidden="true"
      style={{
        backgroundImage: lapis.join(","),
        backgroundSize: ukuran.join(","),
        backgroundPosition: letak.join(","),
        backgroundRepeat: "no-repeat",
      }}
    />
  );
});

/** Garis lintang dan bujur: kertas peta. Dekoratif, di bawah segalanya. */
function Lintang({ s }: { s: number }) {
  const kutub: Titik = [700 * s, -420 * s];
  const lingkar = [];
  for (let k = 0; k < 7; k++) {
    const rr = (560 + k * 270) * s;
    lingkar.push(<circle key={"l" + k} cx={kutub[0].toFixed(1)} cy={kutub[1].toFixed(1)} r={rr.toFixed(1)} />);
  }
  const jari = [];
  for (let a = 55; a <= 125; a += 10) {
    const rad = (a * Math.PI) / 180;
    jari.push(
      <line
        key={"b" + a}
        x1={kutub[0].toFixed(1)}
        y1={kutub[1].toFixed(1)}
        x2={(kutub[0] + Math.cos(rad) * 2600 * s).toFixed(1)}
        y2={(kutub[1] + Math.sin(rad) * 2600 * s).toFixed(1)}
      />,
    );
  }
  return (
    <g className="lt-ik-lintang" aria-hidden="true">
      {lingkar}
      {jari}
    </g>
  );
}

export function Ikhtisar({
  data, saran, cocok, adaKonsep, konsepNama, cocokPer, bekal, adaProfesi, profesiNama, kelompok, onBuka, lebarAkar,
}: Props) {
  const { ref: wadahRef, lebar } = useLebar<HTMLDivElement>(Math.min(lebarAkar, 1800));
  const svgRef = useRef<SVGSVGElement>(null);
  // Sorot (wilayah rasi, cincin bintang, nama bersorot) SENGAJA tidak jadi
  // state React: hover merender ulang seluruh `Ikhtisar` di tiap gerakan
  // kursor yang berganti sasaran, dan itu yang dulu membuat hover lebih mahal
  // daripada peta lama tanpa reticle (selisih 6 sampai 8 ms per gerakan pada
  // CPU 4x terisolasi; mesin berderau, ulangi sebelum percaya satu angka).
  // Sorot ditulis langsung ke DOM lewat `terapkanSorot`, satu kali per bingkai.
  const sorotRef = useRef<Sorot | null>(null);
  const wilayahRef = useRef<SVGPathElement>(null);
  const cincinRef = useRef<SVGCircleElement>(null);
  const namaAktifRef = useRef<Element | null>(null);
  const gerakRef = useRef<{ x: number; y: number } | null>(null);
  const bingkaiRef = useRef(0);
  // Satu-satunya animasi masuk: peta memudar sekali (420 ms, dua elemen),
  // hanya di tingkat gerak penuh. Dibaca SEKALI saat pemasangan dan dilepas
  // sesudah selesai, supaya menutup lensa tidak memudarkannya lagi.
  const [hidup, setHidup] = useState(() => tingkatGerak() === "penuh");
  const pilRef = useRef<HTMLAnchorElement>(null);
  const [posPil, setPosPil] = useState<{ left: number; top: number } | null>(null);

  const skala = lebar > 0 ? lebar / LEBAR_PETA : 0;
  const ik = useMemo(
    () => (skala > 0 ? bangunIkhtisar(data.bahasa, TATA, skala) : null),
    [data, skala],
  );

  const bintangSaran = useMemo(() => {
    if (!ik || !saran) return null;
    const r = ik.rasi.find((x) => x.key === saran.bahasa);
    const b = r?.bintang[saran.indeks];
    return b && b.status !== "terkunci" ? b : null;
  }, [ik, saran]);

  // Letak penanda "mulai di sini": lima calon di sekeliling bintangnya, dan
  // yang dipakai yang pertama tidak menimpa nama rasi atau judul keluarga.
  // Diukur dari kotak sungguhan (teksnya HTML, lebarnya bergantung huruf), jadi
  // tidak bisa dihitung di `lensa-geometri.ts`.
  useLayoutEffect(() => {
    const pil = pilRef.current;
    const wadah = wadahRef.current;
    if (!pil || !wadah || !bintangSaran) {
      setPosPil(null);
      return;
    }
    const hitung = () => {
      const k = wadah.getBoundingClientRect();
      // Ukuran PECAHAN (offsetWidth membulatkan): kapsul 25,19 px tinggi yang dianggap
      // 25 menyentuh sebuah bintang 0,04 px dan lolos dari pemeriksaan.
      const { width: w, height: h } = pil.getBoundingClientRect();
      const kotak = [...wadah.querySelectorAll(".lt-nama, .lt-keluarga")].map((e) => {
        const r = e.getBoundingClientRect();
        return { x0: r.left - k.left, y0: r.top - k.top, x1: r.right - k.left, y1: r.bottom - k.top };
      });
      const { x, y } = bintangSaran;
      // Lima calon dekat bintang, lalu cincin yang makin jauh (16 arah x 5 jarak):
      // lingkungan bintang pertama sebuah rasi padat, jadi lima calon saja
      // semuanya menyentuh bintang dan yang dipakai calon pertama.
      const calon: Array<{ left: number; top: number }> = [
        { left: x + 12, top: y - h - 10 },
        { left: x - w - 12, top: y - h - 10 },
        { left: x + 16, top: y - h / 2 },
        { left: x - w - 16, top: y - h / 2 },
        { left: x + 12, top: y + 12 },
      ];
      for (const jarak of [24, 36, 48, 64, 84, 110, 140]) {
        for (let a = 0; a < 16; a++) {
          const sudut = (a * Math.PI) / 8 - Math.PI / 2;
          calon.push({
            left: x + Math.cos(sudut) * (jarak + w / 2) - w / 2,
            top: y + Math.sin(sudut) * (jarak + h / 2) - h / 2,
          });
        }
      }
      const kena = (c: { left: number; top: number }) =>
        (ik?.semua ?? []).filter(
          (b) => b.x + b.r > c.left - 1 && b.x - b.r < c.left + w + 1 && b.y + b.r > c.top - 1 && b.y - b.r < c.top + h + 1,
        ).length;
      const bebas = (c: { left: number; top: number }) =>
        c.left >= 4 && c.top >= 4 && c.left + w <= k.width - 4 && c.top + h <= k.height - 4 &&
        kotak.every((o) => !(c.left < o.x1 && c.left + w > o.x0 && c.top < o.y1 && c.top + h > o.y0));
      const sah = calon.filter(bebas);
      // Yang pertama (terdekat dengan bintangnya) yang tidak menyentuh bintang
      // mana pun; kalau semuanya menyentuh, yang paling sedikit menyentuh.
      const nol = sah.find((c) => kena(c) === 0);
      const sedikit = sah.reduce<{ c: { left: number; top: number }; n: number } | null>((m, c) => {
        const n = kena(c);
        return m === null || n < m.n ? { c, n } : m;
      }, null);
      setPosPil(nol ?? sedikit?.c ?? (calon[0] as { left: number; top: number }));
    };
    hitung();
    // Hurufnya (Jost) bisa tiba SESUDAH tata letak pertama: kapsulnya jadi lebih
    // lebar daripada saat diukur, dan letak yang tadinya bersih menyentuh
    // sebuah bintang (terukur di akar 1.216 px: 1 bintang). Ukur ulang saat
    // ukuran kapsul berubah dan saat huruf siap.
    let batal = false;
    void document.fonts?.ready.then(() => {
      if (!batal) hitung();
    });
    const amat = new ResizeObserver(() => hitung());
    amat.observe(pil);
    return () => {
      batal = true;
      amat.disconnect();
    };
  }, [bintangSaran, ik, wadahRef]);

  const ikRef = useRef<Ikhtisar | null>(null);
  ikRef.current = ik;

  // Jalur wilayah per rasi, dihitung sekali per peta (bukan di tiap hover).
  const jalurWilayah = useMemo(
    () =>
      ik
        ? ik.rasi.map((r) =>
            pathWilayah(r.bintang.map((b) => [b.x, b.y] as Titik), padWilayah(ik.skala)),
          )
        : [],
    [ik],
  );
  const jalurRef = useRef<string[]>([]);
  jalurRef.current = jalurWilayah;

  /** Menulis sorot ke DOM. Tidak melakukan apa pun bila sasarannya sama. */
  const terapkanSorot = useCallback((baru: Sorot | null) => {
    const lama = sorotRef.current;
    if (
      lama === baru ||
      (lama && baru && lama.rasi === baru.rasi && lama.bintang === baru.bintang)
    ) {
      return;
    }
    sorotRef.current = baru;
    const peta = ikRef.current;
    const wadah = wadahRef.current;
    if (!peta || !wadah) return;
    if (!lama || !baru || lama.rasi !== baru.rasi) {
      const w = wilayahRef.current;
      if (w) {
        if (baru) w.setAttribute("d", jalurRef.current[baru.rasi] ?? "");
        else w.removeAttribute("d");
      }
      namaAktifRef.current?.removeAttribute("data-sorot");
      const r = baru ? peta.rasi[baru.rasi] : undefined;
      const el = r ? wadah.querySelector(`.lt-nama[data-key="${r.key}"]`) : null;
      el?.setAttribute("data-sorot", "ya");
      namaAktifRef.current = el;
    }
    const c = cincinRef.current;
    const b = baru?.bintang ?? null;
    if (c) {
      if (b) {
        c.setAttribute("cx", b.x.toFixed(1));
        c.setAttribute("cy", b.y.toFixed(1));
        c.setAttribute("r", (b.r + 5).toFixed(1));
        c.setAttribute("data-aktif", "ya");
      } else {
        c.removeAttribute("data-aktif");
      }
    }
    svgRef.current?.toggleAttribute("data-sorot", baru !== null);
  }, [wadahRef]);

  // Satu kali per bingkai, dan hanya bila kursor sungguh bergerak: pencarian
  // sasaran memegang grid spasial, tetapi 120 gerakan per detik tidak perlu 120
  // pencarian.
  const jadwalkan = (e: { clientX: number; clientY: number }) => {
    const k = (svgRef.current as SVGSVGElement).getBoundingClientRect();
    gerakRef.current = { x: e.clientX - k.left, y: e.clientY - k.top };
    if (bingkaiRef.current) return;
    bingkaiRef.current = requestAnimationFrame(() => {
      bingkaiRef.current = 0;
      const g = gerakRef.current;
      const peta = ikRef.current;
      if (!g || !peta) return;
      const h = sasaranIkhtisar(peta, g.x, g.y);
      terapkanSorot(h ? { rasi: h.bintang.rasi, bintang: h.tepat ? h.bintang : null } : null);
    });
  };
  const lepasSorot = () => {
    if (bingkaiRef.current) cancelAnimationFrame(bingkaiRef.current);
    bingkaiRef.current = 0;
    gerakRef.current = null;
    terapkanSorot(null);
  };
  useEffect(
    () => () => {
      if (bingkaiRef.current) cancelAnimationFrame(bingkaiRef.current);
    },
    [],
  );

  // Jumlah per keluarga untuk judulnya: dihitung dari data, tidak diketik.
  const jumlahKeluarga = useMemo(() => {
    const j: Record<string, { rasi: number; materi: number }> = {};
    for (const b of data.bahasa) {
      const k = TATA[b.key]?.[2] ?? "tech";
      const x = (j[k] ??= { rasi: 0, materi: 0 });
      x.rasi += 1;
      x.materi += b.materi.length;
    }
    return j;
  }, [data]);

  return (
    <div
      ref={wadahRef}
      className={"lt-ikhtisar" + (hidup ? " lt-ik-hidup" : "")}
      onAnimationEnd={(e) => {
        if (e.target === e.currentTarget.querySelector(".lt-ik-svg")) setHidup(false);
      }}
      role="group"
      aria-label={`Peta bintang: ${data.bahasa.length} kurikulum`}
    >
      {ik ? <Cahaya ik={ik} bekal={bekal} adaProfesi={adaProfesi} /> : null}
      {ik ? (
        <svg
          ref={svgRef}
          className="lt-ik-svg"
          width={ik.lebar}
          height={ik.tinggi}
          viewBox={`0 0 ${ik.lebar.toFixed(1)} ${ik.tinggi.toFixed(1)}`}
          aria-hidden="true"
          onPointerMove={(e) => {
            if (e.pointerType === "touch") return;
            jadwalkan(e);
          }}
          onPointerLeave={lepasSorot}
          onClick={(e) => {
            const k = e.currentTarget.getBoundingClientRect();
            const h = sasaranIkhtisar(ik, e.clientX - k.left, e.clientY - k.top);
            if (!h) return;
            const r = ik.rasi[h.bintang.rasi];
            if (r) onBuka(r.key, h.tepat ? h.bintang.i : null);
          }}
        >
          <Lintang s={ik.skala} />

          {adaProfesi ? (
            <g aria-hidden="true">
              {kelompok.slice(1).map((gb, i) => {
                const ga = kelompok[i] as string[];
                return gb.flatMap((kb) =>
                  ga.map((ka) => {
                    const a = ik.rasi.find((x) => x.key === ka);
                    const b = ik.rasi.find((x) => x.key === kb);
                    if (!a || !b) return null;
                    const mx = (a.cx + b.cx) / 2;
                    const my = (a.cy + b.cy) / 2 - 40 * ik.skala;
                    return (
                      <path
                        key={`${ka}-${kb}`}
                        className="lt-ik-jalur"
                        d={`M${a.cx.toFixed(1)},${a.cy.toFixed(1)}Q${mx.toFixed(1)},${my.toFixed(1)} ${b.cx.toFixed(1)},${b.cy.toFixed(1)}`}
                      />
                    );
                  }),
                );
              })}
            </g>
          ) : null}

          <Statis ik={ik} cocok={cocok} adaKonsep={adaKonsep} data={data} />

          <g className="lt-ik-sorot" aria-hidden="true">
            <path ref={wilayahRef} className="lt-ik-wilayah" />
            <circle ref={cincinRef} className="lt-ik-cincin" />
            {bintangSaran ? (
              <path
                className="lt-ik-braket"
                d={pathBraket(bintangSaran.x, bintangSaran.y, bintangSaran.r + 7, 6)}
              />
            ) : null}
          </g>
        </svg>
      ) : null}

      {ik ? (
        <div className="lt-ik-teks">
          {bintangSaran && saran ? (
            <a
              ref={pilRef}
              className="lt-mulai"
              href={`#/langit/${saran.bahasa}/${saran.indeks}`}
              title={saran.alasan}
              aria-label={`${kataMulai(bintangSaran.status)}: ${tanpaNomor(
                data.bahasa.find((x) => x.key === saran.bahasa)?.materi[saran.indeks]?.judul ?? "",
              )}, ${data.bahasa.find((x) => x.key === saran.bahasa)?.label ?? ""}. Buka di rasinya.`}
              style={
                posPil
                  ? { left: posPil.left + "px", top: posPil.top + "px" }
                  : { left: 0, top: 0, visibility: "hidden" }
              }
              onClick={(e) => {
                if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
                e.preventDefault();
                onBuka(saran.bahasa, saran.indeks);
              }}
            >
              {kataMulai(bintangSaran.status)}
            </a>
          ) : null}
          {/* Urutan DOM = urutan baca = urutan Tab: keluarga demi keluarga, di
              dalamnya urutan peta. Letaknya mutlak (persen), jadi urutan ini
              tidak memengaruhi tampilan; tanpanya Tab melompat-lompat di
              peta mengikuti urutan jawaban API. */}
          {URUTAN_KELUARGA.map((k) => {
            const kel = KELUARGA[k];
            const j = jumlahKeluarga[k];
            if (!kel || !j) return null;
            const anggota = ik.rasi
              .filter((r) => (TATA[r.key]?.[2] ?? "tech") === k)
              .sort((x, y) => urutPeta(x.key) - urutPeta(y.key));
            return (
              <Fragment key={k}>
                <div
                  className="lt-keluarga"
                  data-kel={k}
                  style={{ left: persen(kel[1], LEBAR_PETA), top: persen(kel[2], TINGGI_PETA) }}
                >
                  <h2>{kel[0]}</h2>
                  <p>{`${j.rasi} kurikulum, ${j.materi} materi`}</p>
                </div>
                {anggota.map((r) => {
                  const t = TATA[r.key];
                  const cx = t ? t[0] : r.cx / ik.skala;
                  const cy = t ? t[1] : r.cy / ik.skala;
                  const frak = r.jumlah ? r.selesai / r.jumlah : 0;
                  const diBekal = adaProfesi && bekal.has(r.key);
                  return (
                    <a
                      key={r.key}
                      className="lt-nama"
                      href={`#/langit/${r.key}`}
                      data-key={r.key}
                      data-bekal={diBekal ? "ya" : undefined}
                      style={{ left: persen(cx, LEBAR_PETA), top: persen(cy + 66, TINGGI_PETA) }}
                      aria-label={labelRasi({
                        label: r.label,
                        selesai: r.selesai,
                        jumlah: r.jumlah,
                        konsep: konsepNama,
                        cocok: cocokPer[r.key] ?? 0,
                        profesi: profesiNama,
                        bekal: diBekal,
                      })}
                      onClick={(e) => {
                        if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
                        e.preventDefault();
                        onBuka(r.key, null);
                      }}
                      onPointerEnter={(e) => {
                        if (e.pointerType !== "touch") terapkanSorot({ rasi: ik.rasi.indexOf(r), bintang: null });
                      }}
                      onPointerLeave={lepasSorot}
                      onFocus={() => terapkanSorot({ rasi: ik.rasi.indexOf(r), bintang: null })}
                      onBlur={lepasSorot}
                    >
                      <span className="lt-nama-teks">{r.label}</span>
                      <span className="lt-nama-prog">
                        <span className="lt-nama-jalur">
                          <i style={{ width: `${(frak * 100).toFixed(1)}%` }} />
                        </span>
                        <b>{`${r.selesai}/${r.jumlah}`}</b>
                      </span>
                    </a>
                  );
                })}
              </Fragment>
            );
          })}
        </div>
      ) : null}
    </div>
  );
}

/** Legenda satu baris: bentuk + warna + kata. Dipakai di atas peta dan di
 *  kaki lensa, jadi pelajar tidak perlu menggulir dua tinggi layar untuk tahu
 *  arti sebuah bentuk. */
export function Legenda({ berikutnya = true }: { berikutnya?: boolean }) {
  return (
    <ul className="lt-legenda" aria-label="Arti bentuk bintang">
      {URUTAN_STATUS.map((st) => (
        <li key={st}>
          <Glif status={st} r={st === "terkunci" ? 5 : 6.5} ukuran={20} />
          <span>{KATA_STATUS_BINTANG[st]}</span>
        </li>
      ))}
      {berikutnya ? (
        <li>
          <svg className="lt-glif" viewBox="-10 -10 20 20" width={20} height={20} aria-hidden="true" focusable="false">
            <path className="lt-ik-braket" d={pathBraket(0, 0, 8, 4)} />
          </svg>
          <span>berikutnya</span>
        </li>
      ) : null}
    </ul>
  );
}
