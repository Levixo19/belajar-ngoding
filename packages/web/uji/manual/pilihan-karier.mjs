/* Perilaku dropdown Perencana Peta Karier (komponen `Pilihan`, pengganti
 * `<select>` native). Yang dijanjikan: terbuka saat diklik cepat, TETAP terbuka
 * sampai ada yang memilih atau menutupnya, memilih cukup satu klik cepat tanpa
 * menahan tombol, papan ketik lengkap, dan tidak ada yang menutupnya diam-diam.
 * Dilaporkan pemilik: popup native menutup sendiri begitu klik dilepas dan baru
 * bertahan kalau tombol ditahan.
 *
 *   BELAJAR_URL=http://127.0.0.1:7975/ PLAYWRIGHT_MJS=... node uji/manual/pilihan-karier.mjs
 *   OUT=/jalur/folder  (opsional: simpan tangkapan layar)
 *
 * Jalankan terhadap server berprofil TERPISAH; menolak port 7777. Hanya GET dan
 * gerak mouse: memilih profesi tujuan mengganti alamat lewat `replaceState` dan
 * tidak menulis konfigurasi. CATATAN BATAS: Chrome headless tidak mengeluarkan
 * gejala Wayland yang dilaporkan, jadi skrip ini membuktikan bahwa daftar
 * buatan sendiri tidak punya jalur kegagalan itu, bukan bahwa gejalanya
 * direproduksi lalu hilang.
 */
import fs from "node:fs";
import path from "node:path";

const URL_DASAR = process.env.BELAJAR_URL ?? "";
let alamat = null; try { alamat = new URL(URL_DASAR); } catch { /* kosong */ }
if (!alamat || alamat.hostname !== "127.0.0.1" || alamat.port === "7777" || alamat.port === "") {
  console.error("MENOLAK: BELAJAR_URL harus http://127.0.0.1:<port uji>/, bukan 7777.");
  process.exit(2);
}
const OUT = process.env.OUT ?? "";
if (OUT) fs.mkdirSync(OUT, { recursive: true });
const pw = await import(process.env.PLAYWRIGHT_MJS ?? "playwright");
const chromium = pw.chromium ?? pw.default.chromium;
const browser = await chromium.launch({
  executablePath: process.env.CHROME ?? "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox"] });

let gagal = 0;
const periksa = (nama, ok, rinci = "") => {
  if (!ok) gagal += 1;
  console.log(`${ok ? "lulus " : "GAGAL "} ${nama}${rinci ? "  (" + String(rinci).slice(0, 170) + ")" : ""}`);
};

async function buka({ tema = "gelap", lebar = 1440, tinggi = 900, simulasi = null } = {}) {
  const ctx = await browser.newContext({ viewport: { width: lebar, height: tinggi } });
  // Gerak dibiarkan bawaan ("penuh"): reticle dan semua efek ikut jalan, seperti di pemakaian nyata.
  await ctx.addInitScript((t) => { try { localStorage.setItem("belajar.tema", JSON.stringify(t)); } catch { /* abaikan */ } }, tema);
  const page = await ctx.newPage();
  const galat = [];
  page.on("pageerror", (e) => galat.push(String(e).slice(0, 160)));
  page.on("console", (m) => { if (m.type() === "error") galat.push(m.text().slice(0, 160)); });
  if (simulasi) await simulasi(page);
  await page.goto(URL_DASAR + "#/karier");
  await page.waitForSelector("#kr-pilih-asal", { timeout: 15000 });
  await page.waitForTimeout(800);
  await page.locator(".kr-pilih-jalur").scrollIntoViewIfNeeded();
  await page.evaluate(() => window.scrollBy(0, 120));
  await page.waitForTimeout(250);
  return { page, galat };
}
const foto = async (page, nama) => { if (OUT) await page.screenshot({ path: path.join(OUT, nama + ".png") }); };
const api = (page, jalur) => page.evaluate(async (j) => {
  const r = await fetch("/api/" + j, { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR } });
  return r.json();
}, jalur);
const ASAL = "#kr-pilih-asal", TUJUAN = "#kr-pilih-tujuan";
const daftar = (page) => page.locator(".pil-daftar");
const nilai = (page, sel) => page.locator(sel + " .pil-nilai").textContent();
const terbuka = async (page) => (await daftar(page).count()) === 1;
/** Klik SEPERTI jari yang cepat: tekan dan lepas dalam 40 ms, tanpa menahan. */
async function klikCepat(page, sel) {
  const k = await page.locator(sel).boundingBox();
  await page.mouse.move(k.x + k.width / 2, k.y + k.height / 2, { steps: 3 });
  await page.mouse.down(); await page.waitForTimeout(40); await page.mouse.up();
}
const fokusId = (page) => page.evaluate(() => document.activeElement?.id ?? document.activeElement?.tagName);
const aktifTeks = (page) => page.locator(".pil-daftar li[data-aktif]").textContent().then((t) => t.trim()).catch(() => null);
const sehat = (galat, nama) => periksa(`${nama}: tanpa galat konsol`, galat.length === 0, galat[0]);

