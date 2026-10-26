/* Pembaca materi.
 *
 * Port `layarMateri`, `artikelMateri`, `kolomMateri`, `petaBagian`,
 * `pasangFokus`, dan `pintasanPembaca` dari `webapp/statik/js/layar-belajar.js`.
 * Bagian murninya (`potong`, `labelPeta`) di `belajar-teks.ts`, blok kodenya di
 * `komponen/BlokKode.tsx`, prosanya di `komponen/Prosa.tsx`.
 *
 * Empat aturan dari AGENTS.md yang membentuk layar ini:
 *
 * 1. **Materi dihitung selesai HANYA kalau dibaca sampai habis.** Yang
 *    memutuskan `progress.py`; layar ini cuma melaporkan "sudah sampai ujung"
 *    lewat `IntersectionObserver` di penanda paling bawah.
 * 2. **Jangan pernah menyimpulkan sendiri sebuah bab sudah terbuka.** "Ini
 *    materi terakhir bab, berarti bab berikutnya terbuka" adalah definisi KEDUA
 *    tentang penguncian. Jawabannya ditanyakan ulang ke server dan dibacakan.
 * 3. **`scrollIntoView` dilarang untuk jalur materi.** Ia menggulir setiap
 *    leluhur yang bisa digulir, termasuk dokumen -- `bawaKeTengah()` menyentuh
 *    `scrollTop`/`scrollLeft` wadahnya saja.
 * 4. **Apa pun yang sudah dibawa strip konteks TIDAK digambar lagi di badan
 *    halaman.** Itu sebabnya kolom jalur tidak punya tautan "kembali ke
 *    bahasa", dan kepala materi tidak punya `.materi-balik`.
 */

import {
  useCallback, useEffect, useLayoutEffect, useRef, useState, type ReactNode,
} from "react";

import { ambil, kirim, GalatApi } from "../api.ts";
import { adaGerak } from "../gerak.ts";
import { ambilLokal, simpanLokal } from "../lokal.ts";
import { rayakan, type Hadiah } from "../sorak.tsx";
import { tanpaNomor } from "../util.tsx";
import { BlokKode, type BagianKode } from "../komponen/BlokKode.tsx";
import { Ikon } from "../komponen/Ikon.tsx";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { TombolBookmark, TombolCatatan } from "../komponen/Tanda.tsx";
import { BlokProsa, type Blok } from "../komponen/Prosa.tsx";
import { Visual } from "../komponen/Visual.tsx";
import type { SpekUmum } from "../komponen/visual-bentuk.ts";
import { labelPeta, potong } from "./belajar-teks.ts";
import type { Konteks } from "../Cangkang.tsx";

/* ====================================================== bentuk jawaban API */

interface BagianProsa {
  jenis: "prosa";
  judul?: string;
  blok: Blok[];
  visual?: SpekUmum[];
}
type Bagian = BagianProsa | (BagianKode & { visual?: SpekUmum[] });

interface BabMateri {
  nomor: number;
  judul: string;
  tingkat: string;
  label_tingkat: string;
  jumlah: number;
  selesai: number;
}

interface DataMateri {
  bahasa: string;
  label_bahasa: string;
  sorot: string;
  indeks: number;
  jumlah: number;
  judul: string;
  sebelum: string;
  sesudah: string;
  bagian: Bagian[];
  status: string;
  bab: BabMateri;
  bookmark: boolean;
  kunci: string;
  /* OBJEK, bukan string. `api.materi` mengirim `{teks, diubah}` -- tipe lama
     di sini menyebutnya `string`, dan itu tidak pernah terlihat karena tidak
     ada satu pun pemakainya sampai tombol catatan dipasang. */
  catatan: { teks?: string; diubah?: string } | null;
}

interface ButirMateri {
  indeks: number;
  judul: string;
  status: string;
  bab: number;
  terkunci: boolean;
}
interface BabDaftar {
  nomor: number;
  judul: string;
  status: string;
  selesai: number;
  jumlah: number;
  alasan: string;
  materi: number[];
}
interface DataBahasa {
  key: string;
  label: string;
  runner: string;
  sorot: string;
  siap: boolean;
  statistik: { materi: number; total_materi: number };
  materi: ButirMateri[];
  bab: BabDaftar[];
}

/* ================================================================== jalur */

/**
 * Bawa sebuah butir ke tengah wadahnya, TANPA `scrollIntoView`.
 *
 * Dua arah diurus sekaligus karena jalur materi memang berganti arah: kolom
 * tegak yang menggulir ke bawah di layar lebar, satu jalur yang menggulir ke
 * samping di layar sempit.
 */
function bawaKeTengah(wadah: HTMLElement | null, butir: HTMLElement | null) {
  if (!wadah || !butir) return;
  const w = wadah.getBoundingClientRect();
  const b = butir.getBoundingClientRect();
  if (wadah.scrollHeight > wadah.clientHeight + 4) {
    wadah.scrollTop += (b.top - w.top) - (w.height - b.height) / 2;
  }
  if (wadah.scrollWidth > wadah.clientWidth + 4) {
    wadah.scrollLeft += (b.left - w.left) - (w.width - b.width) / 2;
  }
}

