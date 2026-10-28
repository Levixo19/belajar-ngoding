/* Layar Pengantar (`#/pengantar`): hero yang membuka saat digulir, lalu isi
 * aplikasi dalam satu layar.
 *
 * BUKAN pengganti Dasbor. Dasbor adalah meja kerja (kartu Lanjutkan, antrean,
 * bahasa), dan kalimat gulir sengaja sudah dibuang dari sana. Pengantar layar
 * tersendiri yang boleh dibuka dan dilewati: ia dijangkau dari layar mulai
 * (profil tanpa XP) dan dari alamatnya, tidak dari palet perintah.
 *
 * Dua gambar hero adalah tangkapan layar Langit aplikasi ini sendiri
 * (`uji/manual/gambar-pengantar.mjs`), dengan progres CONTOH. Kalimatnya
 * menyebut itu terang-terangan, supaya bintang hijau di gambar tidak terbaca
 * sebagai progres orang yang sedang melihatnya.
 *
 * Semua angka dihitung dari `awal.bahasa`, tidak diketik: kurikulum ini masih
 * tumbuh, dan kalimat yang menyebut "tiga puluh dua" suatu hari berbohong
 * tanpa satu tes pun gagal.
 */

import { HeroGulir } from "../komponen/HeroGulir.tsx";
import { Ikon } from "../komponen/Ikon.tsx";
import { angka } from "../util.ts";
import type { BahasaAwal } from "./Dasbor.tsx";
import { jumlahKurikulum } from "./dasbor-teks.ts";

const PINTU: Array<{ href: string; ikon: "bintang" | "karier" | "jalankan" | "pustaka"; judul: string; ket: string }> = [
  {
    href: "#/langit",
    ikon: "bintang",
    judul: "Langit",
    ket: "Tiap kurikulum jadi rasi dan tiap materi jadi bintang. Makin terang bintangnya, makin jauh kamu melangkah.",
  },
  {
    href: "#/karier",
    ikon: "karier",
    judul: "Peta Karier",
    ket: "Pilih satu profesi, lihat bekal kurikulumnya, dan seberapa siap kamu sekarang.",
  },
  {
    href: "#/coba",
    ikon: "jalankan",
    judul: "Ruang Coba",
    ket: "Tulis kode apa saja, jalankan, lihat hasilnya. Tidak dinilai dan tidak menyentuh progres.",
  },
  {
    href: "#/pustaka",
    ikon: "pustaka",
    judul: "Pustaka",
    ket: "Tautan belajar dari luar, lengkap dengan sumbernya, disaring per kurikulum.",
  },
];

export function Pengantar({ bahasa }: { bahasa: BahasaAwal[] }) {
  const jml = jumlahKurikulum(bahasa);
  return (
    <HeroGulir
      judul={["Belajar coding,", "bintang demi bintang"]}
      gambarLatar="/gambar/pengantar-peta.jpg"
      gambarMedia="/gambar/pengantar-rasi.jpg"
      altMedia={
        "Rasi Python diperbesar di layar Langit. Tiap bintang bernomor adalah satu materi: " +
        "bintang hijau sudah selesai, cakram kuning sedang dikerjakan, cincin putih belum dibaca, " +
        "belah ketupat abu-abu masih terkunci."
      }
      petunjuk="Gulir, atau tekan Spasi, untuk membuka"
    >
      <div className="pengantar">
        <header className="sambut">
          <span className="mata">Sebelum mulai</span>
          <p className="sambut-sub">
            {`${angka(bahasa.length)} kurikulum, ${angka(jml.materi)} materi, ` +
              `${angka(jml.kuis)} kuis, dan ${angka(jml.latihan)} latihan, ` +
              "semuanya jalan di komputermu sendiri. Tidak perlu akun, dan progresmu " +
              "tersimpan di komputer ini saja."}
          </p>
          <p className="pengantar-catatan">
            Gambar di atas tangkapan layar Langit dengan progres contoh, bukan progresmu.
          </p>
        </header>

        <nav className="pengantar-pintu" aria-label="Tempat yang bisa dibuka">
          {PINTU.map((p) => (
            <a key={p.href} className="pintu-tenang" href={p.href}>
              <span className="ikon-bulat">
                <Ikon nama={p.ikon} ukuran={18} />
              </span>
              <div className="pintu-isi">
                <b>{p.judul}</b>
                <span>{p.ket}</span>
              </div>
              <span className="baris-panah">
                <Ikon nama="lanjut" ukuran={18} />
              </span>
            </a>
          ))}
        </nav>

        <p className="pengantar-aksi">
          <a className="tbl tbl-utama" href="#/">
            Mulai dari Dasbor
            <Ikon nama="lanjut" ukuran={16} />
          </a>
          <span>
            Dasbor menawarkan satu pintu masuk pertama, atau kartu Lanjutkan kalau
            kamu sudah pernah belajar.
          </span>
        </p>
      </div>
    </HeroGulir>
  );
}