const kontrasDi = (page, sel, prop = "color") => page.evaluate(([sel, prop]) => {
  const el = document.querySelector(sel);
  if (!el) return null;
  // `color-mix` dilaporkan sebagai `color(srgb 0.9 0.9 0.8 / a)`, komponen 0 sampai 1.
  const angka = (s) => {
    const n = s.match(/-?\d*\.?\d+(?:e-?\d+)?/g).map(Number);
    return s.startsWith("color(") ? [...n.slice(0, 3).map((v) => v * 255), ...n.slice(3)] : n;
  };
  const campur = (atas, bawah, a) => atas.slice(0, 3).map((c, i) => c * a + bawah[i] * (1 - a));
  const lum = ([r, g, b]) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const lapis = [];
  for (let x = el; x; x = x.parentElement) {
    const m = angka(getComputedStyle(x).backgroundColor);
    const alfa = m.length === 4 ? m[3] : 1;
    if (alfa === 0) continue;
    lapis.push([m.slice(0, 3), alfa]);
    if (alfa === 1) break;
  }
  let dasar = [0, 0, 0];
  if (lapis.length && lapis[lapis.length - 1][1] === 1) dasar = lapis.pop()[0];
  while (lapis.length) { const [w, a] = lapis.pop(); dasar = campur(w, dasar, a); }
  let op = 1;
  for (let x = el; x && x !== document.documentElement; x = x.parentElement) op *= Number(getComputedStyle(x).opacity);
  const teks = angka(getComputedStyle(el)[prop]);
  const efektif = campur(teks, dasar, (teks.length === 4 ? teks[3] : 1) * op);
  const [a, b] = [lum(efektif), lum(dasar)].sort((x, y) => y - x);
  return +((a + 0.05) / (b + 0.05)).toFixed(2);
}, [sel, prop]);

/* ------------------------------------------------------------- A struktur */
{
  const { page, galat } = await buka();
  periksa("A tidak ada <select> native di Perencana", (await page.locator(".kr-pilih-jalur select").count()) === 0);
  periksa("A dua combobox bernama dari labelnya (Sekarang, Ingin menjadi)",
    (await page.getByRole("combobox", { name: "Sekarang" }).count()) === 1 && (await page.getByRole("combobox", { name: "Ingin menjadi" }).count()) === 1);
  periksa("A tertutup di awal (aria-expanded=false, tanpa daftar)",
    (await page.locator(ASAL).getAttribute("aria-expanded")) === "false" && !(await terbuka(page)));
  periksa("A klik pada teks label membuka dan memfokuskan combobox-nya (seperti select)", await (async () => {
    await page.locator('label[for="kr-pilih-asal"]').click(); await page.waitForTimeout(250);
    const ok = (await terbuka(page)) && (await fokusId(page)) === "kr-pilih-asal";
    await page.keyboard.press("Escape"); return ok; })());
  sehat(galat, "A");
  await page.context().close();
}

