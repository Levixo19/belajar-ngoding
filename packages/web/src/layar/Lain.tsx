/* Tiga layar daftar: Bookmark, Catatanku, dan Cari.
 *
 * Port `layarBookmark`, `layarCatatan`, dan `layarCari` dari
 * `webapp/statik/js/layar-belajar.js`. Ketiganya "gambar apa yang dikatakan
 * server" -- urutan, cuplikan, skor relevansi, dan penanda terkunci semuanya
 * datang jadi dari `webapp/api.py`. Karena itu ketiganya TIDAK punya lapisan
 * murni yang layak diadu dengan pembanding sendiri, sama dengan Pustaka,
 * Statistik, dan Pengaturan: yang bisa salah di sini bentuk elemennya, dan
 * yang menangkap itu memuatnya di peramban, bukan rekaman.
 *
 * Tiga aturan yang dibawa utuh:
 *
 * 1. **Keadaan pencarian tinggal di ALAMAT**, bukan di `useState`.
 *    `#/cari?q=pointer&tipe=materi`. Dengan begitu tombol mundur browser, tab
 *    yang dibuka ulang, dan tautan "Cari isi lain" dari antrean dasbor
 *    semuanya mendarat di hasil yang sama. `&tipe=` sengaja TIDAK ditulis
 *    untuk "semua", supaya alamat terpendeknya tetap bersih.
 * 2. **Penanda "terkunci" dipasang SEBELUM diklik.** Tautannya sengaja tetap
 *    hidup: menekannya mendarat di layar yang menjelaskan apa yang kurang, dan
 *    itu jawaban yang lebih berguna daripada baris yang tidak bisa ditekan
 *    sama sekali. Yang tidak boleh terjadi cuma satu -- orang mengklik tanpa
 *    satu pun isyarat lebih dulu.
 * 3. **Catatan tinggal di berkasnya sendiri** (`~/.belajar_ngoding_catatan.json`),
 *    dan kalimat di kepala layarnya mengatakan itu. Alasannya:
 *    `progress.reset()` ada dan orang memakainya -- kalau catatan menumpang di
 *    berkas progres, "kosongkan nilai Java" diam-diam ikut membakar tulisan
 *    tangan penggunanya. Progres bisa dikumpulkan lagi; catatan tidak.
 */

import { useEffect, useRef, useState } from "react";

import { ambil, kirim } from "../api.ts";
import { Ikon } from "../komponen/Ikon.tsx";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { sorak } from "../sorak.tsx";
import { tandai } from "../util.tsx";
import { jamRamah } from "../waktu.ts";
import { PilJenis } from "./Dasbor.tsx";

/* ============================================================== bookmark */

interface EntriBookmark {
  tipe: string;
  bahasa: string;
  label_bahasa: string;
  indeks: number;
  judul: string;
}

