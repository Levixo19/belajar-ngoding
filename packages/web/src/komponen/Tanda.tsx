/* Tombol bookmark dan tombol catatan, plus dialog catatannya.
 *
 * Port `tombolBookmark`, `tombolCatatan`, dan `bukaCatatan` dari
 * `webapp/statik/js/layar-belajar.js`. Keempat layar memakainya (pembaca
 * materi, ruang kerja latihan, halaman bahasa, layar kuis), jadi ia komponen
 * bersama -- bukan empat salinan yang suatu hari berbeda soal `aria-pressed`.
 *
 * Keduanya ikon-tombol, bukan tombol berteks: mereka berdiri di kepala halaman
 * bersebelahan, dan dua tombol berteks penuh di situ memakan lebar yang
 * seharusnya jadi milik judulnya.
 *
 * Keadaannya disampaikan TIGA hal sekaligus -- warna, ketebalan garis ikon, dan
 * `aria-pressed` -- bukan warna saja. Tombol yang cuma berubah warna adalah
 * tombol yang keadaannya hilang untuk mata yang sulit membedakan warna, dan
 * tidak pernah ada sama sekali untuk pembaca layar.
 */

import { useCallback, useEffect, useRef, useState } from "react";

import { ambil, kirim } from "../api.ts";
import { useFokusDialog } from "./fokus-dialog.ts";
import { Ikon } from "./Ikon.tsx";
import { PembungkusModal } from "./Jendela.tsx";
import { sorak } from "../sorak.tsx";
import { jamRamah } from "../waktu.ts";

export function TombolBookmark({
  kunciBahasa, tipe, indeks, awal,
}: {
  kunciBahasa: string;
  /** `"materi"` | `"kuis"` | `"latihan"` */
  tipe: string;
  indeks: number;
  awal: boolean;
}) {
  const [ada, setAda] = useState(awal);
  // Prop-nya jadi nilai AWAL saja; sesudah ditekan, yang berlaku jawaban
  // server. Menyinkronkannya terus-menerus berarti satu permintaan `/api/bahasa`
  // yang datang belakangan bisa mengembalikan tombolnya ke keadaan lama.
  useEffect(() => { setAda(awal); }, [awal, kunciBahasa, tipe, indeks]);

  const judul = ada ? "Hapus dari bookmark" : "Simpan ke bookmark";
  return (
    <button
      type="button"
      className={"ikon-tombol" + (ada ? " aktif" : "")}
      aria-pressed={ada}
      title={judul}
      aria-label={judul}

      onClick={async () => {
        try {
          const r = await kirim<{ bookmark: boolean }>(
            "bookmark", { key: kunciBahasa, tipe, indeks });
          setAda(r.bookmark);
          // Hanya saat DITANDAI. Melepas tanda tidak dirayakan -- perayaan
          // untuk membatalkan sesuatu membingungkan, bukan menyenangkan.
          sorak(r.bookmark ? "Masuk bookmark." : "Dihapus dari bookmark.",
                "", 1.8);
        } catch (e) {
          sorak((e as Error).message, "salah");
        }
      }}
    >
      <Ikon nama="bookmark" ukuran={19} tebal={ada ? 2.4 : 1.7} />
    </button>
  );
}

interface IsiCatatan { teks: string; diubah?: string | null }

/**
 * Tombol catatan plus dialognya.
 *
 * Catatan tinggal di BERKAS SENDIRI (`~/.belajar_ngoding_catatan.json`), bukan
 * menumpang di progres. Alasannya: `progress.reset()` ada dan orang
 * memakainya -- kalau catatan menumpang di situ, "kosongkan nilai Java"
 * diam-diam ikut membakar tulisan tangan penggunanya. Progres bisa dikumpulkan
 * lagi; catatan tidak.
 */
