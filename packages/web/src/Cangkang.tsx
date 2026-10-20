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

import { useEffect, useState, type ReactNode } from "react";

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
    const tanda = arah === "sebelum" ? "‹" : "›";
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
  konteks,
  children,
}: {
  /** Nama rute aktif, untuk menandai navigasi dan memilih kelas ukuran. */
  rute: string;
  konteks?: Konteks;
  children: ReactNode;
}) {
  const [panelBuka, setPanelBuka] = useState(false);
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

  const diPanel = MENU_LAIN.some(([nama]) => nama === rute);

  const butir = ([nama, label, href]: Butir) => {
    const ini = nama === rute;
    return (
      <a
        key={nama}
        className={"rel-butir" + (ini ? " kini" : "")}
        href={href}
        // `aria-current` WAJIB ikut dipasang DAN dilepas: warna tidak
        // dibacakan pembaca layar, jadi kelas `.kini` saja tidak pernah cukup.
        aria-current={ini ? "page" : undefined}
        onClick={() => setPanelBuka(false)}
      >
        {label}
      </a>
    );
  };

  const kelasPanggung =
    (LAYAR_LEBAR.has(rute) ? "lebar " : "") +
    (LAYAR_KOLOM.has(rute) ? "kolom " : "") +
    (konteks ? "berkonteks" : "");

  return (
    <div id="cangkang" className={panelBuka ? "rel-buka" : undefined}>
      <nav className="pil-atas" aria-label="Navigasi utama">
        <a className="merek" href="#/dasbor">
          <span className="merek-teks">
            <b>belajar</b>
            <i>codingV2</i>
          </span>
        </a>

        <div id="rel-alih" className="rel-deret">
          {MENU_UTAMA.map(butir)}

          {/* Pemicu panel ikut ditandai `.kini` kalau butir yang aktif tinggal
              DI DALAM panel. Tanpa itu, membuka Statistik atau Pengaturan
              membuat navigasi tidak menyalakan apa pun sama sekali -- butir di
              panel tertutup ber-`offsetWidth` nol. */}
          <button
            type="button"
            className={"rel-pemicu" + (diPanel ? " kini" : "")}
            aria-expanded={panelBuka}
            aria-current={diPanel ? "true" : undefined}
            onClick={() => setPanelBuka((b) => !b)}
          >
            Lainnya
          </button>
        </div>

        <div className="rel-lipat" hidden={sempit && !panelBuka}>
          {MENU_LAIN.map(butir)}
        </div>
      </nav>

      <div id="panggung" className={kelasPanggung.trim() || undefined}>
        {konteks ? <StripKonteks k={konteks} /> : null}
        <main id="layar" className={LAYAR_PENUH.has(rute) ? "penuh" : undefined}>
          {children}
        </main>
      </div>
    </div>
  );
}
