/* Pembaca berkas catatan pelajar. SATU-SATUNYA pintu layanan ini ke datanya.
 *
 * **Berkas JSON-nya tetap SUMBER KEBENARAN; MongoDB cuma INDEKS.** Itu
 * keputusan yang paling menentukan di seluruh paket ini, dan alasannya sudah
 * tertulis di kepala `webapp/catatan.py`: catatan adalah tulisan tangan orang,
 * dan `progress.reset()` yang ada di aplikasi ini pernah hampir ikut
 * membakarnya. Pengaman yang melindunginya -- karantina berkas rusak, `.bak`
 * bergulir, tulis atomik -- hidup di `pelajar/simpanan.py`, dan tidak satu pun
 * dari itu ada di sebuah container yang bisa dimatikan.
 *
 * Konsekuensi yang mengikat: layanan ini TIDAK PERNAH MENULIS ke berkas itu,
 * dan Mongo yang kosong atau mati tidak pernah berarti catatan yang hilang --
 * ia cuma berarti pencarian yang tidak tersedia. Aplikasinya jalan penuh tanpa
 * paket ini.
 */

import { readFile, stat } from "node:fs/promises";
import { homedir } from "node:os";
import path from "node:path";

/** Satu catatan, apa adanya dari berkas JSON. */
export interface Catatan {
  /** Kunci progres: `"python_materi::Pengenalan Python & Instalasi"`. */
  kunci: string;
  teks: string;
  diubah: string;
}

/**
 * Jalur berkas catatan.
 *
 * `BELAJAR_CATATAN_FILE` dihormati dengan nama yang SAMA dengan yang dipakai
 * `webapp/catatan.py` dan tes Python. Itu bukan kerapian: tes dan percobaan
 * mengalihkan keempat jalur data pemilik ke direktori sementara, dan layanan
 * yang membaca nama variabel lain akan diam-diam membaca catatan SUNGGUHAN
 * milik pemiliknya saat yang dimaksud sebuah profil uji.
 *
 * Nama berkas bawaannya tetap `.belajar_ngoding_catatan.json`, bukan
 * `belajar-codingV2`. Nama lama itu salah satu dari empat jalur data pemilik
 * yang SENGAJA tidak diganti; menggantinya di sini berarti layanan ini mencari
 * berkas yang tidak ada dan melaporkan nol catatan tanpa satu pun galat.
 */
export function jalurCatatan(): string {
  return (
    process.env["BELAJAR_CATATAN_FILE"] ||
    path.join(homedir(), ".belajar_ngoding_catatan.json")
  );
}

/** Bentuk berkasnya. `versi` dibaca tapi tidak dipakai memutuskan apa pun di
 *  sini -- yang memiliki skema itu `webapp/catatan.py`. */
interface BerkasCatatan {
  versi?: number;
  catatan?: Record<string, { teks?: string; diubah?: string }>;
}

/**
 * Baca seluruh catatan. Daftar KOSONG kalau berkasnya belum ada.
 *
 * Berkas yang belum ada adalah keadaan NORMAL, bukan galat: pelajar yang belum
 * pernah menulis catatan tidak punya berkasnya. Yang dilempar hanya berkas yang
 * ADA tapi tidak bisa diurai -- itu keadaan yang pantas dilihat, bukan
 * disembunyikan sebagai "nol catatan".
 */
export async function bacaCatatan(
  jalur = jalurCatatan(),
): Promise<{ daftar: Catatan[]; diubah: number }> {
  let mentah: string;
  let waktu = 0;
  try {
    const s = await stat(jalur);
    waktu = s.mtimeMs;
    mentah = await readFile(jalur, "utf-8");
  } catch (e) {
    if ((e as { code?: string }).code === "ENOENT") {
      return { daftar: [], diubah: 0 };
    }
    throw e;
  }
  const isi = JSON.parse(mentah) as BerkasCatatan;
  const peta = isi.catatan ?? {};
  const daftar: Catatan[] = [];
  for (const kunci of Object.keys(peta)) {
    const c = peta[kunci];
    // Catatan KOSONG dilewati, dan itu cocok dengan apa yang dilakukan
    // `webapp/catatan.py`: menghapus isi sebuah catatan menghapus entrinya,
    // jadi entri bertulisan kosong yang masih tersisa adalah sisa dari versi
    // lain -- dan sebuah hasil pencarian yang isinya kosong tidak menjawab apa
    // pun.
    if (!c || !c.teks) continue;
    daftar.push({ kunci, teks: c.teks, diubah: c.diubah ?? "" });
  }
  return { daftar, diubah: waktu };
}
