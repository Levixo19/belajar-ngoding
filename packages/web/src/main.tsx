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
import { Keadaan } from "./komponen/Keadaan.tsx";
import { Pustaka } from "./layar/Pustaka.tsx";
import { Tebak } from "./layar/Tebak.tsx";

interface Bahasa {
  key: string;
  label: string;
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

function Aplikasi() {
  const [awal, setAwal] = useState<Awal | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [alamat, setAlamat] = useState<Rute>(rute);

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

  if (galat) {
    return (
      <Keadaan
        jenis="salah"
        judul="Tidak bisa menghubungi server"
        ket={galat}
      />
    );
  }
  if (!awal) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat…</span>
      </div>
    );
  }

  const [nama, arg] = alamat.jalur;

  if (nama === "pustaka") {
    return <Pustaka params={alamat.params} />;
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
          Baru dua layar yang diport: Pustaka dan Tebak keluarannya. Sisanya
          masih di antarmuka lama, dan kedua-duanya memakai API serta berkas
          gaya yang sama.
        </p>
        <div className="deret">
          <a className="tbl tbl-utama" href="#/pustaka">
            Pustaka
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

createRoot(akar).render(
  <StrictMode>
    <div id="panggung">
      <main id="layar">
        <Aplikasi />
      </main>
    </div>
  </StrictMode>,
);
