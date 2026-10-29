/* Alur data belajar dari ujung ke ujung: Reset SEMUA, Reset satu bahasa, dan
 * Impor progres, lewat dialognya, dengan HASIL di berkas progres diperiksa.
 *
 *   BELAJAR_URL=http://127.0.0.1:7843/ BELAJAR_PROGRESS_FILE=$S/p.json \
 *   PLAYWRIGHT_MJS=... node uji/manual/data-dialog.mjs
 *
 * Skrip ini MENULIS (reset, impor), jadi ia menolak jalan kecuali menunjuk
 * server berprofil TERPISAH: bukan port 7777, bukan berkas progres di rumah.
 * Profilnya wajib sudah berisi progres (xp > 0); skrip memulihkannya sendiri
 * antar skenario dari salinan yang diambil di awal.
 *
 * Kenapa ada: dialog yang isiannya dibaca lewat `ref` SESUDAH ditutup selalu
 * mendapat null, dan itu merusak Reset SEMUA dan Impor tanpa satu galat pun.
 * tsc dan golden tidak melihatnya; hanya mengklik dialognya yang melihat.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const URL_DASAR = process.env.BELAJAR_URL ?? "";
const BERKAS = process.env.BELAJAR_PROGRESS_FILE ?? "";
const u = URL_DASAR ? new URL(URL_DASAR) : null;
if (!u || u.hostname !== "127.0.0.1" || u.port === "7777" || u.port === "") {
  console.error("MENOLAK: BELAJAR_URL harus http://127.0.0.1:<port uji>/, bukan 7777.");
  process.exit(2);
}
const rumah = path.join(os.homedir(), ".belajar_ngoding_progress.json");
if (!BERKAS || path.resolve(BERKAS) === rumah || path.dirname(path.resolve(BERKAS)) === os.homedir()) {
  console.error("MENOLAK: BELAJAR_PROGRESS_FILE harus berkas profil UJI, bukan milik pelajar.");
  process.exit(2);
}

const baca = () => JSON.parse(fs.readFileSync(BERKAS, "utf8"));
const seed = baca();
if (!(seed.xp > 0) || !(seed.materi_dibaca?.length > 0)) {
  console.error("Profil uji kosong. Isi dulu progresnya (xp > 0, satu materi dibaca).");
  process.exit(2);
}
const pulihkan = () => fs.writeFileSync(BERKAS, JSON.stringify(seed));
const berkasImpor = path.join(path.dirname(path.resolve(BERKAS)), "impor-seed.json");
fs.writeFileSync(berkasImpor, JSON.stringify(seed));

const pw = await import(process.env.PLAYWRIGHT_MJS ?? "playwright");
const chromium = pw.chromium ?? pw.default.chromium;
const browser = await chromium.launch({
  executablePath: process.env.CHROME ?? "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox"] });

let gagal = 0;
function periksa(nama, ok, rinci = "") {
  if (!ok) gagal += 1;
  console.log(`${ok ? "lulus " : "GAGAL "} ${nama}${rinci ? "  (" + rinci + ")" : ""}`);
}

async function buka() {
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  const tulis = [], galat = [];
  page.on("request", (r) => { if (r.method() !== "GET") tulis.push(r.url().replace(URL_DASAR, "/")); });
  page.on("pageerror", (e) => galat.push(String(e).slice(0, 200)));
  page.on("console", (m) => { if (m.type() === "error") galat.push(m.text().slice(0, 200)); });
  const respons = new Map();
  page.on("response", async (r) => {
    if (r.request().method() === "POST") {
      try { respons.set(new globalThis.URL(r.url()).pathname, { status: r.status(), badan: await r.json() }); } catch { /* bukan JSON */ }
    }
  });
  await page.goto(URL_DASAR + "#/atur");
  await page.waitForSelector("text=Reset SEMUA progres", { timeout: 20000 });
  await page.waitForTimeout(500);
  return { page, tulis, galat, respons };
}
const tombolJendela = (page, teks) => page.locator(".jendela-kaki button", { hasText: teks });
const toast = (page) => page.evaluate(() => document.body.innerText);

async function resetSemua(page, kata) {
  await page.locator("button", { hasText: "Reset SEMUA progres" }).click();
  await page.waitForSelector(".jendela");
  await tombolJendela(page, /^Lanjut$/).click();
  const kotak = page.locator('input[aria-label="Ketik HAPUS untuk mengonfirmasi"]');
  await kotak.waitFor();
  await kotak.fill(kata);
  await tombolJendela(page, "Hapus semuanya").click();
  await page.waitForTimeout(2600);
}

