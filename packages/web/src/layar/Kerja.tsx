/* Ruang kerja latihan dan Ruang Coba.
 *
 * Port `layarLatihan` dan `layarCoba` dari `webapp/statik/js/layar-kerja.js`.
 * Algoritmanya tidak ada di sini -- diff baris, diff kata, tangga jawaban, dan
 * contoh awal tinggal di `kerja-beda.ts` dan sudah diadu dengan versi JS-nya.
 *
 * Dua aturan dari AGENTS.md yang membentuk layar ini, dan keduanya gratis
 * dijaga di React:
 *
 * 1. **Jangan pernah menulis definisi "lulus" yang kedua.** Kelulusan
 *    diputuskan `runner.periksa` di server; berkas ini cuma mengubah bentuk
 *    jawabannya. Tidak ada satu pun `if` di sini yang menyimpulkan lulus dari
 *    isi `uji`.
 * 2. **Panel hasil SELALU ADA**, bahkan sebelum ada hasilnya, dan keadaan
 *    kosongnya menjelaskan apa yang akan muncul di situ. Sebelumnya panel ini
 *    baru lahir sesudah tombol ditekan, di bawah baris tombol; di layar pendek
 *    itu berarti umpan balik yang paling ditunggu muncul di luar pandangan.
 */

import {
  useCallback, useEffect, useRef, useState, type ReactNode,
} from "react";

import { ambil, kirim } from "../api.ts";
import { adaGerak } from "../gerak.ts";
import { rayakan, salin, sorak, umumkan, type Hadiah } from "../sorak.tsx";
import { Editor, type PeganganEditor } from "../komponen/Editor.tsx";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { Kode } from "../komponen/Kode.tsx";
import { Pratinjau } from "../komponen/Pratinjau.tsx";
import { BlokProsa, type Blok } from "../komponen/Prosa.tsx";
import {
  bisaDipratinjau, dokumenPratinjau, halamanDikarang,
} from "../komponen/pratinjau-css.ts";
import {
  bedaBaris, bedaKata, contohAwal, nomorDiBaris, pasangkanUbahan, pisahRekor,
  type ButirBeda, type Segmen,
} from "./kerja-beda.ts";
import type { Konteks } from "../Cangkang.tsx";
import type { Token } from "../../../bersama/src/sorot.ts";

/* ====================================================== bentuk jawaban API */

interface BlokGalatData { mentah: string; baris: string[]; artinya: string[] }

interface HasilJalan {
  sukses: boolean;
  keluaran: string;
  galat: BlokGalatData | null;
  kode_keluar: number;
  fase: string;
  timeout: boolean;
  catatan: string;
  stdin?: string;
  detik: number;
}

interface BarisBeda {
  tanda: string;
  harapan: string | null;
  aktual: string | null;
  tampak: boolean;
}
interface BedaData {
  sama: boolean;
  baris: BarisBeda[];
  nomor_beda: number;
  kolom_beda: number;
  catatan: string[];
  ringkas: string;
  nyaris: boolean;
}
interface Uji {
  nama: string;
  lulus: boolean;
  harapan: string;
  aktual: string;
  mode: string;
  stdin: string;
  kode_keluar: number;
  output_cocok: boolean;
  galat: BlokGalatData | null;
  beda: BedaData | null;
}
interface HasilPeriksa {
  bisa_dinilai: boolean;
  alasan?: string;
  lulus: boolean;
  detik?: number;
  uji: Uji[];
  hadiah?: Hadiah | null;
  status?: string;
}

interface DataLatihan {
  bahasa: string;
  label_bahasa: string;
  runner: string;
  sorot: string;
  indeks: number;
  jumlah: number;
  judul: string;
  tingkat: string;
  proyek: boolean;
  soal_blok: Blok[];
  hint: string[];
  solusi: string;
  setup: string;
  /* Token dari `isi.token_kode`. Jenisnya persis anggota `JenisToken` --
     keduanya diturunkan dari `inti/sorot.py`, dan `TestPenyorotJavaScript`
     mengadu kedua pemindai atas seluruh kode kurikulum. JSON tidak membawa
     tipe, jadi pengecorannya di satu tempat: di sini. */
  token_setup: Token[];
  stdin_list: string[];
  dinilai: boolean;
  alasan: string;
  bisa_jalan: boolean;
  status: string;
  kunci: string;
  kode: string;
  berkas: { nama: string; folder: string; perintah: string[] };
  batas_waktu: number;
}

/* ============================================================== pratinjau */

/* Lebar perangkat yang bisa dipilih untuk pratinjau. Urutannya dari sempit ke
   lebar lalu "lebar penuh" di ujung, karena yang terakhir itu BUKAN sebuah
   lebar melainkan tiadanya pilihan -- keadaan bawaan, dan tempatnya di ujung
   daftar supaya ia tidak terbaca sebagai angka keempat.

   Tiga angkanya bukan karangan: 360 lebar yang dipakai seluruh audit layar
   sempit di repo ini, 768 batas tablet, 1280 lebar laptop yang juga viewport
   baku pengukuran di sini. */
const LEBAR_PRATINJAU = [
  { v: 360, nama: "360", ket: "Tata ulang halamanmu selebar ponsel, 360 px" },
  { v: 768, nama: "768", ket: "Tata ulang halamanmu selebar tablet, 768 px" },
  { v: 1280, nama: "1280", ket: "Tata ulang halamanmu selebar laptop, 1280 px" },
  { v: 0, nama: "lebar penuh", ket: "Selebar panelnya sendiri" },
];

/* SATU-SATUNYA tempat lebar terpilih tinggal, dan ia di lingkup MODUL.
 *
 * Bukan kemalasan: kartu hasil lahir baru setiap kali Jalankan ditekan, jadi
 * pilihan yang disimpan di dalam state kartu itu lenyap tepat pada peristiwa
 * yang paling sering terjadi di layar ini. Pelajar yang sedang memeriksa
 * halamannya di 360 px menekan Jalankan untuk melihat akibat satu suntingan,
 * dan menemukan pratinjaunya melompat kembali ke lebar penuh -- yang hilang
 * bukan setelan melainkan perbandingan yang sedang ia kerjakan.
 *
 * TIDAK di `localStorage` dan TIDAK di berkas mana pun. Ini alat periksa
 * sesaat, bukan preferensi tampilan: orang yang pernah mengintip halamannya di
 * 360 px tidak sedang menyatakan ia ingin selalu melihatnya begitu, dan setelan
 * yang bertahan melewati tutup-buka browser akan membuatnya menemukan
 * pratinjau sempit berbulan-bulan kemudian tanpa ingat pernah memintanya. */
let lebarPratinjau = 0;

/**
 * Baris pil pemilih lebar perangkat.
 *
 * Keadaan terpilih ditandai DUA kali: kelasnya dan `aria-pressed`. Warna tidak
 * dibacakan pembaca layar, jadi `.tbl-pilih` sendirian berarti satu-satunya
 * pelajar yang tidak bisa tahu lebar mana yang sedang berlaku adalah yang
 * paling bergantung pada tahu.
 */
function BarisLebarPratinjau({ onPilih }: { onPilih: (v: number) => void }) {
  return (
    <div
      className="pratinjau-lebar"
      style={{ display: "flex", flexWrap: "wrap", alignItems: "center",
               gap: "var(--s2)", marginBottom: "var(--s2)" }}
    >
      <span className="mata">Lebar perangkat</span>
      {LEBAR_PRATINJAU.map((p) => {
        const kini = p.v === lebarPratinjau;
        return (
          <button
            key={p.v}
            type="button"
            className={"tbl tbl-kecil " + (kini ? "tbl-pilih" : "tbl-hantu")}
            title={p.ket}
            aria-pressed={kini}
            onClick={() => { lebarPratinjau = p.v; onPilih(p.v); }}
          >
            {p.nama}
          </button>
        );
      })}
    </div>
  );
}

/* ================================================================== galat */

