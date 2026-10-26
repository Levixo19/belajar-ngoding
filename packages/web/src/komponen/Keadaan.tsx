/* Empat keadaan, satu komponen: kosong, berhasil, gagal, terkunci.
 *
 * Padanan `keadaan()` di inti.js. Keempatnya menjawab satu pertanyaan yang
 * sama -- "tidak ada apa-apa di sini, dan inilah sebabnya" -- dan tiga di
 * antaranya cuma muncul sekali-sekali, persis frekuensi yang membuat sebuah
 * bentuk tidak pernah sempat dikenali. Yang membedakan keempatnya cuma warna
 * garis kiri dan ikonnya.
 *
 * Versi JS punya SEPASANG fungsi: `keadaan({objek})` dan `kosong(judul, ket,
 * aksi)` yang posisional. Keduanya sah dipanggil dengan tanda tangan yang
 * lain, karena mendestrukturisasi sebuah string di JavaScript cuma memberi
 * `undefined` untuk tiap medannya -- tanpa error. Itu sudah pernah terjadi di
 * `layar-tebak.js`, dan yang digambar kotak tanpa judul, tanpa penjelasan,
 * dan tanpa tombol: tepatnya ketiga hal yang jadi satu-satunya alasan
 * komponen ini ada.
 *
 * Di sini kesalahan itu tidak mungkin: cuma ADA SATU komponen, `judul` wajib,
 * dan props-nya bernama. Kalau `judul` lupa diisi, `tsc` yang memberi tahu --
 * bukan pelajar yang menatap kotak kosong.
 */

import type { ReactNode } from "react";

import { Ikon } from "./Ikon.tsx";

/**
 * Jenis keadaan. Menentukan warna garis kiri dan ikonnya, bukan isinya.
 *
 * Keempat nilainya adalah KELAS YANG BENAR-BENAR ADA di `gaya.css`
 * (`.keadaan-tuntas`, `.keadaan-salah`, `.keadaan-kunci`, `.keadaan-kosong`).
 * Versi pertama tipe ini menawarkan `"benar"` -- nama yang terdengar wajar dan
 * tidak punya satu pun aturan gaya, jadi `jenis="benar"` menggambar keadaan
 * tanpa warna maupun ikon berwarna, lolos `tsc`, dan tidak menimbulkan error
 * di mana pun. Itu kelas bug yang sama dengan kelas tata letak karangan yang
 * sudah pernah lolos ke ruang kerja latihan: yang menangkapnya bukan pemeriksa
 * tipe melainkan membaca `gaya.css`.
 */
export type JenisKeadaan = "kosong" | "tuntas" | "salah" | "kunci";

interface Props {
  jenis?: JenisKeadaan;
  /** Nama ikon di sebelah kiri. Hiasan: artinya sudah dibawa `judul`. */
  gambar?: string;
  /** WAJIB. Satu kalimat: apa yang tidak ada di sini. */
  judul: string;
  /** Kenapa ia tidak ada, dan apa yang bisa dilakukan. */
  ket?: ReactNode;
  /** Tombol atau tautan. Boleh kosong, tapi jarang sebaiknya. */
  aksi?: ReactNode;
}

export function Keadaan({ jenis, gambar, judul, ket, aksi }: Props) {
  // `.masuk-mandiri` util entrance yang sudah ada di gaya.css, bukan mesin
  // gerak baru: keempat keadaan datang dengan satu bahasa yang sama, dan
  // bentuk geraknya diatur CSS -- yang lahir dari proses async memudar TANPA
  // bergeser, yang permanen boleh bergeser.
  const kelas = "keadaan masuk-mandiri" + (jenis ? " keadaan-" + jenis : "");
  return (
    <div className={kelas}>
      {gambar ? <Ikon nama={gambar} ukuran={22} /> : null}
      <div className="keadaan-isi">
        <b>{judul}</b>
        {ket ? <p>{ket}</p> : null}
        {aksi ? <div className="deret">{aksi}</div> : null}
      </div>
    </div>
  );
}