export function Bookmark() {
  const [d, setD] = useState<{ daftar: EntriBookmark[]; basi: number } | null>(null);
  const [galat, setGalat] = useState("");
  const [putaran, setPutaran] = useState(0);

  useEffect(() => {
    let dibatalkan = false;
    ambil<{ daftar: EntriBookmark[]; basi: number }>("bookmark")
      .then((x) => {
        if (!dibatalkan) setD(x);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, [putaran]);

  return (
    <div className="masuk">
      <header className="kepala-besar">
        <div className="kepala-teks">
          <span className="mata">Tersimpan</span>
          <h1>Bookmark</h1>
          <p className="kepala-sub">Halaman yang kamu tandai untuk dibuka lagi.</p>
        </div>
      </header>

      {galat ? (
        <Keadaan jenis="salah" gambar="belum" judul="Bookmark tidak terbaca" ket={galat} />
      ) : !d ? (
        <div className="pusaran" aria-label="Memuat" />
      ) : (
        <>
          {d.daftar.length ? (
            <div className="senarai">
              {d.daftar.map((x, i) => (
                <a
                  key={i}
                  className="baris"
                  href={`#/${x.tipe}/${x.bahasa}/${x.indeks}`}
                >
                  <PilJenis tipe={x.tipe} />
                  <div className="isi">
                    <div className="judul">{x.judul}</div>
                    <div className="ket">{x.label_bahasa}</div>
                  </div>
                  <span className="baris-panah">
                    <Ikon nama="lanjut" ukuran={18} />
                  </span>
                </a>
              ))}
            </div>
          ) : (
            <Keadaan
              jenis="kosong"
              judul="Belum ada bookmark"
              ket={
                "Buka materi, kuis, atau latihan mana pun, lalu tekan ikon pita " +
                "di kepala halamannya."
              }
              aksi={
                <a className="tbl tbl-utama" href="#/dasbor">
                  Ke dasbor
                </a>
              }
            />
          )}

          {/* Bookmark BASI tidak dihapus sendiri, dan itu bukan kelalaian:
              judul yang berubah karena kurikulumnya diperbarui bisa saja
              kembali, dan yang menghapus tanda orang lain tanpa diminta
              adalah aplikasi yang berhenti dipercaya. Yang ditawarkan satu
              tombol, beserta sebabnya. */}
          {d.basi ? (
            <Keadaan
              jenis="kunci"
              judul={`${d.basi} bookmark menunjuk halaman yang sudah tidak ada`}
              ket="Biasanya karena kurikulumnya diperbarui dan judulnya berubah."
              aksi={
                <button
                  type="button"
                  className="tbl tbl-kecil"
                  onClick={() => {
                    void (async () => {
                      try {
                        const r = await kirim<{ dibuang: number }>(
                          "bookmark/bersihkan", {});
                        sorak(`${r.dibuang} bookmark basi dibuang.`, "tumbuh");
                        setPutaran((n) => n + 1);
                      } catch (e) {
                        sorak((e as Error).message, "salah");
                      }
                    })();
                  }}
                >
                  Bersihkan
                </button>
              }
            />
          ) : null}
        </>
      )}
    </div>
  );
}

/* =============================================================== catatan */

interface EntriCatatan {
  kunci: string;
  tipe: string;
  bahasa: string;
  label_bahasa: string;
  indeks: number;
  judul: string;
  teks: string;
  diubah: string;
  basi?: boolean;
}

export function Catatan() {
  const [d, setD] = useState<{ daftar: EntriCatatan[] } | null>(null);
  const [galat, setGalat] = useState("");
  const [putaran, setPutaran] = useState(0);
  const [ubah, setUbah] = useState<EntriCatatan | null>(null);
  const areaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    let dibatalkan = false;
    ambil<{ daftar: EntriCatatan[] }>("catatan/semua")
      .then((x) => {
        if (!dibatalkan) setD(x);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, [putaran]);

  const simpan = async () => {
    if (!ubah) return;
    try {
      const hasil = await kirim<{ teks: string }>("catatan", {
        kunci: ubah.kunci,
        teks: areaRef.current?.value ?? "",
      });
      setUbah(null);
      setPutaran((n) => n + 1);
      sorak(hasil.teks ? "Catatan disimpan." : "Catatan dikosongkan.", "tumbuh", 2);
    } catch (e) {
      sorak((e as Error).message, "salah");
    }
  };

  return (
    <div className="masuk">
      <header className="kepala-besar">
        <div className="kepala-teks">
          <span className="mata">Milikmu sendiri</span>
          <h1>Catatanku</h1>
          <p className="kepala-sub">
            Menuliskan ulang dengan bahasamu sendiri adalah cara paling murah
            untuk tahu apakah kamu benar-benar paham. Disimpan terpisah dari
            progres, jadi menghapus progres tidak ikut menghapus tulisanmu.
          </p>
        </div>
      </header>

      {galat ? (
        <Keadaan jenis="salah" gambar="belum" judul="Catatan tidak terbaca" ket={galat} />
      ) : !d ? (
        <div className="pusaran" aria-label="Memuat" />
      ) : d.daftar.length ? (
        <div className="senarai">
          {d.daftar.map((x) => (
            <div className="kartu" key={x.kunci}>
              <div className="deret" style={{ marginBottom: "var(--s3)" }}>
                {/* Catatan yang halamannya hilang tetap DITAMPILKAN, cuma
                    tanpa tautan: isinya tulisan tangan orang, dan satu-satunya
                    hal yang lebih buruk daripada tautan mati adalah catatan
                    yang ikut hilang bersamanya. */}
                {x.basi ? (
                  <span className="pil pil-salah">halaman sudah tidak ada</span>
                ) : (
                  <a className="pil" href={`#/${x.tipe}/${x.bahasa}/${x.indeks}`}>
                    {`${x.label_bahasa} · ${x.judul}`}
                  </a>
                )}
                <span className="deret-kanan baris-sisi">{jamRamah(x.diubah)}</span>
                <button
                  type="button"
                  className="tbl tbl-kecil tbl-hantu"
                  onClick={() => setUbah(x)}
                >
                  Ubah
                </button>
              </div>
              <div className="par" style={{ margin: 0, color: "var(--teks-2)" }}>
                {x.teks}
              </div>
            </div>
          ))}
        </div>
      ) : (
        <Keadaan
          jenis="kosong"
          judul="Belum ada catatan"
          ket="Buka materi mana pun, lalu tekan ikon pena di kepala halamannya."
        />
      )}

      {ubah ? (
        <div
          className="jendela"
          role="dialog"
          aria-modal="true"
          aria-label={"Catatan: " + ubah.judul}
        >
          <h2>{"Catatan: " + ubah.judul}</h2>
          <p className="kepala-sub" style={{ margin: "0 0 var(--s3)" }}>
            Menuliskan ulang dengan bahasa sendiri adalah cara paling murah
            untuk tahu apakah kamu benar-benar paham.
          </p>
          <textarea
            ref={areaRef}
            aria-label={"Catatan pribadimu untuk " + ubah.judul}
            defaultValue={ubah.teks}
            style={{ minHeight: "220px" }}
          />
          <div className="baris-sisi" style={{ marginTop: "var(--s2)" }}>
            {"Terakhir diubah " + jamRamah(ubah.diubah)}
          </div>
          <div className="deret" style={{ marginTop: "var(--s3)" }}>
            <span className="deret-kanan" />
            <button type="button" className="tbl" onClick={() => setUbah(null)}>
              Batal
            </button>
            <button
              type="button"
              className="tbl tbl-utama"
              onClick={() => {
                void simpan();
              }}
            >
              Simpan
            </button>
          </div>
        </div>
      ) : null}
    </div>
  );
}

/* ================================================================== cari */

interface HasilCari {
  tipe: string;
  bahasa: string;
  label_bahasa: string;
  indeks: number;
  judul: string;
  cuplikan?: string;
  terkunci?: boolean;
}

const TIPE_CARI = ["semua", "materi", "kuis", "latihan"] as const;

/** Panjang minimal kata yang dicari.
 *
 *  Dua, bukan satu: satu huruf cocok dengan hampir setiap materi di 32
 *  kurikulum, dan daftar seribu baris adalah jawaban yang sama tidak
 *  bergunanya dengan daftar kosong. */
const MIN_CARI = 2;

/** Alamat hasil pencarian. `&tipe=` sengaja TIDAK ditulis untuk "semua". */
function alamatCari(kata: string, tipe: string): string {
  return (
    "#/cari?q=" + encodeURIComponent(kata) + (tipe !== "semua" ? "&tipe=" + tipe : "")
  );
}

export function Cari({
  params, jumlahBahasa,
}: {
  params: URLSearchParams;
  jumlahBahasa: number;
}) {
  const kata = params.get("q") ?? "";
  const saring = params.get("tipe") ?? "semua";
  const [hasil, setHasil] = useState<HasilCari[] | null>(null);
  const [galat, setGalat] = useState("");
  const [ketikan, setKetikan] = useState(kata);
  const medanRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    setKetikan(kata);
  }, [kata]);

  useEffect(() => {
    if (kata.length < MIN_CARI) {
      setHasil([]);
      return;
    }
    let dibatalkan = false;
    setGalat("");
    ambil<{ hasil: HasilCari[] }>("cari", { q: kata, tipe: saring })
      .then((r) => {
        if (!dibatalkan) setHasil(r.hasil);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, [kata, saring]);

  // Kursor diletakkan di UJUNG teks, bukan di awal: orang yang sampai di sini
  // dari hasil sebelumnya hampir selalu mau MENAMBAH huruf, bukan mengganti
  // seluruh katanya.
  useEffect(() => {
    const m = medanRef.current;
    if (!m) return;
    m.focus();
    m.setSelectionRange(m.value.length, m.value.length);
  }, []);

  const buka = (k: string, t: string) => {
    globalThis.location.hash = alamatCari(k, t);
  };

  return (
    <div className="masuk">
      <header className="kepala-besar">
        <div className="kepala-teks">
          <span className="mata">Pencarian</span>
          <h1>Cari</h1>
          <p className="kepala-sub">
            Menjangkau judul, isi materi, soal kuis, dan solusi latihan di semua
            bahasa sekaligus. Mencari buku atau kursus?{" "}
            <a href={"#/pustaka" + (kata ? "?q=" + encodeURIComponent(kata) : "")}>
              Cari di Pustaka
            </a>
            .
          </p>
        </div>
      </header>

      <input
        ref={medanRef}
        type="text"
        value={ketikan}
        // Jumlah bahasanya DIHITUNG, tidak diketik: kalimat ini dulu berbunyi
        // "11 bahasa" dan tetap begitu sesudah kurikulumnya jadi tiga puluh dua.
        placeholder={
          jumlahBahasa
            ? `Cari di ${jumlahBahasa} bahasa sekaligus…`
            : "Cari di semua bahasa…"
        }
        aria-label="Kata yang dicari"
        style={{ fontSize: "var(--t-baca)" }}
        onChange={(e) => setKetikan(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") buka(ketikan, saring);
        }}
      />

      <div
        className="deret deret-rapat"
        style={{ margin: "var(--s4) 0 var(--s5)" }}
      >
        {TIPE_CARI.map((t) => (
          <button
            key={t}
            type="button"
            className={"tbl tbl-kecil " + (t === saring ? "tbl-pilih" : "tbl-hantu")}
            aria-pressed={t === saring}
            onClick={() => buka(ketikan, t)}
          >
            {t[0]?.toUpperCase() + t.slice(1)}
          </button>
        ))}
      </div>

      {galat ? (
        <Keadaan jenis="salah" gambar="belum" judul="Pencarian gagal" ket={galat} />
      ) : kata.length < MIN_CARI ? (
        <Keadaan
          jenis="kosong"
          judul="Ketik minimal dua huruf"
          ket="Coba: pointer, rekursi, JOIN, closure, malloc, interface."
        />
      ) : !hasil ? (
        <div className="pusaran" aria-label="Mencari" />
      ) : hasil.length ? (
        <div>
          <div className="baris-sisi" style={{ marginBottom: "var(--s3)" }}>
            {`${hasil.length} hasil untuk "${kata}"`}
          </div>
          <div className="senarai">
            {hasil.map((r, i) => (
              <a
                key={i}
                className="baris"
                href={`#/${r.tipe}/${r.bahasa}/${r.indeks}`}
              >
                <PilJenis tipe={r.tipe} />
                <div className="isi">
                  <div className="judul">{tandai(r.judul, kata)}</div>
                  <div className="ket">
                    {r.label_bahasa}
                    {r.cuplikan ? ": " : ""}
                    {r.cuplikan ? tandai(r.cuplikan, kata) : ""}
                  </div>
                </div>
                {r.terkunci ? <span className="pil pil-kunci">terkunci</span> : null}
              </a>
            ))}
          </div>
        </div>
      ) : (
        <Keadaan
          jenis="kosong"
          judul={`Tidak ada yang cocok dengan "${kata}"`}
          ket="Coba kata yang lebih pendek, atau matikan saringan tipe."
        />
      )}
    </div>
  );
}