/**
 * Kolom kiri: jalur seluruh materi bahasa ini, dikelompokkan per bab.
 *
 * Tidak ada tautan "kembali ke bahasa" di kepala jalur ini, dan itu bukan
 * kelalaian: strip konteks yang menempel di atas halaman sudah membawanya,
 * selalu terlihat, di tempat yang sama di semua layar belajar. Dua jalan pulang
 * yang berjarak empat puluh piksel bukan dua pilihan -- ia satu pilihan yang
 * digambar dua kali.
 */
function KolomMateri({
  b, indeksKini, kunciBahasa,
}: {
  b: DataBahasa; indeksKini: number; kunciBahasa: string;
}) {
  const akarRef = useRef<HTMLElement>(null);
  const daftarRef = useRef<HTMLOListElement>(null);

  /* Jalurnya menggulir SENDIRI ke butir yang sedang dibaca. Tanpa ini, membuka
     materi ke-20 dari 26 menampilkan jalur yang tergulir di paling atas --
     butir yang sedang dibaca ada di luar pandangan, dan yang terlihat justru
     daftar yang sudah lama dilewati.

     `useLayoutEffect`, bukan `useEffect`: keduanya mengukur kotak, dan mengukur
     sesudah peramban melukis berarti satu frame terlihat tergulir di tempat
     yang salah lebih dulu. */
  useLayoutEffect(() => {
    const kini = daftarRef.current?.querySelector<HTMLElement>("a.kini");
    if (!kini) return;
    bawaKeTengah(akarRef.current, kini);
    bawaKeTengah(daftarRef.current, kini);
  }, [indeksKini]);

  const bab = new Map(b.bab.map((x) => [x.nomor, x]));
  // Satu bab saja = tidak ada yang dikelompokkan.
  const berbab = b.bab.length > 1;
  const butir: ReactNode[] = [];
  let babKini: number | null = null;

  for (const x of b.materi) {
    if (berbab && x.bab !== babKini) {
      babKini = x.bab;
      const bb = bab.get(babKini);
      if (bb) {
        const kunci = bb.status === "terkunci";
        butir.push(
          <li key={"bab" + bb.nomor} className="materi-rel-bab"
              data-bab={String(bb.nomor)}>
            <span className="materi-rel-bab-judul">
              {`Bab ${bb.nomor} · ${bb.judul}`}
            </span>
            {/* Angkanya ditandai berbeda saat babnya terkunci karena keduanya
                tidak sama pentingnya: di layar sempit "3/7" boleh mengalah demi
                judul yang utuh, sedangkan "terkunci" adalah satu-satunya
                keterangan yang menjelaskan kenapa butir di bawahnya tidak bisa
                ditekan. */}
            <span className={"materi-rel-bab-angka" + (kunci ? " kunci" : "")}>
              {kunci ? "terkunci" : `${bb.selesai}/${bb.jumlah}`}
            </span>
          </li>,
        );
      }
    }

    const kini = x.indeks === indeksKini;
    const alasan = x.terkunci ? bab.get(x.bab)?.alasan : undefined;
    // Yang terkunci tetap ditulis dengan bentuk yang sama persis -- jalurnya
    // harus terbaca utuh -- tapi TANPA href. `<a>` tanpa href bukan tautan bagi
    // siapa pun: tidak bisa diklik, tidak disinggahi Tab, dan tidak diumumkan
    // pembaca layar sebagai tautan.
    butir.push(
      <li key={x.indeks}>
        <a
          className={(kini ? "kini" : "") + (x.terkunci ? " terkunci" : "")}
          data-indeks={String(x.indeks)}
          {...(x.terkunci
            ? {} : { href: `#/materi/${kunciBahasa}/${x.indeks}` })}
          {...(alasan ? { title: alasan } : {})}
          {...(kini ? { "aria-current": "page" as const } : {})}
        >
          <span className="materi-rel-nomor">{String(x.indeks + 1)}</span>
          <span className="materi-rel-judul">{tanpaNomor(x.judul)}</span>
          {/* Penanda status, dan ia BUKAN hiasan: di jalur yang menyimpan dua
              puluh judul, ini satu-satunya yang membedakan "sudah dibaca" dari
              "dibaca sebagian". Artinya tetap ikut dibacakan pembaca layar lewat
              `aria-label` tautannya, bukan lewat ikon ini. */}
          {x.status === "selesai" ? (
            <Ikon nama="selesai" ukuran={16} kelas="materi-rel-tanda" />
          ) : x.status === "sebagian" ? (
            <Ikon nama="sedang" ukuran={16} kelas="materi-rel-tanda" />
          ) : null}
        </a>
      </li>,
    );
  }

  return (
    <aside ref={akarRef} className="materi-rel">
      <div className="mata">
        {`Materi · ${b.statistik.materi}/${b.statistik.total_materi}`}
      </div>
      <ol ref={daftarRef} className="materi-rel-daftar">{butir}</ol>
    </aside>
  );
}

/* ============================================================= peta bagian */