/* ------------------------------------- B klik cepat membuka dan TETAP terbuka */
{
  const { page, galat } = await buka();
  const n = (await api(page, "karier")).profesi.length;
  await klikCepat(page, ASAL);
  await page.waitForTimeout(150);
  periksa("B klik cepat (40 ms, tanpa menahan) membuka daftar", await terbuka(page));
  periksa("B daftar memuat semua profesi dari server", (await page.locator(".pil-daftar li").count()) === n, `n=${n}`);
  periksa("B aria-expanded=true dan aria-controls menunjuk daftarnya",
    (await page.locator(ASAL).getAttribute("aria-expanded")) === "true" &&
    (await page.locator(ASAL).getAttribute("aria-controls")) === (await daftar(page).getAttribute("id")));
  await page.waitForTimeout(1200);
  periksa("B tetap terbuka 1,2 detik sesudah klik dilepas (inti keluhan)", await terbuka(page));
  const k = await page.locator(".pil-daftar li").nth(3).boundingBox();
  await page.mouse.move(k.x + 30, k.y + 8, { steps: 6 }); await page.waitForTimeout(200);
  await page.mouse.move(k.x + 40, k.y + 60, { steps: 6 }); await page.waitForTimeout(600);
  periksa("B tetap terbuka saat penunjuk berkeliling di atas opsi", await terbuka(page));
  periksa("B sorotan mengikuti penunjuk (pointermove)", (await aktifTeks(page)) !== null);
  // Opsi yang separuh terpotong di tepi daftar: dulu efek "gulirkan opsi aktif ke
  // dalam" ikut jalan saat penunjuk melewatinya, menggeser isi daftar DI BAWAH
  // penunjuk, dan kliknya mengenai baris tetangga.
  const gulir = await page.evaluate(() => {
    const d = document.querySelector(".pil-daftar");
    const li = d.children[Math.min(9, d.children.length - 2)];
    d.scrollTop = li.offsetTop + 19;                   // separuh opsi ini terpotong di tepi atas
    const r = d.getBoundingClientRect();
    return { sebelum: d.scrollTop, x: r.left + 40, y: r.top + 9 };
  });
  await page.mouse.move(gulir.x + 6, gulir.y + 30, { steps: 3 });
  await page.mouse.move(gulir.x, gulir.y, { steps: 4 }); await page.waitForTimeout(400);
  const sesudah = await page.evaluate(() => document.querySelector(".pil-daftar").scrollTop);
  periksa("B penunjuk di atas opsi yang terpotong TIDAK menggulir daftar di bawahnya", Math.abs(sesudah - gulir.sebelum) < 0.5, `${gulir.sebelum} -> ${sesudah}`);
  await foto(page, "B-terbuka");
  await page.mouse.click(5, 5); await page.waitForTimeout(150);
  periksa("B klik di luar menutup", !(await terbuka(page)));
  // Jalur `blur` juga menutup saat klik di luar memindahkan fokus, jadi pemeriksaan di atas tidak
  // membuktikan penangan `pointerdown`. Peramban yang tidak memfokuskan tombol saat diklik (Safari,
  // Firefox di macOS) hanya punya penangan itu. Di sini fokus sengaja TIDAK berpindah.
  await klikCepat(page, ASAL); await page.waitForTimeout(150);
  await page.evaluate(() => document.body.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true })));
  await page.waitForTimeout(150);
  periksa("B pointerdown di luar menutup walau fokus tidak berpindah", !(await terbuka(page)) && (await fokusId(page)) === "kr-pilih-asal");
  sehat(galat, "B");
  await page.context().close();
}

/* ------------------------------ C memilih dengan SATU klik cepat, tanpa menahan */
{
  const { page, galat } = await buka();
  await klikCepat(page, ASAL);
  const opsiAnalis = page.locator(".pil-daftar li", { hasText: "Data Analyst" }).first();
  // Daftar terbuka tergulir ke opsi TERPILIH, jadi opsi lain bisa berada di luar
  // area yang terlihat; `boundingBox` tetap melaporkan posisinya. Orangnya
  // menggulir dulu, dan skrip ini juga (jangan mengklik titik di luar daftar).
  await opsiAnalis.scrollIntoViewIfNeeded();
  const kotak = await opsiAnalis.boundingBox();
  await page.mouse.move(kotak.x + 40, kotak.y + 8, { steps: 4 });
  await page.mouse.down(); await page.waitForTimeout(30); await page.mouse.up();   // klik cepat pada opsi
  await page.waitForTimeout(500);
  periksa("C satu klik cepat pada opsi memilihnya", (await nilai(page, ASAL)).trim() === "Data Analyst", await nilai(page, ASAL));
  periksa("C daftar menutup sesudah memilih (dan TIDAK terbuka lagi)", !(await terbuka(page)));
  periksa("C fokus tetap di combobox sesudah memilih", (await fokusId(page)) === "kr-pilih-asal", await fokusId(page));
  periksa("C jalur ikut berubah: langkah pertama = profesi asal yang dipilih",
    (await page.locator(".kr-langkah li").first().textContent()).includes("Data Analyst"));

  await klikCepat(page, TUJUAN);
  const opsiBe = page.locator(".pil-daftar li", { hasText: "Backend Developer" }).first();
  await opsiBe.scrollIntoViewIfNeeded();
  const kb = await opsiBe.boundingBox();
  await page.mouse.move(kb.x + 40, kb.y + 8, { steps: 4 });
  await page.mouse.down(); await page.waitForTimeout(30); await page.mouse.up();
  await page.waitForTimeout(600);
  periksa("C 'Ingin menjadi' memilih tujuan dengan satu klik cepat", (await nilai(page, TUJUAN)).trim() === "Backend Developer");
  periksa("C alamat dan panel profesi mengikuti tujuan",
    (await page.evaluate(() => location.hash)) === "#/karier/backend-developer" &&
    (await page.locator("#kr-panel").textContent()).includes("Backend Developer"));
  periksa("C langkah terakhir jalur = tujuan",
    (await page.locator(".kr-langkah li").last().textContent()).includes("Backend Developer"));
  sehat(galat, "C");
  await page.context().close();
}

