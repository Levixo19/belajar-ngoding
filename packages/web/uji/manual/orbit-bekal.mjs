/* Pemeriksaan orbit bekal di panel profesi Peta Karier (`OrbitBekal.tsx`).
 *
 * Persen kurikulum disemai DETERMINISTIK lewat intersepsi respons GET
 * `/api/karier` di sisi klien (server tidak menulis apa pun): semua status
 * (selesai, sedang, belum) muncul di tiap profesi, dan wakil tiap kelompok
 * dihitung ulang seperti `pelajar/karier.kesiapan` (persen tertinggi, seri
 * jatuh ke yang pertama). Yang diukur adalah perilaku:
 *   A data, posisi, label tegak     B putaran: hover, jeda     C pilih, rincian
 *   D alternatif setara             E papan ketik              F gerak selain penuh
 *   G kontras empat tema            H teks sehat, ganti profesi, tata letak
 *
 *   BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/orbit-bekal.mjs
 *   HANYA=A,C   menjalankan bagian tertentu saja (dipakai baterai mutan)
 *   FOTO=/jalur/pendek   menyimpan tangkapan layar tiap bagian
 */

import fs from "node:fs";
import { URL_DASAR, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Orbit bekal");
const FOTO = process.env.FOTO ?? "";
if (FOTO) fs.mkdirSync(FOTO, { recursive: true });
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
const tunggu = (page, ms) => page.waitForTimeout(ms);
const foto = (page, nama) => (FOTO ? page.screenshot({ path: `${FOTO}/${nama}.png` }) : null);
const esc = (t) => t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function benih(j) {
  const pola = [100, 62, 0, 28, 100, 45, 0, 80];
  Object.keys(j.kurikulum).sort().forEach((k, i) => { j.kurikulum[k].persen = pola[i % pola.length]; });
  for (const p of j.profesi) {
    for (const g of p.kelompok) {
      g.wakil = g.pilihan.reduce((a, x) => (j.kurikulum[x].persen > j.kurikulum[a].persen ? x : a), g.pilihan[0]);
      g.persen = j.kurikulum[g.wakil].persen;
    }
    p.kesiapan = p.kelompok.length ? p.kelompok.reduce((s, g) => s + g.persen, 0) / p.kelompok.length : 0;
  }
  return j;
}

async function buka(opsi = {}) {
  const s = await mulai({ lebar: 1440, tinggi: 1000, tema: "gelap", gerak: "penuh", hash: "#/karier", tunggu: ".kr-panel-isi", ...opsi });
  await s.ctx.route(/\/api\/karier(\?|$)/, async (r) => {
    if (r.request().method() !== "GET") return r.fallback();
    const resp = await r.fetch();
    return r.fulfill({ response: resp, body: JSON.stringify(benih(await resp.json())), contentType: "application/json" });
  });
  await s.page.reload({ waitUntil: "load" });
  await s.page.waitForSelector(".or-papan");
  // Papan ada di bawah tangga karier: titik tengahnya harus terlihat, kalau tidak mouse
  // yang diarahkan ke sana jatuh di luar viewport dan hover tidak pernah terjadi.
  await s.page.evaluate(() => document.querySelector(".or-papan").scrollIntoView({ block: "center" }));
  await tunggu(s.page, 500);
  return s;
}

const dataKarier = (page) => page.evaluate(async () => (await (await fetch("/api/karier", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR } })).json()));
const sudutNow = (page) => page.evaluate(() => parseFloat(document.querySelector(".or-papan").style.getPropertyValue("--or-sudut")) || 0);
const selisihSudut = (a, b) => ((b - a + 540) % 360) - 180;
async function berputar(page, ms = 700) {
  const a = await sudutNow(page);
  await tunggu(page, ms);
  return Math.abs(selisihSudut(a, await sudutNow(page))) > 1;
}
const pusatPapan = (page) => page.evaluate(() => { const b = document.querySelector(".or-papan").getBoundingClientRect(); return { x: b.x + b.width / 2, y: b.y + b.height / 2 }; });
async function diamkan(page) { const c = await pusatPapan(page); await page.mouse.move(c.x, c.y); await tunggu(page, 250); }
const pilihProfesi = async (page, nama) => {
  await page.locator(`[aria-label^="${nama}, kesiapan"]`).first().click();
  await page.waitForFunction((n) => document.querySelector(".or-papan")?.getAttribute("aria-label") === `Orbit bekal ${n}`, nama);
  // Klik di tangga menggulir halaman ke atas; papan di bawahnya harus dikembalikan ke tengah layar.
  await page.evaluate(() => document.querySelector(".or-papan").scrollIntoView({ block: "center" }));
  await tunggu(page, 300);
};

