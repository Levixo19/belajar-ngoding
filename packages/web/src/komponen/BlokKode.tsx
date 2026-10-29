/* Blok kode di halaman materi: bisa dibaca, dijalankan, dan disunting DI TEMPAT.
 *
 * Port `blokKode` dan `kartuKeluaran` dari `webapp/statik/js/layar-belajar.js`.
 *
 * Tombolnya dulu melempar ke Ruang Coba: layar lain, alamat lain, dan kembali
 * berarti kehilangan posisi baca. Untuk pertanyaan sekecil "keluarnya apa kalau
 * ini dijalankan?", ongkos itu jauh lebih besar daripada pertanyaannya, dan
 * yang terjadi bukan orang membayarnya melainkan orang berhenti bertanya.
 *
 * Dua syarat tombol Jalankan, dan KEDUANYA jawaban server, bukan tebakan:
 * `bisa_dijalankan` dari `berkas.py` dan `siap` dari `runner.py`. Tombol yang
 * selalu berakhir dengan "belum terpasang" adalah tombol yang berujung
 * penolakan.
 *
 * Yang dipanggil `/api/coba`, yang memang tidak menyentuh progres sama sekali:
 * definisi "lulus" tetap cuma satu dan tempatnya `runner.periksa`.
 */

import { useMemo, useRef, useState } from "react";

import { kirim } from "../api.ts";
import { salin } from "../sorak.tsx";
import { Editor, type PeganganEditor } from "./Editor.tsx";
import { Ikon } from "./Ikon.tsx";
import { Jejak } from "./Jejak.tsx";
import { Kode } from "./Kode.tsx";
import { PohonBerkas } from "./PohonBerkas.tsx";
import { pecahBerkas } from "./pohon-teks.ts";
import { Pratinjau } from "./Pratinjau.tsx";
import {
  bisaDipratinjau, dokumenPratinjau, halamanDikarang,
} from "./pratinjau-css.ts";
import type { Token } from "../../../bersama/src/sorot.ts";

export interface Petunjuk {
  jenis: string;
  nama?: string;
  instruksi?: string;
  keterangan?: string;
  perintah: string[];
  bisa_dijalankan: boolean;
}

export interface BagianKode {
  jenis: "kode";
  /** Indeks DATA bagian ini (bukan indeks blok): yang dipahami `/api/materi/contoh`. */
  bagian?: number;
  judul?: string;
  kode: string;
  token: Token[];
  bahasa?: string;
  sorot?: string;
  siap?: boolean;
  petunjuk: Petunjuk;
}

interface HasilCoba {
  keluaran: string;
  galat: { mentah: string; baris: string[]; artinya: string[] } | null;
  kode_keluar: number;
  detik: number;
}

const LENCANA: Record<string, string> = {
  program: "berkas utuh", potongan: "potongan", sesi: "sesi",
  multi: "beberapa berkas", ilustrasi: "ilustrasi",
};

/* Kaki blok multi-berkas yang dipecah penampil. Petunjuk dari server ("pisahkan
   sesuai komentar penanda") tidak lagi benar di sini: penandanya sudah jadi
   baris pohon dan tidak terlihat di dalam kode. */
const KAKI_PECAH = "Tombol Salin di atas membawa semua berkas sekaligus beserta komentar "
  + "penandanya; tombol di kepala kode hanya membawa berkas yang sedang dibuka.";