/* ------------------------------------------------------- D menutup daftar */
{
  const { page, galat } = await buka();
  await klikCepat(page, ASAL); await page.waitForTimeout(150);
  await page.keyboard.press("Escape"); await page.waitForTimeout(150);
  periksa("D Escape menutup dan fokus tetap di combobox", !(await terbuka(page)) && (await fokusId(page)) === "kr-pilih-asal");
  await page.locator(ASAL).click(); await page.waitForTimeout(150);
  await page.locator(ASAL).click(); await page.waitForTimeout(150);
  periksa("D klik tombol saat terbuka menutupnya", !(await terbuka(page)));
  await page.locator(ASAL).click(); await page.waitForTimeout(150);
  const awal = (await nilai(page, ASAL)).trim();
  await page.keyboard.press("ArrowDown"); await page.waitForTimeout(80);
  await page.keyboard.press("Tab"); await page.waitForTimeout(250);
  periksa("D Tab menetapkan opsi aktif, menutup, dan meneruskan fokus",
    !(await terbuka(page)) && (await nilai(page, ASAL)).trim() !== awal && (await fokusId(page)) !== "kr-pilih-asal", `${awal} -> ${(await nilai(page, ASAL)).trim()}`);
  await page.locator(ASAL).click(); await page.waitForTimeout(150);
  await page.locator(TUJUAN).click(); await page.waitForTimeout(200);
  periksa("D membuka combobox lain menutup yang pertama", (await page.locator(".pil-daftar").count()) === 1 &&
    (await page.locator(TUJUAN).getAttribute("aria-expanded")) === "true" && (await page.locator(ASAL).getAttribute("aria-expanded")) === "false");
  sehat(galat, "D");
  await page.context().close();
}

/* ----------------------------------------------------------- E papan ketik */
{
  const { page, galat } = await buka();
  await page.locator(ASAL).focus();
  const dipilih = (await nilai(page, ASAL)).trim();
  await page.keyboard.press("ArrowDown"); await page.waitForTimeout(120);
  periksa("E ArrowDown membuka daftar dengan opsi terpilih yang aktif", (await terbuka(page)) && (await aktifTeks(page)) === dipilih, `${dipilih} / ${await aktifTeks(page)}`);
  const idAktif = await page.locator(".pil-daftar li[data-aktif]").getAttribute("id");
  periksa("E aria-activedescendant = opsi aktif", (await page.locator(ASAL).getAttribute("aria-activedescendant")) === idAktif);
  await page.keyboard.press("ArrowDown"); await page.keyboard.press("ArrowDown");
  const teks3 = await aktifTeks(page);
  await page.keyboard.press("Enter"); await page.waitForTimeout(250);
  periksa("E Enter memilih opsi aktif dan menutup", !(await terbuka(page)) && (await nilai(page, ASAL)).trim() === teks3, teks3);
  await page.keyboard.press("End"); await page.waitForTimeout(100);
  const akhir = await aktifTeks(page);
  const semua = await page.locator(".pil-daftar li").allTextContents();
  periksa("E End ke opsi terakhir, Home ke pertama", akhir === semua.at(-1).trim() && (await (async () => { await page.keyboard.press("Home"); return (await aktifTeks(page)) === semua[0].trim(); })()));
  await page.keyboard.press("Escape");
  await page.keyboard.type("dat", { delay: 40 }); await page.waitForTimeout(120);
  periksa("E mengetik 'dat' membuka dan melompat ke opsi berawalan itu", (await terbuka(page)) && /^dat/i.test((await aktifTeks(page)) ?? ""), await aktifTeks(page));
  await page.keyboard.press("Escape"); await page.waitForTimeout(900);
  await page.keyboard.press("d"); await page.waitForTimeout(80);
  const d1 = await aktifTeks(page);
  await page.waitForTimeout(900); await page.keyboard.press("d"); await page.waitForTimeout(80);
  const d2 = await aktifTeks(page);
  periksa("E huruf yang sama berulang menggilir opsi berawalan itu", /^d/i.test(d1 ?? "") && /^d/i.test(d2 ?? "") && d1 !== d2, `${d1} -> ${d2}`);
  await page.keyboard.press("Escape");
  await page.keyboard.press("Alt+ArrowDown"); await page.waitForTimeout(100);
  periksa("E Alt+ArrowDown membuka", await terbuka(page));
  sehat(galat, "E");
  await page.context().close();
}

