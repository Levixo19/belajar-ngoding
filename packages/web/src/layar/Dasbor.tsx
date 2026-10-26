/* Dasbor: meja kerja, bukan beranda. Port `layarDasbor` + `layarMulai` dan
 * sebelas pembantunya dari `webapp/statik/js/layar-belajar.js`.
 *
 * Yang murni tinggal di `dasbor-teks.ts` dan sudah diadu dengan JS yang masih
 * melayani aplikasi lama (`uji/banding-dasbor.mjs`). Yang di berkas ini bentuk
 * elemennya dan tiga hal yang memang harus mengukur DOM.
 *
 * **DUA keadaan, dan yang kedua bukan hiasan.** Profil dengan `xp === 0`
 * mendapat `LayarMulai`, bukan dasbor biasa yang kebetulan semua angkanya nol.
 * Dasbor biasa untuk profil baru berbunyi begini: hamparan 182 hari yang
 * seluruhnya dingin, tiga puluh dua kartu bahasa yang semuanya "0% · 0/44
 * materi", "streak terputus", dan "1/22 badge" -- katalog kegagalan yang bahkan
 * belum sempat dilakukan, dan tidak satu pun darinya menjawab pertanyaan yang
 * sebenarnya dibawa orang itu, yaitu "aku mulai dari mana".
 *
 * Aturan yang mengikat kedua keadaan:
 *
 * * **Satu layar, satu tindakan utama.** `.lanjutkan` adalah SATU-SATUNYA
 *   permukaan yang memakai warna aksen sebagai LATAR. Menambah yang kedua
 *   tidak membuat dua hal penting -- ia membuat nol. Di layar mulai, aksen
 *   dipakai sebagai GARIS kartu dan isi TOMBOLNYA, bukan latarnya: yang
 *   ditawarkan di sana awal, bukan sambungan.
 * * **Antrean datang dari `saran.py`**, bukan dari tebakan di sini. "Habis ini
 *   ngapani" sudah punya satu tempat tinggal, dan membuat tempat kedua berarti
 *   dua jawaban berbeda untuk satu pertanyaan.
 * * **Aturan babnya dari `/api/awal -> aturan_bab`**, tidak ditulis ulang.
 * * **Tidak ada penomoran pada pilihan yang saling menggantikan.** Nomor di
 *   aplikasi ini berarti URUTAN -- nomor bab, nomor materi, nomor langkah --
 *   dan itulah seluruh gunanya sebagai arsitektur.
 *
 * Yang TIDAK diport: koreografi masuk (`ungkap`, `nyalakanBara`, `gerakBeranda`)
 * dan sampul SVG generatif, sama dengan layar lain. Yang DIPERTAHANKAN
 * invariannya: tinggi batang pekan, `stroke-dashoffset` cincin level, dan lebar
 * bilah semuanya ditulis sebagai keadaan ALAMI elemennya, jadi gerak yang
 * dimatikan tidak pernah berarti ada yang hilang.
 */

import { useEffect, useMemo, useRef, useState } from "react";

import { ambil } from "../api.ts";
import { tingkatGerak } from "../gerak.ts";
import { Bilah } from "../komponen/Bilah.tsx";
import { Ikon } from "../komponen/Ikon.tsx";
import { ikonTipe } from "../komponen/ikon-bentuk.ts";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { PetaRasi } from "../komponen/Rasi.tsx";
import type { DataPeta } from "../komponen/rasi-geometri.ts";
import { angka, tanpaNomor } from "../util.ts";
import { hariIniISO } from "../waktu.ts";
import type { Tingkat } from "./Bahasa.tsx";
import {
  bandingHarian, baraPetak, celahBelajar, cincinAngka, dijalaniDasbor,
  jedaBara, jumlahKurikulum, kalimatPembuka, labelLanjut, labelMulai,
  paketTigaPuluh, pecahSapa, pekanAngka, sapaJam, tandaUbin, tautanLangkah,
  type DataDasbor, type Langkah,
} from "./dasbor-teks.ts";

/** Entri `/api/awal -> bahasa`, medan yang dibaca layar ini. */
export interface BahasaAwal {
  key: string;
  label: string;
  siap: boolean;
  tematik?: boolean;
  hilang?: string[];
  pasang?: string;
  materi: number;
  kuis: number;
  latihan: number;
}

/* ------------------------------------------------------------- pembantu */

/** Pil bertanda jenis isi: ikon + kata.
 *
 *  Warnanya NETRAL untuk ketiga jenis. Dulu kuis, latihan, dan materi
 *  masing-masing punya warna sendiri, sehingga satu daftar memuat tiga warna
 *  untuk informasi yang sudah dibawa ikon dan katanya -- dan warna aksen
 *  (latihan) ikut tenggelam di antara dua warna lain yang sama kerasnya. */
export function PilJenis({ tipe }: { tipe: string }) {
  return (
    <span className="pil pil-jenis">
      <Ikon nama={ikonTipe(tipe)} ukuran={14} tebal={1.9} />
      {tipe}
    </span>
  );
}

/**
 * Cincin level. `stroke-dashoffset` AKHIR dipasang langsung di atributnya;
 * animasinya cuma berangkat dari lingkaran kosong.
 *
 * `--panas` diteruskan sebagai properti kustom, dan itu harus lewat gaya inline
 * React (bukan `Object.assign` ke `style` seperti versi JS, yang diam-diam
 * membuang properti `--*`).
 */
