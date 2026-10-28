/* Layar Peta Karier. Port `webapp/statik/js/layar-karier.js`.
 *
 * Tangga karier: BARIS adalah rumpun, KOLOM adalah jenjang (pemula, menengah,
 * senior). Makin ke kanan makin senior.
 *
 * Satu hal yang justru jadi LEBIH BERSIH di React, dan layak dicatat karena
 * versi JS-nya rumit karenanya: **lebar label diukur dari teksnya sendiri**
 * (`getComputedTextLength`), dan garis antarprofesi dirutekan dari ujung label
 * itu. Versi JS menggambar sekali dengan PERKIRAAN per huruf (karena saat itu
 * layarnya belum menempel), menandai gambarnya `perkiraan`, lalu menggambar
 * ulang lewat `saatSiap`. Tanpa itu garis pertama yang dilihat orang bisa
 * menempel ke huruf terakhir label.
 *
 * Di sini dua lintasan itu memang bentuk alami React: render pertama memakai
 * perkiraan, `useEffect` mengukur yang sungguhan dan menyimpannya di state,
 * render kedua memakainya. Tidak ada penanda yang perlu diingat dan tidak ada
 * gambar-ulang manual.
 *
 * Yang TIDAK diport: gambar sampul generatif (`sampul.js`). Ia `aria-hidden`
 * dan murni hiasan, jadi menghilangkannya tidak menghapus satu pun informasi
 * -- beda dengan blok atribusi lisensi di Pustaka, yang wajib ikut.
 *
 * Kesiapan TIDAK dihitung di sini. Ia datang dari `pelajar/karier.py`, yang
 * memakai persen kurikulum yang SAMA dengan halaman bahasa. Menghitungnya
 * ulang di klien berarti dua angka untuk satu hal.
 */

import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  type KeyboardEvent as TekanEvent,
  type ReactNode,
} from "react";

import { ambil, kirim } from "../api.ts";
import { adaGerak, gerakPenuh } from "../gerak.ts";
import { sorak } from "../sorak.tsx";
import { Ikon } from "../komponen/Ikon.tsx";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { OrbitBekal } from "../komponen/OrbitBekal.tsx";
import { Pilihan } from "../komponen/Pilihan.tsx";
import { urlAman } from "../util.tsx";
import {
  aksiMaju,
  bilanganKata,
  judulHasil,
  kalimatSisa,
  labelAksiMaju,
  namaKeahlian,
  nomorSoal,
  parameterPilihan,
  sisaJawaban,
  soalBelumDijawab,
} from "./kuis-cocok-teks.ts";

const W = 1040;
const KIRI = 196;
const ATAS = 52;
const KOLOM = (W - KIRI) / 3;
const LANGKAH = 32;
const BARIS_MIN = 76;
const JENJANG_KOLOM: Record<string, number> = {
  pemula: 0,
  menengah: 1,
  senior: 2,
};
const R_SUDUT = 9;

interface Rumpun {
  id: string;
  label: string;
  ket: string;
}

interface Kelompok {
  pilihan: string[];
  wakil: string;
  persen: number;
}

interface Gaji {
  rentang: string;
  konteks: string;
  sumber: string;
  url: string;
  diperiksa: string;
}

interface Sertifikasi {
  nama: string;
  penerbit: string;
  tingkat: string;
}

interface Profesi {
  id: string;
  nama: string;
  rumpun: string;
  jenjang: string;
  kesiapan: number;
  ringkas: string;
  kelompok: Kelompok[];
  pelengkap: string[];
  harian: string[];
  keahlian: string[];
  alat: string[];
  gaji?: Gaji;
  sertifikasi: Sertifikasi[];
  masuk: string;
  proyek: string[];
  naik: string[];
  dekat: string[];
  peta: string[];
  sumber: Array<{ judul: string; url: string }>;
}

interface Sisi {
  a: string;
  b: string;
  jenis: string;
}

interface Soal {
  q: string;
  opsi: string[];
}

interface DataKarier {
  rumpun: Rumpun[];
  profesi: Profesi[];
  sisi: Sisi[];
  jenjang: Record<string, string>;
  keahlian: Record<string, string>;
  kurikulum: Record<string, { label: string; persen: number }>;
  kuis: Soal[];
  tujuan?: string;
}

interface Letak {
  x: number;
  y: number;
  kolom: number;
  R: number;
}

const bulat = (n: number) => Math.round(Number(n) || 0);
const persenTeks = (p: number) => `${bulat(p)}%`;
const pendek = (nama: string) =>
  nama.replace(/\s*\(.*?\)\s*/g, " ").replace(/ \/ .*$/, "").trim();

function tataLetak(data: DataKarier) {
  const pos = new Map<string, Letak>();
  const baris: Array<{ id: string; label: string; y: number; tinggi: number }> = [];
  let y = ATAS;
  for (const r of data.rumpun) {
    const sel = Object.keys(JENJANG_KOLOM).map((jenjang) =>
      data.profesi.filter((p) => p.rumpun === r.id && p.jenjang === jenjang),
    );
    const tinggi = Math.max(
      BARIS_MIN,
      Math.max(...sel.map((x) => x.length)) * LANGKAH + 28,
    );
    sel.forEach((isi, j) => {
      const blok = (isi.length - 1) * LANGKAH;
      isi.forEach((p, k) => {
        pos.set(p.id, {
          x: KIRI + j * KOLOM + 24,
          y: y + tinggi / 2 - blok / 2 + k * LANGKAH,
          kolom: j,
          R: p.jenjang === "senior" ? 8 : p.jenjang === "menengah" ? 7 : 6,
        });
      });
    });
    baris.push({ id: r.id, label: r.label, y, tinggi });
    y += tinggi;
  }
  return { pos, baris, tinggi: y + 12 };
}

/**
 * Garis dari ujung label simpul KIRI ke sisi kiri simpul KANAN, dirutekan
 * seperti peta metro: mendatar ke BATANG di talang sesudah kolom simpul kiri,
 * tegak di sepanjang batang itu, lalu mendatar masuk ke simpul kanan.
 *
 * Semua garis dari satu simpul berbagi batang yang sama, jadi sepuluh hubungan
 * terbaca sebagai satu pohon bercabang, bukan sepuluh kurva yang saling
 * melintas.
 */