/* --------------------------------------------------- F tanda yang terlihat */
{
  const { page } = await buka();
  await klikCepat(page, TUJUAN); await page.waitForTimeout(200);
  const s = await page.evaluate(() => {
    const li = [...document.querySelectorAll(".pil-daftar li")];
    return { terpilih: li.filter((x) => x.getAttribute("aria-selected") === "true").length,
      cek: li.filter((x) => x.querySelector("svg")).length, cekDiTerpilih: li.every((x) => (x.getAttribute("aria-selected") === "true") === !!x.querySelector("svg")),
      tebal: li.map((x) => Number(getComputedStyle(x).fontWeight)), jumlahAktif: li.filter((x) => x.hasAttribute("data-aktif")).length };
  });
  periksa("F tepat satu opsi aria-selected, dan hanya ia yang bercentang", s.terpilih === 1 && s.cek === 1 && s.cekDiTerpilih);
  periksa("F yang terpilih lebih tebal (bukan warna saja)", Math.max(...s.tebal) >= 600 && s.tebal.filter((t) => t >= 600).length === 1);
  periksa("F tepat satu opsi aktif (sorotan papan ketik atau penunjuk)", s.jumlahAktif === 1);
  const warna = await page.evaluate(() => [
    getComputedStyle([...document.querySelectorAll(".pil-daftar li")].find((x) => !x.hasAttribute("data-aktif"))).backgroundColor,
    getComputedStyle(document.querySelector(".pil-daftar li[data-aktif]")).backgroundColor]);
  periksa("F opsi aktif berlatar beda dari yang tidak", warna[0] !== warna[1], warna.join(" | "));
  await page.context().close();
}

/* -------------------- G tidak ada pemicu non-klik yang menutup (beda dari native) */
{
  const { page, galat } = await buka();
  await klikCepat(page, ASAL); await page.waitForTimeout(200);
  const hasil = [];
  await page.evaluate(() => { const n = document.querySelector(".kr-simpul"); n.dispatchEvent(new PointerEvent("pointerover", { bubbles: true, pointerType: "mouse" })); });
  await page.waitForTimeout(250); hasil.push(["render ulang (hover peta)", await terbuka(page)]);
  await page.evaluate(() => window.scrollBy(0, 4)); await page.waitForTimeout(200); hasil.push(["gulir kecil", await terbuka(page)]);
  await page.evaluate(() => document.dispatchEvent(new Event("progres-berubah"))); await page.waitForTimeout(500); hasil.push(["progres-berubah", await terbuka(page)]);
  await page.evaluate(() => { for (let i = 0; i < 5; i++) document.dispatchEvent(new PointerEvent("pointermove", { bubbles: true, clientX: 200 + i * 15, clientY: 300, pointerType: "mouse" })); }); await page.waitForTimeout(300); hasil.push(["pointermove dokumen (reticle)", await terbuka(page)]);
  await page.setViewportSize({ width: 1430, height: 900 }); await page.waitForTimeout(400); hasil.push(["ubah ukuran jendela", await terbuka(page)]);
  periksa("G daftar bertahan melewati render ulang, gulir, progres, pointer, dan ubah ukuran", hasil.every(([, ok]) => ok), JSON.stringify(hasil.filter(([, ok]) => !ok)));
  // Daftar `position: fixed` tidak ikut halaman. Tanpa pendengar gulir ia tertinggal di layar
  // sementara tombolnya bergeser, dan G di atas tetap hijau karena hanya bertanya "masih terbuka?".
  const sebelumGulir = await page.evaluate(() => scrollY);
  await page.evaluate(() => window.scrollBy(0, 60)); await page.waitForTimeout(250);
  const ikut = await page.evaluate(() => {
    const l = document.querySelector(".pil-daftar").getBoundingClientRect(), t = document.getElementById("kr-pilih-asal").getBoundingClientRect();
    const naik = document.querySelector(".pil-daftar[data-atas]") !== null;
    return { jarak: naik ? t.top - l.bottom : l.top - t.bottom, y: scrollY };
  });
  periksa("G2 daftar mengikuti tombol saat halaman digulir 60 px", ikut.y - sebelumGulir >= 30 && Math.abs(ikut.jarak - 4) <= 1.5,
    JSON.stringify({ geserHalaman: ikut.y - sebelumGulir, jarakKeTombol: Math.round(ikut.jarak) }));
  sehat(galat, "G");
  await page.context().close();
}

