/* Pemeriksaan penampil pohon berkas di halaman materi (`PohonBerkas.tsx`).
 *
 * Profil UJI dengan semua bab dibuka (`buka_semua_bab` di berkas konfigurasi
 * profil itu); `mulai()` menggagalkan semua permintaan selain GET, jadi tidak
 * ada progres yang tertulis. Korpusnya ke-25 blok multi-berkas yang NYATA,
 * dibaca dari `packages/konten/`. Yang diukur adalah perilaku:
 *
 *   A satu blok: peran ARIA, jumlah baris, kepala panel, isi berkas pertama
 *   B SEMUA blok nyata: tiap berkas diklik, isi panel persis sama dengan isinya
 *   C folder: buka dan tutup dengan klik
 *   D papan ketik: roving tabindex, panah, Home dan End, Enter dan Spasi
 *   E penunjuk: klik memilih dan memfokus, tidak menavigasi
 *   F kontras teks dan penanda di empat tema
 *   G tata letak di 1440 dan 1280 dan huruf sangat besar
 *   H kebersihan: konsol, tulisan ditolak, kontrol bukan-multi, kaki blok
 *   J Salin berkas ini
 *
 *   BELAJAR_URL=http://127.0.0.1:7788/ node --experimental-strip-types uji/manual/pohon-berkas.mjs
 *   HANYA=A,D   menjalankan bagian tertentu saja (dipakai baterai mutan)
 *   FOTO=/jalur/pendek   menyimpan tangkapan layar tiap bagian
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { bangunPohon, barisTampak, labelBaris, pecahBerkas, semuaFolder, sorotBerkas } from "../../src/komponen/pohon-teks.ts";
import { URL_DASAR, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Pohon berkas");
const FOTO = process.env.FOTO ?? "";
if (FOTO) fs.mkdirSync(FOTO, { recursive: true });
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
const tunggu = (page, ms) => page.waitForTimeout(ms);
const SINI = path.dirname(fileURLToPath(import.meta.url));
const KONTEN = path.join(SINI, "..", "..", "..", "konten", "kurikulum");
const POLA_DASH = new RegExp("[" + String.fromCharCode(0x2014, 0x2013) + "]");

/* Korpus nyata: tiap blok multi dengan letaknya (kurikulum, indeks materi, urutan di materi itu). */
const blokNyata = [];
for (const f of fs.readdirSync(KONTEN).sort()) {
  const lang = JSON.parse(fs.readFileSync(path.join(KONTEN, f), "utf-8"));
  lang.materi.forEach((m, mi) => {
    let urut = 0;
    m.sections.forEach((s) => {
      if (!s.code) return;
      const h = pecahBerkas(s.code);
      if (h) blokNyata.push({ kunci: lang.key, mi, urut: urut++, judul: m.title.replace(/^\d+\.\s*/, ""), h });
    });
  });
}

const PYTHON = blokNyata.find((b) => b.kunci === "python" && b.h.berkas[0].nama === "toko/__init__.py");
const buka = (o = {}) => mulai({ lebar: 1440, tinggi: 900, tema: "gelap", gerak: "mati", hash: `#/materi/${PYTHON.kunci}/${PYTHON.mi}`, tunggu: ".pb-wadah", ...o });
const foto = (page, nama) => (FOTO ? page.locator(".blok-kode", { has: page.locator(".pb-wadah") }).first().screenshot({ path: `${FOTO}/${nama}.png` }) : null);

/** Pindah ke materi lain di dalam aplikasi yang sama, menunggu judulnya benar-benar berganti. */
async function ke(page, b) {
  await page.evaluate((h) => { location.hash = h; }, `#/materi/${b.kunci}/${b.mi}`);
  await page.waitForFunction(([judul, n]) => {
    const h1 = document.querySelector("h1");
    return h1 && h1.textContent.includes(judul) && document.querySelectorAll(".pb-wadah").length >= n;
  }, [b.judul, b.urut + 1], { timeout: 10000 });
}

/** Baris pohon yang diharapkan (semua folder terbuka), dalam urutan DOM. */
function barisHarap(b) {
  const pohon = bangunPohon(b.h.berkas.map((x) => x.nama));
  return barisTampak(pohon, new Set(semuaFolder(pohon)));
}