/* Satu baris pesan galat = satu simpul. Yang menyebut nomor jadi `<button>`
 * yang mengantar caret ke baris itu; yang tidak tetap teks biasa -- jadi blok
 * galat tanpa satu pun nomor terlihat PERSIS seperti sebelum tombol ini ada.
 *
 * Tombolnya tidak lahir kalau editornya tidak punya baris sebanyak itu. Tombol
 * yang berakhir "baris itu tidak ada" lebih buruk daripada tidak ada tombol --
 * dan `tuju.bisa()` menjawabnya dari isi editor SAAT INI, bukan dari panjang
 * kode yang dikirim tadi. Di antara "Periksa jawaban" dan klik pada pesan
 * galatnya, orangnya mungkin sudah menghapus setengah berkasnya. */
interface Tuju { bisa: (n: number) => boolean; ke: (n: number) => void }

function BarisGalat({ baris, tuju }: { baris: string[]; tuju?: Tuju }) {
  return (
    <>
      {baris.map((teks, i) => {
        const pisah = i < baris.length - 1 ? "\n" : "";
        const n = tuju ? nomorDiBaris(teks) : 0;
        if (n && tuju && tuju.bisa(n)) {
          return (
            <span key={i}>
              <button
                type="button"
                aria-label={"Ke baris " + n}
                onClick={() => tuju.ke(n)}
                style={{ font: "inherit", color: "inherit", background: "none",
                         border: 0, padding: 0, margin: 0, textAlign: "left",
                         whiteSpace: "inherit", cursor: "pointer",
                         borderBottom: "var(--tebal-garis) dotted currentColor" }}
              >
                {teks}
              </button>
              {pisah}
            </span>
          );
        }
        return <span key={i}>{teks + pisah}</span>;
      })}
    </>
  );
}

/* `denganLebih` dipakai HANYA oleh kartu Jalankan. Chipnya lahir TERSEMBUNYI --
 * `usePinKeGalat` yang menyalakannya, dan hanya kalau panel benar-benar
 * digulir. */
function BlokGalatKartu({
  g, fase, tuju, denganLebih,
}: {
  g: BlokGalatData; fase: string; tuju?: Tuju; denganLebih?: boolean;
}) {
  return (
    <div data-galat="1" style={{ marginTop: "var(--s3)" }}>
      <span className="mata">
        {fase === "kompilasi" ? "Pesan dari compiler" : "Pesan error"}
      </span>
      {denganLebih ? (
        <span className="pil pil-tenang" hidden data-lebih="atas">
          panel digulir ke pesan ini; keluaran lengkap ada di atasnya
        </span>
      ) : null}
      <div className="terminal terminal-galat">
        <BarisGalat baris={g.baris} tuju={tuju} />
      </div>
      {g.artinya.length ? (
        <div className="arti">
          <b>Artinya</b>
          {g.artinya.map((t, i) => <div key={i}>{"• " + t}</div>)}
        </div>
      ) : null}
    </div>
  );
}

/* ==================================================================== diff
 * Ini tampilan terpenting di aplikasi. Bentuknya:
 *
 *    1 │ Halo, namaku Andi!
 *    2 - Aku sedang belajar Python.    (diharapkan)
 *    2 + aku sedang belajar python.    (punyamu)
 *        ↑ beda mulai kolom 1
 *  → Isinya sudah benar, hanya beda HURUF BESAR/KECIL.
 *
 * Penunjuk kolom dibangun sebagai `.diff-baris` utuh dengan nomor dan tanda
 * kosong, bukan sebagai baris terpisah yang paddingnya dihitung tangan. Itu
 * satu-satunya cara memastikan tanda ↑ tetap sejajar dengan huruf yang
 * ditunjuknya di semua ukuran layar dan semua ukuran huruf. */

/**
 * Segmen `bedaKata` -> anak-anak `.diff-isi`.
 *
 * Yang TIDAK berubah keluar sebagai string, bukan span. Dua sebabnya: ia tidak
 * butuh gaya apa pun, dan dengan begitu cacah anak ELEMEN `.diff-isi` langsung
 * sama dengan cacah ubahan -- sebuah klaim yang bisa diadu dari luar, bukan
 * cuma dilihat.
 *
 * Ubahan ditandai BENTUK, bukan warna: coretan untuk yang hilang, garis bawah
 * untuk yang bertambah. Warna di baris ini sudah dipakai habis oleh
 * `.diff-kurang`/`.diff-tambah` untuk membedakan SISI, jadi memakai warna lagi
 * untuk membedakan SEGMEN berarti satu kanal memikul dua arti -- dan bagi orang
 * yang tidak membedakan merah-hijau, nol di antaranya terbaca. Tint latarnya
 * `currentColor`, jadi ia mewarisi token baris itu sendiri dan tetap benar di
 * keempat tema tanpa satu nilai warna pun dituliskan di sini.
 */
function SegmenKata({ bagian }: { bagian: Segmen[] }): ReactNode {
  return bagian.map((s, i) => (s.tanda === "=" ? s.teks : (
    <span
      key={i}
      className="diff-kata"
      style={{
        background: "color-mix(in srgb, currentColor 16%, transparent)",
        borderRadius: "2px",
        textDecoration: s.tanda === "-" ? "line-through" : "underline",
        textUnderlineOffset: "2px",
      }}
    >
      {s.teks}
    </span>
  )));
}

function BarisDiff({
  nomor, tanda, teks, kelas, ket, segmen,
}: {
  nomor: number | string; tanda: string; teks?: string | null;
  kelas: string; ket?: string; segmen?: Segmen[] | null;
}) {
  return (
    <div className={"diff-baris " + kelas}>
      <span className="diff-nomor">{String(nomor)}</span>
      <span className="diff-tanda">{tanda}</span>
      <span className="diff-isi">
        {segmen ? <SegmenKata bagian={segmen} />
          : (teks === null || teks === undefined ? "" : teks)}
      </span>
      {ket ? <span className="diff-ket">{"(" + ket + ")"}</span> : null}
    </div>
  );
}

function GambarBeda({ b }: { b: BedaData }) {
  const baris: ReactNode[] = [];
  let nomor = 0;
  for (const d of b.baris) {
    nomor += 1;
    if (d.tanda === "=") {
      baris.push(<BarisDiff key={baris.length} nomor={nomor} tanda="│"
                            teks={d.harapan} kelas="diff-sama" />);
      continue;
    }
    const kata = d.tanda === "~" ? bedaKata(d.harapan, d.aktual) : null;

    /* Pasangan yang berbeda HANYA pada spasi diciutkan jadi satu baris. Dua
     * baris penuh untuk "halo··dunia" lawan "halo·dunia" tidak menambah satu
     * pun keterangan: keduanya terbaca identik dari ujung ke ujung, dan yang
     * sebenarnya membedakannya sudah ditandai di dalam segmennya.
     *
     * `d.tampak` SATU-SATUNYA yang memutuskan "bedanya cuma spasi", dan yang
     * memilikinya `api._beda_json`: di sana `tampak` dihitung sekali dengan
     * membandingkan kedua sisi modulo spasi, dan di sana pula `harapan` dan
     * `aktual` lalu DITUKAR dengan hasil `beda.tampakkan`. Konsekuensinya
     * mengikat ke baris ini: begitu `tampak` menyala, tidak ada satu pun spasi
     * asli yang tersisa di string yang sampai ke `bedaKata` -- semuanya sudah
     * jadi `·` dan `→`, dan bagi `pecahToken` keduanya token BUKAN-spasi
     * seperti huruf mana pun. Jadi jangan pernah menghitung ulang jawabannya
     * dari teks itu.
     *
     * `kata` tetap diperiksa, dan juga bukan basa-basi: baris ciut merender
     * `kata.gabung`, dan `bedaKata` boleh menyerah -- di atas BATAS_SEL_KATA,
     * atau tanpa satu token jangkar. Untuk baris sepanjang itu dua baris penuh
     * memang jawaban yang benar. */
    if (kata && d.tampak) {
      baris.push(<BarisDiff key={baris.length} nomor={nomor} tanda="~"
                            teks={null} kelas="diff-sama" ket="spasi saja"
                            segmen={kata.gabung} />);
      continue;
    }

    if (d.tanda === "-" || d.tanda === "~") {
      baris.push(<BarisDiff key={baris.length} nomor={nomor} tanda="-"
                            teks={d.harapan} kelas="diff-kurang"
                            ket="diharapkan" segmen={kata && kata.kiri} />);
    }
    if (d.tanda === "+" || d.tanda === "~") {
      baris.push(<BarisDiff key={baris.length} nomor={nomor} tanda="+"
                            teks={d.aktual} kelas="diff-tambah"
                            ket="punyamu" segmen={kata && kata.kanan} />);
    }
    if (d.tanda === "~" && nomor === b.nomor_beda && b.kolom_beda) {
      baris.push(
        <div key={baris.length} className="diff-baris">
          <span className="diff-nomor" />
          <span className="diff-tanda" />
          <span className="diff-isi diff-tunjuk">
            {" ".repeat(Math.max(0, b.kolom_beda - 1))
              + "↑ beda mulai kolom " + b.kolom_beda}
          </span>
        </div>,
      );
    }
  }

  return (
    <div>
      <div className="diff">{baris}</div>
      {b.baris.some((d) => d.tampak) ? (
        <div className="baris-sisi" style={{ marginTop: "var(--s2)" }}>
          · menandai spasi dan → menandai tab, supaya beda yang tak terlihat
          jadi terlihat.
        </div>
      ) : null}
      {b.catatan.map((c, i) => (
        <div key={i} className="diagnosa">
          <span className="panah">→</span>
          <div>{c}</div>
        </div>
      ))}
    </div>
  );
}

