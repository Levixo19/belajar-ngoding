/* Regresi piksel antara DUA build (A dan B) pada halaman yang TIDAK boleh
 * berubah oleh pekerjaan layar Langit: tangkapan layar penuh, 10 halaman x
 * terang dan gelap, gerak mati; sidik SHA-1 yang sama = 0 piksel berbeda.
 * Kedua server harus berprofil terpisah dan sama isinya.
 *
 *     URL_A=http://127.0.0.1:7831 URL_B=http://127.0.0.1:7832 node uji/manual/regresi-piksel.mjs
 */
import crypto from "node:crypto";

const A = process.env.URL_A, B = process.env.URL_B;
if (!A || !B) { console.error("isi URL_A dan URL_B"); process.exit(2); }
const jalur = process.env.PLAYWRIGHT_MJS;
const { chromium } = jalur ? await import(jalur) : await import("playwright");
const halaman = [["bahasa-html", "/#/bahasa/html"], ["bahasa-python", "/#/bahasa/python"], ["dasbor", "/#/dasbor"], ["karier", "/#/karier"], ["statistik", "/#/statistik"], ["pustaka", "/#/pustaka"], ["materi", "/#/materi/html/0"], ["lama-langit", "/lama#/langit"], ["lama-bahasa", "/lama#/bahasa/html"], ["lama-dasbor", "/lama#/dasbor"]];
const b = await chromium.launch({ executablePath: process.env.CHROME ?? "/usr/bin/google-chrome", headless: true, args: ["--no-sandbox"] });
const hasil = {};
for (const [etiket, basis] of [["A", A], ["B", B]]) {
  for (const tema of ["terang", "gelap"]) {
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    await ctx.route("**/*", (r) => (r.request().method() === "GET" ? r.continue() : r.abort()));
    await ctx.addInitScript(([t]) => { try { localStorage.setItem("belajar.tema", JSON.stringify(t)); localStorage.setItem("belajar.gerak", JSON.stringify("mati")); } catch { /* tanpa localStorage */ } }, [tema]);
    const p = await ctx.newPage();
    for (const [nama, url] of halaman) {
      await p.goto(basis.replace(/\/$/, "") + url, { waitUntil: "load" });
      await p.waitForTimeout(1300);
      await p.evaluate((t) => { document.documentElement.dataset.tema = t; document.documentElement.dataset.gerak = "mati"; }, tema);
      await p.waitForTimeout(300);
      const buf = await p.screenshot({ fullPage: true });
      (hasil[`${nama}/${tema}`] ??= {})[etiket] = crypto.createHash("sha1").update(buf).digest("hex").slice(0, 10) + ":" + buf.length;
    }
    await ctx.close();
  }
}
await b.close();
let beda = 0;
for (const [k, v] of Object.entries(hasil)) { const sama = v.A === v.B; if (!sama) beda += 1; console.log(sama ? "SAMA " : "BEDA ", k, sama ? "" : JSON.stringify(v)); }
console.log(beda ? `${beda} pasang berbeda` : `0 piksel berbeda di ${Object.keys(hasil).length} pasang`);
process.exit(beda ? 1 : 0);
