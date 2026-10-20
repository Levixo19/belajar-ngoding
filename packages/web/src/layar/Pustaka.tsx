/* Layar Pustaka: 9.809 tautan belajar, bisa dicari dan disaring.
 *
 * Port `webapp/statik/js/layar-pustaka.js`. Dua aturan yang TIDAK boleh
 * berubah saat diport, dan keduanya mudah hilang di React:
 *
 * 1. **Keadaan penyaring tinggal di ALAMAT**, bukan di `useState`.
 *    `#/pustaka?kurikulum=python&jenis=buku`. Dengan begitu tautan "Lihat
 *    semua bacaan Python" dari halaman bahasa, tombol mundur browser, dan tab
 *    yang dibuka ulang semuanya mendarat di saringan yang sama. Memindahkannya
 *    ke state komponen akan membuat ketiganya berhenti bekerja, tanpa satu pun
 *    error.
 * 2. **Semua keputusan isi milik server** (`inti/pustaka.py` lewat
 *    `/api/pustaka`): urutan, cacah tiap penyaring, dan labelnya. Layar ini
 *    cuma menggambar. Menyaring ulang di sisi klien berarti dua definisi
 *    "cocok", dan cacah di tombol berhenti sesuai dengan isi daftarnya.
 *
 * Tautan keluar dibuka di tab baru dengan `rel="noopener noreferrer"`: halaman
 * di luar sana tidak boleh bisa menyentuh jendela aplikasi ini lewat
 * `window.opener`, dan alamat lokal aplikasi tidak perlu ikut terkirim.
 */

import { useEffect, useRef, useState } from "react";

import { ambil } from "../api.ts";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { angka, tandai, urlAman } from "../util.tsx";

const PENYARING = ["q", "kurikulum", "jenis", "bahasa", "sumber"] as const;
type NamaSaring = (typeof PENYARING)[number];
type Saring = Record<NamaSaring, string>;

interface Entri {
  url: string;
  judul: string;
  jenis: string;
  bahasa: string;
  catatan?: string;
  topik?: string[];
}

interface Sumber {
  kunci: string;
  nama: string;
  lisensi: string;
  atribusi: string;
  jumlah: number;
  repo?: string;
  commit?: string;
}

type Cacah = Record<string, number>;

interface Jawaban {
  hasil: Entri[];
  total: number;
  semua: number;
  halaman: number;
  per_halaman: number;
  segi: Record<string, Cacah>;
  label: Record<string, Record<string, string>>;
  sumber: Sumber[];
}

function alamat(saring: Saring): string {
  const q = new URLSearchParams();
  for (const k of PENYARING) if (saring[k]) q.set(k, saring[k]);
  const s = q.toString();
  return "#/pustaka" + (s ? "?" + s : "");
}

/** Satu baris tautan. Dipakai juga oleh tab Bacaan di halaman bahasa. */
export function BarisTautan({
  entri,
  labelJenis,
  kata,
}: {
  entri: Entri;
  labelJenis: Record<string, string>;
  kata?: string;
}) {
  const bagianKet = [entri.catatan || null, entri.topik?.[0] || null]
    .filter(Boolean)
    .join(" · ");
  const href = urlAman(entri.url);
  // Entri yang URL-nya tidak lolos pagar TIDAK digambar sebagai tautan. Ia
  // tetap ditampilkan -- menyembunyikannya membuat cacah di tombol penyaring
  // berhenti sesuai dengan isi daftarnya.
  const Tag = href ? "a" : "div";
  return (
    <Tag
      className="baris"
      {...(href
        ? {
            href,
            target: "_blank",
            rel: "noopener noreferrer",
            title: entri.url,
          }
        : {})}
    >
      <span className="pil pil-jenis">
        {labelJenis[entri.jenis] || entri.jenis}
      </span>
      <div className="isi">
        <div className="judul">{tandai(entri.judul, kata)}</div>
        {bagianKet ? <div className="ket">{tandai(bagianKet, kata)}</div> : null}
      </div>
      {entri.bahasa === "id" ? (
        <span className="pil pil-tumbuh">Indonesia</span>
      ) : null}
    </Tag>
  );
}

/** Deret tombol pilihan untuk satu penyaring.
 *
 *  Nilai bercacah nol TIDAK ditampilkan: tombol yang berujung "tidak ada
 *  hasil" adalah tombol yang berujung penolakan. */
