/* Adu geometri rasi versi TypeScript dengan `webapp/statik/js/rasi.js`.
 *
 * Bentuk tiap rasi deterministik dari benihnya (nama kurikulum), jadi satu bit
 * yang meleset di `hash` atau `prng` mengubah SETIAP rasi -- tanpa satu pun
 * error, cuma peta langit yang tidak lagi sama dengan yang dilihat pelajar
 * kemarin. Itu jenis pergeseran yang tidak akan ada yang laporkan sebagai bug.
 *
 * Versi JS mengimpor `inti.js` yang butuh DOM, jadi fungsi murninya tidak bisa
 * diimpor langsung di Node. Yang dilakukan di sini: AMBIL potongan sumbernya
 * dengan regex lalu evaluasi. Itu rapuh terhadap penulisan ulang -- karena itu
 * ia MENOLAK kalau salah satu potongan tidak ketemu, alih-alih diam-diam
 * membandingkan nol fungsi.
 *
 *     node uji/banding-rasi.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  bentukRasi,
  hash,
  jariBintang,
  magStatus,
  berikutDari,
  ruasAntara,
  tataPetaRasi,
} from "../src/komponen/rasi-geometri.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "rasi.js");

const teks = readFileSync(SUMBER, "utf-8");

/** Ambil satu deklarasi tingkat-atas dari sumber JS, apa adanya. */
function potong(pola, nama) {
  const cocok = teks.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. Sumber rasi.js mungkin ditulis ulang. ` +
        `Perbarui polanya di uji/banding-rasi.mjs, JANGAN biarkan pagar ini ` +
        `membandingkan nol fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const bagian = [
  potong(/export function hash\(teks\) \{[\s\S]*?\n\}/, "hash"),
  potong(/function prng\(benih\) \{[\s\S]*?\n\}/, "prng"),
  potong(/export const jariBintang = [^;]+;/, "jariBintang"),
  potong(/const MAG = \{[^}]*\};/, "MAG"),
  potong(/export const magStatus = [^;]+;/, "magStatus"),
  potong(/export function bentukRasi\(n, benih, w, h\) \{[\s\S]*?\n\}/, "bentukRasi"),
  potong(/export function berikutDari\(materi\) \{[\s\S]*?\n\}/, "berikutDari"),
];

/* Potongannya ditulis ke berkas sementara lalu DIIMPOR, bukan dijalankan
 * lewat `new Function`. Dua alasan, dan yang kedua yang praktis:
 *
 * * `new Function` atas string yang disusun program adalah bentuk yang sama
 *   dengan injeksi kode. Di sini sumbernya berkas repo sendiri, jadi batas
 *   percayanya sama dengan mengimpor modul repo mana pun -- tapi bentuk yang
 *   tidak perlu dibela lebih baik daripada bentuk yang perlu.
 * * Galat sintaks di dalam `new Function` dilaporkan tanpa nomor baris yang
 *   berguna. Sebagai modul, Node menunjuk barisnya.
 */
const kode = bagian.join("\n").replace(/^export /gm, "");
const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-rasi-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  kode + "\nexport {hash, prng, jariBintang, magStatus, bentukRasi, berikutDari};\n",
);
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
/* Dihitung DI DALAM `adu`, bukan dirumuskan di akhir. Versi pertama menghitung
   `BENIH.length * 9 + 21 + ...` dengan tangan, dan rumus itu berhenti menyebut
   kenyataan begitu satu blok perbandingan ditambahkan -- 201 peta utuh di
   bawah tidak terhitung sama sekali. Yang membaca angka ini tes populasi di
   `test_konten_json.py`, jadi hitungan yang lebih kecil daripada kenyataan
   membuat lantainya kehilangan gigi tanpa ada yang tahu. */
let cacah = 0;
const adu = (nama, a, b) => {
  cacah += 1;
  const sa = JSON.stringify(a);
  const sb = JSON.stringify(b);
  if (sa !== sb) {
    gagal += 1;
    console.error(`  ${nama}\n    JS: ${sa}\n    TS: ${sb}`);
  }
};

// Benih nyata: kunci kurikulum yang dipakai aplikasi, plus bentuk pinggiran.
const BENIH = [
  "python", "java", "javascript", "c", "cpp", "sql", "bash", "html", "css",
  "go", "git", "fedora", "aplikasi", "techstack", "frontend", "backend",
  "database", "mobile", "game", "iot", "devops", "keamanan", "data", "ai",
  "bahasalain", "", "a", "kurikulum-yang-namanya-sangat-panjang-sekali",
];