function CincinLevel({ d }: { d: DataDasbor }) {
  const R = 56;
  const keliling = 2 * Math.PI * R;
  const { rasio, panas } = cincinAngka(d);
  const akhir = keliling * (1 - rasio);
  const isiRef = useRef<SVGCircleElement>(null);

  useEffect(() => {
    const isi = isiRef.current;
    if (!isi || tingkatGerak() === "mati") return;
    isi.animate(
      { strokeDashoffset: [String(keliling), String(akhir)] },
      { duration: 900, easing: "cubic-bezier(.32,.72,.36,1)" },
    );
  }, [keliling, akhir]);

  return (
    <div
      className="cincin"
      style={{ "--panas": String(panas) } as React.CSSProperties}
      title={`${d.di_level} dari ${d.butuh_level} XP menuju level ${d.level + 1}`}
    >
      <svg viewBox="0 0 132 132" aria-hidden="true">
        <circle cx="66" cy="66" r={R} fill="none" strokeWidth="7" className="alur" />
        <circle
          ref={isiRef}
          cx="66"
          cy="66"
          r={R}
          fill="none"
          strokeWidth="7"
          className="isi"
          strokeDasharray={keliling}
          strokeDashoffset={akhir}
        />
      </svg>
      <div className="cincin-isi">
        <div className="cincin-angka">{d.level}</div>
        <div className="cincin-label">level</div>
      </div>
    </div>
  );
}

function KartuBara({ d }: { d: DataDasbor }) {
  const kurang = Math.max(0, d.target_harian - d.xp_hari_ini);
  const banding = bandingHarian(d);
  const celah = d.streak ? null : celahBelajar(d);
  return (
    <div className="kartu kartu-level">
      <CincinLevel d={d} />
      <div className="kartu-level-isi">
        <h2>{d.gelar}</h2>
        <div className="kartu-level-ket">
          {`${angka(d.xp)} XP · ${d.di_level}/${d.butuh_level} menuju level ${d.level + 1}`}
        </div>
        <Bilah persen={(d.di_level / Math.max(1, d.butuh_level)) * 100} />

        <div className="target">
          <div className="target-baris">
            <span>Target hari ini</span>
            <b className={kurang ? undefined : "tercapai"}>
              {kurang ? `${d.xp_hari_ini}/${d.target_harian} XP` : "tercapai"}
            </b>
          </div>
          <Bilah
            persen={(d.xp_hari_ini / Math.max(1, d.target_harian)) * 100}
            kelas={kurang ? "" : "tumbuh"}
          />
        </div>

        <div className="banding">
          {banding.teks}
          {banding.arah ? <span className="banding-arah">{banding.arah}</span> : null}
        </div>

        {celah ? (
          <div className="celah">
            <span>Hari belajar terakhir: </span>
            <b>{celah.tanggal}</b>
            <span className="celah-jarak">{` · ${angka(celah.selisih)} hari lalu`}</span>
          </div>
        ) : null}

        <div className="deret deret-rapat">
          <span className={"pil" + (d.streak ? " pil-nyala" : "")}>
            <Ikon nama="api" ukuran={14} tebal={1.9} />
            {d.streak ? `${d.streak} hari belajar` : "belum ada hari berurutan"}
          </span>
          <a
            className={"pil" + (d.badge_dimiliki ? " pil-ungu" : "")}
            href="#/statistik"
          >
            <Ikon nama="bintang" ukuran={14} tebal={1.9} />
            {`${d.badge_dimiliki}/${d.badge_total}`}
          </a>
        </div>
      </div>
    </div>
  );
}

/**
 * Minggu ini: tujuh hari terakhir sebagai tujuh batang, hari ini di ujung.
 *
 * Hamparan enam bulan menjawab "seperti apa ritmeku"; strip ini menjawab
 * pertanyaan yang lebih dekat -- "minggu ini aku ke mana saja" -- tanpa harus
 * mencari tujuh sel kecil di ujung kanan sebuah kisi.
 *
 * `--target` dipasang lewat gaya inline React, dan itu AMAN di sini: versi JS
 * harus memakai `setProperty` karena `h()` menyalin gayanya dengan
 * `Object.assign`, yang membuang properti kustom. React menulis properti `--*`
 * apa adanya.
 */
