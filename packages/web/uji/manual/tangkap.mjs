/* Tangkapan layar Langit untuk ditinjau mata (bukan pemeriksaan otomatis).
 *   BELAJAR_URL=... TK=/jalur/pendek node uji/manual/tangkap.mjs
 */
import { mulai } from "./lib.mjs";
const TK = process.env.TK ?? "/tmp/langit-tk";
import fs from "node:fs";
fs.mkdirSync(TK, { recursive: true });
const jalan = [
  ["ik-terang-1905", { lebar: 1905, tinggi: 904, tema: "terang", hash: "#/langit" }],
  ["ik-gelap-1905", { lebar: 1905, tinggi: 904, tema: "gelap", hash: "#/langit" }],
  ["ik-terang-1366", { lebar: 1366, tinggi: 768, tema: "terang", hash: "#/langit" }],
  ["ik-campur-terang-1905", { lebar: 1905, tinggi: 904, tema: "terang", hash: "#/langit", profil: "campur" }],
  ["lensa-terang-1366x592", { lebar: 1366, tinggi: 592, tema: "terang", hash: "#/langit/html/0" }],
  ["lensa-campur-gelap-1905", { lebar: 1905, tinggi: 904, tema: "gelap", hash: "#/langit/python/20", profil: "campur" }],
  ["lensa-terkunci-terang-1366", { lebar: 1366, tinggi: 768, tema: "terang", hash: "#/langit/python/10" }],
  ["daftar-terang-952", { lebar: 952, tinggi: 700, tema: "terang", hash: "#/langit" }],
];
for (const [nama, o] of jalan) {
  const s = await mulai(o);
  await s.page.waitForTimeout(500);
  await s.page.screenshot({ path: `${TK}/${nama}.png`, fullPage: false });
  await s.tutup();
}
// peta dengan konsep + profesi
{
  const s = await mulai({ lebar: 1905, tinggi: 904, tema: "terang", hash: "#/langit", profil: "campur" });
  await s.page.getByRole("button", { name: "Perulangan" }).click();
  await s.page.locator(".langit-pilih").click();   // Pilihan buatan sendiri, bukan <select>
  await s.page.locator(".pil-daftar li", { hasText: "Frontend Developer" }).first().click();
  await s.page.waitForTimeout(500);
  await s.page.screenshot({ path: `${TK}/ik-saring-terang-1905.png` });
  await s.tutup();
}
console.log("selesai:", TK);