function KartuUji({ u, tuju }: { u: Uji; tuju?: Tuju }) {
  return (
    <div className={"uji " + (u.lulus ? "lulus" : "gagal")}>
      <div className="uji-kepala">
        <span className="uji-cap">{u.lulus ? "LULUS" : "BELUM"}</span>
        <span className="uji-nama">{u.nama}</span>
        {u.stdin ? (
          <span className="pil">
            {"input: " + u.stdin.replace(/\n/g, "⏎").slice(0, 24)}
          </span>
        ) : null}
      </div>
      {!u.lulus ? (
        <div className="uji-badan">
          {u.galat ? <BlokGalatKartu g={u.galat} fase="" tuju={tuju} /> : null}
          {/* Output benar tapi program berakhir dengan error: kasus ini pernah
              dinyatakan lulus, yang justru menyembunyikan bug yang sedang
              dipelajari. */}
          {u.output_cocok && u.kode_keluar !== 0 ? (
            <div className="diagnosa">
              <span className="panah">→</span>
              <div>
                {"Outputmu sudah benar, TAPI program berakhir dengan error "
                  + `(kode keluar ${u.kode_keluar}). Perbaiki dulu errornya.`}
              </div>
            </div>
          ) : null}
          {u.mode === "regex" || u.mode === "mengandung" ? (
            <div>
              <span className="mata">{`Pola yang dicari (${u.mode})`}</span>
              <div className="terminal">{u.harapan}</div>
              <span className="mata">Hasilmu</span>
              <div className="terminal">{u.aktual}</div>
            </div>
          ) : (u.beda ? <GambarBeda b={u.beda} /> : null)}
        </div>
      ) : null}
    </div>
  );
}

/* Jumlah uji yang lulus pada pemeriksaan SEBELUMNYA untuk latihan yang sama,
   selama halaman ini hidup. "tadi 1/3, sekarang 2/3" adalah satu-satunya cara
   kemajuan sebagian terlihat; tanpa itu, dua kegagalan tampak sama persis. */
const LULUS_TADI = new Map<string, number>();
function lulusTadi(kunci: string, lulus: number): number | null {
  const tadi = LULUS_TADI.has(kunci) ? (LULUS_TADI.get(kunci) as number) : null;
  LULUS_TADI.set(kunci, lulus);
  return tadi;
}

function KartuPeriksa({
  r, tadi, tuju,
}: {
  r: HasilPeriksa; tadi: number | null; tuju?: Tuju;
}) {
  if (!r.bisa_dinilai) {
    return <Keadaan jenis="kunci" judul="Belum bisa dinilai" ket={r.alasan} />;
  }
  const lulus = r.uji.filter((u) => u.lulus).length;
  const nyaris = !r.lulus
    && r.uji.some((u) => !u.lulus && u.beda && u.beda.nyaris);
  return (
    <div>
      <div
        className="kartu"
        style={{ marginBottom: "var(--s3)",
                 borderColor: r.lulus ? "var(--tumbuh)"
                   : "color-mix(in srgb, var(--salah) 40%, transparent)" }}
      >
        <div className="deret">
          <h3 style={{ color: r.lulus ? "var(--tumbuh)"
            : nyaris ? "var(--nyala)" : "var(--teks)" }}>
            {r.lulus ? "Benar. Outputmu sudah sesuai."
              : nyaris ? "Hampir. Isinya sudah benar, tinggal bentuknya."
              : "Belum sesuai. Lihat bedanya di bawah."}
          </h3>
          <span className="deret-kanan" />
          <span className={"pil" + (tadi !== null && lulus > tadi ? " pil-tumbuh" : "")}>
            {(tadi !== null && tadi !== lulus ? `tadi ${tadi}, sekarang ` : "")
              + `${lulus}/${r.uji.length} uji lulus`}
          </span>
          <span className="pil">{r.detik + " detik"}</span>
        </div>
        {!r.lulus ? (
          <p style={{ margin: "var(--s2) 0 0", color: "var(--teks-2)",
                      fontSize: "var(--t-ui)" }}>
            Baris hijau bertanda − adalah yang diharapkan; baris merah bertanda +
            adalah punyamu.
          </p>
        ) : null}
      </div>
      {/* Hasil uji urut dari uji pertama. Kalau uji ketiga yang gagal, urutan
          itulah yang membawa mata ke sana: dua kartu hijau lewat, lalu berhenti
          di yang merah. */}
      <div style={{ display: "grid", gap: 0 }}>
        {r.uji.map((u, i) => <KartuUji key={i} u={u} tuju={tuju} />)}
      </div>
    </div>
  );
}

function KartuJalan({
  r, runner, kode, batasWaktu, tuju,
}: {
  r: HasilJalan; runner: string; kode: string; batasWaktu: number; tuju?: Tuju;
}) {
  const [lebar, setLebar] = useState(lebarPratinjau);
  // Untuk HTML dan CSS, "keluaran" adalah pohon struktur -- benar untuk
  // menilai, salah untuk ditonton. Di layar latihan justru di sinilah orang
  // paling ingin melihat halamannya: ia baru saja menulisnya sendiri.
  const dok = kode && bisaDipratinjau(runner)
    ? dokumenPratinjau(runner, kode) : "";
  return (
    <div className="kartu masuk">
      <div className="deret" style={{ marginBottom: "var(--s3)" }}>
        <h3>{dok ? "Halamanmu" : "Hasil menjalankan"}</h3>
        <span className="deret-kanan" />
        <span className={"pil" + (r.kode_keluar === 0 ? " pil-tumbuh" : " pil-salah")}>
          {`kode keluar ${r.kode_keluar}`}
        </span>
        <span className="pil">{r.detik + " detik"}</span>
        {/* Sinyal overflow panel, dan ia lahir TERSEMBUNYI: yang menyalakannya
            cuma pengukuran di `usePinKeGalat`, bukan dugaan dari panjang
            keluaran. Tanpa chip ini keluaran 301 baris di tata letak lebar
            terbaca sebagai keluaran 8 baris. */}
        <span className="pil pil-tenang" hidden data-lebih="bawah">
          keluaran lebih panjang dari panel, gulir ke bawah
        </span>
      </div>
      {r.stdin ? (
        <div style={{ marginBottom: "var(--s2)" }}>
          <span className="mata">Masukan yang dikirim</span>
          <div className="terminal">{r.stdin}</div>
        </div>
      ) : null}
      {dok ? (
        <div style={{ marginBottom: "var(--s3)" }}>
          {halamanDikarang(runner, kode) ? (
            <p className="pratinjau-ket">
              Halaman contoh ini dibuatkan dari pemilih di CSS-mu sendiri:{" "}
              <b>bukan</b> berkas HTML-mu.
            </p>
          ) : null}
          <BarisLebarPratinjau onPilih={setLebar} />
          <Pratinjau kode={dok} lebar={lebar} />
        </div>
      ) : null}
      <span className="mata">{dok ? "Struktur yang dinilai" : "Keluaran"}</span>
      <div className="terminal">{r.keluaran}</div>
      {r.galat ? (
        <BlokGalatKartu g={r.galat} fase={r.fase} tuju={tuju} denganLebih />
      ) : null}
      {r.timeout ? (
        <div className="diagnosa">
          <span className="panah">→</span>
          <div>
            {`Program dihentikan setelah ${batasWaktu} detik. `
              + "Kemungkinan ada loop yang tidak pernah berhenti."}
          </div>
        </div>
      ) : null}
      {r.catatan ? (
        <div className="baris-sisi" style={{ marginTop: "var(--s2)" }}>
          {r.catatan}
        </div>
      ) : null}
    </div>
  );
}

