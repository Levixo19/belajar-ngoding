/* Titik masuk React dan router hash.
 *
 * Masih sengaja KECIL. `webapp/statik/js/aplikasi.js` 1.570 baris karena ia
 * mengurus sembilan belas rute, kelas ukuran layar, strip konteks, panel
 * navigasi, dan koreografi pergantian layar. Memindahkan semuanya sekaligus
 * berarti satu lompatan besar yang tidak bisa dibandingkan dengan apa pun;
 * yang dikerjakan di sini satu layar lebih dulu, sampai polanya mapan.
 *
 * Yang SUDAH mengikat sejak sekarang:
 *
 * * Router memakai hash, sama seperti versi lama, supaya alamat yang sudah
 *   dibagikan atau di-bookmark pelajar tetap menunjuk tempat yang sama.
 * * Daftar bahasa dan labelnya datang dari `/api/awal`, tidak diketik. Kalimat
 *   atau menu yang menyebut "dua belas bahasa" adalah kalimat yang suatu hari
 *   berbohong tanpa satu pun tes gagal.
 */

import { StrictMode, useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

import { ambil } from "./api.ts";
import { Cangkang, type Konteks } from "./Cangkang.tsx";
import { Keadaan } from "./komponen/Keadaan.tsx";
import { Atur } from "./layar/Atur.tsx";
import { Karier } from "./layar/Karier.tsx";
import { Langit } from "./layar/Langit.tsx";
import { Pustaka } from "./layar/Pustaka.tsx";
import { Statistik } from "./layar/Statistik.tsx";
import { Belajar } from "./layar/Belajar.tsx";
import { Coba, Latihan } from "./layar/Kerja.tsx";
import { Tebak } from "./layar/Tebak.tsx";
import { ingat, terapkanTampilan } from "./lokal.ts";
import { Sorak } from "./sorak.tsx";

/* Medan yang dipakai router ini dari `/api/awal -> bahasa`. Ia sengaja
   TIDAK menyalin seluruh entri: yang ditambahkan di server tanpa dipakai
   di sini tidak perlu disebut, dan daftar yang menyebut semuanya akan
   memerahkan tipe setiap kali server menambah satu medan. Yang WAJIB ada
   cuma yang benar-benar dibaca -- `runner`/`sorot`/`siap` oleh Ruang Coba
   untuk menyaring toolchain yang terpasang. */
interface Bahasa {
  key: string;
  label: string;
  runner: string;
  sorot: string;
  siap: boolean;
}

interface Awal {
  bahasa: Bahasa[];
  versi: string;
}

interface Rute {
  /** Ruas jalur: `["bahasa", "python"]` dari `#/bahasa/python`. */
  jalur: string[];
  /** Parameter kueri di belakang hash. */
  params: URLSearchParams;
}

/**
 * Baca hash jadi jalur dan parameter.
 *
 * Parameter kueri ikut dibaca, dan itu bukan kelengkapan: layar Pustaka
 * menyimpan SELURUH keadaan penyaringnya di alamat
 * (`#/pustaka?kurikulum=python&jenis=buku`). Membuangnya di sini akan membuat
 * tautan "Lihat semua bacaan Python", tombol mundur browser, dan tab yang
 * dibuka ulang semuanya mendarat di saringan kosong -- tanpa satu pun error.
 */
function rute(): Rute {
  const hash = globalThis.location.hash.replace(/^#\/?/, "");
  const [jalurMentah, kueri] = hash.split("?");
  return {
    jalur: (jalurMentah ?? "").split("/").filter(Boolean),
    params: new URLSearchParams(kueri ?? ""),
  };
}

/**
 * Pembungkus: mengambil `/api/awal` sekali, mendengarkan `hashchange`, lalu
 * menyerahkan rute dan datanya ke cangkang beserta isinya.
 *
 * Dipisah dari `Isi` supaya kelas ukuran layar dan isi halaman berasal dari
 * SATU render yang sama. Di versi JS keduanya dua langkah terpisah, dan
 * menyetel kelasnya lebih dulu membuat layar lama yang masih terlihat melompat
 * melebar tepat sebelum memudar.
 */
function Aplikasi() {
  const [awal, setAwal] = useState<Awal | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [alamat, setAlamat] = useState<Rute>(rute);
  /* Strip konteks punya DUA sumber, dan itu bukan kelalaian.
     `konteksRute` menjawab dari ALAMATNYA -- sinkron, dan itu yang benar
     untuk rute yang judulnya memang sudah ada di hash. Ruang kerja
     latihan tidak: judul dan posisinya baru diketahui sesudah
     `/api/latihan` menjawab, jadi layarnya yang MELAPORKAN lewat
     `onKonteks`. Yang dilaporkan menang; yang dari alamat jadi jawaban
     sementara selama permintaannya belum sampai -- bukan strip kosong
     yang lalu melompat muncul. */
  const [konteksLayar, setKonteksLayar] =
    useState<Konteks | undefined>(undefined);

  /* Dikosongkan tiap kali alamatnya berganti. Tanpa ini, strip dari layar
     SEBELUMNYA masih terbaca di layar berikutnya sampai layar itu sempat
     melapor -- dan untuk rute yang tidak punya strip sama sekali, ia
     tidak pernah hilang. */
  useEffect(() => { setKonteksLayar(undefined); }, [alamat]);

  useEffect(() => {
    const dengar = () => setAlamat(rute());
    globalThis.addEventListener("hashchange", dengar);
    return () => globalThis.removeEventListener("hashchange", dengar);
  }, []);

  useEffect(() => {
    ambil<Awal>("awal")
      .then(setAwal)
      .catch((e: Error) => setGalat(e.message));
  }, []);

  const nama = alamat.jalur[0] ?? "dasbor";

  if (galat) {
    return (
      <Cangkang rute={nama}>
        <Keadaan
          jenis="salah"
          judul="Tidak bisa menghubungi server"
          ket={galat}
        />
      </Cangkang>
    );
  }
  if (!awal) {
    return (
      <Cangkang rute={nama}>
        <div className="deret">
          <div className="pusaran" />
          <span>Memuat…</span>
        </div>
      </Cangkang>
    );
  }
  return (
    <Cangkang rute={nama}
              konteks={konteksLayar ?? konteksRute(alamat, awal)}>
      <Isi alamat={alamat} awal={awal} onKonteks={setKonteksLayar} />
    </Cangkang>
  );
}

/**
 * Strip konteks untuk rute yang punya POSISI.
 *
 * Layar yang tidak punya posisi mengembalikan `undefined`, dan stripnya tidak
 * dirender sama sekali -- 44 piksel itu kembali jadi milik isinya.
 */
function konteksRute(alamat: Rute, awal: Awal): Konteks | undefined {
  const [nama, arg] = alamat.jalur;
  if (nama === "tebak" && arg) {
    const bhs = awal.bahasa.find((b) => b.key === arg);
    if (bhs) {
      return {
        balik: { label: bhs.label, href: "#/bahasa/" + bhs.key },
        bab: "Latih baca kode",
        judul: "Tebak keluarannya",
      };
    }
  }
  return undefined;
}

function Isi({
  alamat, awal, onKonteks,
}: {
  alamat: Rute;
  awal: Awal;
  onKonteks: (k: Konteks | undefined) => void;
}) {
  const [nama, arg, arg2] = alamat.jalur;

  if (nama === "pustaka") {
    return <Pustaka params={alamat.params} />;
  }

  if (nama === "langit") {
    return <Langit />;
  }

  if (nama === "statistik") {
    return <Statistik />;
  }

  if (nama === "atur") {
    return <Atur />;
  }

  if (nama === "karier") {
    return <Karier id={arg} />;
  }

  if (nama === "materi" && arg) {
    return (
      <Belajar
        kunciBahasa={arg}
        indeks={Number(arg2 ?? 0) || 0}
        onKonteks={onKonteks}
      />
    );
  }

  if (nama === "latihan" && arg) {
    return (
      <Latihan
        kunciBahasa={arg}
        indeks={Number(arg2 ?? 0) || 0}
        onKonteks={onKonteks}
      />
    );
  }

  if (nama === "coba") {
    return (
      <Coba
        bahasaAwal={awal.bahasa}
        params={{
          ...(alamat.params.get("bahasa")
            ? { bahasa: alamat.params.get("bahasa") as string } : {}),
          ...(alamat.params.get("key")
            ? { key: alamat.params.get("key") as string } : {}),
          ...(alamat.params.get("materi") !== null
            ? { materi: alamat.params.get("materi") as string } : {}),
          ...(alamat.params.get("bagian") !== null
            ? { bagian: alamat.params.get("bagian") as string } : {}),
        }}
        ingat={ingat}
      />
    );
  }

  if (nama === "tebak" && arg) {
    const bhs = awal.bahasa.find((b) => b.key === arg);
    if (!bhs) {
      return (
        <Keadaan
          jenis="kosong"
          judul="Kurikulum tidak dikenal"
          ket={`Tidak ada kurikulum dengan kunci "${arg}".`}
          aksi={
            <a className="tbl" href="#/">
              Ke daftar kurikulum
            </a>
          }
        />
      );
    }
    return <Tebak bahasaKey={bhs.key} label={bhs.label} />;
  }

  // Beranda sementara: daftar kurikulum yang punya layar Tebak. Ia akan
  // digantikan dasbor saat layar itu diport; sampai itu terjadi, halaman ini
  // tetap harus bisa mengantar ke SESUATU -- halaman kosong yang cuma berisi
  // judul adalah halaman yang membuat orang mengira aplikasinya rusak.
  return (
    <div>
      <header className="kepala">
        <span className="mata">belajar-codingV2 · versi {awal.versi}</span>
        <h1>Antarmuka React</h1>
        <p className="kepala-sub">
          Sembilan layar sudah diport: Langit, Peta Karier, Pustaka,
          Statistik, Pengaturan, Tebak keluarannya, Ruang Coba, ruang
          kerja latihan, dan pembaca materi. Yang tersisa dasbor, halaman
          bahasa, kuis, bookmark, catatan, dan pencarian. Kedua antarmuka
          memakai API serta berkas gaya yang sama.
        </p>
        <div className="deret">
          <a className="tbl tbl-utama" href="#/langit">
            Langit
          </a>
          <a className="tbl" href="#/pustaka">
            Pustaka
          </a>
          <a className="tbl" href="#/statistik">
            Statistik
          </a>
          <a className="tbl" href="#/karier">
            Peta Karier
          </a>
          <a className="tbl" href="#/coba">
            Ruang Coba
          </a>
          <a className="tbl" href="#/atur">
            Pengaturan
          </a>
        </div>
      </header>
      <div className="senarai">
        {awal.bahasa.map((b) => (
          <a key={b.key} className="baris" href={`#/tebak/${b.key}`}>
            <span className="baris-judul">{b.label}</span>
            <span className="mata">Tebak keluarannya</span>
          </a>
        ))}
      </div>
    </div>
  );
}

const akar = document.getElementById("akar");
if (!akar) throw new Error("#akar tidak ada di index.html");

/* Preferensi tampilan dipasang SEBELUM React menggambar apa pun. Kalau
   dipasang di dalam sebuah efek, halaman sempat tergambar satu frame dengan
   tema bawaan lebih dulu -- dan di tema terang itu berarti kilatan putih di
   wajah orang yang justru memilih tema gelap. */
terapkanTampilan();

createRoot(akar).render(
  <StrictMode>
    <Aplikasi />
    <Sorak />
  </StrictMode>,
);