const keadaan = (page, n = 0) => page.evaluate((n) => {
  const w = document.querySelectorAll(".pb-wadah")[n];
  const baris = [...w.querySelectorAll(".pb-baris")];
  const pre = w.querySelector(".pb-isi pre.kode");
  return {
    baris: baris.length,
    label: baris.map((e) => e.getAttribute("aria-label")),
    dipilih: baris.filter((e) => e.getAttribute("aria-selected") === "true").map((e) => e.getAttribute("aria-label")),
    terbuka: baris.map((e) => e.getAttribute("aria-expanded")),
    aktif: document.activeElement?.closest(".pb-baris")?.getAttribute("aria-label") ?? null,
    tab0: baris.filter((e) => e.tabIndex === 0).length,
    jalur: w.querySelector(".pb-jalur")?.textContent ?? null,
    meta: w.querySelector(".pb-meta")?.textContent ?? null,
    isi: pre ? pre.textContent : (w.querySelector(".pb-kosong") ? "" : null),
    spans: pre ? pre.querySelectorAll('[class^="tk-"]').length : 0,
    jenis: pre ? [...new Set([...pre.querySelectorAll('[class^="tk-"]')].map((e) => e.className))] : [],
    catatan: w.querySelector(".pb-catatan")?.textContent ?? null,
    regionNama: w.querySelector(".pb-isi")?.getAttribute("aria-label") ?? null,
    panah: baris.map((e) => (e.classList.contains("pb-folder") ? getComputedStyle(e.querySelector(".pb-panah")).transform : null)),
  };
}, n);

const ukur = (page, sel, prop) => page.evaluate(([s, pr]) => {
  const el = document.querySelector(s); if (!el) return null;
  const rgba = (css) => { const c = document.createElement("canvas"); c.width = c.height = 1; const x = c.getContext("2d", { willReadFrequently: true }); x.clearRect(0, 0, 1, 1); x.fillStyle = css; x.fillRect(0, 0, 1, 1); const d = x.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255]; };
  const lapis = [];
  for (let e = el; e; e = e.parentElement) { const c = rgba(getComputedStyle(e).backgroundColor); if (c[3] > 0) lapis.push(c); if (c[3] >= 1) break; }
  let bg = [255, 255, 255];
  for (const [r, g, b, a] of lapis.reverse()) bg = [r * a + bg[0] * (1 - a), g * a + bg[1] * (1 - a), b * a + bg[2] * (1 - a)];
  const fg = rgba(getComputedStyle(el)[pr]);
  const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const L = (c) => 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]);
  const a = L(fg), b = L(bg);
  return Math.round(((Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05)) * 100) / 100;
}, [sel, prop]);

const idr = (n) => n.toLocaleString("id-ID");
const metaHarap = (x) => (x.baris === 0 ? "kosong" : `${idr(x.baris)} baris`);

