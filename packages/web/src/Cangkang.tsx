/* Cangkang aplikasi: navigasi, kelas ukuran layar, dan strip konteks.
 *
 * Port bagian CANGKANG dari `webapp/statik/js/aplikasi.js` (1.570 baris, yang
 * sebagian besarnya penangan rute -- itu digantikan router di `main.tsx`).
 *
 * Tiga aturan yang dipindahkan apa adanya karena ketiganya pernah salah:
 *
 * 1. **Butir navigasi aktif ditandai DUA kali: kelasnya dan `aria-current`.**
 *    Warna tidak dibacakan pembaca layar. Dan untuk butir yang tinggal di
 *    dalam panel yang tertutup, yang ditandai PEMICU panelnya -- `offsetWidth`
 *    butir di panel tertutup nol, jadi penanda yang meluncur tidak punya
 *    tempat berdiri, dan versi sebelumnya memadamkannya sama sekali.
 * 2. **`AMBANG_PANEL` 860 WAJIB cocok dengan `@media (max-width: 860px)` di
 *    `gaya.css`.** Kalau meleset, ada pita lebar tempat tombol menu diam saja
 *    padahal panelnya satu-satunya jalan ke menu.
 * 3. **Kelas ukuran dipasang bersama ISI yang baru, bukan di awal transisi.**
 *    Menyetelnya lebih dulu berarti layar LAMA yang masih terlihat ditata ulang
 *    ke lebar layar berikutnya -- yang terlihat bukan pergantian melainkan isi
 *    lama yang melompat melebar tepat sebelum memudar. Di React itu gratis:
 *    kelas dan isi berasal dari satu render yang sama.
 */

import { useCallback, useEffect, useMemo, useRef, useState,
         type ReactNode } from "react";
import { arahkanLangit, nyalakanLangit } from "./langit.ts";
import { nyalakanKursor } from "./kursor.ts";
import { pasangSorot } from "./permukaan.ts";
import { ungkapJudulSaatTiba } from "./sinema.ts";
import { masuk, pasangIsyarat } from "./gerak.ts";

import { Ikon } from "./komponen/Ikon.tsx";
import { Lencana, MajuBaca } from "./komponen/Lencana.tsx";
import { Palet } from "./komponen/Palet.tsx";
import type { BahasaPalet } from "./komponen/palet-cari.ts";
import { Bantuan, usePintasanCangkang } from "./komponen/Pintasan.tsx";
import { temaBerikutnya } from "./lokal.ts";
import { sorak } from "./sorak.tsx";

/* Layar yang butuh ruang penuh: pembaca materi memakai tiga kolom, dan editor
   lebih enak tanpa batas lebar. */
const LAYAR_LEBAR = new Set(["latihan", "coba", "materi", "langit"]);

/* Layar yang mengisi TINGGI jendela alih-alih tumbuh dari isinya: dua layar
   tempat orang MENULIS KODE. Editor yang setinggi isinya berarti kerangka tiga
   baris menyisakan empat ratus piksel kosong di bawahnya -- ruang kerja yang
   menolak dipakai bekerja. */
const LAYAR_PENUH = new Set(["latihan", "coba"]);

/* Layar yang isinya pada dasarnya SATU kolom daftar, jadi memakai ukuran
   halaman yang lebih sempit. Alasannya bukan kelapangan: daftar satu kolom
   yang dipaksa selebar 1164 px menaruh judul materi di tepi kiri dan
   penandanya di tepi kanan dengan delapan ratus piksel kosong di antaranya --
   dan dua ujung yang sejauh itu berhenti terbaca sebagai satu baris. */
const LAYAR_KOLOM = new Set([
  "bahasa", "kuis", "bookmark", "catatan", "cari", "statistik", "atur",
  "pustaka", "karier", "tebak",
]);

/** ANGKA INI DIPAKAI JUGA DI `gaya.css` (blok `@media 860px`). Jaga cocok. */
const AMBANG_PANEL = 860;

type Butir = [nama: string, label: string, href: string];