function jalurGaris(
  kiri: Letak,
  ujungLabel: number,
  kanan: Letak,
  geser = 0,
): string {
  const x1 = ujungLabel + 14;
  const x2 = kanan.x - kanan.R - 9;
  const talang = KIRI + (kiri.kolom + 1) * KOLOM + 24 - 30 + geser;
  const xt = Math.min(Math.max(talang, x1 + R_SUDUT + 4), x2 - R_SUDUT - 4);
  const y1 = kiri.y;
  const y2 = kanan.y;
  const f = (n: number) => n.toFixed(1);
  const dy = y2 - y1;
  if (Math.abs(dy) < 1) return `M${f(x1)},${f(y1)} H${f(x2)}`;
  const r = Math.min(R_SUDUT, Math.abs(dy) / 2);
  const arah = Math.sign(dy);
  return (
    `M${f(x1)},${f(y1)} H${f(xt - r)} Q${f(xt)},${f(y1)} ${f(xt)},${f(y1 + arah * r)} ` +
    `V${f(y2 - arah * r)} Q${f(xt)},${f(y2)} ${f(xt + r)},${f(y2)} H${f(x2)}`
  );
}

/** Nama rumpun yang panjang dipecah dua baris di batas kata terdekat dari
 *  tengahnya, supaya tidak menabrak kolom pemula. */
function LabelRumpun({
  teks,
  x,
  yTengah,
  kelas,
  rumpun,
}: {
  teks: string;
  x: number;
  yTengah: number;
  kelas: string;
  rumpun: string;
}) {
  if (teks.length <= 18) {
    return (
      <text className={kelas} data-rumpun={rumpun} x={x} y={yTengah} dy="0.35em">
        {teks}
      </text>
    );
  }
  const spasi = [...teks.matchAll(/ /g)].map((m) => m.index);
  const potong = spasi.reduce((a, b) =>
    Math.abs(b - teks.length / 2) < Math.abs(a - teks.length / 2) ? b : a,
  );
  return (
    <text className={kelas} data-rumpun={rumpun} x={x} y={yTengah}>
      <tspan x={x} dy="-0.25em">
        {teks.slice(0, potong)}
      </tspan>
      <tspan x={x} dy="1.2em">
        {teks.slice(potong + 1)}
      </tspan>
    </text>
  );
}

/** Cincin kesiapan. */
function Cincin({ persen, ukuran }: { persen: number; ukuran: number }) {
  const r = ukuran / 2 - 4;
  const keliling = 2 * Math.PI * r;
  return (
    <svg
      className="kr-cincin"
      width={ukuran}
      height={ukuran}
      viewBox={`0 0 ${ukuran} ${ukuran}`}
      aria-hidden="true"
    >
      <circle cx={ukuran / 2} cy={ukuran / 2} r={r} className="kr-cincin-alas" />
      {persen > 0 ? (
        <circle
          cx={ukuran / 2}
          cy={ukuran / 2}
          r={r}
          className="kr-cincin-isi"
          strokeDasharray={`${((keliling * persen) / 100).toFixed(2)} ${keliling.toFixed(2)}`}
          transform={`rotate(-90 ${ukuran / 2} ${ukuran / 2})`}
        />
      ) : null}
    </svg>
  );
}