/* ------------------------------------------------ A satu blok */
if (jalan("A")) {
  const s = await buka(); const page = s.page;
  const harap = barisHarap(PYTHON);
  const k = await keadaan(page);
  P.cek(`A ${PYTHON.h.berkas.length} berkas bertingkat jadi ${harap.length} baris pohon`, k.baris === harap.length, { baris: k.baris, harap: harap.length });
  P.cek("A nama tiap baris sama dengan labelBaris (nama, folder, jumlah baris)", JSON.stringify(k.label) === JSON.stringify(harap.map((b) => labelBaris(b, PYTHON.h.berkas))), k.label);
  const peran = await page.evaluate(() => {
    const w = document.querySelector(".pb-wadah"); const t = w.querySelector(".pb-pohon");
    const baris = [...w.querySelectorAll(".pb-baris")];
    return {
      tree: t.getAttribute("role"), nama: t.getAttribute("aria-label"),
      item: baris.every((e) => e.getAttribute("role") === "treeitem"),
      level: baris.map((e) => Number(e.getAttribute("aria-level"))),
      pos: baris.map((e) => `${e.getAttribute("aria-posinset")}/${e.getAttribute("aria-setsize")}`),
      region: w.querySelector(".pb-isi").getAttribute("role"), regionNama: w.querySelector(".pb-isi").getAttribute("aria-label"),
    };
  });
  P.cek("A peran: tree bernama, treeitem tiap baris, panel kode region bernama berkasnya", peran.tree === "tree" && /^Berkas/.test(peran.nama) && peran.item && peran.region === "region" && peran.regionNama === "Isi " + PYTHON.h.berkas[0].nama, peran);
  P.cek("A aria-level mengikuti kedalaman (toko 1, isinya 2, model/ isinya 3)", JSON.stringify(peran.level) === JSON.stringify(harap.map((b) => b.kedalaman + 1)), peran.level);
  P.cek("A aria-posinset/aria-setsize benar di antara saudara", JSON.stringify(peran.pos) === JSON.stringify(harap.map((b) => `${b.posisi}/${b.ukuran}`)), peran.pos);
  P.cek("A folder terbuka sejak awal (aria-expanded true), berkas tanpa aria-expanded", JSON.stringify(k.terbuka) === JSON.stringify(harap.map((b) => (b.simpul.folder ? "true" : null))), k.terbuka);
  P.cek("A folder terbuka ditandai segitiga yang diputar (aria-expanded true punya transform)", k.panah.filter((t) => t !== null).length === harap.filter((b) => b.simpul.folder).length && k.panah.filter((t) => t !== null).every((t) => t !== "none"), k.panah);
  P.cek("A berkas pertama terpilih (satu-satunya aria-selected)", k.dipilih.length === 1 && k.dipilih[0] === labelBaris(harap.find((b) => !b.simpul.folder && b.simpul.berkas === 0), PYTHON.h.berkas), k.dipilih);
  P.cek("A kepala panel: jalur berkas dan jumlah barisnya", k.jalur === PYTHON.h.berkas[0].nama && k.meta === metaHarap(PYTHON.h.berkas[0]), { jalur: k.jalur, meta: k.meta });
  P.cek("A isi panel = isi berkas pertama persis", k.isi === PYTHON.h.berkas[0].isi);
  P.cek("A tidak ada blok kode utuh tersisa di luar penampil (isi tidak dobel)",
    await page.evaluate(() => { const b = document.querySelector(".blok-kode:has(.pb-wadah)"); return b.querySelectorAll(":scope > .blok-sarung > pre.kode").length === 0; }));
  await foto(page, "A-python");
  await s.tutup();
}

/* ------------------------------------------------ B seluruh blok nyata */
if (jalan("B")) {
  const s = await buka(); const page = s.page;
  P.cek(`B korpus nyata memuat 25 blok multi (${blokNyata.length})`, blokNyata.length >= 25, blokNyata.length);
  let jumlahBerkas = 0; let berwarnaKhas = 0; let polosKataKunci = 0; let berwarna = 0;
  // Jenis token yang HANYA ada dengan penyorot bahasanya. Pewarnaan dasar pemindai (string, angka, operator, dan
  // nama yang disusul kurung sebagai fungsi) ada untuk bahasa apa pun, jadi tidak bisa dijadikan tanda.
  const KHAS = new Set(["tk-kunci", "tk-komentar", "tk-bawaan"]);
  for (const b of blokNyata) {
    await ke(page, b);
    const harap = barisHarap(b);
    const k0 = await keadaan(page, b.urut);
    const nama = `${b.kunci}/${b.judul.slice(0, 28)}#${b.urut}`;
    P.cek(`B ${nama}: ${harap.length} baris pohon`, k0.baris === harap.length, { baris: k0.baris, harap: harap.length });
    P.cek(`B ${nama}: catatan ${b.h.catatan ? "tampil persis" : "tidak ada"}`, b.h.catatan ? k0.catatan === b.h.catatan : k0.catatan === null, k0.catatan);
    const berkasBaris = harap.map((x, i) => ({ x, i })).filter((r) => !r.x.simpul.folder);
    let salah = "";
    for (const { x, i } of berkasBaris) {
      const idx = x.simpul.berkas;
      const sasaran = b.h.berkas[idx];
      await page.locator(".pb-wadah").nth(b.urut).locator(".pb-baris").nth(i).click();
      const k = await keadaan(page, b.urut);
      jumlahBerkas++;
      if (k.jalur !== sasaran.nama) salah = `jalur ${k.jalur} bukan ${sasaran.nama}`;
      else if (k.isi !== sasaran.isi) salah = `isi ${sasaran.nama} tidak sama (${(k.isi ?? "null").length} vs ${sasaran.isi.length})`;
      else if (k.meta !== metaHarap(sasaran)) salah = `meta ${sasaran.nama}: ${k.meta}`;
      else if (k.regionNama !== "Isi " + sasaran.nama) salah = `nama region ${sasaran.nama}: ${k.regionNama}`;
      else if (k.dipilih.length !== 1 || k.dipilih[0] !== labelBaris(x, b.h.berkas)) salah = `terpilih ${sasaran.nama}: ${JSON.stringify(k.dipilih)}`;
      if (salah) break;
      const warna = sorotBerkas(sasaran.nama);
      if (warna === "" && k.jenis.some((j) => KHAS.has(j))) polosKataKunci++;
      if (warna !== "" && sasaran.isi !== "") { berwarna++; if (k.jenis.some((j) => KHAS.has(j))) berwarnaKhas++; }
    }
    P.cek(`B ${nama}: tiap berkas diklik, panel = isinya persis (${berkasBaris.length} berkas)`, salah === "", salah);
  }
  P.cek(`B ${jumlahBerkas} berkas diperiksa; yang tidak dikenal penyorotnya tanpa kata kunci, komentar, atau nama bawaan`, jumlahBerkas >= 60 && polosKataKunci === 0, { jumlahBerkas, polosKataKunci });
  // Pewarnaan dasar (string, angka, operator) ada di SEMUA berkas, jadi yang diukur token khas bahasa: kata kunci, komentar, kunci.
  P.cek("B berkas yang dikenal penyorotnya benar-benar bertoken khas bahasanya (>= 80 persen)", berwarna > 0 && berwarnaKhas / berwarna >= 0.8, { berwarna, berwarnaKhas, rasio: Math.round((berwarnaKhas / berwarna) * 100) / 100 });
  P.cek("B tanpa galat konsol selain POST yang sengaja digagalkan harness", s.konsol.filter((x) => !/ERR_FAILED/.test(x)).length === 0, s.konsol.filter((x) => !/ERR_FAILED/.test(x)));
  await s.tutup();
}