/* Yang diharapkan ada di orbit: semua alternatif bekal, lalu pelengkap yang belum muncul. */
function harapan(p, kur) {
  const lihat = new Set(); const dalam = []; const luar = [];
  for (const g of p.kelompok) for (const x of g.pilihan) if (!lihat.has(x)) { lihat.add(x); dalam.push(x); }
  for (const x of p.pelengkap) if (!lihat.has(x)) { lihat.add(x); luar.push(x); }
  const f = (x, lingkar) => ({ kunci: x, label: kur[x]?.label ?? x, persen: kur[x]?.persen ?? 0, lingkar });
  return [...dalam.map((x) => f(x, "dalam")), ...luar.map((x) => f(x, "luar"))];
}

/* ------------------------------------------------ A data, posisi, label tegak */
if (jalan("A")) {
  const s = await buka(); const page = s.page;
  const d = await dataKarier(page);
  const nama = await page.evaluate(() => document.querySelector(".or-papan").getAttribute("aria-label").replace("Orbit bekal ", ""));
  const p = d.profesi.find((x) => x.nama === nama);
  const harap = harapan(p, d.kurikulum);
  const dom = await page.evaluate(() => [...document.querySelectorAll(".or-node")].map((n) => ({
    label: n.querySelector(".or-nama").textContent, persen: n.querySelector(".or-persen").textContent,
    status: n.dataset.status, lingkar: n.dataset.lingkar, aria: n.getAttribute("aria-label"),
    busur: !!n.querySelector(".or-ring-isi"),
  })));
  P.cek(`A jumlah simpul sama dengan bekal dan pelengkap profesi (${harap.length})`, dom.length === harap.length, { dom: dom.length, harap: harap.length });
  const kunciDom = dom.map((x) => `${x.lingkar}|${x.label}|${x.persen}`).sort();
  const kunciHarap = harap.map((x) => `${x.lingkar}|${x.label}|${Math.round(x.persen)}%`).sort();
  P.cek("A tiap simpul membawa cincin, label, dan persen yang sama dengan /api/karier", JSON.stringify(kunciDom) === JSON.stringify(kunciHarap), { dom: kunciDom.slice(0, 3), harap: kunciHarap.slice(0, 3) });
  const status = (v) => (v >= 100 ? "selesai" : v > 0 ? "jalan" : "belum");
  P.cek("A status tiap simpul mengikuti persennya", harap.every((h) => dom.find((x) => x.label === h.label && x.lingkar === h.lingkar)?.status === status(h.persen)));
  P.cek("A busur cincin hanya digambar bila persen > 0", harap.every((h) => dom.find((x) => x.label === h.label)?.busur === (h.persen > 0)));
  P.cek("A nama aksesibel memuat label, cincin, persen, dan status",
    dom.every((x) => new RegExp(`^${esc(x.label)}, (bekal|pelengkap), \\d+ persen, (selesai|sedang dikerjakan|belum dimulai)$`).test(x.aria)), dom.slice(0, 2).map((x) => x.aria));
  const geo = await page.evaluate(() => {
    const b = document.querySelector(".or-papan").getBoundingClientRect(); const cx = b.x + b.width / 2, cy = b.y + b.height / 2;
    return {
      w: b.width, h: b.height,
      node: [...document.querySelectorAll(".or-node")].map((n) => {
        const r = n.getBoundingClientRect(); const m = new DOMMatrix(getComputedStyle(n).transform);
        return { lingkar: n.dataset.lingkar, jarak: Math.hypot(r.x + r.width / 2 - cx, r.y + r.height / 2 - cy), a: m.a, b: m.b };
      }),
    };
  });
  P.cek("A papan persegi dan tidak lebih lebar dari 34rem", Math.abs(geo.w - geo.h) <= 1 && geo.w <= 545, { w: geo.w, h: geo.h });
  P.cek("A simpul cincin dalam berjarak 30% lebar papan dari pusat, luar 44% (tetap saat berputar)",
    geo.node.every((n) => Math.abs(n.jarak - geo.w * (n.lingkar === "dalam" ? 0.3 : 0.44)) <= 2), geo.node.map((n) => `${n.lingkar}:${Math.round(n.jarak)}`));
  P.cek("A label tegak: rantai rotate dan rotate balik meniadakan putaran (matriks a=1, b=0)", geo.node.every((n) => Math.abs(n.a - 1) < 0.001 && Math.abs(n.b) < 0.001), geo.node.slice(0, 2));
  const pusat = await page.evaluate(() => ({ teks: document.querySelector(".or-pusat").textContent, judul: document.querySelector("#kr-judul-orbit")?.textContent }));
  P.cek("A pusat menampilkan kesiapan profesi, dan judul bagian menyebut profesinya", pusat.teks.includes(`${Math.round(p.kesiapan)}%`) && pusat.judul === nama, pusat);
  const warna = await page.evaluate(() => {
    const w = (sel) => { const e = document.querySelector(sel); return e ? getComputedStyle(e).stroke : null; };
    return { selesai: w('.or-node[data-status="selesai"] .or-ring-isi'), jalan: w('.or-node[data-status="jalan"] .or-ring-isi') };
  });
  P.cek("A busur selesai dan sedang dikerjakan berbeda warna", warna.selesai && warna.jalan && warna.selesai !== warna.jalan, warna);
  await foto(page, "A-awal");
  P.cek("A tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

/* ------------------------------------------------ B putaran: hover dan jeda */
if (jalan("B")) {
  const s = await buka(); const page = s.page;
  await page.mouse.move(5, 5);
  P.cek("B berputar sendiri pada gerak penuh", await berputar(page));
  const c = await pusatPapan(page);
  await page.mouse.move(c.x, c.y); await tunggu(page, 250);
  P.cek("B berhenti saat penunjuk ada di atas papan", !(await berputar(page)));
  await page.mouse.move(5, 5); await tunggu(page, 250);
  P.cek("B berputar lagi saat penunjuk meninggalkan papan", await berputar(page));
  const jeda = page.locator(".or-jeda");
  P.cek("B tombol Jeda terlihat dan bernama", (await jeda.count()) === 1 && (await jeda.innerText()) === "Jeda putaran" && (await jeda.getAttribute("aria-pressed")) === "false");
  await jeda.click(); await page.mouse.move(5, 5); await tunggu(page, 300);
  P.cek("B Jeda menghentikan putaran walau penunjuk di luar, dan tombolnya berganti arti",
    !(await berputar(page)) && (await jeda.innerText()) === "Putar lagi" && (await jeda.getAttribute("aria-pressed")) === "true");
  await jeda.click(); await page.mouse.move(5, 5); await tunggu(page, 300);
  P.cek("B Putar lagi melanjutkan putaran", await berputar(page));
  P.cek("B tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

/* ------------------------------------------------ C pilih, rincian, lepas */
if (jalan("C")) {
  const s = await buka(); const page = s.page;
  await diamkan(page);
  const node = page.locator('.or-node[data-lingkar="dalam"]').first();
  const label = await node.locator(".or-nama").innerText();
  await node.click(); await tunggu(page, 250);
  const pilih = await page.evaluate(() => ({
    pressed: document.querySelector(".or-node.aktif")?.getAttribute("aria-pressed"), judul: document.querySelector(".or-rinci h4")?.textContent,
    status: document.querySelector(".or-rinci .pil")?.textContent, bilah: document.querySelector(".or-rinci .kr-bekal-bilah")?.getAttribute("aria-label"),
    tautan: document.querySelector(".or-buka")?.getAttribute("href"), ket: document.querySelector(".or-rinci-ket")?.textContent,
  }));
  P.cek("C klik simpul: aria-pressed menyala dan rincian memuat judulnya", pilih.pressed === "true" && pilih.judul === label, pilih);
  P.cek("C rincian memuat status, bilah persen, kalimat cincin, dan tautan Buka kurikulum",
    /^(selesai|sedang dikerjakan|belum dimulai)$/.test(pilih.status) && /^\d+ persen$/.test(pilih.bilah) && /^Bekal/.test(pilih.ket) && /^#\/bahasa\/[a-z0-9-]+$/.test(pilih.tautan), pilih);
  // Simpul yang baru diklik masih berfokus, dan fokus SENDIRI sudah menghentikan putaran (bagian E):
  // tanpa melepasnya, pagar ini tidak bisa membedakan "ada pilihan" dari "ada fokus".
  await page.mouse.move(5, 5);
  await page.evaluate(() => document.activeElement?.blur());
  await tunggu(page, 200);
  P.cek("C putaran tetap berhenti selama ada simpul terpilih, walau penunjuk keluar papan dan fokus pergi", !(await berputar(page)));
  await foto(page, "C-pilih");
  // Verdigris = selesai dan kuningan = sedang dikerjakan: bilah di rincian sewarna dengan busur simpulnya.
  for (const st of ["selesai", "jalan"]) {
    const n = page.locator(`.or-node[data-status="${st}"]`).first();
    if (!(await n.count())) continue;
    // Mengklik simpul yang sudah terpilih MELEPAS pilihannya (toggle), jadi hanya klik bila belum aktif.
    if (!(await n.evaluate((e) => e.classList.contains("aktif")))) { await n.click(); await tunggu(page, 200); }
    const w = await page.evaluate(() => ({
      bilah: getComputedStyle(document.querySelector(".or-rinci .kr-bekal-bilah > i")).backgroundColor,
      busur: getComputedStyle(document.querySelector(".or-node.aktif .or-ring-isi")).stroke,
    }));
    P.cek(`C bilah rincian sewarna dengan busur simpulnya (${st})`, w.bilah === w.busur, w);
  }
  await page.locator(".or-papan").click({ position: { x: 6, y: 6 } }); await page.mouse.move(5, 5); await tunggu(page, 300);
  const lepas = await page.evaluate(() => ({ aktif: document.querySelectorAll(".or-node.aktif").length, ket: document.querySelector(".or-rinci-ket")?.textContent ?? "" }));
  P.cek("C klik ruang kosong di papan melepas pilihan dan rincian kembali ke ringkasan", lepas.aktif === 0 && /kurikulum di orbit sudah selesai/.test(lepas.ket), lepas);
  P.cek("C putaran berlanjut sesudah pilihan dilepas", await berputar(page));
  await diamkan(page);
  const luar = page.locator('.or-node[data-lingkar="luar"]').first();
  if (await luar.count()) {
    await luar.click(); await tunggu(page, 200);
    const kal = await page.evaluate(() => document.querySelector(".or-rinci-ket")?.textContent ?? "");
    P.cek("C simpul cincin luar dijelaskan sebagai pelengkap yang tidak dihitung ke kesiapan", /^Pelengkap:.*tidak dihitung ke kesiapannya\.$/.test(kal), kal);
  }
  P.cek("C tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

/* ------------------------------------------------ D alternatif setara */
if (jalan("D")) {
  const s = await buka(); const page = s.page;
  const d = await dataKarier(page);
  const p = d.profesi.find((x) => x.kelompok.some((g) => g.pilihan.length > 1));
  await pilihProfesi(page, p.nama);
  await diamkan(page);
  const g = p.kelompok.find((x) => x.pilihan.length > 1);
  const label = (k) => d.kurikulum[k].label;
  const bukan = g.pilihan.find((x) => x !== g.wakil);
  await page.locator(".or-node", { has: page.locator(".or-nama", { hasText: new RegExp(`^${esc(label(bukan))}$`) }) }).first().click();
  await tunggu(page, 250);
  const r = await page.evaluate(() => ({
    berkaitan: document.querySelectorAll(".or-node.berkaitan").length, ket: [...document.querySelectorAll(".or-rinci-ket")].map((x) => x.textContent).join(" | "),
    tautan: document.querySelectorAll(".or-tautan").length,
  }));
  P.cek("D simpul alternatif: anggota kelompok lain disorot (berkaitan) sebanyak alternatifnya", r.berkaitan === g.pilihan.length - 1, r);
  P.cek("D kalimat menyebut wakil yang sedang terdepan dan 'Cukup salah satu'",
    r.ket.includes(`Bekal setara dengan ${label(g.wakil)}, yang sekarang terdepan`) && r.ket.includes("Cukup salah satu. Setara dengan "), r.ket);
  await foto(page, "D-setara");
  await page.locator(".or-tautan").first().click(); await tunggu(page, 250);
  const baru = await page.evaluate(() => document.querySelector(".or-rinci h4")?.textContent);
  P.cek("D tautan alternatif memindahkan pilihan ke simpul lain di kelompok yang sama", baru !== label(bukan) && g.pilihan.map(label).includes(baru), baru);
  const wakilKet = await page.evaluate(() => document.querySelector(".or-rinci-ket")?.textContent);
  P.cek("D bila yang dipilih wakil, kalimatnya menyebut ia yang dihitung ke kesiapan", baru === label(g.wakil) ? /yang dihitung ke kesiapan/.test(wakilKet) : true, wakilKet);
  P.cek("D tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

/* ------------------------------------------------ E papan ketik */
if (jalan("E")) {
  const s = await buka(); const page = s.page;
  const aria = () => page.evaluate(() => document.activeElement?.getAttribute?.("aria-label") ?? "");
  const semua = await page.evaluate(() => [...document.querySelectorAll(".or-node")].map((n) => n.getAttribute("aria-label")));
  await page.locator(".or-node").first().focus(); await tunggu(page, 150);
  P.cek("E fokus pada satu simpul menghentikan putaran", !(await berputar(page, 500)));
  await page.keyboard.press("ArrowRight");
  P.cek("E panah kanan memindahkan fokus ke simpul berikutnya", (await aria()) === semua[1], await aria());
  await page.keyboard.press("ArrowLeft"); await page.keyboard.press("ArrowLeft");
  P.cek("E panah kiri dari simpul pertama berputar ke yang terakhir", (await aria()) === semua[semua.length - 1], await aria());
  await page.keyboard.press("Home");
  P.cek("E Home ke simpul pertama", (await aria()) === semua[0]);
  await page.keyboard.press("End");
  P.cek("E End ke simpul terakhir", (await aria()) === semua[semua.length - 1]);
  await page.keyboard.press("Home"); await page.keyboard.press("Enter"); await tunggu(page, 200);
  P.cek("E Enter memilih simpul", (await page.evaluate(() => document.querySelector(".or-node.aktif")?.getAttribute("aria-label"))) === semua[0]);
  await page.keyboard.press("Escape"); await tunggu(page, 200);
  P.cek("E Esc melepas pilihan dan fokus tetap di simpul", (await page.evaluate(() => document.querySelectorAll(".or-node.aktif").length)) === 0 && (await aria()) === semua[0]);
  await page.keyboard.press("Escape"); await tunggu(page, 100);
  P.cek("E Esc tanpa pilihan tidak berbuat apa pun", (await page.evaluate(() => document.querySelectorAll(".or-node.aktif").length)) === 0);
  await page.locator(".or-node").first().evaluate((n) => n.blur()); await page.mouse.move(5, 5); await tunggu(page, 300);
  P.cek("E putaran berlanjut sesudah fokus pergi", await berputar(page));
  P.cek("E tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

/* ------------------------------------------------ F gerak selain penuh: diam, tetap bisa dipakai */
if (jalan("F")) {
  for (const [nama, o] of [["halus", { gerak: "halus" }], ["mati", { gerak: "mati" }], ["prefers-reduced-motion", { reduce: true, gerak: "penuh" }]]) {
    const s = await buka(o); const page = s.page;
    await page.mouse.move(5, 5);
    P.cek(`F ${nama}: orbit tidak berputar dan tidak ada tombol Jeda`, !(await berputar(page, 800)) && (await page.locator(".or-jeda").count()) === 0);
    await page.locator(".or-node").first().click(); await tunggu(page, 200);
    P.cek(`F ${nama}: simpul tetap bisa dipilih dan rincian tampil`, (await page.evaluate(() => document.querySelectorAll(".or-node.aktif").length)) === 1 && (await page.locator(".or-rinci h4").count()) === 1);
    await s.tutup();
  }
}

/* ------------------------------------------------ G kontras empat tema */
if (jalan("G")) {
  const ukur = (page, sel, prop) => page.evaluate(([s, pr]) => {
    const el = document.querySelector(s); if (!el) return null;
    const rgba = (css) => { const c = document.createElement("canvas"); c.width = c.height = 1; const x = c.getContext("2d", { willReadFrequently: true }); x.clearRect(0, 0, 1, 1); x.fillStyle = css; x.fillRect(0, 0, 1, 1); const d = x.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255]; };
    const lapis = [];
    for (let e = el; e; e = e.parentElement) { const c = rgba(getComputedStyle(e).backgroundColor); if (c[3] > 0) lapis.push(c); if (c[3] >= 1) break; }
    let bg = [255, 255, 255];
    for (const [r, g, b, a] of lapis.reverse()) bg = [r * a + bg[0] * (1 - a), g * a + bg[1] * (1 - a), b * a + bg[2] * (1 - a)];
    const fg = rgba(getComputedStyle(el)[pr]);
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    const L = (c) => 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]);
    const a = L(fg), b = L(bg);
    return Math.round(((Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05)) * 100) / 100;
  }, [sel, prop]);
  for (const tema of ["gelap", "malam", "terang", "kontras"]) {
    const s = await buka({ tema }); const page = s.page;
    await diamkan(page);
    await page.locator(".or-node", { has: page.locator(".or-ring-isi") }).first().click(); await tunggu(page, 200);
    const teks = {
      // `.or-nama` PERTAMA di DOM adalah simpul yang baru dipilih (warnanya `--teks` lewat aturan simpul aktif):
      // label biasa harus diukur pada simpul yang TIDAK aktif, atau warna bawaannya tidak pernah diuji.
      persen: await ukur(page, ".or-persen", "color"), nama: await ukur(page, ".or-node:not(.aktif) .or-nama", "color"),
      namaAktif: await ukur(page, ".or-node.aktif .or-nama", "color"),
      pusatNama: await ukur(page, ".or-pusat-nama", "color"), ket: await ukur(page, ".or-rinci-ket", "color"),
      judul: await ukur(page, ".or-rinci h4", "color"), tautan: await ukur(page, ".or-buka", "color"),
    };
    const rendah = Object.entries(teks).filter(([, v]) => v === null || v < 4.5);
    P.cek(`G ${tema}: teks orbit dan rincian >= 4,5:1`, rendah.length === 0, teks);
    const busur = {
      selesai: await ukur(page, '.or-node[data-status="selesai"] .or-ring-isi', "stroke"),
      jalan: await ukur(page, '.or-node[data-status="jalan"] .or-ring-isi', "stroke"),
    };
    P.cek(`G ${tema}: busur cincin >= 3:1 terhadap simpul`, busur.selesai >= 3 && busur.jalan >= 3, busur);
    await foto(page, `G-${tema}`);
    await s.tutup();
  }
}

/* ------------------------------------------------ H teks sehat, ganti profesi, tata letak */
if (jalan("H")) {
  const s = await buka(); const page = s.page;
  const d = await dataKarier(page);
  const teks = await page.evaluate(() => document.querySelector(".or-wadah").textContent);
  P.cek("H teks orbit tanpa undefined, NaN, [object Object], atau null", !/undefined|NaN|\[object Object\]|\bnull\b/.test(teks));
  // Dua profesi yang berbagi satu kurikulum. Tanpa `key` pada orbit, pilihan atas simpul bersama itu ikut
  // terbawa; pasangan profesi sembarang tidak menguji apa-apa, karena pilihan lama baru tampak hilang
  // (penjaga `?? null`) bila id-nya tidak ada di profesi baru.
  const dalamDari = (p) => new Set(p.kelompok.flatMap((g) => g.pilihan));
  let pasangan = null;
  for (const a of d.profesi) {
    for (const b of d.profesi) {
      if (a.id === b.id || pasangan) continue;
      const x = [...dalamDari(a)].find((k) => dalamDari(b).has(k));
      if (x) pasangan = { a, b, x };
    }
  }
  P.cek("H ada dua profesi yang berbagi satu bekal (bahan uji pergantian profesi)", pasangan !== null);
  if (pasangan) {
    await pilihProfesi(page, pasangan.a.nama);
    await diamkan(page);
    await page.locator(`.or-node[aria-label^="${d.kurikulum[pasangan.x].label}, bekal"]`).click(); await tunggu(page, 200);
    const sebelum = await page.evaluate(() => document.querySelectorAll(".or-node.aktif").length);
    await pilihProfesi(page, pasangan.b.nama);
    const sesudah = await page.evaluate(() => ({ aktif: document.querySelectorAll(".or-node.aktif").length, rinci: document.querySelectorAll(".or-rinci h4").length }));
    P.cek("H berganti ke profesi yang berbagi bekal itu mengosongkan pilihan (key = id profesi)",
      sebelum === 1 && sesudah.aktif === 0 && sesudah.rinci === 0, { dari: pasangan.a.nama, ke: pasangan.b.nama, bersama: pasangan.x, sebelum, ...sesudah });
  }
  const lebar = await page.evaluate(() => { const w = document.querySelector(".or-wadah"); return { sw: w.scrollWidth, cw: w.clientWidth, doc: document.documentElement.scrollWidth, vw: innerWidth }; });
  P.cek("H tidak meluber ke samping (wadah dan halaman)", lebar.sw <= lebar.cw + 1 && lebar.doc <= lebar.vw + 1, lebar);
  P.cek("H tanpa galat konsol dan tanpa permintaan tulis", s.konsol.length === 0 && s.tulisDitolak.length === 0, [...s.konsol, ...s.tulisDitolak]);
  await s.tutup();
}

P.selesai();