for (const benih of BENIH) {
  adu(`hash(${JSON.stringify(benih)})`, acuan.hash(benih), hash(benih));
  for (const n of [0, 1, 2, 3, 7, 12, 44, 83]) {
    adu(
      `bentukRasi(${n}, ${JSON.stringify(benih)})`,
      acuan.bentukRasi(n, benih, 1000, 250),
      bentukRasi(n, benih, 1000, 250),
    );
  }
}

for (const mag of [0, 1, 1.5, 3, 5, 6, 12]) {
  for (const skala of [1, 0.5, 2.25]) {
    adu(
      `jariBintang(${mag}, ${skala})`,
      acuan.jariBintang(mag, skala),
      jariBintang(mag, skala),
    );
  }
}

const CONTOH = [
  { judul: "a", status: "selesai" },
  { judul: "b", status: "sebagian" },
  { judul: "c", status: "baru" },
  { judul: "d", status: "baru", terkunci: true },
  { judul: "e", status: "entah-apa" },
];
for (const m of CONTOH) {
  adu(`magStatus(${m.judul})`, acuan.magStatus(m), magStatus(m));
}
adu("berikutDari(contoh)", acuan.berikutDari(CONTOH), berikutDari(CONTOH));
adu(
  "berikutDari(semua selesai)",
  acuan.berikutDari([{ judul: "x", status: "selesai" }]),
  berikutDari([{ judul: "x", status: "selesai" }]),
);

// `ruas` versi JS menghasilkan elemen SVG, jadi yang diadu KOORDINATNYA:
// nilai yang sama yang dipasang ke atribut x1/y1/x2/y2 di sana.
const PASANG = [
  [[0, 0], [100, 0], 3, 3],
  [[0, 0], [5, 0], 3, 3],
  [[10, 20], [-30, 44], 1.1, 5.2],
  [[0, 0], [0, 0], 1, 1],
];
for (const [a, b, ra, rb] of PASANG) {
  const d = Math.hypot(b[0] - a[0], b[1] - a[1]);
  const harap =
    d < ra + rb + 4
      ? null
      : {
          x1: Number((a[0] + ((b[0] - a[0]) / d) * (ra + 3)).toFixed(1)),
          y1: Number((a[1] + ((b[1] - a[1]) / d) * (ra + 3)).toFixed(1)),
          x2: Number((b[0] - ((b[0] - a[0]) / d) * (rb + 3)).toFixed(1)),
          y2: Number((b[1] - ((b[1] - a[1]) / d) * (rb + 3)).toFixed(1)),
        };
  const nyata = ruasAntara(a, b, ra, rb);
  const bulat =
    nyata === null
      ? null
      : {
          x1: Number(nyata.x1.toFixed(1)),
          y1: Number(nyata.y1.toFixed(1)),
          x2: Number(nyata.x2.toFixed(1)),
          y2: Number(nyata.y2.toFixed(1)),
        };
  adu(`ruasAntara(${JSON.stringify([a, b, ra, rb])})`, harap, bulat);
}

/* ======================================================== tata letak peta

   Yang di atas mengadu fungsi-fungsi kecilnya. Yang di bawah mengadu
   SUSUNANNYA: `petaRasi()` meletakkan satu rasi per bab dengan pusat yang
   naik-turun mengikuti sinus berbenih `hash(key)`, memangkas judul bab pada
   batas yang dihitung dari lebar railnya, dan menjangkarkan label di ujung ke
   dalam. Tidak satu pun dari itu bisa salah dengan menimbulkan error -- yang
   terjadi cuma peta yang bergeser, dan tidak ada yang akan melaporkannya.

   Sisi JS dijalankan di atas shim DOM, pola yang sama dengan
   `banding-visual.mjs`: lapisan ini cuma memakai `createElementNS`,
   `setAttribute`, `appendChild`, `createTextNode`, `style.setProperty`, dan
   `dataset`. Merekam keenamnya lebih jujur daripada memuat peramban -- yang
   dibandingkan jadi persis apa yang sampai ke atribut. */

/* ------------------------------------------------------------- shim DOM */

