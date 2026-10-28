/* Memeriksa logika pohon berkas (`komponen/pohon-teks.ts`).
 *
 * Tidak ada JS lama untuk diadu, jadi yang ditagih adalah SIFAT yang dijanjikan
 * komentar kepala modulnya, atas dua jenis masukan: SELURUH kode kurikulum yang
 * nyata (dibaca dari `packages/konten/`, 25 blok multi-berkas) dan kasus
 * sintetis berbenih tetap untuk bentuk yang tidak ada di data. Oracle ditulis
 * sendiri di sini (hitungan lurus, bukan salinan algoritmanya).
 *
 *   [pecah]    blok nyata: nama sama dengan yang dikenali server, TIDAK ADA BARIS HILANG
 *   [bentuk]   bentuk penanda, pembuka, nama ganda, berkas kosong, CRLF
 *   [pohon]    jalur bertingkat, urutan penulis, folder berantai dipadatkan
 *   [tampak]   baris yang tampak: kedalaman, induk, posisi
 *   [langkah]  navigasi papan ketik menurut pola WAI-ARIA tree
 *   [teks]     jalur, penyorot per ekstensi, nama yang dibacakan
 *
 *     node uji/banding-pohon.mjs
 */

import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { bahasaDikenal } from "../../bersama/src/sorot.ts";
import {
  POLA_PENANDA, barisTampak, bangunPohon, hitungBerkas, jalurBerkas, labelBaris, langkahPohon,
  pecahBerkas, semuaFolder, sorotBerkas,
} from "../src/komponen/pohon-teks.ts";

let cacah = 0;
let gagal = 0;
function adu(kategori, nama, ok, rinci = "") {
  cacah += 1;
  if (!ok) {
    gagal += 1;
    console.error(`[${kategori}] ${nama}${rinci === "" ? "" : "  " + JSON.stringify(rinci)}`);
  }
}

