/* Halaman bahasa: satu kurikulum, empat tab, dan peta bab yang bisa dilipat.
 *
 * Port `layarBahasa` beserta tujuh pembantunya dari
 * `webapp/statik/js/layar-belajar.js`. Ini tujuan yang PALING SERING dibuka di
 * aplikasi ini, dan jalur yang paling sering dilalui bukan "buka pertama kali"
 * melainkan "kembali dari materi yang baru dibaca".
 *
 * Yang murni tinggal di `bahasa-teks.ts` (kalimat kepala, baris fakta, dan
 * pilihan kartu Lanjutkan) dan di `komponen/rasi-geometri.ts` (tata letak peta
 * rasi). Keduanya diadu dengan JS yang masih melayani aplikasi lama. Yang di
 * berkas ini cuma bentuk elemennya.
 *
 * Empat aturan yang dibawa utuh dari versi JS, dan tiga di antaranya mudah
 * hilang saat diport:
 *
 * 1. **Penguncian bab hanya diputuskan `pelajar/bab.py`.** Status tiap bab
 *    sudah jadi saat sampai. Tidak ada satu pun `if (materi_dibaca >= ...)` di
 *    sini, dan tidak boleh ada: definisi kedua tentang "boleh dibuka" adalah
 *    cara tercepat membuat dua antarmuka berbeda pendapat soal hal yang sama.
 * 2. **Bab yang terkunci tetap DITAMPILKAN** -- judulnya, tingkatnya, jumlah
 *    materinya, dan alasannya, semuanya di KEPALA bab yang tidak pernah ikut
 *    terlipat. Yang disembunyikan cuma daftar judul materi yang memang belum
 *    boleh dibuka.
 * 3. **Kalimat aturannya datang dari server** (`/api/awal -> aturan_bab`),
 *    termasuk label dan keterangan tiap tingkat. Halaman ini tidak menamai
 *    tingkat dengan kata-katanya sendiri.
 * 4. **Tidak boleh ada tombol yang berujung penolakan.** Materi terkunci
 *    digambar sebagai `<div>`, bukan `<a>` yang dimatikan CSS: baris yang
 *    tidak bisa dibuka juga tidak boleh disinggahi Tab, dan pembaca layar
 *    tidak boleh mengumumkannya sebagai tautan. Toolchain yang belum terpasang
 *    ditandai SEBELUM diklik, bukan sesudah.
 *
 * Yang TIDAK diport: koreografi masuk per baris (`ungkap`/`ungkapSekali`) dan
 * FLIP saat penyaring tingkat dipakai (`tata`). Keduanya mesin di `gerak.js`;
 * penggantinya kelas entrance CSS yang sudah ada (`.masuk`, `.masuk-mandiri`),
 * dan penyaringnya jadi turunan state. Yang dipertahankan justru invariannya:
 * keadaan akhir sebuah animasi = keadaan alami elemennya, jadi gerak yang
 * dimatikan tidak pernah berarti ada yang hilang.
 */

import { useEffect, useMemo, useRef, useState } from "react";
import { useUngkap } from "../gerak-react.ts";

import { ambil } from "../api.ts";
import type { Konteks } from "../Cangkang.tsx";
import { tingkatGerak } from "../gerak.ts";
import { Bilah } from "../komponen/Bilah.tsx";
import { Ikon } from "../komponen/Ikon.tsx";
import { ikonTipe } from "../komponen/ikon-bentuk.ts";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { PetaRasi } from "../komponen/Rasi.tsx";
import { dariBahasa } from "../komponen/rasi-geometri.ts";
import { ingat } from "../lokal.ts";
import { salin } from "../sorak.tsx";
import { angka, tanpaNomor } from "../util.tsx";
import { jamRamah, selisihHari } from "../waktu.ts";
import {
  faktaBahasa, kalimatBahasa, pilihLanjut,
  type Lanjut, type StatBahasa,
} from "./bahasa-teks.ts";
import { BarisTautan } from "./Pustaka.tsx";

/* --------------------------------------------------------------- bentuk data */

interface Materi {
  indeks: number;
  judul: string;
  status: string;
  menit?: number;
  bagian?: number;
  bookmark?: boolean;
  terkunci?: boolean;
  tingkat?: string;
}

interface Kuis {
  indeks: number;
  judul: string;
  soal: number;
  terbaik: number;
  percobaan: number;
  total_soal: number;
  terakhir_waktu?: string | null;
  pernah?: boolean;
  jatuh_tempo?: boolean;
  jadwal?: string | null;
  salah_tersisa?: number;
  siap?: boolean;
  sisa_materi?: number;
}

interface Latihan {
  indeks: number;
  judul: string;
  tingkat: string;
  status: string;
  dinilai: boolean;
  alasan?: string;
  proyek?: boolean;
}

interface Bab {
  nomor: number;
  judul: string;
  ket?: string;
  tingkat: string;
  label_tingkat: string;
  materi: number[];
  selesai: number;
  jumlah: number;
  status: string;
  alasan?: string;
  persen: number;
}

interface JenisPustaka {
  jenis: string;
  label: string;
  jumlah: number;
}