/* ------------------------------------------------ C folder */
if (jalan("C")) {
  const s = await buka(); const page = s.page;
  const w = page.locator(".pb-wadah").first();
  const harap = barisHarap(PYTHON);
  const iToko = harap.findIndex((b) => b.simpul.kunci === "toko");
  await w.locator(".pb-baris").nth(iToko).click();
  let k = await keadaan(page);
  const sisa = harap.filter((b) => b.kedalaman === 0).length;
  P.cek("C klik folder teratas menutupnya: tinggal baris tingkat atas", k.baris === sisa && k.terbuka[iToko] === "false", { baris: k.baris, sisa });
  P.cek("C folder tertutup: segitiganya kembali tegak (tanpa transform)", k.panah[iToko] === "none" && k.panah[harap.findIndex((b) => b.simpul.kunci === "toko/model")] !== "none", k.panah);
  P.cek("C isi panel tidak berubah saat folder ditutup (berkas terpilih tetap tampil)", k.jalur === PYTHON.h.berkas[0].nama && k.isi === PYTHON.h.berkas[0].isi);
  await w.locator(".pb-baris").nth(iToko).click();
  k = await keadaan(page);
  P.cek("C klik lagi membukanya: semua baris kembali", k.baris === harap.length && k.terbuka[iToko] === "true", k.baris);
  const iModel = harap.findIndex((b) => b.simpul.kunci === "toko/model");
  await w.locator(".pb-baris").nth(iModel).click();
  k = await keadaan(page);
  P.cek("C folder bersarang menutup hanya isinya sendiri", k.baris === harap.length - 2 && k.terbuka[iModel] === "false" && k.terbuka[iToko] === "true", k.baris);
  P.cek("C klik folder tidak memilih berkas dan tidak mengubah panel", k.jalur === PYTHON.h.berkas[0].nama);
  await foto(page, "C-folder-tertutup");
  await s.tutup();
}