function acak(benih) {
  let a = benih >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const R = acak(20261028);
const bulat = (n) => Math.floor(R() * n);

const SINI = path.dirname(fileURLToPath(import.meta.url));
const KONTEN = path.join(SINI, "..", "..", "konten", "kurikulum");

/* Oracle deteksi, sama dengan server (`berkas_ganda` di inti/berkas.py): pola yang sama dicari DI MANA SAJA. */
const POLA_SERVER = /(?:\/\*|\/\/|#|--)\s*=*\s*[Ff]ile\s*:\s*([\w./-]+)/g;
const bersih = (n) => n.split("/").filter((s) => s !== "" && s !== ".").join("/");
function namaServer(kode) {
  const nama = [...kode.matchAll(POLA_SERVER)].map((m) => bersih(m[1])).filter((n) => n !== "");
  const unik = [...new Set(nama)];
  return unik.length >= 2 ? unik : [];
}
const lurusPenanda = (b) => POLA_PENANDA.test(b);
const takKosong = (kode) => kode.split(/\r?\n/).filter((b) => b.trim() !== "");
const DASH = [String.fromCharCode(0x2014), String.fromCharCode(0x2013)];

/* ------------------------------------------------ pecah: SELURUH blok nyata */
const nyata = [];
for (const f of readdirSync(KONTEN).sort()) {
  const lang = JSON.parse(readFileSync(path.join(KONTEN, f), "utf-8"));
  for (const m of lang.materi) {
    m.sections.forEach((s, si) => {
      if (s.code) nyata.push({ nama: `${lang.key}/${m.title}#${si}`, kode: s.code });
    });
  }
}
let banyakMulti = 0;
let adaCatatan = false;
let adaPembukaMenempel = false;
const semuaNama = [];
for (const b of nyata) {
  const harap = namaServer(b.kode);
  const h = pecahBerkas(b.kode);
  adu("pecah", `${b.nama}: dipecah tepat bila server menyebutnya multi`, (h !== null) === (harap.length >= 2), { harap });
  if (!h) continue;
  banyakMulti++;
  adu("pecah", `${b.nama}: nama dan urutan sama dengan server`, JSON.stringify(h.berkas.map((x) => x.nama)) === JSON.stringify(harap), h.berkas.map((x) => x.nama));
  semuaNama.push(...h.berkas.map((x) => x.nama));

  // TIDAK ADA BARIS YANG HILANG: baris tak kosong bukan-penanda, berurutan, sama dengan gabungan catatan dan berkas.
  const asli = takKosong(b.kode).filter((x) => !lurusPenanda(x));
  const pecahan = takKosong([h.catatan, ...h.berkas.map((x) => x.isi)].join("\n"));
  adu("pecah", `${b.nama}: tidak ada baris hilang, bertambah, atau tertukar`, JSON.stringify(asli) === JSON.stringify(pecahan), { asli: asli.length, pecahan: pecahan.length });

  for (const x of h.berkas) {
    const baris = x.isi === "" ? [] : x.isi.split("\n");
    adu("pecah", `${b.nama}/${x.nama}: tanpa baris kosong di ujung`, baris.length === 0 || (baris[0].trim() !== "" && baris[baris.length - 1].trim() !== ""));
    adu("pecah", `${b.nama}/${x.nama}: jumlah baris tercatat benar`, x.baris === baris.length, { baris: x.baris, nyata: baris.length });
    adu("pecah", `${b.nama}/${x.nama}: tanpa nama berawalan ./ atau segmen kosong`, x.nama === bersih(x.nama) && x.nama !== "");
  }
  adu("pecah", `${b.nama}: catatan hanya berisi komentar`, h.catatan === "" || takKosong(h.catatan).every((x) => /^\s*(?:\/\/|#|--|\/\*|\*)/.test(x)), h.catatan.slice(0, 40));
  if (h.catatan.startsWith("// Siapkan dulu:")) adaCatatan = true;
  if (h.berkas[0].isi.startsWith("<?php")) adaPembukaMenempel = true;
}
adu("pecah", "korpus nyata memuat 25 blok multi-berkas (pagar anti korpus kosong)", banyakMulti >= 25, banyakMulti);
adu("pecah", "pembuka berupa komentar jadi catatan (materi Go)", adaCatatan);
adu("pecah", "pembuka bukan komentar menempel di berkas pertama (<?php di materi PHPUnit)", adaPembukaMenempel);

/* ------------------------------------------------ bentuk sintetis */
{
  const h = (k) => pecahBerkas(k);
  adu("bentuk", "satu nama saja: bukan multi", h("# File: a.py\nx = 1\n") === null);
  adu("bentuk", "nama yang sama dua kali: tetap bukan multi", h("# File: a.py\nx = 1\n# File: a.py\ny = 2\n") === null);
  adu("bentuk", "tanpa penanda: bukan multi", h("x = 1\ny = 2\n") === null && h("") === null);
  adu("bentuk", "penanda di tengah baris bukan penanda", h("x = 1  # file: a.py\ny = 2  # file: b.py\n") === null);

  const dua = h("# File: a.py\nA = 1\n\n\n# File: b/c.py\nB = 2\n");
  adu("bentuk", "dua berkas: nama, isi, jumlah baris", dua && dua.berkas.length === 2 && dua.berkas[0].nama === "a.py" && dua.berkas[0].isi === "A = 1" && dua.berkas[1].nama === "b/c.py" && dua.berkas[1].baris === 1 && dua.catatan === "", dua);

  const bentuk = h("/* ===== File: m.h ===== */\nint f(void);\n-- file: x.sql\nSELECT 1;\n// ==== file: ./d/e.go ====\npackage e\n");
  adu("bentuk", "bentuk penanda: blok komentar C, dua tanda hubung SQL, garis sama dengan Go", bentuk && JSON.stringify(bentuk.berkas.map((x) => x.nama)) === JSON.stringify(["m.h", "x.sql", "d/e.go"]), bentuk);
  adu("bentuk", "penanda dihapus dari isi (tidak ikut tampil)", bentuk && bentuk.berkas.every((x) => !/file\s*:/i.test(x.isi)), bentuk);

  const crlf = h("# File: a.py\r\nA = 1\r\n# File: b.py\r\nB = 2\r\n");
  adu("bentuk", "baris Windows (CRLF) tidak meninggalkan karakter CR di isi", crlf && crlf.berkas.every((x) => !x.isi.includes("\r")) && crlf.berkas[0].isi === "A = 1", crlf);

  const ganda = h("# File: a.py\nA = 1\n# File: b.py\nB = 2\n# File: a.py\nC = 3\n");
  adu("bentuk", "nama ganda digabung ke satu berkas, dipisah satu baris kosong", ganda && ganda.berkas.length === 2 && ganda.berkas[0].isi === "A = 1\n\nC = 3", ganda);

  const kosong = h("# File: a/__init__.py\n# File: a/b.py\nX = 1\n");
  adu("bentuk", "berkas kosong: isi kosong dan nol baris", kosong && kosong.berkas[0].isi === "" && kosong.berkas[0].baris === 0 && kosong.berkas[1].baris === 1, kosong);

  const indent = h("# File: a.py\n\n\n    x = 1\n\n  y = 2\n\n\n# File: b.py\nz = 3\n");
  adu("bentuk", "baris kosong di ujung dipangkas, inden dan baris kosong di tengah dipertahankan", indent && indent.berkas[0].isi === "    x = 1\n\n  y = 2" && indent.berkas[0].baris === 3, indent);

  const catatan = h("// Siapkan dulu:\n//   mkdir x\n\n// ==== file: a.go ====\npackage a\n// ==== file: b.go ====\npackage b\n");
  adu("bentuk", "pembuka berupa komentar jadi catatan", catatan && catatan.catatan === "// Siapkan dulu:\n//   mkdir x" && catatan.berkas[0].isi === "package a", catatan);
  const menempel = h("<?php\n// ==== File: src/a.php ====\ndeclare(strict_types=1);\n// ==== File: src/b.php ====\n<?php\n");
  adu("bentuk", "pembuka bukan komentar menempel di depan berkas pertama", menempel && menempel.catatan === "" && menempel.berkas[0].isi === "<?php\ndeclare(strict_types=1);", menempel);
  const campur = h("# komentar\nimport os\n# File: a.py\nA = 1\n# File: b.py\nB = 2\n");
  adu("bentuk", "pembuka campuran (komentar dan kode): seluruhnya menempel, tidak terpecah", campur && campur.catatan === "" && campur.berkas[0].isi === "# komentar\nimport os\nA = 1", campur);
  adu("bentuk", "penanda tanpa nama yang berarti (hanya titik) dianggap baris biasa", h("# File: .\nx\n# File: a.py\n1\n# File: b.py\n2\n")?.berkas.length === 2);
}

/* ------------------------------------------------ pohon */
const daftarKunci = (pohon) => {
  const k = [];
  const jalan = (d) => d.forEach((s) => { k.push(s.kunci); jalan(s.anak); });
  jalan(pohon);
  return k;
};
const daun = (pohon) => {
  const d = [];
  const jalan = (daftar, jalur) => daftar.forEach((s) => {
    const baru = jalur === "" ? s.label : `${jalur}/${s.label}`;
    if (s.folder) jalan(s.anak, baru); else d.push({ jalur: baru, berkas: s.berkas, kunci: s.kunci });
  });
  jalan(pohon, "");
  return d;
};
function periksaPohon(label, nama) {
  const pohon = bangunPohon(nama);
  const d = daun(pohon);
  adu("pohon", `${label}: satu daun per berkas, indeksnya 0..n-1 tanpa kembar`, d.length === nama.length && new Set(d.map((x) => x.berkas)).size === nama.length && d.every((x) => x.berkas >= 0 && x.berkas < nama.length), d.length);
  adu("pohon", `${label}: jalur dari akar ke daun sama dengan nama berkas`, d.every((x) => x.jalur === nama[x.berkas]) && d.every((x) => x.kunci === nama[x.berkas]), d.slice(0, 2));
  const kunci = daftarKunci(pohon);
  adu("pohon", `${label}: kunci unik di seluruh pohon`, new Set(kunci).size === kunci.length);
  let tiga = "";
  const telusur = (daftar) => daftar.forEach((s) => {
    if (s.folder) {
      if (s.anak.length === 0) tiga = `folder kosong ${s.kunci}`;
      if (s.anak.length === 1 && s.anak[0].folder) tiga = `folder berantai tak dipadatkan ${s.kunci}`;
      if (hitungBerkas(s) < 1) tiga = `folder tanpa berkas ${s.kunci}`;
      telusur(s.anak);
    } else if (hitungBerkas(s) !== 1 || s.anak.length !== 0) tiga = `daun ganjil ${s.kunci}`;
  });
  telusur(pohon);
  adu("pohon", `${label}: folder berantai dipadatkan, tak ada folder kosong`, tiga === "", tiga);
  adu("pohon", `${label}: jumlah berkas di bawah akar sama dengan jumlah nama`, pohon.reduce((t, s) => t + hitungBerkas(s), 0) === nama.length);
  return pohon;
}
for (const b of nyata) {
  const h = pecahBerkas(b.kode);
  if (h) periksaPohon(b.nama, h.berkas.map((x) => x.nama));
}
{
  const a = bangunPohon(["a/b/c.py"]);
  adu("pohon", "rantai satu berkas dipadatkan jadi satu folder berlabel a/b", a.length === 1 && a[0].folder && a[0].label === "a/b" && a[0].kunci === "a/b" && a[0].anak.length === 1 && a[0].anak[0].label === "c.py", a);
  const b = bangunPohon(["src/main/java/id/Aplikasi.java", "src/main/resources/app.properties"]);
  adu("pohon", "cabang menghentikan pemadatan: src/main lalu java/id dan resources",
    b.length === 1 && b[0].label === "src/main" && b[0].anak.map((s) => s.label).join("|") === "java/id|resources", b);
  const c = bangunPohon(["z.py", "a/x.py", "m.py", "a/y.py"]);
  adu("pohon", "urutan penulis dipertahankan, bukan abjad; folder di tempat berkas pertamanya", c.map((s) => s.label).join("|") === "z.py|a|m.py" && c[1].anak.map((s) => s.label).join("|") === "x.py|y.py", c);
  adu("pohon", "tanpa nama: pohon kosong", bangunPohon([]).length === 0);
  const d = bangunPohon(["./a//b.py", "c.py"]);
  adu("pohon", "segmen titik dan kosong dibuang: folder a berisi b.py, lalu c.py",
    d.length === 2 && d[0].folder && d[0].kunci === "a" && d[0].anak[0].kunci === "a/b.py" && d[0].anak[0].label === "b.py" && d[1].kunci === "c.py", d);
  const e = bangunPohon(["a/b/x.py", "a/b/y.py", "a/z.py"]);
  adu("pohon", "folder bercabang tidak dipadatkan walau anaknya folder (a punya b dan z.py)", e.length === 1 && e[0].label === "a" && e[0].anak.length === 2, e);
}
{
  // Pohon acak: setiap pemadatan harus menjaga seluruh berkas.
  for (let k = 0; k < 200; k++) {
    const n = 1 + bulat(12);
    const nama = [];
    const dipakai = new Set();
    while (nama.length < n) {
      const dalam = bulat(5);
      const bagian = Array.from({ length: dalam }, () => ["src", "lib", "a", "b", "tes"][bulat(5)]);
      const berkas = `${["x", "y", "z", "m"][bulat(4)]}${bulat(40)}.${["py", "js", "go"][bulat(3)]}`;
      const jalur = [...bagian, berkas].join("/");
      if (dipakai.has(jalur)) continue;
      dipakai.add(jalur);
      nama.push(jalur);
    }
    periksaPohon(`acak ${k}`, nama);
  }
}

/* ------------------------------------------------ tampak */
function periksaTampak(label, pohon, terbuka) {
  const baris = barisTampak(pohon, terbuka);
  let masalah = "";
  baris.forEach((b, i) => {
    if (b.kedalaman === 0 && b.induk !== -1) masalah = `tingkat atas ber-induk di ${i}`;
    if (b.kedalaman > 0) {
      const p = baris[b.induk];
      if (!p || !p.simpul.folder || !terbuka.has(p.simpul.kunci) || p.kedalaman !== b.kedalaman - 1 || b.induk >= i) masalah = `induk ${i} salah`;
    }
    if (b.posisi < 1 || b.posisi > b.ukuran) masalah = `posisi ${i}`;
  });
  // Saudara serumah: posisi menaik 1..ukuran dalam urutan baris.
  const peta = new Map();
  baris.forEach((b) => { const k = `${b.induk}`; if (!peta.has(k)) peta.set(k, []); peta.get(k).push(b); });
  for (const [, g] of peta) g.forEach((b, i) => { if (b.posisi !== i + 1 || b.ukuran !== g.length) masalah = `saudara ${b.simpul.kunci}`; });
  adu("tampak", `${label}: kedalaman, induk, posisi konsisten`, masalah === "", masalah);
  return baris;
}
for (const b of nyata) {
  const h = pecahBerkas(b.kode);
  if (!h) continue;
  const pohon = bangunPohon(h.berkas.map((x) => x.nama));
  const folder = semuaFolder(pohon);
  const semuaTerbuka = periksaTampak(`${b.nama} terbuka`, pohon, new Set(folder));
  adu("tampak", `${b.nama}: semua terbuka = folder + berkas`, semuaTerbuka.length === folder.length + h.berkas.length, { baris: semuaTerbuka.length });
  const semuaTutup = periksaTampak(`${b.nama} tertutup`, pohon, new Set());
  adu("tampak", `${b.nama}: semua tertutup = anak teratas saja`, semuaTutup.length === pohon.length && semuaTutup.every((x) => x.kedalaman === 0));
}

/* ------------------------------------------------ langkah */
{
  const pohon = bangunPohon(["package.json", "alat/matematika.js", "alat/uang.js", "src/main/java/id/App.java", "src/main/resources/app.properties", "utama.js"]);
  const folder = semuaFolder(pohon);
  const buka = new Set(folder);
  const baris = barisTampak(pohon, buka);
  const idx = (kunci) => baris.findIndex((b) => b.simpul.kunci === kunci);
  const aksi = (i, t, set = buka, b = baris) => langkahPohon(b, i, t, set);

  adu("langkah", "tanpa baris: bukan milik pohon", langkahPohon([], 0, "ArrowDown", buka) === null);
  adu("langkah", "tombol lain: null", aksi(0, "a") === null && aksi(0, "Tab") === null && aksi(0, "Escape") === null);
  adu("langkah", "bawah dan atas dijepit di ujung, tanpa berputar", aksi(baris.length - 1, "ArrowDown")?.fokus === baris.length - 1 && aksi(0, "ArrowUp")?.fokus === 0);
  adu("langkah", "Home dan End", aksi(3, "Home")?.fokus === 0 && aksi(3, "End")?.fokus === baris.length - 1);

  const i = idx("alat");
  adu("langkah", "kanan di folder terbuka pindah ke anak pertama", aksi(i, "ArrowRight")?.fokus === i + 1 && baris[i + 1].induk === i && aksi(i, "ArrowRight")?.buka === undefined);
  const tutup = new Set(buka); tutup.delete("alat");
  const barisTutup = barisTampak(pohon, tutup);
  const j = barisTutup.findIndex((b) => b.simpul.kunci === "alat");
  adu("langkah", "kanan di folder tertutup membukanya, fokus tetap", aksi(j, "ArrowRight", tutup, barisTutup)?.buka === "alat" && aksi(j, "ArrowRight", tutup, barisTutup)?.fokus === j);
  adu("langkah", "kiri di folder terbuka menutupnya, fokus tetap", aksi(i, "ArrowLeft")?.tutup === "alat" && aksi(i, "ArrowLeft")?.fokus === i);
  adu("langkah", "kiri di folder tertutup tingkat atas diam di tempat", aksi(j, "ArrowLeft", tutup, barisTutup)?.fokus === j);
  const k = idx("alat/uang.js");
  adu("langkah", "kiri di berkas pindah ke folder induknya", aksi(k, "ArrowLeft")?.fokus === i && aksi(k, "ArrowLeft")?.tutup === undefined);
  adu("langkah", "kanan di berkas tidak berbuat apa-apa", aksi(k, "ArrowRight")?.fokus === k && aksi(k, "ArrowRight")?.buka === undefined);
  adu("langkah", "Enter dan Spasi di berkas memilihnya", aksi(k, "Enter")?.pilih === true && aksi(k, " ")?.pilih === true);
  adu("langkah", "Enter di folder terbuka menutupnya, di tertutup membukanya",
    aksi(i, "Enter")?.tutup === "alat" && aksi(j, "Enter", tutup, barisTutup)?.buka === "alat" && aksi(i, "Enter")?.pilih === undefined);
  adu("langkah", "fokus di luar jangkauan dijepit, tidak melempar", aksi(999, "ArrowUp")?.fokus === baris.length - 2 && aksi(-5, "ArrowDown")?.fokus === 1);
}
for (let k = 0; k < 300; k++) {
  const n = 2 + bulat(8);
  const nama = [];
  const dipakai = new Set();
  while (nama.length < n) {
    const bagian = Array.from({ length: bulat(4) }, () => ["src", "lib", "a", "b"][bulat(4)]);
    const jalur = [...bagian, `f${bulat(30)}.py`].join("/");
    if (!dipakai.has(jalur)) { dipakai.add(jalur); nama.push(jalur); }
  }
  const pohon = bangunPohon(nama);
  const buka = new Set(semuaFolder(pohon).filter(() => R() < 0.6));
  const baris = barisTampak(pohon, buka);
  for (let i = 0; i < baris.length; i++) {
    for (const t of ["ArrowDown", "ArrowUp", "ArrowRight", "ArrowLeft", "Home", "End", "Enter", " "]) {
      const a = langkahPohon(baris, i, t, buka);
      if (a === null) { adu("langkah", `acak: ${t} dari ${i} tidak boleh null`, false); continue; }
      adu("langkah", `acak: ${t} dari ${i}/${baris.length} tetap di dalam daftar`, a !== null && Number.isInteger(a.fokus) && a.fokus >= 0 && a.fokus < baris.length, a);
      const s = baris[i].simpul;
      if (t === "ArrowRight" && s.folder && buka.has(s.kunci)) adu("langkah", "acak: kanan di folder terbuka masuk ke anaknya", baris[a.fokus].induk === i, { i, a });
      if (t === "ArrowLeft" && !(s.folder && buka.has(s.kunci)) && baris[i].induk >= 0) adu("langkah", "acak: kiri naik ke induk yang folder", a.fokus === baris[i].induk && baris[a.fokus].simpul.folder, { i, a });
      if ((t === "Enter" || t === " ") && !s.folder) adu("langkah", "acak: Enter di berkas memilih tanpa membuka apa pun", a.pilih === true && a.buka === undefined && a.tutup === undefined);
    }
  }
}

/* ------------------------------------------------ teks */
{
  adu("teks", "jalurBerkas memisah folder dan nama", JSON.stringify(jalurBerkas("toko/model/produk.py")) === JSON.stringify({ folder: "toko/model/", berkas: "produk.py" }) && JSON.stringify(jalurBerkas("main.py")) === JSON.stringify({ folder: "", berkas: "main.py" }));
  const tabel = [
    ["a.py", "python"], ["x/y.js", "javascript"], ["u.mjs", "javascript"], ["package.json", "javascript"], ["m.ts", "typescript"],
    ["k.go", "go"], ["kas.c", "c"], ["kecil.h", "c"], ["r.cpp", "cpp"], ["r.hpp", "cpp"], ["R.java", "java"], ["R.kt", "kotlin"],
    ["s/R.php", "php"], ["x.rb", "ruby"], ["x.rs", "rust"], ["x.sh", "bash"], ["q.sql", "sql"], ["index.html", "html"],
    ["gaya.css", "css"], ["gaya.scss", "css"], ["docker-compose.yml", "yaml"], ["a.yaml", "yaml"], ["x.toml", "toml"],
    ["application.properties", "ini"], [".env", "ini"], ["a/B.CS", "csharp"], ["GAYA.CSS", "css"],
    ["Makefile", ""], ["Dockerfile", ""], [".dockerignore", ""], [".gitignore", ""], ["go.mod", ""], ["pesan.txt", ""], ["x.tidakada", ""], ["README", ""],
  ];
  for (const [n, harap] of tabel) adu("teks", `sorotBerkas(${n}) = ${harap === "" ? "(polos)" : harap}`, sorotBerkas(n) === harap, sorotBerkas(n));
  for (const n of semuaNama) {
    const s = sorotBerkas(n);
    adu("teks", `penyorot untuk ${n} dikenal penyorot klien (atau polos)`, s === "" || bahasaDikenal(s), s);
  }
  const pohon = bangunPohon(["src/a.py", "src/b.py", "k.py"]);
  const berkas = [{ nama: "src/a.py", isi: "x", baris: 1 }, { nama: "src/b.py", isi: "", baris: 0 }, { nama: "k.py", isi: "a\nb", baris: 2 }];
  const baris = barisTampak(pohon, new Set(semuaFolder(pohon)));
  adu("teks", "folder: nama, kata folder, jumlah berkas", labelBaris(baris[0], berkas) === "src, folder, 2 berkas", labelBaris(baris[0], berkas));
  adu("teks", "berkas: nama dan jumlah baris", labelBaris(baris[1], berkas) === "a.py, 1 baris" && labelBaris(baris[3], berkas) === "k.py, 2 baris", [labelBaris(baris[1], berkas), labelBaris(baris[3], berkas)]);
  adu("teks", "berkas kosong disebut kosong, bukan 0 baris", labelBaris(baris[2], berkas) === "b.py, kosong", labelBaris(baris[2], berkas));
  for (const s of [labelBaris(baris[0], berkas), labelBaris(baris[1], berkas)]) adu("teks", "tanpa dash", !s.includes(DASH[0]) && !s.includes(DASH[1]), s);
}

console.log(gagal ? `GAGAL: ${gagal} dari ${cacah} perbandingan` : `COCOK: ${cacah} perbandingan, pohon berkas sesuai janji kepala modulnya`);
process.exit(gagal ? 1 : 0);
