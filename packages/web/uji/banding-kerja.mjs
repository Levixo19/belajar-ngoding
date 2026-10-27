/* Adu bagian murni ruang kerja dengan `webapp/statik/js/layar-kerja.js`.
 *
 * Empat algoritma, satu akibat yang sama kalau bergeser: pelajar melihat
 * perbedaan antara kodenya dan kode yang benar di tempat yang salah. Satu
 * karakter yang hilang menggambar baris yang TIDAK pernah ditulis siapa pun,
 * dan tidak ada cara ia tahu bedanya.
 *
 * Korpus `bedaBaris` DIHASILKAN, bukan ditulis tangan: 558 solusi latihan
 * diganggu dengan gangguan yang deterministik (benih 20261020) -- baris
 * dihapus, baris disisipkan, kata ditukar, dua baris ditukar posisinya,
 * indentasi digeser. Yang ditulis tangan cuma kasus PINGGIRAN `bedaKata`,
 * karena ketiga jalur `null`-nya memang tidak pernah terpicu kode kurikulum.
 *
 * Benihnya bagian dari pagar ini: menggantinya berarti mengganti seluruh
 * korpus, dan korpus yang berubah tidak membuktikan apa pun soal perubahan
 * yang sedang diperiksa. Perluas dengan MENAMBAH gangguan di ujung daftar.
 *
 * `jadwalRamah` SENGAJA tidak ikut. Ia membaca jam, jadi dua pemanggilan yang
 * mengapit tengah malam akan memberi jawaban berbeda dengan benar -- pagar
 * yang bisa merah tanpa ada yang rusak adalah pagar yang berhenti dibaca.
 * Yang diadu `tanggalLokal`, bagian murninya.
 *
 *     node uji/banding-kerja.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  bedaBaris, bedaKata, contohAwal, nomorDiBaris, pasangkanUbahan, pecahToken,
  pisahRekor,
} from "../src/layar/kerja-beda.ts";
import { tanggalLokal } from "../src/waktu.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const KERJA = path.join(AKAR, "webapp", "statik", "js", "layar-kerja.js");
const INTI = path.join(AKAR, "webapp", "statik", "js", "inti.js");
const KONTEN = path.join(AKAR, "packages", "konten");

function potong(dari, pola, nama) {
  const cocok = dari.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. Sumbernya mungkin ditulis ulang. ` +
        `Perbarui polanya, JANGAN biarkan pagar ini membandingkan nol fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const kerja = readFileSync(KERJA, "utf-8");
const inti = readFileSync(INTI, "utf-8");

const bagian = [
  potong(kerja, /const AMBANG_REKOR = \d+;/, "AMBANG_REKOR"),
  potong(kerja, /const LANGKAH_REKOR = \d+;/, "LANGKAH_REKOR"),
  potong(kerja, /export function pisahRekor\([\s\S]*?\n\}/, "pisahRekor"),
  potong(kerja, /const POLA_BARIS_BERKAS = [^\n]+/, "POLA_BARIS_BERKAS"),
  potong(kerja, /const POLA_KATA_LINE = [^\n]+/, "POLA_KATA_LINE"),
  potong(kerja, /function nomorDiBaris\(teks\) \{[\s\S]*?\n\}/, "nomorDiBaris"),
  potong(kerja, /function bedaBaris\(a, b\) \{[\s\S]*?\n\}/, "bedaBaris"),
  potong(kerja, /const BATAS_SEL_KATA = \d+;/, "BATAS_SEL_KATA"),
  potong(kerja, /const POLA_TOKEN_KATA = [^\n]+/, "POLA_TOKEN_KATA"),
  potong(kerja, /function pecahToken\(s\) \{[\s\S]*?\n\}/, "pecahToken"),
  potong(kerja, /function bedaKata\(a, b\) \{[\s\S]*?\n\}/, "bedaKata"),
  potong(kerja, /function pasangkanUbahan\(baris\) \{[\s\S]*?\n\}/, "pasangkanUbahan"),
  potong(kerja, /function contohAwal\(bahasa\) \{[\s\S]*?\n\}/, "contohAwal"),
  potong(inti, /export function tanggalLokal\(iso\) \{[\s\S]*?\n\}/, "tanggalLokal"),
];

const kode = bagian.join("\n").replace(/^export /gm, "");
const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-kerja-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  kode + "\nexport {pisahRekor, nomorDiBaris, bedaBaris, pecahToken, bedaKata,"
    + " pasangkanUbahan, contohAwal, tanggalLokal};\n",
);
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
let takUtuh = 0;
let cemar = 0;
/* Fungsi yang bergeser DITALLY, bukan cuma lima temuan pertama yang dicetak.
   Lima baris pertama tergantung URUTAN perbandingan di berkas ini, bukan pada
   lapisan mana yang patah -- satu perubahan di `bedaKata` memerahkan
   `pasangkanUbahan` lebih dulu (ia memanggilnya), dan yang terbaca di laporan
   jadi lapisan yang salah. Ia juga yang dipakai baterai mutasi sebagai
   kategori keluhan. */