/* Layar "pintu": yang dibuka untuk MEMILIH, bukan untuk dikerjakan. Sama
   persis dengan `LAYAR_PINTU` di `aplikasi.js`. */
const LAYAR_PINTU = new Set(["dasbor", "bahasa", "statistik", "bookmark",
                             "catatan", "atur", "pustaka", "karier"]);

const MENU_UTAMA: Butir[] = [
  ["dasbor", "Dasbor", "#/dasbor"],
  ["langit", "Langit", "#/langit"],
  ["pustaka", "Pustaka", "#/pustaka"],
  ["karier", "Karier", "#/karier"],
  ["coba", "Ruang Coba", "#/coba"],
];

const MENU_LAIN: Butir[] = [
  ["catatan", "Catatanku", "#/catatan"],
  ["bookmark", "Bookmark", "#/bookmark"],
  ["statistik", "Statistik", "#/statistik"],
  ["atur", "Pengaturan", "#/atur"],
];

/** Yang dikembalikan tiap layar supaya strip konteks bisa dibangun router. */
export interface Konteks {
  balik: { label: string; href: string };
  bab?: string;
  judul?: string;
  posisi?: string;
  persen?: number;
  langkah?: boolean;
  sebelum?: string;
  sesudah?: string;
  judulSebelum?: string;
  judulSesudah?: string;
}

/**
 * Strip konteks. Remah roti sudah TIDAK ada.
 *
 * Penggantinya satu strip tempel yang dibangun dari objek `konteks` yang
 * dikembalikan tiap layar. Layar yang TIDAK punya posisi mengembalikan
 * `undefined`, dan stripnya tidak dirender sama sekali -- 44 piksel itu kembali
 * jadi milik isinya. Alasannya bukan estetika: remah roti lama berbunyi
 * "Belajar › HTML › 3. Struktur Dokumen", dan dua dari tiga ruasnya mengulang
 * judul yang sudah tertulis besar-besar tepat di bawahnya.
 *
 * Konsekuensi yang mengikat: apa pun yang sudah dibawa strip TIDAK boleh
 * digambar lagi di badan halaman.
 */
function StripKonteks({ k }: { k: Konteks }) {
  /* Tombol langkah yang tidak punya tujuan tetap DIGAMBAR, sebagai `<span>`
     redup. Melepasnya dari DOM akan mengubah lebar strip tiap kali pindah
     materi, dan pergeseran sepuluh piksel di bilah yang menempel terbaca
     sebagai halaman yang goyang -- bukan sebagai tombol yang tidak ada. */
  const langkah = (arah: "sebelum" | "sesudah", href?: string, judul?: string) => {
    const tanda = <Ikon nama={arah === "sebelum" ? "kembali" : "lanjut"} ukuran={18} />;
    return href ? (
      <a href={href} title={judul ?? ""} aria-label={judul ?? arah}>
        {tanda}
      </a>
    ) : (
      <span aria-hidden="true">{tanda}</span>
    );
  };

  return (
    <div id="konteks">
      <a className="konteks-balik" href={k.balik.href}>
        <Ikon nama="kembali" ukuran={16} />
        {k.balik.label}
      </a>
      <div className="konteks-tengah">
        {k.bab ? <span className="konteks-bab">{k.bab}</span> : null}
        {k.judul ? <span className="konteks-judul">{k.judul}</span> : null}
      </div>
      {k.posisi ? (
        <div className="konteks-maju">
          <span className="konteks-angka">{k.posisi}</span>
        </div>
      ) : null}
      {k.langkah ? (
        <div className="konteks-langkah">
          {langkah("sebelum", k.sebelum, k.judulSebelum)}
          {langkah("sesudah", k.sesudah, k.judulSesudah)}
        </div>
      ) : null}
    </div>
  );
}

