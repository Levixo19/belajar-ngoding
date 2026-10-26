/* Pintasan papan ketik cangkang, dan dialog yang mendaftarnya.
 *
 * Port `pasangPintasan()` + `PINTASAN_G` dari `webapp/statik/js/aplikasi.js`
 * dan `PINTASAN` + `tampilkanBantuan()` dari `layar-lain.js`.
 *
 * **`PINTASAN_G` adalah SATU definisi untuk dua pembaca:** penangan papan
 * ketik di bawah, dan label `<kbd>` di dialog bantuan. Di sisi JS huruf-huruf
 * itu pernah ditulis di TIGA tempat (penangan, palet, dan tabel prosa di
 * `layar-lain.js`), dan akibat rumusan yang melenceng bisa disebut: huruf yang
 * dipindah di satu tempat membuat tempat lain menjanjikan halaman yang
 * berbeda, tanpa satu pun tes gagal.
 *
 * Satu beda yang disengaja dari antarmuka lama, dan ia disebut di dialognya:
 * **Ctrl+K mengantar ke layar Cari**, bukan membuka palet perintah. Palet
 * (~495 baris, dengan ingatan kemutakhiran dan kontrak combobox-nya sendiri)
 * belum diport; mengantar ke tujuan terdekat yang benar lebih baik daripada
 * pintasan yang tidak melakukan apa pun.
 */

import { useEffect } from "react";

import { temaBerikutnya } from "../lokal.ts";
import { sorak } from "../sorak.tsx";

/** Huruf `G lalu <huruf>` dan alamat yang dibukanya. SATU definisi. */
export const PINTASAN_G: Record<string, string> = {
  d: "#/dasbor",
  c: "#/coba",
  s: "#/statistik",
  b: "#/bookmark",
  n: "#/catatan",
  p: "#/atur",
};

/** Berapa lama keadaan "G baru ditekan" bertahan.
 *
 *  Sembilan ratus milidetik, sama dengan versi JS. Ia cukup lama untuk
 *  rangkaian yang diketik santai, dan cukup pendek sehingga `g` yang ditekan
 *  lalu dilupakan tidak membajak huruf berikutnya semenit kemudian. */
const UMUR_G_MS = 900;

/** Daftar lengkap untuk dialog bantuan. */
export const PINTASAN: Array<[string, string]> = [
  ["Ctrl K", "Ke layar Cari (palet perintah belum diport)"],
  ["Ctrl B", "Buka / tutup menu"],
  ["Ctrl J", "Ganti tema"],
  ["G lalu D", "Ke dasbor"],
  ["G lalu C", "Ke ruang coba"],
  ["G lalu S", "Ke statistik"],
  ["G lalu B", "Ke bookmark"],
  ["G lalu N", "Ke catatanku"],
  ["G lalu P", "Ke pengaturan"],
  ["?", "Tampilkan daftar ini"],
  ["Esc", "Tutup dialog"],
  ["1-9 atau A-J", "Menjawab soal kuis"],
  ["Ctrl ⏎", "Jalankan kode di editor"],
  ["Ctrl ⇧ ⏎", "Periksa jawaban latihan"],
  ["Ctrl S", "Simpan kode"],
  ["Ctrl /", "Komentari baris di editor"],
  ["Tab atau ⇧ Tab", "Tambah atau kurangi indentasi"],
  ["j", "Blok kode berikutnya (di halaman materi)"],
  ["k", "Blok kode sebelumnya (di halaman materi)"],
  ["]", "Bagian berikutnya (di halaman materi)"],
  ["[", "Bagian sebelumnya (di halaman materi)"],
  ["f", "Mode fokus (di halaman materi)"],
  ["⏎", "Jalankan blok kode yang sedang difokus"],
];

/** Apakah ADA dialog yang sedang terbuka.
 *
 *  Ditanyakan ke DOM, bukan ke sebuah state bersama, dan itu keputusan: tiap
 *  layar memegang dialognya sendiri sebagai state lokal (ruang kerja punya
 *  tiga), jadi state bersama berarti setiap layar harus ingat mendaftarkan
 *  diri -- dan yang lupa mendaftar menghasilkan pintasan satu huruf yang
 *  memindahkan halaman di belakang dialog yang sedang dibaca. */