/* ------------------------------------------- H dekat tepi bawah: naik, tetap terlihat */
{
  const { page } = await buka({ tinggi: 520 });
  await page.evaluate(() => { const k = document.getElementById("kr-pilih-asal").getBoundingClientRect(); window.scrollBy(0, k.top - 400); });
  await page.waitForTimeout(250);
  await klikCepat(page, ASAL); await page.waitForTimeout(250);
  const m = await page.evaluate(() => { const l = document.querySelector(".pil-daftar").getBoundingClientRect(), t = document.getElementById("kr-pilih-asal").getBoundingClientRect(); return { atas: l.top, bawah: l.bottom, tombolAtas: t.top, naik: document.querySelector(".pil-daftar[data-atas]") !== null }; });
  periksa("H di dekat tepi bawah daftar naik dan seluruhnya terlihat", m.naik && m.atas >= 0 && m.bawah <= m.tombolAtas + 1, JSON.stringify({ atas: m.atas | 0, bawah: m.bawah | 0, tombol: m.tombolAtas | 0 }));
  await page.context().close();
}

/* ---------------------------------------------------- I kontras empat tema */
for (const tema of ["gelap", "malam", "terang", "kontras"]) {
  const { page } = await buka({ tema });
  await klikCepat(page, TUJUAN); await page.waitForTimeout(200);
  await page.keyboard.press("ArrowDown"); await page.waitForTimeout(100);
  const ukur = {
    pemicu: await kontrasDi(page, "#kr-pilih-tujuan .pil-nilai"),
    label: await kontrasDi(page, 'label[for="kr-pilih-tujuan"]'),
    panah: await kontrasDi(page, "#kr-pilih-tujuan .pil-panah"),
    opsi: await kontrasDi(page, ".pil-daftar li:not([data-aktif]):not([aria-selected='true'])"),
    aktif: await kontrasDi(page, ".pil-daftar li[data-aktif]"),
    terpilih: await kontrasDi(page, ".pil-daftar li[aria-selected='true']"),
    centang: await kontrasDi(page, ".pil-daftar li[aria-selected='true'] svg"),
  };
  const rendah = Object.entries(ukur).filter(([k, v]) => v === null || v < (k === "centang" || k === "panah" ? 3 : 4.5));
  periksa(`I ${tema}: teks >= 4,5:1 (centang dan panah >= 3:1)`, rendah.length === 0, JSON.stringify(ukur));
  await foto(page, `I-${tema}`);
  await page.context().close();
}

/* -------------------------------------------------------------- J teks sehat */
{
  const { page } = await buka();
  await klikCepat(page, ASAL); await page.waitForTimeout(200);
  periksa("J tanpa teks undefined, NaN, [object Object], null di Perencana",
    !/undefined|NaN|\[object Object\]|\bnull\b/.test(await page.locator(".kr-pilih-jalur").textContent()));
  await page.context().close();
}

await browser.close();
console.log(gagal === 0 ? "\nSEMUA PEMERIKSAAN LULUS" : `\n${gagal} PEMERIKSAAN GAGAL`);
process.exit(gagal === 0 ? 0 : 1);