export function Cangkang({
  rute,
  alamat,
  konteks,
  bahasa,
  children,
}: {
  /** Nama rute aktif, untuk menandai navigasi dan memilih kelas ukuran. */
  rute: string;
  /** Alamat LENGKAP, termasuk parameternya.
   *
   *  Dipisah dari `rute` karena transisi harus menyala saat berpindah dari
   *  satu bahasa ke bahasa lain -- di situ nama rutenya SAMA (`bahasa`) dan
   *  cuma parameternya berganti, padahal yang terjadi di layar pergantian
   *  halaman seutuhnya. Menandainya dengan `rute` saja berarti perpindahan
   *  yang paling sering dilakukan di aplikasi ini justru yang tidak pernah
   *  dianimasikan. */
  alamat?: string;
  konteks?: Konteks;
  /** Daftar kurikulum untuk palet perintah. Dari `/api/awal`. */
  bahasa: BahasaPalet[];
  children: ReactNode;
}) {
  const [panelBuka, setPanelBuka] = useState(false);
  /* Lencana disegarkan pada setiap pergantian rute, dan itu memang kasar --
     tapi pergantian rute adalah SATU-SATUNYA isyarat yang pasti tersedia di
     cangkang: XP naik di dalam sebuah layar (materi tuntas, latihan lulus,
     kuis dijawab), dan cangkang tidak pernah tahu kapan. Menyiarkannya dari
     tiap layar berarti tiga tempat yang harus ingat memanggilnya. */
  const putaranUkuran = useMemo(() => rute, [rute]);
  const [bantuanBuka, setBantuanBuka] = useState(false);
  const [paletBuka, setPaletBuka] = useState(false);

  /* Kedua callback DIBUNGKUS `useCallback`, dan itu bukan optimasi: keduanya
     dependensi efek yang memasang pendengar `keydown` di `document`. Fungsi
     literal baru pada setiap render berarti pendengar itu dilepas dan dipasang
     ulang pada setiap render -- dan keadaan `g` yang tinggal di dalam efeknya
     ikut hilang setiap kali, jadi rangkaian "G lalu D" tidak akan pernah
     selesai. */
  const bukaBantuan = useCallback(() => setBantuanBuka(true), []);
  const alihPanel = useCallback(() => setPanelBuka((b) => !b), []);
  const bukaPalet = useCallback(() => setPaletBuka(true), []);
  usePintasanCangkang({
    onBantuan: bukaBantuan, onAlihPanel: alihPanel, onPalet: bukaPalet,
  });
  const [sempit, setSempit] = useState(
    () => globalThis.innerWidth <= AMBANG_PANEL,
  );

  useEffect(() => {
    const media = matchMedia(`(max-width: ${AMBANG_PANEL}px)`);
    const dengar = () => {
      setSempit(media.matches);
      // Melebar melewati ambang membuat panel tidak lagi jadi satu-satunya
      // jalan ke menu, jadi ia ditutup -- panel yang menggantung terbuka di
      // layar lebar menutupi isi tanpa alasan.
      if (!media.matches) setPanelBuka(false);
    };
    media.addEventListener("change", dengar);
    return () => media.removeEventListener("change", dengar);
  }, []);

  // Esc menutup panel. Tanpa ini satu-satunya jalan keluar adalah menemukan
  // kembali tombol yang membukanya, yang kini tertutup panelnya sendiri.
  useEffect(() => {
    if (!panelBuka) return;
    const dengar = (e: KeyboardEvent) => {
      if (e.key === "Escape") setPanelBuka(false);
    };
    globalThis.addEventListener("keydown", dengar);
    return () => globalThis.removeEventListener("keydown", dengar);
  }, [panelBuka]);

  /* Langit dipasang SESUDAH `#latar` ada di DOM -- ia mencarinya lewat
     `getElementById`, jadi memanggilnya di tingkat modul akan mendapat null
     dan diam-diam tidak melakukan apa pun. Pelepasnya dipakai: `StrictMode`
     menjalankan efek dua kali, dan tanpa melepas pendengar `pointermove`,
     `resize`, dan kedua `MutationObserver`, setiap pemasangan menumpuk satu
     langit lagi di belakang yang lama. */
  /* ---------------------------------------------------- transisi rute ---
     Isi `#layar` dianimasikan MASUK tiap kali rutenya berganti. Di React
     tidak ada "DOM lama" untuk dianimasikan keluar seperti di `aplikasi.js`
     -- React sudah menukarnya sebelum efek ini jalan -- jadi yang tersisa
     setengah geraknya, dan itu yang benar: `keluar()` di sisi JS ada supaya
     halaman lama tidak lenyap mendadak, sementara di sini ia memang tidak
     pernah sempat terlihat lenyap.

     `masuk()` memakai `fill: "backwards"`, jadi keadaan AKHIR-nya keadaan
     alami elemennya. Gerak yang dimatikan berarti layarnya langsung berdiri
     di tempatnya -- bukan tak terlihat selamanya. */
  const layarRef = useRef<HTMLElement>(null);
  useEffect(() => {
    if (!layarRef.current) return;
    masuk(layarRef.current, { geser: 8, zum: 0.995, pegas: "halus" });
    // Dan langitnya ikut diarahkan ulang: berpindah layar di aplikasi ini
    // adalah instrumen yang diputar ke sasaran baru, bukan halaman yang
    // ditukar. Ia memakai peredam paralaks yang sudah ada -- nol animasi
    // baru, nol properti yang diperebutkan dua mesin.
    arahkanLangit();
  }, [rute, alamat]);

  /* Judul kata demi kata, HANYA di layar "pintu". Materi, latihan, kuis, dan
     Ruang Coba sengaja tidak ikut: ketiganya dibuka ratusan kali dalam satu
     sesi panjang, dan gerak yang menyenangkan di kunjungan pertama jadi
     penghalang di kunjungan keempat puluh. Daftarnya sama persis dengan
     `LAYAR_PINTU` di `aplikasi.js`. */
  useEffect(() => {
    if (!LAYAR_PINTU.has(rute) || !layarRef.current) return;
    return ungkapJudulSaatTiba(layarRef.current);
  }, [rute, alamat]);

  /* ------------------------------------------------ umpan balik tekan ---
     Seluruhnya di `pasangIsyarat()` (gerak.ts), port dari `gerak.js`: satu
     pendengar di tingkat dokumen, daftar putih `BISA_DITEKAN`, dan elemen yang
     DITEKAN-lah yang dilepas -- di mana pun jari diangkat.

     Versi pertama di sini menulis penangannya sendiri, dengan komentar yang
     menyebut antarmuka lama "NOL pemanggil" `tekan()`. Itu keliru: pemanggilnya
     `pasangIsyarat()` di dalam `gerak.js` sendiri, dan tes lamanya malah
     melarang komponen memanggil `tekan()` langsung. Penangan buatan sendiri itu
     memilih sasaran dengan `button, a, [role="button"]` (termasuk node SVG
     Peta Karier) dan melepas `closest(target)` saat `pointerup`. Akibatnya node
     yang ditekan melompat ke titik asal SVG, `pointerup` mendarat di elemen
     lain, dan node itu terparkir di pojok kiri atas selamanya -- sampai klik
     mouse tidak bisa memilih node sama sekali. */
  useEffect(() => pasangIsyarat(), []);

  const latarRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!latarRef.current) return;
    return nyalakanLangit();
  }, []);

  /* Reticle teleskop dan sorot permukaan. Keduanya memasang pendengar di
     tingkat DOKUMEN, jadi keduanya WAJIB mengembalikan pelepas: `StrictMode`
     menjalankan efek dua kali, dan reticle yang dipasang dua kali berarti dua
     set braket yang saling menimpa. Versi JS-nya tidak pernah melepas apa pun
     karena di sana modulnya memang dimuat sekali seumur halaman. */
  useEffect(() => nyalakanKursor(), []);
  useEffect(() => pasangSorot(), []);

  const diPanel = MENU_LAIN.some(([nama]) => nama === rute);

  /* `<li><a>`, BUKAN `<a>` telanjang. `gaya.css` mendesain butir navigasi
     lewat `.rel-menu a` (21 aturan), dan `.rel-menu` itu sebuah `<ul>`.
     Versi pertama cangkang ini mengarang `.rel-butir` di dalam `.rel-deret`
     -- dua kelas yang NOL kali muncul di stylesheet, jadi nol aturan berlaku
     dan navigasinya tampil sebagai teks telanjang berdempetan. */
  const butir = ([nama, label, href]: Butir) => {
    const ini = nama === rute;
    return (
      <li key={nama}>
      <a
        className={ini ? "kini" : undefined}
        href={href}
        // `aria-current` WAJIB ikut dipasang DAN dilepas: warna tidak
        // dibacakan pembaca layar, jadi kelas `.kini` saja tidak pernah cukup.
        aria-current={ini ? "page" : undefined}
        onClick={() => setPanelBuka(false)}
      >
        <span className="nama">{label}</span>
      </a>
      </li>
    );
  };

  /* KETIGA kelas ukuran menempel di `#layar`, BUKAN di `#panggung`, dan itu
     bukan selera: `gaya.css` menulis selektornya `#layar.lebar`,
     `#layar.kolom`, `#layar.penuh`. Versi pertama cangkang ini memasang `lebar`
     dan `kolom` di `#panggung` -- lolos `tsc`, lolos pembacaan sepintas (nama
     variabel `panggung` di `aplikasi.js` justru menunjuk `$("#layar")`), dan
     tidak menimbulkan satu pun error. Yang terjadi: tidak ada satu pun dari
     kedua aturan itu yang pernah berlaku, jadi SELURUH halaman daftar berhenti
     di 1240 px alih-alih 1400 (diukur: 1240 lawan 1400 pada jendela 1440), dan
     SELURUH layar lebar -- pembaca materi, ruang kerja, Langit -- yang
     seharusnya `max-width: none` juga terjepit di 1240.

     `berkonteks` tetap di `#panggung`: ia memang ditulis `#panggung.berkonteks`
     dan ia yang mengatur ruang untuk strip tempel di atasnya. */
  const kelasLayar =
    (LAYAR_LEBAR.has(rute) ? "lebar " : "") +
    (LAYAR_KOLOM.has(rute) ? "kolom " : "") +
    (LAYAR_PENUH.has(rute) ? "penuh" : "");

  return (
    <>
      {/* Lapisan latar: grain fraktal plus satu cahaya lebar dari atas layar,
          keduanya DIAM. Lima aturan `#latar` di `gaya.css` tidak pernah punya
          elemen untuk dikenakan sampai sekarang, jadi kanvasnya rata gelap.
          Bintang dan garis rasi di atasnya digambar `langit.ts` ke dalam
          elemen ini; yang di sini lapisan dasarnya, dan ia berdiri sendiri
          kalau kanvas langitnya tidak pernah menyala. */}
      <div id="latar" ref={latarRef} aria-hidden="true" />
      <div id="cangkang" className={panelBuka ? "rel-buka" : undefined}>
      {/* `id="rel"`, dan itu bukan kosmetik: 25 aturan di `gaya.css` menunjuk
          `#rel`, termasuk SELURUH bentuk "pil melayang di tengah atas" di
          blok `@media (min-width: 861px)`. Versi pertama memberinya
          `className="pil-atas"` -- nama yang dipakai KOMENTAR blok itu, bukan
          selektornya -- jadi nol dari 25 aturan berlaku dan yang tersisa
          bilah lengket telanjang. Komentar CSS-nya sendiri sudah menuliskan
          kontraknya: "DOM-nya SAMA dengan bilah atas lebar sempit -- yang
          berubah cuma bentuknya."

          `pakai-tanda` sengaja TIDAK dipasang: ia menyalakan penanda meluncur
          yang posisinya dihitung `tandaiRel()` di antarmuka lama, dan penanda
          tanpa penghitungnya akan berdiri di koordinat nol. Tanpa kelas itu,
          yang menandai butir aktif `.rel-menu a.kini::before` -- yang memang
          sudah ada di stylesheet. */}
      <nav id="rel" aria-label="Navigasi utama">
        <a className="merek" href="#/dasbor">
          <span className="merek-bara" aria-hidden="true" />
          <span className="merek-teks">
            <b>belajar</b>
            <i>codingV2</i>
          </span>
        </a>

        <div id="rel-lipat" className="rel-lipat" hidden={sempit && !panelBuka}>
          <ul id="rel-utama" className="rel-menu">
            {MENU_UTAMA.map(butir)}
          </ul>

          {/* Pemicu panel ikut ditandai `.kini` kalau butir yang aktif tinggal
              DI DALAM panel. Tanpa itu, membuka Statistik atau Pengaturan
              membuat navigasi tidak menyalakan apa pun sama sekali -- butir di
              panel tertutup ber-`offsetWidth` nol. */}
          <div className={"rel-turun rel-turun-kanan" + (panelBuka ? " buka" : "")}>
            <button
              type="button"
              className={"rel-pemicu" + (diPanel ? " kini" : "")}
              aria-expanded={panelBuka}
              aria-current={diPanel ? "true" : undefined}
              onClick={() => setPanelBuka((b) => !b)}
            >
              Lainnya
              <span className="rel-panah" aria-hidden="true">▾</span>
            </button>
            <div className="rel-panel">
              <ul className="rel-menu">{MENU_LAIN.map(butir)}</ul>
            </div>
          </div>
        </div>

        {/* Pembuka palet, di tempat yang sama dengan antarmuka lama. Petunjuk
            `Ctrl K` ikut dipasang karena pintasannya memang ada -- dan ia
            TOMBOL, bukan tautan: yang dibukanya dialog, dan tautan yang tidak
            pernah berpindah halaman adalah tautan yang membohongi menu
            konteks serta tombol tengah tetikus. */}
        <button
          type="button"
          className="rel-tombol"
          onClick={() => {
            setPanelBuka(false);
            setPaletBuka(true);
          }}
        >
          <span className="ikon" aria-hidden="true">
            <Ikon nama="cari" ukuran={16} />
          </span>
          <span className="rel-label">Cari apa saja</span>
          <kbd>Ctrl K</kbd>
        </button>

        <div id="ukuran">
          {/* Lencana streak dan XP. Keduanya TAUTAN ke Statistik, bukan tombol
              seperti di antarmuka lama: di sana keduanya `<button>` yang tidak
              melakukan apa pun saat ditekan -- dan tombol yang tidak menjawab
              tekanan adalah tombol yang membuat orang menekannya dua kali lalu
              menyimpulkan aplikasinya macet. Yang dijanjikan judulnya (level,
              gelar, rekor streak) memang ada di layar Statistik. */}
          <Lencana putaran={putaranUkuran} />
          {/* Pengganti tombol tema di antarmuka lama (Ctrl+J di sana).
              Keempat tema tetap bisa dipilih satu per satu di Pengaturan;
              tombol ini cuma memutarnya, dan ia ada karena mengganti tema
              adalah hal yang dilakukan di tengah membaca -- bukan hal yang
              pantas menuntut dua kali pindah layar. */}
          <button
            type="button"
            className="ikon-tombol"
            title="Ganti tema"
            aria-label="Ganti tema"
            onClick={() => sorak("Tema: " + temaBerikutnya(), "", 1.6)}
          >
            <Ikon nama="tema" ukuran={18} />
          </button>
          <button
            type="button"
            className="ikon-tombol"
            title="Pintasan papan ketik (?)"
            aria-label="Bantuan pintasan"
            onClick={bukaBantuan}
          >
            <Ikon nama="bantuan" ukuran={18} />
          </button>
        </div>

        {/* Bilah kemajuan baca menempel di KAKI bilah ini, bukan di bilah
            kedua: bilah kedua cuma ada di layar yang punya konteks, sementara
            halaman panjang bisa muncul di mana saja. */}
        <MajuBaca rute={rute} />
      </nav>

      <div id="panggung" className={konteks ? "berkonteks" : undefined}>
        {konteks ? <StripKonteks k={konteks} /> : null}
        <main
          id="layar"
          ref={layarRef}
          className={kelasLayar.trim() || undefined}
        >
          {children}
        </main>
      </div>

      {bantuanBuka ? <Bantuan onTutup={() => setBantuanBuka(false)} /> : null}
      {paletBuka ? (
        <Palet bahasa={bahasa} onTutup={() => setPaletBuka(false)} />
      ) : null}
      </div>
    </>
  );
}