export function Karier({ id }: { id?: string }) {
  const [data, setData] = useState<DataKarier | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [terpilihId, setTerpilihId] = useState<string | null>(id ?? null);
  // Alamat bisa berubah selagi layar ini terbuka (`#/karier/a` ke
  // `#/karier/b`). Tanpa ini panel tetap yang lama dan "Jadikan tujuanku"
  // menyimpan profesi di panel, bukan yang ada di alamat.
  useEffect(() => { setTerpilihId(id ?? null); }, [id]);
  const [sorotId, setSorotId] = useState<string | null>(null);
  const [saringRumpun, setSaringRumpun] = useState("semua");
  const [tujuan, setTujuan] = useState<string>("");
  /** Lebar label SUNGGUHAN, hasil pengukuran. Kosong pada render pertama. */
  const [ujungLabel, setUjungLabel] = useState<Record<string, number>>({});
  const svgRef = useRef<SVGSVGElement>(null);

  useEffect(() => {
    let dibatalkan = false;
    ambil<DataKarier>("karier")
      .then((d) => {
        if (dibatalkan) return;
        setData(d);
        setTujuan(d.tujuan ?? "");
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, []);

  const letak = useMemo(() => (data ? tataLetak(data) : null), [data]);

  const perId = useMemo(
    () => new Map((data?.profesi ?? []).map((p) => [p.id, p])),
    [data],
  );

  const tetangga = useMemo(() => {
    const m = new Map<string, Set<string>>();
    for (const p of data?.profesi ?? []) m.set(p.id, new Set());
    for (const e of data?.sisi ?? []) {
      m.get(e.a)?.add(e.b);
      m.get(e.b)?.add(e.a);
    }
    return m;
  }, [data]);

  const jenisSisi = useMemo(() => {
    const m = new Map<string, string>();
    for (const e of data?.sisi ?? []) {
      m.set(e.a + "|" + e.b, e.jenis);
      m.set(e.b + "|" + e.a, e.jenis);
    }
    return m;
  }, [data]);

  const palingSiap = useMemo(() => {
    const urut = [...(data?.profesi ?? [])].sort((a, b) => b.kesiapan - a.kesiapan);
    return urut[0] ?? null;
  }, [data]);

  /* Profesi terpilih: dari alamat kalau ada, lalu yang paling siap, lalu
     frontend-developer sebagai titik mulai yang paling tidak asing. */
  const terpilih = useMemo(() => {
    if (!data) return null;
    return (
      (terpilihId ? perId.get(terpilihId) : null) ??
      (palingSiap && palingSiap.kesiapan > 0 ? palingSiap : null) ??
      perId.get("frontend-developer") ??
      data.profesi[0] ??
      null
    );
  }, [data, terpilihId, perId, palingSiap]);

  /* Ukur lebar label SESUDAH menempel. Ini lintasan kedua yang di versi JS
     harus dipicu manual lewat `saatSiap`; di sini ia efek biasa. Diukur sekali
     per muatan data: lebar teks tidak berubah karena sorotan berpindah. */
  useEffect(() => {
    const svg = svgRef.current;
    if (!svg || !letak) return;
    const hasil: Record<string, number> = {};
    for (const [pid, t] of letak.pos) {
      const teks = svg.querySelector<SVGTextElement>(
        `.kr-simpul[data-id="${pid}"] .kr-label`,
      );
      if (!teks) continue;
      const panjang = teks.getComputedTextLength();
      if (panjang) hasil[pid] = t.x + t.R + 10 + panjang;
    }
    if (Object.keys(hasil).length) setUjungLabel(hasil);
  }, [letak]);

  const ujung = useCallback(
    (pid: string) => {
      const diukur = ujungLabel[pid];
      if (diukur !== undefined) return diukur;
      const t = letak?.pos.get(pid);
      const nama = perId.get(pid)?.nama ?? "";
      // Perkiraan per huruf untuk render PERTAMA. Ia tidak disimpan, jadi
      // lintasan kedua selalu memakai ukuran sungguhan.
      return (t?.x ?? 0) + (t?.R ?? 0) + 10 + pendek(nama).length * 7.6;
    },
    [ujungLabel, letak, perId],
  );

  const pilih = useCallback((pid: string, dariPengguna: boolean) => {
    setTerpilihId(pid);
    setSorotId(null);
    if (dariPengguna) {
      // `replaceState`, bukan `location.hash`: router tidak perlu menggambar
      // ulang halaman yang sedang dilihat hanya karena satu simpul dipilih.
      try {
        history.replaceState(null, "", "#/karier/" + pid);
      } catch {
        // Beberapa browser membatasi laju replaceState. Alamat yang tidak
        // ikut berubah bukan alasan menggagalkan pemilihannya.
      }
    }
  }, []);

  if (galat) {
    return <Keadaan jenis="salah" judul="Gagal memuat Peta Karier" ket={galat} />;
  }
  if (!data || !letak || !terpilih) {
    return (
      <div className="deret" role="status">
        <div className="pusaran" aria-hidden="true" />
        <span>Memuat peta karier…</span>
      </div>
    );
  }

  const H = letak.tinggi;
  const fokus = sorotId ?? terpilih.id;
  const dekat = tetangga.get(fokus) ?? new Set<string>();
  const tersaring = (rumpun: string) =>
    saringRumpun !== "semua" && rumpun !== saringRumpun;

  /* Garis hanya untuk simpul yang sedang dibicarakan. Tetangga SEJENJANG tidak
     digaris: lingkar putus-putus di luar cincinnya yang membawa hubungan itu,
     karena garis mendatar antara dua simpul di kolom yang sama akan menembus
     label keduanya. */
  const garis: Array<{
    kunci: string;
    d: string;
    jenis: string;
    cx: number;
    cy: number;
  }> = [];
  for (const lain of dekat) {
    const a = letak.pos.get(fokus);
    const b = letak.pos.get(lain);
    if (!a || !b || a.kolom === b.kolom) continue;
    if (tersaring(perId.get(lain)?.rumpun ?? "")) continue;
    const [kiri, kanan] = a.kolom < b.kolom ? [fokus, lain] : [lain, fokus];
    const jenis = jenisSisi.get(fokus + "|" + lain) ?? "dekat";
    const pk = letak.pos.get(kanan as string) as Letak;
    garis.push({
      kunci: `${fokus}-${lain}`,
      d: jalurGaris(
        letak.pos.get(kiri as string) as Letak,
        ujung(kiri as string),
        pk,
        jenis === "naik" ? 0 : -8,
      ),
      jenis,
      cx: pk.x - pk.R - 9,
      cy: pk.y,
    });
  }

  return (
    <div className="masuk">
      <header className="kepala-besar kr-kepala">
        <div className="kepala-teks">
          <span className="mata">Peta karier</span>
          <h1>{`${data.profesi.length} profesi, satu jalan belajar.`}</h1>
          <p className="kepala-sub">
            Kesiapan tiap profesi dihitung dari kurikulum yang sudah kamu
            kerjakan di aplikasi ini. Arahkan kursor ke sebuah profesi untuk
            melihat ke mana ia terhubung, lalu pilih untuk membaca rinciannya.
          </p>
          <div className="kr-aksi">
            {/* Tombol, bukan tautan ke `#kr-cocok`: alamat di aplikasi ini
                adalah rute, jadi `#kr-cocok` dibaca sebagai rute tak dikenal
                dan melempar orangnya ke Dasbor. */}
            <button
              type="button"
              className="tbl tbl-utama"
              onClick={() => document.getElementById("kr-cocok")?.scrollIntoView({
                behavior: adaGerak() ? "smooth" : "auto", block: "start",
              })}
            >
              Cari yang cocok
            </button>
            {palingSiap && palingSiap.kesiapan > 0 ? (
              <button
                type="button"
                className="kr-tautan"
                onClick={() => pilih(palingSiap.id, true)}
              >
                {`Paling siap: ${pendek(palingSiap.nama)} (${persenTeks(palingSiap.kesiapan)})`}
              </button>
            ) : null}
          </div>
        </div>
      </header>

      <div className="kr-saring" role="radiogroup" aria-label="Saring rumpun">
        {[{ id: "semua", label: "Semua" }, ...data.rumpun].map((r) => (
          <button
            key={r.id}
            type="button"
            className="kr-chip"
            role="radio"
            aria-checked={saringRumpun === r.id}
            onClick={() => setSaringRumpun(r.id)}
          >
            {r.label}
          </button>
        ))}
      </div>

      <div className="kr-utama">
        <figure className="kr-kanvas">
          <svg
            ref={svgRef}
            viewBox={`0 0 ${W} ${H}`}
            className="kr-graf"
            role="group"
            aria-label="Konstelasi profesi. Pilih satu untuk melihat rinciannya."
          >
            <g>
              {letak.baris.map((r, i) => (
                <rect
                  key={r.id}
                  x={0}
                  y={r.y}
                  width={W}
                  height={r.tinggi}
                  className={
                    "kr-pita" +
                    (i % 2 ? " kr-pita-genap" : "") +
                    (tersaring(r.id) ? " redup" : "")
                  }
                  data-rumpun={r.id}
                />
              ))}
            </g>
            <g>
              {Object.keys(JENJANG_KOLOM).map((j, i) => (
                <text key={j} className="kr-kolom" x={KIRI + i * KOLOM + 16} y={30}>
                  {(data.jenjang[j] ?? "").startsWith("Bisa")
                    ? "Pemula"
                    : j === "menengah"
                      ? "Menengah"
                      : "Senior"}
                </text>
              ))}
            </g>
            <g>
              {letak.baris.map((r) => (
                <LabelRumpun
                  key={r.id}
                  teks={r.label}
                  x={22}
                  yTengah={r.y + r.tinggi / 2}
                  kelas={"kr-rumpun" + (tersaring(r.id) ? " redup" : "")}
                  rumpun={r.id}
                />
              ))}
            </g>

            <g className="kr-lapis-garis">
              {garis.map((g) => (
                <GarisSisi key={g.kunci} d={g.d} jenis={g.jenis} cx={g.cx} cy={g.cy} />
              ))}
            </g>

            <g>
              {data.profesi.map((p) => {
                const t = letak.pos.get(p.id) as Letak;
                const keliling = 2 * Math.PI * (t.R + 4);
                const jauh =
                  (p.id !== fokus && !dekat.has(p.id)) || tersaring(p.rumpun);
                const kelas =
                  "kr-simpul" +
                  (jauh ? " redup" : "") +
                  (p.id === terpilih.id ? " dipilih" : "") +
                  (p.id === fokus || p.id === terpilih.id || dekat.has(p.id)
                    ? " tampak"
                    : "") +
                  (dekat.has(p.id) &&
                  letak.pos.get(p.id)?.kolom === letak.pos.get(fokus)?.kolom
                    ? " sejajar"
                    : "");
                return (
                  <g
                    key={p.id}
                    className={kelas}
                    tabIndex={0}
                    role="button"
                    data-id={p.id}
                    data-rumpun={p.rumpun}
                    aria-pressed={p.id === terpilih.id}
                    aria-label={`${p.nama}, kesiapan ${bulat(p.kesiapan)} persen`}
                    transform={`translate(${t.x.toFixed(1)},${t.y.toFixed(1)})`}
                    onClick={() => pilih(p.id, true)}
                    onKeyDown={(e) => {
                      if (e.key === "Enter" || e.key === " ") {
                        e.preventDefault();
                        pilih(p.id, true);
                      }
                    }}
                    onPointerEnter={() => setSorotId(p.id)}
                    onPointerLeave={() => setSorotId(null)}
                    onFocus={() => setSorotId(p.id)}
                    onBlur={() => setSorotId(null)}
                  >
                    <rect
                      x={-t.R - 8}
                      y={-LANGKAH / 2 + 2}
                      width={KOLOM - 20}
                      height={LANGKAH - 4}
                      rx={8}
                      className="kr-sasaran"
                    />
                    <circle r={t.R + 9} className="kr-halo" />
                    <circle r={t.R + 4} className="kr-cincin-alas" />
                    {p.kesiapan > 0 ? (
                      <circle
                        r={t.R + 4}
                        className="kr-cincin-isi"
                        strokeDasharray={`${((keliling * p.kesiapan) / 100).toFixed(2)} ${keliling.toFixed(2)}`}
                        transform="rotate(-90)"
                      />
                    ) : null}
                    <circle r={t.R} className="kr-inti" />
                    <text className="kr-label" x={t.R + 10} y={0} dy="0.35em">
                      {pendek(p.nama)}
                    </text>
                  </g>
                );
              })}
            </g>
          </svg>
          <figcaption className="kr-legenda">
            <span>
              <i className="kr-leg-naik" />
              Jalur naik
            </span>
            <span>
              <i className="kr-leg-dekat" />
              Keahlian beririsan
            </span>
            <span>
              <i className="kr-leg-sejajar" />
              Sejenjang &amp; beririsan
            </span>
            <span>
              <i className="kr-leg-siap" />
              Kesiapanmu
            </span>
            <span>
              Garis muncul untuk profesi yang dipilih. Makin ke kanan, makin
              senior.
            </span>
          </figcaption>
        </figure>

        <aside className="kr-panel" id="kr-panel" aria-live="polite">
          <PanelDetail
            p={terpilih}
            data={data}
            tujuan={tujuan}
            onPilih={pilih}
            onTujuan={setTujuan}
          />
        </aside>
      </div>

      {/* Orbit di bagian sendiri, BUKAN di dalam panel: panel itu kolom samping
          selebar sekitar 370 px, dan papan orbit yang dikecilkan sampai 318 px
          membuat label saling menimpa dan simpul dua cincin bertumpuk (jarak antar
          cincin 45 px lebih kecil dari simpulnya). `key` mengosongkan pilihan dan
          putaran hanya saat profesinya berganti. */}
      <section className="kr-bagian" id="kr-orbit" aria-labelledby="kr-judul-orbit">
        <div className="kr-bagian-kepala">
          <span className="mata">Bekal dalam orbit</span>
          <h2 id="kr-judul-orbit">{terpilih.nama}</h2>
          <p>
            Kurikulum yang dibutuhkan profesi yang sedang kamu pilih di atas, dan seberapa jauh kamu
            sudah melangkah di tiap-tiapnya.
          </p>
        </div>
        <OrbitBekal
          key={terpilih.id}
          nama={terpilih.nama}
          kelompok={terpilih.kelompok}
          pelengkap={terpilih.pelengkap}
          kur={data.kurikulum}
          pusat={
            <>
              <Cincin persen={terpilih.kesiapan} ukuran={56} />
              <span className="or-pusat-angka">{persenTeks(terpilih.kesiapan)}</span>
              <span className="or-pusat-nama">kesiapan</span>
            </>
          }
        />
      </section>

      <KuisCocok
        data={data}
        perId={perId}
        tujuan={tujuan}
        onPilih={pilih}
        onTujuan={setTujuan}
      />
      <Perencana data={data} terpilih={terpilih} onPilih={pilih} />

      <section className="kr-bagian" aria-labelledby="kr-judul-rumpun">
        <div className="kr-bagian-kepala">
          <span className="mata">Indeks</span>
          <h2 id="kr-judul-rumpun">{`${data.rumpun.length} rumpun, dibaca utuh.`}</h2>
        </div>
        <div className="kr-indeks">
          {data.rumpun.map((r) => (
            <section key={r.id} className="kr-rumpun-kartu">
              <h3>{r.label}</h3>
              <p>{r.ket}</p>
              <ul>
                {data.profesi
                  .filter((p) => p.rumpun === r.id)
                  .map((p) => (
                    <li key={p.id}>
                      <button type="button" onClick={() => pilih(p.id, true)}>
                        <span>{p.nama}</span>
                        <span className="kr-persen">{persenTeks(p.kesiapan)}</span>
                      </button>
                    </li>
                  ))}
              </ul>
            </section>
          ))}
        </div>
      </section>
    </div>
  );
}

/** Satu garis antarprofesi, beserta titik ujungnya.
 *
 *  Garis "naik" ditarik dari kiri ke kanan saat gerak penuh. Keadaan akhirnya
 *  keadaan ALAMI (dashoffset 0), jadi gerak yang dimatikan tidak
 *  menyembunyikan apa pun -- pola yang sama dengan `Bilah`. */
function GarisSisi({
  d,
  jenis,
  cx,
  cy,
}: {
  d: string;
  jenis: string;
  cx: number;
  cy: number;
}) {
  const ref = useRef<SVGPathElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el || jenis !== "naik" || !gerakPenuh()) return;
    el.animate(
      { strokeDashoffset: [1, 0] },
      { duration: 420, easing: "cubic-bezier(.2,.7,.2,1)" },
    );
  }, [d, jenis]);
  return (
    <>
      <path
        ref={ref}
        d={d}
        className={"kr-sisi kr-sisi-" + jenis}
        pathLength={jenis === "naik" ? 1 : undefined}
        strokeDasharray={jenis === "naik" ? "1" : undefined}
      />
      <circle
        className={"kr-ujung kr-ujung-" + jenis}
        r={2.6}
        cx={cx.toFixed(1)}
        cy={cy.toFixed(1)}
      />
    </>
  );
}