/**
 * Kartu keluaran satu kali jalan.
 *
 * Untuk bahasa yang MENCETAK sesuatu, keluarannya memang teks dan kartunya cuma
 * membingkainya. Untuk HTML tidak: `struktur.py` mengubahnya jadi pohon elemen
 * karena mesin penilaian di sini bekerja dengan membandingkan keluaran, dan
 * HTML tidak punya keluaran. Pohon itu WAJIB tetap ada -- ia yang dinilai, dan
 * ia juga satu-satunya cara melihat apa yang sebenarnya terjadi pada markup
 * yang tag penutupnya lupa ditulis. Tapi ia jawaban untuk pertanyaan LAIN
 * daripada yang sedang ditanyakan orang yang baru saja mengetik
 * `<h1>Halo, Dunia!</h1>`.
 *
 * Jadi keduanya ditampilkan, dengan yang dicari lebih dulu: Tampilan di depan,
 * Struktur satu klik di sebelahnya.
 *
 * Keduanya tinggal di DOM dan cuma disembunyikan bergantian -- `hidden`, bukan
 * render bersyarat. Mencabut lalu memasang ulang `<iframe>` MEMUAT ULANG
 * dokumennya: halaman yang punya skrip akan menjalankannya lagi dari awal,
 * animasi mengulang, dan tingginya diukur ulang dari nol -- semua itu hanya
 * karena seseorang ingin mengintip pohon strukturnya sebentar lalu kembali.
 */
export function KartuKeluaran({
  r, runner, kode, onTutup,
}: {
  r: HasilCoba; runner: string; kode: string; onTutup: () => void;
}) {
  const [lihat, setLihat] = useState(true);
  const lulus = r.kode_keluar === 0;
  const dok = bisaDipratinjau(runner) && kode.trim()
    ? dokumenPratinjau(runner, kode) : "";
  const bisa = !!dok;
  const dikarang = bisa && halamanDikarang(runner, kode);

  return (
    <div className={"keluaran-kartu" + (lulus ? "" : " keluaran-salah")}>
      <div className="keluaran-kepala">
        <span className="mata">
          {!bisa ? "Keluaran" : dikarang ? "Hasilnya" : "Halamanmu"}
        </span>
        {bisa ? (
          <div className="keluaran-tab">
            <button
              type="button"
              className={"tbl tbl-kecil " + (lihat ? "tbl-pilih" : "tbl-hantu")}
              aria-pressed={lihat}
              onClick={() => setLihat(true)}
            >
              Tampilan
            </button>
            <button
              type="button"
              className={"tbl tbl-kecil " + (!lihat ? "tbl-pilih" : "tbl-hantu")}
              aria-pressed={!lihat}
              onClick={() => setLihat(false)}
            >
              Struktur
            </button>
          </div>
        ) : null}
        <span className="deret-kanan" />
        <span
          className={"pil" + (lulus ? " pil-tumbuh" : " pil-salah")}
          title="Kode keluar 0 berarti programnya selesai tanpa error. Angka lain berarti ia berhenti karena error."
        >
          {lulus ? "selesai tanpa error" : `berhenti dengan error (kode keluar ${r.kode_keluar})`}
        </span>
        <span className="pil">{r.detik + " detik"}</span>
        <button type="button" className="tbl tbl-kecil tbl-hantu"
                title="Tutup keluaran" onClick={onTutup}>
          Tutup
        </button>
      </div>
      <div className="keluaran-isi">
        {/* Halaman yang DIBUATKAN wajib mengaku. CSS tidak menggambar apa pun
            sendirian, jadi untuk blok CSS murni halamannya disusun dari pemilih
            di aturannya sendiri -- berguna, tapi bukan berkas milik siapa pun.
            Tanpa kalimat ini, yang terlihat adalah markup yang tidak pernah ia
            tulis dan tidak akan pernah ia temukan lagi di mana pun.

            Keterangannya menerangkan HALAMANNYA, bukan pohonnya; membiarkannya
            berdiri di atas daftar aturan membuatnya menerangkan hal yang
            salah. */}
        {dikarang ? (
          <p className="pratinjau-ket" hidden={!lihat}>
            Halaman contoh ini dibuatkan dari pemilih di CSS-mu sendiri:{" "}
            <b>bukan</b> berkas HTML-mu. Gunanya satu: melihat aturan mana
            mengenai apa.
          </p>
        ) : null}
        {bisa ? (
          <div hidden={!lihat}><Pratinjau kode={dok} /></div>
        ) : null}
        <div className="terminal" hidden={bisa && lihat}>
          {r.keluaran || "(program ini tidak mencetak apa pun)"}
        </div>
      </div>
      {r.galat ? (
        <div className="arti">
          <b>Artinya</b>
          <div>{r.galat.artinya.length ? r.galat.artinya.join(" ")
            : r.galat.mentah}</div>
        </div>
      ) : null}
    </div>
  );
}