export function TombolCatatan({
  kunci, awal, judul,
}: {
  kunci: string;
  awal: { teks?: string } | null | undefined;
  judul: string;
}) {
  const [punya, setPunya] = useState(Boolean(awal && awal.teks));
  const [buka, setBuka] = useState(false);
  const [isi, setIsi] = useState<IsiCatatan | null>(null);
  const areaRef = useRef<HTMLTextAreaElement>(null);
  const kotakRef = useRef<HTMLDivElement>(null);
  const tutupDialog = useCallback(() => setBuka(false), []);
  useFokusDialog(kotakRef, tutupDialog, buka && Boolean(isi));
  // Orang membuka dialog ini untuk menulis, jadi kolomnya yang berfokus, bukan
  // tombol Tutup di kepala. Harus sesudah `useFokusDialog`: efek itu mencatat
  // tempat asal fokus lebih dulu, dan `autoFocus` bawaan React akan menjalankan
  // fokus sebelum pencatatan itu, sehingga fokus tidak kembali ke tombol catatan.
  useEffect(() => {
    if (buka && isi) areaRef.current?.focus();
  }, [buka, isi]);

  useEffect(() => { setPunya(Boolean(awal && awal.teks)); }, [awal, kunci]);

  const bukaDialog = async () => {
    try {
      const kini = await ambil<IsiCatatan>("catatan", { kunci });
      setIsi({ teks: kini.teks || "", diubah: kini.diubah ?? null });
      setBuka(true);
    } catch (e) {
      sorak((e as Error).message, "salah");
    }
  };

  const simpan = async () => {
    const teks = areaRef.current?.value ?? "";
    try {
      const hasil = await kirim<IsiCatatan>("catatan", { kunci, teks });
      setPunya(Boolean(hasil.teks));
      setBuka(false);
      sorak(hasil.teks ? "Catatan disimpan." : "Catatan dikosongkan.",
            "tumbuh", 2);
    } catch (e) {
      sorak((e as Error).message, "salah");
    }
  };

  const tip = punya ? "Catatanmu untuk halaman ini (tersimpan)"
    : "Tulis catatan untuk halaman ini";

  return (
    <>
      <button
        type="button"
        className={"ikon-tombol" + (punya ? " aktif" : "")}
        title={tip}
        aria-label={tip}

        onClick={() => { void bukaDialog(); }}
      >
        <Ikon nama="catatan" ukuran={19} tebal={punya ? 2.4 : 1.7} />
      </button>

      {/* Dialognya modal: tirai menutup layar, jadi tidak ada yang bisa
          diklik di belakangnya. Tanpa pembungkus ini ia tergambar inline di
          tengah kepala halaman. Kepala, badan, dan kaki dipisah seperti
          `Jendela.tsx`: badan yang menggulir, tombol kaki yang selalu terlihat. */}
      {buka && isi ? (
        <PembungkusModal onTutup={tutupDialog}>
          <div className="jendela" role="dialog" aria-modal="true"
               aria-label={"Catatan: " + judul} ref={kotakRef} tabIndex={-1}>
            <div className="jendela-kepala">
              <h2>{"Catatan: " + judul}</h2>
              <button type="button" className="ikon-tombol"
                      onClick={tutupDialog} title="Tutup (Esc)"
                      aria-label="Tutup">
                ✕
              </button>
            </div>
            <div className="jendela-badan">
              <p className="kepala-sub" style={{ margin: "0 0 var(--s3)" }}>
                Menuliskan ulang dengan bahasa sendiri adalah cara paling murah
                untuk tahu apakah kamu benar-benar paham.
              </p>
              <textarea
                ref={areaRef}
                aria-label={"Catatan pribadimu untuk " + judul}
                defaultValue={isi.teks}
                placeholder={"Tulis dengan kalimatmu sendiri: apa inti halaman "
                  + "ini, dan bagian mana yang tadi sempat membingungkan."}
                style={{ minHeight: "220px" }}
              />
              {isi.diubah ? (
                <div className="baris-sisi" style={{ marginTop: "var(--s2)" }}>
                  {"Terakhir diubah " + jamRamah(isi.diubah)}
                </div>
              ) : null}
            </div>
            <div className="jendela-kaki">
              <button type="button" className="tbl" onClick={tutupDialog}>
                Batal
              </button>
              <button type="button" className="tbl tbl-utama"
                      onClick={() => { void simpan(); }}>
                Simpan
              </button>
            </div>
          </div>
        </PembungkusModal>
      ) : null}
    </>
  );
}
