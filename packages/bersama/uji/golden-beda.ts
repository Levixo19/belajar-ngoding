/* Adu penjelas beda keluaran TypeScript dengan rekaman yang dihasilkan Python.
 *
 * Yang paling berisiko di port `beda` bukan heuristik diagnosisnya, melainkan
 * PENYEJAJAR barisnya: `inti/beda.py` memakai `difflib.SequenceMatcher`, yang
 * bukan Myers diff. Pustaka diff npm mana pun akan memberi penyejajaran yang
 * berbeda untuk baris yang berpindah tempat, dan yang pelajar lihat bukan
 * "diff-nya lain" melainkan penjelasan yang menunjuk baris yang salah.
 *
 *     node uji/golden-beda.ts
 */

import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { bandingkan, kolomPertamaBeda, nyaris, type Beda } from "../src/beda.ts";
import { sidik } from "./sidik.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const GOLDEN = path.join(path.resolve(SINI, ".."), "golden");

interface KasusGolden {
  harap: string;
  aktual: string;
  harap_sha256: string;
  aktual_sha256: string;
  bandingkan_sha256: string;
  nyaris: boolean;
  kolom_pertama_beda: number | null;
}

/**
 * Bentuk yang disidik `alat/golden_bersama.py:golden_beda`.
 *
 * Medannya snake_case karena itu nama atribut di `inti/beda.py`, sementara API
 * TS memakai camelCase seperti sisa kode JavaScript di repo ini. Pemetaannya
 * ditulis di SINI, di pembandingnya, bukan di `src/beda.ts`: yang perlu
 * mengenal bentuk rekaman cuma yang mengadu dengannya, dan membuat modulnya
 * sendiri memakai nama Python berarti seluruh React ikut memakai nama itu demi
 * sebuah tes.
 */
function bentukRekaman(b: Beda) {
  return {
    sama: b.sama,
    nomor_beda: b.nomorBeda,
    kolom_beda: b.kolomBeda,
    catatan: b.catatan,
    harapan: b.harapan,
    aktual: b.aktual,
    baris: b.baris.map((x) => [...x]),
  };
}

function main(): number {
  const rekaman = JSON.parse(
    readFileSync(path.join(GOLDEN, "beda.json"), "utf-8"),
  ) as { kasus: KasusGolden[] };

  // Populasi ditagih lebih dulu: rekaman kosong membuat setiap perbandingan di
  // bawah lulus karena tidak ada yang dibandingkan.
  if (rekaman.kasus.length < 5) {
    console.error(
      `POPULASI TERLALU KECIL: ${rekaman.kasus.length} kasus. ` +
        `Jalankan python3 alat/golden_bersama.py --tulis.`,
    );
    return 1;
  }

  const gagal: string[] = [];
  for (const k of rekaman.kasus) {
    const label = `${JSON.stringify(k.harap)} vs ${JSON.stringify(k.aktual)}`;
    const b = bandingkan(k.harap, k.aktual);

    const s = sidik(bentukRekaman(b));
    if (s !== k.bandingkan_sha256) {
      gagal.push(
        `${label}: bandingkan() berbeda\n` +
          `      sama=${b.sama} nomorBeda=${b.nomorBeda} ` +
          `kolomBeda=${b.kolomBeda}\n` +
          `      catatan=${JSON.stringify(b.catatan)}`,
      );
    }
    if (nyaris(b) !== k.nyaris) {
      gagal.push(`${label}: nyaris() ${nyaris(b)}, rekaman ${k.nyaris}`);
    }
    const kol = kolomPertamaBeda(k.harap, k.aktual);
    if (kol !== k.kolom_pertama_beda) {
      gagal.push(
        `${label}: kolomPertamaBeda() ${kol}, rekaman ${k.kolom_pertama_beda}`,
      );
    }
  }

  console.log(`rekaman: ${rekaman.kasus.length} pasangan keluaran`);
  if (gagal.length) {
    console.error(`bergeser: ${gagal.length}`);
    for (const g of gagal.slice(0, 10)) console.error(`  - ${g}`);
    return 1;
  }
  console.log("COCOK: penjelas beda TypeScript sepadan dengan Python.");
  return 0;
}

process.exit(main());
