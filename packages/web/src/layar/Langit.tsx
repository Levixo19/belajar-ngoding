/* Layar Langit: 32 kurikulum sebagai rasi, 1.062 materi sebagai bintang.
 *
 * Dua tampilan atas data yang SAMA (`/api/langit`):
 *
 *   ikhtisar  peta 32 rasi, dibaca dari jauh. Memilih sebuah rasi membuka
 *   lensa     satu rasi diperbesar; bintangnya berbentuk per status, berlabel
 *             nomor, bisa dipilih, dan panel di sampingnya menampilkan detail
 *             bintang yang dipilih.
 *
 * Yang TIDAK berubah: peta ini tidak memutuskan apa pun. Status dan
 * "terkunci" datang dari `bab.status` lewat `/api/langit`, garis profesi dari
 * `data/karier.py`, alasan terkunci dari `pelajar/bab.py`. Layar ini menautkan
 * ke Peta Karier, bukan menghitung kesiapan kedua.
 *
 * Keadaan lensa ada di ALAMAT (`#/langit/<kurikulum>/<nomor>`), ditulis lewat
 * `history.replaceState` seperti Peta Karier: router tidak perlu menggambar
 * ulang layar hanya karena sebuah bintang dipilih, dan "Kembali" dari layar
 * materi mendarat di lensa yang sama dengan bintang yang sama, bukan di puncak
 * peta setinggi dua layar. Router sendiri TIDAK berubah: ia membaca ruas
 * pertama saja, dan `hashchange` didengarkan di sini.
 */

import { useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";

import { ambil } from "../api.ts";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { Pilihan } from "../komponen/Pilihan.tsx";
import { bacaAlamat } from "../komponen/lensa-teks.ts";
import type { MateriBintang } from "../komponen/rasi-geometri.ts";
import { tanpaNomor } from "../util.tsx";
import { Daftar } from "./LangitDaftar.tsx";
import { Ikhtisar, Legenda } from "./LangitIkhtisar.tsx";
import { Lensa, skalaTeksAplikasi } from "./LangitLensa.tsx";
import {
  bentukJawabanSah,
  KELUARGA,
  KONSEP,
  TATA,
  Tembolok,
  type DataB,
  type DataM,
  type Jawaban,
  type Langkah,
  type Saran,
} from "./langit-data.ts";

/** Lebar `.lt-halaman` (px) di bawah ini memakai DAFTAR rasi, bukan peta.
 *
 *  Angkanya diukur, bukan diperkirakan: pada peta selebar 1.126 px masih ada
 *  satu nama rasi yang menimpa bintang dan penanda "mulai di sini" menimpa
 *  label; 1.141 px masih satu nama~bintang; dari 1.156 px nol tabrakan nama,
 *  judul keluarga, bintang, dan penanda (diukur dengan teks 12 px sebagai
 *  lantai). Diukur pada ELEMEN AKAR layar, bukan pada jendela: lebar yang
 *  tersedia = jendela - padding `#layar` (64 px) - lebar bilah gulir, dan
 *  zoom peramban serta setelan lebar kolom ikut terhitung dengan sendirinya.
 *  Hanya JS yang memutuskannya (CSS cuma menata masing-masing tampilan),
 *  jadi tidak ada angka kedua yang bisa meleset darinya.
 *
 *  Angkanya berlaku pada ukuran huruf 16 px dan DIKALIKAN faktor ukuran huruf
 *  aplikasi (`skalaTeksAplikasi`): teks peta mengikuti `rem`, jadi pada 20 px
 *  (faktor 1,25) petanya baru bebas tabrakan dari 1.445 px. Di bawah itu yang
 *  tampil Daftar, yang tumbuh bersama hurufnya. */
export const AMBANG_PETA = 1156;

interface PilihanLensa {
  key: string;
  indeks: number | null;
}

/** Pilihan perkakas (konsep, profesi) disimpan di `history.state` entri ini,
 *  BUKAN di localStorage: "buka materi lalu Kembali" harus memulihkannya, tetapi
 *  kunjungan besok tidak boleh membuka peta yang sudah meredup oleh saringan
 *  yang dipilih minggu lalu. `profesi === ""` = sengaja memilih "Tanpa
 *  profesi"; `null` = belum memilih (tujuan karier dari server berlaku). */
interface KeadaanPerkakas {
  konsep: string | null;
  profesi: string | null;
}

function bacaKeadaan(): KeadaanPerkakas | null {
  const st = history.state as { lt?: Partial<KeadaanPerkakas> } | null;
  const k = st?.lt;
  if (!k || typeof k !== "object") return null;
  return {
    konsep: typeof k.konsep === "string" ? k.konsep : null,
    profesi: typeof k.profesi === "string" ? k.profesi : null,
  };
}

function tulisKeadaan(k: KeadaanPerkakas) {
  try {
    history.replaceState({ ...(history.state as object | null), lt: k }, "", location.href);
  } catch {
    // Browser membatasi laju replaceState; keadaan yang tak tersimpan cuma
    // berarti Kembali memulihkan tanpa saringan.
  }
}

function tulisAlamat(p: PilihanLensa | null) {
  try {
    history.replaceState(
      history.state,
      "",
      "#/langit" + (p ? "/" + p.key + (p.indeks !== null ? "/" + p.indeks : "") : ""),
    );
  } catch {
    // Browser membatasi laju replaceState. Alamat yang tidak ikut berubah
    // bukan alasan menggagalkan pilihannya.
  }
}

/** Pemuatan dokumen pertama tidak boleh merebut fokus (pelajar yang baru
 *  menempel alamat belum memilih apa pun). Kunjungan berikutnya di dokumen
 *  yang sama (Kembali dari materi, menu) memindahkan fokus ke bintangnya. */
let pemuatanPertama = true;

/** Lebar elemen akar layar; 0 sampai diukur (sebelum gambar pertama). Memakai
 *  ref-panggilan, bukan `useRef`: akarnya baru ada SESUDAH data tiba (sebelum
 *  itu layar menggambar pusaran), dan efek berbasis `useRef` sudah berjalan
 *  dengan elemen yang belum ada -- pengamatnya tidak pernah terpasang. */
function useLebarAkar(): [(el: HTMLDivElement | null) => void, number] {
  const [el, setEl] = useState<HTMLDivElement | null>(null);
  const [lebar, setLebar] = useState(0);
  useLayoutEffect(() => {
    if (!el) return;
    setLebar(el.clientWidth);
    const amat = new ResizeObserver((e) => {
      const w = e[0]?.contentRect.width ?? 0;
      if (w === 0) return;
      setLebar((lama) => (Math.abs(lama - w) < 0.5 ? lama : w));
    });
    amat.observe(el);
    return () => amat.disconnect();
  }, [el]);
  return [setEl, lebar];
}

export function Langit() {
  const [data, setData] = useState<Jawaban | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [saran, setSaran] = useState<Saran | null>(null);
  /* Pilihan perkakas dipulihkan dari `history.state` (lihat `KeadaanPerkakas`),
     karena "buka materi lalu Kembali" adalah pola pemakaian yang paling umum
     di layar ini dan dulu menghapus keduanya. `profesiPilihan` null = pelajar
     belum memilih di layar ini: profesi tujuan karier dari server berlaku, dan
     ia diturunkan (`profesiId`), tidak disalin ke state. Yang disalin akan
     ikut tertulis ke `history.state` seolah pilihan pelajar dan basi begitu
     tujuannya diganti di Peta Karier. */
  const [profesiPilihan, setProfesiPilihan] = useState<string | null>(() => bacaKeadaan()?.profesi ?? null);
  const [konsep, setKonsep] = useState<string | null>(() => bacaKeadaan()?.konsep ?? null);
  // `true` bila Langit ini adalah mount PERTAMA di dokumen ini: lensa yang
  // dibuka oleh alamat yang sedang dimuat (bukan oleh tindakan pelajar) tidak
  // memindahkan fokus. Tindakan pelajar (`buka`) dan navigasi riwayat
  // sesudahnya (Kembali, menu) memindahkannya.
  const dokumenBaru = useRef(pemuatanPertama);
  const fokusLensa = useRef(false);
  useEffect(() => {
    pemuatanPertama = false;
  }, []);
  const [lensa, setLensa] = useState<PilihanLensa | null>(null);
  const lensaRef = useRef<PilihanLensa | null>(null);
  lensaRef.current = lensa;
  const [setAkar, lebarAkar] = useLebarAkar();
  const [skalaTeks] = useState(skalaTeksAplikasi);
  const peta = lebarAkar >= AMBANG_PETA * skalaTeks;
  const berkas = useRef({ b: new Tembolok<DataB>(), m: new Tembolok<DataM>() }).current;
  const terakhir = useRef<string | null>(null);

  useEffect(() => {
    let dibatalkan = false;
    ambil<unknown>("langit")
      .then((d) => {
        if (dibatalkan) return;
        if (!bentukJawabanSah(d)) {
          setGalat("Jawaban server untuk peta langit tidak berbentuk yang dikenal.");
          return;
        }
        setData(d);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    // Satu penanda "mulai di sini": langkah materi pertama dari saran yang
    // SAMA dengan kartu utama Dasbor. Gagal memuatnya tidak mengganggu apa
    // pun; petanya cuma tanpa penanda itu.
    ambil<{ xp: number; langkah: Langkah[] }>("dasbor")
      .then((d) => {
        if (dibatalkan) return;
        const l = d.langkah.find((x) => x.tipe === "materi");
        if (l) setSaran({ bahasa: l.bahasa, indeks: l.indeks, alasan: l.alasan });
      })
      .catch(() => {});
    return () => {
      dibatalkan = true;
    };
  }, []);

  // Lensa mengikuti alamat: saat data tiba, dan setiap `hashchange` (Kembali
  // dari layar materi, tautan "Langit" di menu).
  useEffect(() => {
    if (!data) return;
    const sinkron = (awal: boolean) => {
      fokusLensa.current = !(awal && dokumenBaru.current);
      const p = bacaAlamat(globalThis.location.hash);
      const b = p ? data.bahasa.find((x) => x.key === p.key) : undefined;
      if (!p || !b) {
        setLensa(null);
        // Kunci yang tidak dikenal (tautan lama, salah ketik) dibersihkan dari
        // alamat; tanpa ini "Kembali" mendarat lagi di alamat yang kosong.
        if (p) tulisAlamat(null);
        return;
      }
      setLensa({ key: p.key, indeks: p.indeks !== null && p.indeks < b.materi.length ? p.indeks : null });
    };
    sinkron(true);
    const ubah = () => sinkron(false);
    globalThis.addEventListener("hashchange", ubah);
    return () => globalThis.removeEventListener("hashchange", ubah);
  }, [data]);

  const buka = useCallback((key: string, indeks: number | null) => {
    const p = { key, indeks };
    terakhir.current = key;
    fokusLensa.current = true;
    setLensa(p);
    tulisAlamat(p);
  }, []);

  const pilihBintang = useCallback((i: number | null) => {
    const l = lensaRef.current;
    if (!l) return;
    const p = { key: l.key, indeks: i };
    setLensa(p);
    tulisAlamat(p);
  }, []);

  const tutup = useCallback(() => {
    setLensa(null);
    tulisAlamat(null);
  }, []);

  // Sesudah lensa tertutup: kembalikan pembaca ke rasi yang baru ditinggalkan
  // (gulir + fokus). Hanya menyentuh `scrollTop` jendela; `scrollIntoView`
  // menggulir SEMUA leluhur yang bisa digulir.
  useLayoutEffect(() => {
    if (lensa || !terakhir.current) return;
    const key = terakhir.current;
    terakhir.current = null;
    const el = document.querySelector<HTMLElement>(
      `.lt-nama[data-key="${key}"], .lt-daftar-baris[data-key="${key}"]`,
    );
    if (!el) return;
    const k = el.getBoundingClientRect();
    globalThis.scrollTo({ top: globalThis.scrollY + k.top - globalThis.innerHeight * 0.4 });
    el.focus({ preventScroll: true });
  }, [lensa]);

  // Lensa menggantikan kepala, perkakas, dan peta (semuanya `hidden`, bukan
  // dilepas: peta yang dilepas harus dihitung ulang tiap kali lensa ditutup),
  // jadi ia mulai di puncak halaman dan tidak ada yang mengintip di atasnya.
  const kunciLensa = lensa?.key ?? null;
  useLayoutEffect(() => {
    if (!kunciLensa) return;
    terakhir.current = kunciLensa;
    globalThis.scrollTo({ top: 0 });
  }, [kunciLensa]);

  useEffect(() => {
    tulisKeadaan({ konsep, profesi: profesiPilihan });
  }, [konsep, profesiPilihan]);

  const polaKonsep = konsep ? (KONSEP.find(([n]) => n === konsep)?.[1] ?? null) : null;
  const cocok = useCallback(
    (m: MateriBintang) => polaKonsep !== null && polaKonsep.test(tanpaNomor(m.judul)),
    [polaKonsep],
  );

  // Cacah materi yang cocok per kurikulum: masuk nama aksesibel rasi, supaya
  // hasil saringan konsep tidak hanya ada di cincin yang digambar.
  const cocokPer = useMemo(() => {
    const o: Record<string, number> = {};
    if (polaKonsep && data) for (const b of data.bahasa) o[b.key] = b.materi.filter((m) => cocok(m)).length;
    return o;
  }, [data, polaKonsep, cocok]);

  // Pilihan pelajar menang; tanpa itu tujuan karier dari server. Memilih nilai
  // yang sama dengan tujuan disimpan sebagai null, supaya tujuan yang diganti
  // sesudahnya tetap diikuti.
  const profesiId = profesiPilihan ?? data?.tujuan ?? null;
  const pilihProfesi = useCallback(
    (id: string) => setProfesiPilihan(id === (data?.tujuan ?? "") ? null : id),
    [data],
  );
  const profesi = useMemo(
    () => data?.profesi.find((p) => p.id === (profesiId ?? "")) ?? null,
    [data, profesiId],
  );
  const pusat = useMemo(() => new Set(data?.bahasa.map((b) => b.key) ?? []), [data]);
  // Kelompok bekal yang kurikulumnya benar-benar ada di peta. Yang tidak ada
  // dibuang di sini, bukan saat menggambar: kelompok kosong menghasilkan garis
  // dari dan ke tempat yang tidak ada.
  const kelompok = useMemo(
    () =>
      profesi
        ? profesi.bekal.map((g) => g.filter((k) => pusat.has(k))).filter((g) => g.length)
        : [],
    [profesi, pusat],
  );
  const bekal = useMemo(() => new Set(kelompok.flat()), [kelompok]);

  // Urutan baca antar-rasi: keluarga lebih dulu, lalu urutan peta.
  const urutan = useMemo(() => {
    const k = Object.keys(TATA);
    const di = (key: string) => {
      const x = k.indexOf(key);
      return x < 0 ? k.length : x;
    };
    return (data?.bahasa ?? []).map((b) => b.key).sort((a, b) => di(a) - di(b));
  }, [data]);

  if (galat) return <Keadaan jenis="salah" judul="Gagal memuat Langit" ket={galat} />;
  if (!data) {
    return (
      <div className="deret" role="status">
        <div className="pusaran" aria-hidden="true" />
        <span>Memuat peta langit…</span>
      </div>
    );
  }

  const totalMateri = data.bahasa.reduce((a, b) => a + b.materi.length, 0);
  const menyala = data.bahasa.reduce(
    (a, b) => a + b.materi.filter((m) => m.status === "selesai").length,
    0,
  );
  const labelKurikulum = (k: string) => data.bahasa.find((b) => b.key === k)?.label ?? k;

  let jumlahKonsep = 0;
  const kurikulumKonsep = new Set<string>();
  if (polaKonsep) {
    for (const b of data.bahasa) {
      for (const m of b.materi) {
        if (cocok(m)) {
          jumlahKonsep += 1;
          kurikulumKonsep.add(b.label);
        }
      }
    }
  }
  let keterangan = "";
  if (konsep) {
    keterangan =
      `${konsep}: ${jumlahKonsep} materi di ${kurikulumKonsep.size} kurikulum. ` +
      "Konsepnya sama, cara menulisnya yang berbeda.";
  } else if (profesi) {
    const bagian = kelompok.map((g) =>
      g.length > 1
        ? `salah satu dari ${g.map(labelKurikulum).join(", ")}`
        : labelKurikulum(g[0] as string),
    );
    keterangan = `${profesi.nama} berbekal ${bagian.join("; lalu ")}.`;
  }

  const idxLensa = lensa ? urutan.indexOf(lensa.key) : -1;
  const tetangga = (i: number) => {
    const key = urutan[i];
    return key ? { key, label: labelKurikulum(key) } : null;
  };
  const keluargaLensa = lensa
    ? (KELUARGA[TATA[lensa.key]?.[2] ?? "tech"]?.[0] ?? "Tech stack")
    : "";

  return (
    <div ref={setAkar} className="bimasakti lt-halaman">
      <div className="lt-krom" hidden={lensa !== null}>
        {/* Lewati saringan (profesi dan 14 chip konsep) ke isi layar. Di Daftar
            (akar sempit) tanpa ini papan ketik melewati sekitar 16 kontrol
            lebih dulu, dan di sana justru orang yang paling bergantung pada Tab. */}
        <button
          type="button"
          className="tbl tbl-kecil lt-lewati"
          onClick={() =>
            document.querySelector<HTMLElement>(peta ? ".lt-ik-teks a" : ".lt-daftar a")?.focus()
          }
        >
          {peta ? "Lewati ke peta bintang" : "Lewati ke daftar rasi"}
        </button>
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
            <Pilihan
              kelasPemicu="langit-pilih"
              label="Hubungkan rasi lewat profesi"
              namaTombol="Hubungkan rasi lewat profesi"
              gaya={{ minWidth: "13rem" }}
              nilai={profesiId ?? ""}
              opsi={[
                { id: "", nama: "Tanpa profesi" },
                ...data.profesi.map((p) => ({ id: p.id, nama: p.nama })),
              ]}
              onUbah={pilihProfesi}
            />
          </label>
          <a className="tbl tbl-kecil tbl-hantu" href="#/karier">
            Buka Peta Karier
          </a>
          <Legenda />
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
      </div>

      <div hidden={lensa !== null}>
        {lebarAkar === 0 ? null : !peta ? (
          <Daftar
            bahasa={data.bahasa}
            bekal={bekal}
            adaProfesi={!!profesi}
            profesiNama={profesi?.nama ?? null}
            konsepNama={konsep}
            cocokPer={cocokPer}
            saran={saran}
            onBuka={buka}
          />
        ) : (
          <Ikhtisar
            data={data}
            saran={saran}
            cocok={cocok}
            adaKonsep={konsep !== null}
            konsepNama={konsep}
            cocokPer={cocokPer}
            bekal={bekal}
            adaProfesi={!!profesi}
            profesiNama={profesi?.nama ?? null}
            kelompok={kelompok}
            onBuka={buka}
            lebarAkar={lebarAkar}
          />
        )}
      </div>

      {lensa ? <h1 className="lt-sr">Langit</h1> : null}
      {lensa ? (
        <Lensa
          key={lensa.key}
          fokusAwal={fokusLensa.current}
          data={data}
          kunci={lensa.key}
          indeks={lensa.indeks}
          berkas={berkas}
          keluarga={keluargaLensa}
          cocok={cocok}
          adaKonsep={konsep !== null}
          konsepNama={konsep}
          profesiNama={profesi?.nama ?? null}
          sebelum={tetangga(idxLensa - 1)}
          sesudah={tetangga(idxLensa + 1)}
          onPilih={pilihBintang}
          onTutup={tutup}
          onKeRasi={(key) => buka(key, null)}
          onLepasKonsep={() => setKonsep(null)}
          onLepasProfesi={() => pilihProfesi("")}
        />
      ) : null}
    </div>
  );
}
