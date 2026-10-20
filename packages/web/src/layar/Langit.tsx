/* Layar Langit: 32 kurikulum sebagai rasi, 1.062 materi sebagai bintang.
 *
 * Port `webapp/statik/js/layar-langit.js`. Perbedaan terbesar saat diport:
 * versi JS men-TOGGLE kelas (`rasi-konsep`, `langit-terpilih`, `ada-profesi`,
 * `ada-konsep`) langsung pada elemen lewat `classList`. Di sini semuanya
 * TURUNAN dari state. Itu bukan selera: versi imperatif harus ingat
 * membersihkan kelas yang dipasang sebelumnya, dan satu cabang yang lupa
 * membersihkannya meninggalkan bintang yang menyala untuk konsep yang sudah
 * tidak dipilih lagi -- tanpa satu pun error.
 *
 * Yang TIDAK berubah: peta ini tidak memutuskan apa pun. Status dan "terkunci"
 * datang dari `bab.status` lewat `/api/langit`, dan garis profesi dari
 * `data/karier.py`. Layar ini menautkan ke Peta Karier, bukan menghitung
 * kesiapan kedua.
 */

import { useEffect, useMemo, useState } from "react";

import { ambil } from "../api.ts";
import { tingkatGerak } from "../gerak.ts";
import { Keadaan } from "../komponen/Keadaan.tsx";
import {
  Bintang,
  GarisRasi,
  jariSemua,
  Reticle,
  useTip,
  useWadahPeta,
} from "../komponen/Rasi.tsx";
import {
  berikutDari,
  bentukRasi,
  KATA_STATUS,
  type MateriBintang,
  type Titik,
} from "../komponen/rasi-geometri.ts";
import { tanpaNomor } from "../util.tsx";

const W = 1400;
const H = 1420;

/* Letak tiap kurikulum (pusat rasi) dan keluarganya. Kurikulum baru yang
   belum terdaftar di sini tetap muncul, di baris cadangan paling bawah --
   jalur itu sengaja ada supaya menambah kurikulum tidak pernah membuat sebuah
   kurikulum hilang dari peta. */
const TATA: Record<string, [number, number, string]> = {
  html: [170, 200, "web"], css: [330, 140, "web"], javascript: [300, 330, "web"],
  typescript: [470, 260, "web"], php: [150, 420, "web"],
  c: [700, 150, "sistem"], cpp: [860, 210, "sistem"], rust: [760, 350, "sistem"],
  go: [930, 380, "sistem"],
  java: [1090, 150, "jvm"], kotlin: [1270, 220, "jvm"], aplikasi: [1060, 350, "jvm"],
  csharp: [1270, 420, "jvm"], vb: [1120, 540, "jvm"],
  python: [430, 560, "skrip"], ruby: [250, 640, "skrip"], bash: [570, 700, "skrip"],
  git: [790, 600, "perkakas"], fedora: [980, 680, "perkakas"], sql: [1290, 680, "perkakas"],
  techstack: [150, 980, "tech"], frontend: [390, 1055, "tech"], backend: [630, 975, "tech"],
  database: [870, 1050, "tech"], devops: [1110, 975, "tech"], keamanan: [1310, 1065, "tech"],
  mobile: [150, 1235, "tech"], game: [390, 1300, "tech"], iot: [630, 1230, "tech"],
  data: [870, 1300, "tech"], ai: [1110, 1230, "tech"], bahasalain: [1310, 1310, "tech"],
};

const KELUARGA: Record<string, [string, number, number]> = {
  web: ["Web", 60, 60], sistem: ["Sistem", 640, 50], jvm: ["JVM & .NET", 1080, 50],
  skrip: ["Skrip", 60, 835], perkakas: ["Perkakas & data", 1110, 835],
  tech: ["Tech stack", 60, 1405],
};

/* Konsep yang muncul di banyak kurikulum sekaligus. Polanya mencocokkan JUDUL
   materi, bukan isinya: judul di kurikulum ini memang menyebut konsepnya, dan
   mencocokkan isi akan menyalakan hampir semua bintang untuk hampir semua
   konsep. */