class Simpul {}
class Teks extends Simpul {
  constructor(t) { super(); this.nilai = String(t); }
  get textContent() { return this.nilai; }
}
class Elemen extends Simpul {
  constructor(tag) {
    super();
    this.tag = tag;
    this.sifat = {};
    this.anak = [];
    this.dataset = {};
    this.gaya = {};
    this.kelas = [];
    this.style = { setProperty: (k, v) => { this.gaya[k] = String(v); } };
    this.classList = { add: (k) => this.kelas.push(k) };
  }
  setAttribute(k, v) { this.sifat[k] = String(v); }
  appendChild(n) { this.anak.push(n); return n; }
  append(n) { this.anak.push(n); return n; }
  addEventListener() {}
  querySelectorAll() { return []; }
  get textContent() { return this.anak.map((a) => a.textContent).join(""); }
}
globalThis.Node = Simpul;
globalThis.document = {
  createElementNS: (_ns, tag) => new Elemen(tag),
  createTextNode: (t) => new Teks(t),
};

/* `h()` milik `inti.js` tidak diiris: ia 60 baris yang mengurus event, gaya,
   dan penyaringan null, dan tidak satu pun dari itu memengaruhi geometri.
   Yang dibutuhkan slice ini cuma "bikin elemen HTML, bawa kelasnya, tempel
   anaknya" -- dan membuat shim-nya 8 baris jauh lebih mudah dibaca daripada
   mengiris modul kedua. Kalau `h()` suatu hari ikut menentukan tata letak,
   pagar ini berhenti cukup; sekarang tidak. */
function hShim(pemilih, _sifat = {}, ...anak) {
  const [tag, ...kelas] = String(pemilih).split(".");
  const el = new Elemen(tag || "div");
  if (kelas.length) el.setAttribute("class", kelas.join(" "));
  for (const a of anak.flat(4)) {
    if (a === null || a === undefined || a === false) continue;
    el.appendChild(a instanceof Simpul ? a : new Teks(String(a)));
  }
  return el;
}

/* --------------------------------------------- iris lapisan peta JS-nya */

const AWAL_PETA = 'const NS = "http://www.w3.org/2000/svg";';
const AKHIR_PETA = "/** Data /api/bahasa -> bentuk yang dipakai petaRasi. */";
const i0 = teks.indexOf(AWAL_PETA);
const i1 = teks.indexOf(AKHIR_PETA);
if (i0 < 0 || i1 < 0 || i1 <= i0) {
  console.error(
    "IRISAN PETA TIDAK KETEMU di rasi.js. Penandanya mungkin dipindah. " +
      "Perbaiki penandanya, JANGAN biarkan pagar ini membandingkan nol peta.",
  );
  process.exit(1);
}
const irisan = teks.slice(i0, i1);
const WAJIB_PETA = [
  "export function s(", "export function ruas(", "export function reticle(",
  "export function bintangSvg(", "export function pasangTip(",
  "export function petaRasi(", "export const ROMAWI", "const MAG =",
  "export const KATA_STATUS",
];
const kurang = WAJIB_PETA.filter((w) => !irisan.includes(w));
if (kurang.length) {
  console.error(`IRISAN PETA TIDAK LENGKAP, hilang: ${kurang.join(", ")}`);
  process.exit(1);
}

const jalurPeta = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-peta-")),
  "acuan-peta.mjs",
);
writeFileSync(
  jalurPeta,
  "const h = globalThis.__h;\nconst isikan = () => {};\n" +
    "const tingkatGerak = () => \"mati\";\nconst api = {};\n" +
    irisan.replace(/^export /gm, "") +
    "\nexport { petaRasi };\n",
);
globalThis.__h = hShim;
const acuanPeta = await import(pathToFileURL(jalurPeta).href);

/* ------------------------------------- pohon JS -> daftar primitif datar */

const kls = (el) => el.sifat.class || "";
const sv = (el, k) => (k in el.sifat ? el.sifat[k] : null);

function dariGaris(el) {
  return {
    jenis: "garis",
    kelas: kls(el),
    x1: sv(el, "x1"), y1: sv(el, "y1"), x2: sv(el, "x2"), y2: sv(el, "y2"),
    pathLength: sv(el, "pathLength"),
    urut: "--i" in el.gaya ? el.gaya["--i"] : null,
  };
}

function dariBintangJs(el) {
  const titik = el.anak.find((a) => kls(a).startsWith("rasi-titik"));
  const cahaya = el.anak.find((a) => kls(a) === "rasi-cahaya");
  return {
    jenis: "bintang",
    tag: el.tag,
    kelas: kls(el),
    label: sv(el, "aria-label"),
    href: sv(el, "href"),
    // `String()`: DOM sungguhan memaksa `dataset` jadi string, shim 40 baris
    // di atas tidak. Tanpa ini seluruh 201 peta berbeda pada satu medan yang
    // tidak pernah salah -- dan 198 sel merah yang semuanya palsu adalah cara
    // tercepat membuat pagar ini berhenti dibaca.
    indeks: el.dataset.indeks === undefined ? null : String(el.dataset.indeks),
    cx: sv(titik, "cx"), cy: sv(titik, "cy"), r: sv(titik, "r"),
    cahaya: cahaya ? sv(cahaya, "r") : null,
    urut: "--i" in el.gaya ? el.gaya["--i"] : null,
  };
}

