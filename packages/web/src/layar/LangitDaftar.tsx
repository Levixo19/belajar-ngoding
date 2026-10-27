/* Ikhtisar di layar sempit: daftar rasi per keluarga, bukan peta.
 *
 * Peta 1.400 satuan yang diciutkan ke 360 px bukan "peta kecil", ia peta yang
 * tidak bisa dibaca: nama rasi 5 px dan jarak tetangga median 1,7 px. Karena
 * ikhtisar sekarang cuma menjawab "kurikulum mana, dan sudah sejauh apa",
 * jawabannya muat sebagai daftar: nama, angka kemajuan, dan sketsa rasi
 * (bentuk yang SAMA dengan di peta, 52 x 36 px) sebagai pengenal. Menekan
 * satu baris membuka lensa yang lebar penuh.
 *
 * Datanya persis datanya peta; tidak ada informasi yang hanya muncul di salah
 * satunya.
 */

import { useMemo } from "react";

import {
  bagianGlif,
  type BahasaLangit,
  statusBintang,
  URUTAN_STATUS,
} from "../komponen/lensa-geometri.ts";
import { KELAS_GLIF } from "../komponen/Glif.tsx";
import { kataMulai, labelRasi } from "../komponen/lensa-teks.ts";
import { tanpaNomor } from "../util.tsx";
import { bentukRasi, type Titik } from "../komponen/rasi-geometri.ts";
import { KELUARGA, TATA, URUTAN_KELUARGA, type Saran } from "./langit-data.ts";

const W = 56;
const H = 40;
const JARI: Record<string, number> = { selesai: 3.1, sebagian: 2.6, baru: 2.4, terkunci: 1.2 };

function Sketsa({ b }: { b: BahasaLangit }) {
  const d = useMemo(() => {
    const t = bentukRasi(b.materi.length, "langit·" + b.key, W - 10, H - 10);
    const per: Record<string, { isi: string[]; tepi: string[] }> = {};
    b.materi.forEach((m, i) => {
      const p = t[i] as Titik;
      const st = statusBintang(m);
      const bg = bagianGlif(st, W / 2 + p[0], H / 2 + p[1], JARI[st] as number);
      const g = (per[st] ??= { isi: [], tepi: [] });
      if (bg.isi) g.isi.push(bg.isi);
      if (bg.tepi) g.tepi.push(bg.tepi);
    });
    return per;
  }, [b]);
  return (
    <svg className="lt-sketsa" width={W} height={H} viewBox={`0 0 ${W} ${H}`} aria-hidden="true" focusable="false">
      {URUTAN_STATUS.map((st) => {
        const g = d[st];
        if (!g) return null;
        return [
          g.isi.length ? <path key={st + "i"} className={`${KELAS_GLIF[st]} lt-gl-isi`} d={g.isi.join("")} /> : null,
          g.tepi.length ? <path key={st + "t"} className={`${KELAS_GLIF[st]} lt-gl-tepi`} d={g.tepi.join("")} /> : null,
        ];
      })}
    </svg>
  );
}

export function Daftar({
  bahasa, bekal, adaProfesi, profesiNama, konsepNama, cocokPer, saran, onBuka,
}: {
  bahasa: BahasaLangit[];
  bekal: ReadonlySet<string>;
  adaProfesi: boolean;
  profesiNama: string | null;
  konsepNama: string | null;
  cocokPer: Readonly<Record<string, number>>;
  /** Penanda "mulai di sini" yang SAMA dengan di peta (langkah materi pertama
   *  kartu utama Dasbor). Daftar dipakai pada zum 125 persen ke atas dan
   *  jendela setengah layar, jadi pelajar baru di sana tidak boleh kehilangan
   *  jawaban atas "mulai dari mana". */
  saran: Saran | null;
  onBuka: (key: string, indeks: number | null) => void;
}) {
  const bSaran = saran ? bahasa.find((x) => x.key === saran.bahasa) : undefined;
  const mSaran = bSaran && saran ? bSaran.materi[saran.indeks] : undefined;
  const tampilSaran = !!(saran && bSaran && mSaran && !mSaran.terkunci);
  return (
    <div className="lt-daftar">
      {tampilSaran && saran && bSaran && mSaran ? (
        <a
          className="lt-mulai lt-mulai-daftar"
          href={`#/langit/${saran.bahasa}/${saran.indeks}`}
          title={saran.alasan}
          onClick={(e) => {
            if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
            e.preventDefault();
            onBuka(saran.bahasa, saran.indeks);
          }}
        >
          {`${kataMulai(statusBintang(mSaran))}: ${tanpaNomor(mSaran.judul)} (${bSaran.label})`}
        </a>
      ) : null}
      {URUTAN_KELUARGA.map((kel) => {
        const isi = bahasa.filter((b) => (TATA[b.key]?.[2] ?? "tech") === kel);
        if (!isi.length) return null;
        const nama = KELUARGA[kel]?.[0] ?? kel;
        return (
          <section key={kel} aria-label={nama}>
            <h2 className="lt-daftar-keluarga">{nama}</h2>
            <ul>
              {isi.map((b) => {
                const selesai = b.materi.filter((m) => m.status === "selesai").length;
                const frak = b.materi.length ? (100 * selesai) / b.materi.length : 0;
                const diBekal = adaProfesi && bekal.has(b.key);
                const cocok = cocokPer[b.key] ?? 0;
                return (
                  <li key={b.key}>
                    <a
                      className="lt-daftar-baris"
                      href={`#/langit/${b.key}`}
                      data-key={b.key}
                      data-bekal={diBekal ? "ya" : undefined}
                      aria-label={labelRasi({
                        label: b.label,
                        selesai,
                        jumlah: b.materi.length,
                        konsep: konsepNama,
                        cocok,
                        profesi: profesiNama,
                        bekal: diBekal,
                      })}
                      onClick={(e) => {
                        if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
                        e.preventDefault();
                        onBuka(b.key, null);
                      }}
                    >
                      <Sketsa b={b} />
                      <span className="lt-daftar-nama">{b.label}</span>
                      <span className="lt-nama-prog">
                        <span className="lt-nama-jalur">
                          <i style={{ width: `${frak.toFixed(1)}%` }} />
                        </span>
                        <b>{`${selesai}/${b.materi.length}`}</b>
                        {konsepNama && cocok > 0 ? <span className="lt-daftar-cocok">{`${cocok} cocok`}</span> : null}
                      </span>
                    </a>
                  </li>
                );
              })}
            </ul>
          </section>
        );
      })}
    </div>
  );
}