/* ------------------------------------------------ D papan ketik */
if (jalan("D")) {
  const s = await buka(); const page = s.page;
  const w = page.locator(".pb-wadah").first();
  const harap = barisHarap(PYTHON);
  const lab = (kunci) => labelBaris(harap.find((b) => b.simpul.kunci === kunci), PYTHON.h.berkas);
  const k0 = await keadaan(page);
  P.cek("D roving tabindex: tepat satu baris berperhentian Tab (berkas terpilih)", k0.tab0 === 1);
  await w.locator('.pb-baris[tabindex="0"]').focus();
  const urut = [
    ["ArrowDown", "toko/uang.py", "bawah: baris berikutnya"],
    ["ArrowDown", "toko/model", "bawah ke folder"],
    ["ArrowRight", "toko/model/__init__.py", "kanan di folder terbuka: anak pertama"],
    ["ArrowLeft", "toko/model", "kiri di berkas: folder induknya"],
    ["ArrowLeft", "toko/model", "kiri di folder terbuka: menutupnya, fokus tetap"],
    ["ArrowRight", "toko/model", "kanan di folder tertutup: membukanya, fokus tetap"],
    ["End", "main.py", "End: baris terakhir"],
    ["ArrowDown", "main.py", "bawah di ujung: tidak berputar"],
    ["Home", "toko", "Home: baris pertama"],
    ["ArrowUp", "toko", "atas di ujung: tidak berputar"],
    ["ArrowLeft", "toko", "kiri di folder teratas terbuka: menutupnya"],
    ["ArrowDown", "main.py", "bawah dari folder tertutup: berkas berikutnya"],
  ];
  let salah = null;
  for (const [tombol, kunci, ket] of urut) {
    await page.keyboard.press(tombol); await tunggu(page, 60);
    const k = await keadaan(page);
    if (k.aktif !== lab(kunci)) { salah = { tombol, ket, aktif: k.aktif, harap: lab(kunci) }; break; }
  }
  P.cek(`D ${urut.length} penekanan: fokus mengikuti pola tree`, salah === null, salah);
  let k = await keadaan(page);
  P.cek("D menutup toko lewat kiri menyembunyikan isinya (tinggal toko dan main.py)", k.baris === 2 && k.terbuka[0] === "false", k.baris);

  await page.keyboard.press("Enter"); await tunggu(page, 60);
  k = await keadaan(page);
  P.cek("D Enter di berkas memilihnya (panel berganti ke main.py)", k.jalur === "main.py" && k.dipilih.length === 1 && k.isi === PYTHON.h.berkas.find((b) => b.nama === "main.py").isi, k.jalur);
  await page.keyboard.press("ArrowUp"); await tunggu(page, 60);
  await page.keyboard.press(" "); await tunggu(page, 60);
  k = await keadaan(page);
  P.cek("D Spasi di folder tertutup membukanya", k.baris === harap.length && k.terbuka[0] === "true", k.baris);
  await page.keyboard.press("ArrowDown"); await tunggu(page, 60);
  await page.keyboard.press(" "); await tunggu(page, 60);
  k = await keadaan(page);
  P.cek("D Spasi di berkas memilihnya", k.jalur === PYTHON.h.berkas[0].nama && k.dipilih[0] === lab("toko/__init__.py"), k.jalur);
  await page.keyboard.press("Enter"); await tunggu(page, 60);
  P.cek("D Enter di berkas tidak menjalankan apa pun (blok multi tidak punya tombol Jalankan)", (await page.locator(".keluaran-kartu").count()) === 0);

  const lepas = await page.evaluate(() => {
    const e = document.activeElement;
    const dari = (key, init) => { const ev = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true, ...init }); e.dispatchEvent(ev); return ev.defaultPrevented; };
    return { alt: dari("ArrowLeft", { altKey: true }), ctrl: dari("ArrowDown", { ctrlKey: true }), meta: dari("Home", { metaKey: true }), polos: dari("ArrowDown", {}), tab: dari("Tab", {}), huruf: dari("a", {}), esc: dari("Escape", {}) };
  });
  P.cek("D Alt, Ctrl, dan Meta bersama panah dilepas; panah polos ditelan; Tab, huruf, Esc dibiarkan",
    !lepas.alt && !lepas.ctrl && !lepas.meta && lepas.polos && !lepas.tab && !lepas.huruf && !lepas.esc, lepas);
  const ring = await page.evaluate(() => { const e = document.activeElement; const c = getComputedStyle(e); return { fv: e.matches(":focus-visible"), gaya: c.outlineStyle, lebar: parseFloat(c.outlineWidth), geser: parseFloat(c.outlineOffset) }; });
  P.cek("D cincin fokus terlihat dan jatuh DI DALAM baris (kontainernya menggulir, cincin luar akan terpotong)", ring.fv && ring.gaya !== "none" && ring.lebar >= 2 && ring.geser < 0, ring);
  const terakhirFokus = (await keadaan(page)).aktif;
  await page.keyboard.press("Tab"); await tunggu(page, 60);
  P.cek("D Tab keluar dari pohon (tidak menyusuri tiap baris)", await page.evaluate(() => !document.activeElement?.closest(".pb-pohon")));
  await page.keyboard.press("Shift+Tab"); await tunggu(page, 60);
  k = await keadaan(page);
  P.cek("D Shift+Tab kembali tepat ke baris yang terakhir berfokus (roving tabindex)", k.aktif === terakhirFokus && terakhirFokus !== null && k.tab0 === 1, { aktif: k.aktif, terakhirFokus });
  await foto(page, "D-papan-ketik");
  await s.tutup();
}