/* ====================================================== pin ke pesan galat */

/* Isyarat bahwa pengguna sudah mengambil alih gulir panel hasil. `keydown` ikut
   karena panel yang bisa digulir juga bisa difokus. */
const SENTUHAN_HASIL = ["wheel", "pointerdown", "keydown"] as const;
/* Batas waktu pengamat ukuran panel hasil. Angkanya kembar dengan `PIN_BARA_MS`
   di pembaca materi, dan itu disengaja: keduanya menjawab satu pertanyaan --
   berapa lama sebuah pengamat boleh hidup di layar yang dibuka lalu ditinggal. */
const PIN_HASIL_MS = 4000;

/**
 * Nyalakan sinyal "ada lebih di bawah", lalu antar panel ke pesan galatnya.
 *
 * Panel hasil DIPAGARI tingginya, tapi hanya di tata letak lebar
 * (`.kerja-hasil { overflow-y: auto; max-height: 46cqh }` di dalam
 * `@container panggung (min-width: 1100px)`). Akibatnya keluaran panjang + blok
 * galat di bawahnya = blok galat SELURUHNYA di luar jendela panel sementara
 * `scrollTop` tetap 0, dan satu-satunya isyarat bahwa jawabannya ada di bawah
 * sebuah bilah gulir setipis `thin`.
 *
 * `scrollIntoView` DILARANG di sini: ia menggulir SEMUA leluhur termasuk
 * dokumen. Dan tanpa animasi apa pun -- guliran dan sinyalnya tetap terjadi
 * pada tingkat gerak `mati`, karena keduanya INFORMASI, bukan hiasan.
 *
 * Pengamat ukuran mengawasi ANAK-ANAK panel, bukan panelnya: panel
 * ber-`max-height` tidak pernah berubah ukuran ketika isinya tumbuh, dan untuk
 * HTML/CSS tinggi kartu BERTAMBAH sesudah iframe pratinjau melaporkan dirinya.
 *
 * Pin-nya WAJIB lepas -- posisi gulir adalah keadaan PENGGUNA, dan merebutnya
 * kembali sesudah dia menggeser sendiri lebih buruk daripada tidak mem-pin sama
 * sekali. Jadi putus pada isyarat sentuhan pertama dan pada batas waktu.
 */
function usePinKeGalat(
  panelRef: React.RefObject<HTMLDivElement | null>, tanda: unknown,
) {
  useEffect(() => {
    const panel = panelRef.current;
    if (!panel) return;
    const blok = panel.querySelector<HTMLElement>("[data-galat]");
    const chipBawah = panel.querySelector<HTMLElement>('[data-lebih="bawah"]');
    const chipAtas = blok
      ? blok.querySelector<HTMLElement>('[data-lebih="atas"]') : null;

    /* Posisi blok galat diambil dari KOORDINAT LAYOUT, bukan rect mentah.
     *
     * `getBoundingClientRect()` termasuk transform, dan kartu hasilnya
     * `div.kartu.masuk`: `@keyframes masuk` berangkat dari `translateY(7px)`.
     * Mengukur dengan rect berarti menggulir ke tempat yang akan BERPINDAH
     * tujuh piksel ke atas begitu animasinya selesai -- dan `ResizeObserver`
     * tidak akan pernah menangkapnya, karena transform tidak mengubah satu
     * kotak layout pun. Jalan keluarnya: rect (sub-piksel) DIKURANGI
     * translateY simpul yang beranimasi di antara blok dan panel. */
    const geserTransform = () => {
      let dy = 0;
      for (let n: HTMLElement | null = blok; n && n !== panel;
           n = n.parentElement) {
        const t = getComputedStyle(n).transform;
        if (t && t !== "none") dy += new DOMMatrixReadOnly(t).m42;
      }
      return dy;
    };

    const kotak = () => {
      const kp = panel.getBoundingClientRect();
      const kb = (blok as HTMLElement).getBoundingClientRect();
      const dy = geserTransform();
      return { atas: kb.top - kp.top - dy, bawah: kb.bottom - kp.top - dy };
    };

    const pasang = () => {
      // Chipnya DISEMBUNYIKAN lebih dulu, lalu panelnya diukur. Kalau tinggi
      // chip ikut memutuskan, panel yang pas-pasan berkedip: chip muncul ->
      // panelnya memotong -> chip tetap muncul, selamanya, atas keadaan yang
      // sudah tidak ada.
      if (chipBawah) chipBawah.hidden = true;
      if (chipAtas) chipAtas.hidden = true;

      // DUA syarat, dan syarat pertama yang paling mudah dilupakan: panelnya
      // harus benar-benar MEMOTONG. Di tata letak sempit `overflow-y`
      // terhitung `visible`, dan di sana `scrollHeight` melebihi `clientHeight`
      // PERMANEN tujuh piksel -- margin anak yang menyembul dari kotak yang
      // tidak memotong apa pun. Yang menjawab "memotong" propertinya, bukan
      // selisihnya.
      const cs = getComputedStyle(panel);
      const memotong = cs.overflowY === "auto" || cs.overflowY === "scroll";
      const lebih = memotong && panel.scrollHeight > panel.clientHeight;
      if (chipBawah) chipBawah.hidden = !lebih;
      if (!lebih || !blok) return;

      let k = kotak();
      if (k.atas >= 0 && k.bawah <= panel.clientHeight) return;

      // Chipnya dinyalakan SEBELUM rect-nya dipakai menggulir: `.mata` dan chip
      // ini masing-masing memakai barisnya sendiri, jadi reveal menggeser isi
      // blok ke bawah.
      if (chipAtas) { chipAtas.hidden = false; k = kotak(); }

      const maks = panel.scrollHeight - panel.clientHeight;
      panel.scrollTop = Math.max(0, Math.min(maks, panel.scrollTop + k.atas));
    };

    pasang();
    if (typeof ResizeObserver !== "function") return;

    // Pengamatnya memanggil `pasang()` TANPA penjaga "tinggi berubah atau
    // tidak". Penjaga seperti itu membuat keputusan sesaat TERKUNCI. Yang
    // menahan lingkarannya sifat `pasang()` sendiri: ia IDEMPOTEN -- dari
    // keadaan apa pun ia mendarat di keadaan yang sama, jadi tik kedua
    // menghasilkan ukuran yang identik dan peramban tidak mengirim
    // pemberitahuan ketiga.
    let lepas = () => {};
    const pengamat = new ResizeObserver(() => pasang());
    for (const anak of Array.from(panel.children)) pengamat.observe(anak);
    const jam = setTimeout(() => lepas(), PIN_HASIL_MS);

    lepas = () => {
      clearTimeout(jam);
      pengamat.disconnect();
      for (const nama of SENTUHAN_HASIL) panel.removeEventListener(nama, lepas);
    };
    for (const nama of SENTUHAN_HASIL) {
      panel.addEventListener(nama, lepas, { passive: true });
    }
    return lepas;
  }, [panelRef, tanda]);
}