function DeretPilihan({
  nama,
  nilaiKini,
  segi,
  label,
  ganti,
}: {
  nama: NamaSaring;
  nilaiKini: string;
  segi: Cacah;
  label: Record<string, string>;
  ganti: (ubah: Partial<Saring>) => void;
}) {
  const urutan = Object.keys(label).filter((k) => segi[k]);
  if (urutan.length < 2 && !nilaiKini) return null;
  const tombol = (nilai: string, teks: string, jumlah: number | null) => {
    const aktif = nilai === nilaiKini;
    return (
      <button
        key={nilai || "semua"}
        type="button"
        className={"tbl tbl-kecil " + (aktif ? "tbl-pilih" : "tbl-hantu")}
        aria-pressed={aktif}
        onClick={() => ganti({ [nama]: nilai } as Partial<Saring>)}
      >
        {teks}
        {jumlah !== null ? (
          <span className="tab-jumlah">{angka(jumlah)}</span>
        ) : null}
      </button>
    );
  };
  return (
    <div
      className="deret deret-rapat"
      role="group"
      aria-label={"Saring " + nama}
      style={{ marginBottom: "var(--s3)" }}
    >
      {tombol("", "Semua", null)}
      {urutan.map((k) => tombol(k, label[k] as string, segi[k] as number))}
    </div>
  );
}

function Pilihan({
  nama,
  nilaiKini,
  segi,
  label,
  teksSemua,
  ganti,
}: {
  nama: NamaSaring;
  nilaiKini: string;
  segi: Cacah;
  label: Record<string, string>;
  teksSemua: string;
  ganti: (ubah: Partial<Saring>) => void;
}) {
  return (
    <select
      aria-label={teksSemua}
      value={nilaiKini}
      // Lebar dipatok di sini, bukan di gaya.css: `select` bawaan aplikasi ini
      // selebar wadahnya, dan dua pilihan yang masing-masing merentang 1000 px
      // mendorong daftar tautan satu layar ke bawah.
      style={{ width: "auto", flex: "0 1 15rem", minWidth: 0 }}
      onChange={(e) => ganti({ [nama]: e.target.value } as Partial<Saring>)}
    >
      <option value="">{teksSemua}</option>
      {Object.keys(label)
        .filter((k) => segi[k] || k === nilaiKini)
        .map((k) => (
          <option key={k} value={k}>
            {`${label[k]} (${angka(segi[k] || 0)})`}
          </option>
        ))}
    </select>
  );
}

