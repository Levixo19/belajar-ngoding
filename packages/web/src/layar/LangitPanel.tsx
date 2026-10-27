/* Panel di sebelah lensa: rasi yang sedang diperbesar, atau satu bintang
 * yang dipilih.
 *
 * Tiap baris panel punya SATU sumber data yang bisa ditunjuk, dan yang tidak
 * punya sumber tidak ada di sini:
 *
 *   judul, nomor, status, bab ......... `/api/langit` (sudah di tangan)
 *   kemajuan bab ...................... dihitung dari status bintang di atas
 *   menit, jumlah bagian, tingkat ..... `/api/bahasa?key=`  (per kurikulum)
 *   alasan terkunci, ringkasan bab .... `/api/bahasa?key=`  (kalimat milik server)
 *   deskripsi ......................... `/api/materi`, paragraf pembuka, hanya
 *                                       untuk materi yang BUKAN terkunci
 *   profesi yang membutuhkan .......... `/api/langit -> profesi[].bekal`
 *
 * Yang tidak ada dan tidak dijanjikan: kuis atau latihan PER MATERI (tidak ada
 * di API mana pun), dan deskripsi materi terkunci (server menolaknya 403).
 * Kalimat alasan terkunci milik `pelajar/bab.py`; di sini cuma dicetak ulang.
 */

import { useEffect, useState } from "react";

import { ambil } from "../api.ts";
import { Glif } from "../komponen/Glif.tsx";
import { Ikon } from "../komponen/Ikon.tsx";
import {
  KATA_STATUS_BINTANG,
  romawi,
  statusBintang,
  type BahasaLangit,
} from "../komponen/lensa-geometri.ts";
import { hitungBab, kataAksiBaca, pecahKode, ringkasPembuka } from "../komponen/lensa-teks.ts";
import { tanpaNomor } from "../util.tsx";
import { Tembolok, type DataB, type DataM, type Profesi } from "./langit-data.ts";

/** Pil status memakai kelas yang SUDAH ada di `gaya.css`: selesai = verdigris,
 *  sebagian = kuningan, terkunci = pil paling redup. */
const PIL_STATUS = {
  selesai: "pil pil-tumbuh",
  sebagian: "pil pil-nyala",
  baru: "pil",
  terkunci: "pil pil-kunci",
} as const;

/** Profesi yang disebut satu per satu di "Dipakai di profesi"; sisanya
 *  disebut jumlahnya (git dipakai 18 profesi, python 13). */
const MAKS_PROFESI = 4;

export interface Berkas {
  b: Tembolok<DataB>;
  m: Tembolok<DataM>;
}

/** Hasil satu permintaan bertembolok. `kunci` ikut dicatat supaya jawaban lama
 *  tidak pernah dibaca untuk kunci yang sudah berganti. */