const KONSEP: Array<[string, RegExp]> = [
  ["Variabel & tipe", /variabel|tipe data|\bval\b|\bvar\b|konstanta/i],
  ["Percabangan", /percabangan|kendali alur|\bif\b|switch|\bwhen\b|select case|\bcase\b/i],
  ["Perulangan", /perulangan|loop|\bfor\b|while|iterasi|iterator/i],
  ["Fungsi", /fungsi|function|method|\bsub\b|prosedur|closure|lambda/i],
  ["Koleksi", /array|\blist\b|slice|koleksi|collection|\bmap\b|dict|hash|\bset\b|\bvec\b|tuple|stl/i],
  ["Teks & regex", /string|teks|regex|ekspresi reguler/i],
  ["Objek & class", /class|objek|oop|struct|record|interface|trait|pewarisan|inheritance|polymorph/i],
  ["Galat", /exception|galat|error|panic|\bresult\b/i],
  ["Berkas & I/O", /berkas|\bfile\b|i\/o|input|output|json|csv/i],
  ["Pengujian", /pengujian|\btest|\buji|debug/i],
  ["Konkurensi", /konkurensi|thread|goroutine|async|await|paralel|bersamaan|coroutine|race/i],
  ["Algoritma", /rekursi|algoritma|big-o|sorting|pengurutan|pencarian|kompleksitas/i],
  ["Modul & paket", /modul|paket|package|import|namespace|crate|dependensi|maven|gradle/i],
  ["Database", /database|\bsql\b|query|join|tabel|jdbc|pdo|transaksi/i],
];

interface Bab {
  materi: number[];
}

interface BahasaLangit {
  key: string;
  label: string;
  materi: MateriBintang[];
  bab?: Bab[];
}

interface Profesi {
  id: string;
  nama: string;
  /** Tiap kelompok = "salah satu dari". */
  bekal: string[][];
}

interface Jawaban {
  bahasa: BahasaLangit[];
  profesi: Profesi[];
  tujuan?: string;
}

