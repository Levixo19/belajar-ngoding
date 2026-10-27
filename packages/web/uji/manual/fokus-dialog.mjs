/* Fokus tiga dialog yang digambar sendiri (Bantuan, Palet, catatan): fokus awal
 * di dalam kotak, Tab dan Shift+Tab terjerat, Esc menutup, dan fokus kembali ke
 * pemicunya. Tanpa `useFokusDialog` ketiganya gagal semua (dulu: menutup Bantuan
 * menjatuhkan fokus ke awal halaman). Hanya membuka dan menutup; tidak menekan
 * Simpan, jadi tidak menulis catatan.
 *
 *     BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/fokus-dialog.mjs
 */
import { mulai } from "./lib.mjs";
const hasil = [];
const cek = (nama, ok, info = "") => { hasil.push(ok); console.log((ok ? "  ok     " : "  GAGAL  ") + nama + (info ? "  " + info : "")); };
const dalam = (page) => page.evaluate(() => { const d = document.querySelector('.jendela[role=dialog]'); return !!d && d.contains(document.activeElement); });
const aktif = (page) => page.evaluate(() => { const a = document.activeElement; return a ? (a.getAttribute("aria-label") || a.id || a.tagName) : "null"; });
const ada = (page) => page.evaluate(() => !!document.querySelector('.jendela[role=dialog]'));

async function uji(nama, hash, bukaFn) {
  const s = await mulai({ lebar: 1366, tinggi: 768, tema: "terang", gerak: "mati", hash: "#/langit" });
  const page = s.page;
  if (hash !== "#/langit") { await page.evaluate((h) => { location.hash = h; }, hash); await page.waitForSelector("h1", { timeout: 15000 }); }
  await page.waitForTimeout(900);
  const asal = await bukaFn(page);                    // mengembalikan label elemen pemicu
  await page.waitForTimeout(250);
  cek(`${nama}: dialog terbuka`, await ada(page));
  cek(`${nama}: fokus awal di dalam dialog`, await dalam(page), await aktif(page));
  let keluar = 0;
  for (let i = 0; i < 8; i++) { await page.keyboard.press("Tab"); if (!(await dalam(page))) keluar++; }
  cek(`${nama}: Tab 8x tidak pernah keluar dari dialog`, keluar === 0, `keluar ${keluar}x`);
  keluar = 0;
  for (let i = 0; i < 8; i++) { await page.keyboard.press("Shift+Tab"); if (!(await dalam(page))) keluar++; }
  cek(`${nama}: Shift+Tab 8x tidak pernah keluar`, keluar === 0, `keluar ${keluar}x`);
  await page.keyboard.press("Escape"); await page.waitForTimeout(250);
  cek(`${nama}: Esc menutup`, !(await ada(page)));
  const kini = await aktif(page);
  cek(`${nama}: fokus kembali ke pemicu`, kini === asal, `pemicu "${asal}" sekarang "${kini}"`);
  await s.tutup();
}

await uji("Bantuan", "#/langit", async (page) => {
  const t = page.getByRole("button", { name: "Bantuan pintasan" });
  await t.focus(); await page.keyboard.press("Enter"); return "Bantuan pintasan";
});
await uji("Palet", "#/langit", async (page) => {
  const t = page.getByRole("link", { name: "Pustaka" }).first();
  await t.focus(); const nama = await aktif(page); await page.keyboard.press("Control+k"); return nama;
});
await uji("Catatan", "#/materi/html/0", async (page) => {
  const t = page.getByRole("button", { name: /catatan untuk halaman ini|Catatanmu untuk halaman ini/ }).first();
  await t.focus(); const nama = await aktif(page); await page.keyboard.press("Enter"); return nama;
});
console.log(hasil.every(Boolean) ? `LULUS: ${hasil.length} pemeriksaan` : `GAGAL: ${hasil.filter((x) => !x).length} dari ${hasil.length}`);
