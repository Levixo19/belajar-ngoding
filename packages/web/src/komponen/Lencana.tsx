/* Lencana streak dan XP di bilah atas, plus bilah kemajuan baca.
 *
 * Port blok `ukuran` dan `maju baca` dari `webapp/statik/js/aplikasi.js`.
 * Keduanya tinggal di satu berkas karena keduanya milik CANGKANG, bukan milik
 * sebuah layar: mereka hidup selama aplikasinya hidup dan tidak pernah
 * digambar ulang saat rute berganti.
 *
 * `/api/dasbor` diambil SEKALI di sini dan diambil lagi oleh layar Dasbor, dan
 * itu memang dua permintaan untuk satu jawaban. Alternatifnya menaruh datanya
 * di context lalu dibagi -- dan itu berarti lencana yang baru saja naik karena
 * satu latihan lulus harus menunggu layar yang sedang terbuka selesai dengan
 * datanya. Yang dipilih: lencana punya sumbernya sendiri, dan `segarkan()`
 * dipanggil dari peristiwa yang memang mengubah XP.
 */

import { useCallback, useEffect, useRef, useState } from "react";

import { ambil } from "../api.ts";
import { adaGerak } from "../gerak.ts";
import { angka } from "../util.ts";

/** Medan `/api/dasbor` yang dibaca lencana. Sengaja cuma yang dipakai. */
interface Ukuran {
  xp: number;
  level: number;
  gelar: string;
  streak: number;
  streak_rekor: number;
  xp_hari_ini: number;
  target_harian: number;
}

/**
 * Angka yang BERJALAN naik, tidak melompat. Port `angkaKe()` dari `gerak.js`.
 *
 * Ini salah satu dari sedikit animasi di aplikasi ini yang benar-benar
 * MENYAMPAIKAN sesuatu: melihat 43 merangkak jadi 68 memberi tahu berapa yang
 * barusan didapat, dan angka yang berganti begitu saja tidak pernah bisa.
 *
 * `tabular-nums` dipatok SEBELUM cabang gerak, bukan sesudah. Kalau tidak,
 * tingkat gerak `mati` dan angka yang tidak berubah tetap menukar teksnya
 * tanpa pernah mendapat properti itu -- dan digit proporsional menggeser apa
 * pun yang berdiri di sebelahnya.
 */
