/* Biaya hover di ikhtisar pada CPU 4x (CDP): 120 gerakan mouse menyapu peta.
 * ISOLASI=1 mematikan efek global cangkang (reticle, kanvas langit) supaya yang
 * terukur biaya peta ini saja; tanpa itu angkanya biaya seluruh aplikasi.
 * Mesin berderau dan CPU 4x hanya perkiraan: ini BUKTI untuk dibaca manusia,
 * bukan batas yang dipasang di suite. Ulangi dan selang-seling antar build.
 *
 *     ISOLASI=1 PROFIL=campur BELAJAR_URL=... node uji/manual/perf-hover.mjs
 */
import { mulai } from "./lib.mjs";

const s = await mulai({ lebar: 1905, tinggi: 904, tema: "terang", gerak: "penuh", profil: process.env.PROFIL ?? "campur", hash: "#/langit", throttle: 4 });
const page = s.page;
if (process.env.ISOLASI) await page.addStyleTag({ content: ".kursor,.kursor-jejak,#latar canvas,.langit,.langit-kelip{display:none !important}" });
const cdp = await s.ctx.newCDPSession(page);
await cdp.send("Performance.enable");
const metr = async () => Object.fromEntries((await cdp.send("Performance.getMetrics")).metrics.map((m) => [m.name, m.value]));
await page.waitForTimeout(800);
const hitung = await page.evaluate(() => {
  const inf = document.getAnimations().filter((a) => { try { return a.effect.getComputedTiming().iterations === Infinity && a.playState === "running"; } catch { return false; } });
  return { domTotal: document.querySelectorAll("*").length, domPeta: document.querySelector(".lt-ik-svg")?.querySelectorAll("*").length ?? 0, animasiTakBerhingga: inf.length };
});
const i0 = await metr(); const t0 = Date.now(); await page.waitForTimeout(4000); const i1 = await metr();
const idle = (100 * (i1.TaskDuration - i0.TaskDuration)) / ((Date.now() - t0) / 1000);
const k = await page.evaluate(async () => {
  const p = document.querySelector(".lt-ik-svg"); const r = p.getBoundingClientRect();
  scrollTo(0, Math.max(0, r.top + scrollY - 110)); await new Promise((z) => setTimeout(z, 500));
  const r2 = p.getBoundingClientRect();
  return { x: r2.left, w: r2.width, y: Math.max(r2.top, 120), h: Math.min(r2.bottom, 880) - Math.max(r2.top, 120) };
});
const h0 = await metr(); const N = 120, baris = 8;
for (let i = 0; i < N; i++) {
  const b = Math.floor(i / (N / baris)), f = (i % (N / baris)) / (N / baris - 1);
  await page.mouse.move(k.x + 20 + (b % 2 === 0 ? f : 1 - f) * (k.w - 40), k.y + ((b + 0.5) / baris) * k.h);
}
const h1 = await metr();
const per = (kunci) => ((1000 * (h1[kunci] - h0[kunci])) / N).toFixed(2);
console.log(JSON.stringify({ hitung, idleSibukPersen: +idle.toFixed(1), hoverPerGerakan: { tugasMs: per("TaskDuration"), skripMs: per("ScriptDuration"), gayaMs: per("RecalcStyleDuration"), tataMs: per("LayoutDuration") }, isolasi: !!process.env.ISOLASI }));
await s.tutup();