/**
 * Bawa sebuah bagian ke tepi atas kolom baca, TANPA `scrollIntoView`.
 *
 * Di sini yang digulir memang dokumennya, jadi masalahnya bukan leluhur
 * melainkan PENDARATANNYA: `block: "start"` menghormati `scroll-padding-top`,
 * dan nilai itu terukur 26 px lebih kecil daripada dasar chrome yang menempel
 * di pembaca (72 px lawan 98 px) karena `--lengket-atas` diisi ulang di subtree
 * `#panggung`, tempat yang tidak bisa dilihat aturan di `html`.
 *
 * Jaraknya dibaca dari `scrollPaddingTop` yang SUDAH terhitung, bukan disalin
 * sebagai angka. Jadi tidak ada angka kedua yang bisa melenceng: kalau CSS-nya
 * berubah, pendaratannya ikut.
 */
function bawaKeAtas(sasaran: HTMLElement) {
  const pad = parseFloat(
    getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
  const atas = sasaran.getBoundingClientRect().top + globalThis.scrollY - pad;
  globalThis.scrollTo({ top: Math.max(0, atas),
                        behavior: adaGerak() ? "smooth" : "auto" });
}

interface ButirPeta { i: number; judul: string; jenis: string }

function butirPeta(bagian: Bagian[]): ButirPeta[] {
  const keluar: ButirPeta[] = [];
  bagian.forEach((bg, i) => {
    let judul = bg.judul;
    if (!judul && bg.jenis === "kode") {
      judul = (bg.petunjuk && bg.petunjuk.nama) || "Contoh kode";
    }
    if (!judul && bg.jenis === "prosa") judul = labelPeta(bg);
    if (!judul) return;
    keluar.push({ i, judul, jenis: bg.jenis });
  });
  return keluar;
}

/**
 * Bagian yang sedang dibaca = bagian TERAKHIR yang tepinya sudah melewati
 * sepertiga atas layar. Aturan "yang paling banyak terlihat" terdengar lebih
 * benar tapi terasa gelisah: penandanya melompat bolak-balik tiap kali dua
 * bagian pendek bergantian mengisi layar.
 *
 * Aturan itu hidup di SATU tempat -- `hitungAktif` di bawah -- dan dipanggil
 * dari DUA jalur: pengamat persilangan menangkap perubahan yang terjadi TANPA
 * gulir (tata letak yang bergeser, gambar yang selesai dimuat, jendela yang
 * diubah ukurannya), dan pendengar `scroll` menangkap perpindahan yang TIDAK
 * melintasi ambang pengamatnya.
 *
 * Kenapa pengamatnya TIDAK cukup sendirian, dan ini terukur bukan dikira: ia
 * hanya dipanggil ulang kalau ada bagian yang MELINTASI ambangnya. Dari puncak
 * halaman ke bagian pertama (gulir 0 -> 241 px di 1440), bagian 0 sudah memotong
 * pita `rootMargin` di KEDUA posisi -- tidak ada ambang yang dilewati, callback
 * tidak jalan, dan penandanya tetap -1 padahal aturannya sudah memberi jawaban
 * 0. Penekanan `]` berikutnya membaca -1 lagi dan mendarat di tempat yang sama.
 */
function usePetaAktif(
  artikelRef: React.RefObject<HTMLElement | null>, butir: ButirPeta[],
): number {
  const [aktif, setAktif] = useState(-1);

  useEffect(() => {
    const artikel = artikelRef.current;
    if (!artikel || butir.length < 2) return;

    const hitungAktif = () => {
      let n = -1;
      butir.forEach((x, k) => {
        const anak = artikel.children[x.i] as HTMLElement | undefined;
        if (anak
            && anak.getBoundingClientRect().top
               <= globalThis.innerHeight * 0.34) {
          n = k;
        }
      });
      setAktif(n);
    };

    hitungAktif();
    const dengar = () => hitungAktif();
    globalThis.addEventListener("scroll", dengar, { passive: true });

    let hentikan = () => {};
    if (typeof IntersectionObserver !== "undefined") {
      const pengamat = new IntersectionObserver(hitungAktif,
        { rootMargin: "-30% 0px -55% 0px", threshold: [0, 1] });
      for (const x of butir) {
        const anak = artikel.children[x.i];
        if (anak) pengamat.observe(anak);
      }
      hentikan = () => pengamat.disconnect();
    }
    return () => {
      globalThis.removeEventListener("scroll", dengar);
      hentikan();
    };
  }, [artikelRef, butir]);

  return aktif;
}

function PetaBagian({
  butir, aktif, artikelRef,
}: {
  butir: ButirPeta[];
  aktif: number;
  artikelRef: React.RefObject<HTMLElement | null>;
}) {
  // Peta kosong adalah KEADAAN, bukan ketiadaan: kelasnya tetap dipasang supaya
  // kisi tiga kolomnya tidak kehilangan satu track.
  if (butir.length < 2) {
    return <aside className="materi-peta materi-peta-kosong" />;
  }
  return (
    <aside className="materi-peta">
      <div className="mata">Di halaman ini</div>
      <nav className="materi-peta-daftar">
        {butir.map((x, n) => (
          <a
            key={x.i}
            href="#"
            className={n === aktif ? "kini" : undefined}
            onClick={(e) => {
              e.preventDefault();
              const sasaran = artikelRef.current?.children[x.i] as
                HTMLElement | undefined;
              if (sasaran) bawaKeAtas(sasaran);
            }}
          >
            <span>{x.judul}</span>
          </a>
        ))}
      </nav>
    </aside>
  );
}

/* ============================================================== mode fokus */

/**
 * Mode fokus pembaca: kolom daftar materi dan peta halaman disingkirkan, kolom
 * baca berdiri sendiri di tengah, dan navbar meredup sampai disentuh.
 *
 * Untuk sesi membaca yang panjang, yang melelahkan bukan teksnya melainkan
 * semua yang bukan teks: dua kolom di kiri-kanan yang terus tertangkap sudut
 * mata, dan bilah navigasi yang tidak pernah dipakai selama membaca. Strip
 * konteks (kembali, posisi, maju-mundur) TIDAK ikut disembunyikan -- tanpa itu
 * mode fokus berubah jadi jalan buntu.
 *
 * Pilihannya diingat per browser (preferensi tampilan, bukan capaian belajar),
 * tapi kelasnya hidup HANYA selama pembaca terpasang: pembersih efeknya WAJIB
 * mencabutnya, atau navbar dasbor ikut redup.
 */
function useFokusBaca(): [boolean, () => void] {
  /* `<boolean>` eksplisit, dan `=== true` BUKAN basa-basi: nilai di
     localStorage ditulis versi lain dari aplikasi ini dan bisa apa pun. Tanpa
     tipe itu, `ambilLokal` menyimpulkan `false` sebagai tipe literalnya dan
     tsc menolak pembandingnya; tanpa pembandingnya, string `"0"` yang
     kebetulan tersimpan di situ akan menyalakan mode fokus. */
  const [nyala, setNyala] = useState(
    () => ambilLokal<boolean>("fokus_baca", false) === true);

  useEffect(() => {
    const akar = document.documentElement;
    akar.classList.toggle("fokus-baca", nyala);
    return () => akar.classList.remove("fokus-baca");
  }, [nyala]);

  const alih = useCallback(() => {
    setNyala((v) => {
      simpanLokal("fokus_baca", !v);
      return !v;
    });
  }, []);

  return [nyala, alih];
}

/* ====================================================== pintasan papan ketik */

/* Tabel pintasan pembaca materi. SATU tabel, dibaca penangan di bawah -- bukan
   deretan cabang `if` yang tersebar. Kolom pertamanya lambang yang
   DITAMPILKAN, dan itu disengaja: daftar bantuan di layar Pengaturan adalah
   definisi KEDUA dari lapisan ini, dan dua definisi yang tidak pernah
   dibandingkan adalah dua definisi yang suatu hari berbeda tanpa ada yang
   menyadarinya.

   `?` sengaja TIDAK di sini. Pemiliknya cangkang aplikasi, dan tombol yang
   punya dua pemilik adalah tombol yang perilakunya bergantung pada urutan
   pendaftaran pendengar. */
export const PINTASAN_PEMBACA: Array<[string, string]> = [
  ["j", "Blok kode berikutnya"],
  ["k", "Blok kode sebelumnya"],
  ["]", "Bagian berikutnya"],
  ["[", "Bagian sebelumnya"],
  ["f", "Mode fokus"],
  ["⏎", "Jalankan blok kode yang sedang difokus"],
];

/**
 * Lapisan papan ketik halaman materi: `j`/`k` antar blok kode, `[`/`]` antar
 * bagian, `⏎` menjalankan blok yang sedang difokus, `f` mode fokus.
 *
 * Kenapa blok kode yang dapat pintasan, dan bukan paragraf: blok kode
 * satu-satunya hal di halaman ini yang bisa DIKERJAKAN. Menggulir prosa sudah
 * punya alatnya sendiri di setiap peramban; melompat ke contoh berikutnya lalu
 * menjalankannya tanpa melepas papan ketik tidak punya.
 *
 * BENTURAN YANG DITERIMA APA ADANYA: `g` lalu `j`. Cangkang memakai rangkaian
 * ala Vim `g` + huruf, dan `j` bukan salah satu tujuannya -- jadi menekan `g`
 * lalu `j` memindahkan fokus satu blok kode sementara keadaan `g` di sana masih
 * menyala. Menyalin keadaan itu ke layar ini akan membuat dua salinan satu
 * keadaan, dan itu ongkos yang lebih besar daripada benturannya. Ditulis di
 * sini supaya ia tercatat sebagai keputusan, bukan ditemukan lagi sebagai
 * kejutan.
 */
function usePintasanPembaca(
  artikelRef: React.RefObject<HTMLElement | null>,
  butir: ButirPeta[],
  aktifRef: React.RefObject<number>,
  alihFokus: () => void,
) {
  useEffect(() => {
    // Urutan sasaran dihitung dari posisi VERTIKAL nyata, bukan dari urutan
    // dokumen. Keduanya sama hari ini; yang membuat mereka berbeda adalah
    // perubahan tata letak apa pun di kemudian hari, dan saat itu terjadi yang
    // benar adalah yang dilihat mata.
    const daftarBlok = () => {
      const artikel = artikelRef.current;
      if (!artikel) return [] as HTMLElement[];
      return [...artikel.querySelectorAll<HTMLElement>(".blok-kode")]
        .sort((a, b) =>
          a.getBoundingClientRect().top - b.getBoundingClientRect().top);
    };

    const keBlok = (arah: number) => {
      const daftar = daftarBlok();
      if (!daftar.length) return false;
      const i = daftar.indexOf(document.activeElement as HTMLElement);
      // Dijepit di ujung, tidak dilingkar.
      const tuju = i >= 0
        ? Math.max(0, Math.min(daftar.length - 1, i + arah))
        : (arah > 0 ? 0 : daftar.length - 1);
      const sasaran = daftar[tuju];
      if (!sasaran) return false;
      sasaran.focus({ preventScroll: true });
      bawaKeAtas(sasaran);
      return true;
    };

    const keBagian = (arah: number) => {
      const artikel = artikelRef.current;
      if (!artikel || butir.length < 2) return false;
      const i = aktifRef.current;
      const tuju = Math.max(0, Math.min(butir.length - 1, i + arah));
      const sasaran = artikel.children[(butir[tuju] as ButirPeta).i] as
        HTMLElement | undefined;
      if (!sasaran) return false;
      bawaKeAtas(sasaran);
      return true;
    };

    const jalankanFokus = () => {
      const blok = (document.activeElement as HTMLElement | null)
        ?.closest<HTMLElement>(".blok-kode");
      const tbl = blok?.querySelector<HTMLButtonElement>(
        ".blok-alat .tbl-utama");
      if (!tbl) return false;
      tbl.click();
      return true;
    };

    const saatTombol = (e: KeyboardEvent) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      // Pengetikan di editor sisipan tidak boleh ikut tertangkap: `j` di dalam
      // kode adalah huruf, bukan perintah.
      const t = e.target as HTMLElement | null;
      if (t && (t.tagName === "TEXTAREA" || t.tagName === "INPUT"
                || t.isContentEditable)) return;
      let kena = false;
      if (e.key === "j") kena = keBlok(+1);
      else if (e.key === "k") kena = keBlok(-1);
      else if (e.key === "]") kena = keBagian(+1);
      else if (e.key === "[") kena = keBagian(-1);
      else if (e.key === "f") { alihFokus(); kena = true; }
      else if (e.key === "Enter") kena = jalankanFokus();
      // `preventDefault()` HANYA kalau benar-benar ada yang dikerjakan. `⏎`
      // yang mendarat saat fokusnya bukan blok kode wajib tetap menekan tombol
      // atau membuka tautan yang sedang difokus.
      if (kena) e.preventDefault();
    };

    document.addEventListener("keydown", saatTombol);
    return () => document.removeEventListener("keydown", saatTombol);
  }, [artikelRef, butir, aktifRef, alihFokus]);
}