function jendelaTerbuka(): boolean {
  return document.querySelector(".jendela") !== null;
}

/**
 * Lapisan papan ketik cangkang.
 *
 * Urutan penjaganya bagian dari artinya:
 *
 * 1. `e.target instanceof Element` SEBELUM `.matches()`. Sasaran `keydown`
 *    tidak selalu elemen (bisa `document` sendiri), dan memanggil `.matches()`
 *    di atasnya melempar `TypeError` yang membunuh SELURUH penanganan pintasan
 *    tanpa satu pun pesan.
 * 2. Pintasan ber-Ctrl diperiksa lebih dulu, dan tiga di antaranya berlaku
 *    JUGA di dalam medan isian -- Ctrl+K dan Ctrl+J tidak mungkin bertabrakan
 *    dengan pengetikan. Ctrl+B tidak, karena di beberapa peramban ia pindah
 *    kursor satu karakter.
 * 3. Dialog yang terbuka menahan SEMUA pintasan satu huruf. Tanpa ini,
 *    menekan G lalu D sambil membaca dialog "Lihat jawaban" memindahkan
 *    halaman di belakangnya ke dasbor, dan dialognya tertinggal menggantung di
 *    atas layar yang sudah bukan miliknya.
 */
export function usePintasanCangkang({
  onBantuan, onAlihPanel,
}: {
  onBantuan: () => void;
  onAlihPanel: () => void;
}) {
  useEffect(() => {
    // Keadaan `g` tinggal di dalam efek, bukan di `useState`: ia tidak pernah
    // digambar, dan menaruhnya di state berarti satu render untuk setiap
    // ketukan `g`.
    let tombolG = false;
    let jam: ReturnType<typeof setTimeout> | null = null;

    const dengar = (e: KeyboardEvent) => {
      const diMedan =
        e.target instanceof Element &&
        e.target.matches("input, textarea, select");

      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        if (!jendelaTerbuka()) globalThis.location.hash = "#/cari";
        return;
      }
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "b" && !diMedan) {
        e.preventDefault();
        onAlihPanel();
        return;
      }
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "j") {
        e.preventDefault();
        sorak("Tema: " + temaBerikutnya(), "", 1.6);
        return;
      }
      if (diMedan || e.ctrlKey || e.metaKey || e.altKey) return;
      if (jendelaTerbuka()) return;

      if (e.key === "?") {
        e.preventDefault();
        onBantuan();
        return;
      }
      // Rangkaian ala Vim: G lalu satu huruf. Aman karena hanya aktif di luar
      // medan isian, jadi tidak pernah bertabrakan dengan pengetikan.
      if (e.key.toLowerCase() === "g") {
        tombolG = true;
        if (jam) clearTimeout(jam);
        jam = setTimeout(() => {
          tombolG = false;
        }, UMUR_G_MS);
        return;
      }
      if (tombolG) {
        const ke = PINTASAN_G[e.key.toLowerCase()];
        tombolG = false;
        if (ke) {
          e.preventDefault();
          globalThis.location.hash = ke;
        }
      }
    };

    document.addEventListener("keydown", dengar);
    return () => {
      if (jam) clearTimeout(jam);
      document.removeEventListener("keydown", dengar);
    };
  }, [onBantuan, onAlihPanel]);
}

/** Dialog daftar pintasan. Esc dan tombol Tutup sama-sama menutupnya. */
export function Bantuan({ onTutup }: { onTutup: () => void }) {
  useEffect(() => {
    const dengar = (e: KeyboardEvent) => {
      if (e.key === "Escape") onTutup();
    };
    globalThis.addEventListener("keydown", dengar);
    return () => globalThis.removeEventListener("keydown", dengar);
  }, [onTutup]);

  return (
    <div className="jendela" role="dialog" aria-modal="true"
         aria-label="Pintasan papan ketik">
      <h2>Pintasan papan ketik</h2>
      <div style={{ display: "grid", gap: "var(--s2)" }}>
        {PINTASAN.map(([tombol, arti]) => (
          <div className="pintasan-baris" key={tombol}>
            <kbd>{tombol}</kbd>
            <span>{arti}</span>
          </div>
        ))}
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