function PanelDetail({
  p,
  data,
  tujuan,
  onPilih,
  onTujuan,
}: {
  p: Profesi;
  data: DataKarier;
  tujuan: string;
  onPilih: (id: string, dariPengguna: boolean) => void;
  onTujuan: (v: string) => void;
}) {
  const kur = data.kurikulum;
  const rumpun = data.rumpun.find((r) => r.id === p.rumpun);
  const chip = (ids: string[]) => (
    <div className="kr-chip-deret">
      {ids.map((pid) => {
        const q = data.profesi.find((x) => x.id === pid);
        return q ? (
          <button
            key={pid}
            type="button"
            className="kr-chip"
            onClick={() => onPilih(pid, true)}
          >
            {pendek(q.nama)}
          </button>
        ) : null;
      })}
    </div>
  );
  const daftar = (butir: string[]) => (
    <ul className="kr-daftar">
      {butir.map((b, i) => (
        <li key={i}>{b}</li>
      ))}
    </ul>
  );
  const Blok = ({ judul, children }: { judul: string; children: ReactNode }) => (
    <section className="kr-blok">
      <h3>{judul}</h3>
      {children}
    </section>
  );

  return (
    <div className="kr-panel-isi">
      <div className="kr-panel-kepala">
        <div>
          <span className="mata">{rumpun?.label}</span>
          <h2>{p.nama}</h2>
          <span className="pil">{data.jenjang[p.jenjang]}</span>
          <TombolTujuan p={p} tujuan={tujuan} onTujuan={onTujuan} />
        </div>
        <div className="kr-siap">
          <Cincin persen={p.kesiapan} ukuran={68} />
          <span className="kr-siap-angka">{persenTeks(p.kesiapan)}</span>
          <span className="kr-siap-ket">siap</span>
        </div>
      </div>
      <p className="kr-ringkas">{p.ringkas}</p>

      <Blok judul="Bekal dari aplikasi ini">
        <ul className="kr-bekal">
          {p.kelompok.map((k, i) => (
            <li key={i}>
              <div className="kr-bekal-nama">
                {k.pilihan.length > 1 ? (
                  <>
                    <span className="kr-atau">salah satu</span>
                    {k.pilihan.map((x) => (
                      <a
                        key={x}
                        href={"#/bahasa/" + x}
                        className={x === k.wakil ? "wakil" : undefined}
                      >
                        {kur[x]?.label ?? x}
                      </a>
                    ))}
                  </>
                ) : (
                  <a href={"#/bahasa/" + k.wakil}>{kur[k.wakil]?.label ?? k.wakil}</a>
                )}
              </div>
              <div
                className="kr-bekal-bilah"
                role="img"
                aria-label={`${bulat(k.persen)} persen`}
              >
                <i style={{ width: `${Math.max(0, Math.min(100, k.persen))}%` }} />
              </div>
              <span className="kr-persen">{persenTeks(k.persen)}</span>
            </li>
          ))}
        </ul>
        {p.pelengkap.length ? (
          <p className="kr-catatan">
            Pelengkap:{" "}
            {p.pelengkap.map((x, i) => (
              <span key={x}>
                {i ? ", " : ""}
                <a href={"#/bahasa/" + x}>{kur[x]?.label ?? x}</a>
              </span>
            ))}
          </p>
        ) : null}
      </Blok>

      <Blok judul="Sehari-hari">{daftar(p.harian)}</Blok>
      <Blok judul="Keahlian">
        <div className="kr-tag-deret">
          {p.keahlian.map((k) => (
            <span key={k} className="kr-tag">
              {data.keahlian[k] ?? k}
            </span>
          ))}
        </div>
      </Blok>
      <Blok judul="Alat yang sering dipakai">
        <div className="kr-tag-deret">
          {p.alat.map((a) => (
            <span key={a} className="kr-tag kr-tag-kode">
              {a}
            </span>
          ))}
        </div>
      </Blok>

      <Blok judul="Gaji di Indonesia">
        {p.gaji ? (
          <>
            <p className="kr-gaji">{p.gaji.rentang}</p>
            <p className="kr-catatan">
              {p.gaji.konteks} Sumber:{" "}
              <a
                href={urlAman(p.gaji.url) ?? undefined}
                target="_blank"
                rel="noopener noreferrer"
              >
                {p.gaji.sumber}
              </a>
              {`, diperiksa ${p.gaji.diperiksa}.`}
            </p>
          </>
        ) : (
          /* Angka yang tidak bisa diperiksa SENGAJA tidak ditebak. Gaji yang
             dikarang lebih buruk daripada gaji yang tidak disebut: orang
             mengambil keputusan karier dari angka itu. */
          <p className="kr-catatan">
            Belum ada sumber publik yang angkanya bisa diperiksa untuk peran
            ini, jadi sengaja tidak ditebak.
          </p>
        )}
      </Blok>

      <Blok judul="Sertifikasi">
        {p.sertifikasi.length ? (
          <ul className="kr-daftar">
            {p.sertifikasi.map((x) => (
              <li key={x.nama}>
                {x.nama}
                <span className="kr-catatan">{` · ${x.penerbit} · ${x.tingkat}`}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="kr-catatan">
            Tidak ada sertifikasi yang diakui luas untuk peran ini. Portofolio
            dan kontribusi nyata yang berbicara.
          </p>
        )}
      </Blok>

      <Blok judul="Jalan masuk">
        <p>{p.masuk}</p>
      </Blok>
      <Blok judul="Proyek untuk portofolio">{daftar(p.proyek)}</Blok>
      {p.naik.length ? <Blok judul="Langkah berikutnya">{chip(p.naik)}</Blok> : null}
      <Blok judul="Profesi yang dekat">{chip(p.dekat)}</Blok>
      <Blok judul="Bacaan lanjut">
        <ul className="kr-daftar kr-tautan-luar">
          {p.peta.map((slug) => (
            <li key={slug}>
              <a
                href={"https://roadmap.sh/" + slug}
                target="_blank"
                rel="noopener noreferrer"
              >
                {"roadmap.sh/" + slug}
              </a>
            </li>
          ))}
          {p.sumber.map((x) => (
            <li key={x.url}>
              <a
                href={urlAman(x.url) ?? undefined}
                target="_blank"
                rel="noopener noreferrer"
              >
                {x.judul}
              </a>
            </li>
          ))}
          {p.kelompok[0] ? (
            <li>
              <a href={"#/pustaka?kurikulum=" + p.kelompok[0].wakil}>
                {`Pustaka: bacaan ${kur[p.kelompok[0].wakil]?.label ?? ""}`}
              </a>
            </li>
          ) : null}
        </ul>
      </Blok>
    </div>
  );
}

/** "Jadikan tujuanku": menyimpan profesi tujuan ke `tujuan_karier`.
 *
 *  Dasbor dan perencana perpindahan membacanya; tanpa ini keduanya menebak
 *  dari kesiapan tertinggi. Setelan yang sama ada di Pengaturan, jadi kalau
 *  penyimpanannya gagal tombolnya tetap ada dan tidak ada yang terkunci. */
function TombolTujuan({
  p,
  tujuan,
  onTujuan,
}: {
  p: Profesi;
  tujuan: string;
  onTujuan: (v: string) => void;
}) {
  const ini = tujuan === p.id;
  return (
    <button
      type="button"
      className="tbl tbl-kecil kr-tujuan"
      aria-pressed={ini}
      onClick={async () => {
        const baru = ini ? "" : p.id;
        try {
          await kirim("konfigurasi", { tujuan_karier: baru });
          onTujuan(baru);
        } catch (e) {
          // Setelan yang sama ada di Pengaturan, jadi tidak ada yang terkunci;
          // tetapi gagal diam-diam membuat tombolnya tampak mati.
          sorak("Gagal menyimpan tujuan: " + (e as Error).message, "salah");
        }
      }}
    >
      <span>{ini ? "Tujuanmu" : "Jadikan tujuanku"}</span>
    </button>
  );
}

/** Jawaban server untuk satu profesi hasil kuis. `dari` menyebut soal mana
 *  yang mendorongnya; server lama tanpa medan itu tetap terbaca (`cocok`). */
interface HasilKuis {
  id: string;
  cocok: string[];
  dari?: Array<{ soal: number; keahlian: string[] }>;
}

/** Kuis kecocokan: satu soal sekali tampil, jawaban tercatat di sampingnya.
 *
 *  Kuis lama menampilkan enam soal dan 24 pilihan sekaligus, pilihan terpilih
 *  hanya dibedakan garis tipis, tombol hasilnya mati tanpa alasan, dan hasilnya
 *  cuma nama profesi dengan "Cocok karena: Antarmuka web". Orang tidak tahu
 *  jawaban mana yang membawanya ke sana, dan "Lihat profesi" menggulir tidak ke
 *  mana-mana (panelnya ada di atas, jauh dari kuis).
 *
 *  Prinsip yang dipakai, masing-masing dengan akibat yang bisa dilihat. Semuanya
 *  hipotesis desain: belum pernah diuji pada pelajar sungguhan.
 *   - Beban ingatan kerja: satu soal dan empat pilihan per layar, dengan
 *     "Soal 2 dari 6". Kemajuannya nyata, bukan hitung mundur atau desakan.
 *   - Keadaan sistem terlihat: pilihan terpilih bertanda centang, nomor terisi,
 *     dan huruf tebal. Bukan warna saja. Daftar jawaban di samping merekam apa
 *     yang sudah dipilih, dengan kalimat pilihannya sendiri.
 *   - Kendali dan bisa dibalik: Kembali, lompat lewat daftar, lewati tanpa
 *     denda, ubah jawaban kapan saja. Tidak ada pilihan yang terpilih dari awal.
 *   - Syarat minimum disebut dengan angkanya, dan tidak ada tombol yang buntu.
 *   - Hasil dalam kata-kata pemilihnya: "Soal 1: <jawabanmu> menunjuk ke
 *     <keahlian>". Tidak ada label tentang siapa orangnya: urutannya
 *     kedekatan dengan jawaban, bukan penilaian kemampuan.
 *   - Tindakan sesudahnya jelas: lihat profesi (menggulir ke panelnya) atau
 *     jadikan tujuan. Memilih tetap keputusan orangnya.
 */
function KuisCocok({
  data,
  perId,
  tujuan,
  onPilih,
  onTujuan,
}: {
  data: DataKarier;
  perId: Map<string, Profesi>;
  tujuan: string;
  onPilih: (id: string, dariPengguna: boolean) => void;
  onTujuan: (v: string) => void;
}) {
  const total = data.kuis.length;
  const [jawaban, setJawaban] = useState<Array<number | null>>(() =>
    data.kuis.map(() => null),
  );
  const [aktif, setAktif] = useState(0);
  const [tahap, setTahap] = useState<"soal" | "hasil">("soal");
  // Jawaban disimpan BERSAMA hasilnya: yang ditampilkan di kartu adalah
  // jawaban saat hasil dihitung, bukan yang sudah berubah sesudahnya.
  const [hasil, setHasil] = useState<{
    daftar: HasilKuis[];
    jawaban: Array<number | null>;
  } | null>(null);
  const soalRef = useRef<HTMLLegendElement>(null);
  const hasilRef = useRef<HTMLHeadingElement>(null);
  // Fokus pindah ke judul soal atau hasil HANYA sesudah orang berpindah lewat
  // tombol, supaya pembaca layar langsung mendengar apa yang baru. Dipasang
  // dulu, dipakai efek sesudah gambar baru terpasang.
  const fokus = useRef<"soal" | "hasil" | null>(null);
  // Penjaga klik ganda. Bukan `disabled`: tombol yang sedang berfokus lalu
  // dinonaktifkan menjatuhkan fokusnya ke body.
  const sibuk = useRef(false);
  const nomorMinta = useRef(0);

  const cukup = sisaJawaban(jawaban) === 0;
  const maju = aksiMaju(jawaban, aktif);
  const soal = data.kuis[aktif] as Soal;

  useEffect(() => {
    const mau = fokus.current;
    if (!mau) return;
    fokus.current = null;
    (mau === "hasil" ? hasilRef.current : soalRef.current)?.focus({ preventScroll: true });
  }, [aktif, tahap, hasil]);

  function pergi(i: number) {
    const baru = Math.max(0, Math.min(total - 1, i));
    if (baru === aktif && tahap === "soal") {
      soalRef.current?.focus({ preventScroll: true });
      return;
    }
    fokus.current = "soal";
    setAktif(baru);
    setTahap("soal");
  }

  function pilihJawaban(i: number, j: number) {
    setJawaban((d) => d.map((x, k) => (k === i ? j : x)));
  }

  async function lihat() {
    if (sibuk.current || !cukup) return;
    sibuk.current = true;
    const ini = ++nomorMinta.current;
    const salinan = [...jawaban];
    try {
      const r = await ambil<{ hasil: HasilKuis[] }>("karier/kuis", {
        pilihan: parameterPilihan(salinan),
      });
      if (ini !== nomorMinta.current) return;
      fokus.current = "hasil";
      setHasil({ daftar: r.hasil, jawaban: salinan });
      setTahap("hasil");
    } catch (e) {
      sorak("Gagal memuat hasil kuis: " + (e as Error).message, "salah");
    } finally {
      sibuk.current = false;
    }
  }

  function lanjutkan() {
    if (maju.jenis === "hasil") void lihat();
    else pergi(maju.jenis === "belum" ? maju.ke : aktif + 1);
  }

  function keBelumDijawab() {
    const ke = soalBelumDijawab(jawaban, aktif + 1);
    if (ke !== null) pergi(ke);
  }

  /** Memilih profesi di peta lalu membawa orangnya ke panelnya: panel itu ada
   *  di atas kuis, jadi tanpa gulir tombolnya terlihat tidak berbuat apa-apa. */
  function lihatProfesi(id: string) {
    onPilih(id, true);
    document.getElementById("kr-panel")?.scrollIntoView({
      behavior: adaGerak() ? "smooth" : "auto",
      block: "start",
    });
  }

  function tombolSoal(e: TekanEvent<HTMLFieldSetElement>) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    const n = Number(e.key);
    if (Number.isInteger(n) && n >= 1 && n <= soal.opsi.length) {
      e.preventDefault();
      // Fokus ikut ke pilihan itu: panah berikutnya mulai dari yang terpilih.
      e.currentTarget.querySelectorAll<HTMLInputElement>("input[type=radio]")[n - 1]?.focus();
      pilihJawaban(aktif, n - 1);
    } else if (e.key === "Enter" && jawaban[aktif] !== null) {
      e.preventDefault();
      lanjutkan();
    }
  }

  // Tombol di daftar jawaban hanya muncul bila ia bukan salinan tombol maju.
  const salinanMaju = (cukup && maju.jenis === "hasil") || (!cukup && maju.jenis === "belum");

  return (
    <section className="kr-bagian" id="kr-cocok" aria-labelledby="kr-judul-cocok">
      <div className="kr-bagian-kepala">
        <span className="mata">Kuis kecocokan</span>
        <h2 id="kr-judul-cocok">Mana yang cocok denganmu?</h2>
        <p>
          {`${bilanganKata(total)} pertanyaan tentang apa yang membuatmu betah bekerja, satu per satu. `}
          Jawabanmu tercatat di sebelah kanan dan bisa kamu ubah kapan saja. Tidak
          ada jawaban yang salah; hasilnya cuma titik mulai.
        </p>
      </div>
      <div className="kr-soal-kisi">
        <div className="kc-utama">
          {tahap === "hasil" && hasil ? (
            <div className="kc-hasil kr-hasil-kuis">
              <h3 className="kc-hasil-judul" ref={hasilRef} tabIndex={-1}>
                {judulHasil(hasil.daftar.length)}
              </h3>
              <p className="kr-catatan">
                Urutannya menunjukkan kedekatan dengan jawabanmu, bukan penilaian
                kemampuanmu. Ini titik mulai; profesi lain tetap bisa kamu jelajahi
                di peta di atas.
              </p>
              {hasil.daftar.length ? (
                <ol className="kr-juara">
                  {hasil.daftar.map((x, i) => {
                    const p = perId.get(x.id);
                    if (!p) return null;
                    return (
                      <li key={x.id}>
                        <span className="kr-juara-no" aria-hidden="true">{i + 1}</span>
                        <div className="isi">
                          <h4 className="judul">{p.nama}</h4>
                          <p className="kc-ringkas">{p.ringkas}</p>
                          <div className="kc-alasan">
                            <span className="kc-alasan-judul">Muncul karena jawabanmu</span>
                            {x.dari?.length ? (
                              <ul>
                                {x.dari.map((d) => {
                                  const pil = hasil.jawaban[d.soal];
                                  const teks = pil === null || pil === undefined
                                    ? ""
                                    : data.kuis[d.soal]?.opsi[pil] ?? "";
                                  return (
                                    <li key={d.soal}>
                                      <span className="kc-ref">{`Soal ${d.soal + 1}`}</span>{" "}
                                      {`“${teks}” `}
                                      <span className="kc-ke">
                                        {`menunjuk ke ${namaKeahlian(d.keahlian, data.keahlian)}`}
                                      </span>
                                    </li>
                                  );
                                })}
                              </ul>
                            ) : (
                              <p className="ket">
                                {"Cocok karena: " + namaKeahlian(x.cocok, data.keahlian)}
                              </p>
                            )}
                          </div>
                        </div>
                        <div className="kc-aksi-kartu">
                          <button
                            type="button"
                            className="tbl tbl-hantu tbl-kecil"
                            onClick={() => lihatProfesi(p.id)}
                          >
                            Lihat profesi
                          </button>
                          <TombolTujuan p={p} tujuan={tujuan} onTujuan={onTujuan} />
                        </div>
                      </li>
                    );
                  })}
                </ol>
              ) : (
                <p className="kr-catatan">
                  Jawabanmu belum menunjuk ke profesi mana pun. Coba jawab beberapa
                  soal lagi, atau ubah jawaban yang masih kamu ragukan.
                </p>
              )}
              <div className="kr-aksi">
                <button type="button" className="tbl tbl-hantu" onClick={() => pergi(aktif)}>
                  Ubah jawaban
                </button>
              </div>
            </div>
          ) : (
            <>
              <p className="kc-kepala-soal">
                <span className="kc-hitung">{`Soal ${aktif + 1} dari ${total}`}</span>
                <span className="kc-bantu">
                  {`Pilih satu. Tombol 1 sampai ${soal.opsi.length} juga bisa.`}
                </span>
              </p>
              <fieldset className="kr-soal" key={aktif} onKeyDown={tombolSoal}>
                <legend ref={soalRef} tabIndex={-1}>
                  <span className="kr-soal-no" aria-hidden="true">{nomorSoal(aktif)}</span>
                  <span className="kc-sr">{`Soal ${aktif + 1} dari ${total}. `}</span>
                  {soal.q}
                </legend>
                <div className="kr-opsi">
                  {soal.opsi.map((o, j) => (
                    <label key={j} className="kr-pilihan">
                      <input
                        type="radio"
                        className="kc-radio"
                        name={`kc-soal-${aktif}`}
                        value={j}
                        checked={jawaban[aktif] === j}
                        onChange={() => pilihJawaban(aktif, j)}
                      />
                      <span className="kc-nomor" aria-hidden="true">{j + 1}</span>
                      <span className="kc-label">{o}</span>
                      <span className="kc-tanda" aria-hidden="true">
                        <Ikon nama="selesai" ukuran={20} />
                      </span>
                    </label>
                  ))}
                </div>
              </fieldset>
              <div className="kr-aksi kc-nav">
                {aktif > 0 ? (
                  <button type="button" className="tbl tbl-hantu" onClick={() => pergi(aktif - 1)}>
                    Kembali
                  </button>
                ) : null}
                <button
                  type="button"
                  className={"tbl " + (maju.jenis === "lanjut" || maju.jenis === "hasil" ? "tbl-utama" : "tbl-hantu")}
                  onClick={lanjutkan}
                >
                  {labelAksiMaju(maju)}
                </button>
              </div>
            </>
          )}
        </div>
        <aside className="kc-rel" aria-labelledby="kc-rel-judul">
          <h3 className="kc-rel-judul" id="kc-rel-judul">Jawabanmu</h3>
          <ol className="kc-daftar">
            {data.kuis.map((s, i) => {
              const j = jawaban[i] ?? null;
              return (
                <li key={i}>
                  <button
                    type="button"
                    className="kc-baris"
                    data-kosong={j === null ? "" : undefined}
                    aria-current={tahap === "soal" && i === aktif ? "step" : undefined}
                    aria-label={`Soal ${i + 1}: ${j === null ? "belum dijawab" : s.opsi[j]}`}
                    onClick={() => pergi(i)}
                  >
                    <span className="kc-no" aria-hidden="true">{nomorSoal(i)}</span>
                    <span className="kc-teks" aria-hidden="true">
                      {j === null ? "Belum dijawab" : s.opsi[j]}
                    </span>
                    <span className="kc-cek" aria-hidden="true">
                      {j === null ? null : <Ikon nama="selesai" ukuran={16} />}
                    </span>
                  </button>
                </li>
              );
            })}
          </ol>
          <p className="kc-sisa">{kalimatSisa(jawaban)}</p>
          {salinanMaju ? null : (
            <button
              type="button"
              className="tbl tbl-hantu tbl-kecil"
              onClick={cukup ? () => void lihat() : keBelumDijawab}
            >
              {cukup ? "Lihat yang cocok" : "Ke soal yang belum dijawab"}
            </button>
          )}
        </aside>
      </div>
    </section>
  );
}

/** Perencana perpindahan. Jalurnya dihitung server dari hubungan
 *  antarprofesi; layar ini tidak punya pendapat sendiri soal rute. */
function Perencana({
  data,
  terpilih,
  onPilih,
}: {
  data: DataKarier;
  terpilih: Profesi;
  onPilih: (id: string, dariPengguna: boolean) => void;
}) {
  const palingSiap = useMemo(
    () => [...data.profesi].sort((a, b) => b.kesiapan - a.kesiapan)[0] ?? null,
    [data],
  );
  const [dari, setDari] = useState<string>(
    palingSiap && palingSiap.kesiapan > 0 ? palingSiap.id : "qa-engineer",
  );
  const ke = terpilih.id;
  const [jalur, setJalur] = useState<{ jalur: string[]; celah: string[][] } | null>(
    null,
  );
  const [catatan, setCatatan] = useState<string | null>(null);
  const nomor = useRef(0);

  useEffect(() => {
    if (dari === ke) {
      setJalur(null);
      setCatatan("Asal dan tujuannya sama. Pilih profesi lain.");
      return;
    }
    const ini = ++nomor.current;
    setCatatan(null);
    ambil<{ jalur: string[]; celah: string[][] }>("karier/jalur", { dari, ke })
      .then((r) => {
        // Jawaban yang datang terlambat dibuang. Tanpa penomoran ini, mengubah
        // asal dua kali cepat bisa menampilkan jalur permintaan PERTAMA.
        if (ini !== nomor.current) return;
        if (!r.jalur.length) {
          setJalur(null);
          setCatatan("Belum ada jalur yang tercatat di antara keduanya.");
        } else {
          setJalur(r);
        }
      })
      .catch((e: Error) => {
        if (ini === nomor.current) setCatatan(e.message);
      });
  }, [dari, ke]);

  const kur = data.kurikulum;
  const perId = new Map(data.profesi.map((p) => [p.id, p]));
  const opsiProfesi = useMemo(
    () => data.profesi.map((p) => ({ id: p.id, nama: p.nama })),
    [data],
  );

  return (
    <section className="kr-bagian" aria-labelledby="kr-judul-pindah">
      <div className="kr-bagian-kepala">
        <span className="mata">Perencana perpindahan</span>
        <h2 id="kr-judul-pindah">Dari sini ke sana, lewat mana?</h2>
        <p>
          Jalur dihitung dari hubungan antarprofesi. Peran senior dihindari
          sebagai batu loncatan, karena jarang ada yang menjadi arsitek hanya
          untuk pindah ke peran lain.
        </p>
      </div>
      <div className="kr-pilih-jalur">
        {/* Bukan `<select>`: popup native-nya di luar kendali halaman dan di
            Wayland menutup sendiri begitu klik dilepas. Lihat `Pilihan.tsx`. */}
        <div className="pil-medan">
          <label htmlFor="kr-pilih-asal">Sekarang</label>
          <Pilihan
            id="kr-pilih-asal"
            label="Profesi asal"
            nilai={dari}
            opsi={opsiProfesi}
            onUbah={setDari}
          />
        </div>
        <span className="kr-panah" aria-hidden="true">
          <Ikon nama="lanjut" ukuran={20} />
        </span>
        <div className="pil-medan">
          <label htmlFor="kr-pilih-tujuan">Ingin menjadi</label>
          <Pilihan
            id="kr-pilih-tujuan"
            label="Profesi tujuan"
            nilai={ke}
            opsi={opsiProfesi}
            onUbah={(v) => onPilih(v, true)}
          />
        </div>
      </div>
      <div className="kr-jalur" aria-live="polite">
        {catatan ? <p className="kr-catatan">{catatan}</p> : null}
        {jalur ? (
          <>
            <ol className="kr-langkah">
              {jalur.jalur.map((pid, i) => (
                <li key={pid}>
                  <button
                    type="button"
                    className="kr-langkah-tbl"
                    onClick={() => onPilih(pid, true)}
                  >
                    <span className="kr-langkah-no">
                      {i === 0
                        ? "sekarang"
                        : i === jalur.jalur.length - 1
                          ? "tujuan"
                          : "lewat"}
                    </span>
                    <span>{perId.get(pid)?.nama ?? pid}</span>
                  </button>
                </li>
              ))}
            </ol>
            {jalur.celah.length ? (
              <div className="kr-celah">
                <h3>Bekal yang perlu ditambah</h3>
                <ul>
                  {jalur.celah.map((grup, i) => (
                    <li key={i}>
                      {grup.map((k, j) => (
                        <span key={k}>
                          {j ? <span className="kr-atau">atau</span> : null}
                          <a href={"#/bahasa/" + k}>
                            {kur[k]?.label ?? k}
                            <span className="kr-persen">
                              {persenTeks(kur[k]?.persen ?? 0)}
                            </span>
                          </a>
                        </span>
                      ))}
                    </li>
                  ))}
                </ul>
              </div>
            ) : (
              <p className="kr-catatan">
                Bekal profesi tujuan sudah tercakup bekal profesi asal. Yang
                membedakan tinggal pengalaman dan kedalaman.
              </p>
            )}
          </>
        ) : null}
      </div>
    </section>
  );
}