export function BlokKode({
  b, indeksBagian, kunciBahasa, indeksMateri, judulMateri, sorotMateri,
  runnerBahasa, siapBahasa,
}: {
  b: BagianKode;
  indeksBagian: number;
  kunciBahasa: string;
  indeksMateri: number;
  judulMateri: string;
  sorotMateri: string;
  runnerBahasa: string;
  siapBahasa: boolean;
}) {
  const [editorBuka, setEditorBuka] = useState(false);
  const [hasil, setHasil] = useState<
    { jenis: "kosong" } | { jenis: "sibuk" }
    | { jenis: "jalan"; r: HasilCoba; kode: string }
    | { jenis: "galat"; pesan: string }>({ jenis: "kosong" });
  const [jejakBuka, setJejakBuka] = useState(false);
  const pegangan = useRef<PeganganEditor | null>(null);

  const p = b.petunjuk;
  const lencana = LENCANA[p.jenis] || p.jenis;
  // Blok multi-berkas yang penandanya bisa dipecah tampil sebagai pohon dan panel kode.
  const pecah = useMemo(
    () => (p.jenis === "multi" ? pecahBerkas(b.kode) : null),
    [p.jenis, b.kode],
  );
  // Menjalankan butuh DUA syarat, dan keduanya jawaban server: blok ini memang
  // program utuh (`bisa_dijalankan` dari berkas.py) DAN toolchain-nya
  // benar-benar terpasang di mesin ini (`siap` dari runner.py).
  const bisaJalan = p.bisa_dijalankan && (b.siap ?? siapBahasa);
  const bahasaJalan = b.bahasa || runnerBahasa;
  const kodeKini = () => (editorBuka ? pegangan.current?.nilai() ?? b.kode : b.kode);

  const jalankan = async () => {
    if (hasil.jenis === "sibuk") return;
    setHasil({ jenis: "sibuk" });
    const kode = kodeKini();
    try {
      const r = await kirim<HasilCoba>("coba", { bahasa: bahasaJalan, kode });
      setHasil({ jenis: "jalan", r, kode });
    } catch (e) {
      setHasil({ jenis: "galat", pesan: (e as Error).message });
    }
  };

  /* `tabIndex={-1}`, bukan `0`: pembungkusnya harus bisa DIFOKUS supaya `j`/`k`
     punya sasaran dan `⏎` punya pemilik, tapi ia tidak boleh menambah satu pun
     perhentian Tab. Tombol di `.blok-alat` sudah native dan sudah ada di urutan
     Tab; menambahkan pembungkusnya berarti setiap contoh kode menyisipkan satu
     perhentian kosong di antara tombol-tombol yang memang berguna. */
  return (
    <div className="blok-kode" tabIndex={-1}
         data-jalankan={bisaJalan ? "1" : undefined}>
      <div className="blok-kepala">
        {p.nama ? <span className="berkas">{p.nama}</span>
          : <span>{b.judul || p.instruksi}</span>}
        <span className="lencana">{lencana}</span>
        <div className="blok-alat">
          {bisaJalan ? (
            <button
              type="button"
              className="tbl tbl-kecil tbl-utama"
              title="Jalankan kode ini di komputermu (Ctrl+Enter)"
              disabled={hasil.jenis === "sibuk"}
              onClick={() => { void jalankan(); }}
            >
              <Ikon nama="jalankan" ukuran={14} tebal={2} />
              Jalankan
            </button>
          ) : null}
          {/* Membaca kode orang lain dan MENGUBAHNYA lalu melihat apa yang
              rusak adalah dua kegiatan yang sangat berbeda, dan yang kedua
              itulah yang mengajari. Kodenya tidak pernah ditimpa: `b.kode`
              tetap utuh, jadi "Kembalikan" selalu bisa. */}
          {bisaJalan && !editorBuka ? (
            <button type="button" className="tbl tbl-kecil tbl-hantu"
                    title="Ubah kodenya lalu jalankan lagi"
                    onClick={() => setEditorBuka(true)}>
              Ubah kodenya
            </button>
          ) : null}
          {editorBuka ? (
            <button type="button" className="tbl tbl-kecil tbl-hantu"
                    title="Kembalikan ke kode aslinya"
                    onClick={() => {
                      setEditorBuka(false);
                      setHasil({ jenis: "kosong" });
                    }}>
              Kembalikan
            </button>
          ) : null}
          <button type="button" className="tbl tbl-kecil tbl-hantu"
                  onClick={() => { void salin(b.kode); }}>
            Salin
          </button>
          {/* "Lihat jalannya": rekaman langkah demi langkah dari `/api/jejak`.
              Hanya Python, dan hanya contoh yang tidak menunggu input. */}
          {bisaJalan && bahasaJalan === "python"
            && !/\binput\s*\(/.test(b.kode) ? (
            <button
              type="button"
              className="tbl tbl-kecil tbl-hantu"
              title="Putar ulang program ini baris demi baris, lengkap dengan isi variabelnya"
              onClick={() => setJejakBuka((v) => !v)}
            >
              Lihat baris demi baris
            </button>
          ) : null}
          {/* Ruang Coba tetap ada, tapi tidak lagi jadi satu-satunya jalan:
              untuk kerja yang lebih panjang (stdin, ganti bahasa, draf
              tersimpan) ia punya yang tidak muat di sini. */}
          {p.bisa_dijalankan ? (
            <a
              className="tbl tbl-kecil tbl-hantu"
              title="Buka di Ruang Coba: layar penuh, bisa diberi masukan (stdin)"
              href={`#/coba?key=${kunciBahasa}&materi=${indeksMateri}`
                + `&bagian=${b.bagian ?? indeksBagian}`}
            >
              Ruang Coba
            </a>
          ) : null}
        </div>
      </div>

      <div className="blok-sarung">
        {editorBuka ? (
          <Editor
            pegangan={pegangan}
            bahasa={b.sorot || sorotMateri}
            kodeAwal={b.kode}
            label={"Utak-atik kode: " + (p.nama || b.judul || judulMateri)}
            pintasan={{ "ctrl+enter": () => { void jalankan(); } }}
          />
        ) : pecah ? (
          <PohonBerkas catatan={pecah.catatan} berkas={pecah.berkas} />
        ) : (
          <Kode token={b.token} />
        )}
      </div>

      {pecah ? (
        <div className="blok-kaki">{KAKI_PECAH}</div>
      ) : p.perintah.length ? (
        <div className="blok-kaki">
          {"Jalankan: "}
          <span className="perintah">{p.perintah.join("   lalu   ")}</span>
        </div>
      ) : p.keterangan ? (
        <div className="blok-kaki">{p.keterangan}</div>
      ) : (p.instruksi && !p.nama) ? (
        <div className="blok-kaki">{p.instruksi}</div>
      ) : null}

      <div className="blok-keluaran">
        {hasil.jenis === "sibuk" ? (
          <div className="keluaran-kartu deret" role="status">
            <div className="pusaran" aria-hidden="true" />
            <span>Menjalankan…</span>
          </div>
        ) : hasil.jenis === "galat" ? (
          <div className="keluaran-kartu keluaran-salah">
            <div className="terminal">{hasil.pesan}</div>
          </div>
        ) : hasil.jenis === "jalan" ? (
          <KartuKeluaran
            r={hasil.r}
            runner={runnerBahasa}
            kode={hasil.kode}
            onTutup={() => setHasil({ jenis: "kosong" })}
          />
        ) : null}
      </div>

      {jejakBuka ? (
        <Jejak
          kode={kodeKini()}
          token={kodeKini() === b.kode ? b.token : null}
          onTutup={() => setJejakBuka(false)}
        />
      ) : null}
    </div>
  );
}
