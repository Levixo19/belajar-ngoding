/* Sapuan kontrol lintas layar: dialog modal, kotak angka dan tema Pengaturan,
 * panel "Lainnya", fokus Pustaka, tombol Peta Karier, penanda terkunci di
 * Palet, dan lencana XP yang ikut naik. Semuanya cacat yang lolos tsc, golden,
 * dan tes sumber, dan hanya ketahuan dengan mengklik.
 *
 *   BELAJAR_URL=http://127.0.0.1:7844/ BELAJAR_PROGRESS_FILE=$S/p.json \
 *   BELAJAR_CONFIG_FILE=$S/k.json PLAYWRIGHT_MJS=... \
 *   node uji/manual/sapuan-kontrol.mjs
 *
 * MENULIS (setelan, tandai selesai), jadi menolak jalan kecuali menunjuk
 * server berprofil TERPISAH: bukan port 7777, bukan berkas di rumah. Profil
 * wajib sudah berisi progres (xp > 0, materi Python dibaca berurutan dari
 * nol, tetap di Bab 1) dan `buka_semua_bab` MATI. Pemeriksaan G menandai SATU
 * materi lagi selesai, jadi semai profil dari awal tiap kali skrip dijalankan.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const URL_DASAR = process.env.BELAJAR_URL ?? "";
const BERKAS = process.env.BELAJAR_PROGRESS_FILE ?? "";
const KONFIG = process.env.BELAJAR_CONFIG_FILE ?? "";
const u = URL_DASAR ? new URL(URL_DASAR) : null;
if (!u || u.hostname !== "127.0.0.1" || u.port === "7777" || u.port === "") {
  console.error("MENOLAK: BELAJAR_URL harus http://127.0.0.1:<port uji>/, bukan 7777.");
  process.exit(2);
}
for (const [nama, jalur] of [["BELAJAR_PROGRESS_FILE", BERKAS], ["BELAJAR_CONFIG_FILE", KONFIG]]) {
  if (!jalur || path.dirname(path.resolve(jalur)) === os.homedir()) {
    console.error(`MENOLAK: ${nama} harus berkas profil UJI, bukan milik pelajar.`);
    process.exit(2);
  }
}
const progres = () => JSON.parse(fs.readFileSync(BERKAS, "utf8"));
const konfig = () => JSON.parse(fs.readFileSync(KONFIG, "utf8"));
if (!(progres().xp > 0)) { console.error("Profil uji kosong (xp harus > 0)."); process.exit(2); }

const pw = await import(process.env.PLAYWRIGHT_MJS ?? "playwright");
const chromium = pw.chromium ?? pw.default.chromium;
const browser = await chromium.launch({
  executablePath: process.env.CHROME ?? "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox"] });
let gagal = 0;
const periksa = (nama, ok, rinci = "") => {
  if (!ok) gagal += 1;
  console.log(`${ok ? "lulus " : "GAGAL "} ${nama}${rinci ? "  (" + rinci + ")" : ""}`);
};
async function buka(hash) {
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  const tulis = [], galat = [];
  page.on("request", (r) => { if (r.method() !== "GET") tulis.push(r.url().replace(URL_DASAR, "/")); });
  page.on("pageerror", (e) => galat.push(String(e).slice(0, 160)));
  page.on("console", (m) => { if (m.type() === "error") galat.push(m.text().slice(0, 160)); });
  await page.goto(URL_DASAR + hash);
  await page.waitForSelector("#panggung, #layar, main, header", { timeout: 20000 });
  await page.waitForTimeout(900);
  return { page, tulis, galat };
}
const fokusDi = (page) => page.evaluate(() => {
  const a = document.activeElement;
  return a ? (a.tagName + (a.getAttribute("aria-label") ? "[" + a.getAttribute("aria-label") + "]" : "")) : "null";
});
const modal = (page) => page.evaluate(() => {
  const t = document.querySelector("#tirai"), j = document.querySelector("#tirai .jendela");
  if (!t || !j) return null;
  const k = j.getBoundingClientRect();
  return { posisiTirai: getComputedStyle(t).position, kiri: Math.round(k.left), lebar: Math.round(k.width),
           tengah: Math.abs((k.left + k.width / 2) - innerWidth / 2) < 40 };
});

// A. Bantuan (?) dan Palet (Ctrl+K) adalah modal sungguhan
{
  const { page, galat } = await buka("#/");
  // Fokus ditaruh di elemen nyata lebih dulu: dari <body> fokus memang kembali
  // ke <body>, dan itu tidak membuktikan apa pun.
  await page.locator("#rel-utama a").first().focus();
  const asalFokus = await fokusDi(page);
  await page.keyboard.press("?");
  await page.waitForSelector("#tirai .jendela");
  const m = await modal(page);
  periksa("A Bantuan: tirai fixed dan kotak di tengah", m?.posisiTirai === "fixed" && m.tengah, JSON.stringify(m));
  periksa("A Bantuan: fokus di dalam dialog", (await fokusDi(page)).length > 0 && await page.evaluate(() => !!document.activeElement?.closest(".jendela")));
  await page.keyboard.press("Escape");
  await page.waitForTimeout(300);
  periksa("A Bantuan: Esc menutup", (await modal(page)) === null);
  periksa("A Bantuan: fokus kembali ke pemicunya", (await fokusDi(page)) === asalFokus && asalFokus !== "BODY",
    `${asalFokus} -> ${await fokusDi(page)}`);
  await page.keyboard.press("Control+k");
  await page.waitForSelector("#tirai .jendela");
  const p = await modal(page);
  periksa("A Palet: tirai fixed dan kotak di tengah", p?.posisiTirai === "fixed" && p.tengah, JSON.stringify(p));
  await page.keyboard.press("Escape");
  await page.waitForTimeout(300);
  periksa("A Palet: Esc menutup", (await modal(page)) === null);
  periksa("A tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// B. Pengaturan: kotak angka, tema
{
  const { page, tulis, galat } = await buka("#/atur");
  const kotak = page.locator(".medan", { hasText: "Target XP harian" }).locator("input");
  await kotak.fill("5000");
  await kotak.press("Enter");
  await page.waitForTimeout(900);
  periksa("B angka: Enter menyimpan, server menjepit ke 1000", konfig().target_xp_harian === 1000, String(konfig().target_xp_harian));
  periksa("B angka: kotak menampilkan nilai yang tersimpan", (await kotak.inputValue()) === "1000", await kotak.inputValue());
  const sebelum = tulis.length;
  await kotak.fill("");
  await kotak.blur();
  await page.waitForTimeout(500);
  periksa("B angka: kotak kosong tidak dikirim", tulis.length === sebelum && (await kotak.inputValue()) === "1000", `${tulis.length - sebelum} permintaan`);
  periksa("B angka: target tetap 1000", konfig().target_xp_harian === 1000);
  const temaKini = () => page.evaluate(() => ({
    html: document.documentElement.dataset.tema,
    kartu: [...document.querySelectorAll('button[aria-pressed="true"]')].map((b) => b.textContent.trim().slice(0, 20)).join("|") }));
  const t0 = await temaKini();
  await page.keyboard.press("Control+j");
  await page.waitForTimeout(500);
  const t1 = await temaKini();
  periksa("B tema: Ctrl+J mengganti tema", t0.html !== t1.html, `${t0.html} -> ${t1.html}`);
  periksa("B tema: kartu di Pengaturan ikut berubah", t0.kartu !== t1.kartu, `${t0.kartu} -> ${t1.kartu}`);
  periksa("B tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// C. Panel "Lainnya" menutup saat klik di luar
{
  const { page } = await buka("#/");
  await page.locator(".rel-pemicu").click();
  await page.waitForTimeout(300);
  const buka1 = await page.evaluate(() => document.querySelector(".rel-turun")?.classList.contains("buka"));
  await page.mouse.click(700, 600);
  await page.waitForTimeout(300);
  const buka2 = await page.evaluate(() => document.querySelector(".rel-turun")?.classList.contains("buka"));
  periksa("C panel Lainnya: terbuka lalu menutup saat klik di luar", buka1 === true && buka2 === false, `${buka1} -> ${buka2}`);
  await page.close();
}

// D. Pustaka: fokus ke kotak cari dan bertahan sesudah mencari
{
  const { page } = await buka("#/pustaka");
  await page.waitForSelector('input[aria-label="Cari di Pustaka"]');
  await page.waitForTimeout(500);
  periksa("D Pustaka: fokus awal di kotak cari", (await fokusDi(page)).includes("Cari di Pustaka"), await fokusDi(page));
  await page.keyboard.type("python");
  await page.keyboard.press("Enter");
  await page.waitForTimeout(1200);
  periksa("D Pustaka: fokus bertahan sesudah mencari", (await fokusDi(page)).includes("Cari di Pustaka"), await fokusDi(page));
  await page.close();
}

// E. Peta Karier: "Cari yang cocok" menggulir, tidak mengganti rute
{
  const { page } = await buka("#/karier");
  await page.waitForSelector("text=Cari yang cocok");
  await page.locator("button", { hasText: "Cari yang cocok" }).click();
  await page.waitForTimeout(700);
  const r = await page.evaluate(() => ({ hash: location.hash, atas: Math.round(document.getElementById("kr-cocok")?.getBoundingClientRect().top ?? -1), h1: document.querySelector("h1")?.textContent?.slice(0, 30) }));
  periksa("E Karier: rute tetap #/karier", r.hash === "#/karier", r.hash);
  periksa("E Karier: bagian kuis tergulir ke layar", r.atas >= 0 && r.atas < 400, `top=${r.atas}`);
  await page.close();
}

// F. Palet menandai hasil terkunci sebelum dipilih
{
  const { page } = await buka("#/");
  await page.keyboard.press("Control+k");
  await page.waitForSelector("#tirai .jendela");
  await page.keyboard.type("pointer");
  await page.waitForTimeout(1500);
  const n = await page.evaluate(() => document.querySelectorAll("#tirai .pil-kunci").length);
  periksa("F Palet: ada hasil bertanda terkunci", n > 0, `${n} penanda`);
  await page.close();
}

// G. Lencana XP naik tanpa pindah rute
{
  const { page, galat } = await buka("#/materi/python/" + progres().materi_dibaca.length);
  await page.waitForSelector("text=Tandai selesai");
  const lencana = () => page.evaluate(() => [...document.querySelectorAll(".tanda-angka")].map((e) => e.textContent.trim()));
  const sebelum = (await lencana()).at(-1);
  await page.locator("button", { hasText: "Tandai selesai" }).first().click();
  await page.waitForTimeout(1800);
  const sesudah = (await lencana()).at(-1);
  periksa("G lencana XP: naik tanpa pindah rute dan sama dengan berkas",
    sesudah !== sebelum && Number(sesudah) === progres().xp, `${sebelum} -> ${sesudah}, berkas ${progres().xp}`);
  periksa("G tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

await browser.close();
console.log(gagal ? `GAGAL: ${gagal} pemeriksaan` : "SEMUA pemeriksaan lulus");
process.exit(gagal ? 1 : 0);
