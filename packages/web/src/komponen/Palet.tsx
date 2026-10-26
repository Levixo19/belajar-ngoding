/* Palet perintah (Ctrl+K). Port blok `palet` dari
 * `webapp/statik/js/aplikasi.js`.
 *
 * Pencocok dan pengelompoknya tinggal di `palet-cari.ts` dan sudah diadu
 * dengan `aplikasi.js` (`uji/banding-palet.mjs`), jadi tidak ada urutan yang
 * bisa bergeser dari berkas ini.
 *
 * **Pola combobox APG**, dan arahnya mengikat: medan satu-satunya yang
 * memegang FOKUS, dan sorotan dikirim ke pembaca layar lewat
 * `aria-activedescendant`. Pola sebaliknya -- memindahkan fokus ke butirnya --
 * mencabut papan ketik dari medan pada ArrowDown pertama, dan huruf berikutnya
 * yang diketik mendarat di tempat yang bukan kotak pencarian.
 *
 * Satu sorotan, TIGA pembaca: kelas `.pilih` untuk mata, `aria-selected` untuk
 * pembaca layar yang menyusuri daftarnya sendiri, dan `aria-activedescendant`
 * untuk menyebut butir mana yang aktif. Yang terakhir DILEPAS saat tidak ada
 * butir, bukan dikosongkan: atribut yang ada tapi tidak menunjuk apa pun
 * terbaca sebagai sorotan yang hilang entah ke mana -- bukan sebagai daftar
 * yang memang kosong.
 */

import { useEffect, useMemo, useRef, useState } from "react";

import { ambil } from "../api.ts";
import { ingatJson } from "../lokal.ts";
import {
  daftarPerintah, kelompokkan, riwayatNaikkan, riwayatPotong, saringPerintah,
  type BahasaPalet, type ButirPalet, type ButirRiwayat,
} from "./palet-cari.ts";

/* Dua id yang dirujuk kontrak combobox, ditulis sekali supaya tidak ada
   rumusan kedua yang bisa melenceng. `ID_LISTBOX` jadi sasaran `aria-controls`
   di medan; tiap butir dapat `PRA_OPSI + indeks` supaya
   `aria-activedescendant` punya sesuatu untuk ditunjuk. Rujukan id yang tidak
   ada di DOM bukan error di mana pun -- ia cuma dibacakan pembaca layar
   sebagai "tidak ada apa-apa yang terpilih", tepat ketika sesuatu terpilih. */
const ID_LISTBOX = "palet-list";
const PRA_OPSI = "palet-opt-";

/** Jeda sebelum kueri dikirim ke `/api/cari`. */
const JEDA_CARI_MS = 220;

/** Panjang kueri minimal sebelum isi kurikulum ikut dicari. */
const MIN_CARI = 2;

/** Berapa banyak hasil isi yang ikut ditampilkan. */
const MAKS_ISI = 40;

interface HasilCari {
  tipe: string;
  bahasa: string;
  label_bahasa: string;
  indeks: number;
  judul: string;
  cuplikan?: string;
}

