/* Kontras TERENDER layar Langit (komposit alfa dan antialias ikut): pasangan
 * tangkapan A (utuh) dan B (satu kelompok elemen disembunyikan), dianalisis
 * `kontras.py` (butuh numpy dan Pillow; BUKAN bagian suite).
 *
 *   BELAJAR_URL=... OUT=/jalur/pendek node uji/manual/kontras.mjs <etiket> <tema> <lebar> <tinggi> [ikhtisar|lensa:<key>]
 *   python3 uji/manual/kontras.py $OUT/<awalan>   (awalan dicetak oleh langkah pertama)
 *
 * Env: PROFIL=nyata|campur|semua, LINTASAN=selesai,baru,... , EKSTRA_CSS.
 */
import fs from "node:fs";
import { mulai } from "./lib.mjs";
const OUT = process.env.OUT ?? "/tmp/langit-kontras";
fs.mkdirSync(OUT, { recursive: true });
const [etiket, tema, wS, hS, mode = "ikhtisar"] = process.argv.slice(2);
const port = "url", w = +wS, h = +hS;
const IK = { akar: ".lt-ikhtisar", lintasan: [
  { nama: "selesai", hide: ".lt-ik-svg .lt-gl-selesai", tipe: "glif" },
  { nama: "sebagian", hide: ".lt-ik-svg .lt-gl-sebagian", tipe: "glif" },
  { nama: "baru", hide: ".lt-ik-svg .lt-gl-baru", tipe: "glif" },
  { nama: "terkunci", hide: ".lt-ik-svg .lt-gl-terkunci", tipe: "glif" },
  { nama: "garis", hide: ".lt-ik-svg .lt-ik-garis", tipe: "garis" },
  { nama: "teks-nama", hide: ".lt-nama-teks", rect: ".lt-nama-teks", tipe: "teks" },
  { nama: "teks-angka", hide: ".lt-nama-prog b", rect: ".lt-nama-prog b", tipe: "teks" },
  { nama: "teks-keluarga", hide: ".lt-keluarga h2", rect: ".lt-keluarga h2", tipe: "teks" },
  { nama: "teks-ket", hide: ".lt-keluarga p", rect: ".lt-keluarga p", tipe: "teks" },
] };
const LN = { akar: ".lt-lensa-kanvas", lintasan: [
  { nama: "selesai", hide: ".lt-ln-svg .lt-gl-selesai", tipe: "glif" },
  { nama: "sebagian", hide: ".lt-ln-svg .lt-gl-sebagian", tipe: "glif" },
  { nama: "baru", hide: ".lt-ln-svg .lt-gl-baru", tipe: "glif" },
  { nama: "terkunci", hide: ".lt-ln-svg .lt-gl-terkunci", tipe: "glif" },
  { nama: "garis", hide: ".lt-ln-garis", tipe: "garis" },
  { nama: "teks-nomor", hide: ".lt-ln-nomor", rect: ".lt-ln-nomor", tipe: "teks" },
  { nama: "teks-pilbab", hide: ".lt-ln-bab text", rect: ".lt-ln-bab text", tipe: "teks" },
] };
const kf0 = mode.startsWith("lensa") ? LN : IK;
const pilih = process.env.LINTASAN ? process.env.LINTASAN.split(",") : null;
const kf = { akar: kf0.akar, lintasan: kf0.lintasan.filter((l) => !pilih || pilih.includes(l.nama)) };
const r = await mulai({ tema, lebar: w, tinggi: h, gerak: "mati", profil: process.env.PROFIL || "nyata" });
const page = r.page;
if (process.env.EKSTRA_CSS) await page.addStyleTag({ content: process.env.EKSTRA_CSS });
if (mode.startsWith("lensa")) {
  const key = mode.split(":")[1] || "html";
  await page.evaluate((k) => { location.hash = "#/langit/" + k; }, key);
  await page.waitForSelector(".lt-lensa-kanvas svg", { timeout: 10000 });
  await page.waitForTimeout(700);
}
await page.addStyleTag({ content: "#rel, .kursor, .kursor-jejak { visibility: hidden !important; } *{caret-color:transparent!important}" });
await page.waitForTimeout(300);
const akar = page.locator(kf.akar).first();
const awal = await akar.evaluate((el) => { el.scrollIntoView({ block: "start" }); const q = el.getBoundingClientRect(); return { x: q.x + scrollX, y: q.y + scrollY, w: q.width, h: q.height }; });
const meta = { usul: etiket, port, tema, w, h, akar: awal, lintasan: [] };
const awalan = `${OUT}/${etiket}-${mode.replace(":", "_")}-${port}-${tema}-${w}`;
for (const l of kf.lintasan) {
  let rects = null;
  if (l.rect) rects = await page.evaluate(([sel, ak]) => {
    const a = document.querySelector(ak).getBoundingClientRect();
    return [...document.querySelectorAll(sel)].map((el) => { const q = el.getBoundingClientRect(); const cs = getComputedStyle(el);
      let sc = 1; try { if (el.getScreenCTM && el instanceof SVGElement) sc = el.getScreenCTM().a; } catch (e) {}
      return { x: q.x - a.x, y: q.y - a.y, w: q.width, h: q.height, fs: parseFloat(cs.fontSize), sc, fw: cs.fontWeight, t: (el.textContent || "").trim().slice(0, 40), ff: cs.fontFamily.slice(0, 30) }; })
      .filter((q) => q.w > 2 && q.h > 2);
  }, [l.rect, kf.akar]);
  await akar.screenshot({ path: `${awalan}-${l.nama}-A.png`, animations: "disabled" });
  const hs = await page.addStyleTag({ content: `${l.hide} { visibility: hidden !important; }` });
  await page.waitForTimeout(80);
  await akar.screenshot({ path: `${awalan}-${l.nama}-B.png`, animations: "disabled" });
  await hs.evaluate((el) => el.remove());
  meta.lintasan.push({ nama: l.nama, tipe: l.tipe, rects });
}
fs.writeFileSync(`${awalan}.json`, JSON.stringify(meta));
console.log("ok", awalan.split("/").pop(), JSON.stringify(awal));
await r.tutup();