function PekanIni({ d }: { d: DataDasbor }) {
  const p = pekanAngka(d);
  if (!p) return null;
  return (
    <section className="pekan" aria-label="Tujuh hari terakhir">
      <div className="bagian-kepala">
        <span className="mata">Minggu ini</span>
        <span className="baris-sisi">
          {`${angka(p.total)} XP dalam ${p.aktif} dari 7 hari`}
        </span>
      </div>
      <div
        className="pekan-petak"
        style={{ "--target": p.target + "%" } as React.CSSProperties}
      >
        {p.hari.map((x) => (
          <div
            key={x.tanggal}
            className={
              "pekan-hari" + (x.kini ? " kini" : "") + (x.capai ? " capai" : "")
            }
            title={x.judul}
          >
            <span className="pekan-xp">{x.xpTeks}</span>
            <span className="pekan-batang">
              {/* Tinggi akhir di gaya inline -- keadaan alaminya. Tidak
                  dianimasikan dari nol: tujuh batang yang tumbuh bersamaan
                  tidak menjawab satu pertanyaan pun. */}
              <i style={{ height: x.tinggi + "%" }} />
            </span>
            <span className="pekan-nama">{x.nama}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

/* Batas waktu pengamat ukuran kisi bara. Terukur di sisi JS: penyusutan kotak
   yang menyebabkan pin pertama salah terjadi dalam satu-dua frame sesudah
   pemasangan, jadi empat detik kelonggaran besar -- dan ia ada supaya
   pengamatnya tidak hidup selamanya di layar yang dibuka lalu ditinggal. */
const PIN_BARA_MS = 4000;

/* Isyarat bahwa pengguna sudah mengambil alih gulirnya sendiri. `keydown`
   hanya bisa datang karena `.bara-petak` bisa difokus. */
const SENTUHAN_GULIR = ["wheel", "pointerdown", "keydown"] as const;

/**
 * Pin kisi pada HARI INI, dan LEPAS begitu penggunanya menyentuhnya.
 *
 * Terukur di sisi JS sebelum perbaikannya, profil 182 hari, empat jalur
 * pemuatan: `requestAnimationFrame` polos hanya menang pada pemuatan yang
 * beruntung, dan di 1100 px pemuatan pertama `clientWidth` petak menyusut
 * 299 -> 262 SESUDAH pemasangan -- jadi pin yang dihitung pada 299 mendarat di
 * `scrollLeft` 80 padahal ujung yang benar 117.
 *
 * Di React, `useEffect` sudah menjawab "terpasang dan punya ukuran". Yang TIDAK
 * dijawabnya "ukurannya sudah berhenti berubah", jadi pengamat ukurannya tetap
 * perlu -- dan ia WAJIB lepas: posisi gulir adalah keadaan PENGGUNA, dan
 * merebutnya kembali sesudah dia menggeser sendiri lebih buruk daripada tidak
 * mem-pin sama sekali.
 */
function usePinKeHariIni(
  petakRef: React.RefObject<HTMLDivElement | null>,
  geserRef: React.RefObject<HTMLSpanElement | null>,
  tanda: unknown,
) {
  useEffect(() => {
    const petak = petakRef.current;
    if (!petak) return;

    const pasang = () => {
      petak.scrollLeft = petak.scrollWidth;
      // Kondisi penandanya tinggal di dalam callback yang SAMA dengan pin-nya.
      // Dihitung di luar, ia menjawab pertanyaan tentang kotak yang belum ada
      // dan melaporkan "tidak ada yang tersembunyi" sementara lima bulan
      // berada di luar kotaknya.
      const geser = geserRef.current;
      if (geser) geser.hidden = petak.scrollWidth <= petak.clientWidth;
    };

    pasang();
    if (typeof ResizeObserver !== "function") return;

    // Bandingkan lebarnya sendiri sebelum memasang ulang: `pasang()` menyentuh
    // `geser.hidden`, dan pengamat yang bereaksi pada akibat tulisannya sendiri
    // adalah lingkaran pengamat-ukuran, bukan perbaikan.
    let lebarTerakhir = petak.clientWidth;
    let lepas = () => {};
    const pengamat = new ResizeObserver(() => {
      if (petak.clientWidth === lebarTerakhir) return;
      lebarTerakhir = petak.clientWidth;
      pasang();
    });
    const jam = setTimeout(() => lepas(), PIN_BARA_MS);

    lepas = () => {
      clearTimeout(jam);
      pengamat.disconnect();
      for (const nama of SENTUHAN_GULIR) petak.removeEventListener(nama, lepas);
    };
    for (const nama of SENTUHAN_GULIR) {
      petak.addEventListener(nama, lepas, { passive: true });
    }
    pengamat.observe(petak);
    return lepas;
  }, [petakRef, geserRef, tanda]);
}

function BlokBara({ d }: { d: DataDasbor }) {
  const petakRef = useRef<HTMLDivElement>(null);
  const geserRef = useRef<HTMLSpanElement>(null);
  const p = useMemo(() => baraPetak(d, hariIniISO()), [d]);
  const jeda = useMemo(() => jedaBara(d.heatmap), [d.heatmap]);
  usePinKeHariIni(petakRef, geserRef, p);

  return (
    <section>
      <span className="mata">Bara enam bulan terakhir</span>
      <div className="kartu kartu-rapat">
        {/* Kisi ini menggulir ke samping, jadi ia WAJIB bisa difokus: tanpa
            `tabIndex`, pengguna papan ketik tidak punya satu pun cara menggeser
            isinya -- dan sesudah pin di bawah, yang tidak terjangkau justru
            lima bulan pertamanya. */}
        <div
          ref={petakRef}
          className="bara-petak"
          tabIndex={0}
          role="group"
          aria-label="Hamparan XP harian enam bulan terakhir, bisa digeser ke samping"
        >
          {/* Sel kosong pembuka supaya kolom pertama jatuh di hari yang benar.
              Sel sungguhan berkelas, bukan div bergaya inline: ukurannya satu
              angka yang hidup di CSS bersama `.bara-sel` dan `.bara-petak`. */}
          {Array.from({ length: p.kosong }, (_v, i) => (
            <div key={"k" + i} className="bara-kosong" aria-hidden="true" />
          ))}
          {p.sel.map((s) => (
            <div
              key={s.tanggal}
              className={
                "bara-sel" +
                (s.tingkat ? " bara-" + s.tingkat : "") +
                (s.kini ? " bara-kini" : "")
              }
              title={s.judul}
            />
          ))}
        </div>

        {/* Jeda dirender DI BAWAH kisi, bukan di dalamnya, dan letaknya bukan
            selera: `.bara-petak` adalah `grid-auto-flow: column` dengan tujuh
            baris yang berarti Senin..Minggu, jadi satu sisipan teks di dalamnya
            menelan satu slot dan menggeser SELURUH kolom sesudahnya -- hari
            Rabu pindah ke baris Selasa, tanpa satu pun pesan galat. */}
        {jeda ? (
          <p className="bara-jeda">
            {`Jeda terpanjang ${angka(jeda.panjang)} hari tanpa XP, `}
            <span className="bara-jeda-kapan">{jeda.kapan}</span>
          </p>
        ) : null}

        <div className="bara-legenda">
          {/* "hari ber-XP", bukan "hari belajar". `riwayat_harian` cuma
              mencatat hari yang MENGHASILKAN XP; hari yang isinya bacaan
              setengah menaikkan streak tanpa meninggalkan entri apa pun di
              sini. Kalimat yang menyebut "belajar" akan berdiri di sebelah pil
              streak dan membantahnya. */}
          <span>{`${angka(p.aktif)} hari ber-XP`}</span>
          {/* Arahnya disebut, bukan cuma keberadaannya: sesudah kisinya dipin
              di ujung kanan, yang tersembunyi ada di KIRI. */}
          <span ref={geserRef} className="bara-geser" hidden>
            · geser ke kiri untuk yang lebih lama
          </span>
          {/* Rampa diberi kata di kedua ujungnya, bukan angka ambang:
              ambangnya dihitung dari target harian yang bisa diubah, jadi
              angka apa pun di sini akan jadi salinan kedua yang cepat basi. */}
          <div className="bara-rampa">
            <span>sedikit</span>
            <div className="bara-sel" />
            <div className="bara-sel bara-1" />
            <div className="bara-sel bara-2" />
            <div className="bara-sel bara-3" />
            <span>banyak XP</span>
          </div>
        </div>
      </div>
    </section>
  );
}

/** Kartu tindakan utama dasbor: satu-satunya permukaan beraksen di layar ini. */
function KartuLanjutkan({ s }: { s: Langkah }) {
  return (
    <a className="lanjutkan" href={tautanLangkah(s)}>
      <span className="lanjutkan-nomor">{s.indeks + 1}</span>
      <div className="lanjutkan-isi">
        <span className="mata">
          {`${labelLanjut(s.tipe)} · ${s.label_bahasa}` +
            (s.menit ? ` · ≈${s.menit} menit` : "")}
        </span>
        <h2>{tanpaNomor(s.judul)}</h2>
        <p>{s.alasan}</p>
      </div>
      <span className="lanjutkan-tbl">
        <span>Lanjutkan</span>
        <Ikon nama="lanjut" ukuran={20} />
      </span>
    </a>
  );
}

/**
 * Antrean hari ini: sisa langkah dari `saran.py` PLUS tantangan harian, jadi
 * SATU daftar.
 *
 * Sebelumnya keduanya dua blok terpisah dengan dua judul, dan tantangannya
 * bahkan punya kartunya sendiri lengkap dengan tombol -- padahal keduanya
 * menjawab pertanyaan yang sama persis ("apa lagi yang bisa kukerjakan
 * sekarang") dan disusun modul yang sama. Dua daftar untuk satu pertanyaan
 * memaksa orang membandingkan keduanya sebelum memilih.
 */
function BlokAntrean({
  langkah, tantangan, bahasa,
}: {
  langkah: Langkah[];
  tantangan?: Langkah | null;
  bahasa: BahasaAwal[];
}) {
  const siap = useMemo(
    () => new Map(bahasa.map((b) => [b.key, b.siap])),
    [bahasa],
  );
  const baris = (s: Langkah, cap: string | null, kunci: string) => (
    <a className="baris" key={kunci} href={tautanLangkah(s)}>
      <PilJenis tipe={s.tipe} />
      <div className="isi">
        <div className="judul">{tanpaNomor(s.judul)}</div>
        <div className="ket">
          {`${s.label_bahasa} · ${s.alasan}` + (s.menit ? ` · ≈${s.menit} menit` : "")}
        </div>
      </div>
      {cap ? <span className="pil pil-ungu sembunyi-hp">{cap}</span> : null}
      {/* Ditandai SEBELUM diklik, bukan sesudah. Latihan di bahasa yang
          toolchain-nya belum terpasang tetap bisa dikerjakan dan ditandai
          selesai sendiri -- yang mati cuma penilaian otomatisnya -- tapi orang
          berhak tahu itu sebelum membuka halamannya, bukan sesudah menulis
          tiga puluh baris kode. */}
      {s.tipe === "latihan" && siap.get(s.bahasa) === false ? (
        <span className="pil pil-kunci">tanpa nilai otomatis</span>
      ) : null}
      <span className="baris-panah">
        <Ikon nama="lanjut" ukuran={18} />
      </span>
    </a>
  );

  return (
    <section>
      <div className="bagian-kepala">
        <span className="mata">Antrean berikutnya</span>
        <a href="#/cari">Cari isi lain</a>
      </div>
      <div className="senarai">
        {langkah.map((s, i) => baris(s, null, "l" + i))}
        {tantangan ? baris(tantangan, "tantangan hari ini", "t") : null}
      </div>
    </section>
  );
}

/**
 * Ubin Peta Karier di dasbor: profesi yang paling dekat dicapai.
 *
 * Ubin lahir dengan isi yang sudah bermakna (judul dan tautan), lalu angkanya
 * menyusul; kalau permintaannya gagal, yang tertinggal tetap tautan yang benar.
 * Kesiapannya dihitung `pelajar/karier.py` -- tidak ada persen yang dihitung
 * ulang di sini.
 */
function UbinKarier() {
  const [p, setP] = useState<
    { id: string; nama: string; kesiapan: number; tujuan: boolean } | null>(null);

  useEffect(() => {
    let dibatalkan = false;
    ambil<{
      profesi: Array<{ id: string; nama: string; kesiapan: number }>;
      tujuan?: string;
    }>("karier")
      .then((k) => {
        if (dibatalkan) return;
        const pilih =
          k.profesi.find((x) => x.id === k.tujuan) ??
          [...k.profesi].sort((a, b) => b.kesiapan - a.kesiapan)[0];
        if (!pilih || (pilih.kesiapan <= 0 && pilih.id !== k.tujuan)) return;
        setP({ ...pilih, tujuan: pilih.id === k.tujuan });
      })
      .catch(() => {
        /* tautannya tetap benar tanpa angka */
      });
    return () => {
      dibatalkan = true;
    };
  }, []);

  return (
    <a className="meja-ubin-satu" href={p ? "#/karier/" + p.id : "#/karier"}>
      <span className="meja-ubin-kepala">
        <Ikon nama="karier" ukuran={18} />
        Peta karier
      </span>
      <span className="meja-ubin-isi">
        {p ? (
          <>
            <b>{(p.tujuan ? "Tujuanmu: " : "") + p.nama}</b>
            <span className="meja-ubin-angka">
              {`${Math.round(p.kesiapan)}% siap`}
            </span>
            <Bilah persen={p.kesiapan} kelas="meja-ubin-bilah" diam />
          </>
        ) : (
          "Lihat profesi yang bisa kamu tuju."
        )}
      </span>
    </a>
  );
}

/** Ubin Pustaka di dasbor: bacaan gratis untuk bahasa yang sedang dipelajari. */
function UbinPustaka({ kunci, label }: { kunci?: string | null; label?: string | null }) {
  const [isi, setIsi] = useState<{ judul?: string; total: number; id: number } | null>(
    null,
  );
  const href = kunci
    ? "#/pustaka?kurikulum=" + encodeURIComponent(kunci)
    : "#/pustaka";

  useEffect(() => {
    if (!kunci) return;
    let dibatalkan = false;
    ambil<{
      hasil: Array<{ judul: string }>;
      total: number;
      segi: { bahasa: Record<string, number> };
    }>("pustaka", { kurikulum: kunci, bahasa: "id" })
      .then((r) => {
        if (dibatalkan) return;
        const total = Object.values(r.segi.bahasa).reduce((a, b) => a + b, 0);
        setIsi({
          ...(r.hasil[0] ? { judul: r.hasil[0].judul } : {}),
          total,
          id: r.total,
        });
      })
      .catch(() => {
        /* tautannya tetap benar tanpa angka */
      });
    return () => {
      dibatalkan = true;
    };
  }, [kunci]);

  return (
    <a className="meja-ubin-satu" href={href}>
      <span className="meja-ubin-kepala">
        <Ikon nama="pustaka" ukuran={18} />
        {label ? `Bacaan ${label}` : "Pustaka"}
      </span>
      <span className="meja-ubin-isi">
        {isi ? (
          <>
            {isi.judul ? <b>{isi.judul}</b> : null}
            <span className="meja-ubin-angka">
              {`${angka(isi.total)} tautan, ${angka(isi.id)} berbahasa Indonesia`}
            </span>
          </>
        ) : (
          "Buku, kursus, dan proyek gratis."
        )}
      </span>
    </a>
  );
}

/** Panel "Langitmu": rasi kurikulum yang sedang dijalani.
 *
 *  Kalau tidak ada satu pun kurikulum yang sudah disentuh, panelnya TIDAK
 *  digambar -- bukan digambar kosong. Langit yang seluruh bintangnya redup
 *  tidak menjawab apa pun, dan ia memakan setinggi 230 piksel untuk itu. */
function PanelLangitMeja({ kunci }: { kunci?: string | null }) {
  const [bhs, setBhs] = useState<DataPeta | null>(null);

  useEffect(() => {
    let dibatalkan = false;
    ambil<{ bahasa: DataPeta[] }>("langit")
      .then((d) => {
        if (dibatalkan) return;
        const pilih =
          d.bahasa.find((x) => x.key === kunci) ??
          d.bahasa.find((x) => x.materi.some((m) => m.status !== "baru"));
        if (pilih) setBhs(pilih);
      })
      .catch(() => {
        /* panelnya tidak digambar */
      });
    return () => {
      dibatalkan = true;
    };
  }, [kunci]);

  if (!bhs) return null;
  return (
    <section className="meja-langit" aria-label="Peta langit belajarmu">
      <div className="meja-langit-kepala">
        <h2 className="meja-judul">Langitmu</h2>
        <span className="meja-langit-ket">
          Satu materi, satu bintang. Yang sudah kamu baca menyala.
        </span>
        <a className="meja-langit-tautan" href="#/langit">
          Seluruh langit
        </a>
      </div>
      <div className="meja-langit-isi">
        <PetaRasi data={bhs} tinggi={230} />
      </div>
    </section>
  );
}

/** Bahasa yang sedang dijalani: satu baris per bahasa, persennya SELALU
 *  terlihat. Akordeon lama menyembunyikannya sampai di-hover. Tanpa nomor
 *  01-04: nomor di aplikasi ini berarti urutan, dan bahasa-bahasa ini bukan
 *  urutan. */
function BarisBahasaMeja({ daftar }: { daftar: DataDasbor["bahasa"] }) {
  if (!daftar.length) return null;
  return (
    <section className="meja-bahasa" aria-label="Bahasa yang sedang kamu jalani">
      <h2 className="meja-judul">Yang sedang kamu jalani</h2>
      <div className="meja-bahasa-daftar">
        {daftar.map((b) => (
          <a key={b.key} className="meja-bahasa-baris" href={"#/bahasa/" + b.key}>
            <span className="meja-bahasa-nama">{b.label}</span>
            <span className="meja-bahasa-ket">
              {`${b.materi}/${b.total_materi} materi`}
            </span>
            <span className="meja-bahasa-bilah">
              <Bilah
                persen={Math.min(100, b.persen)}
                kelas={b.persen >= 100 ? "tumbuh" : ""}
              />
            </span>
            {/* "selesai", bukan "materi": persennya ikut menghitung kuis dan
                latihan. */}
            <b className="meja-bahasa-persen">{`${Math.round(b.persen)}% selesai`}</b>
          </a>
        ))}
      </div>
    </section>
  );
}

/* --------------------------------------------------------- layar mulai */

/** Kartu "mulai di sini" untuk orang yang belum mengerjakan apa pun.
 *
 *  Aksen dipakai sebagai GARIS kartu dan isi TOMBOLNYA, bukan latar kartunya.
 *  Latar aksen sudah punya satu pemilik di seluruh aplikasi -- `.lanjutkan` di
 *  dasbor -- dan yang membuat kartu itu berarti "ini yang sedang kamu
 *  kerjakan" justru batas tersebut. Layar ini belum melanjutkan apa pun. */
function KartuMulaiUtama({ s, bahasa }: { s: Langkah; bahasa: BahasaAwal[] }) {
  const b = bahasa.find((x) => x.key === s.bahasa);
  const jenis = labelMulai(s.tipe);
  return (
    <a className="mulai-utama" href={tautanLangkah(s)}>
      <div className="mulai-utama-isi">
        <span className="mata mata-nyala">{`Disarankan · ${s.label_bahasa}`}</span>
        <h2>{tanpaNomor(s.judul)}</h2>
        <p>
          {b && !b.pasang
            ? `${jenis}. Tidak perlu memasang apa pun: cukup aplikasi ini dan ` +
              "browser yang sedang kamu buka."
            : `${jenis}. Langkah pertama di jalur ${s.label_bahasa}.`}
        </p>
      </div>
      <span className="tbl tbl-utama tbl-besar">
        Mulai
        <Ikon nama="lanjut" ukuran={18} />
      </span>
    </a>
  );
}

/** Satu ubin bahasa di layar mulai. */
function UbinBahasa({
  b, urut, aktif, onFokus, elRef,
}: {
  b: BahasaAwal;
  urut: number;
  aktif: boolean;
  onFokus: (i: number) => void;
  elRef: (el: HTMLAnchorElement | null) => void;
}) {
  const tanda = tandaUbin(b);
  return (
    <a
      ref={elRef}
      className="ubin"
      href={"#/bahasa/" + b.key}
      tabIndex={aktif ? 0 : -1}
      onFocus={() => onFokus(urut)}
    >
      <b className="ubin-nama">{b.label}</b>
      <span className="ubin-jml">{`${b.materi} materi · ${b.latihan} latihan`}</span>
      {tanda ? <span className={"ubin-tanda " + tanda[0]}>{tanda[1]}</span> : null}
    </a>
  );
}

/**
 * Panah memindah fokus antar-ubin, dengan SATU ubin saja yang ikut Tab.
 *
 * Kisi tiga puluh dua tautan berarti tiga puluh dua perhentian Tab sebelum
 * sampai ke apa pun di bawahnya. Pola roving tabindex memampatkannya jadi satu:
 * Tab masuk ke kisi, panah berjalan di dalamnya, Tab keluar lagi.
 *
 * Jumlah kolom dihitung dari POSISI NYATA tiap ubin, bukan dari CSS: kisinya
 * `auto-fill`, jadi jumlah kolomnya berubah mengikuti lebar jendela dan tidak
 * pernah tertulis di satu tempat yang bisa dibaca. Menebaknya dari breakpoint
 * berarti panah bawah melompat salah tiap kali lebarnya di antara dua ambang.
 *
 * Tidak ada role ARIA yang ditambahkan. Ini sekumpulan tautan, bukan grid data;
 * memberinya `role="grid"` menuntut struktur baris/sel yang tidak ada, dan
 * pembaca layar akan menjanjikan navigasi yang tidak pernah disediakan.
 */
function KisiUbin({ daftar }: { daftar: BahasaAwal[] }) {
  const [fokus, setFokus] = useState(0);
  const ubinRef = useRef<Array<HTMLAnchorElement | null>>([]);

  const kolom = () => {
    const ubin = ubinRef.current.filter(Boolean) as HTMLAnchorElement[];
    if (!ubin.length) return 1;
    const atas = (ubin[0] as HTMLAnchorElement).getBoundingClientRect().top;
    let n = 0;
    for (const el of ubin) {
      if (Math.abs(el.getBoundingClientRect().top - atas) > 1) break;
      n++;
    }
    return Math.max(1, n);
  };

  return (
    <div
      className="ubin-bahasa"
      onKeyDown={(e) => {
        const k = kolom();
        const tuju: Record<string, number> = {
          ArrowRight: fokus + 1,
          ArrowLeft: fokus - 1,
          ArrowDown: fokus + k,
          ArrowUp: fokus - k,
          Home: 0,
          End: daftar.length - 1,
        };
        if (!(e.key in tuju)) return;
        e.preventDefault();
        const j = Math.max(0, Math.min(daftar.length - 1, tuju[e.key] as number));
        setFokus(j);
        ubinRef.current[j]?.focus();
      }}
    >
      {daftar.map((b, i) => (
        <UbinBahasa
          key={b.key}
          b={b}
          urut={i}
          aktif={i === fokus}
          onFokus={setFokus}
          elRef={(el) => {
            ubinRef.current[i] = el;
          }}
        />
      ))}
    </div>
  );
}

function LayarMulai({
  d, bahasa, aturan,
}: {
  d: DataDasbor;
  bahasa: BahasaAwal[];
  aturan: { aturan?: string; pintu_darurat?: string; tingkat?: Tingkat[] };
}) {
  const langkah = d.langkah[0];
  const jml = jumlahKurikulum(bahasa);
  const tematik = bahasa.filter((b) => b.tematik);
  const bukanTematik = bahasa.filter((b) => !b.tematik);

  return (
    <div className="mulai masuk-urut">
      <header className="sambut sambut-tengah">
        <span className="mata">Selamat datang</span>
        <h1>Mau mulai dari mana?</h1>
        <p className="sambut-sub">
          {`${angka(bahasa.length)} bahasa · ${angka(jml.materi)} materi · ` +
            `${angka(jml.kuis)} kuis · ${angka(jml.latihan)} latihan. ` +
            "Pilih satu; sisanya menunggu dan tidak ke mana-mana."}
        </p>
      </header>

      {langkah ? <KartuMulaiUtama s={langkah} bahasa={bahasa} /> : null}

      {/* SEMUA bahasa, bukan dua. Menyembunyikan tiga puluh di balik menu pada
          layar yang justru bertanya "mau mulai dari mana" berarti menjawab
          pertanyaannya dengan setengah katalog -- dan orang yang sedang
          menimbang apakah aplikasi ini sepadan waktunya tidak punya cara
          melihat isinya. */}
      <section className="mulai-pilih">
        <div className="bagian-kepala">
          <span className="mata">Atau pilih sendiri</span>
          {/* Dihitung dari `siap`, bukan diketik: yang terpasang di satu
              komputer belum tentu terpasang di komputer berikutnya. */}
          <span className="bagian-ket">
            {`${angka(bahasa.filter((b) => b.siap).length)} dari ` +
              `${angka(bahasa.length)} bisa dijalankan di komputer ini`}
          </span>
        </div>
        <KisiUbin daftar={bukanTematik} />
        {/* Kurikulum yang bukan bahasa pemrograman: satu mengajarkan cara
            BERPIKIR membangun aplikasi, satu lagi cara MENGOPERASIKAN sistem.
            Berbaris di kisi yang sama, keduanya terbaca sebagai bahasa asing
            yang belum pernah pelajar dengar -- dan "Bikin Aplikasi" bahkan
            terbaca seperti nama bahasa. */}
        {tematik.length ? (
          <>
            <div className="bagian-kepala bagian-kepala-lanjutan">
              <span className="mata">Bukan bahasa, tapi tetap kurikulum</span>
              <span className="bagian-ket">
                Cara berpikir dan cara mengoperasikan, bukan sintaks
              </span>
            </div>
            <KisiUbin daftar={tematik} />
          </>
        ) : null}
      </section>

      <a className="pintu-tenang" href="#/coba">
        <span className="ikon-bulat">
          <Ikon nama="jalankan" ukuran={18} />
        </span>
        <div className="pintu-isi">
          <b>Belum mau memilih?</b>
          <span>
            Ruang Coba: tulis kode apa saja, jalankan, lihat hasilnya. Tidak
            dinilai, tidak menyentuh progres.
          </span>
        </div>
        <span className="baris-panah">
          <Ikon nama="lanjut" ukuran={18} />
        </span>
      </a>

      <section>
        <span className="mata">Cara kerjanya</span>
        <div className="kartu kartu-aturan">
          {/* Kalimat aturannya datang dari `bab.KALIMAT_ATURAN` lewat
              `/api/awal`, TIDAK ditulis ulang di sini. Tiga permukaan
              menjelaskan aturan yang sama ke pelajar; rumusan yang disalin bisa
              melenceng satu per satu tanpa satu tes pun gagal. */}
          <p className="aturan-utama">{aturan.aturan || ""}</p>
          {aturan.tingkat && aturan.tingkat.length ? (
            <dl className="tingkat-daftar">
              {aturan.tingkat.map((t) => (
                <div key={t.nama} style={{ display: "contents" }}>
                  <dt className={"pil t-" + t.nama}>{t.label}</dt>
                  <dd>{t.ket}</dd>
                </div>
              ))}
            </dl>
          ) : null}
          {aturan.pintu_darurat ? (
            <p className="aturan-pintu">
              <span>{aturan.pintu_darurat}</span>
              <a className="tbl tbl-kecil tbl-hantu" href="#/atur">
                Buka Pengaturan
              </a>
            </p>
          ) : null}
        </div>
      </section>
    </div>
  );
}

/* ----------------------------------------------------------- meja kerja */

function MejaKerja({ d, bahasa }: { d: DataDasbor; bahasa: BahasaAwal[] }) {
  const sapa = sapaJam(new Date().getHours());
  const { awal, sisa } = pecahSapa(sapa, d.nama);
  // Langkah PERTAMA diangkat keluar dari daftar dan diberi kartunya sendiri.
  // Inilah perubahan susunan yang paling menentukan di seluruh dasbor: yang
  // dibutuhkan orang yang belajar dari nol bukan ringkasan capaiannya,
  // melainkan satu kalimat yang menjawab "sekarang aku ngapain". Sisanya tetap
  // ada, tapi di KOLOM SEBELAH, bukan di bawahnya.
  const [utama, ...sisaLangkah] = d.langkah;
  const dijalani = useMemo(() => dijalaniDasbor(d.bahasa), [d.bahasa]);
  const p = d.posisi;
  const paket = paketTigaPuluh([utama, ...sisaLangkah]);

  return (
    <div className="meja">
      <section className="meja-atas">
        <div className="meja-kini">
          <span className="mata">
            {new Date().toLocaleDateString("id-ID", {
              weekday: "long",
              day: "numeric",
              month: "long",
              year: "numeric",
            })}
          </span>
          {/* Satu pil gambar di dalam judulnya belum diport bersama
              `sampul.js`; judulnya tetap terbaca utuh karena pil itu memang
              `aria-hidden` dan kosong teks. */}
          <h1>{awal + " " + sisa}</h1>
          {p ? (
            <p className="meja-posisi">
              <a href={"#/bahasa/" + p.key}>
                <b>{p.label}</b>
              </a>
              {p.bab ? ` · Bab ${p.bab} dari ${p.bab_total}: ${p.bab_judul}` : ""}
              {` · ${p.materi}/${p.total_materi} materi`}
            </p>
          ) : null}
          {paket.muat.length > 1 ? (
            <p className="meja-paket">
              <Ikon nama="waktu" ukuran={16} />
              {`Punya 30 menit? ${paket.muat.length} langkah teratas kira-kira ${paket.total} menit.`}
            </p>
          ) : null}
          {utama ? (
            <KartuLanjutkan s={utama} />
          ) : (
            <p className="sambut-sub">{kalimatPembuka(d)}</p>
          )}
        </div>
        <div className="meja-antrean">
          {sisaLangkah.length || d.tantangan ? (
            <BlokAntrean
              langkah={sisaLangkah}
              tantangan={d.tantangan}
              bahasa={bahasa}
            />
          ) : (
            <p className="sambut-sub">{kalimatPembuka(d)}</p>
          )}
          {d.kuis_jatuh_tempo > 2 ? (
            <p className="meja-catatan">
              {`${d.kuis_jatuh_tempo} kuis menunggu diulang. ` +
                "Dua yang paling mendesak sudah ada di antrean; sisanya bisa besok."}
            </p>
          ) : null}
          {/* Di kolom kanan, bukan di bawah: kolom kiri (sapaan + kartu) lebih
              tinggi daripada antrean, dan ruang di bawah antrean itulah tempat
              persen tiap bahasa terlihat tanpa menggulir. */}
          <BarisBahasaMeja daftar={dijalani.slice(0, 4)} />
        </div>
      </section>

      <PanelLangitMeja kunci={p ? p.key : null} />

      <div className="bento">
        <div className="bento-level">
          <KartuBara d={d} />
        </div>
        <div className="bento-pekan">
          <PekanIni d={d} />
        </div>
        <div className="bento-karier">
          <UbinKarier />
        </div>
        <div className="bento-pustaka">
          <UbinPustaka
            kunci={utama ? utama.bahasa : null}
            label={utama ? utama.label_bahasa : null}
          />
        </div>
      </div>

      <section className="meja-ritme">
        <BlokBara d={d} />
      </section>
    </div>
  );
}

/* ================================================================== layar */

export function Dasbor({
  bahasa, aturan,
}: {
  bahasa: BahasaAwal[];
  aturan: { aturan?: string; pintu_darurat?: string; tingkat?: Tingkat[] };
}) {
  const [d, setD] = useState<DataDasbor | null>(null);
  const [galat, setGalat] = useState("");

  useEffect(() => {
    let dibatalkan = false;
    ambil<DataDasbor>("dasbor")
      .then((x) => {
        if (!dibatalkan) setD(x);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, []);

  if (galat) {
    return (
      <Keadaan
        jenis="salah"
        gambar="belum"
        judul="Dasbor tidak terbaca"
        ket={galat}
        aksi={
          <a className="tbl" href="#/langit">
            Ke Langit
          </a>
        }
      />
    );
  }
  if (!d) return <div className="pusaran" aria-label="Memuat" />;
  if (d.xp === 0) return <LayarMulai d={d} bahasa={bahasa} aturan={aturan} />;
  return <MejaKerja d={d} bahasa={bahasa} />;
}