// A. kata salah: tidak ada yang dihapus
pulihkan();
{
  const { page, tulis, galat } = await buka();
  await resetSemua(page, "SALAH");
  periksa("A reset semua, kata salah: tanpa permintaan tulis", tulis.length === 0, tulis.join(","));
  periksa("A reset semua, kata salah: pesan penolakan", /tidak cocok/i.test(await toast(page)));
  periksa("A reset semua, kata salah: progres utuh", baca().xp === seed.xp);
  periksa("A tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// B. kata benar: terhapus, dengan cadangan
pulihkan();
{
  const { page, tulis, galat, respons } = await buka();
  await resetSemua(page, "HAPUS");
  const r = respons.get("/api/data/reset");
  periksa("B reset semua, HAPUS: satu POST /api/data/reset 200", tulis.length === 1 && r?.status === 200, tulis.join(","));
  periksa("B reset semua: xp 0 dan materi kosong", baca().xp === 0 && (baca().materi_dibaca ?? []).length === 0, `xp=${baca().xp}`);
  const cad = r?.badan?.cadangan;
  periksa("B reset semua: cadangan ada di disk", Boolean(cad) && fs.existsSync(cad), String(cad));
  // `.bak` bergulir ditimpa setiap penyimpanan; salinan bertanggal tidak boleh.
  // Membuka sebuah materi menulis progres ("sebagian"), persis yang dilakukan
  // pelajar sesudah reset.
  await page.goto(URL_DASAR + "#/materi/python/0");
  await page.waitForTimeout(2500);
  let xpSalinan = null;
  try { xpSalinan = JSON.parse(fs.readFileSync(cad, "utf8")).xp; } catch { /* hilang */ }
  periksa("B reset semua: salinan bertanggal bertahan sesudah progres ditulis lagi",
    /\.cadangan-/.test(String(cad)) && xpSalinan === seed.xp, `xp salinan=${xpSalinan}, seed=${seed.xp}`);
  periksa("B tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// C. impor tanpa berkas: pesan, tanpa permintaan
{
  const { page, tulis } = await buka();
  await page.locator("button", { hasText: "Impor progres" }).click();
  await page.waitForSelector(".jendela");
  await tombolJendela(page, /^Impor$/).click();
  await page.waitForTimeout(600);
  periksa("C impor tanpa berkas: pesan jelas", /Pilih berkas progres/i.test(await toast(page)));
  periksa("C impor tanpa berkas: tanpa permintaan tulis", tulis.length === 0, tulis.join(","));
  await page.close();
}

// D. impor dengan berkas: progres kembali
{
  const { page, tulis, respons, galat } = await buka();
  await page.locator("button", { hasText: "Impor progres" }).click();
  await page.waitForSelector(".jendela");
  await page.locator('input[aria-label="Berkas progres untuk diimpor"]').setInputFiles(berkasImpor);
  await tombolJendela(page, /^Impor$/).click();
  await page.waitForTimeout(2200);
  const r = respons.get("/api/data/impor");
  periksa("D impor: POST /api/data/impor 200", tulis.length === 1 && r?.status === 200, `${tulis.join(",")} ${r?.status}`);
  periksa("D impor: progres kembali (xp dan materi)", baca().xp === seed.xp && baca().materi_dibaca.length === seed.materi_dibaca.length, `xp=${baca().xp}`);
  periksa("D tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// E. reset satu bahasa
pulihkan();
{
  const { page, tulis, respons, galat } = await buka();
  // Pilihan buatan sendiri (`Pilihan.tsx`), bukan <select>: buka daftarnya lalu klik opsinya.
  await page.locator('button[aria-label="Bahasa yang direset"]').click();
  await page.locator(".pil-daftar li", { hasText: /^Python/ }).first().click();
  await page.locator("button", { hasText: "Reset satu bahasa" }).click();
  await page.waitForSelector(".jendela");
  await tombolJendela(page, /^Hapus progres/).click();
  await page.waitForTimeout(2200);
  const r = respons.get("/api/data/reset");
  periksa("E reset satu bahasa: POST 200", tulis.length === 1 && r?.status === 200, `${tulis.join(",")} ${r?.status}`);
  periksa("E reset satu bahasa: materi python hilang", !(baca().materi_dibaca ?? []).some((k) => String(k).startsWith("python_materi")));
  periksa("E tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// F. pulihkan dari salinan: reset dulu (membuat salinan pra-reset), lalu pilih
// salinan itu di dialog dan periksa HASILNYA di berkas progres.
pulihkan();
{
  const awal = await buka();
  await resetSemua(awal.page, "HAPUS");
  await awal.page.close();
  const { page, tulis, respons, galat } = await buka();
  periksa("F sebelum pulih: progres memang kosong", baca().xp === 0, `xp=${baca().xp}`);
  await page.locator("button", { hasText: "Pulihkan dari salinan" }).click();
  await page.waitForSelector(".jendela");
  const terpilih = await page.locator('button[aria-label="Salinan progres yang dipulihkan"] .pil-nilai').textContent();
  periksa("F dialog: salinan terbaru terpilih, menyebut tanggal dan XP-nya",
    new RegExp(`\\d{4}, \\d{2}[.:]\\d{2} · ${seed.xp} XP · \\d+ materi dibaca`).test(terpilih), terpilih);
  periksa("F dialog: fokus ada di dalam dialog",
    await page.evaluate(() => Boolean(document.activeElement?.closest(".jendela"))));
  await tombolJendela(page, /^Pulihkan$/).click();
  await page.waitForTimeout(2200);
  const r = respons.get("/api/data/impor");
  periksa("F pulihkan: satu POST /api/data/impor 200", tulis.length === 1 && r?.status === 200, `${tulis.join(",")} ${r?.status}`);
  periksa("F pulihkan: progres kembali (xp dan materi)",
    baca().xp === seed.xp && baca().materi_dibaca.length === seed.materi_dibaca.length, `xp=${baca().xp}`);
  const sebelum = r?.badan?.cadangan;
  let xpSebelum = null;
  try { xpSebelum = JSON.parse(fs.readFileSync(sebelum, "utf8")).xp; } catch { /* hilang */ }
  periksa("F pulihkan: keadaan sebelumnya (kosong) tersimpan sebagai salinan baru", xpSebelum === 0, String(sebelum));
  periksa("F tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// F2. salinan rusak: tidak ditawarkan di pilihan, tetapi disebut di dialog.
{
  const folder = path.dirname(path.resolve(BERKAS));
  fs.writeFileSync(path.join(folder, path.basename(BERKAS) + ".cadangan-29990101-000000"), "{rusak");
  const { page, galat } = await buka();
  await page.locator("button", { hasText: "Pulihkan dari salinan" }).click();
  await page.waitForSelector(".jendela");
  const teks = await page.locator(".jendela").first().innerText();
  periksa("F2 salinan rusak: disebut di dialog", /1 salinan lain tidak bisa dibaca/.test(teks), teks.replace(/\n/g, " ").slice(0, 220));
  await page.locator('button[aria-label="Salinan progres yang dipulihkan"]').click();
  await page.waitForSelector(".pil-daftar");
  periksa("F2 salinan rusak: tidak ada di pilihan",
    (await page.locator(".pil-daftar li").count()) >= 1 && !/tidak bisa dibaca/.test(await page.locator(".pil-daftar").innerText()));
  // Daftar di dalam dialog: tidak terpotong `.jendela { overflow: hidden }` dan Escape hanya menutup daftarnya.
  const dalam = await page.evaluate(() => { const l = document.querySelector(".pil-daftar").getBoundingClientRect();
    const e = document.elementFromPoint(l.left + l.width / 2, l.top + Math.min(20, l.height / 2));
    return { terlihat: !!e && !!e.closest(".pil-daftar"), induk: document.querySelector(".pil-daftar").parentElement.id };
  });
  periksa("F2 daftar Pilihan di dalam dialog terlihat (tidak terpotong) dan hidup di #tirai", dalam.terlihat && dalam.induk === "tirai", JSON.stringify(dalam));
  await page.keyboard.press("Escape"); await page.waitForTimeout(250);
  periksa("F2 Escape pada daftar yang terbuka hanya menutup daftarnya, dialog tetap",
    (await page.locator(".pil-daftar").count()) === 0 && (await page.locator(".jendela").count()) === 1);
  periksa("F2 tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

// G. tanpa salinan: pesan yang jelas, tanpa dialog, tanpa permintaan tulis.
// Yang dihapus HANYA salinan bernama persis di folder profil uji ini.
{
  const folder = path.dirname(path.resolve(BERKAS));
  const dasar = path.basename(BERKAS);
  const pola = new RegExp("^" + dasar.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\.cadangan-\\d{8}-\\d{6}(-\\d+)?$");
  for (const n of fs.readdirSync(folder)) if (pola.test(n)) fs.unlinkSync(path.join(folder, n));
  const { page, tulis, galat } = await buka();
  await page.locator("button", { hasText: "Pulihkan dari salinan" }).click();
  await page.waitForTimeout(800);
  periksa("G tanpa salinan: pesan jelas dan tidak ada dialog",
    /Belum ada salinan progres/i.test(await toast(page)) && (await page.locator(".jendela").count()) === 0);
  periksa("G tanpa salinan: tanpa permintaan tulis", tulis.length === 0, tulis.join(","));
  periksa("G tanpa galat konsol", galat.length === 0, galat[0]);
  await page.close();
}

pulihkan();
await browser.close();
console.log(gagal ? `GAGAL: ${gagal} pemeriksaan` : "SEMUA pemeriksaan lulus");
process.exit(gagal ? 1 : 0);