export function Langit() {
  const [data, setData] = useState<Jawaban | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [profesiId, setProfesiId] = useState("");
  const [konsep, setKonsep] = useState<string | null>(null);
  const wadahRef = useWadahPeta();
  const tip = useTip(wadahRef);

  useEffect(() => {
    let dibatalkan = false;
    ambil<Jawaban>("langit")
      .then((d) => {
        if (dibatalkan) return;
        setData(d);
        // Tujuan karier yang sudah dipilih pelajar langsung ditandai, sama
        // seperti versi JS-nya.
        if (d.tujuan) setProfesiId(d.tujuan);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, []);

  /* Letak seluruh bintang dihitung SEKALI per muatan data. Tanpa `useMemo`, ia
     dihitung ulang setiap kali tip bergerak atau konsep diklik -- 1.062 bintang
     kali tiap gerakan mouse. */
  const tataLetak = useMemo(() => {
    if (!data) return null;
    let cadangan = 0;
    const pusat: Record<string, Titik> = {};
    const rasi = data.bahasa.map((b, urut) => {
      const letak = TATA[b.key] ?? [140 + cadangan++ * 180, 820];
      const cx = letak[0] as number;
      const cy = letak[1] as number;
      pusat[b.key] = [cx, cy];
      const titik = bentukRasi(b.materi.length, "langit·" + b.key, 150, 112).map(
        ([x, y]) => [cx + x, cy + y] as Titik,
      );
      const r = jariSemua(b.materi, 0.62);
      const awalBab = new Set((b.bab ?? []).map((x) => x.materi[0]));
      const selesai = b.materi.filter((m) => m.status === "selesai").length;
      return { b, urut, cx, cy, titik, r, awalBab, selesai };
    });
    return { pusat, rasi };
  }, [data]);

  if (galat) {
    return <Keadaan jenis="salah" judul="Gagal memuat Langit" ket={galat} />;
  }
  if (!data || !tataLetak) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat peta langit…</span>
      </div>
    );
  }

  const totalMateri = data.bahasa.reduce((a, b) => a + b.materi.length, 0);
  const menyala = data.bahasa.reduce(
    (a, b) => a + b.materi.filter((m) => m.status === "selesai").length,
    0,
  );

  const profesi = data.profesi.find((p) => p.id === profesiId) ?? null;
  // Kelompok bekal yang kurikulumnya benar-benar ada di peta. Yang tidak ada
  // dibuang di sini, bukan saat menggambar: kelompok kosong akan menghasilkan
  // garis dari dan ke tempat yang tidak ada.
  const kelompok = profesi
    ? profesi.bekal
        .map((g) => g.filter((k) => tataLetak.pusat[k]))
        .filter((g) => g.length)
    : [];
  const terpilih = new Set(kelompok.flat());

  const polaKonsep = konsep
    ? (KONSEP.find(([n]) => n === konsep)?.[1] ?? null)
    : null;
  const cocokKonsep = (m: MateriBintang) =>
    polaKonsep !== null && polaKonsep.test(tanpaNomor(m.judul));

  let jumlahKonsep = 0;
  const kurikulumKonsep = new Set<string>();
  if (polaKonsep) {
    for (const b of data.bahasa) {
      for (const m of b.materi) {
        if (cocokKonsep(m)) {
          jumlahKonsep += 1;
          kurikulumKonsep.add(b.label);
        }
      }
    }
  }

  const labelKurikulum = (k: string) =>
    data.bahasa.find((b) => b.key === k)?.label ?? k;

  let keterangan = "";
  if (konsep) {
    keterangan =
      `${konsep}: ${jumlahKonsep} materi di ${kurikulumKonsep.size} ` +
      `kurikulum. Konsepnya sama, cara menulisnya yang berbeda.`;
  } else if (profesi) {
    const bagian = kelompok.map((g) =>
      g.length > 1
        ? `salah satu dari ${g.map(labelKurikulum).join(", ")}`
        : labelKurikulum(g[0] as string),
    );
    keterangan = `${profesi.nama} berbekal ${bagian.join("; lalu ")}.`;
  }

  const kelasSvg =
    "rasi-svg langit-svg" +
    (profesi ? " ada-profesi" : "") +
    (konsep ? " ada-konsep" : "");

  return (
    <div className="bimasakti">
      <header className="kepala-besar bimasakti-kepala">
        <span className="mata">Peta bintang</span>
        <h1>Langit</h1>
        <p className="kepala-sub">
          {`${data.bahasa.length} kurikulum, ${totalMateri} materi. Tiap materi satu bintang; `}
          {menyala
            ? `${menyala} sudah menyala karena sudah kamu baca.`
            : "belum ada yang menyala. Baca satu materi untuk menyalakan yang pertama."}
        </p>
      </header>

      <div className="langit-alat">
        <label className="langit-label">
          Hubungkan lewat profesi
          <select
            className="langit-pilih"
            aria-label="Hubungkan rasi lewat profesi"
            value={profesiId}
            onChange={(e) => setProfesiId(e.target.value)}
          >
            <option value="">Tanpa profesi</option>
            {data.profesi.map((p) => (
              <option key={p.id} value={p.id}>
                {p.nama}
              </option>
            ))}
          </select>
        </label>
        <a className="tbl tbl-kecil tbl-hantu" href="#/karier">
          Buka Peta Karier
        </a>
      </div>

      <div
        className="langit-konsep-deret"
        role="group"
        aria-label="Nyalakan konsep yang sama di semua kurikulum"
      >
        <span className="langit-label">Konsep yang sama</span>
        {KONSEP.map(([nama]) => (
          <button
            key={nama}
            type="button"
            className="tbl tbl-kecil tbl-hantu langit-konsep"
            aria-pressed={konsep === nama}
            onClick={() => setKonsep((k) => (k === nama ? null : nama))}
          >
            {nama}
          </button>
        ))}
      </div>

      <p className="langit-keterangan" aria-live="polite">
        {keterangan}
      </p>

      <div
        ref={wadahRef}
        className={
          "rasi langit-peta" + (tingkatGerak() === "penuh" ? " rasi-hidup" : "")
        }
      >
        <p className="rasi-ringkasan">
          {`Peta langit seluruh kurikulum: ${menyala} dari ${totalMateri} bintang menyala.`}
        </p>
        <svg
          viewBox={`0 0 ${W} ${H}`}
          className={kelasSvg}
          preserveAspectRatio="xMidYMid meet"
          onPointerLeave={tip.sembunyi}
        >
          {/* Lapis jalur profesi digambar PALING DULU supaya ia di bawah
              bintangnya. Garisnya melengkung ke atas (kontrol Q di -40) supaya
              dua rasi yang bertetangga tidak dihubungkan garis lurus yang
              menembus rasi di antaranya. */}
          <g>
            {kelompok.slice(1).map((gb, i) => {
              const ga = kelompok[i] as string[];
              return gb.flatMap((kb) =>
                ga.map((ka) => {
                  const a = tataLetak.pusat[ka] as Titik;
                  const b = tataLetak.pusat[kb] as Titik;
                  const mx = (a[0] + b[0]) / 2;
                  const my = (a[1] + b[1]) / 2 - 40;
                  return (
                    <path
                      key={`${ka}-${kb}`}
                      className="langit-profesi-garis"
                      fill="none"
                      d={`M${a[0]},${a[1]} Q${mx},${my} ${b[0]},${b[1]}`}
                    />
                  );
                }),
              );
            })}
          </g>

          <g>
            {tataLetak.rasi.map(({ b, urut, titik, r, awalBab }) => (
              <g
                key={b.key}
                className={
                  "rasi-kelompok langit-rasi" +
                  (terpilih.has(b.key) ? " langit-terpilih" : "")
                }
                data-key={b.key}
              >
                {b.materi.map((m, i) =>
                  // Garis putus di batas bab: tiap bab jadi rasi kecil di
                  // dalam rasi besar.
                  i > 0 && !awalBab.has(i) ? (
                    <GarisRasi
                      key={`g${i}`}
                      a={titik[i - 1] as Titik}
                      b={titik[i] as Titik}
                      ra={r[i - 1] as number}
                      rb={r[i] as number}
                      terang={
                        (b.materi[i - 1] as MateriBintang).status === "selesai" &&
                        m.status === "selesai"
                      }
                    />
                  ) : null,
                )}
                {b.materi.map((m, i) => (
                  <Bintang
                    key={`b${i}`}
                    materi={m}
                    x={(titik[i] as Titik)[0]}
                    y={(titik[i] as Titik)[1]}
                    r={r[i] as number}
                    href={`#/materi/${b.key}/${i}`}
                    dataKey={b.key}
                    indeks={i}
                    urut={urut * 3 + (i % 9)}
                    kelasEkstra={
                      (cocokKonsep(m) ? "rasi-konsep " : "") +
                      (terpilih.has(b.key) ? "langit-terpilih" : "")
                    }
                    onTunjuk={(el, materi) =>
                      tip.tunjuk(
                        el,
                        materi.judul,
                        `${b.label} · ${
                          materi.terkunci
                            ? "masih terkunci"
                            : (KATA_STATUS[materi.status] ?? "")
                        }`,
                      )
                    }
                  />
                ))}
              </g>
            ))}
          </g>

          <g>
            {Object.values(KELUARGA).map(([nama, x, y]) => (
              <text key={nama} className="langit-keluarga" x={x} y={y}>
                {nama}
              </text>
            ))}
            {tataLetak.rasi.map(({ b, titik, r, selesai }) => {
              const berikut = berikutDari(b.materi);
              return selesai && berikut !== null ? (
                <Reticle
                  key={`r${b.key}`}
                  x={(titik[berikut] as Titik)[0]}
                  y={(titik[berikut] as Titik)[1]}
                  r={r[berikut] as number}
                />
              ) : null;
            })}
            {tataLetak.rasi.map(({ b, cx, cy, selesai }) => (
              <a
                key={`n${b.key}`}
                className={
                  "langit-nama" + (terpilih.has(b.key) ? " langit-terpilih" : "")
                }
                href={`#/bahasa/${b.key}`}
                data-key={b.key}
                aria-label={`${b.label}: ${selesai} dari ${b.materi.length} materi sudah dibaca`}
              >
                <text
                  x={cx}
                  y={cy + 82}
                  textAnchor="middle"
                  className="langit-nama-teks"
                >
                  {b.label}
                </text>
                <text
                  x={cx}
                  y={cy + 100}
                  textAnchor="middle"
                  className="langit-nama-angka"
                >
                  {`${selesai}/${b.materi.length}`}
                </text>
              </a>
            ))}
          </g>
        </svg>
        {tip.elemen}
      </div>

      <Legenda />
    </div>
  );
}

/** Keterangan warna bintang. `aria-hidden`: isinya sudah dibacakan tiap
 *  `aria-label` bintangnya sendiri, jadi membacakannya lagi di sini cuma
 *  menambah empat kalimat sebelum petanya. */
function Legenda() {
  const butir: Array<[string, string]> = [
    ["selesai", "sudah dibaca"],
    ["sebagian", "dibaca sebagian"],
    ["baru", "belum dibaca"],
    ["terkunci", "terkunci"],
  ];
  return (
    <div className="langit-legenda" aria-hidden="true">
      {butir.map(([st, kata]) => {
        const m: MateriBintang = {
          judul: "",
          status: st === "terkunci" ? "baru" : st,
          terkunci: st === "terkunci",
        };
        const jari = jariSemua([m], 0.9)[0] as number;
        return (
          <span key={st} className="langit-legenda-butir">
            <svg viewBox="-10 -10 20 20" width={20} height={20}>
              <circle r={jari.toFixed(2)} className={"rasi-titik rasi-" + st} />
            </svg>
            {kata}
          </span>
        );
      })}
      <span className="langit-legenda-butir">
        <svg viewBox="-16 -16 32 32" width={24} height={24}>
          <Reticle x={0} y={0} r={2} />
        </svg>
        berikutnya
      </span>
    </div>
  );
}