interface Pustaka {
  total: number;
  per_jenis: JenisPustaka[];
  pembuka: Array<{
    url: string;
    judul: string;
    jenis: string;
    bahasa: string;
    catatan?: string;
    topik?: string[];
  }>;
}

export interface DataBahasa {
  key: string;
  label: string;
  runner: string;
  siap: boolean;
  tebak: number;
  hilang?: string[];
  pasang?: string;
  catatan?: string;
  statistik: StatBahasa;
  materi: Materi[];
  kuis: Kuis[];
  latihan: Latihan[];
  bab: Bab[];
  bab_kalimat?: string;
  buka_semua_bab?: boolean;
  pustaka: Pustaka;
}

/** Satu tingkat seperti yang dikirim `/api/awal -> aturan_bab.tingkat`. */
export interface Tingkat {
  nama: string;
  label: string;
  ket: string;
}

type NamaTab = "materi" | "kuis" | "latihan" | "bacaan";
const TAB: NamaTab[] = ["materi", "kuis", "latihan", "bacaan"];

/* --------------------------------------------------------------- pembantu */

/** "perlu go, dotnet". Ditempel di tab Latihan dan tautan Ruang coba. */
function PilBelumSiap({ hilang }: { hilang?: string[] }) {
  return (
    <span className="pil pil-kunci">
      {"perlu " + (hilang && hilang.length ? hilang.join(", ") : "dipasang")}
    </span>
  );
}

/**
 * Tindakan utama halaman: satu tautan menuju hal berikutnya.
 *
 * Kartu ini SATU-SATUNYA permukaan di layar ini yang memakai warna aksen
 * sebagai LATAR. Menambah yang kedua tidak membuat dua hal penting -- ia
 * membuat nol.
 */
function KartuLanjut({ s, kunci }: { s: Lanjut; kunci: string }) {
  return (
    <a className="lanjutkan lanjutkan-rapat" href={`#/${s.tipe}/${kunci}/${s.indeks}`}>
      <span className="lanjutkan-nomor">{s.indeks + 1}</span>
      <div className="lanjutkan-isi">
        <span className="mata">{s.mata}</span>
        <h2>{tanpaNomor(s.judul)}</h2>
        <p>{s.ket}</p>
      </div>
      <span className="lanjutkan-tbl">
        <span>Buka</span>
        <Ikon nama="lanjut" ukuran={20} />
      </span>
    </a>
  );
}

/** Toolchain yang belum terpasang, beserta perintah pemasangannya. */
function BlokToolchain({ b }: { b: DataBahasa }) {
  return (
    <Keadaan
      jenis="salah"
      gambar="belum"
      judul={`Kode ${b.label} belum bisa dijalankan di komputer ini`}
      ket={
        `Yang belum terpasang: ${(b.hilang || []).join(", ")}. Materi dan kuis ` +
        "tetap berjalan penuh; yang mati hanya penilaian otomatis latihan, dan " +
        "latihannya tetap bisa dikerjakan lalu ditandai selesai sendiri."
      }
      aksi={
        b.pasang ? (
          <>
            <code className="berkas-jalur">{b.pasang}</code>
            <button
              type="button"
              className="tbl tbl-kecil"
              onClick={() => {
                void salin(b.pasang as string,
                           "Perintah disalin. Tempel di terminal.");
              }}
            >
              Salin
            </button>
          </>
        ) : null
      }
    />
  );
}

/**
 * Cincin persen kecil yang MEMELUK nomor bab.
 *
 * `stroke-dashoffset` AKHIR dipasang langsung di atributnya; animasinya cuma
 * berangkat dari lingkaran kosong. Kalau gerak dimatikan atau JS tidak jalan
 * sama sekali, yang tertinggal tetap busur dengan panjang yang benar.
 *
 * Versi JS menunggu `saatTampak()` sebelum menganimasikan. Di sini tidak, dan
 * itu aman justru KARENA pola di atas: pengamat yang tidak pernah menyala
 * berarti cincinnya sudah benar sejak awal, jadi pengamatnya optimasi, bukan
 * alat kebenaran. Yang dipertahankan hal yang memang menjawab sesuatu: hanya
 * bab yang SEDANG dikerjakan beranimasi. Sebelas busur yang mengisi diri
 * bersamaan adalah sebelas gerakan yang tidak menjawab satu pertanyaan pun.
 */
function CincinBab({ bab, animasikan }: { bab: Bab; animasikan: boolean }) {
  const R = 15;
  const keliling = 2 * Math.PI * R;
  const akhir = keliling * (1 - Math.max(0, Math.min(1, bab.persen / 100)));
  const isiRef = useRef<SVGCircleElement>(null);

  useEffect(() => {
    const isi = isiRef.current;
    if (!isi || !animasikan || tingkatGerak() === "mati") return;
    isi.animate(
      { strokeDashoffset: [String(keliling), String(akhir)] },
      { duration: 700, easing: "cubic-bezier(.32,.72,.36,1)" },
    );
  }, [animasikan, keliling, akhir]);

  return (
    <div className="bab-cincin">
      <svg viewBox="0 0 36 36" aria-hidden="true">
        <circle cx="18" cy="18" r={R} fill="none" strokeWidth="3" className="alur" />
        <circle
          ref={isiRef}
          cx="18"
          cy="18"
          r={R}
          fill="none"
          strokeWidth="3"
          className="isi"
          strokeDasharray={keliling}
          strokeDashoffset={akhir}
        />
      </svg>
      <span className="bab-nomor">{String(bab.nomor).padStart(2, "0")}</span>
    </div>
  );
}

