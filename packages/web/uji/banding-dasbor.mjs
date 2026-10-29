/* Adu bagian murni dasbor dengan `webapp/statik/js/layar-belajar.js`.
 *
 * Dasbor adalah layar yang paling banyak MEMUTUSKAN tanpa menggambar apa pun
 * yang kelihatan salah kalau keputusannya meleset: ambang tingkat bara, jeda
 * terpanjang, paket "punya 30 menit", pembanding XP kemarin, tinggi batang
 * pekan, dan empat cabang kalimat pembuka. Semuanya angka, dan angka yang salah
 * di dasbor tampil dengan sangat yakin.
 *
 * Sisi JS MENGGAMBAR, jadi `h()` diganti perekam dan mesin geraknya
 * (`ungkap`, `saatTampak`, `nyalakanBara`, `pinKeHariIni`, ...) diganti no-op.
 * Itu sah karena yang diadu keputusannya, bukan simpulnya -- dan tiap
 * penerjemah di bawah MENUNTUT bentuk yang diharapkan, jadi pohon yang berubah
 * menghentikan pagar ini dengan pesan, bukan dengan nol perbandingan.
 *
 * Pembantu tanggal (`tanggalLokal`, `tanggalRamah`, `hariIniISO`,
 * `selisihHari`, `angka`) DIIRIS dari `inti.js`, tidak distub: keduanya harus
 * memakai aritmetika tanggal yang sama persis, dan "mungkin sama" adalah
 * tempat bug zona waktu tinggal.
 *
 *     node uji/banding-dasbor.mjs
 */

import { mkdtempSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  bandingHarian, baraPetak, celahBelajar, cincinAngka, dijalaniDasbor,
  jedaBara, jumlahKurikulum, kalimatPembuka, labelLanjut, labelMulai,
  paketTigaPuluh, pecahSapa, pekanAngka, sapaJam, tandaUbin, tautanLangkah,
} from "../src/layar/dasbor-teks.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const JS = path.join(AKAR, "webapp", "statik", "js");

const belajar = readFileSync(path.join(JS, "layar-belajar.js"), "utf-8");
const inti = readFileSync(path.join(JS, "inti.js"), "utf-8");

