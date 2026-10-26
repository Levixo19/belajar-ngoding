/* Layar Statistik. Port bagian `layarStatistik` dari `layar-lain.js`.
 *
 * Satu aturan yang paling mudah dilanggar saat memport layar ini, dan
 * komentarnya di versi JS panjang justru karena itu: **ruas di dalam batang
 * dibagi dengan JUMLAH KETIGA PEMBILANGNYA SENDIRI**, bukan dengan
 * `total_materi`/`total_kuis`/`total_latihan`. Membaginya dengan `total_*`
 * berarti sisi web mulai menghitung sendiri "berapa yang selesai", padahal
 * `pelajar/progress.py` sudah menjawabnya -- dan `min(selesai, target)` di
 * sana membuat kedua angka itu berpisah diam-diam begitu pembilangnya
 * melewati targetnya. Satu angka, satu tempat; kembaran dari "jangan pernah
 * menulis definisi lulus yang kedua".
 *
 * Panjang BATANGNYA sendiri tetap milik server (`b.persen`) dan tidak disentuh
 * di sini sama sekali.
 */

import { useEffect, useRef, useState } from "react";

import { ambil } from "../api.ts";
import { adaGerak } from "../gerak.ts";
import { Bilah } from "../komponen/Bilah.tsx";
import { BlokData } from "../komponen/BlokData.tsx";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { salin } from "../sorak.tsx";
import { angka } from "../util.tsx";
import { tanggalRamah } from "../waktu.ts";

interface BahasaStat {
  key: string;
  label: string;
  persen: number;
  materi: number;
  total_materi: number;
  kuis: number;
  total_kuis: number;
  latihan_lulus: number;
  latihan_manual: number;
  total_latihan: number;
  skor?: number;
  skor_maks?: number;
}

interface Badge {
  nama: string;
  deskripsi: string;
  punya: boolean;
}

interface Toolchain {
  label: string;
  siap: boolean;
  hilang: string[];
  pasang?: string;
}

interface Gelar {
  level: number;
  nama: string;
}

/* Bentuknya dari `saran.kuis_perlu_diulang` lewat `/api/statistik`.
 *
 * Versi pertama tipe ini menyebut `key`, `skor`, dan `maks` -- tiga nama yang
 * TIDAK ADA satu pun di muatannya. `tsc` tidak bisa menangkapnya (tipe yang
 * salah tetap tipe yang sah), dan yang digambar di layar: pil bertuliskan
 * `undefined/undefined`, tautan ke `#/kuis/undefined`, dan kunci kurikulum
 * mentah ("python") di tempat labelnya ("Python"). Nol galat di konsol.
 *
 * `riwayat` triplet `[tanggal, benar, total]`, dan ia dipakai apa adanya
 * untuk menggambar jejak "3/8 → 6/8". */
interface KuisLemah {
  bahasa: string;
  label_bahasa: string;
  indeks: number;
  judul: string;
  terbaik: number;
  total: number;
  salah_tersisa: number;
  jadwal: string | null;
  riwayat: Array<[string, number, number]>;
}

interface Statistik {
  xp: number;
  xp_hari_ini: number;
  xp_kemarin: number;
  level: number;
  gelar: string;
  di_level: number;
  butuh_level: number;
  streak: number;
  streak_rekor: number;
  streak_total: number;
  hari_belajar_terakhir?: string;
  bahasa: BahasaStat[];
  semua_badge: Badge[];
  toolchain: Toolchain[];
  tangga_gelar?: Gelar[];
  kuis_lemah?: KuisLemah[];
  skor_kuis: { benar: number; maks: number };
  xp_tarif: {
    materi: number;
    latihan_dilihat: number;
    latihan_lulus: number;
    latihan_manual: number;
    per_jawaban_benar: number;
    bonus_kuis_sempurna: number;
  };
}

/**
 * Angka besar yang BERJALAN naik dari nol saat kartunya tergulir ke layar.
 *
 * Pengamatnya sekali pakai dan langsung dicabut. Pengamat yang tertinggal
 * hidup sesudah layarnya diganti akan menembak ke elemen yang sudah tidak ada
 * -- dan di layar ini ada tiga sekaligus.
 */