/**
 * Kepala satu bab: nomor besar, tingkat, judul, satu kalimat isi, kemajuan.
 *
 * NOMOR ADALAH ARSITEKTUR, dan ini penerapannya yang paling langsung: nomor
 * bab tampil sebesar judulnya sendiri, di kolomnya sendiri. Mata memakai kolom
 * itu sebagai penggaris, dan "aku di bab berapa" berhenti butuh dibaca.
 *
 * Warna tingkat sengaja BUKAN aksen, walau tangga kesulitan latihan
 * memakainya: aksen sudah dipakai untuk menandai bab yang sedang dikerjakan,
 * dan memberi warna yang sama kepada setiap pil "Menengah" berarti membuat
 * penanda itu hilang di tengah keramaian.
 */
function KepalaBab({ bab, kini }: { bab: Bab; kini: boolean }) {
  return (
    <summary className="bab-kepala">
      <CincinBab bab={bab} animasikan={kini} />
      <div className="bab-teks">
        <div className="bab-atas">
          <span
            className={"pil bab-tingkat bab-" + bab.tingkat}
            title={"Tingkat " + bab.label_tingkat.toLowerCase()}
          >
            {bab.label_tingkat}
          </span>
          {bab.status === "terkunci" ? (
            <span className="pil bab-cap">belum terbuka</span>
          ) : null}
          {bab.status === "tuntas" ? (
            <span className="pil pil-tumbuh">
              <Ikon nama="selesai" ukuran={13} tebal={2} />
              tuntas
            </span>
          ) : null}
        </div>
        <h3 className="bab-judul">{bab.judul}</h3>
        {bab.ket ? <p className="bab-ket">{bab.ket}</p> : null}
      </div>
      <div className="bab-maju">
        <span className="bab-angka">{`${bab.selesai}/${bab.jumlah} materi`}</span>
      </div>
      {/* Chevron yang berputar 90 derajat saat babnya terbuka (gaya.css).
          Ini SATU-SATUNYA tanda bahwa kepala bab bisa diklik: `.bab-kepala`
          memasang `list-style: none` dan menyembunyikan
          `::-webkit-details-marker`, jadi tanpa ikon ini bab yang terlipat
          terbaca sebagai kartu mati. */}
      <span className="bab-lipat">
        <Ikon nama="lanjut" ukuran={18} />
      </span>
    </summary>
  );
}

/** Kenapa sebuah bab masih terkunci, dan -- sekali saja -- jalan keluarnya.
 *
 *  Kalimatnya datang utuh dari `bab.py`; ia sudah menyebut berapa materi lagi
 *  yang kurang dan di bab mana. Menyusun ulang kalimat itu di sini berarti
 *  aturan yang sama dijelaskan dengan dua cara berbeda di dua antarmuka. */
function CatatanKunci({ bab, tawarkan }: { bab: Bab; tawarkan: boolean }) {
  return (
    <div className="bab-kunci">
      <span>{bab.alasan}</span>
      {tawarkan ? (
        <a className="bab-kunci-jalan" href="#/atur">
          Sudah pernah belajar bahasa ini? Buka semua bab di Pengaturan.
        </a>
      ) : null}
    </div>
  );
}

/** Satu baris materi. Yang terkunci tetap ditampilkan utuh -- judulnya,
 *  nomornya, panjangnya -- tapi bukan sebagai tautan. */
function BarisMateri({ kunci, m }: { kunci: string; m: Materi }) {
  const isi = (
    <>
      <span className="nomor">{m.indeks + 1}</span>
      <span
        className={
          "titik" +
          (m.status === "selesai" ? " selesai" : m.status === "sebagian" ? " sedang" : "")
        }
      />
      <div className="isi">
        <div className="judul">{tanpaNomor(m.judul)}</div>
        {m.status === "sebagian" ? (
          <div className="ket">berhenti di tengah, belum dihitung selesai</div>
        ) : null}
      </div>
      {m.bookmark ? <span className="pil pil-nyala">ditandai</span> : null}
      <span className="baris-sisi sembunyi-hp">
        {m.menit ? `≈${m.menit} menit` : `${m.bagian} bagian`}
      </span>
    </>
  );
  if (m.terkunci) return <div className="baris baris-terkunci">{isi}</div>;
  return (
    <a
      className={"baris" + (m.status === "selesai" ? " selesai" : "")}
      href={`#/materi/${kunci}/${m.indeks}`}
    >
      {isi}
    </a>
  );
}

/** Gulir ke sebuah bab dan buka lipatannya. Elemennya harus sudah terlihat:
 *  `scrollIntoView` pada elemen `hidden` (bab yang tersaring chip tingkat)
 *  tidak berbuat apa-apa, jadi pemanggilnya melepas saringannya lebih dulu. */