/* ============================================================ layar latihan */

type Hasil =
  | { jenis: "kosong" }
  | { jenis: "sibuk"; pesan: string }
  | { jenis: "galat"; pesan: string }
  | { jenis: "jalan"; r: HasilJalan; kode: string }
  | { jenis: "periksa"; r: HasilPeriksa; tadi: number | null };

export function Latihan({
  kunciBahasa, indeks, onKonteks,
}: {
  kunciBahasa: string;
  indeks: number;
  onKonteks: (k: Konteks | undefined) => void;
}) {
  const [x, setX] = useState<DataLatihan | null>(null);
  const [galatMuat, setGalatMuat] = useState("");
  const [status, setStatus] = useState("");
  const [hintTerbuka, setHintTerbuka] = useState(0);
  const [hasil, setHasil] = useState<Hasil>({ jenis: "kosong" });
  const [rekorLangkah, setRekorLangkah] = useState(-1);
  const [banding, setBanding] = useState<ButirBeda[] | null>(null);
  const pegangan = useRef<PeganganEditor | null>(null);
  const panelRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    let dibatalkan = false;
    setX(null);
    setGalatMuat("");
    setHasil({ jenis: "kosong" });
    setHintTerbuka(0);
    (async () => {
      try {
        const d = await ambil<DataLatihan>("/api/latihan",
                                           { key: kunciBahasa, indeks });
        if (dibatalkan) return;
        setX(d);
        setStatus(d.status);
        onKonteks({
          balik: { label: d.label_bahasa, href: "#/bahasa/" + kunciBahasa },
          bab: d.proyek ? "Proyek akhir" : "Latihan",
          judul: d.judul,
          posisi: `${d.indeks + 1} / ${d.jumlah}`,
          langkah: true,
          ...(d.indeks > 0
            ? { sebelum: `#/latihan/${kunciBahasa}/${d.indeks - 1}` } : {}),
          ...(d.indeks + 1 < d.jumlah
            ? { sesudah: `#/latihan/${kunciBahasa}/${d.indeks + 1}` } : {}),
        });
      } catch (e) {
        if (!dibatalkan) setGalatMuat((e as Error).message);
      }
    })();
    return () => { dibatalkan = true; };
  }, [kunciBahasa, indeks, onKonteks]);

  usePinKeGalat(panelRef, hasil);

  const simpan = useCallback(async (kode: string, diam: boolean) => {
    try {
      await kirim("/api/latihan/simpan", { key: kunciBahasa, indeks, kode });
      pegangan.current?.catat("tersimpan");
      if (!diam && x) sorak("Tersimpan di " + x.berkas.nama, "tumbuh", 2);
    } catch (e) {
      if (!diam) sorak((e as Error).message, "salah");
    }
  }, [kunciBahasa, indeks, x]);

  const jalankan = useCallback(async () => {
    setHasil({ jenis: "sibuk", pesan: "Menjalankan kodemu…" });
    const kode = pegangan.current?.nilai() ?? "";
    try {
      const r = await kirim<HasilJalan>("/api/latihan/jalankan",
                                        { key: kunciBahasa, indeks, kode });
      setHasil({ jenis: "jalan", r, kode });
    } catch (e) {
      setHasil({ jenis: "galat", pesan: (e as Error).message });
    }
  }, [kunciBahasa, indeks]);

  const periksa = useCallback(async () => {
    if (!x) return;
    setHasil({
      jenis: "sibuk",
      pesan: "Menyiapkan kunci jawaban lalu menjalankan kodemu…",
    });
    try {
      const r = await kirim<HasilPeriksa>(
        "/api/latihan/periksa",
        { key: kunciBahasa, indeks, kode: pegangan.current?.nilai() ?? "" },
      );
      const lulus = r.uji.filter((u) => u.lulus).length;
      setHasil({ jenis: "periksa", r, tadi: lulusTadi(x.kunci, lulus) });
      if (r.bisa_dinilai) {
        umumkan(r.lulus ? "Benar. Outputmu sudah sesuai."
          : `Belum sesuai. ${lulus} dari ${r.uji.length} uji lulus.`);
      }
      if (r.lulus) {
        setStatus("lulus");
        rayakan(r.hadiah);
      }
      // Belum lulus BUKAN kegagalan, jadi tidak ada getaran di sini. Yang
      // dibutuhkan cuma mata yang dibawa ke diff-nya. Menggetarkan layar tiap
      // kali output belum cocok akan membuat mencoba terasa seperti dihukum.
      if (!r.lulus) {
        panelRef.current?.scrollIntoView({
          behavior: adaGerak() ? "smooth" : "auto", block: "nearest",
        });
      }
    } catch (e) {
      setHasil({ jenis: "galat", pesan: (e as Error).message });
    }
  }, [kunciBahasa, indeks, x]);

  const tandaiManual = useCallback(async () => {
    const nyalakan = status !== "manual";
    if (nyalakan && !globalThis.confirm(
      "Tandai latihan ini selesai? Ini penilaian jujur dari kamu sendiri: "
      + "mesin tidak memeriksanya.")) return;
    try {
      const r = await kirim<{ status: string } & Hadiah>(
        "/api/latihan/manual", { key: kunciBahasa, indeks, nyalakan });
      setStatus(r.status);
      rayakan(r);
      sorak(nyalakan ? "Ditandai selesai." : "Tanda selesai dibatalkan.",
            "tumbuh");
    } catch (e) {
      sorak((e as Error).message, "salah");
    }
  }, [kunciBahasa, indeks, status]);

  if (galatMuat) {
    return <Keadaan jenis="salah" judul="Latihan tidak terbuka" ket={galatMuat} />;
  }
  if (!x) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat latihan…</span>
      </div>
    );
  }

  const tuju: Tuju = {
    bisa: (n) => n >= 1
      && n <= (pegangan.current?.nilai() ?? "").split("\n").length,
    ke: (n) => { pegangan.current?.keBaris(n); },
  };

  const semuaBaris = x.solusi.split("\n");
  const rekor = pisahRekor(semuaBaris);

  return (
    <div className="masuk kerja">
      <header className="kepala-besar kepala-latihan">
        <div className="kepala-judul">
          <span className="mata">
            {x.proyek ? `${x.label_bahasa} · proyek akhir`
              : `${x.label_bahasa} · latihan ${x.indeks + 1} dari ${x.jumlah}`}
          </span>
          <h1>{x.judul}</h1>
          {x.proyek ? (
            <p className="kepala-sub">
              Tidak ada materi baru di sini. Yang diuji cuma satu: apakah yang
              sudah kamu baca terpisah-pisah itu nyambung jadi satu program yang
              jalan.
            </p>
          ) : null}
        </div>
        <div className="kepala-aksi">
          <div className="deret deret-rapat">
            {x.proyek ? <span className="pil pil-nyala">PROYEK AKHIR</span> : null}
            <span className={"pil t-" + x.tingkat}>{x.tingkat}</span>
            <span>
              {status === "lulus" ? <span className="pil pil-tumbuh">LULUS</span>
                : status === "manual"
                  ? <span className="pil pil-tumbuh">ditandai selesai</span>
                  : <span className="pil">belum selesai</span>}
            </span>
            {x.dinilai ? <span className="pil">dinilai otomatis</span>
              : <span className="pil pil-kunci">tanpa nilai otomatis</span>}
          </div>
        </div>
      </header>

      {/* Dua panel: yang DIBACA di kiri, yang DIKERJAKAN di kanan. Susunan lama
          menumpuk keduanya, jadi soalnya tergulir keluar layar tepat saat kode
          mulai ditulis -- dan menulis jawaban sambil lupa pertanyaannya adalah
          cara tercepat mengerjakan latihan yang salah. */}
      <div className="kerja-tata">
        <div className="kerja-soal">
          <section>
            <span className="mata">Soal</span>
            <div className="kartu prosa prosa-soal">
              {(x.soal_blok || []).map((b, i) => <BlokProsa key={i} blk={b} />)}
            </div>
          </section>

          {!x.dinilai ? (
            <Keadaan
              jenis="kunci"
              judul="Latihan ini tidak dinilai mesin"
              ket={x.alasan}
              aksi={
                <button type="button" className="tbl tbl-kecil"
                        onClick={tandaiManual}>
                  {status === "manual" ? "Batalkan tanda selesai"
                    : "Saya sudah menyelesaikannya"}
                </button>
              }
            />
          ) : null}

          <section>
            <span className="mata">Berkas jawabanmu</span>
            <div className="kartu kartu-rapat">
              <code style={{ color: "var(--nyala)", fontWeight: 700 }}>
                {x.berkas.nama}
              </code>
              {/* Path-nya dipatahkan di karakter mana pun, bukan digulir
                  mendatar: penggulir sendiri di dalam kolom 360 px menghasilkan
                  path yang TETAP terpotong plus satu bilah gulir tambahan di
                  tempat yang paling sedikit ruangnya. */}
              <div className="berkas-jalur" style={{ marginTop: "var(--s1)" }}>
                {"di " + x.berkas.folder}
              </div>
              {x.runner === "java" ? (
                <div className="baris-sisi" style={{ marginTop: "var(--s2)" }}>
                  {`Nama kelasnya harus ${x.berkas.nama.replace(/\.java$/, "")}: `
                    + "javac mewajibkannya sama dengan nama berkas."}
                </div>
              ) : null}
              {x.berkas.perintah.length ? (
                <div className="berkas-jalur" style={{ marginTop: "var(--s2)" }}>
                  {"Di terminal: "}
                  <code style={{ color: "var(--tenang)" }}>
                    {x.berkas.perintah.join("   lalu   ")}
                  </code>
                </div>
              ) : null}
              <div className="baris-sisi" style={{ marginTop: "var(--s2)" }}>
                Kode yang kamu tulis di sini tersimpan ke berkas itu, jadi bisa
                dibuka di editor mana pun dan dijalankan dari terminal.
              </div>
            </div>
          </section>

          {x.setup ? (
            <section>
              <span className="mata">
                Kondisi awal (sudah disiapkan, tak perlu kamu tulis)
              </span>
              <div className="blok-kode"><Kode token={x.token_setup} /></div>
            </section>
          ) : null}

          {x.stdin_list.length > 1 ? (
            <Keadaan
              judul="Diuji dengan beberapa masukan"
              ket={`Kodemu dijalankan ${x.stdin_list.length} kali dengan input `
                + "berbeda, jadi jawaban yang di-hardcode tidak akan lolos."}
            />
          ) : null}
        </div>

        <div className="kerja-kode">
          <Editor
            pegangan={pegangan}
            bahasa={x.sorot}
            kodeAwal={x.kode}
            label={"Kode jawabanmu untuk " + x.judul}
            isiRuang
            onUbah={(kode) => { void simpan(kode, true); }}
            pintasan={{
              "ctrl+enter": () => { void jalankan(); },
              "ctrl+shift+enter": () => { void periksa(); },
              "ctrl+s": () => {
                void simpan(pegangan.current?.nilai() ?? "", false);
              },
            }}
          />

          <div className="kerja-bawah">
            <div className="kerja-tindakan">
              {/* Dua tindakan utama berdiri sendiri, di kiri. Alat-alat
                  dikelompokkan rapat di kanan sebagai SATU benda. Jarak antar
                  kelompok lebih lebar daripada jarak di dalam kelompok -- itu
                  yang membuat keduanya terbaca sebagai dua hal, bukan lima
                  benda sederajat yang harus dibaca semua sebelum memilih. */}
              <div className="kerja-utama">
                {x.bisa_jalan ? (
                  <button
                    type="button"
                    className={"tbl" + (x.dinilai ? "" : " tbl-utama")}
                    onClick={() => { void jalankan(); }}
                  >
                    Jalankan<kbd>Ctrl ⏎</kbd>
                  </button>
                ) : null}
                {x.dinilai ? (
                  <button type="button" className="tbl tbl-utama"
                          onClick={() => { void periksa(); }}>
                    Periksa jawaban<kbd>Ctrl ⇧ ⏎</kbd>
                  </button>
                ) : null}
              </div>

              <span className="deret-kanan" />

              <div className="tbl-set">
                <button type="button" className="tbl tbl-kecil"
                        title="Simpan ke berkas (Ctrl+S)"
                        onClick={() => {
                          void simpan(pegangan.current?.nilai() ?? "", false);
                        }}>
                  Simpan
                </button>
                <button type="button" className="tbl tbl-kecil"
                        onClick={() => {
                          void salin(pegangan.current?.nilai() ?? "");
                        }}>
                  Salin
                </button>
                <button
                  type="button"
                  className="tbl tbl-kecil"
                  title="Kembalikan editor ke kerangka kosong"
                  onClick={async () => {
                    if (!globalThis.confirm(
                      "Kembalikan editor ke kerangka kosong? Kodemu yang "
                      + "sekarang hilang.")) return;
                    const r = await ambil<{ kode: string }>(
                      "/api/latihan/kerangka", { key: kunciBahasa, indeks });
                    pegangan.current?.setNilai(r.kode);
                    void simpan(r.kode, true);
                  }}
                >
                  Kerangka
                </button>
              </div>
            </div>

            {/* Satu panel bertingkat, bukan empat tombol sederajat di baris
                tindakan. Urutannya mengikuti urutan yang benar-benar menolong:
                petunjuk satu per satu lebih dulu, dan jalan keluar terakhir ada
                DI BAWAHNYA, di balik garis putus-putus. Untuk orang yang buntu,
                jalan termudah dan jalan terburuk tidak boleh berjarak sama. */}
            <details className="bantuan">
              <summary className="bantuan-kepala">
                <b>Buntu?</b>
                <span>
                  {x.hint.length ? `${x.hint.length} petunjuk tersedia`
                    : "lihat contoh solusi"}
                </span>
              </summary>
              <div className="bantuan-isi">
                <div>
                  {hintTerbuka === 0 ? (x.hint.length ? (
                    <p className="baris-sisi">
                      {`Tersedia ${x.hint.length} petunjuk. Coba sendiri dulu; `
                        + "buntu selama beberapa menit justru bagian yang "
                        + "mengajari."}
                    </p>
                  ) : null) : (
                    <div style={{ display: "grid", gap: "var(--s2)" }}>
                      {x.hint.slice(0, hintTerbuka).map((t, i) => (
                        <div key={i} className="arti masuk">
                          <b>{"Petunjuk " + (i + 1)}</b>
                          <div>{t}</div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
                {x.hint.length ? (
                  <button
                    type="button"
                    className="tbl tbl-kecil"
                    disabled={hintTerbuka >= x.hint.length}
                    onClick={() =>
                      setHintTerbuka((n) => Math.min(n + 1, x.hint.length))}
                  >
                    {hintTerbuka >= x.hint.length ? "Semua petunjuk terbuka"
                      : hintTerbuka === 0
                        ? `Buka petunjuk pertama (1/${x.hint.length})`
                        : `Buka petunjuk berikutnya (${hintTerbuka + 1}/${x.hint.length})`}
                  </button>
                ) : null}
                {/* Jalan keluar terakhir, dipisahkan garis putus-putus dan
                    ditulis paling redup. Bukan untuk menyembunyikannya -- ia
                    harus ada, dan orang yang benar-benar buntu harus bisa
                    menemukannya -- melainkan supaya ia tidak pernah jadi yang
                    pertama terbaca oleh orang yang baru dua menit mencoba. */}
                <div className="bantuan-akhir">
                  <button
                    type="button"
                    className="tbl tbl-kecil tbl-hantu"
                    onClick={() => {
                      if (!rekor.length) return;
                      /* Gerbangnya MENYATAKAN KEADAAN, tidak menghakimi, dan ia
                         memang DILEWATI begitu semua petunjuk terbuka: sesudah
                         petunjuk terakhir dibaca tidak ada lagi "coba sendiri
                         dulu" yang tersisa untuk dijaga, jadi menagih
                         konfirmasi di situ cuma menghukum yang paling gigih. */
                      const tafsir = hintTerbuka === 0
                        ? `0 dari ${x.hint.length} petunjuk terbuka, belum ada `
                          + "yang kamu buka. Petunjuk pertama biasanya sudah "
                          + "cukup, dan yang tersisa tetap kamu yang kerjakan."
                        : `Kamu membuka ${hintTerbuka} dari ${x.hint.length} `
                          + "petunjuk, itu cara yang benar untuk buntu.";
                      if (hintTerbuka < x.hint.length && !globalThis.confirm(
                        `${tafsir} Solusinya dibuka dari ekornya: `
                        + `${(rekor[0] as string[]).length} baris terakhir `
                        + `dulu, bukan ${semuaBaris.length} baris sekaligus.`,
                      )) return;
                      setRekorLangkah(0);
                    }}
                  >
                    Lihat contoh solusi
                  </button>
                  <button
                    type="button"
                    className="tbl tbl-kecil tbl-hantu"
                    onClick={() => setBanding(pasangkanUbahan(bedaBaris(
                      semuaBaris,
                      (pegangan.current?.nilai() ?? "").split("\n"),
                    )))}
                  >
                    Bandingkan dengan kodeku
                  </button>
                </div>
              </div>
            </details>
          </div>

          <div ref={panelRef} className="kerja-hasil">
            {hasil.jenis === "kosong" ? (
              <Keadaan
                jenis="kosong"
                judul={x.dinilai ? "Hasil muncul di sini"
                  : "Keluaran muncul di sini"}
                ket={x.dinilai
                  ? "Tekan Jalankan untuk melihat keluaran kodemu, atau Periksa "
                    + "jawaban untuk mengadunya dengan kunci jawaban, baris per "
                    + "baris."
                  : "Tekan Jalankan untuk melihat keluaran kodemu."}
              />
            ) : hasil.jenis === "sibuk" ? (
              <div className="kartu deret">
                <div className="pusaran" />
                <span>{hasil.pesan}</span>
              </div>
            ) : hasil.jenis === "galat" ? (
              <Keadaan jenis="salah" judul="Belum jalan" ket={hasil.pesan} />
            ) : hasil.jenis === "jalan" ? (
              <KartuJalan r={hasil.r} runner={x.runner} kode={hasil.kode}
                          batasWaktu={x.batas_waktu} tuju={tuju} />
            ) : (
              <>
                <KartuPeriksa r={hasil.r} tadi={hasil.tadi} tuju={tuju} />
                {/* Sesudah lulus: satu tombol ke latihan berikutnya, tepat di
                    bawah kartu hasil. Dulu satu-satunya jalan maju adalah panah
                    32 px di strip konteks, di pojok kanan atas, jauh dari mata
                    yang sedang membaca kartu "Benar". */}
                {hasil.r.lulus && x.indeks + 1 < x.jumlah ? (
                  <div className="deret" style={{ marginTop: "var(--s3)" }}>
                    <a className="tbl tbl-utama"
                       href={`#/latihan/${kunciBahasa}/${x.indeks + 1}`}>
                      Latihan berikutnya
                    </a>
                  </div>
                ) : null}
              </>
            )}
          </div>
        </div>
      </div>

      {/* TIDAK ada kaki "latihan sebelumnya / berikutnya" di sini, dan itu bukan
          kelalaian. Ketiga tautannya sudah dibawa strip konteks yang menempel di
          atas, jadi kaki ini akan mengulang tiga hal yang sudah terlihat sambil
          memakan sembilan puluh piksel dari ruang kerja yang justru tidak boleh
          digulir. */}

      {rekorLangkah >= 0 ? (
        <RekorSolusi
          rekor={rekor}
          langkah={rekorLangkah}
          semua={semuaBaris}
          judul={x.judul}
          sorot={x.sorot}
          solusi={x.solusi}
          onLangkah={setRekorLangkah}
          onTutup={() => setRekorLangkah(-1)}
        />
      ) : null}

      {banding ? (
        <PanelBanding baris={banding} onTutup={() => setBanding(null)} />
      ) : null}
    </div>
  );
}

/* Satu solusi, satu panel. Tangganya hidup DI DALAM panelnya, bukan sebagai
   aksi kaki: tiap aksi kaki menutup panelnya, jadi "Lihat lebih banyak" sebagai
   aksi berarti tiga panel untuk satu solusi.

   Keadaan akhir tiap langkah = keadaan alami DOM-nya. Nol animasi dan nol
   `fill: "forwards"` di sini: apa yang sudah terbuka wajib tetap terbuka pada
   gerak "mati", dan satu-satunya cara memastikannya adalah dengan tidak pernah
   menggantungkan kehadirannya pada sebuah animasi. */
function RekorSolusi({
  rekor, langkah, semua, judul, sorot, solusi, onLangkah, onTutup,
}: {
  rekor: string[][]; langkah: number; semua: string[]; judul: string;
  sorot: string; solusi: string;
  onLangkah: (n: number) => void; onTutup: () => void;
}) {
  const potongan = rekor[langkah] as string[];
  const penuh = langkah >= rekor.length - 1;
  return (
    <div className="jendela jendela-lebar" role="dialog" aria-modal="true"
         aria-label={"Contoh solusi: " + judul}>
      <h2>{"Contoh solusi: " + judul}</h2>
      <p className="kepala-sub" style={{ margin: "0 0 var(--s3)" }}>
        Ini cuma SATU cara. Kode yang berbeda belum tentu salah, selama
        outputnya sama. Yang terbuka lebih dulu baris-baris TERAKHIR: di situlah
        hasilnya dicetak, dan sering itu saja sudah cukup.
      </p>
      {/* Ditokenkan ULANG per potongan, bukan diraut dari `token_solusi`: token
          bawaan server adalah token seluruh program, dan memotong deretnya di
          tengah bisa membelah satu string atau satu komentar jadi dua -- yang
          terlihat pelajar kemudian warna yang terasa acak. */}
      <div className="blok-kode">
        <Kode kode={potongan.join("\n")} bahasa={sorot} />
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center",
                    gap: "var(--s2)", marginTop: "var(--s3)" }}>
        <span className="pil">
          {penuh ? `seluruh ${semua.length} baris`
            : `${potongan.length} baris terakhir dari ${semua.length}`}
        </span>
        {penuh ? null : (
          <button type="button" className="tbl tbl-kecil"
                  onClick={() => onLangkah(langkah + 1)}>
            Lihat lebih banyak
          </button>
        )}
        {/* Salin baru ADA saat seluruhnya terbuka. Menyalin separuh solusi
            adalah cara tercepat membuat jawaban yang salah terlihat sah: yang
            tertempel jalan, outputnya cuma sebagian, dan yang disalahkan
            pelajar adalah pemahamannya sendiri. */}
        {penuh ? (
          <button type="button" className="tbl tbl-kecil tbl-hantu"
                  onClick={() => { void salin(solusi); }}>
            Salin seluruhnya
          </button>
        ) : null}
        <span className="deret-kanan" />
        <button type="button" className="tbl tbl-utama" onClick={onTutup}>
          Tutup
        </button>
      </div>
    </div>
  );
}

function PanelBanding({
  baris, onTutup,
}: {
  baris: ButirBeda[]; onTutup: () => void;
}) {
  return (
    <div className="jendela jendela-lebar" role="dialog" aria-modal="true"
         aria-label="Kodemu dibanding contoh solusi">
      <h2>Kodemu dibanding contoh solusi</h2>
      <p className="kepala-sub" style={{ margin: "0 0 var(--s3)" }}>
        Baris hijau dari contoh solusi, baris merah dari kodemu. Yang dicoret
        hilang dari kodemu, yang bergaris bawah kamu tambahkan. Beda tulisan itu
        wajar. Yang menentukan lulus cuma outputnya.
      </p>
      <div className="diff">
        {baris.length ? baris.map((d, i) => (
          <BarisDiff
            key={i}
            nomor={d.nomor}
            tanda={d.tanda === "=" ? "│" : d.tanda}
            teks={d.teks}
            kelas={d.tanda === "=" ? "diff-sama"
              : d.tanda === "-" ? "diff-kurang" : "diff-tambah"}
            segmen={d.segmen}
          />
        )) : (
          <div className="diff-baris">
            <span className="diff-isi">Sama persis.</span>
          </div>
        )}
      </div>
      <div className="deret" style={{ marginTop: "var(--s3)" }}>
        <span className="deret-kanan" />
        <button type="button" className="tbl tbl-utama" onClick={onTutup}>
          Tutup
        </button>
      </div>
    </div>
  );
}

/* ============================================================= ruang coba */

interface BahasaAwal {
  key: string; label: string; runner: string; sorot: string; siap: boolean;
}

export function Coba({
  bahasaAwal, params, ingat,
}: {
  bahasaAwal: BahasaAwal[];
  params: { bahasa?: string; key?: string; materi?: string; bagian?: string };
  /** Penyimpan preferensi sesi; `undefined` sebagai nilai berarti baca. */
  ingat: (kunci: string, nilai?: string) => string | undefined;
}) {
  // Satu runner bisa dipakai beberapa entri LANGUAGES ("Bikin Aplikasi" juga
  // memakai java), jadi daftarnya disaring supaya tiap runner muncul sekali.
  const daftar: BahasaAwal[] = [];
  const sudah = new Set<string>();
  for (const b of bahasaAwal) {
    if (!b.siap || sudah.has(b.runner)) continue;
    sudah.add(b.runner);
    daftar.push(b);
  }
  // Bawaannya Python, bukan yang pertama di registry: ia yang paling mungkin
  // dipakai untuk mencoba sesuatu dengan cepat, dan paling sedikit upacaranya.
  const bawaan = sudah.has("python") ? "python"
    : (daftar[0] && daftar[0].runner) || "python";
  const diminta = params.bahasa || ingat("coba.bahasa");
  // Pilihan yang tersimpan bisa jadi menunjuk toolchain yang sudah dicopot;
  // jangan menyisakan pemilih tanpa nilai yang cocok.
  const awal = diminta && sudah.has(diminta) ? diminta : bawaan;
  const [bahasa, setBahasa] = useState(awal);
  const [judulContoh, setJudulContoh] = useState("");
  const [kodeAwal, setKodeAwal] = useState(
    () => ingat("coba.kode." + awal) || contohAwal(awal));
  const [stdin, setStdin] = useState(() => ingat("coba.stdin") || "");
  const [hasil, setHasil] = useState<Hasil>({ jenis: "kosong" });
  const pegangan = useRef<PeganganEditor | null>(null);
  const panelRef = useRef<HTMLDivElement>(null);

  usePinKeGalat(panelRef, hasil);

  // Dibuka dari tombol "Ruang Coba" di halaman materi: ambil blok kodenya.
  useEffect(() => {
    if (!params.key || params.materi === undefined) return;
    let dibatalkan = false;
    (async () => {
      try {
        const c = await ambil<{ bahasa: string; kode: string; judul: string }>(
          "/api/materi/contoh",
          { key: params.key, indeks: params.materi, bagian: params.bagian || 0 },
        );
        if (dibatalkan) return;
        setBahasa(c.bahasa);
        setKodeAwal(c.kode);
        setJudulContoh(c.judul);
        pegangan.current?.setNilai(c.kode);
      } catch (e) {
        if (!dibatalkan) sorak((e as Error).message, "salah");
      }
    })();
    return () => { dibatalkan = true; };
  }, [params.key, params.materi, params.bagian]);

  const sorotUntuk = (runner: string) => {
    const b = bahasaAwal.find((y) => y.runner === runner);
    return b ? b.sorot : runner;
  };

  const jalankan = useCallback(async () => {
    setHasil({ jenis: "sibuk", pesan: "Menjalankan kodemu…" });
    const kode = pegangan.current?.nilai() ?? "";
    try {
      const r = await kirim<HasilJalan>("/api/coba", { bahasa, kode, stdin });
      setHasil({ jenis: "jalan", r, kode });
    } catch (e) {
      setHasil({ jenis: "galat", pesan: (e as Error).message });
    }
  }, [bahasa, stdin]);

  const gantiBahasa = (b: string) => {
    ingat("coba.bahasa", b);
    setBahasa(b);
    const kode = ingat("coba.kode." + b) || contohAwal(b);
    setKodeAwal(kode);
    setJudulContoh("");
    pegangan.current?.setNilai(kode);
    setHasil({ jenis: "kosong" });
  };

  return (
    <div className="masuk kerja">
      <header className="kepala-besar">
        <div className="kepala-judul">
          <span className="mata">Ruang Coba</span>
          <h1>{judulContoh || "Coba kode apa pun"}</h1>
          <p className="kepala-sub">
            Tidak ada yang dinilai di sini dan tidak ada yang dicatat ke
            progresmu. Tulis apa saja, tekan Jalankan, lihat hasilnya.
          </p>
        </div>
        <div className="kepala-aksi">
          <label className="deret deret-rapat">
            <span className="mata">Bahasa</span>
            <select
              value={bahasa}
              aria-label="Bahasa yang dipakai"
              onChange={(e) => gantiBahasa(e.target.value)}
            >
              {daftar.map((b) => (
                <option key={b.runner} value={b.runner}>{b.label}</option>
              ))}
            </select>
          </label>
        </div>
      </header>

      <div className="kerja-tata kerja-tata-coba">
        <div className="kerja-kode">
          <Editor
            pegangan={pegangan}
            bahasa={sorotUntuk(bahasa)}
            kodeAwal={kodeAwal}
            label="Kode di Ruang Coba"
            isiRuang
            onUbah={(kode) => { ingat("coba.kode." + bahasa, kode); }}
            pintasan={{ "ctrl+enter": () => { void jalankan(); } }}
          />

          <div className="kerja-bawah">
            <div className="kerja-tindakan">
              <div className="kerja-utama">
                <button type="button" className="tbl tbl-utama"
                        onClick={() => { void jalankan(); }}>
                  Jalankan<kbd>Ctrl ⏎</kbd>
                </button>
              </div>
              <span className="deret-kanan" />
              <div className="tbl-set">
                <button type="button" className="tbl tbl-kecil"
                        onClick={() => {
                          void salin(pegangan.current?.nilai() ?? "");
                        }}>
                  Salin
                </button>
                <button type="button" className="tbl tbl-kecil"
                        title="Kembalikan ke contoh awal bahasa ini"
                        onClick={() => {
                          const kode = contohAwal(bahasa);
                          pegangan.current?.setNilai(kode);
                          ingat("coba.kode." + bahasa, kode);
                        }}>
                  Contoh awal
                </button>
              </div>
            </div>

            <div>
              <span className="mata">Masukan (stdin)</span>
              <textarea
                value={stdin}
                placeholder="Masukan untuk program (stdin). Kosongkan kalau tidak dipakai."
                style={{ minHeight: "62px", fontFamily: "var(--f-kode)",
                         fontSize: "var(--t-kecil)" }}
                onChange={(e) => {
                  setStdin(e.target.value);
                  ingat("coba.stdin", e.target.value);
                }}
              />
            </div>
          </div>

          <div ref={panelRef} className="kerja-hasil">
            {hasil.jenis === "kosong" ? (
              <Keadaan jenis="kosong" judul="Keluaran muncul di sini"
                       ket="Tekan Jalankan untuk melihat keluaran kodemu." />
            ) : hasil.jenis === "sibuk" ? (
              <div className="kartu deret">
                <div className="pusaran" />
                <span>{hasil.pesan}</span>
              </div>
            ) : hasil.jenis === "galat" ? (
              <Keadaan jenis="salah" judul="Belum jalan" ket={hasil.pesan} />
            ) : hasil.jenis === "jalan" ? (
              <KartuJalan r={hasil.r} runner={bahasa} kode={hasil.kode}
                          batasWaktu={0} />
            ) : null}
          </div>
        </div>
      </div>
    </div>
  );
}
