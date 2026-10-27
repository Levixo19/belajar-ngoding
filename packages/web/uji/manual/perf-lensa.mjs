/* Biaya satu langkah panah dan satu pilihan di lensa pada CPU 4x (CDP). Angka
 * milidetik di mesin berderau: ini PAGAR BUKTI untuk dibaca manusia, bukan
 * batas yang dipasang di suite.
 *
 *     BELAJAR_URL=... node uji/manual/perf-lensa.mjs
 */
import { mulai } from "./lib.mjs";

const s = await mulai({ lebar: 1905, tinggi: 904, tema: "terang", gerak: "penuh", profil: "campur", hash: "#/langit/python", throttle: 4 });
const cdp = await s.ctx.newCDPSession(s.page);
await cdp.send("Performance.enable");
const metrik = async () => Object.fromEntries((await cdp.send("Performance.getMetrics")).metrics.map((m) => [m.name, m.value]));
await s.page.evaluate(() => document.querySelector("g[role=option]").focus({ preventScroll: true }));
await s.page.keyboard.press("ArrowRight"); await s.page.waitForTimeout(300);
// Diam: biaya latar (reticle, langit, animasi cangkang) selama waktu yang sama,
// dikurangkan supaya yang tampil adalah biaya LANGKAHNYA.
const diam = {};
{
  const a = await metrik();
  for (let i = 0; i < 40; i++) await s.page.waitForTimeout(70);
  const b = await metrik();
  for (const k of ["TaskDuration", "ScriptDuration", "LayoutDuration", "RecalcStyleDuration"]) diam[k] = ((b[k] - a[k]) * 1000) / 40;
  console.log(`diam (latar, per 70 ms)            tugas ${diam.TaskDuration.toFixed(1)} ms  skrip ${diam.ScriptDuration.toFixed(1)} ms`);
}
const ukur = async (nama, n, langkah) => {
  const a = await metrik();
  for (let i = 0; i < n; i++) { await langkah(i); await s.page.waitForTimeout(70); }
  const b = await metrik();
  const per = (k) => ((((b[k] - a[k]) * 1000) / n) - diam[k]).toFixed(1);
  console.log(`${nama.padEnd(34)} tugas ${per("TaskDuration")} ms  skrip ${per("ScriptDuration")} ms  tata letak ${per("LayoutDuration")} ms  gaya ${per("RecalcStyleDuration")} ms  (bersih dari latar, per langkah, ${n} langkah, CPU 4x)`);
};
await ukur("ArrowRight (pindah fokus)", 40, () => s.page.keyboard.press("ArrowRight"));
await ukur("ArrowLeft", 40, () => s.page.keyboard.press("ArrowLeft"));
await ukur("Enter (pilih bintang)", 20, async (i) => { await s.page.keyboard.press("ArrowRight"); await s.page.keyboard.press("Enter"); });
await s.tutup();