/* ------------------------------------------------ E penunjuk */
if (jalan("E")) {
  const s = await buka(); const page = s.page;
  const w = page.locator(".pb-wadah").first();
  const harap = barisHarap(PYTHON);
  const i = harap.findIndex((b) => !b.simpul.folder && b.simpul.kunci === "toko/uang.py");
  const url = page.url();
  await w.locator(".pb-baris").nth(i).click(); await tunggu(page, 80);
  const k = await keadaan(page);
  P.cek("E klik berkas memilihnya dan memindahkan fokus ke barisnya", k.aktif === labelBaris(harap[i], PYTHON.h.berkas) && k.dipilih[0] === k.aktif && k.jalur === "toko/uang.py", k);
  P.cek("E klik tidak menavigasi (alamat tetap)", page.url() === url);
  P.cek("E roving: sesudah klik, baris yang diklik jadi satu-satunya berperhentian Tab", k.tab0 === 1 && await page.evaluate((n) => document.querySelectorAll(".pb-baris")[n].tabIndex === 0, i));
  P.cek("E klik di panel kode tidak mengubah pilihan", await (async () => { await w.locator(".pb-isi pre.kode").click(); return (await keadaan(page)).jalur === "toko/uang.py"; })());
  await s.tutup();
}

/* ------------------------------------------------ F kontras */
if (jalan("F")) {
  for (const tema of ["gelap", "malam", "terang", "kontras"]) {
    const s = await buka({ tema }); const page = s.page;
    const teks = {
      baris: await ukur(page, '.pb-baris[aria-selected="false"]', "color"),
      folder: await ukur(page, ".pb-folder", "color"),
      terpilih: await ukur(page, '.pb-baris[aria-selected="true"]', "color"),
      jalur: await ukur(page, ".pb-jalur", "color"),
      folderJalur: await ukur(page, ".pb-jalur-folder", "color"),
      meta: await ukur(page, ".pb-meta", "color"),
    };
    const rendah = Object.entries(teks).filter(([, v]) => v === null || v < 4.5);
    P.cek(`F ${tema}: teks pohon dan kepala panel >= 4,5:1`, rendah.length === 0, teks);
    const penanda = { batas: await ukur(page, '.pb-baris[aria-selected="true"]', "borderLeftColor") };
    P.cek(`F ${tema}: garis penanda berkas terpilih >= 3:1 terhadap latarnya`, penanda.batas >= 3, penanda);
    const papan = { nama: await ukur(page, ".pb-berkas > svg", "color") };
    P.cek(`F ${tema}: ikon berkas terbaca (>= 3:1)`, papan.nama >= 3, papan);
    await foto(page, `F-${tema}`);
    await s.tutup();
  }
}

/* ------------------------------------------------ G tata letak */
if (jalan("G")) {
  for (const [lebar, tinggi, ukuranTeks] of [[1440, 900, null], [1280, 800, null], [1440, 900, "sangat besar"]]) {
    const s = await buka({ lebar, tinggi, ukuranTeks }); const page = s.page;
    const t = await page.evaluate(() => {
      const r = (sel) => { const b = document.querySelector(sel).getBoundingClientRect(); return { x: b.x, w: b.width, r: b.right, h: b.height }; };
      const blok = r(".blok-kode:has(.pb-wadah)"); const pohon = r(".pb-pohon"); const isi = r(".pb-isi");
      return { blok, pohon, isi, halaman: document.documentElement.scrollWidth, jendela: innerWidth, root: parseFloat(getComputedStyle(document.documentElement).fontSize) };
    });
    const nama = `${lebar}${ukuranTeks ? " huruf " + ukuranTeks : ""}`;
    P.cek(`G ${nama}: pohon dan panel di dalam blok, berdampingan`, t.pohon.x >= t.blok.x - 0.5 && t.isi.r <= t.blok.r + 0.5 && Math.abs(t.pohon.r - t.isi.x) <= 1.5, t);
    P.cek(`G ${nama}: lebar pohon 8 sampai 12rem, panel kode mendapat sisanya`, t.pohon.w >= 8 * t.root - 1 && t.pohon.w <= 12 * t.root + 1 && t.isi.w >= 300, { pohon: t.pohon.w, isi: t.isi.w, root: t.root });
    P.cek(`G ${nama}: halaman tidak meluber ke samping`, t.halaman <= t.jendela, { halaman: t.halaman, jendela: t.jendela });
    await foto(page, `G-${nama.replace(/ /g, "-")}`);
    await s.tutup();
  }
}