export function Palet({
  bahasa, onTutup,
}: {
  bahasa: BahasaPalet[];
  onTutup: () => void;
}) {
  const perintah = useMemo(() => daftarPerintah(bahasa), [bahasa]);
  const [kata, setKata] = useState("");
  const [isi, setIsi] = useState<ButirPalet[]>([]);
  const [pilihan, setPilihan] = useState(0);
  const medanRef = useRef<HTMLInputElement>(null);
  const hasilRef = useRef<HTMLUListElement>(null);
  const butirRef = useRef<Array<HTMLLIElement | null>>([]);

  /* Jam dibaca SEKALI per palet yang dibuka, dan ingatannya dipotong sekali di
     tempat yang sama. Dua hal yang dicegah oleh "sekali di sini" alih-alih "di
     dalam pencocok": batas umur yang berbeda antara dua ketukan papan ketik,
     dan pembacaan ingatan yang berulang pada tiap huruf.
     
     `ingatJson`, bukan `ingat`: kuncinya DIBAGI dengan antarmuka lama, dan di
     sana nilainya sebuah array yang diurai sekali. Lihat komentar
     `ingatJson()` di `lokal.ts` -- nilai tersandi ganda dari sini akan
     membuat palet antarmuka lama melempar.
     
     `Array.isArray` bukan kehati-hatian berlebihan: yang tersimpan bisa
     berasal dari versi lain, dan `riwayatPotong` yang murni tetap menuntut
     daftar. Yang menerjemahkan ketiadaan cuma satu tempat: di sini. */
  const riwayat = useMemo<ButirRiwayat[]>(() => {
    const mentah = ingatJson<ButirRiwayat[]>("palet-riwayat");
    return riwayatPotong(Array.isArray(mentah) ? mentah : [], Date.now());
  }, []);

  /* Isi kurikulum dicari TERTUNDA, dan hasilnya disimpan terpisah dari
     perintah: perintah tetap di atas, karena kalau kamu mengetik "python" yang
     kamu maksud hampir pasti bahasanya -- bukan salah satu dari puluhan materi
     yang kebetulan menyebut kata itu. */
  useEffect(() => {
    const k = kata.trim();
    if (k.length < MIN_CARI) {
      setIsi([]);
      return;
    }
    let dibatalkan = false;
    const jam = setTimeout(() => {
      ambil<{ hasil: HasilCari[] }>("cari", { q: k })
        .then((r) => {
          if (dibatalkan) return;
          setIsi(
            r.hasil.slice(0, MAKS_ISI).map((x) => ({
              label: `${x.label_bahasa} · ${x.judul}`,
              ...(x.cuplikan ? { ket: x.cuplikan } : {}),
              tipe: x.tipe,
              href: `#/${x.tipe}/${x.bahasa}/${x.indeks}`,
            })),
          );
        })
        .catch(() => {
          /* biarkan hasil perintah yang sudah tampil */
        });
    }, JEDA_CARI_MS);
    return () => {
      dibatalkan = true;
      clearTimeout(jam);
    };
  }, [kata]);

  /* `baris` mengikuti urutan TERKELOMPOK, bukan urutan masukan. Kalau tidak,
     indeks papan ketik dan urutan di layar jadi dua susunan berbeda -- dan yang
     terjadi bukan error melainkan ArrowDown yang memindahkan sorotan ke tempat
     yang tidak ada hubungannya dengan tempat sorotan tadi berdiri. */
  const rombongan = useMemo(
    () => kelompokkan([...saringPerintah(perintah, kata.trim(), riwayat), ...isi]),
    [perintah, kata, riwayat, isi],
  );
  const baris = useMemo(() => rombongan.flatMap((r) => r.isi), [rombongan]);

  // Sorotan kembali ke atas setiap kali daftarnya berganti: indeks lama
  // menunjuk baris yang sudah bukan itu lagi.
  useEffect(() => setPilihan(0), [kata, isi]);

  useEffect(() => {
    medanRef.current?.focus();
  }, []);

  /** Padanan `bawaKeTengah()` di pembaca materi, dikerutkan ke satu arah: yang
   *  disentuh cuma `scrollTop` wadah hasil. `scrollIntoView` menggulir SEMUA
   *  leluhur yang bisa digulir, termasuk dokumen di belakang tirai -- jadi
   *  menahan ArrowDown memindahkan halaman yang sedang dibaca, dan yang
   *  terlihat sesudah palet ditutup bukan lagi tempat orang
   *  meninggalkannya. */
  useEffect(() => {
    const el = butirRef.current[pilihan];
    const wadah = hasilRef.current;
    if (!el || !wadah) return;
    const kotak = el.getBoundingClientRect();
    const luar = wadah.getBoundingClientRect();
    if (kotak.top < luar.top) wadah.scrollTop -= luar.top - kotak.top;
    else if (kotak.bottom > luar.bottom) {
      wadah.scrollTop += kotak.bottom - luar.bottom;
    }
  }, [pilihan, baris]);

  const buka = (d: ButirPalet) => {
    onTutup();
    globalThis.location.hash = d.href;
    // Dicatat SESUDAH bernavigasi, dan jamnya dibaca ULANG -- bukan jam saat
    // palet dibuka: palet yang dibuka lalu didiamkan sepuluh menit mencatat
    // saat ia DIPAKAI, bukan saat ia dibuka. Yang disimpan hasil pemotongan di
    // atas, jadi butir yang sudah kedaluwarsa tidak pernah dituliskan kembali.
    ingatJson("palet-riwayat", riwayatNaikkan(riwayat, d.href, Date.now()));
  };

  const tekan = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "ArrowDown" || (e.ctrlKey && e.key === "n")) {
      e.preventDefault();
      setPilihan((i) => Math.min(i + 1, baris.length - 1));
    } else if (e.key === "ArrowUp" || (e.ctrlKey && e.key === "p")) {
      e.preventDefault();
      setPilihan((i) => Math.max(i - 1, 0));
    } else if (e.key === "Home") {
      e.preventDefault();
      setPilihan(0);
    } else if (e.key === "End") {
      e.preventDefault();
      setPilihan(Math.max(baris.length - 1, 0));
    } else if (e.key === "Enter") {
      const d = baris[pilihan];
      if (d) {
        e.preventDefault();
        buka(d);
      }
    } else if (e.key === "Escape") {
      e.preventDefault();
      onTutup();
    }
  };

  let nomor = -1;
  return (
    <div
      className="jendela"
      role="dialog"
      aria-modal="true"
      // Tanpa nama, pembaca layar cuma mendengar "Dialog" -- dan palet ini
      // dibuka dengan Ctrl+K justru oleh orang yang tidak sedang melihat
      // layarnya.
      aria-label="Palet perintah"
    >
      <h2>Palet perintah</h2>
      <input
        ref={medanRef}
        className="palet-cari"
        type="text"
        value={kata}
        placeholder="Ke mana? Ketik nama bahasa, materi, atau apa pun…"
        aria-label="Cari perintah atau isi"
        role="combobox"
        aria-expanded={baris.length > 0}
        aria-controls={ID_LISTBOX}
        aria-autocomplete="list"
        {...(baris[pilihan] ? { "aria-activedescendant": PRA_OPSI + pilihan } : {})}
        onChange={(e) => setKata(e.target.value)}
        onKeyDown={tekan}
      />
      {/* Satu nama untuk listbox-nya. APG tidak menuntutnya, tapi tanpa itu
          susur daftar di pembaca layar berbunyi "daftar, satu dari dua puluh
          lima" tanpa sepatah pun soal daftar APA -- dan sebuah daftar yang
          tidak bisa disebut adalah daftar yang tidak bisa dirujuk lagi sesudah
          fokus berpindah. */}
      <ul
        ref={hasilRef}
        className="palet-hasil"
        id={ID_LISTBOX}
        role="listbox"
        aria-label="Hasil palet perintah"
      >
        {baris.length ? (
          rombongan.map((r) => (
            <li className="palet-grup" role="presentation" key={r.label}>
              {r.label}
              {/* Penanda rombongan BUKAN sebuah opsi, jadi ia tidak pernah
                  masuk ke `baris` -- tiga mesin membaca array itu dan
                  ketiganya menghitung OPSI, bukan baris di layar. Satu
                  penanda yang ikut masuk berarti satu indeks yang menunjuk
                  baris yang tidak bisa dibuka, dan yang terlihat bukan error
                  melainkan sorotan yang menghilang satu ketukan lalu `Enter`
                  yang diam.

                  Karena itu butirnya digambar sebagai `<ul>` bersarang di
                  dalam penandanya: satu induk per rombongan, dan indeks
                  papan ketik tetap menghitung opsi saja. */}
              <ul role="group" aria-label={r.label}>
                {r.isi.map((d) => {
                  nomor += 1;
                  const i = nomor;
                  return (
                    <li
                      key={d.href + i}
                      ref={(el) => {
                        butirRef.current[i] = el;
                      }}
                      className={"palet-item" + (i === pilihan ? " pilih" : "")}
                      id={PRA_OPSI + i}
                      role="option"
                      aria-selected={i === pilihan}
                      onClick={() => buka(d)}
                      onMouseMove={() => setPilihan(i)}
                    >
                      <span
                        className={
                          "pil" +
                          (d.tipe === "kuis"
                            ? " pil-ungu"
                            : d.tipe === "latihan"
                              ? " pil-nyala"
                              : d.tipe === "materi"
                                ? " pil-tenang"
                                : "")
                        }
                      >
                        {d.tipe || "buka"}
                      </span>
                      <div className="isi">
                        <div className="judul">{d.label}</div>
                        {d.ket ? <div className="cuplik">{d.ket}</div> : null}
                      </div>
                      {d.pintasan ? <kbd>{d.pintasan}</kbd> : null}
                    </li>
                  );
                })}
              </ul>
            </li>
          ))
        ) : (
          <li className="palet-kosong" role="presentation">
            Tidak ada yang cocok.
          </li>
        )}
      </ul>
      <div className="palet-kaki">
        <span>
          <kbd>↑↓</kbd> pilih
        </span>
        <span>
          <kbd>Home/End</kbd> ujung
        </span>
        <span>
          <kbd>⏎</kbd> buka
        </span>
        <span>
          <kbd>Esc</kbd> tutup
        </span>
      </div>
    </div>
  );
}