export function Pustaka({ params }: { params: URLSearchParams }) {
  const saring = {} as Saring;
  for (const k of PENYARING) saring[k] = params.get(k) ?? "";
  const kunciSaring = alamat(saring);

  const [data, setData] = useState<Jawaban | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [lanjutan, setLanjutan] = useState<Entri[]>([]);
  const [halaman, setHalaman] = useState(1);
  const [memuat, setMemuat] = useState(false);
  const medanRef = useRef<HTMLInputElement>(null);
  const [ketikan, setKetikan] = useState(saring.q);

  const ganti = (ubah: Partial<Saring>) => {
    globalThis.location.hash = alamat({ ...saring, ...ubah });
  };

  useEffect(() => {
    let dibatalkan = false;
    setData(null);
    setGalat(null);
    setLanjutan([]);
    setHalaman(1);
    const kirim: Record<string, string> = {};
    const sekarang = new URLSearchParams(kunciSaring.split("?")[1] ?? "");
    for (const k of PENYARING) {
      const v = sekarang.get(k);
      if (v) kirim[k] = v;
    }
    setKetikan(sekarang.get("q") ?? "");
    ambil<Jawaban>("pustaka", kirim)
      .then((d) => {
        if (!dibatalkan) {
          setData(d);
          setHalaman(d.halaman);
        }
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
    // `kunciSaring` dipakai sebagai dependensi, bukan objek `saring`: objek itu
    // dibuat baru setiap render, jadi memakainya langsung membuat efek ini
    // berjalan tanpa henti.
  }, [kunciSaring]);

  useEffect(() => {
    if (!("ontouchstart" in globalThis)) medanRef.current?.focus();
  }, []);

  if (galat) {
    return <Keadaan jenis="salah" judul="Gagal memuat Pustaka" ket={galat} />;
  }
  if (!data) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat tautan…</span>
      </div>
    );
  }

  const labelJenis = (data.label.jenis ?? {}) as Record<string, string>;
  const labelKurikulum = (data.label.kurikulum ?? {}) as Record<string, string>;
  const labelBahasa = (data.label.bahasa ?? {}) as Record<string, string>;
  const labelSumber = Object.fromEntries(
    data.sumber.map((s) => [s.kunci, s.nama]),
  );
  const kata = saring.q.trim();
  const semuaHasil = [...data.hasil, ...lanjutan];
  const tersisa = data.total - halaman * data.per_halaman;
  const adaSaringan = PENYARING.some((k) => saring[k]);
  const ringkas =
    data.total === data.semua
      ? `${angka(data.total)} tautan dari ${data.sumber.length} sumber.`
      : `${angka(data.total)} dari ${angka(data.semua)} tautan cocok.`;

  async function muatLagi() {
    setMemuat(true);
    try {
      const kirim: Record<string, string | number> = { hal: halaman + 1 };
      for (const k of PENYARING) if (saring[k]) kirim[k] = saring[k];
      const lanjut = await ambil<Jawaban>("pustaka", kirim);
      setLanjutan((d) => [...d, ...lanjut.hasil]);
      setHalaman(lanjut.halaman);
    } catch (e) {
      setGalat((e as Error).message);
    } finally {
      setMemuat(false);
    }
  }

  return (
    <div className="masuk">
      <header className="kepala">
        <span className="mata">Pustaka</span>
        <h1>Bacaan, kursus, dan proyek</h1>
        <p className="kepala-sub">
          Buku, kursus, tutorial, proyek praktik, peta belajar, dan API publik
          dari repo kurasi terbuka. Yang berbahasa Indonesia selalu tampil lebih
          dulu. Semua tautan dibuka di tab baru.
        </p>
      </header>

      <div className="deret" style={{ marginBottom: "var(--s4)" }}>
        <input
          ref={medanRef}
          // type "text", bukan "search": gaya medan isian aplikasi ini
          // menyasar input[type="text"], dan "search" tampil sebagai kotak
          // polos browser.
          type="text"
          enterKeyHint="search"
          value={ketikan}
          placeholder={`Cari di ${angka(data.semua)} tautan: judul, topik, penulis…`}
          aria-label="Cari di Pustaka"
          style={{ fontSize: "var(--t-baca)", flex: "1 1 18rem", minWidth: 0 }}
          onChange={(e) => setKetikan(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") ganti({ q: ketikan.trim() });
          }}
        />
        <button
          type="button"
          className="tbl tbl-utama"
          onClick={() => ganti({ q: ketikan.trim() })}
        >
          Cari
        </button>
        <Pilihan
          nama="kurikulum"
          nilaiKini={saring.kurikulum}
          segi={data.segi.kurikulum ?? {}}
          label={labelKurikulum}
          teksSemua="Semua kurikulum"
          ganti={ganti}
        />
        <Pilihan
          nama="sumber"
          nilaiKini={saring.sumber}
          segi={data.segi.sumber ?? {}}
          label={labelSumber}
          teksSemua="Semua sumber"
          ganti={ganti}
        />
      </div>

      <DeretPilihan
        nama="jenis"
        nilaiKini={saring.jenis}
        segi={data.segi.jenis ?? {}}
        label={labelJenis}
        ganti={ganti}
      />
      <DeretPilihan
        nama="bahasa"
        nilaiKini={saring.bahasa}
        segi={data.segi.bahasa ?? {}}
        label={labelBahasa}
        ganti={ganti}
      />

      <div className="baris-sisi" style={{ margin: "var(--s3) 0" }}>
        {ringkas}
        {adaSaringan ? (
          <a href="#/pustaka" style={{ marginLeft: "var(--s3)" }}>
            Hapus semua saringan
          </a>
        ) : null}
      </div>

      {data.total ? (
        <div>
          <div className="senarai">
            {semuaHasil.map((e, i) => (
              <BarisTautan
                key={`${e.url}-${i}`}
                entri={e}
                labelJenis={labelJenis}
                kata={kata}
              />
            ))}
          </div>
          {tersisa > 0 ? (
            <div className="deret" style={{ marginTop: "var(--s4)" }}>
              <button
                type="button"
                className="tbl tbl-hantu"
                disabled={memuat}
                onClick={muatLagi}
              >
                {`Tampilkan ${angka(Math.min(tersisa, data.per_halaman))} lagi`}
                <span className="tab-jumlah">{`sisa ${angka(tersisa)}`}</span>
              </button>
            </div>
          ) : null}
        </div>
      ) : (
        <Keadaan
          jenis="kosong"
          judul={
            kata ? `Tidak ada yang cocok dengan "${kata}"` : "Tidak ada tautan"
          }
          ket="Coba kata yang lebih pendek, atau hapus salah satu saringan."
        />
      )}

      <BlokSumber sumber={data.sumber} />
    </div>
  );
}

/** Lisensi dan atribusi tiap sumber.
 *
 *  Ini BUKAN hiasan: CC BY dan MIT mewajibkannya, dan pelajar berhak tahu dari
 *  mana tautan ini berasal. Membuangnya saat memport adalah pelanggaran
 *  lisensi, bukan penyederhanaan tampilan. */
function BlokSumber({ sumber }: { sumber: Sumber[] }) {
  return (
    <details className="bantuan-isi" style={{ marginTop: "var(--s7)" }}>
      <summary>Sumber dan lisensi</summary>
      <div className="senarai">
        {sumber.map((s) => {
          const href = urlAman(s.repo);
          const Tag = href ? "a" : "div";
          return (
            <Tag
              key={s.kunci}
              className="baris"
              {...(href
                ? { href, target: "_blank", rel: "noopener noreferrer" }
                : {})}
            >
              <span className="pil">{s.lisensi}</span>
              <div className="isi">
                <div className="judul">{`${s.nama} · ${angka(s.jumlah)} tautan`}</div>
                <div className="ket">
                  {s.atribusi +
                    (s.commit ? ` Dipanen dari commit ${s.commit}.` : "")}
                </div>
              </div>
            </Tag>
          );
        })}
      </div>
    </details>
  );
}