/** Ambil satu deklarasi tingkat-atas dari sumber JS, apa adanya. */
function potong(teks, pola, nama) {
  const cocok = teks.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. Sumbernya mungkin ditulis ulang. ` +
        `Perbarui polanya di uji/banding-dasbor.mjs, JANGAN biarkan pagar ini ` +
        `membandingkan nol fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const dariInti = [
  potong(inti, /export const bulat = [^;]+;/, "bulat"),
  potong(inti, /export function angka\(n\) \{[\s\S]*?\n\}/, "angka"),
  potong(inti, /export function tanggalLokal\(iso\) \{[\s\S]*?\n\}/, "tanggalLokal"),
  potong(inti, /export function hariIniISO\(\) \{[\s\S]*?\n\}/, "hariIniISO"),
  potong(inti, /export function tanggalRamah\(iso\) \{[\s\S]*?\n\}/, "tanggalRamah"),
  potong(inti, /export function selisihHari\(iso\) \{[\s\S]*?\n\}/, "selisihHari"),
];

const dariBelajar = [
  potong(belajar, /function kalimatPembuka\(d\) \{[\s\S]*?\n\}/, "kalimatPembuka"),
  potong(belajar, /function bandingHarian\(d\) \{[\s\S]*?\n\}/, "bandingHarian"),
  potong(belajar, /function celahBelajar\(d\) \{[\s\S]*?\n\}/, "celahBelajar"),
  potong(belajar, /function jedaBara\(heatmap\) \{[\s\S]*?\n\}/, "jedaBara"),
  potong(belajar, /function pekanIni\(d\) \{[\s\S]*?\n\}/, "pekanIni"),
  potong(belajar, /function petakPekan\(target, isi\) \{[\s\S]*?\n\}/, "petakPekan"),
  potong(belajar, /function cincinLevel\(d\) \{[\s\S]*?\n\}/, "cincinLevel"),
  potong(belajar, /function kartuBara\(d\) \{[\s\S]*?\n\}/, "kartuBara"),
  potong(belajar, /function blokBara\(d\) \{[\s\S]*?\n\}/, "blokBara"),
  potong(belajar, /function ubinBahasa\(b\) \{[\s\S]*?\n\}/, "ubinBahasa"),
  potong(belajar, /function kartuMulaiUtama\(s, bahasa\) \{[\s\S]*?\n\}/, "kartuMulaiUtama"),
  potong(belajar, /function kartuLanjutkan\(s\) \{[\s\S]*?\n\}/, "kartuLanjutkan"),
  potong(belajar, /function tautanLangkah\(s\) \{[\s\S]*?\n\}/, "tautanLangkah"),
  potong(belajar, /function dasborMeja\(d, ctx, \{ utama[\s\S]*?\n\}/, "dasborMeja"),
  potong(belajar, /function layarMulai\(d, ctx\) \{[\s\S]*?\n\}/, "layarMulai"),
];

/* Dua ekspresi sebaris yang tidak punya fungsinya sendiri di sisi JS, jadi
   DIAMBIL apa adanya lalu dibungkus di sini. Keduanya tetap datang dari
   sumbernya, bukan ditulis ulang -- yang berubah cuma cara memanggilnya. */
const ternarySapa = potong(
  belajar,
  /jam < 11 \? "Selamat pagi" : jam < 15 \? "Selamat siang"\s*\n\s*: jam < 19 \? "Selamat sore" : "Selamat malam"/,
  "ternary sapa",
);
const pecahJudul = potong(
  belajar,
  /const \[awal, \.\.\.sisa\] = sapa\.split\(" "\);/,
  "pecah judulSapa",
);

/* ------------------------------------------------------------- shim DOM */

class Elemen {
  constructor(tag) {
    this.tag = tag;
    this.sifat = {};
    this.anak = [];
    this.gaya = {};
    this.style = { setProperty: (k, v) => { this.gaya[k] = String(v); } };
  }
  setAttribute(k, v) { this.sifat[k] = String(v); }
  appendChild(n) { this.anak.push(n); return n; }
}
globalThis.document = { createElementNS: (_ns, tag) => new Elemen(tag) };

/* `h()` jadi perekam: pemilih, sifat, dan anak-anaknya apa adanya. Nilai
   `null`/`false` disaring persis seperti `tambah()` di `inti.js`. */
const PRELUDE = `
const h = (pemilih, sifat = {}, ...anak) => {
  const el = { pemilih, sifat, anak: [], gaya: sifat && sifat.gaya || {},
               style: { setProperty(k, v) { el.gaya[k] = String(v); } },
               appendChild(n) { el.anak.push(n); return n; },
               get textContent() { return teksDari(el); } };
  for (const a of anak.flat(4)) {
    if (a === null || a === undefined || a === false) continue;
    el.anak.push(a);
  }
  return el;
};
function teksDari(x) {
  if (x === null || x === undefined || x === false) return "";
  if (typeof x !== "object") return String(x);
  return (x.anak || []).map(teksDari).join("");
}
const ikon = (nama, opsi = {}) => ({ ikon: nama, opsi });
const sampul = (benih, opsi = {}) => ({ sampul: benih, opsi });
const bilah = (persen, kelas = "", opsi = {}) => ({ bilah: persen, kelas, opsi });
const pilJenis = (tipe) => ({ pilJenis: tipe });
const keadaan = (o) => ({ keadaan: o });
const kosong = (judul, ket, aksi) => ({ kosong: [judul, ket, aksi] });
const isikan = () => {};
const api = { ambil: () => ({ then: () => ({ catch: () => {} }) }) };
const tanpaNomor = (t) => String(t).replace(/^\\s*\\d+\\.\\s*/, "");
const potong = (t, n) => (t && t.length > n ? t.slice(0, n - 1) + "\\u2026" : t);
/* Mesin gerak dan pengukur DOM: no-op. Yang diadu keputusannya. */
const ungkap = () => {};
const ungkapSekali = (el) => el;
const ungkapSenarai = (el) => el;
const masuk = () => {};
const tata = (_a, f) => { if (f) f(); };
const animasi = () => {};
const berurut = () => () => 0;
const saatTampak = () => () => {};
const saatSiap = () => {};
const adaGerak = () => false;
const gerakPenuh = () => false;
const tingkatGerak = () => "mati";
const nyalakanBara = () => {};
const pinKeHariIni = () => {};
const gerakBeranda = () => () => {};
const panelLangitMeja = (key) => ({ panelLangit: key });
const barisBahasaMeja = (daftar) => ({ barisBahasa: daftar.map((b) => b.key) });
const blokAntrean = (langkah, tantangan) => ({
  antrean: langkah.map((s) => s.judul), tantangan: tantangan ? tantangan.judul : null,
});
const judulSapa = (sapa, nama) => ({ judulSapa: [sapa, nama] });
const kisiUbin = (daftar) => ({ kisi: daftar.map((b) => b.key) });
const ubinKarier = () => ({ ubin: "karier" });
const ubinPustaka = (k, l) => ({ ubin: "pustaka", k, l });
const dasborMejaStub = null;
`;

const EKOR = `
export const sapaJamAcuan = (jam) => (${ternarySapa});
export function pecahSapaAcuan(sapa, nama) {
  ${pecahJudul}
  return { awal, sisa: sisa.join(" ") + (nama ? \`, \${nama}.\` : ".") };
}
export {
  kalimatPembuka, bandingHarian, celahBelajar, jedaBara, pekanIni, cincinLevel,
  kartuBara, blokBara, ubinBahasa, kartuMulaiUtama, kartuLanjutkan,
  tautanLangkah, dasborMeja, layarMulai, hariIniISO,
};
`;

const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-dasbor-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  PRELUDE +
    [...dariInti, ...dariBelajar].join("\n").replace(/^export /gm, "") +
    EKOR,
);
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
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

const tagih = (ok, pesan) => {
  if (ok) return;
  console.error("BENTUK BERUBAH: " + pesan);
  process.exit(1);
};

/* --------------------------------------------- penerjemah pohon -> data */

const teks = (x) => {
  if (x === null || x === undefined || x === false) return "";
  if (typeof x !== "object") return String(x);
  return (x.anak || []).map(teks).join("");
};

function bandingDariPohon(p) {
  tagih(p.pemilih === "div.banding", `banding: ${p.pemilih}`);
  const arah = p.anak.find((a) => a && a.pemilih === "span.banding-arah");
  return { teks: p.anak[0], arah: arah ? arah.anak[0] : null };
}

function celahDariPohon(p) {
  if (!p) return null;
  tagih(p.pemilih === "div.celah", `celah: ${p.pemilih}`);
  const [, b, jarak] = p.anak;
  const m = /· (\d[\d.]*) hari lalu/.exec(teks(jarak));
  tagih(Boolean(m), `celah-jarak: ${teks(jarak)}`);
  return { tanggal: b.anak[0], selisih: Number(m[1].replace(/\./g, "")) };
}

function jedaDariPohon(p) {
  if (!p) return null;
  tagih(p.pemilih === "p.bara-jeda", `jeda: ${p.pemilih}`);
  const m = /Jeda terpanjang ([\d.]+) hari/.exec(p.anak[0]);
  tagih(Boolean(m), `jeda-teks: ${p.anak[0]}`);
  return {
    panjang: Number(m[1].replace(/\./g, "")),
    kapan: p.anak[1].anak[0],
  };
}

function pekanDariPohon(p) {
  if (!p) return null;
  tagih(p.pemilih === "section.pekan", `pekan: ${p.pemilih}`);
  const kepala = p.anak[0];
  const petak = p.anak[1];
  const m = /([\d.]+) XP dalam (\d+) dari 7 hari/.exec(teks(kepala.anak[1]));
  tagih(Boolean(m), `pekan-kepala: ${teks(kepala)}`);
  tagih(petak.pemilih === "div.pekan-petak", `pekan-petak: ${petak.pemilih}`);
  return {
    total: Number(m[1].replace(/\./g, "")),
    aktif: Number(m[2]),
    target: petak.gaya["--target"],
    hari: petak.anak.map((x) => ({
      kelas: x.pemilih,
      judul: x.sifat.title,
      xpTeks: x.anak[0].anak[0] ?? "",
      tinggi: x.anak[1].anak[0].sifat.gaya.height,
      nama: x.anak[2].anak[0] ?? "",
    })),
  };
}

function baraDariPohon(p) {
  tagih(p.pemilih === "section", `bara: ${p.pemilih}`);
  const kartu = p.anak[1];
  const petak = kartu.anak[0];
  tagih(petak.pemilih === "div.bara-petak", `bara-petak: ${petak.pemilih}`);
  const legenda = kartu.anak[kartu.anak.length - 1];
  const m = /([\d.]+) hari ber-XP/.exec(teks(legenda.anak[0]));
  tagih(Boolean(m), `bara-legenda: ${teks(legenda)}`);
  return {
    kosong: petak.anak.filter((x) => x.pemilih === "div.bara-kosong").length,
    aktif: Number(m[1].replace(/\./g, "")),
    sel: petak.anak
      .filter((x) => x.pemilih !== "div.bara-kosong")
      .map((x) => ({ kelas: x.pemilih, judul: x.sifat.title })),
  };
}

function cincinDariPohon(p) {
  tagih(p.pemilih === "div.cincin", `cincin: ${p.pemilih}`);
  const svg = p.anak[0];
  const isi = svg.anak.find((c) => c.sifat.class === "isi");
  tagih(Boolean(isi), "cincin: circle.isi tidak ketemu");
  return {
    panas: p.gaya["--panas"],
    dasharray: isi.sifat["stroke-dasharray"],
    dashoffset: isi.sifat["stroke-dashoffset"],
  };
}

/* ----------------------------------------------------------------- korpus

   DIHASILKAN dengan benih tetap, pola yang sama dengan `banding-kerja.mjs`.
   Benihnya bagian dari pagar: menggantinya berarti mengganti seluruh korpus,
   dan korpus yang berubah tidak membuktikan apa pun soal perubahan yang sedang
   diperiksa. Perluas dengan MENAMBAH di ujung. */
const BENIH = 20261026;
function prng(benih) {
  let b = benih;
  return () => {
    b |= 0;
    b = (b + 0x6d2b79f5) | 0;
    let t = Math.imul(b ^ (b >>> 15), 1 | b);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** Heatmap `n` hari yang berakhir hari ini, dengan pola XP tertentu. */
function heatmap(n, xpDari, acak) {
  const sel = [];
  const kini = new Date();
  for (let i = n - 1; i >= 0; i--) {
    const t = new Date(kini);
    t.setDate(kini.getDate() - i);
    const dua = (x) => String(x).padStart(2, "0");
    sel.push({
      tanggal: `${t.getFullYear()}-${dua(t.getMonth() + 1)}-${dua(t.getDate())}`,
      xp: xpDari(n - 1 - i, acak),
    });
  }
  return sel;
}

const POLA = {
  kosong: () => 0,
  padat: (_i, r) => Math.floor(r() * 120),
  jarang: (i, r) => (i % 11 === 0 ? Math.floor(r() * 90) : 0),
  "jeda-panjang": (i) => (i < 40 ? 30 : i < 150 ? 0 : 45),
  "jeda-di-ujung": (i, _r) => (i < 100 ? 25 : 0),
  "mulai-telat": (i) => (i < 120 ? 0 : 70),
  "tepat-target": () => 60,
  "satu-hari": (i, _r) => (i === 90 ? 999 : 0),
  /* Jeda TEPAT tujuh dan TEPAT enam hari. Keduanya ada karena diukur: ambang
     `panjang < 7` tidak bisa digeser ke `< 8` tanpa satu pun kasus yang
     panjangnya pas tujuh, dan pola lain di atas menghasilkan jeda 0 atau
     ratusan hari. Enam hari ikut supaya sisi "akhir pekan biasa, bukan jeda"
     juga punya saksi. */
  "jeda-tujuh": (i) => (i >= 50 && i < 57 ? 0 : 40),
  "jeda-enam": (i) => (i >= 50 && i < 56 ? 0 : 40),
};

const LANGKAH = (bahasa, tipe, i, menit) => ({
  tipe, bahasa, label_bahasa: bahasa.toUpperCase(),
  judul: `${i + 1}. Judul materi ${i}`, alasan: "alasan " + i, indeks: i,
  ...(menit === null ? {} : { menit }),
});

const PROFIL = [];
for (const [namaPola, fn] of Object.entries(POLA)) {
  for (const hari of [182, 7, 6, 1]) {
    for (const [target, xpKini, kemarin, streak, diLevel, butuhLevel] of [
      [60, 0, 0, 0], [60, 7, 0, 1], [60, 60, 34, 5], [60, 120, 200, 0],
      [1, 0, 0, 0], [500, 120, 120, 2],
      /* `di_level` DI LUAR jangkauan, di kedua arah. Keduanya ada karena
         diukur: tanpa mereka, jepit di `cincinAngka` tidak bisa dicabut tanpa
         satu pun kasus berubah -- 23/90 tidak pernah keluar dari [0,1].
         Keadaannya sendiri bukan karangan: ambang level bisa berubah di
         `progress.py`, dan XP yang sudah tercatat tidak ikut dihitung ulang. */
      [60, 60, 0, 1, 140, 90], [60, 60, 0, 1, -10, 90], [60, 300, 0, 1, 0, 0],
    ]) {
      const acak = prng(BENIH + PROFIL.length);
      PROFIL.push({
        nama: `${namaPola}/${hari}h/t${target}/x${xpKini}`,
        d: {
          xp: 1234, level: 7, gelar: "Penjelajah",
          di_level: diLevel === undefined ? 23 : diLevel,
          butuh_level: butuhLevel === undefined ? 90 : butuhLevel,
          streak, xp_hari_ini: xpKini, xp_kemarin: kemarin,
          hari_belajar_terakhir: namaPola === "kosong" ? null : "2026-10-14",
          target_harian: target, badge_dimiliki: 3, badge_total: 22,
          heatmap: heatmap(hari, fn, acak),
          bahasa: [],
          langkah: [], tantangan: null, kuis_jatuh_tempo: 0, nama: "",
        },
      });
    }
  }
}

// DEVIASI DISENGAJA, SATU-SATUNYA di pagar ini: port tidak memakai dorongan
// streak yang masih ada di layar-belajar.js. Cabangnya hanya tampil saat target
// hari ini belum tercapai, jadi "Jaga apinya tetap menyala." terbaca sebagai
// peringatan bahwa streak akan padam. Tabelnya sempit dengan sengaja: yang
// dibuang persis satu akhiran, dan dua pengaman di bawah menolak tabel yang
// mati (tidak pernah terpakai) atau basi (antarmuka lama sudah berubah).
const DORONGAN_STREAK_LAMA = " Jaga apinya tetap menyala.";
let dorongan = 0;
const tanpaDorongan = (t) => {
  if (!t.endsWith(DORONGAN_STREAK_LAMA)) return t;
  dorongan += 1;
  return t.slice(0, -DORONGAN_STREAK_LAMA.length);
};

for (const { nama, d } of PROFIL) {
  adu(`kalimatPembuka(${nama})`, tanpaDorongan(acuan.kalimatPembuka(d)), kalimatPembuka(d));
  adu(
    `bandingHarian(${nama})`,
    bandingDariPohon(acuan.bandingHarian(d)),
    bandingHarian(d),
  );
  adu(
    `celahBelajar(${nama})`,
    celahDariPohon(acuan.celahBelajar(d)),
    celahBelajar(d),
  );
  adu(
    `jedaBara(${nama})`,
    jedaDariPohon(acuan.jedaBara(d.heatmap)),
    (() => {
      const j = jedaBara(d.heatmap);
      return j && { panjang: j.panjang, kapan: j.kapan };
    })(),
  );
  adu(
    `pekanAngka(${nama})`,
    pekanDariPohon(acuan.pekanIni(d)),
    (() => {
      const p = pekanAngka(d);
      return p && {
        total: p.total, aktif: p.aktif, target: p.target + "%",
        hari: p.hari.map((x) => ({
          kelas: "div.pekan-hari" + (x.kini ? ".kini" : "") + (x.capai ? ".capai" : ""),
          judul: x.judul, xpTeks: x.xpTeks, tinggi: x.tinggi + "%", nama: x.nama,
        })),
      };
    })(),
  );
  adu(
    `baraPetak(${nama})`,
    baraDariPohon(acuan.blokBara(d)),
    (() => {
      const p = baraPetak(d, acuan.hariIniISO());
      return {
        kosong: p.kosong,
        aktif: p.aktif,
        sel: p.sel.map((s) => ({
          kelas:
            "div.bara-sel" +
            (s.tingkat ? ".bara-" + s.tingkat : "") +
            (s.kini ? ".bara-kini" : ""),
          judul: s.judul,
        })),
      };
    })(),
  );
  adu(
    `cincinAngka(${nama})`,
    cincinDariPohon(acuan.cincinLevel(d)),
    (() => {
      const { rasio, panas } = cincinAngka(d);
      const keliling = 2 * Math.PI * 56;
      return {
        panas: String(panas),
        dasharray: String(keliling),
        dashoffset: String(keliling * (1 - rasio)),
      };
    })(),
  );
}

/* ------------------------------------------------- langkah dan paket 30' */

const SET_LANGKAH = [
  [],
  [LANGKAH("python", "materi", 0, 5)],
  [LANGKAH("python", "materi", 0, 5), LANGKAH("python", "kuis", 1, 6),
   LANGKAH("go", "latihan", 2, 8)],
  [LANGKAH("python", "materi", 0, 25), LANGKAH("python", "kuis", 1, 6),
   LANGKAH("go", "latihan", 2, 8)],
  [LANGKAH("python", "materi", 0, 30), LANGKAH("python", "kuis", 1, 1)],
  // Langkah tanpa `menit`: memutus paketnya, tidak dianggap nol.
  [LANGKAH("python", "materi", 0, null), LANGKAH("python", "kuis", 1, 6)],
  [LANGKAH("python", "materi", 0, 10), LANGKAH("python", "kuis", 1, null),
   LANGKAH("go", "latihan", 2, 10)],
  [LANGKAH("c", "entah", 3, 4)],
  /* Totalnya PAS 30 di langkah kedua, dan langkah ketiga melewatinya. Set ini
     ada karena diukur: `> 30` tidak bisa digeser ke `>= 30` tanpa kasus yang
     jumlahnya tepat tiga puluh, dan set di atas yang menyentuh 30 kebetulan
     berakhir dengan satu langkah di kedua varian -- jadi keduanya sama-sama
     tidak menggambar paketnya. */
  [LANGKAH("python", "materi", 0, 10), LANGKAH("python", "kuis", 1, 20),
   LANGKAH("go", "latihan", 2, 5)],
];

for (const [i, langkah] of SET_LANGKAH.entries()) {
  const d = {
    ...PROFIL[0].d, langkah, xp: 500,
    bahasa: [], posisi: { key: "python", label: "Python", bab: 4, bab_total: 11,
                          bab_judul: "Bab empat", materi: 14, total_materi: 44 },
  };
  const pohon = acuan.dasborMeja(d, { awal: { bahasa: [] } }, {
    utama: langkah[0], sisaLangkah: langkah.slice(1), dijalani: [],
    bento: null, sapa: "Selamat pagi",
  });
  const kini = pohon.anak[0].anak[0];
  const paketEl = kini.anak.find((x) => x && x.pemilih === "p.meja-paket");
  const m = paketEl
    ? /Punya 30 menit\? (\d+) langkah teratas kira-kira (\d+) menit\./.exec(
        teks(paketEl))
    : null;
  tagih(!paketEl || Boolean(m), `meja-paket: ${paketEl && teks(paketEl)}`);
  const p = paketTigaPuluh(langkah);
  adu(
    `paketTigaPuluh(set ${i})`,
    m ? { muat: Number(m[1]), total: Number(m[2]) } : null,
    p.muat.length > 1 ? { muat: p.muat.length, total: p.total } : null,
  );

  const posisiEl = kini.anak.find((x) => x && x.pemilih === "p.meja-posisi");
  adu(
    `posisi(set ${i})`,
    posisiEl ? teks(posisiEl) : null,
    "Python · Bab 4 dari 11: Bab empat · 14/44 materi",
  );

  for (const s of langkah) {
    const kartu = acuan.kartuLanjutkan(s);
    tagih(kartu.pemilih === "a.lanjutkan", `lanjutkan: ${kartu.pemilih}`);
    adu(`tautanLangkah(${s.tipe})`, kartu.sifat.href, tautanLangkah(s));
    // DICARI lewat pemilihnya, bukan lewat indeks: `kartuLanjutkan` menempel
    // sampul sebagai anak pertama, jadi indeks yang dihitung tangan menunjuk
    // nomor kartunya dan pagarnya mengadu "1" dengan sebuah kalimat.
    const isi = kartu.anak.find((x) => x && x.pemilih === "div.lanjutkan-isi");
    tagih(Boolean(isi), "lanjutkan-isi tidak ketemu");
    adu(
      `labelLanjut(${s.tipe})`,
      teks(isi.anak[0]),
      `${labelLanjut(s.tipe)} · ${s.label_bahasa}` +
        (s.menit ? ` · ≈${s.menit} menit` : ""),
    );
  }
}

/* ------------------------------------------------------- sapaan dan ubin */

for (let jam = 0; jam < 24; jam++) {
  adu(`sapaJam(${jam})`, acuan.sapaJamAcuan(jam), sapaJam(jam));
}
for (const nama of ["", "Vi", "Nama Panjang Sekali"]) {
  for (const sapa of ["Selamat pagi", "Selamat malam", "Hai", ""]) {
    adu(
      `pecahSapa(${JSON.stringify(sapa)}, ${JSON.stringify(nama)})`,
      acuan.pecahSapaAcuan(sapa, nama),
      pecahSapa(sapa, nama),
    );
  }
}

const UBIN = [
  { key: "html", label: "HTML", siap: true, hilang: [], materi: 23, kuis: 5, latihan: 12 },
  { key: "go", label: "Go", siap: false, hilang: ["go"], pasang: "sudo dnf install golang", materi: 30, kuis: 7, latihan: 15 },
  { key: "vb", label: "VB", siap: false, hilang: ["dotnet", "mono"], pasang: "x", materi: 20, kuis: 4, latihan: 10 },
  { key: "python", label: "Python", siap: true, pasang: "sudo dnf install python3", materi: 44, kuis: 7, latihan: 19 },
  /* TIDAK siap DAN tanpa perintah pemasangan: satu-satunya bentuk yang
     membedakan urutan kedua cabang `tandaUbin`. Ia bukan karangan --
     `runner.perintah_instalasi()` mengembalikan string kosong untuk runner
     yang tidak punya perintah terdaftar, dan binernya tetap bisa hilang.
     Yang harus menang "butuh", bukan "tanpa pasang apa pun": menyebut sesuatu
     bebas pasang padahal ia tidak bisa dijalankan adalah janji yang langsung
     dibantah layar berikutnya. */
  { key: "entah", label: "Entah", siap: false, hilang: ["entah"], materi: 5, kuis: 1, latihan: 2 },
];
for (const b of UBIN) {
  const pohon = acuan.ubinBahasa(b);
  tagih(pohon.pemilih === "a.ubin", `ubin: ${pohon.pemilih}`);
  const tanda = pohon.anak.find((x) => x && x.pemilih === "span.ubin-tanda");
  adu(
    `tandaUbin(${b.key})`,
    tanda ? [tanda.sifat.kelas, teks(tanda)] : null,
    tandaUbin(b),
  );
  adu(
    `ubinJml(${b.key})`,
    teks(pohon.anak.find((x) => x && x.pemilih === "span.ubin-jml")),
    `${b.materi} materi · ${b.latihan} latihan`,
  );
}

adu("jumlahKurikulum", (() => {
  const pohon = acuan.layarMulai(
    { ...PROFIL[0].d, langkah: [] },
    { awal: { bahasa: UBIN, aturan_bab: {} } },
  );
  const sub = pohon.el.anak[0].anak[2];
  tagih(sub.pemilih === "p.sambut-sub", `sambut-sub: ${sub.pemilih}`);
  return teks(sub);
})(), (() => {
  const j = jumlahKurikulum(UBIN);
  const a = (n) => n.toLocaleString("id-ID");
  return `${a(UBIN.length)} bahasa · ${a(j.materi)} materi · ` +
    `${a(j.kuis)} kuis · ${a(j.latihan)} latihan. ` +
    "Pilih satu; sisanya menunggu dan tidak ke mana-mana.";
})());

for (const s of [LANGKAH("html", "materi", 0, 5), LANGKAH("go", "latihan", 2, 8),
                 LANGKAH("c", "entah", 1, 3)]) {
  const pohon = acuan.kartuMulaiUtama(s, UBIN);
  tagih(pohon.pemilih === "a.mulai-utama", `mulai-utama: ${pohon.pemilih}`);
  const b = UBIN.find((x) => x.key === s.bahasa);
  adu(
    `labelMulai(${s.tipe}/${s.bahasa})`,
    teks(pohon.anak[0].anak[2]),
    b && !b.pasang
      ? `${labelMulai(s.tipe)}. Tidak perlu memasang apa pun: cukup aplikasi ini dan ` +
        "browser yang sedang kamu buka."
      : `${labelMulai(s.tipe)}. Langkah pertama di jalur ${s.label_bahasa}.`,
  );
}

/* ------------------------------------------- bahasa yang sedang dijalani */

const SET_BAHASA = [
  [],
  [{ key: "a", label: "A", siap: true, materi: 1, total_materi: 10, persen: 0 }],
  [
    { key: "a", label: "A", siap: true, materi: 1, total_materi: 10, persen: 12 },
    { key: "b", label: "B", siap: true, materi: 9, total_materi: 10, persen: 95 },
    { key: "c", label: "C", siap: true, materi: 0, total_materi: 10, persen: 0 },
    { key: "d", label: "D", siap: true, materi: 5, total_materi: 10, persen: 50 },
    { key: "e", label: "E", siap: true, materi: 2, total_materi: 10, persen: 20 },
    { key: "f", label: "F", siap: true, materi: 3, total_materi: 10, persen: 30 },
    { key: "g", label: "G", siap: true, materi: 4, total_materi: 10, persen: 40 },
    { key: "h", label: "H", siap: true, materi: 10, total_materi: 10, persen: 100 },
  ],
];
for (const [i, bahasa] of SET_BAHASA.entries()) {
  const d = { ...PROFIL[0].d, bahasa, langkah: [], xp: 9 };
  const pohon = acuan.dasborMeja(d, { awal: { bahasa: [] } }, {
    utama: undefined, sisaLangkah: [],
    dijalani: bahasa.filter((b) => b.persen > 0)
      .sort((a, b) => b.persen - a.persen).slice(0, 6),
    bento: null, sapa: "Selamat pagi",
  });
  const antrean = pohon.anak[0].anak[1];
  const baris = antrean.anak.find((x) => x && x.barisBahasa);
  adu(
    `dijalaniDasbor(set ${i})`,
    baris ? baris.barisBahasa : null,
    dijalaniDasbor(bahasa).slice(0, 4).map((b) => b.key),
  );
}

if (dorongan === 0 || !belajar.includes(DORONGAN_STREAK_LAMA.trim())) {
  console.error(
    `DEVIASI MATI ATAU BASI: dorongan streak terpakai ${dorongan}x dan ` +
      `${belajar.includes(DORONGAN_STREAK_LAMA.trim()) ? "masih" : "TIDAK lagi"} ` +
      `ada di layar-belajar.js. Perbarui atau hapus DORONGAN_STREAK_LAMA.`,
  );
  process.exit(1);
}

console.log(
  `${cacah} perbandingan atas ${PROFIL.length} profil dasbor, ` +
    `${SET_LANGKAH.length} set langkah, ${UBIN.length} ubin bahasa`,
);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: bagian murni dasbor identik dengan layar-belajar.js.");
