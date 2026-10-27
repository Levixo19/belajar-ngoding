/* Ukuran ikhtisar (peta) layar Langit di peramban: tabrakan nama, judul
 * keluarga, bintang, dan penanda "mulai di sini"; huruf terkecil yang tampil;
 * dan ambang peta/Daftar. Butuh `--experimental-strip-types` (mengimpor
 * geometri murni untuk posisi bintang, rumus yang sama dengan yang dipakai
 * aplikasi).
 *
 *     BELAJAR_URL=http://127.0.0.1:7788/ node --experimental-strip-types uji/manual/ukur-peta.mjs
 */
import { bangunIkhtisar } from "../../src/komponen/lensa-geometri.ts";
import { TATA } from "../../src/layar/langit-data.ts";
import { aktif, mulai, pemeriksa } from "./lib.mjs";

const P = pemeriksa("ukur peta");

/* ---- tabrakan di akar >= 1156 px (jendela - 64 px padding - bilah gulir) */
// SAPU=1: setiap 15 px dari 1.230 sampai 1.920 (sekitar 47 lebar), untuk menangkap
// lebar yang jatuh di antara titik uji. Bawaannya tujuh lebar.
const LEBAR = process.env.SAPU
  ? Array.from({ length: 47 }, (_, i) => 1230 + i * 15)
  : [1230, 1280, 1366, 1440, 1536, 1600, 1905];
for (const w of LEBAR) {
  const s = await mulai({ lebar: w, tinggi: 904, hash: "#/langit", tunggu: ".lt-ikhtisar" });
  const d = await s.page.evaluate(async () => {
    const r = await fetch("/api/langit", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR } });
    const j = await r.json();
    const k = document.querySelector(".lt-ikhtisar").getBoundingClientRect();
    const rel = (e) => { const b = e.getBoundingClientRect(); return { x0: b.left - k.left, y0: b.top - k.top, x1: b.right - k.left, y1: b.bottom - k.top }; };
    return {
      bahasa: j.bahasa, lebar: k.width,
      nama: [...document.querySelectorAll(".lt-nama")].map(rel),
      kel: [...document.querySelectorAll(".lt-keluarga")].map(rel),
      mulai: [...document.querySelectorAll(".lt-mulai")].map(rel),
      mulaiAda: document.querySelectorAll(".lt-mulai").length,
    };
  });
  const ik = bangunIkhtisar(d.bahasa, TATA, d.lebar / 1400);
  const tindih = (a, b) => a.x0 < b.x1 && a.x1 > b.x0 && a.y0 < b.y1 && a.y1 > b.y0;
  const kotak = [...d.nama, ...d.kel];
  let teksTeks = 0;
  for (let i = 0; i < kotak.length; i++) for (let j = i + 1; j < kotak.length; j++) if (tindih(kotak[i], kotak[j])) teksTeks += 1;
  const bintangDi = (k) => ik.semua.filter((b) => b.x + b.r > k.x0 && b.x - b.r < k.x1 && b.y + b.r > k.y0 && b.y - b.r < k.y1).length;
  // teks tanpa bantalan tautan: nama dan keluarga dihitung dari kotak teksnya (padding .3em .6em dibuang)
  const namaTeks = d.nama.map((k) => ({ x0: k.x0 + 7, x1: k.x1 - 7, y0: k.y0 + 4, y1: k.y1 - 4 }));
  const nBintangNama = namaTeks.reduce((a, k) => a + bintangDi(k), 0) + d.kel.reduce((a, k) => a + bintangDi(k), 0);
  const nBintangMulai = d.mulai.reduce((a, k) => a + bintangDi(k), 0);
  const mulaiLabel = d.mulai.reduce((a, m) => a + kotak.filter((k) => tindih(m, k)).length, 0);
  P.cek(`jendela ${w} (peta ${Math.round(d.lebar)} px): nama~nama, nama~judul keluarga, teks~bintang = 0`, teksTeks === 0 && nBintangNama === 0, { teksTeks, nBintangNama });
  P.cek(`jendela ${w}: penanda "mulai di sini" tidak menimpa bintang atau label`, d.mulaiAda === 0 || (nBintangMulai === 0 && mulaiLabel === 0), { nBintangMulai, mulaiLabel, ada: d.mulaiAda });
  await s.tutup();
}

