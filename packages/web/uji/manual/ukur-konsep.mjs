/* Berapa judul yang dinyalakan tiap alternatif regex konsep Langit, dengan
 * contoh. Pakai ini sebelum mengubah `KONSEP`: yang diukur judul NYATA, bukan
 * dugaan (dari sini ketemu `oop` di "Loop" dan `race` di "Trace").
 *
 *     node --experimental-strip-types uji/manual/ukur-konsep.mjs [semua]
 */
import fs from "node:fs";
import { KONSEP } from "../../src/layar/langit-data.ts";
const dir = new URL("../../../konten/kurikulum", import.meta.url).pathname;
const judul = [];
for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".json"))) {
  const k = JSON.parse(fs.readFileSync(`${dir}/${f}`, "utf8"));
  const daftar = k.materi;
  if (!daftar) { console.log("tidak ada daftar materi di", f, Object.keys(k).slice(0, 8)); continue; }
  for (const m of daftar) judul.push([f.replace(".json", ""), String(m.title).replace(/^\d+\.\s*/, "")]);
}
console.log("judul:", judul.length);
const cetak = process.argv[2] === "semua";
for (const [nama, pola] of KONSEP) {
  const alt = pola.source.split("|");
  const total = judul.filter(([, j]) => pola.test(j)).length;
  console.log(`\n## ${nama}: ${total} judul cocok`);
  for (const a of alt) {
    const re = new RegExp(a, "i");
    const cocok = judul.filter(([, j]) => re.test(j));
    if (!cocok.length) { console.log(`   ${a.padEnd(18)} 0 (mati)`); continue; }
    const contoh = cocok.slice(0, cetak ? 8 : 3).map(([, j]) => j).join(" | ");
    console.log(`   ${a.padEnd(18)} ${String(cocok.length).padStart(3)}  ${contoh.slice(0, 150)}`);
  }
}
