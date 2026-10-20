/* Adu penggambar gambar konsep versi TypeScript dengan `webapp/statik/js/visual.js`.
 *
 * Korpusnya SELURUH 1.356 spesifikasi gambar yang sungguhan ada di kurikulum,
 * dibaca dari `packages/konten/visual/`. Tiap gambar dibandingkan SIMPUL DEMI
 * SIMPUL: tag, setiap atribut, dan setiap anak -- plus lebar dan tingginya.
 *
 * Kenapa seketat itu. Gambar konsep adalah data (`data/visual/<key>.py`), dan
 * yang membuatnya berguna bukan keindahannya melainkan bahwa angka di gambar
 * SAMA dengan angka di contoh kode di dekatnya. Satu koordinat yang bergeser
 * tidak menghasilkan error di mana pun: yang terjadi panah menunjuk kotak yang
 * salah, dan pelajar yang mempercayainya belajar hal yang salah dengan yakin.
 *
 * Sisi JS dijalankan di atas shim DOM 20 baris. Itu bukan kemalasan: lapisan
 * geometri `visual.js` cuma memakai empat API DOM (`createElementNS`,
 * `setAttribute`, `appendChild`, `textContent`), dan merekamnya jauh lebih
 * jujur daripada memuat seluruh peramban -- yang dibandingkan jadi persis apa
 * yang sampai ke atribut.
 *
 *     node uji/banding-visual.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { bentukVisual } from "../src/komponen/visual-bentuk.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "visual.js");
const KONTEN = path.join(AKAR, "packages", "konten", "visual");

/* ------------------------------------------------------------- shim DOM */

class Simpul {}
class Teks extends Simpul {
  constructor(t) { super(); this.nilai = String(t); }
  get textContent() { return this.nilai; }
}
class Elemen extends Simpul {
  constructor(tag) { super(); this.tag = tag; this.sifat = {}; this.anak = []; }
  setAttribute(k, v) { this.sifat[k] = String(v); }
  appendChild(n) { this.anak.push(n); return n; }
  get textContent() { return this.anak.map((a) => a.textContent).join(""); }
}
globalThis.Node = Simpul;
globalThis.document = {
  createElementNS: (_ns, tag) => new Elemen(tag),
  createTextNode: (t) => new Teks(t),
};

/** Elemen shim -> bentuk yang sama dengan `Simpul` di visual-bentuk.ts. */
function pohon(el) {
  return {
    tag: el.tag,
    sifat: el.sifat,
    anak: el.anak.map((a) => (a instanceof Teks ? a.nilai : pohon(a))),
  };
}

/* ------------------------------------------- iris lapisan geometri JS-nya */

const teks = readFileSync(SUMBER, "utf-8");
const AWAL = 'const NS = "http://www.w3.org/2000/svg";';
const AKHIR = "/** Spesifikasi gambar -> <figure>";
const i0 = teks.indexOf(AWAL);
const i1 = teks.indexOf(AKHIR);
if (i0 < 0 || i1 < 0 || i1 <= i0) {
  console.error(
    "IRISAN TIDAK KETEMU di visual.js. Lapisan geometrinya mungkin dipindah. " +
      "Perbaiki penandanya, JANGAN biarkan pagar ini membandingkan nol gambar.",
  );
  process.exit(1);
}
const irisan = teks.slice(i0, i1);

/* Diiris sebagai SATU potongan, bukan fungsi demi fungsi lewat regex. Regex
   per fungsi punya satu kegagalan yang tidak kelihatan: satu pola yang tidak
   cocok lagi sesudah sumbernya disunting membuat fungsi itu HILANG dari
   acuan, dan yang dibandingkan jadi versi TS melawan dirinya sendiri. Irisan
   menuntut kedua penandanya ada; daftar di bawah menuntut isinya lengkap. */
const WAJIB = ["function s(", "const putus", "const lebarTeks", "function teks(",
               "function kotak(", "function garis(", "function jalur(",
               "function kepalaSudut(", "function panah(", "const ARAH",
               "function bentukAlur(", "const RUMUS", "const PENGGAMBAR",
               "gVariabel", "gLarik", "gAlur", "gTumpukan", "gPohon", "gTabel",
               "gUrutan", "gKotak", "gTata", "gGit", "gMemori", "gBit", "gKurva"];