/* ------------------------------------------------ H kebersihan dan kontrol */
if (jalan("H")) {
  const s = await buka({ gerak: "penuh" }); const page = s.page;
  const k = await keadaan(page);
  const teks = await page.evaluate(() => document.querySelector(".blok-kode:has(.pb-wadah)").textContent);
  P.cek("H teks penampil tanpa undefined, NaN, [object Object], atau null", !/undefined|NaN|\[object Object\]|\bnull\b/.test(teks) && k.baris > 0);
  P.cek("H tanpa dash di teks yang dibuat penampil (nama pohon, kepala, kaki)", !POLA_DASH.test(await page.evaluate(() => [...document.querySelectorAll(".pb-nama, .pb-meta, .blok-kaki, .pb-baris")].map((e) => e.getAttribute("aria-label") ?? e.textContent).join(" "))));
  const kaki = await page.evaluate(() => document.querySelector(".blok-kode:has(.pb-wadah) .blok-kaki")?.textContent ?? "");
  P.cek("H kaki blok menjelaskan tombol Salin, bukan lagi 'pisahkan sesuai komentar penanda' (penandanya sudah tidak terlihat)", /Tombol Salin di atas membawa semua berkas sekaligus/.test(kaki) && !/komentar penanda di dalam kode/.test(kaki), kaki);
  P.cek("H lencana tetap 'beberapa berkas'", await page.evaluate(() => document.querySelector(".blok-kode:has(.pb-wadah) .lencana")?.textContent === "beberapa berkas"));
  P.cek("H tombol Salin utama (seluruh blok) tetap ada", await page.evaluate(() => [...document.querySelectorAll(".blok-kode:has(.pb-wadah) .blok-alat button")].some((b) => b.textContent === "Salin")));
  P.cek("H satu-satunya permintaan tulis yang ditolak adalah penanda materi dibaca", s.tulisDitolak.every((u) => /\/api\/materi\/selesai/.test(u)), s.tulisDitolak);
  P.cek("H tanpa galat konsol selain POST yang sengaja digagalkan harness", s.konsol.filter((x) => !/ERR_FAILED/.test(x)).length === 0, s.konsol);
  // Kontrol: blok yang BUKAN multi tidak berubah.
  await page.evaluate(() => { location.hash = "#/materi/python/0"; });
  await page.waitForFunction(() => document.querySelectorAll(".blok-kode pre.kode").length > 0 && document.querySelectorAll(".pb-wadah").length === 0, { timeout: 10000 });
  P.cek("H kontrol: materi tanpa blok multi tetap memakai blok kode biasa (tanpa penampil pohon)", true);
  await s.tutup();
}

/* ------------------------------------------------ J Salin berkas ini */
if (jalan("J")) {
  const s = await buka(); const page = s.page;
  await s.ctx.grantPermissions(["clipboard-read", "clipboard-write"], { origin: new URL(URL_DASAR).origin });
  const w = page.locator(".pb-wadah").first();
  const harap = barisHarap(PYTHON);
  const i = harap.findIndex((b) => !b.simpul.folder && b.simpul.kunci === "toko/uang.py");
  await w.locator(".pb-baris").nth(i).click();
  await w.getByRole("button", { name: "Salin berkas ini" }).click(); await tunggu(page, 200);
  const salinan = await page.evaluate(() => navigator.clipboard.readText());
  P.cek("J Salin berkas ini menyalin HANYA isi berkas yang dibuka", salinan === PYTHON.h.berkas.find((b) => b.nama === "toko/uang.py").isi, salinan.slice(0, 40));
  await foto(page, "J-salin");
  await s.tutup();
}

P.selesai();