/* ---- huruf terkecil yang tampil: ikhtisar */
for (const [w, h] of [[1366, 768], [1905, 904]]) {
  const s = await mulai({ lebar: w, tinggi: h, hash: "#/langit", tunggu: ".lt-ikhtisar" });
  const kecil = await s.page.evaluate(() => {
    const hasil = [];
    for (const e of document.querySelectorAll(".lt-halaman *")) {
      if (e.closest("svg") && !e.closest("text")) continue;
      const teks = [...e.childNodes].filter((n) => n.nodeType === 3 && n.textContent.trim()).map((n) => n.textContent.trim()).join(" ");
      if (!teks) continue;
      const r = e.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const f = parseFloat(getComputedStyle(e).fontSize);
      if (f < 11.99) hasil.push(`${e.className || e.tagName}: ${f.toFixed(2)}px "${teks.slice(0, 24)}"`);
    }
    return hasil;
  });
  P.cek(`ikhtisar ${w}x${h}: tidak ada teks di bawah 12 px`, kecil.length === 0, kecil.slice(0, 5));
  await s.tutup();
}

/* ---- huruf terkecil yang tampil: lensa (bintang terbuka dan terkunci terpilih) */
for (const [hash, ket] of [["#/langit/html/0", "terbuka"], ["#/langit/html/8", "terkunci"]]) {
  const s = await mulai({ lebar: 1366, tinggi: 768, hash, tunggu: ".lt-lensa g[role=option]" });
  await s.page.waitForTimeout(500);
  const kecil = await s.page.evaluate(() => {
    const hasil = [];
    for (const e of document.querySelectorAll(".lt-lensa *")) {
      const teks = [...e.childNodes].filter((n) => n.nodeType === 3 && n.textContent.trim()).map((n) => n.textContent.trim()).join(" ");
      if (!teks || e.closest(".lt-sr") || e.classList.contains("lt-sr")) continue;
      const f = parseFloat(getComputedStyle(e).fontSize);
      if (f < 11.99) hasil.push(`${e.getAttribute("class") || e.tagName}: ${f.toFixed(2)}px "${teks.slice(0, 20)}"`);
    }
    return hasil;
  });
  P.cek(`lensa (bintang ${ket} terpilih): tidak ada teks di bawah 12 px`, kecil.length === 0, kecil.slice(0, 5));
  await s.tutup();
}

/* ---- ambang peta/Daftar: nol kedipan, dan Daftar punya jawaban atas "mulai dari mana" */
{
  const hasil = [];
  for (const w of [1225, 1230, 1235, 1240]) {
    const s = await mulai({ lebar: w, tinggi: 800, bilahKlasik: true, hash: "#/langit", tunggu: ".lt-ikhtisar, .lt-daftar" });
    const m = await s.page.evaluate(() => ({ peta: !!document.querySelector(".lt-ikhtisar"), akar: document.querySelector(".lt-halaman").clientWidth }));
    await s.page.waitForTimeout(600);
    const m2 = await s.page.evaluate(() => !!document.querySelector(".lt-ikhtisar"));
    hasil.push({ w, ...m, stabil: m.peta === m2 });
    await s.tutup();
  }
  P.cek("bilah gulir klasik: ambang memakai lebar akar yang SUDAH tanpa bilah, dan tidak berkedip", hasil.every((x) => x.stabil && (x.peta === x.akar >= 1156)), hasil);
  const s = await mulai({ lebar: 952, tinggi: 700, hash: "#/langit", tunggu: ".lt-daftar" });
  const d = await s.page.evaluate(() => ({ mulai: document.querySelectorAll(".lt-daftar .lt-mulai").length, urutan: [...document.querySelectorAll(".lt-daftar > *")].slice(0, 2).map((e) => e.className || e.tagName) }));
  P.cek("Daftar (profil xp = 0): penanda mulai ada dan di urutan pertama", d.mulai === 1 && d.urutan[0].includes("lt-mulai"), d);
  await s.tutup();
}

P.selesai();
