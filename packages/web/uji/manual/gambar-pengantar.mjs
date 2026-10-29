/* Membuat dua gambar hero layar Pengantar dari layar Langit SUNGGUHAN:
 *   pengantar-peta.jpg  ikhtisar 32 rasi (latar yang memudar saat hero dibuka)
 *   pengantar-rasi.jpg  satu rasi diperbesar (media yang mengembang)
 *
 * Gambarnya tangkapan aplikasi ini sendiri, bukan foto stok, jadi yang dilihat
 * calon pelajar di pengantar adalah layar yang akan ia pakai. Profil "campur"
 * (lib.mjs) mewarnai tiap status bintang lewat intersepsi respons di sisi
 * klien; server tidak menulis apa pun. Jalankan lagi bila tampilan Langit
 * berubah:
 *
 *   S=<direktori sementara>
 *   BELAJAR_PROGRESS_FILE=$S/p.json BELAJAR_CONFIG_FILE=$S/k.json \
 *   BELAJAR_CATATAN_FILE=$S/c.json BELAJAR_WORKSPACE=$S/kerja \
 *     python3 belajar-web.py --tanpa-browser --port 7788
 *   PLAYWRIGHT_MJS=... node packages/web/uji/manual/gambar-pengantar.mjs
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { URL_DASAR, mulai } from "./lib.mjs";

// Progres di rumah adalah catatan belajar sungguhan; skrip ini hanya boleh
// menyentuh server berprofil sementara.
if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const AKAR = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../../..");
const KELUAR = process.env.KELUAR ?? path.join(AKAR, "webapp", "statik", "gambar");
fs.mkdirSync(KELUAR, { recursive: true });

const TARGET = [
  // Lebar 1600 supaya ikhtisar (ambang 1.156 px pada ukuran huruf bawaan) tergambar
  // sebagai peta, bukan daftar.
  ["pengantar-peta.jpg", { hash: "#/langit", tunggu: ".lt-ikhtisar" }, ".lt-ikhtisar"],
  ["pengantar-rasi.jpg", { hash: "#/langit/python/12" }, ".lt-lensa-kanvas"],
];

for (const [nama, o, elemen] of TARGET) {
  const s = await mulai({ lebar: 1600, tinggi: 1000, tema: "gelap", gerak: "mati", profil: "campur", ...o });
  try {
    await s.page.waitForTimeout(600);
    const berkas = path.join(KELUAR, nama);
    await s.page.locator(elemen).first().screenshot({ path: berkas, type: "jpeg", quality: 80 });
    const kb = Math.round(fs.statSync(berkas).size / 1024);
    console.log(`${nama}: ${kb} KB`);
    if (s.tulisDitolak.length) throw new Error("ada permintaan tulis: " + s.tulisDitolak.join(", "));
  } finally {
    await s.tutup();
  }
}