function gulirKeBab(nomor: number) {
  const sasaran = document.getElementById("bab-" + nomor);
  if (!sasaran) return;
  (sasaran as HTMLDetailsElement).open = true;
  sasaran.scrollIntoView({
    behavior: tingkatGerak() === "mati" ? "auto" : "smooth",
    block: "start",
  });
}

/** Satu segmen di peta bab. */
function SegmenBab({
  bab, kini, onBuka,
}: {
  bab: Bab; kini: boolean; onBuka: (bab: Bab) => void;
}) {
  const kelas =
    bab.status === "tuntas"
      ? "peta-tuntas"
      : bab.status === "terkunci"
        ? "peta-terkunci"
        : kini
          ? "peta-kini"
          : "peta-jalan";
  return (
    <a
      className={kelas}
      href={"#bab-" + bab.nomor}
      // Bab terkunci membawa ALASANNYA, bukan cuma penanda bahwa ia terkunci.
      // Kalimatnya datang utuh dari `bab.py`; halaman ini cuma meneruskannya ke
      // tempat yang bisa dibaca sebelum diklik.
      title={
        `Bab ${bab.nomor} · ${bab.judul}: ${bab.selesai}/${bab.jumlah} materi ` +
        `(${bab.label_tingkat.toLowerCase()})` +
        (bab.alasan ? ". " + bab.alasan : "")
      }
      // Tautan ini menunjuk id di halaman yang sama, BUKAN rute. Router membaca
      // fragmen sebagai alamat layar, jadi pemindahannya diurus di sini dan
      // hash-nya tidak pernah ikut berubah -- kalau tidak, mengeklik "Bab 5"
      // akan mendarat di dasbor. Penggulirannya sendiri milik `DaftarMateri`,
      // yang memegang saringan tingkat.
      onClick={(e) => {
        e.preventDefault();
        onBuka(bab);
      }}
    >
      <span>{bab.nomor}</span>
      <i style={{ opacity: String(0.35 + 0.65 * (bab.persen / 100)) }} />
    </a>
  );
}

/**
 * Peta bab: satu rail per TINGKAT, bukan satu barisan panjang tanpa batas.
 *
 * Sebelas bab dalam satu deretan menjawab "ada berapa", tapi tidak menjawab
 * "sampai mana yang masih dasar". Labelnya dan keterangannya datang dari server
 * (`aturan_bab.tingkat`), jadi halaman ini tidak menamai tingkat dengan
 * kata-katanya sendiri.
 *
 * Rail TIDAK ikut disaring chip tingkat: yang digambarkannya SELURUH jalur
 * bahasa itu, dan jalur yang ikut menyusut saat disaring berhenti bisa
 * menjawab "ada berapa seluruhnya".
 */
function PetaBab({
  daftar, sedang, tingkat, onBuka,
}: {
  daftar: Bab[];
  sedang?: Bab;
  tingkat: Tingkat[];
  onBuka: (bab: Bab) => void;
}) {
  const kelompok = tingkat.filter((t) => daftar.some((b) => b.tingkat === t.nama));
  return (
    <nav className="peta-bab" aria-label="Peta bab">
      {kelompok.length ? (
        kelompok.map((t) => {
          const isi = daftar.filter((b) => b.tingkat === t.nama);
          return (
            <div className="peta-tingkat" key={t.nama}>
              <span className="peta-label" title={t.ket}>
                {t.label}
                <span className="peta-jml">{isi.length}</span>
              </span>
              <div className="peta-rel">
                {isi.map((bab) => (
                  <SegmenBab key={bab.nomor} bab={bab} kini={bab === sedang}
                               onBuka={onBuka} />
                ))}
              </div>
            </div>
          );
        })
      ) : (
        // Server tanpa `aturan_bab` (atau bahasa yang semua babnya satu tingkat)
        // tetap dapat railnya, cuma tanpa kepala tingkat. Tidak ada label yang
        // dikarang di sini sebagai gantinya.
        <div className="peta-rel">
          {daftar.map((bab) => (
            <SegmenBab key={bab.nomor} bab={bab} kini={bab === sedang}
                               onBuka={onBuka} />
          ))}
        </div>
      )}
    </nav>
  );
}

/**
 * Chip tingkat yang menyaring bab yang SUDAH ADA, bukan memuat ulang apa pun.
 *
 * Tanpa chip yang ditekan, semuanya tampil -- jadi keadaan diamnya adalah
 * keadaan LENGKAP, dan tidak ada pilihan bawaan yang diam-diam menyembunyikan
 * sesuatu dari orang yang belum pernah menyentuh chip-nya.
 *
 * Satu tingkat berarti tidak ada yang bisa disaring; chip tunggal yang
 * menyembunyikan segalanya atau tidak sama sekali bukan penyaring, jadi deret
 * ini tidak digambar sama sekali.
 */