function dariPetaJs(wadah) {
  const ringkasan = wadah.anak.find((a) => kls(a) === "rasi-ringkasan");
  const svg = wadah.anak.find((a) => a.tag === "svg");
  const [lapisGaris, lapisBintang, lapisLabel] = svg.anak;
  return {
    ringkasan: ringkasan.textContent,
    viewBox: sv(svg, "viewBox"),
    jalur: lapisGaris.anak.map(dariGaris),
    kelompok: lapisBintang.anak.map((g) =>
      g.anak.map((x) => (x.tag === "line" ? dariGaris(x) : dariBintangJs(x))),
    ),
    label: lapisLabel.anak
      .filter((x) => x.tag === "text")
      .map((x) => ({
        x: sv(x, "x"), y: sv(x, "y"), jangkar: sv(x, "text-anchor"),
        nomor: x.anak[0].textContent, judul: x.anak[1].textContent,
      })),
    reticle: (() => {
      const g = lapisLabel.anak.find((x) => kls(x) === "rasi-reticle");
      if (!g) return null;
      return { transform: sv(g, "transform"), r: sv(g.anak[0].anak[0], "r") };
    })(),
  };
}

/* ------------------------------- tata letak TS -> daftar primitif datar

   Pemetaan di bawah MENIRU `PetaRasi` di `komponen/Rasi.tsx` -- `toFixed` yang
   sama, nama kelas yang sama. Batasnya karena itu sama dengan
   `banding-visual.mjs`: yang dibuktikan identik adalah LAPISAN MURNI-nya, dan
   komponennya memang dijaga tipis supaya klaim itu berarti. */

const MAG_TS = { selesai: 1, sebagian: 3, baru: 5 };
const KATA_TS = {
  selesai: "sudah dibaca", sebagian: "dibaca sebagian", baru: "belum dibaca",
};

function garisTs(x, jalur) {
  const u = ruasAntara(x.a, x.b, x.ra, x.rb);
  return {
    jenis: "garis",
    kelas:
      "rasi-garis" +
      (x.terang ? " rasi-garis-terang" : "") +
      (jalur ? " rasi-garis-jalur" : ""),
    x1: u.x1.toFixed(1), y1: u.y1.toFixed(1),
    x2: u.x2.toFixed(1), y2: u.y2.toFixed(1),
    pathLength: jalur ? null : "1",
    urut: x.urut === undefined ? null : String(x.urut),
  };
}

function bintangTs(x, data) {
  const m = data.materi[x.indeks];
  const kelas = m.terkunci
    ? "rasi-terkunci"
    : "rasi-" + (MAG_TS[m.status] ? m.status : "baru");
  const kunci = Boolean(m.terkunci);
  return {
    jenis: "bintang",
    tag: kunci ? "g" : "a",
    kelas: "rasi-bintang" + (kunci ? " rasi-bintang-kunci" : ""),
    label: `${m.judul}, ${kunci ? "masih terkunci" : (KATA_TS[m.status] ?? "")}`,
    href: kunci ? null : `#/materi/${data.key}/${x.indeks}`,
    indeks: String(x.indeks),
    cx: x.x.toFixed(1), cy: x.y.toFixed(1), r: x.r.toFixed(2),
    cahaya: m.status === "selesai" && !m.terkunci ? (x.r * 3.2).toFixed(1) : null,
    urut: String(x.urut),
  };
}

function dariPetaTs(data, tinggi) {
  const t = tataPetaRasi(data, tinggi);
  return {
    ringkasan: t.ringkasan,
    viewBox: `0 0 ${t.W} ${t.H}`,
    jalur: t.jalur.map((j) => garisTs({ ...j, terang: false }, true)),
    kelompok: t.kelompok.map((isi) =>
      isi.map((x) =>
        x.jenis === "garis" ? garisTs(x, false) : bintangTs(x, data),
      ),
    ),
    label: t.label.map((l) => ({
      x: l.x.toFixed(1), y: l.y.toFixed(1), jangkar: l.jangkar,
      nomor: l.nomor, judul: l.judul,
    })),
    reticle: t.reticle
      ? {
          transform:
            `translate(${t.reticle.x.toFixed(1)},${t.reticle.y.toFixed(1)})`,
          r: String(t.reticle.r + 7),
        }
      : null,
  };
}

