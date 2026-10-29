/* Adu penerjemah pesan galat TypeScript dengan rekaman yang dihasilkan Python.
 *
 * Yang diuji di sini bukan heuristiknya melainkan seluruh REGEX di
 * `pola-galat.json` yang diterjemahkan dari Python ke JavaScript. Satu pola yang berhenti cocok di sisi TS tidak
 * menimbulkan error di mana pun: pesan errornya cuma kembali tampil mentah
 * kepada orang yang paling tidak bisa membacanya, dan itu justru alasan modul
 * itu ada.
 *
 * Korpusnya karena itu ditagih MENJALANI SEMUA pola, bukan sekadar lulus.
 * Pesan sungguhan dari toolchain hanya menjalani sebagian; sisanya ditutup
 * pesan uji di `alat/golden_bersama.py:PROBE`. Skrip ini melaporkan "N/N pola
 * terjalani", dan angka itu yang ditagih, bukan angka di komentar.
 *
 *     node uji/golden-galat.ts
 */

import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { rapikan, ringkas, terjemahkan } from "../src/galat.ts";
import { sidik } from "./sidik.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const GOLDEN = path.join(path.resolve(SINI, ".."), "golden");

interface KasusGolden {
  bahasa: string;
  masukan: string;
  masukan_sha256: string;
  terjemahan_sha256: string;
  ringkas_sha256: string;
  rapikan_sha256: string;
}

interface Rekaman {
  cakupan: { pola: number; tersentuh: number; tidak_tersentuh: number[] };
  kasus: KasusGolden[];
}

function main(): number {
  const rekaman = JSON.parse(
    readFileSync(path.join(GOLDEN, "galat.json"), "utf-8"),
  ) as Rekaman;

  // Populasi dan CAKUPAN ditagih lebih dulu. Yang kedua tidak kalah penting:
  // rekaman yang lulus sempurna atas korpus yang cuma menjalani sepersepuluh
  // polanya terbaca sebagai bukti, padahal ia kebalikan dari bukti.
  if (rekaman.kasus.length < 50) {
    console.error(`POPULASI TERLALU KECIL: ${rekaman.kasus.length} pesan.`);
    return 1;
  }
  if (rekaman.cakupan.tidak_tersentuh.length) {
    console.error(
      `CAKUPAN BOLONG: ${rekaman.cakupan.tersentuh} dari ` +
        `${rekaman.cakupan.pola} pola terjalani. Pola yang tidak pernah cocok ` +
        `di korpus ini tidak diuji sama sekali: ` +
        `${rekaman.cakupan.tidak_tersentuh.slice(0, 15).join(", ")}. ` +
        `Tambahkan pesan uji di alat/golden_bersama.py:PROBE.`,
    );
    return 1;
  }

  const gagal: string[] = [];
  for (const k of rekaman.kasus) {
    const label = `${k.bahasa}: ${JSON.stringify(k.masukan.slice(0, 54))}`;

    if (sidik(k.masukan) !== k.masukan_sha256) {
      gagal.push(`${label}: MASUKANNYA sendiri tidak cocok dengan sidiknya`);
      continue;
    }

    const t = terjemahkan(k.masukan);
    if (sidik(t) !== k.terjemahan_sha256) {
      gagal.push(`${label}: terjemahkan() berbeda\n      ${JSON.stringify(t)}`);
    }
    const r = ringkas(k.masukan);
    if (sidik(r) !== k.ringkas_sha256) {
      gagal.push(`${label}: ringkas() berbeda (${r.length} baris)`);
    }
    // `"program"` sama dengan argumen yang dipakai sisi Python saat merekam.
    const p = rapikan(k.masukan, "program");
    if (sidik(p) !== k.rapikan_sha256) {
      gagal.push(
        `${label}: rapikan() berbeda\n      ${JSON.stringify(p.slice(0, 120))}`,
      );
    }
  }

  console.log(
    `rekaman: ${rekaman.kasus.length} pesan, ` +
      `${rekaman.cakupan.tersentuh}/${rekaman.cakupan.pola} pola terjalani`,
  );
  if (gagal.length) {
    console.error(`bergeser: ${gagal.length}`);
    for (const g of gagal.slice(0, 12)) console.error(`  - ${g}`);
    return 1;
  }
  console.log("COCOK: penerjemah galat TypeScript sepadan dengan Python.");
  return 0;
}

process.exit(main());