function AngkaBesar({
  nilai,
  label,
  ket,
  mentah,
}: {
  nilai: string;
  label: string;
  ket?: string;
  /** Kalau diisi, angkanya dihitung naik dari nol sampai ke situ. */
  mentah?: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [tampil, setTampil] = useState(mentah === undefined ? nilai : "0");

  useEffect(() => {
    if (mentah === undefined || !adaGerak()) {
      setTampil(nilai);
      return;
    }
    const el = ref.current;
    if (!el) return;
    let henti: number | null = null;
    const jalan = () => {
      const mulai = performance.now();
      const langkah = (t: number) => {
        const maju = Math.min(1, (t - mulai) / 900);
        // Kurva sama dengan `angkaKe` di gerak.js: cepat di awal, melambat di
        // ujung, supaya angka akhirnya terbaca bukan terlewat.
        const halus = 1 - Math.pow(1 - maju, 3);
        setTampil(angka(Math.round(mentah * halus)));
        if (maju < 1) henti = requestAnimationFrame(langkah);
      };
      henti = requestAnimationFrame(langkah);
    };

    if (typeof IntersectionObserver === "undefined") {
      jalan();
      return;
    }
    const o = new IntersectionObserver(
      (c) => {
        if (c.some((x) => x.isIntersecting)) {
          o.disconnect();
          jalan();
        }
      },
      { threshold: 0.3 },
    );
    o.observe(el);
    return () => {
      o.disconnect();
      if (henti !== null) cancelAnimationFrame(henti);
    };
  }, [mentah, nilai]);

  return (
    <div ref={ref} className="kartu kartu-rapat kartu-angka">
      <div className="angka-besar">{tampil}</div>
      <div className="mata">{label}</div>
      {ket ? <div className="ket">{ket}</div> : null}
    </div>
  );
}

/** Tiga ruas DI DALAM bagian batang yang sudah terisi.
 *
 *  Kalau ketiga pembilangnya nol, tidak ada satu ruas pun dipasang. Batang
 *  kosong memang keadaan yang benar untuk bahasa yang belum disentuh, dan tiga
 *  ruas selebar nol cuma menambah simpul yang tidak menjelaskan apa-apa. */
function RuasTumpuk({
  ruas,
}: {
  ruas: Array<{ kelas: string; nama: string; nilai: number }>;
}) {
  const jumlah = ruas.reduce((a, r) => a + r.nilai, 0);
  if (jumlah <= 0) return null;
  return (
    <div className="ruas-tumpuk">
      {ruas.map((r) => (
        <div
          key={r.kelas}
          className={"ruas " + r.kelas}
          title={`${r.nama}: ${r.nilai}`}
          // Keadaan diamnya ditulis sebagai gaya inline: pada gerak yang
          // dimatikan, yang tertinggal tetap lebar yang benar.
          style={{ width: (r.nilai / jumlah) * 100 + "%" }}
        />
      ))}
    </div>
  );
}

export function Statistik() {
  const [s, setS] = useState<Statistik | null>(null);
  const [galat, setGalat] = useState<string | null>(null);

  useEffect(() => {
    let dibatalkan = false;
    ambil<Statistik>("statistik")
      .then((d) => {
        if (!dibatalkan) setS(d);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, []);

  if (galat) {
    return <Keadaan jenis="salah" judul="Gagal memuat statistik" ket={galat} />;
  }
  if (!s) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat statistik…</span>
      </div>
    );
  }

  const punya = s.semua_badge.filter((b) => b.punya);
  const belum = s.semua_badge.filter((b) => !b.punya);
  const jml = (f: keyof BahasaStat) =>
    s.bahasa.reduce((a, b) => a + (Number(b[f]) || 0), 0);
  const t = s.xp_tarif;

  return (
    <div className="masuk-urut">
      <header className="kepala">
        <span className="mata">Sejauh ini</span>
        <h1>Statistik</h1>
        <p className="kepala-sub">
          {s.hari_belajar_terakhir
            ? `${s.streak_total} hari belajar, terakhir ${tanggalRamah(s.hari_belajar_terakhir)}.`
            : "Belum ada hari belajar yang tercatat."}
        </p>
      </header>

      <div className="petak petak-3">
        <AngkaBesar
          nilai={angka(s.xp)}
          label="XP total"
          ket={`${angka(s.xp_hari_ini)} hari ini, ${angka(s.xp_kemarin)} kemarin`}
          mentah={s.xp}
        />
        <AngkaBesar
          nilai={String(s.level)}
          label={s.gelar}
          ket={`${angka(s.di_level)} dari ${angka(s.butuh_level)} XP ke gelar berikutnya`}
          mentah={s.level}
        />
        <AngkaBesar
          nilai={String(s.streak)}
          label="hari beruntun"
          ket={`rekor ${s.streak_rekor} hari`}
          mentah={s.streak}
        />
      </div>

      <section>
        <span className="mata">Rincian per bahasa</span>
        <div className="kartu">
          <div className="rinci">
            {s.bahasa.map((b) => (
              <div key={b.key} className="rinci-baris">
                <div className="rinci-atas">
                  <a href={`#/bahasa/${b.key}`}>{b.label}</a>
                  <span className="rinci-angka">
                    {`${b.materi}/${b.total_materi} materi · ` +
                      `${b.kuis}/${b.total_kuis} kuis · ` +
                      `${b.latihan_lulus + b.latihan_manual}/${b.total_latihan} latihan` +
                      (b.skor_maks ? ` · skor ${b.skor}/${b.skor_maks}` : "")}
                  </span>
                </div>
                <Bilah
                  persen={b.persen}
                  kelas={b.persen >= 100 ? "tumbuh" : undefined}
                  label={`${b.label}: ${Math.round(b.persen)}% selesai`}
                />
                <RuasTumpuk
                  ruas={[
                    { kelas: "ruas-materi", nama: "materi dibaca", nilai: b.materi },
                    { kelas: "ruas-kuis", nama: "kuis lulus", nilai: b.kuis },
                    {
                      kelas: "ruas-latihan",
                      nama: "latihan selesai",
                      nilai: b.latihan_lulus + b.latihan_manual,
                    },
                  ]}
                />
              </div>
            ))}
            <div className="rinci-total">
              {`Total: ${jml("materi")} dari ${jml("total_materi")} materi dibaca, ` +
                `${jml("latihan_lulus")} latihan lulus dengan kode sendiri, dan ` +
                (s.skor_kuis.maks
                  ? `${s.skor_kuis.benar} dari ${s.skor_kuis.maks} soal kuis benar.`
                  : "belum ada kuis yang dikerjakan.")}
            </div>
          </div>
        </div>
      </section>

      {/* "Paling perlu diulang", label yang SAMA dengan antarmuka lama.
          Versi pertama memakai "Di mana aku lemah?" -- itu nama fiturnya di
          docstring `blokKuisLemah`, bukan teks yang digambar, dan dua
          antarmuka yang menamai satu bagian dengan dua kalimat adalah dua
          antarmuka yang isinya berbeda.

          Urutan dan isinya dari server (`saran.kuis_perlu_diulang`); bilahnya
          skor TERBAIK dengan garis dasar nol, dan riwayat ditulis sebagai
          angka ("3/8 → 6/8") bukan grafik -- paling banyak dua belas titik per
          kuis, dan yang ingin dilihat cuma arahnya. */}
      {s.kuis_lemah && s.kuis_lemah.length ? (
        <section>
          <span className="mata">Paling perlu diulang</span>
          <div className="senarai">
            {s.kuis_lemah.map((k) => {
              const persen = k.total ? (k.terbaik / k.total) * 100 : 0;
              const jejak = k.riwayat
                .slice(-4)
                .map((r) => `${r[1]}/${r[2]}`)
                .join(" → ");
              const ket = [
                k.label_bahasa,
                k.salah_tersisa ? `${k.salah_tersisa} soal masih salah` : null,
                k.jadwal ? `ulang ${tanggalRamah(k.jadwal)}` : null,
                k.riwayat.length > 1 ? `riwayat ${jejak}` : null,
              ]
                .filter(Boolean)
                .join(" · ");
              return (
                <a
                  key={`${k.bahasa}-${k.indeks}`}
                  className="baris"
                  href={`#/kuis/${k.bahasa}/${k.indeks}`}
                >
                  <div className="isi">
                    <div className="judul">{k.judul}</div>
                    <div className="ket">{ket}</div>
                  </div>
                  <span className="kuis-lemah-angka">
                    {`terbaik ${k.terbaik}/${k.total}`}
                  </span>
                  <span className="kuis-lemah-bilah">
                    <Bilah persen={persen} kelas={persen >= 70 ? "tumbuh" : ""} />
                  </span>
                </a>
              );
            })}
          </div>
        </section>
      ) : null}

      <section>
        <span className="mata">Tangga gelar</span>
        <div className="kartu deret deret-rapat">
          {(s.tangga_gelar ?? []).map((g) => (
            <span
              key={g.level}
              className={"pil" + (s.level >= g.level ? " pil-nyala" : "")}
            >
              {`Lv ${g.level} · ${g.nama}`}
            </span>
          ))}
        </div>
      </section>

      <section>
        <span className="mata">{`Badge, ${punya.length} dari ${s.semua_badge.length}`}</span>
        {/* Yang sudah didapat lebih dulu, yang terkunci di belakangnya. Urutan
            itu penting: yang dilihat lebih dulu adalah yang sudah dikerjakan,
            bukan daftar panjang yang belum. */}
        <div className="petak petak-2">
          {[...punya, ...belum].map((b) => (
            <div
              key={b.nama}
              className={"medali " + (b.punya ? "punya" : "terkunci")}
            >
              <div className="cap">{b.punya ? "★" : "·"}</div>
              <div>
                <b>{b.nama}</b>
                <span>{b.deskripsi}</span>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section>
        <span className="mata">Ketersediaan toolchain</span>
        <div className="kartu">
          <div className="rinci">
            {s.toolchain.map((tc) => (
              <div key={tc.label} className="alat-baris">
                <span className={"titik " + (tc.siap ? "selesai" : "gagal")} />
                <b>{tc.label}</b>
                {tc.siap ? (
                  <span style={{ color: "var(--tumbuh)" }}>siap dipakai</span>
                ) : (
                  <span className="baris-sisi">{`butuh ${tc.hilang.join(", ")}`}</span>
                )}
                {!tc.siap && tc.pasang ? <code>{tc.pasang}</code> : null}
                {!tc.siap && tc.pasang ? (
                  <button
                    type="button"
                    className="tbl tbl-kecil tbl-hantu"
                    onClick={() => salin(tc.pasang as string, "Perintah disalin.")}
                  >
                    Salin
                  </button>
                ) : null}
              </div>
            ))}
          </div>
          <p className="baris-sisi" style={{ margin: "var(--s4) 0 0" }}>
            Toolchain itu opsional. Materi dan kuis berjalan penuh tanpa satu pun
            compiler; yang mati hanya penilaian otomatis untuk bahasa itu.
          </p>
        </div>
      </section>

      <section>
        <span className="mata">Dari mana XP datang</span>
        <div className="kartu deret deret-rapat">
          <span className="pil">{`Materi tuntas +${t.materi}`}</span>
          <span className="pil">{`Latihan dibuka +${t.latihan_dilihat}`}</span>
          <span className="pil pil-nyala">{`Latihan lulus +${t.latihan_lulus}`}</span>
          <span className="pil">{`Latihan ditandai manual +${t.latihan_manual}`}</span>
          <span className="pil">{`Tiap jawaban kuis benar +${t.per_jawaban_benar}`}</span>
          <span className="pil pil-tumbuh">{`Kuis sempurna +${t.bonus_kuis_sempurna}`}</span>
        </div>
      </section>

      <BlokData />
    </div>
  );
}