const fungsiBergeser = new Set();
const adu = (nama, a, b) => {
  const sa = JSON.stringify(a);
  const sb = JSON.stringify(b);
  if (sa !== sb) {
    gagal += 1;
    fungsiBergeser.add(String(nama).split(" ")[0]);
    if (gagal <= 5) {
      console.error(
        `  ${nama}\n    JS: ${sa.slice(0, 200)}\n    TS: ${sb.slice(0, 200)}`,
      );
    }
  }
};

/* --------------------------------------------------------------- korpus */

const solusi = [];
for (const nama of readdirSync(path.join(KONTEN, "kurikulum")).sort()) {
  const lang = JSON.parse(
    readFileSync(path.join(KONTEN, "kurikulum", nama), "utf-8"),
  );
  for (const x of lang.latihan) {
    if (x.solution) solusi.push({ nama: `${lang.key}/${x.title}`, kode: x.solution });
  }
}

/** PRNG berbenih (mulberry32). Deterministik, dan itu seluruh gunanya. */
function prng(benih) {
  let a = benih >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/* Lima gangguan, masing-masing menyasar satu bentuk kesalahan yang nyata
   dilakukan pelajar: lupa satu baris, menambah baris, salah ketik satu kata,
   menukar urutan dua baris, dan salah indentasi. */
const GANGGUAN = [
  (b, r) => { const i = Math.floor(r() * b.length); return b.filter((_x, k) => k !== i); },
  (b, r) => {
    const i = Math.floor(r() * (b.length + 1));
    return [...b.slice(0, i), "print('sisipan')", ...b.slice(i)];
  },
  (b, r) => {
    const i = Math.floor(r() * b.length);
    return b.map((t, k) => (k === i ? t.replace(/[\p{L}\p{N}_]+/u, "beda") : t));
  },
  (b, r) => {
    if (b.length < 2) return b;
    const i = Math.floor(r() * (b.length - 1));
    const c = [...b];
    [c[i], c[i + 1]] = [c[i + 1], c[i]];
    return c;
  },
  (b, r) => {
    const i = Math.floor(r() * b.length);
    return b.map((t, k) => (k === i ? "  " + t : t));
  },
];

const r = prng(20261020);
let pasanganBeda = 0;
const barisKata = [];
for (const s of solusi) {
  const asli = s.kode.split("\n");
  for (let g = 0; g < GANGGUAN.length; g++) {
    const ubah = GANGGUAN[g](asli, r);
    pasanganBeda += 1;

    const js = acuan.bedaBaris(asli, ubah);
    const ts = bedaBaris(asli, ubah);
    adu(`bedaBaris ${s.nama} #${g}`, js, ts);

    // Kemurnian `pasangkanUbahan` ditagih SENDIRI, bukan lewat hasilnya.
    // Versi yang memutasi butir masukannya di tempat mengembalikan daftar
    // yang sama persis, jadi perbandingan hasil tidak bisa melihatnya -- yang
    // rusak baru terasa di pemanggil berikutnya yang masih memegang daftar
    // lama, dan di situ tidak ada apa pun yang menunjuk ke sini.
    const sebelumTs = JSON.stringify(ts);
    adu(`pasangkanUbahan ${s.nama} #${g}`,
        acuan.pasangkanUbahan(js), pasangkanUbahan(ts));
    if (JSON.stringify(ts) !== sebelumTs) cemar += 1;

    // Pasangan baris yang benar-benar berubah dikumpulkan untuk diadu lagi
    // sebagai masukan `bedaKata` langsung, tanpa lewat perjodohannya.
    for (let k = 0; k + 1 < ts.length; k++) {
      if (ts[k].tanda === "-" && ts[k + 1].tanda === "+") {
        barisKata.push([ts[k].teks, ts[k + 1].teks]);
      }
    }
  }
  // Kontrak lossless `pecahToken`, ditagih sendiri: kedua sisi bisa konsisten
  // salah, dan hasil yang cocok tidak akan memberi tahu apa pun soal itu.
  for (const t of asli) {
    if (pecahToken(t).join("") !== t) takUtuh += 1;
  }
}

for (const [a, b] of barisKata) {
  adu(`bedaKata ${JSON.stringify(a).slice(0, 40)}`,
      acuan.bedaKata(a, b), bedaKata(a, b));
}

/* ------------------------------------------------- bedaKata, tiga jalur null */

const PINGGIR = [
  [null, "a"], ["a", null], [undefined, undefined], [42, "a"], [{}, "a"],
  ["", ""], ["", "abc"], ["abc", ""],
  ["sama", "sama"],
  // Nol token bukan-spasi yang sama -> null, bukan "semua kata disorot".
  ["aaa bbb", "ccc ddd"],
  [" ", "  "],
  // Di atas BATAS_SEL_KATA: 250 token x 250 token = 62.500 sel.
  [Array.from({ length: 250 }, (_x, i) => "k" + i).join(" "),
   Array.from({ length: 250 }, (_x, i) => "j" + i).join(" ")],
  // Tepat di bawah atapnya.
  [Array.from({ length: 60 }, (_x, i) => "k" + i).join(" "),
   Array.from({ length: 60 }, (_x, i) => "k" + i).join(" ") + " lagi"],
  ["huruf beraksen: naïve café", "huruf beraksen: naive cafe"],
  ["tab\there", "tab  here"],
  ["a·b→c", "a·b c"],
];
PINGGIR.forEach(([a, b], i) => {
  adu(`bedaKata pinggiran #${i}`, acuan.bedaKata(a, b), bedaKata(a, b));
});

/* ------------------------------------------------------------- pisahRekor */

for (const s of solusi) {
  const baris = s.kode.split("\n");
  for (const maks of [1, 2, 3, 4]) {
    adu(`pisahRekor ${s.nama} maks=${maks}`,
        acuan.pisahRekor(baris, maks), pisahRekor(baris, maks));
  }
  adu(`pisahRekor ${s.nama} bawaan`, acuan.pisahRekor(baris), pisahRekor(baris));
}
for (const aneh of [null, undefined, [], ["satu"], ["a", "b"]]) {
  adu(`pisahRekor aneh ${JSON.stringify(aneh)}`,
      acuan.pisahRekor(aneh), pisahRekor(aneh));
}

/* ----------------------------------------------------------- nomorDiBaris */

const GALAT = [
  "Traceback (most recent call last):",
  '  File "/tmp/xyz/jawab.py", line 7, in <module>',
  "jawab.py:12: error: something",
  "Main.java:3: error: ';' expected",
  "  at Main.main(Main.java:14)",
  "error[E0425]: cannot find value `x` in this scope",
  "  --> src/main.rs:4:5",
  "line 99",
  "tanpa nomor sama sekali",
  "",
  "a.b:0",
  "C:\\kerja\\jawab.cs:21",
  "line 2 dan line 5",
  "99 line",
];
GALAT.forEach((g, i) => {
  adu(`nomorDiBaris #${i}`, acuan.nomorDiBaris(g), nomorDiBaris(g));
});

/* ------------------------------------------------------------- contohAwal
 *
 * Diadu BYTE-PER-BYTE. Satu salah ketik di salah satu dari sembilan belas
 * string itu berarti Ruang Coba terbuka dengan program yang tidak bisa
 * dikompilasi, pada bahasa yang mungkin tidak ada yang mencobanya selama
 * berbulan-bulan. Daftar bahasanya dibaca dari registry kurikulum, bukan
 * diketik di sini: bahasa baru yang contohnya lupa ditambahkan akan terlihat
 * sebagai dua string kosong yang cocok -- jadi yang menagihnya pagar di
 * bawahnya, bukan perbandingan ini. */

const bahasaRunner = new Set();
for (const nama of readdirSync(path.join(KONTEN, "kurikulum")).sort()) {
  const lang = JSON.parse(
    readFileSync(path.join(KONTEN, "kurikulum", nama), "utf-8"),
  );
  bahasaRunner.add(lang.runner);
}
const RUNNER = [...bahasaRunner].sort();
for (const b of [...RUNNER, "bahasa-yang-tidak-ada", ""]) {
  adu(`contohAwal ${b || "(kosong)"}`, acuan.contohAwal(b), contohAwal(b));
}
/* Celah yang SENGAJA dibawa dari aplikasi lama. Kosong sekarang.
 *
 * Port ini menuntut identitas byte dengan `contohAwal` di `layar-kerja.js`,
 * jadi runner yang contohnya ditambahkan di satu sisi saja memerahkan
 * perbandingan di atas. Runner `git` pernah ada di sini: ia lolos
 * `runner.tersedia()` dan muncul di pemilih Ruang Coba, tapi editornya terbuka
 * KOSONG. Ia ditambal di KEDUA sisi sekaligus (f99e16a), satu-satunya cara
 * tanpa memerahkan pembanding ini.
 *
 * Daftarnya tetap ada karena tetap bergigi: runner BARU yang contohnya
 * terlewat tidak ada di sini, jadi ia memerahkan pagarnya. */
const CELAH_DIKETAHUI = new Set([]);
const tanpaContoh = RUNNER.filter(
  (b) => !contohAwal(b) && !CELAH_DIKETAHUI.has(b),
);
const celahDibawa = RUNNER.filter((b) => !contohAwal(b) && CELAH_DIKETAHUI.has(b));

/* ----------------------------------------------------------- tanggalLokal */

const ISO = ["2026-10-20", "2026-01-01", "2026-12-31", "1999-02-28",
             "2026-02-29", "bukan tanggal", "", null, undefined,
             "2026-10-20T13:45:00", "2026-10-20T13:45:00Z", "2026-10-7"];
ISO.forEach((iso, i) => {
  const a = acuan.tanggalLokal(iso);
  const b = tanggalLokal(iso);
  adu(`tanggalLokal #${i} ${iso}`,
      a === null ? null : a.getTime(), b === null ? null : b.getTime());
});

if (tanpaContoh.length) {
  console.error(
    `RUNNER TANPA CONTOH AWAL: ${tanpaContoh.join(", ")}. Ruang Coba akan ` +
      `terbuka dengan editor KOSONG untuk bahasa itu, dan perbandingan di ` +
      `atas tetap hijau karena kedua sisi sama-sama kosong.`,
  );
}
if (celahDibawa.length) {
  console.log(`celah dibawa dari aplikasi lama: contoh awal kosong untuk ` +
              `${celahDibawa.join(", ")}`);
}
console.log(`${solusi.length} solusi, ${pasanganBeda} pasangan beda, ` +
            `${barisKata.length} pasangan baris, ${PINGGIR.length} pinggiran, ` +
            `${GALAT.length} baris galat, ${ISO.length} tanggal`);
if (takUtuh) {
  console.error(
    `PECAH TOKEN RUSAK: ${takUtuh} baris. ` +
      `pecahToken(s).join("") tidak sama dengan s, jadi diff kata akan ` +
      `menggambar baris yang tidak pernah ditulis siapa pun.`,
  );
}
if (cemar) {
  console.error(
    `MENCEMARI MASUKAN: ${cemar} pemanggilan pasangkanUbahan mengubah daftar ` +
      `yang diberikan kepadanya. Hasilnya tetap sama, jadi yang rusak baru ` +
      `terasa di pemanggil berikutnya yang masih memegang daftar lama.`,
  );
}
if (gagal || takUtuh || cemar || tanpaContoh.length) {
  if (gagal) {
    console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
    console.error(`FUNGSI BERGESER: ${[...fungsiBergeser].sort().join(", ")}`);
  }
  process.exit(1);
}
console.log("COCOK: bagian murni ruang kerja TypeScript identik dengan layar-kerja.js.");