function SaringBab({
  daftar, tingkat, pilih, setPilih,
}: {
  daftar: Bab[];
  tingkat: Tingkat[];
  pilih: Set<string>;
  setPilih: (s: Set<string>) => void;
}) {
  const kelompok = tingkat.filter((t) => daftar.some((b) => b.tingkat === t.nama));
  if (kelompok.length < 2) return null;
  const tampil = daftar.filter((b) => pilih.size === 0 || pilih.has(b.tingkat)).length;
  return (
    <div className="deret bab-saring-deret">
      <span className="mata">Saring tingkat</span>
      {kelompok.map((t) => {
        const aktif = pilih.has(t.nama);
        const jml = daftar.filter((b) => b.tingkat === t.nama).length;
        return (
          <button
            key={t.nama}
            type="button"
            className={"tbl bab-saring " + (aktif ? "tbl-pilih" : "tbl-hantu")}
            title={t.ket}
            aria-pressed={aktif}
            onClick={() => {
              const s = new Set(pilih);
              if (s.has(t.nama)) s.delete(t.nama);
              else s.add(t.nama);
              setPilih(s);
            }}
          >
            {t.label}
            <span className="tab-jumlah">{jml}</span>
          </button>
        );
      })}
      <span className="deret-kanan">
        <span className="bab-saring-jml" role="status">
          {pilih.size === 0
            ? `${daftar.length} bab, semuanya ditampilkan`
            : `${tampil} dari ${daftar.length} bab ditampilkan`}
        </span>
      </span>
    </div>
  );
}

/**
 * Daftar materi, dikelompokkan per bab dan BISA DILIPAT.
 *
 * Pelipatannya menyelesaikan masalah paling nyata di halaman ini: HTML punya
 * 11 bab berisi 44 materi, dan dirender penuh semuanya halamannya lima ribu
 * piksel -- tanpa satu titik pun yang menjawab "ada berapa bab dan aku di
 * mana" tanpa menggulir seluruhnya lebih dulu.
 *
 * Satu bab saja berarti tidak ada yang dikelompokkan: bahasa itu belum punya
 * pembagian bab, dan kepala "Semua materi" di atas seluruh daftarnya cuma satu
 * lapis tambahan yang tidak menjawab apa pun.
 */
function DaftarMateri({ b, tingkat }: { b: DataBahasa; tingkat: Tingkat[] }) {
  const daftar = b.bab || [];
  const [pilih, setPilih] = useState<Set<string>>(new Set());
  const materi = useMemo(
    () => new Map(b.materi.map((m) => [m.indeks, m])),
    [b.materi],
  );
  // Bab yang baru saja dipilih lewat peta dan menunggu dilepasnya `hidden`.
  const [tuju, setTuju] = useState<number | null>(null);
  useEffect(() => {
    if (tuju === null) return;
    gulirKeBab(tuju);
    setTuju(null);
  }, [tuju]);

  /* Peta bab sengaja TIDAK ikut tersaring, jadi segmen bab yang disaring chip
     tingkat tetap tampak bisa diklik. Bab itu `hidden` (`display: none`), dan
     menggulir ke elemen seperti itu tidak berbuat apa-apa: klik tampak mati.
     Tingkat babnya ditambahkan ke saringan, bukan seluruh saringan dibuang:
     pilihan orang tetap utuh dan chip yang menyala menjelaskan kenapa babnya
     kini muncul. Penggulirannya menunggu render, karena `hidden` baru lepas
     sesudah state diterapkan. */
  const bukaBab = (bab: Bab) => {
    if (pilih.size > 0 && !pilih.has(bab.tingkat)) {
      setPilih(new Set([...pilih, bab.tingkat]));
      setTuju(bab.nomor);
      return;
    }
    gulirKeBab(bab.nomor);
  };

  const ringkas =
    b.bab_kalimat || b.buka_semua_bab ? (
      <div className="bab-ringkas">
        {b.bab_kalimat ? <p>{b.bab_kalimat}</p> : null}
        {/* Saat saklarnya menyala, yang perlu dijawab halaman ini bukan "kenapa
            bab ini terbuka" melainkan "kenapa TIDAK ADA yang terkunci" -- dan
            pertanyaan itu datang berbulan-bulan sesudah saklarnya dipindahkan,
            ketika alasannya sudah lama lupa. */}
        {b.buka_semua_bab ? (
          <p className="bab-bebas">
            Penguncian bab sedang dimatikan: semua bab terbuka tanpa syarat.{" "}
            <a href="#/atur">Ubah di Pengaturan</a>.
          </p>
        ) : null}
      </div>
    ) : null;

  if (daftar.length < 2) {
    return (
      <div>
        {ringkas}
        <div className="senarai">
          {b.materi.map((m) => (
            <BarisMateri key={m.indeks} kunci={b.key} m={m} />
          ))}
        </div>
      </div>
    );
  }

  // Bab terkunci PERTAMA adalah satu-satunya pintu yang benar-benar dihadapi
  // orang sekarang; sisanya menunggu di belakangnya. Jalan pintas ke Pengaturan
  // ditempel di situ saja -- tawaran yang sama persis diulang tiga kali di satu
  // layar berhenti terbaca sebagai tawaran, dan mulai terbaca sebagai bujukan
  // untuk melewati jalurnya.
  const pintu = daftar.find((x) => x.status === "terkunci");
  const sedang = daftar.find((x) => x.status === "terbuka");

  return (
    <div>
      {ringkas}
      <PetaBab daftar={daftar} sedang={sedang} tingkat={tingkat}
               onBuka={bukaBab} />
      <SaringBab
        daftar={daftar}
        tingkat={tingkat}
        pilih={pilih}
        setPilih={setPilih}
      />
      <div className="bab-daftar">
        {daftar.map((bab) => {
          // Yang terbuka cuma bab yang sedang dikerjakan -- dan kalau tidak ada
          // satu pun yang berstatus "terbuka" (semuanya tuntas), bab PERTAMA
          // yang dibuka supaya halaman ini tidak pernah tampil sebagai sebelas
          // kepala tanpa satu pun isi.
          const terbuka = bab === sedang || (!sedang && bab === daftar[0]);
          const lolos = pilih.size === 0 || pilih.has(bab.tingkat);
          return (
            <details
              key={bab.nomor}
              id={"bab-" + bab.nomor}
              className={
                "bab" +
                (bab.status === "terkunci"
                  ? " bab-terkunci"
                  : bab.status === "tuntas"
                    ? " bab-tuntas"
                    : "") +
                (bab === sedang ? " bab-kini" : "")
              }
              aria-label={`Bab ${bab.nomor}: ${bab.judul}`}
              data-tingkat={bab.tingkat}
              open={terbuka}
              hidden={!lolos}
            >
              <KepalaBab bab={bab} kini={bab === sedang} />
              {/* `.masuk-mandiri` (util CSS) dipakai apa adanya, bukan mesin
                  entrance kedua: ia `@starting-style` + `transition-behavior:
                  allow-discrete`, jadi di browser tanpa dukungan itu -- dan
                  saat gerak dimatikan -- isinya tetap muncul apa adanya, bukan
                  tertinggal pada opacity nol.

                  Bab yang SUDAH terbuka saat halaman digambar tidak
                  mendapatkannya: `@starting-style` juga menyala pada render
                  pertama, dan itu akan bertumpuk di atas koreografi masuk
                  `.bab` yang membungkusnya. */}
              <div className={"bab-isi" + (terbuka ? "" : " masuk-mandiri")}>
                {bab.status === "terkunci" ? (
                  <CatatanKunci bab={bab} tawarkan={bab === pintu} />
                ) : null}
                <div className="senarai">
                  {bab.materi
                    .map((i) => materi.get(i))
                    .filter((m): m is Materi => Boolean(m))
                    .map((m) => (
                      <BarisMateri key={m.indeks} kunci={b.key} m={m} />
                    ))}
                </div>
              </div>
            </details>
          );
        })}
      </div>
    </div>
  );
}