function useBertembolok<T>(
  tembolok: Tembolok<T>,
  kunci: string | null,
  buat: () => Promise<T>,
): { data: T | null; galat: string | null } {
  const [hasil, setHasil] = useState<{ kunci: string; data: T | null; galat: string | null } | null>(null);
  useEffect(() => {
    if (kunci === null) return;
    let dibatalkan = false;
    tembolok
      .ambil(kunci, buat)
      .then((data) => { if (!dibatalkan) setHasil({ kunci, data, galat: null }); })
      .catch((e: Error) => { if (!dibatalkan) setHasil({ kunci, data: null, galat: e.message }); });
    return () => { dibatalkan = true; };
    // `buat` sengaja di luar daftar: ia dibuat ulang tiap render, dan satu-
    // satunya yang menentukan permintaan mana yang jalan adalah `kunci`.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [kunci, tembolok]);
  if (!hasil || hasil.kunci !== kunci) return { data: null, galat: null };
  return { data: hasil.data, galat: hasil.galat };
}

export function useDataB(berkas: Berkas, key: string) {
  return useBertembolok(berkas.b, key, () => ambil<DataB>("bahasa", { key }));
}

/** Deskripsi hanya untuk bintang yang BUKAN terkunci: yang terkunci pasti
 *  ditolak server (403), jadi tidak pernah ditanyakan. */
export function useDataM(berkas: Berkas, key: string, i: number | null, terkunci: boolean) {
  const kunci = i === null || terkunci ? null : `${key}/${i}`;
  return useBertembolok(berkas.m, kunci, () => ambil<DataM>("materi", { key, indeks: i as number }));
}

/* ------------------------------------------------------------- panel rasi */

export function PanelRasi({
  b, dataB, berikut, babSorot, onPilih, onSorotBab, keluarga,
}: {
  b: BahasaLangit;
  dataB: DataB | null;
  berikut: number | null;
  babSorot: number | null;
  onPilih: (i: number) => void;
  onSorotBab: (k: number | null) => void;
  keluarga: string;
}) {
  const selesai = b.materi.filter((m) => m.status === "selesai").length;
  const frak = b.materi.length ? (100 * selesai) / b.materi.length : 0;
  const babList = b.bab ?? [];
  return (
    <div className="lt-panel-isi">
      <div className="lt-panel-kepala">
        <div>
          <span className="mata">{`Rasi · ${keluarga}`}</span>
          <h3>{b.label}</h3>
        </div>
      </div>
      <p className="lt-panel-ringkas">
        {`${selesai} dari ${b.materi.length} materi sudah dibaca, dalam ${babList.length} bab.`}
      </p>
      <div className="lt-bilah" role="img" aria-label={`${Math.round(frak)} persen materi dibaca`}>
        <i style={{ width: `${frak.toFixed(1)}%` }} />
      </div>

      {berikut !== null ? (
        <div className="lt-panel-blok">
          <h4>Berikutnya</h4>
          <button type="button" className="lt-berikut" onClick={() => onPilih(berikut)}>
            <Glif status={statusBintang(b.materi[berikut] as BahasaLangit["materi"][number])} r={7} ukuran={24} />
            <span>{tanpaNomor((b.materi[berikut] as BahasaLangit["materi"][number]).judul)}</span>
          </button>
        </div>
      ) : null}

      {babList.length ? (
        <div className="lt-panel-blok">
          <h4>Bab</h4>
          <ol className="lt-bab-daftar">
            {babList.map((bb, k) => {
              const h = hitungBab(b.materi, bb.materi);
              const bB = dataB?.bab[k];
              const kunci = bb.materi.every((i) => b.materi[i]?.terkunci);
              return (
                <li key={bb.nomor}>
                  <button
                    type="button"
                    className={"lt-bab-baris" + (babSorot === k ? " lt-bab-sorot" : "")}
                    onClick={() => onPilih(bb.materi[0] as number)}
                    onPointerEnter={() => onSorotBab(k)}
                    onPointerLeave={() => onSorotBab(null)}
                    onFocus={() => onSorotBab(k)}
                    onBlur={() => onSorotBab(null)}
                    title={bB?.ket || undefined}
                  >
                    <span className="lt-bab-nomor">{romawi(bb.nomor)}</span>
                    <span className="lt-bab-judul">{bb.judul}</span>
                    <span className="lt-bab-hitung">
                      {kunci ? "terkunci" : `${h.selesai}/${h.jumlah}`}
                    </span>
                  </button>
                </li>
              );
            })}
          </ol>
        </div>
      ) : null}

      <div className="lt-panel-aksi">
        <a className="tbl tbl-kecil tbl-hantu" href={`#/bahasa/${b.key}`}>
          Buka kurikulum
        </a>
      </div>
    </div>
  );
}

/* ----------------------------------------------------------- panel bintang */

export function PanelBintang({
  b, i, dataB, deskripsi, galatDeskripsi, memuatDeskripsi, profesi, berikut,
  onPilih, onKosong,
}: {
  b: BahasaLangit;
  i: number;
  dataB: DataB | null;
  deskripsi: DataM | null;
  galatDeskripsi: string | null;
  memuatDeskripsi: boolean;
  profesi: Profesi[];
  berikut: number | null;
  onPilih: (i: number) => void;
  onKosong: () => void;
}) {
  const m = b.materi[i] as BahasaLangit["materi"][number];
  const status = statusBintang(m);
  const nomorBab = (b.bab ?? []).findIndex((x) => x.materi.includes(i));
  const bab = nomorBab >= 0 ? (b.bab as NonNullable<BahasaLangit["bab"]>)[nomorBab] : undefined;
  const babB = nomorBab >= 0 ? dataB?.bab[nomorBab] : undefined;
  const materiB = dataB?.materi[i];
  const h = bab ? hitungBab(b.materi, bab.materi) : null;
  const ringkas = status === "terkunci" ? null : ringkasPembuka(deskripsi?.bagian);
  const aksi = kataAksiBaca(status);
  const dipakai = profesi.filter((p) => p.bekal.some((g) => g.includes(b.key)));

  return (
    <div className="lt-panel-isi">
      <div className="lt-panel-kepala">
        <Glif status={status} r={10} ukuran={36} />
        <div>
          <span className="mata">{`Materi ${i + 1} dari ${b.materi.length} · ${b.label}`}</span>
          <h3>{tanpaNomor(m.judul)}</h3>
        </div>
        <button type="button" className="ikon-tombol lt-tutup" aria-label="Tutup detail bintang" onClick={onKosong}>
          <span aria-hidden="true">×</span>
        </button>
      </div>

      <ul className="lt-panel-meta">
        <li className={PIL_STATUS[status]}>{KATA_STATUS_BINTANG[status]}</li>
        {babB ? <li className="pil pil-tenang">{babB.label_tingkat || babB.tingkat}</li> : null}
        {materiB ? <li className="pil">{`± ${materiB.menit} menit`}</li> : null}
        {materiB ? <li className="pil">{`${materiB.bagian} bagian`}</li> : null}
      </ul>

      {status === "terkunci" ? (
        <div className="lt-kunci">
          <p>{babB?.alasan ?? "Materi ini masih terkunci."}</p>
        </div>
      ) : null}
      <div className="lt-panel-aksi">
        {aksi ? (
          <a className="tbl tbl-utama" href={`#/materi/${b.key}/${i}`}>
            {aksi}
            <Ikon nama="lanjut" ukuran={16} />
          </a>
        ) : berikut !== null ? (
          <button type="button" className="tbl tbl-utama" onClick={() => onPilih(berikut)}>
            Ke bintang yang bisa dibuka
            <Ikon nama="lanjut" ukuran={16} />
          </button>
        ) : null}
        <a className="tbl tbl-kecil tbl-hantu" href={`#/bahasa/${b.key}`}>
          Buka kurikulum
        </a>
      </div>

      {/* `ringkas` null (materi tanpa paragraf pembuka): yang tampil keterangan
          bab, atau tidak ada paragraf sama sekali. */}
      {status !== "terkunci" && (ringkas || memuatDeskripsi || galatDeskripsi || babB?.ket) ? (
        <p className="lt-panel-ringkas">
          {ringkas
            ? pecahKode(ringkas).map((x, k) => (x.kode ? <code key={k}>{x.teks}</code> : <span key={k}>{x.teks}</span>))
            : memuatDeskripsi
              ? "Memuat paragraf pembuka…"
              : galatDeskripsi
                ? "Paragraf pembuka tidak bisa dimuat."
                : babB?.ket}
        </p>
      ) : null}
      {status === "terkunci" && babB?.ket ? (
        <p className="lt-panel-ringkas lt-panel-redup">{babB.ket}</p>
      ) : null}

      {bab && h ? (
        <div className="lt-panel-blok">
          <h4>{`Bab ${romawi(bab.nomor)} · ${bab.judul}`}</h4>
          <div className="lt-bilah" role="img" aria-label={`${h.selesai} dari ${h.jumlah} materi bab ini sudah dibaca`}>
            <i style={{ width: `${h.persen}%` }} />
          </div>
          <p className="lt-panel-kecil">{`${h.selesai} dari ${h.jumlah} materi sudah dibaca`}</p>
        </div>
      ) : null}

      <div className="lt-panel-nav">
        <button
          type="button"
          className="tbl tbl-kecil tbl-hantu"
          aria-disabled={i === 0 ? true : undefined}
          onClick={() => {
            if (i > 0) onPilih(i - 1);
          }}
        >
          <Ikon nama="kembali" ukuran={14} />
          Sebelumnya
        </button>
        <button
          type="button"
          className="tbl tbl-kecil tbl-hantu"
          aria-disabled={i === b.materi.length - 1 ? true : undefined}
          onClick={() => {
            if (i < b.materi.length - 1) onPilih(i + 1);
          }}
        >
          Sesudahnya
          <Ikon nama="lanjut" ukuran={14} />
        </button>
      </div>

      {dipakai.length ? (
        <div className="lt-panel-blok">
          <h4>Dipakai di profesi</h4>
          <ul className="lt-panel-tautan">
            {dipakai.slice(0, MAKS_PROFESI).map((p) => (
              <li key={p.id}>
                <a href={`#/karier/${p.id}`}>{p.nama}</a>
              </li>
            ))}
            {dipakai.length > MAKS_PROFESI ? (
              <li>
                <a href="#/karier">{`dan ${dipakai.length - MAKS_PROFESI} lainnya, di Peta Karier`}</a>
              </li>
            ) : null}
          </ul>
        </div>
      ) : null}
    </div>
  );
}