/* ================================================================== layar */

export function Belajar({
  kunciBahasa, indeks, onKonteks,
}: {
  kunciBahasa: string;
  indeks: number;
  onKonteks: (k: Konteks | undefined) => void;
}) {
  const [m, setM] = useState<DataMateri | null>(null);
  const [b, setB] = useState<DataBahasa | null>(null);
  const [terkunci, setTerkunci] = useState("");
  const [galat, setGalat] = useState("");
  const [status, setStatus] = useState("");
  const [pintuBaru, setPintuBaru] = useState<
    { href: string; label: string } | null>(null);
  const artikelRef = useRef<HTMLElement>(null);
  const penandaRef = useRef<HTMLDivElement>(null);
  const [fokus, alihFokus] = useFokusBaca();

  /* Dua permintaan SEKALIGUS, bukan berurutan: daftar materi bahasa ini dipakai
     untuk kolom kiri, dan menunggunya setelah materinya sendiri selesai berarti
     membayar dua kali perjalanan untuk satu layar.

     `allSettled`, bukan `all`: materi yang babnya belum terbuka dijawab 403, dan
     403 di sini BUKAN kegagalan -- ia jawaban yang punya layarnya sendiri.
     Dengan `all`, penolakan yang pertama membuat permintaan bahasa yang sudah
     telanjur jalan jadi penolakan tanpa penangkap, dan justru data itulah yang
     dibutuhkan untuk menjelaskan apa yang sedang terkunci. */
  useEffect(() => {
    let dibatalkan = false;
    setM(null); setB(null); setTerkunci(""); setGalat(""); setPintuBaru(null);
    (async () => {
      const [jm, jb] = await Promise.allSettled([
        ambil<DataMateri>("materi", { key: kunciBahasa, indeks }),
        ambil<DataBahasa>("bahasa", { key: kunciBahasa }),
      ]);
      if (dibatalkan) return;
      const bhs = jb.status === "fulfilled" ? jb.value : null;
      if (bhs) setB(bhs);

      if (jm.status === "rejected") {
        const e = jm.reason as Error;
        /* 403 juga dipakai untuk token yang sudah tidak sah (servernya
           dinyalakan ulang sementara tab ini terbuka), dan pembedanya
           sederhana: penguncian bab cuma berlaku untuk satu materi, jadi
           permintaan bahasanya pasti tetap berhasil. Kalau KEDUANYA ditolak,
           yang tertutup bukan babnya melainkan sesinya. */
        if (bhs && e instanceof GalatApi && e.kode === 403) {
          setTerkunci(e.message);
        } else {
          setGalat(e.message);
        }
        return;
      }
      if (!bhs) {
        setGalat("Daftar materi tidak terbaca.");
        return;
      }

      const d = jm.value;
      setM(d);
      setStatus(d.status);
      onKonteks({
        balik: { label: d.label_bahasa, href: "#/bahasa/" + kunciBahasa },
        ...(bhs.bab.length > 1 && d.bab
          ? { bab: `Bab ${d.bab.nomor} · ${d.bab.judul}` } : {}),
        judul: tanpaNomor(d.judul),
        posisi: `${d.indeks + 1} / ${d.jumlah}`,
        langkah: true,
        ...(d.indeks > 0 && d.sebelum
          ? { sebelum: `#/materi/${kunciBahasa}/${d.indeks - 1}`,
              judulSebelum: tanpaNomor(d.sebelum) } : {}),
        ...(d.sesudah
          ? { sesudah: `#/materi/${kunciBahasa}/${d.indeks + 1}`,
              judulSesudah: tanpaNomor(d.sesudah) } : {}),
      });

      /* Dibuka tapi belum tuntas dicatat sebagai "sebagian" -- tanpa XP.
         Aturannya milik `progress.py`: materi dihitung selesai HANYA kalau
         dibaca sampai habis, dan antarmuka ini tidak berhak melonggarkannya. */
      if (d.status === "baru") {
        kirim("materi/selesai", { key: kunciBahasa, indeks, tuntas: false })
          .catch(() => {});
        setStatus("sebagian");
      }
    })();
    return () => { dibatalkan = true; };
  }, [kunciBahasa, indeks, onKonteks]);

  /** Tawarkan materi berikutnya kalau bab yang memuatnya BARU SAJA terbuka.
   *
   *  Saat halaman ini digambar, tetangga di bab yang masih terkunci sengaja
   *  dikosongkan server -- jadi materi terakhir sebuah bab datang tanpa tombol
   *  "berikutnya". Yang menuntaskan bab itu justru pembacaan halaman ini
   *  sendiri, dan tanpa langkah di bawah orang yang baru saja menyelesaikan
   *  sebuah bab berdiri di halaman yang satu-satunya jalannya ke BELAKANG,
   *  tepat pada momen yang seharusnya jadi hadiahnya.
   *
   *  Yang TIDAK dilakukan di sini: menyimpulkan sendiri bahwa babnya sudah
   *  terbuka. Jawabannya ditanyakan ulang ke server dan cuma dibacakan.
   *
   *  Gagal bertanya = tidak menawarkan apa-apa. Tombol yang muncul karena
   *  tebakan lebih buruk daripada tombol yang tidak muncul: yang pertama
   *  mengantar ke layar "belum terbuka" sesudah menjanjikan kebalikannya. */
  const tawarkanPintuBaru = useCallback(async () => {
    if (!m || m.sesudah || m.indeks + 1 >= m.jumlah || pintuBaru) return;
    let baru: DataBahasa;
    try {
      baru = await ambil<DataBahasa>("bahasa", { key: kunciBahasa });
    } catch {
      return;
    }
    const lanjut = baru.materi.find((x) => x.indeks === m.indeks + 1);
    if (!lanjut || lanjut.terkunci) return;
    // Kolom kiri digambar ulang dari data BARU, bukan ditambal di tempat.
    // Membiarkannya berarti tombol di kaki halaman mengumumkan "Bab 3 terbuka"
    // sementara seluruh Bab 3 di sebelahnya masih tertulis "terkunci" -- dua
    // jawaban berbeda untuk pertanyaan yang sama, di satu layar.
    setB(baru);
    const bb = baru.bab.find((x) => x.materi.includes(lanjut.indeks));
    setPintuBaru({
      href: `#/materi/${kunciBahasa}/${lanjut.indeks}`,
      label: bb
        ? `Bab ${bb.nomor} terbuka: ${potong(tanpaNomor(lanjut.judul), 22)}`
        : potong(tanpaNomor(lanjut.judul), 26),
    });
  }, [m, kunciBahasa, pintuBaru]);

  const tandaiSelesai = useCallback(async (pindah: boolean) => {
    if (!m) return;
    if (status !== "selesai") {
      setStatus("selesai");
      const hasil = await kirim<Hadiah>("materi/selesai",
        { key: kunciBahasa, indeks, tuntas: true });
      rayakan(hasil);
    }
    if (pindah && m.sesudah) {
      globalThis.location.hash = `#/materi/${kunciBahasa}/${m.indeks + 1}`;
    } else {
      await tawarkanPintuBaru();
    }
  }, [m, status, kunciBahasa, indeks, tawarkanPintuBaru]);

  /* Sampai di ujung halaman = benar-benar dibaca habis. Ini padanan web dari
     paginasi terminal, yang juga hanya menandai tuntas kalau halaman
     terakhirnya dilewati. */
  useEffect(() => {
    const penanda = penandaRef.current;
    if (!penanda || !m || status === "selesai") return;
    if (typeof IntersectionObserver === "undefined") return;
    const pengamat = new IntersectionObserver((catatan) => {
      if (catatan.some((c) => c.isIntersecting)) void tandaiSelesai(false);
    }, { rootMargin: "0px 0px -40px 0px" });
    // Ditunda satu tik: pada materi yang lebih pendek daripada jendela,
    // penandanya sudah terlihat pada frame pertama -- dan menandai tuntas
    // SEBELUM halamannya sempat dilihat bukan "dibaca sampai habis".
    const jam = setTimeout(() => pengamat.observe(penanda), 80);
    return () => { clearTimeout(jam); pengamat.disconnect(); };
  }, [m, status, tandaiSelesai]);

  const butir = m ? butirPeta(m.bagian) : [];
  const aktif = usePetaAktif(artikelRef, butir);
  const aktifRef = useRef(aktif);
  aktifRef.current = aktif;
  usePintasanPembaca(artikelRef, butir, aktifRef, alihFokus);

  if (galat) {
    return <Keadaan jenis="salah" judul="Materi tidak terbuka" ket={galat} />;
  }
  if (terkunci && b) {
    const bb = b.bab.find((x) => x.materi.includes(indeks));
    return (
      <Keadaan
        jenis="kunci"
        judul={bb ? `Bab ${bb.nomor} belum terbuka`
          : "Materi ini belum terbuka"}
        ket={terkunci}
        aksi={
          <a className="tbl tbl-utama" href={"#/bahasa/" + kunciBahasa}>
            Lihat daftar materi
          </a>
        }
      />
    );
  }
  if (!m || !b) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat materi…</span>
      </div>
    );
  }

  const berbab = b.bab.length > 1;
  const jumlahKode = m.bagian.filter((x) => x.jenis === "kode").length;

  return (
    <div className="masuk materi-tata">
      <KolomMateri b={b} indeksKini={m.indeks} kunciBahasa={kunciBahasa} />

      <div className="materi-utama">
        {/* Kartu aksi tinggal DI SINI, bukan di antara anak `.materi-tata`.
            `.materi-tata` adalah kisi dua kolom (>=1130) dan tiga kolom (>=1380)
            dengan tepat TIGA item tata letak: rail, kolom utama, peta bagian.
            Selama kartunya `fixed` ia tidak memakan track -- tapi begitu sebuah
            aturan membuatnya `static`, ia jadi item keempat yang ditempatkan
            otomatis dan MENGGESER saudara-saudaranya. Di dalam `.materi-utama`
            (yang `display: block`) `static` cuma berarti satu baris di atas
            kepala materi, dan `fixed` tidak berubah sama sekali.

            RELOKASI, bukan duplikasi: tombol "Tandai selesai" keluar dari
            `nav.materi-kaki` dan tinggal di sini saja. Kaki tetap memegang
            tautan sebelum/sesudah dan tombol beraksen "selesai lalu lanjut",
            yang SENGAJA tidak ikut naik -- ia satu-satunya permukaan beraksen
            di layar ini, dan menaikkannya membuat tindakan utama yang kedua. */}
        <aside className="aksi-tepi masuk-mandiri"
               aria-label="Tindakan untuk materi ini">
          <button type="button" className="tbl"
                  onClick={() => { void tandaiSelesai(false); }}>
            {status === "selesai" ? (
              <>
                <Ikon nama="selesai" ukuran={15} tebal={2} />
                Sudah selesai
              </>
            ) : (
              "Tandai selesai"
            )}
          </button>
          {/* RELOKASI, bukan duplikasi: kedua tombol ini keluar dari
              `div.materi-alat` yang karena itu bubar. Keduanya memakai
              komponen bersama `Tanda.tsx`, yang sama dengan yang dipakai
              kepala kuis dan kepala ruang kerja latihan -- bukan tiga salinan
              yang suatu hari berbeda soal `aria-pressed`. */}
          <TombolBookmark
            kunciBahasa={kunciBahasa}
            tipe="materi"
            indeks={indeks}
            awal={m.bookmark}
          />
          <TombolCatatan kunci={m.kunci} awal={m.catatan} judul={m.judul} />
          <button
            type="button"
            className={"ikon-tombol" + (fokus ? " aktif" : "")}
            aria-pressed={fokus}
            title={fokus ? "Keluar dari mode fokus (F)" : "Mode fokus (F)"}
            aria-label={fokus ? "Keluar dari mode fokus (F)" : "Mode fokus (F)"}
            onClick={alihFokus}
          >
            <Ikon nama="panel" ukuran={19} />
          </button>
        </aside>

        {/* Kepala sengaja PENDEK. Yang dulu berdiri di sini: satu baris mata,
            judul, lalu EMPAT pil dan dua tombol berteks penuh -- dua ratus
            piksel metadata sebelum kata pertama pelajaran. Tiga dari empat pil
            itu menjawab pertanyaan yang belum ditanyakan siapa pun saat halaman
            baru dibuka; mereka turun ke KAKI artikel, tempat pertanyaannya
            memang muncul. */}
        <header className="kepala-besar kepala-materi">
          <span className="mata">
            {berbab && m.bab
              ? `Bab ${m.bab.nomor} · ${m.bab.judul}`
              : `${m.label_bahasa} · materi ${m.indeks + 1} dari ${m.jumlah}`}
          </span>
          <h1>{tanpaNomor(m.judul)}</h1>
          <div className="kepala-aksi">
            <div className="deret deret-rapat">
              <span className="pil">
                {`materi ${m.indeks + 1} dari ${m.jumlah}`}
              </span>
              {berbab && m.bab ? (
                <span
                  className={"pil bab-tingkat bab-" + m.bab.tingkat}
                  title={`Tingkat ${m.bab.label_tingkat.toLowerCase()} · `
                    + `${m.bab.selesai} dari ${m.bab.jumlah} materi bab ini `
                    + "sudah dibaca tuntas"}
                >
                  {m.bab.label_tingkat}
                </span>
              ) : null}
            </div>
          </div>
        </header>

        <article ref={artikelRef} className="prosa">
          {m.bagian.map((bg, i) => (bg.jenis === "prosa" ? (
            <section key={i}
                     className={bg.judul === "Di dunia nyata"
                       ? "dunia-nyata" : undefined}>
              {bg.judul ? <h3>{bg.judul}</h3> : null}
              {bg.blok.map((blk, j) => <BlokProsa key={j} blk={blk} />)}
              {(bg.visual || []).map((sp, j) => <Visual key={j} spek={sp} />)}
            </section>
          ) : (
            // Gambar menempel pada blok TERAKHIR bagiannya, tidak pernah jadi
            // blok sendiri: peta bagian dan tautan Ruang Coba menunjuk blok
            // lewat indeks, jadi menyisipkan satu simpul akan menggeser
            // semuanya.
            (bg.visual || []).length ? (
              <div key={i} className="blok-bergambar">
                <BlokKode
                  b={bg} indeksBagian={i} kunciBahasa={kunciBahasa}
                  indeksMateri={m.indeks} judulMateri={m.judul}
                  sorotMateri={m.sorot} runnerBahasa={b.runner}
                  siapBahasa={b.siap}
                />
                {(bg.visual || []).map((sp, j) => <Visual key={j} spek={sp} />)}
              </div>
            ) : (
              <BlokKode
                key={i}
                b={bg} indeksBagian={i} kunciBahasa={kunciBahasa}
                indeksMateri={m.indeks} judulMateri={m.judul}
                sorotMateri={m.sorot} runnerBahasa={b.runner}
                siapBahasa={b.siap}
              />
            )
          )))}
        </article>

        <div className="materi-meta">
          <span className={"pil" + (status === "selesai" ? " pil-tumbuh" : "")}>
            {status === "selesai" ? "sudah dibaca tuntas" : "belum tuntas"}
          </span>
          <span className="pil">
            <Ikon nama="bagian" ukuran={14} tebal={1.9} />
            {`${m.bagian.length} bagian`}
          </span>
          {jumlahKode ? (
            <span className="pil">
              <Ikon nama="latihan" ukuran={14} tebal={1.9} />
              {`${jumlahKode} contoh kode`}
            </span>
          ) : null}
        </div>

        <nav className="materi-kaki">
          {/* `sebelum`/`sesudah` sengaja dikosongkan server kalau tetangganya
              ada di bab yang masih terkunci. Memakai `m.indeks > 0` saja pernah
              cukup; sekarang tidak lagi -- tombol tanpa nama yang mengantar ke
              403 adalah cara paling membingungkan untuk memberi tahu bahwa
              sesuatu belum boleh dibuka. */}
          {m.indeks > 0 && m.sebelum ? (
            <a className="tbl tbl-hantu"
               href={`#/materi/${kunciBahasa}/${m.indeks - 1}`}>
              <Ikon nama="kembali" ukuran={17} />
              {potong(m.sebelum, 26)}
            </a>
          ) : (
            <a className="tbl tbl-hantu" href={"#/bahasa/" + kunciBahasa}>
              <Ikon nama="kembali" ukuran={17} />
              Daftar materi
            </a>
          )}
          <span className="deret-kanan" />
          {m.sesudah ? (
            <button type="button" className="tbl tbl-utama"
                    onClick={() => { void tandaiSelesai(true); }}>
              {potong(m.sesudah, 26)}
            </button>
          ) : null}
          {pintuBaru ? (
            <a className="tbl tbl-utama tbl-pintu" href={pintuBaru.href}>
              {pintuBaru.label}
              <Ikon nama="lanjut" ukuran={17} />
            </a>
          ) : null}
        </nav>

        <div ref={penandaRef} style={{ height: "1px" }} />
      </div>

      <PetaBagian butir={butir} aktif={aktif} artikelRef={artikelRef} />
    </div>
  );
}