function DaftarKuis({ b }: { b: DataBahasa }) {
  // Diungkap saat tergulir, berurutan. `kunci` berisi PANJANG daftarnya:
  // kurikulum yang berganti berarti daftar baru yang pantas diungkap lagi,
  // sementara render ulang dengan isi yang sama tidak boleh menyembunyikan
  // lalu memunculkannya lagi di bawah mata orang yang sedang membaca.
  const ref = useUngkap<HTMLDivElement>({ per: 46, geser: 10 }, [b.kuis.length]);
  return (
    <div className="senarai" ref={ref}>
      {b.kuis.map((q) => {
        const persen = q.total_soal ? (q.terbaik / q.total_soal) * 100 : 0;
        const hari = selisihHari(q.jadwal);
        return (
          <a className="baris" key={q.indeks} href={`#/kuis/${b.key}/${q.indeks}`}>
            <span className="nomor">{q.indeks + 1}</span>
            <span
              className={
                "titik" +
                (q.pernah && q.terbaik === q.total_soal
                  ? " selesai"
                  : q.pernah
                    ? " sedang"
                    : "")
              }
            />
            <div className="isi">
              <div className="judul">{q.judul}</div>
              <div className="ket">
                {q.pernah
                  ? `Terbaik ${q.terbaik}/${q.total_soal} · ${q.percobaan}× dikerjakan` +
                    (q.terakhir_waktu ? ` · terakhir ${jamRamah(q.terakhir_waktu)}` : "")
                  : `${q.soal} soal · ` +
                    (q.siap
                      ? "semua materi yang diujinya sudah kamu baca"
                      : `${q.sisa_materi} materi yang diujinya belum dibaca`)}
              </div>
            </div>
            {q.jatuh_tempo ? (
              <span className="pil pil-ungu">saatnya diulang</span>
            ) : q.pernah && hari !== null && hari > 0 ? (
              <span className="pil sembunyi-hp">{`ulang ${hari} hari lagi`}</span>
            ) : null}
            {q.salah_tersisa ? (
              <span className="pil pil-salah">{`${q.salah_tersisa} masih salah`}</span>
            ) : null}
            {q.pernah ? (
              <span className="sembunyi-hp" style={{ width: "56px", flex: "none" }}>
                <Bilah persen={persen} kelas={persen >= 100 ? "tumbuh" : ""} />
              </span>
            ) : null}
          </a>
        );
      })}
    </div>
  );
}

