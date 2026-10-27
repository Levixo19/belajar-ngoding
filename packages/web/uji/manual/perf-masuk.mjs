/* Biaya MASUK ke layar Langit dan diamnya, pada CPU 4x (CDP), di rute asli.
 * Dipakai untuk mengadu build baru dengan peta lama (server HEAD) pada profil
 * yang SAMA: PROFIL=campur menyuntik status di sisi klien untuk keduanya
 * (server tidak menulis apa pun).
 *
 *     PROFIL=campur BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/perf-masuk.mjs
 *
 * Mesin berderau dan CPU 4x hanya perkiraan: bukti untuk dibaca manusia, bukan
 * batas di suite. Ulangi dan selang-seling antar build.
 */
import { mulai } from "./lib.mjs";

const s = await mulai({ lebar: 1905, tinggi: 904, tema: "terang", gerak: "penuh", profil: process.env.PROFIL ?? "campur", hash: "#/dasbor", tunggu: "#layar", throttle: 4 });
const page = s.page;
await page.waitForTimeout(1200);
await page.evaluate(() => {
  window.__lt = [];
  try { new PerformanceObserver((l) => { for (const e of l.getEntries()) window.__lt.push(e.duration); }).observe({ entryTypes: ["longtask"] }); } catch { /* tanpa longtask */ }
});
const cdp = await s.ctx.newCDPSession(page);
await cdp.send("Performance.enable");
const metr = async () => Object.fromEntries((await cdp.send("Performance.getMetrics")).metrics.map((m) => [m.name, m.value]));
const m0 = await metr(); const t0 = Date.now();
await page.evaluate(() => { location.hash = "#/langit"; });
await page.waitForFunction(() => document.querySelector(".lt-ik-svg, .bimasakti svg, .lt-daftar"), null, { timeout: 60000 });
await page.waitForTimeout(3500);
const m1 = await metr(); const t1 = Date.now();
const lt = await page.evaluate(() => window.__lt);
const hitung = await page.evaluate(() => {
  const inf = document.getAnimations().filter((a) => { try { return a.effect.getComputedTiming().iterations === Infinity && a.playState === "running"; } catch { return false; } });
  return { domTotal: document.querySelectorAll("*").length, animasiTakBerhingga: inf.length };
});
await page.waitForTimeout(500);
const i0 = await metr(); const ti0 = Date.now(); await page.waitForTimeout(4000); const i1 = await metr();
const idle = (100 * (i1.TaskDuration - i0.TaskDuration)) / ((Date.now() - ti0) / 1000);
console.log(JSON.stringify({
  masuk: { tugasDetik: +(m1.TaskDuration - m0.TaskDuration).toFixed(2), tugasPanjang: lt.length, totalPanjangMs: Math.round(lt.reduce((a, b) => a + b, 0)), maksMs: Math.round(Math.max(0, ...lt)) },
  idleSibukPersen: +idle.toFixed(1), ...hitung,
}));
await s.tutup();