function useAngkaJalan(ke: number, format: (n: number) => string): string {
  const [tampil, setTampil] = useState(() => format(ke));
  const sebelumnya = useRef(ke);

  useEffect(() => {
    const dari = sebelumnya.current;
    sebelumnya.current = ke;
    if (!adaGerak() || dari === ke) {
      setTampil(format(ke));
      return;
    }
    const DURASI = 620;
    const mulai = performance.now();
    let id = requestAnimationFrame(function langkah(kini: number) {
      const t = Math.min(1, Math.max(0, (kini - mulai) / DURASI));
      const e = 1 - Math.pow(1 - t, 3); // easeOutCubic
      setTampil(format(dari + (ke - dari) * e));
      if (t < 1) id = requestAnimationFrame(langkah);
      else setTampil(format(ke));
    });
    return () => cancelAnimationFrame(id);
    // `format` sengaja tidak jadi dependensi: pemanggilnya meneruskan fungsi
    // literal, jadi memasukkannya berarti animasi ini mulai ulang pada setiap
    // render induknya.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [ke]);

  return tampil;
}

/**
 * Dua lencana di bilah atas: streak dan XP.
 *
 * `title` BUKAN nama aksesibel (WCAG 4.1.2), jadi `aria-label` dipasang
 * terpisah dengan kalimat yang sama -- aturan yang sama yang sudah dipegang
 * versi JS-nya.
 */
export function Lencana({ putaran }: { putaran: string }) {
  const [d, setD] = useState<Ukuran | null>(null);

  const segarkan = useCallback(() => {
    // Lencana cuma hiasan; kegagalannya tidak boleh mengganggu apa pun, jadi
    // galatnya ditelan dan yang tertinggal angka terakhir yang benar.
    ambil<Ukuran>("dasbor")
      .then(setD)
      .catch(() => {});
  }, []);

  useEffect(segarkan, [segarkan, putaran]);

  // `rayakan()` menyiarkan `progres-berubah` setiap kali sebuah aksi memberi
  // XP, badge, atau menulis progres; tanpa pendengar ini angkanya baru
  // menyusul saat rute berganti.
  useEffect(() => {
    document.addEventListener("progres-berubah", segarkan);
    return () => document.removeEventListener("progres-berubah", segarkan);
  }, [segarkan]);

  const streakTeks = useAngkaJalan(d?.streak ?? 0, (n) => String(Math.round(n)));
  const xpTeks = useAngkaJalan(d?.xp ?? 0, (n) => String(Math.round(n)));

  // Tiga keadaan, dan tak satu pun menyebut kata "terputus": teks ini tampil di
  // SETIAP layar, termasuk untuk orang yang belum pernah punya streak dan
  // selagi datanya belum termuat. Kalimatnya menjelaskan hitungannya dan apa
  // yang memulainya, bukan menyatakan sesuatu telah hilang.
  const judulStreak = !d
    ? "Streak: jumlah hari berurutan kamu belajar"
    : d.streak
      ? `Streak ${d.streak} hari berjalan · rekor ${d.streak_rekor} hari`
      : d.streak_rekor
        ? `Belum ada hari berurutan sekarang · rekor ${d.streak_rekor} hari. `
          + "Satu hal kecil hari ini memulai hitungan baru."
        : "Belum ada hari berurutan. Satu hal kecil hari ini memulai hitungannya.";
  // Gelar adalah tingkat dari total XP, bukan penilaian kemampuan; target
  // harian punya bawaan yang tak pernah dijelaskan ke pelajar baru.
  const judulXp = d
    ? `Level ${d.level}, gelar ${d.gelar} (tingkat dari total XP) · `
      + `${d.xp_hari_ini} dari ${d.target_harian} XP target hari ini, `
      + "bisa diubah di Pengaturan"
    : "Total XP dan level";

  return (
    <>
      <a
        className={"tanda tanda-api" + (d && d.streak > 0 ? " menyala" : "")}
        href="#/statistik"
        title={judulStreak}
        aria-label={judulStreak}
      >
        <span className="tanda-ikon" aria-hidden="true" />
        <span className="tanda-angka" style={{ fontVariantNumeric: "tabular-nums" }}>
          {streakTeks}
        </span>
      </a>
      <a
        className="tanda"
        href="#/statistik"
        title={judulXp}
        aria-label={d ? `${angka(d.xp)} XP total. ` + judulXp : judulXp}
      >
        <span className="tanda-angka" style={{ fontVariantNumeric: "tabular-nums" }}>
          {xpTeks}
        </span>
        <span className="tanda-satuan">XP</span>
      </a>
    </>
  );
}

/* Browser yang bisa menggerakkan bilah maju baca sendiri lewat
   scroll-timeline. Diperiksa SEKALI: jawabannya tidak berubah sepanjang umur
   halaman, dan menanyakannya tiap rute berarti membayar parse CSS di jalur
   navigasi. */
const MAJU_LEWAT_CSS =
  typeof CSS !== "undefined" &&
  typeof CSS.supports === "function" &&
  CSS.supports("animation-timeline: scroll(root block)");

/**
 * Garis tipis di kaki bilah navigasi yang mengikuti posisi gulir.
 *
 * SATU MESIN PER BROWSER, bukan dua yang saling menimpa. Di browser yang
 * mendukung scroll-timeline, `transform` bilah ini sepenuhnya milik CSS dan
 * pendengar gulirnya TIDAK dipasang sama sekali -- bukan dipasang lalu
 * dibiarkan menulis nilai yang sama diam-diam. Di browser lain CSS-nya tidak
 * pernah menyala (ia di balik `@supports`) dan JS yang memegangnya.
 *
 * Yang tidak ikut pindah: kelas `.tampak`. Ia menggerakkan `opacity`, bukan
 * `transform`, jadi ia bukan mesin kedua untuk properti yang sama -- dan
 * syaratnya ("halamannya memang cukup panjang untuk digulir") tidak bisa
 * dinyatakan CSS.
 *
 * `data-mesin` ditulis supaya jumlah mesin yang hidup bisa DIBUKTIKAN dari
 * luar, bukan disimpulkan dari membaca kode ini.
 */
export function MajuBaca({ rute }: { rute: string }) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const garis = ref.current;
    if (!garis) return;
    const cukupPanjang = () =>
      document.documentElement.scrollHeight - window.innerHeight > 260;

    /* Kelas `.tampak` DIUKUR ULANG saat dokumennya tumbuh, dan itu bukan
       kelengkapan: di antarmuka lama router MENUNGGU datanya sebelum
       menempelkan layarnya, jadi `pasangMajuBaca()` selalu mengukur halaman
       yang sudah penuh. Di React cangkang digambar LEBIH DULU -- saat efek ini
       jalan, dasbor masih sebuah pusaran setinggi seratus piksel. Terukur:
       tanpa pengamat di bawah, bilahnya tetap tersembunyi di halaman 2.235 px
       sementara antarmuka lama menampilkannya. */
    const pantau = () => garis.classList.toggle("tampak", cukupPanjang());

    if (MAJU_LEWAT_CSS) {
      pantau();
      if (typeof ResizeObserver !== "function") return;
      // Mengamati `documentElement`, bukan `body`: `scrollHeight` yang
      // dibandingkan di `cukupPanjang()` miliknya, dan body yang tingginya
      // ditentukan isinya tidak selalu ikut berubah ukuran.
      const pengamat = new ResizeObserver(pantau);
      pengamat.observe(document.documentElement);
      window.addEventListener("resize", pantau, { passive: true });
      return () => {
        pengamat.disconnect();
        window.removeEventListener("resize", pantau);
      };
    }

    let menunggu = false;
    const hitung = () => {
      menunggu = false;
      const atas = window.scrollY || document.documentElement.scrollTop || 0;
      const total = document.documentElement.scrollHeight - window.innerHeight;
      pantau();
      const maju = total > 0 ? Math.min(1, Math.max(0, atas / total)) : 0;
      garis.style.transform = `scaleX(${maju.toFixed(4)})`;
    };
    const saat = () => {
      if (menunggu) return;
      menunggu = true;
      requestAnimationFrame(hitung);
    };
    hitung();
    window.addEventListener("scroll", saat, { passive: true });
    window.addEventListener("resize", saat, { passive: true });
    const pengamat =
      typeof ResizeObserver === "function" ? new ResizeObserver(saat) : null;
    pengamat?.observe(document.documentElement);
    return () => {
      pengamat?.disconnect();
      window.removeEventListener("scroll", saat);
      window.removeEventListener("resize", saat);
    };
    // `rute` jadi dependensi supaya panjang halaman diukur ulang tiap kali
    // isinya berganti -- itu yang dilakukan `pasangMajuBaca()` per rute.
  }, [rute]);

  return (
    <div
      ref={ref}
      id="maju-baca"
      aria-hidden="true"
      data-mesin={MAJU_LEWAT_CSS ? "css" : "js"}
    />
  );
}