function DaftarLatihan({ b }: { b: DataBahasa }) {
  // Diungkap saat tergulir, berurutan. `kunci` berisi PANJANG daftarnya:
  // kurikulum yang berganti berarti daftar baru yang pantas diungkap lagi,
  // sementara render ulang dengan isi yang sama tidak boleh menyembunyikan
  // lalu memunculkannya lagi di bawah mata orang yang sedang membaca.
  const ref = useUngkap<HTMLDivElement>({ per: 46, geser: 10 }, [b.latihan.length]);
  return (
    <div className="senarai" ref={ref}>
      {b.latihan.map((e) => (
        <a
          className={
            "baris" +
            (e.status === "lulus" || e.status === "manual" ? " selesai" : "") +
            (e.proyek ? " baris-proyek" : "")
          }
          key={e.indeks}
          href={`#/latihan/${b.key}/${e.indeks}`}
        >
          <span className="nomor">{e.indeks + 1}</span>
          <span
            className={
              "titik" +
              (e.status === "lulus" || e.status === "manual"
                ? " selesai"
                : e.status === "dibuka"
                  ? " sedang"
                  : "")
            }
          />
          <div className="isi">
            <div className="judul">{e.judul}</div>
            {e.status === "lulus" ? (
              <div className="ket">lulus dengan kodemu sendiri</div>
            ) : e.status === "manual" ? (
              <div className="ket">ditandai selesai manual</div>
            ) : !e.dinilai && e.alasan ? (
              <div className="ket">{e.alasan}</div>
            ) : null}
          </div>
          {e.proyek ? <span className="pil pil-nyala">PROYEK AKHIR</span> : null}
          <span className={"pil t-" + e.tingkat}>{e.tingkat}</span>
          {!e.dinilai ? (
            <span className="pil sembunyi-hp">tanpa nilai otomatis</span>
          ) : null}
        </a>
      ))}
    </div>
  );
}

/** Tab Bacaan: ringkasan Pustaka untuk satu kurikulum. Pilihan tautannya dan
 *  urutannya diputuskan `inti/pustaka.py`; layar ini cuma menambah jalan ke
 *  Pustaka lengkap. */
function DaftarBacaan({ b }: { b: DataBahasa }) {
  const p = b.pustaka;
  const semua = "#/pustaka?kurikulum=" + encodeURIComponent(b.key);
  if (!p.total) {
    return (
      <Keadaan
        jenis="kosong"
        judul={"Belum ada bacaan untuk " + b.label}
        ket="Pustaka tetap bisa dijelajah untuk bahasa dan topik lain."
        aksi={
          <a className="tbl tbl-hantu" href="#/pustaka">
            Buka Pustaka
          </a>
        }
      />
    );
  }
  const labelJenis = Object.fromEntries(p.per_jenis.map((j) => [j.jenis, j.label]));
  return (
    <div>
      <p className="baris-sisi" style={{ margin: "0 0 var(--s3)" }}>
        {`${angka(p.total)} tautan gratis untuk ${b.label}: buku, kursus, ` +
          "proyek, dan lainnya. Yang berbahasa Indonesia tampil lebih dulu."}
      </p>
      <div className="deret deret-rapat" style={{ marginBottom: "var(--s4)" }}>
        {p.per_jenis.map((j) => (
          <a
            key={j.jenis}
            className="tbl tbl-kecil tbl-hantu"
            href={semua + "&jenis=" + j.jenis}
          >
            {j.label}
            <span className="tab-jumlah">{angka(j.jumlah)}</span>
          </a>
        ))}
      </div>
      <div className="senarai">
        {p.pembuka.map((e, i) => (
          <BarisTautan key={i} entri={e} labelJenis={labelJenis} />
        ))}
      </div>
      <div className="deret" style={{ marginTop: "var(--s4)" }}>
        <a className="tbl tbl-pergi" href={semua}>
          <Ikon nama="pustaka" ukuran={17} />
          {`Semua ${angka(p.total)} bacaan ${b.label}`}
          <Ikon nama="lanjut" ukuran={15} />
        </a>
      </div>
    </div>
  );
}

/* ================================================================== layar */