/* ----------------------------------------------------------------- korpus

   Dibangun dari `packages/konten/`, bukan dikarang: 32 kurikulum sungguhan
   dengan pembagian bab sungguhan. Status materinya DIPUTAR deterministik
   (selesai / sebagian / baru / terkunci) supaya keempat cabang magnitudo dan
   kedua cabang `terang` benar-benar terpakai -- korpus yang semua materinya
   "baru" tidak akan pernah menyentuh garis terang maupun lingkaran cahaya. */

const KONTEN = path.join(AKAR, "packages", "konten", "kurikulum");
const BAB_JSON = JSON.parse(
  readFileSync(path.join(AKAR, "packages", "konten", "bab.json"), "utf-8"),
);
const POLA_STATUS = [
  { status: "selesai" },
  { status: "selesai" },
  { status: "sebagian" },
  { status: "baru" },
  { status: "baru", terkunci: true },
];

const PETA = [];
for (const nama of readdirSync(KONTEN).sort()) {
  const k = JSON.parse(readFileSync(path.join(KONTEN, nama), "utf-8"));
  const materi = k.materi.map((m, i) => ({
    judul: m.title,
    ...POLA_STATUS[(i + hash(k.key)) % POLA_STATUS.length],
  }));
  const bab = (BAB_JSON[k.key] || []).map((b, i) => ({
    nomor: i + 1,
    judul: b.judul,
    materi: Array.from({ length: b.akhir - b.awal }, (_v, j) => b.awal + j),
  }));
  PETA.push({ key: k.key, label: k.label, materi, bab });
  // Bahasa yang sama TANPA pembagian bab: jalur cadangan satu-rasi, yang
  // dipakai bahasa baru sebelum babnya ditulis.
  PETA.push({ key: k.key, label: k.label, materi, bab: [] });
}
// Bentuk pinggiran: nol materi, satu materi, dan bab yang menunjuk indeks
// yang tidak ada (yang di JS di-`return` begitu saja di dalam forEach).
PETA.push({ key: "kosong", label: "Kosong", materi: [], bab: [] });
PETA.push({
  key: "satu", label: "Satu",
  materi: [{ judul: "Satu-satunya", status: "baru" }],
  bab: [{ nomor: 1, judul: "Bab tunggal", materi: [0] }],
});
PETA.push({
  key: "bolong", label: "Bolong",
  materi: [{ judul: "A", status: "selesai" }, { judul: "B", status: "baru" }],
  bab: [{ nomor: 1, judul: "Menunjuk ke luar", materi: [0, 9, 1] }],
});

/* DUA dan TIGA bab, dan keduanya ada karena diukur: jangkar label bergantung
   pada `bab.length > 2`, dan kurikulum paling kecil di repo ini punya ENAM bab
   -- jadi tanpa kedua bentuk di bawah, mutasi `> 2` menjadi `> 1` tetap hijau
   bukan karena tidak berakibat melainkan karena tidak ada masukannya. Dengan
   dua bab semuanya `middle`; dengan tiga, yang pertama `start` dan yang
   terakhir `end`. Bahasa baru yang babnya belum lengkap akan melewati jalur
   itu, jadi ia bukan bentuk karangan. */
for (const n of [2, 3]) {
  PETA.push({
    key: `bab${n}`,
    label: `Bab ${n}`,
    materi: Array.from({ length: n * 2 }, (_v, i) => ({
      judul: `M${i}`,
      ...POLA_STATUS[i % POLA_STATUS.length],
    })),
    bab: Array.from({ length: n }, (_v, i) => ({
      nomor: i + 1,
      judul: `Bab nomor ${i + 1} yang judulnya cukup panjang untuk dipangkas`,
      materi: [i * 2, i * 2 + 1],
    })),
  });
}

for (const data of PETA) {
  for (const tinggi of [250, 230, 400]) {
    adu(
      `petaRasi(${data.key}, bab=${data.bab.length}, h=${tinggi})`,
      dariPetaJs(acuanPeta.petaRasi(data, { tinggi })),
      dariPetaTs(data, tinggi),
    );
  }
}

console.log(
  `${cacah} perbandingan atas ${BENIH.length} benih dan ` +
    `${PETA.length} bentuk kurikulum (tiap kurikulum sebagai peta utuh, ` +
    `tiga tinggi)`,
);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: geometri rasi TypeScript identik dengan rasi.js.");