const hilang = WAJIB.filter((w) => !irisan.includes(w));
if (hilang.length) {
  console.error(`IRISAN TIDAK LENGKAP, hilang: ${hilang.join(", ")}`);
  process.exit(1);
}

const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-visual-")),
  "acuan.mjs",
);
writeFileSync(jalurTemp, irisan + `
export function bentukVisual(sp) {
  const fn = PENGGAMBAR[sp && sp.jenis];
  if (!fn) return null;
  return fn(sp);
}
`);
const acuan = await import(pathToFileURL(jalurTemp).href);

/* ----------------------------------------------------------------- korpus */

const spek = [];
for (const nama of readdirSync(KONTEN).sort()) {
  const d = JSON.parse(readFileSync(path.join(KONTEN, nama), "utf-8"));
  const telusur = (x, jalan) => {
    if (Array.isArray(x)) {
      x.forEach((v, i) => telusur(v, `${jalan}[${i}]`));
    } else if (x && typeof x === "object") {
      if (typeof x.jenis === "string") {
        spek.push({ nama: `${nama}${jalan}`, sp: x });
        return;
      }
      for (const [k, v] of Object.entries(x)) telusur(v, `${jalan}.${k}`);
    }
  };
  telusur(d, "");
}

let gagal = 0;
const jenisDilihat = new Set();
/* Jenis yang bergeser DITALLY, bukan cuma tiga temuan pertama yang dicetak.
   Satu perubahan di `s()` atau di `putus()` menyentuh ketiga belas jenis
   sekaligus, dan tiga baris pertama tidak memberi tahu apa pun soal cakupan
   kerusakannya -- sementara daftar jenisnya langsung menunjuk lapisan mana
   yang patah. Ia juga yang dipakai baterai mutasi sebagai kategori keluhan. */
const jenisBergeser = new Set();
for (const { nama, sp } of spek) {
  jenisDilihat.add(sp.jenis);
  const a = acuan.bentukVisual(sp);
  const b = bentukVisual(sp);
  if (a === null || b === null) {
    if (a !== b) {
      gagal += 1;
      jenisBergeser.add(sp.jenis);
      console.error(`  ${nama} ${sp.jenis}: satu sisi null, satu sisi tidak`);
    }
    continue;
  }
  const sa = JSON.stringify({ w: a.w, h: a.h, simpul: a.simpul.map(pohon) });
  const sb = JSON.stringify({ w: b.w, h: b.h, simpul: b.simpul });
  if (sa !== sb) {
    gagal += 1;
    jenisBergeser.add(sp.jenis);
    if (gagal <= 3) {
      // Titik selisih pertama dicetak, bukan seluruh pohonnya: satu gambar
      // bisa 600 simpul, dan pesan sepanjang itu tidak terbaca siapa pun.
      let k = 0;
      while (k < sa.length && sa[k] === sb[k]) k++;
      console.error(
        `  ${nama} ${sp.jenis} berbeda di karakter ${k}\n` +
          `    JS: ...${sa.slice(Math.max(0, k - 60), k + 80)}\n` +
          `    TS: ...${sb.slice(Math.max(0, k - 60), k + 80)}`,
      );
    }
  }
}

/* Pagar jenis: tiga belas penggambar ada, dan korpus yang kebetulan tidak
   memuat salah satunya berarti penggambar itu TIDAK diuji sama sekali --
   hijau tanpa membuktikan apa pun untuk seperenam belas kode di berkas itu. */
const SEMUA_JENIS = ["variabel", "larik", "alur", "tumpukan", "pohon", "tabel",
                     "urutan", "kotak", "tata", "git", "memori", "bit", "kurva"];
const takDiuji = SEMUA_JENIS.filter((j) => !jenisDilihat.has(j));

console.log(`${spek.length} spesifikasi gambar, ${jenisDilihat.size} jenis`);
if (takDiuji.length) {
  console.error(`JENIS TIDAK DIUJI: ${takDiuji.join(", ")}`);
}
if (gagal || takDiuji.length) {
  if (gagal) {
    console.error(`BERGESER: ${gagal} gambar berbeda.`);
    console.error(`JENIS BERGESER: ${[...jenisBergeser].sort().join(", ")}`);
  }
  process.exit(1);
}
console.log("COCOK: penggambar visual TypeScript identik dengan visual.js.");