export function Bahasa({
  kunciBahasa, tingkat, onKonteks,
}: {
  kunciBahasa: string;
  tingkat: Tingkat[];
  onKonteks: (k: Konteks | undefined) => void;
}) {
  const [b, setB] = useState<DataBahasa | null>(null);
  const [galat, setGalat] = useState("");
  // Tab terakhir diingat PER BAHASA: orang yang sedang mengerjakan latihan
  // Python tidak otomatis mau tab Latihan saat membuka HTML.
  const [tab, setTab] = useState<NamaTab>(
    () => (ingat("tab." + kunciBahasa) as NamaTab) || "materi",
  );

  useEffect(() => {
    setTab((ingat("tab." + kunciBahasa) as NamaTab) || "materi");
  }, [kunciBahasa]);

  useEffect(() => {
    let dibatalkan = false;
    setB(null);
    setGalat("");
    ambil<DataBahasa>("bahasa", { key: kunciBahasa })
      .then((d) => {
        if (dibatalkan) return;
        setB(d);
        onKonteks({
          balik: { label: "Dasbor", href: "#/dasbor" },
          bab: d.label,
          // Kalimat ringkas bab SENGAJA tidak ikut di sini walau muat. Ia sudah
          // berdiri di badan halaman, dan strip ini menyembunyikan bagian
          // tengahnya di layar sempit -- jadi menaruhnya di dua tempat berarti
          // mengulang di layar lebar dan menghilang di layar sempit,
          // dua-duanya salah untuk kalimat yang justru paling menerangkan
          // halaman ini.
          posisi: `${d.statistik.materi}/${d.statistik.total_materi} materi`,
          persen: d.statistik.persen,
        });
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, [kunciBahasa, onKonteks]);

  const rasi = useMemo(() => (b ? dariBahasa(b) : null), [b]);

  if (galat) {
    return (
      <Keadaan
        jenis="salah"
        judul="Halaman bahasa tidak terbaca"
        ket={galat}
        aksi={
          <a className="tbl" href="#/dasbor">
            Ke dasbor
          </a>
        }
      />
    );
  }
  if (!b || !rasi) return <div className="pusaran" aria-label="Memuat" />;

  const s = b.statistik;
  const belumSiap = !b.siap;
  const lanjut = pilihLanjut(b);

  return (
    <div className="masuk">
      <header className="kepala-besar kepala-bersampul">
        <div className="kepala-teks">
          <span className="mata">Bahasa</span>
          <h1>{b.label}</h1>
          <p className="kepala-sub">{kalimatBahasa(s)}</p>
          <div className="fakta">
            {faktaBahasa(s, b.siap, b.hilang).map((f) => (
              <div
                className={"fakta-butir" + (f.kurang ? " fakta-kurang" : "")}
                key={f.gambar}
              >
                <Ikon nama={f.gambar} ukuran={19} />
                <span>{f.teks}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="kepala-sampul kepala-rasi">
          <PetaRasi data={rasi} tinggi={250} />
        </div>
      </header>

      {lanjut ? (
        <KartuLanjut s={lanjut} kunci={kunciBahasa} />
      ) : (
        <Keadaan
          jenis="tuntas"
          gambar="selesai"
          judul="Tidak ada yang tersisa di sini."
          ket={
            "Materi, kuis, dan latihannya sudah kamu selesaikan semua. " +
            "Kuisnya akan muncul lagi sendiri saat waktunya diulang."
          }
        />
      )}

      {b.siap ? null : <BlokToolchain b={b} />}
      {b.catatan ? (
        <Keadaan gambar="bantuan" judul="Perlu diketahui" ket={b.catatan} />
      ) : null}

      <div className="deret tab-deret">
        {TAB.map((t) => {
          const ini = t === tab;
          return (
            <button
              key={t}
              type="button"
              // `.tbl-pilih`, bukan `.tbl-utama`. Tab yang sedang terbuka adalah
              // KEADAAN, bukan tindakan yang disarankan -- dan mewarnainya aksen
              // penuh membuat ia bersaing dengan kartu Lanjutkan yang justru
              // dimaksudkan untuk ditekan.
              className={"tbl " + (ini ? "tbl-pilih" : "tbl-hantu")}
              aria-pressed={ini}
              {...(belumSiap && t === "latihan"
                ? {
                    title:
                      "Latihan tetap bisa dibaca, tapi kodenya belum bisa " +
                      "dijalankan di mesin ini.",
                  }
                : {})}
              onClick={() => {
                setTab(t);
                ingat("tab." + kunciBahasa, t);
              }}
            >
              <Ikon nama={t === "bacaan" ? "pustaka" : ikonTipe(t)} ukuran={17} />
              {t[0]?.toUpperCase() + t.slice(1)}
              <span className="tab-jumlah">
                {t === "bacaan" ? b.pustaka.total : b[t].length}
              </span>
              {belumSiap && t === "latihan" ? (
                <PilBelumSiap hilang={b.hilang} />
              ) : null}
            </button>
          );
        })}
        {/* Dipisahkan dari empat tab di sebelahnya, dan sengaja BUKAN
            `.tbl-hantu`: dengan bentuk yang sama persis, ia terbaca sebagai
            "tab kelima yang sedang tidak aktif" -- padahal menekannya
            meninggalkan halaman ini. */}
        {b.tebak && b.siap ? (
          <a
            className="tbl tbl-pergi deret-kanan"
            href={"#/tebak/" + kunciBahasa}
            title="Latih membaca kode: tebak keluaran contoh materi yang sudah kamu baca"
          >
            <Ikon nama="kuis" ukuran={17} />
            Tebak keluaran
          </a>
        ) : null}
        <a
          className={"tbl tbl-pergi" + (b.tebak && b.siap ? "" : " deret-kanan")}
          href={"#/coba?bahasa=" + b.runner}
        >
          <Ikon nama="jalankan" ukuran={17} />
          {"Ruang coba " + b.label}
          {belumSiap ? <PilBelumSiap hilang={b.hilang} /> : null}
          <Ikon nama="lanjut" ukuran={15} />
        </a>
      </div>

      {tab === "kuis" ? (
        <DaftarKuis b={b} />
      ) : tab === "latihan" ? (
        <DaftarLatihan b={b} />
      ) : tab === "bacaan" ? (
        <DaftarBacaan b={b} />
      ) : (
        <DaftarMateri b={b} tingkat={tingkat} />
      )}
    </div>
  );
}
