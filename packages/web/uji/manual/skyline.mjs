/* Pemeriksaan cakrawala bara di kartu Bara dasbor (`Skyline.tsx`, `BlokBara`).
 *
 * Profil yang dipakai profil UJI dengan riwayat harian disemai (server tidak
 * ditulisi apa pun: `mulai()` menggagalkan semua permintaan selain GET).
 * Kasus tepi (semua hari kosong) disemai lewat intersepsi respons
 * `/api/dasbor` di SISI KLIEN dan ditandai begitu. Yang diukur adalah perilaku:
 *
 *   A bawaan datar, tombol tampilan, ingatan pilihan, kembali ke datar
 *   B isi sama dengan hamparan datar: tingkat, hari ini, ringkasan, urutan gambar
 *   C tinggi batang linear terhadap XP, hari kosong rata
 *   D hover: keterangan berganti, tanpa diumumkan, garis sorot pas di batangnya
 *   E papan ketik: satu perhentian Tab, panah, Home dan End, diumumkan, Alt dilepas
 *   F gerak: penuh menganimasikan, halus dan mati tidak, keadaan akhir sama
 *   G kontras teks dan garis di empat tema
 *   H tata letak: 1440 dan 1280, label tidak menimpa, huruf sangat besar
 *   I kebersihan: tanpa galat konsol, tanpa tulisan ditolak, teks sehat
 *   J semua hari kosong (simulasi)
 *
 *   BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/skyline.mjs
 *   HANYA=A,E   menjalankan bagian tertentu saja (dipakai baterai mutan)
 *   FOTO=/jalur/pendek   menyimpan tangkapan layar tiap bagian
 */

import fs from "node:fs";
import { URL_DASAR, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Cakrawala bara");
const FOTO = process.env.FOTO ?? "";
if (FOTO) fs.mkdirSync(FOTO, { recursive: true });
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
const tunggu = (page, ms) => page.waitForTimeout(ms);
const foto = (page, nama) => (FOTO ? page.locator(".meja-ritme").screenshot({ path: `${FOTO}/${nama}.png` }) : null);
const KUNCI = "belajar.bara.tampil";
const NAMA_HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"];

const buka = (o = {}) => mulai({ lebar: 1440, tinggi: 900, tema: "gelap", gerak: "mati", hash: "#/", tunggu: ".meja-ritme", ...o });

const kePanggung = async (page) => {
  await page.locator(".meja-ritme").scrollIntoViewIfNeeded();
  await page.getByRole("button", { name: "Cakrawala", exact: true }).click();
  await page.waitForSelector(".sk-svg");
  await tunggu(page, 150);
};

/** Hamparan datar apa adanya: judul tiap sel, tingkat, XP, dan jumlah sel kosong pembuka. */
const bacaDatar = (page) => page.evaluate(() => {
  const sel = [...document.querySelectorAll(".bara-petak > .bara-sel")];
  return {
    kosong: document.querySelectorAll(".bara-petak > .bara-kosong").length,
    hari: sel.map((e) => ({
      judul: e.getAttribute("title"),
      tingkat: Number((e.className.match(/bara-(\d)/) || [])[1] ?? 0),
      kini: e.classList.contains("bara-kini"),
      xp: Number((e.getAttribute("title").match(/: (\d+) XP/) || [])[1]),
    })),
  };
});

const info = (page) => page.evaluate(() => document.querySelector(".sk-info")?.textContent ?? null);
const pengumum = (page) => page.evaluate(() => document.querySelector(".pengumum")?.textContent ?? "");

/** Ukur kontras satu properti warna terhadap latar opaque terdekat (menelusuri leluhur). */
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

/* ------------------------------------------------ A bawaan, tombol, ingatan */
if (jalan("A")) {
  const s = await buka(); const page = s.page;
  P.cek("A bawaan: hamparan datar tampil, cakrawala tidak",
    (await page.locator(".bara-petak").count()) === 1 && (await page.locator(".sk-wadah").count()) === 0);
  const tombol = await page.evaluate(() => [...document.querySelectorAll('[aria-label="Tampilan hamparan"] button')].map((b) => [b.textContent, b.getAttribute("aria-pressed")]));
  P.cek("A dua tombol: Datar ditekan, Cakrawala tidak", JSON.stringify(tombol) === JSON.stringify([["Datar", "true"], ["Cakrawala", "false"]]), tombol);
  P.cek("A kelompok tombol bernama dan bertanda role group",
    await page.evaluate(() => document.querySelector('[aria-label="Tampilan hamparan"]')?.getAttribute("role") === "group"));
  P.cek("A bawaan tidak menulis ingatan lokal apa pun", await page.evaluate((k) => localStorage.getItem(k) === null, KUNCI));
  const datar0 = await bacaDatar(page);
  await foto(page, "A-datar");

  await kePanggung(page);
  P.cek("A pindah ke cakrawala: gambar tampil, kisi datar hilang",
    (await page.locator(".sk-svg").count()) === 1 && (await page.locator(".bara-petak").count()) === 0);
  P.cek("A tombol berganti keadaan",
    await page.evaluate(() => { const b = [...document.querySelectorAll('[aria-label="Tampilan hamparan"] button')]; return b[0].getAttribute("aria-pressed") === "false" && b[1].getAttribute("aria-pressed") === "true"; }));
  P.cek("A judul kartu, legenda, dan rampa warna tetap ada",
    await page.evaluate(() => document.querySelector(".bara-kepala .mata")?.textContent === "Bara enam bulan terakhir" && !!document.querySelector(".bara-legenda .bara-rampa") && document.querySelectorAll(".bara-rampa .bara-sel").length === 4));
  P.cek("A petunjuk geser ke kiri tidak ada di cakrawala (ia tidak menggulir)", (await page.locator(".bara-geser").count()) === 0);
  P.cek("A pilihan diingat sebagai teks JSON", await page.evaluate((k) => localStorage.getItem(k) === '"cakrawala"', KUNCI));
  await foto(page, "A-cakrawala");

  await page.reload({ waitUntil: "load" });
  await page.waitForSelector(".meja-ritme .sk-svg");
  P.cek("A muat ulang: tetap cakrawala", (await page.locator(".sk-svg").count()) === 1 && (await page.locator(".bara-petak").count()) === 0);

  // Kembali ke datar: kisinya dipin ke hari ini lagi (tandanya ikut berubah). Kisi dipersempit dengan CSS
  // sisipan karena di lebar desktop isinya tidak pernah melebihi kartu.
  await page.addStyleTag({ content: ".bara-petak { max-width: 200px; }" });
  await page.getByRole("button", { name: "Datar", exact: true }).click();
  await page.waitForSelector(".bara-petak");
  await tunggu(page, 250);
  const pin = await page.evaluate(() => { const e = document.querySelector(".bara-petak"); return { kiri: e.scrollLeft, lebar: e.clientWidth, isi: e.scrollWidth, geser: !document.querySelector(".bara-geser").hidden }; });
  P.cek("A kembali ke datar: kisi dipin ke ujung kanan (hari ini)", pin.isi > pin.lebar && Math.abs(pin.kiri + pin.lebar - pin.isi) <= 2, pin);
  P.cek("A kembali ke datar: petunjuk geser tampil karena ada yang tersembunyi", pin.geser === true, pin);
  const datar1 = await bacaDatar(page);
  P.cek("A kembali ke datar: isi kisi sama persis seperti semula", JSON.stringify(datar1) === JSON.stringify(datar0));
  P.cek("A kembali ke datar: pilihan diingat", await page.evaluate((k) => localStorage.getItem(k) === '"datar"', KUNCI));
  P.cek("A kisi datar tetap bisa difokus dan bernama", await page.evaluate(() => { const e = document.querySelector(".bara-petak"); return e.tabIndex === 0 && e.getAttribute("role") === "group" && /bisa digeser ke samping/.test(e.getAttribute("aria-label")); }));
  await s.tutup();

  // Nilai ingatan yang tidak dikenal jatuh ke datar, tidak merusak halaman.
  for (const [nama, nilai] of [["teks aneh", '"aneh"'], ["bukan JSON", "{"], ["angka", "7"], ["null", "null"]]) {
    const t = await buka(); const pg = t.page;
    await pg.evaluate(([k, v]) => localStorage.setItem(k, v), [KUNCI, nilai]);
    await pg.reload({ waitUntil: "load" });
    await pg.waitForSelector(".meja-ritme");
    await tunggu(pg, 200);
    P.cek(`A ingatan ${nama}: jatuh ke datar tanpa galat`, (await pg.locator(".bara-petak").count()) === 1 && (await pg.locator(".sk-wadah").count()) === 0 && t.konsol.length === 0, t.konsol);
    await t.tutup();
  }
}

/* ------------------------------------------------ B isi sama dengan datar */
if (jalan("B")) {
  const s = await buka(); const page = s.page;
  const d = await bacaDatar(page);
  await kePanggung(page);
  const n = d.hari.length;
  const hasil = await page.evaluate(() => ({
    batang: document.querySelectorAll(".sk-b").length,
    kelas: [...document.querySelectorAll(".sk-b")].sort((a, b) => Number(a.dataset.i) - Number(b.dataset.i)).map((g) => Number((g.getAttribute("class").match(/sk-t(\d)/) || [])[1])),
    kini: [...document.querySelectorAll(".sk-kini")].map((g) => Number(g.dataset.i)),
  }));
  P.cek(`B satu batang per hari (${n})`, hasil.batang === n && n >= 150, { batang: hasil.batang, n });
  P.cek("B tingkat warna tiap batang sama dengan sel datarnya", JSON.stringify(hasil.kelas) === JSON.stringify(d.hari.map((h) => h.tingkat)));
  P.cek("B hanya hari ini yang bertanda kini, dan itu hari terakhir", JSON.stringify(hasil.kini) === JSON.stringify([n - 1]) && d.hari[n - 1].kini, hasil.kini);

  const awal = await info(page);
  const hariIni = await page.evaluate(() => (new Date().getDay() + 6) % 7);
  P.cek("B keterangan awal = hari ini, lengkap dengan nama hari dan judul datar",
    awal === `${NAMA_HARI[hariIni]}, ${d.hari[n - 1].judul}, hari ini`, { awal, harap: `${NAMA_HARI[hariIni]}, ${d.hari[n - 1].judul}, hari ini` });

  const dd = await page.evaluate(() => [...document.querySelectorAll(".sk-ringkas dd")].map((e) => e.textContent));
  const total = d.hari.reduce((a, h) => a + h.xp, 0);
  const puncak = d.hari.reduce((a, h) => Math.max(a, h.xp), 0);
  const aktif = d.hari.filter((h) => h.xp > 0).length;
  let rentetan = 0; let jalanR = 0;
  for (const h of d.hari) { jalanR = h.xp > 0 ? jalanR + 1 : 0; rentetan = Math.max(rentetan, jalanR); }
  const idr = (x) => x.toLocaleString("id-ID");
  P.cek("B ringkasan: total XP sama dengan jumlah di sel datar", dd[0] === idr(total), { dd0: dd[0], total });
  P.cek("B ringkasan: hari tersibuk memuat XP tertinggi", dd[1].includes(`${idr(puncak)} XP`), { dd1: dd[1], puncak });
  P.cek("B ringkasan: rentetan terpanjang sama dengan hitungan lurus", dd[2] === `${idr(rentetan)} hari`, { dd2: dd[2], rentetan });
  const label = await page.evaluate(() => document.querySelector(".sk-papan").getAttribute("aria-label"));
  P.cek("B nama kelompok memuat jumlah hari ber-XP dan total", label.includes(`${idr(aktif)} hari ber-XP, total ${idr(total)} XP`), label);

  // Urutan gambar di DOM: tidak ada batang yang digambar sebelum batang yang lebih belakang darinya.
  const urutan = await page.evaluate((kosong) => {
    const g = [...document.querySelectorAll(".sk-b")];
    const pos = new Map(g.map((e, idx) => [Number(e.dataset.i), idx]));
    const kb = (i) => ({ k: Math.floor((kosong + i) / 7), b: (kosong + i) % 7 });
    let salah = 0; let contoh = null;
    for (const [a, pa] of pos) for (const [b, pb] of pos) {
      if (a === b) continue;
      const x = kb(a); const y = kb(b);
      if (x.k <= y.k && x.b <= y.b && pa > pb) { salah++; contoh = contoh ?? [a, b]; }
    }
    return { salah, contoh };
  }, d.kosong);
  P.cek("B urutan gambar di DOM: yang lebih belakang digambar lebih dulu", urutan.salah === 0, urutan);
  await s.tutup();
}

/* ------------------------------------------------ C tinggi batang */
if (jalan("C")) {
  const s = await buka(); const page = s.page;
  const d = await bacaDatar(page);
  await kePanggung(page);
  const tinggi = await page.evaluate(() => Object.fromEntries([...document.querySelectorAll(".sk-b")].map((g) => [g.dataset.i, g.getBBox().height])));
  const puncak = d.hari.reduce((a, h) => Math.max(a, h.xp), 0);
  const nol = d.hari.map((h, i) => (h.xp === 0 ? tinggi[i] : null)).filter((x) => x !== null);
  P.cek("C hari tanpa XP: semua setinggi petak rata, tanpa dinding", nol.length > 10 && Math.max(...nol) - Math.min(...nol) < 0.05, { n: nol.length, min: Math.min(...nol), max: Math.max(...nol) });
  const lantai = nol[0];
  const kandidat = d.hari.map((h, i) => ({ xp: h.xp, i })).filter((x) => x.xp > 0 && x.xp < puncak);
  let terburuk = 0; let uji = 0;
  for (let a = 0; a + 7 < kandidat.length && uji < 40; a += 5) {
    const p = kandidat[a]; const q = kandidat[a + 7];
    // Sama-sama di atas lantai tinggi (0,12 satuan = 4,08 px) dan di bawah puncak: selisihnya linear.
    const hp = (p.xp / puncak) * 2.4 * 34; const hq = (q.xp / puncak) * 2.4 * 34;
    if (hp < 4.2 || hq < 4.2) continue;
    uji++;
    const selisihUkur = tinggi[q.i] - tinggi[p.i];
    const selisihHarap = hq - hp;
    terburuk = Math.max(terburuk, Math.abs(selisihUkur - selisihHarap));
  }
  P.cek("C tinggi batang linear terhadap XP (selisih pasangan < 0,6 px)", uji >= 10 && terburuk < 0.6, { uji, terburuk });
  const iPuncak = d.hari.findIndex((h) => h.xp === puncak);
  P.cek("C hari terbaik setinggi 2,4 satuan di atas petaknya", Math.abs(tinggi[iPuncak] - lantai - 2.4 * 34) < 0.6, { ukur: tinggi[iPuncak] - lantai, harap: 2.4 * 34 });
  const iKecil = d.hari.findIndex((h) => h.xp > 0 && (h.xp / puncak) * 2.4 * 34 < 4.08);
  if (iKecil >= 0) P.cek("C hari ber-XP yang kecil tetap terlihat (lantai 0,12 satuan)", tinggi[iKecil] - lantai >= 4.0, { xp: d.hari[iKecil].xp, lebih: tinggi[iKecil] - lantai });
  await foto(page, "C-tinggi");
  await s.tutup();
}

/* ------------------------------------------------ D hover */
if (jalan("D")) {
  const s = await buka(); const page = s.page;
  const d = await bacaDatar(page);
  await kePanggung(page);
  await page.evaluate(() => document.querySelector(".sk-svg").scrollIntoView({ block: "center" }));
  await tunggu(page, 150);
  const titik = (i) => page.evaluate((i) => {
    const g = document.querySelector(`.sk-b[data-i="${i}"]`); const r = g.querySelector(".sk-atas").getBoundingClientRect();
    const x = r.x + r.width / 2; const y = r.y + r.height / 2;
    const el = document.elementFromPoint(x, y); const kena = el && el.closest("[data-i]");
    return { x, y, kena: kena ? Number(kena.getAttribute("data-i")) : -1 };
  }, i);
  // Hanya batang yang puncaknya terlihat (tidak tertutup batang depannya) yang bisa dituju penunjuk.
  const terlihat = [];
  for (let i = 20; i < 170 && terlihat.length < 4; i += 9) { const t = await titik(i); if (t.kena === i) terlihat.push({ i, ...t }); }
  P.cek("D ada batang yang puncaknya terlihat untuk dituju", terlihat.length >= 3, terlihat.map((t) => t.i));
  const kosongN = d.kosong;
  const sebelumUmum = await pengumum(page);
  for (const t of terlihat) {
    await page.mouse.move(t.x, t.y); await tunggu(page, 120);
    const teks = await info(page);
    const hariBaris = (kosongN + t.i) % 7;
    P.cek(`D hover hari ke-${t.i}: keterangan memuat nama hari dan judul datar`, teks === `${NAMA_HARI[hariBaris]}, ${d.hari[t.i].judul}`, { teks, harap: `${NAMA_HARI[hariBaris]}, ${d.hari[t.i].judul}` });
    const kotak = await page.evaluate((i) => {
      const g = document.querySelector(`.sk-b[data-i="${i}"]`).getBBox(); const a = document.querySelector(".sk-aktif");
      if (!a) return null; const b = a.getBBox();
      return { dx: Math.abs(g.x - b.x), dy: Math.abs(g.y - b.y), dw: Math.abs(g.width - b.width), dh: Math.abs(g.height - b.height) };
    }, t.i);
    P.cek(`D hover hari ke-${t.i}: garis sorot pas melingkupi batangnya`, kotak && Math.max(kotak.dx, kotak.dy, kotak.dw, kotak.dh) < 0.1, kotak);
  }
  P.cek("D hover tidak diumumkan ke pembaca layar", (await pengumum(page)) === sebelumUmum, await pengumum(page));
  P.cek("D garis sorot digambar terakhir, di atas semua batang (hari tersembunyi tetap terlihat terpilih)",
    await page.evaluate(() => document.querySelector(".sk-svg").lastElementChild?.classList.contains("sk-aktif") === true));
  const terakhirTeks = await info(page);
  await page.mouse.move(2, 2); await tunggu(page, 120);
  P.cek("D penunjuk keluar dari gambar: keterangan tidak melompat", (await info(page)) === terakhirTeks);
  P.cek("D klik tidak menavigasi (alamat tetap) dan tidak membuka apa pun",
    await (async () => { const sebelum = page.url(); const t = terlihat[0]; await page.mouse.click(t.x, t.y); await tunggu(page, 150); return page.url() === sebelum; })());
  await foto(page, "D-hover");
  await s.tutup();
}

/* ------------------------------------------------ E papan ketik */
if (jalan("E")) {
  const s = await buka(); const page = s.page;
  const d = await bacaDatar(page);
  await kePanggung(page);
  const n = d.hari.length;
  const kb = (i) => ({ k: Math.floor((d.kosong + i) / 7), b: (d.kosong + i) % 7 });
  const nama = (i) => `${NAMA_HARI[kb(i).b]}, ${d.hari[i].judul}${i === n - 1 ? ", hari ini" : ""}`;
  const papan = await page.evaluate(() => { const e = document.querySelector(".sk-papan"); return { tab: e.tabIndex, role: e.getAttribute("role"), label: e.getAttribute("aria-label"), fokusBisa: [...e.querySelectorAll("a[href],button,input,select,textarea,[tabindex]")].length, svgFokus: document.querySelector(".sk-svg").getAttribute("focusable"), svgHidden: document.querySelector(".sk-svg").getAttribute("aria-hidden") }; });
  P.cek("E satu perhentian Tab: kelompok berfokus, isinya tidak", papan.tab === 0 && papan.role === "group" && papan.fokusBisa === 0, papan);
  P.cek("E gambar disembunyikan dari pembaca layar dan tidak berfokus", papan.svgHidden === "true" && papan.svgFokus === "false", papan);
  P.cek("E nama kelompok menyebut cara menjelajah", /Panah menjelajah hari, Home dan End ke ujung/.test(papan.label), papan.label);

  await page.focus(".sk-papan");
  const mulaiTeks = await info(page);
  P.cek("E fokus tidak mengubah keterangan (tetap hari ini)", mulaiTeks === nama(n - 1), mulaiTeks);

  let i = n - 1;
  const langkah = (tombol) => {
    const akhir = n - 1; const b = kb(i).b;
    return { ArrowRight: Math.min(akhir, i + 7), ArrowLeft: Math.max(0, i - 7), ArrowDown: b < 6 && i < akhir ? i + 1 : i, ArrowUp: b > 0 && i > 0 ? i - 1 : i, Home: 0, End: akhir, PageDown: Math.min(akhir, i + 28), PageUp: Math.max(0, i - 28) }[tombol];
  };
  const urut = ["ArrowLeft", "ArrowLeft", "ArrowUp", "ArrowDown", "ArrowDown", "ArrowRight", "Home", "ArrowRight", "End", "PageUp", "PageUp", "PageDown", "ArrowUp", "ArrowUp", "ArrowUp", "ArrowUp", "ArrowUp", "ArrowUp", "ArrowUp", "ArrowDown"];
  let salah = null;
  for (const t of urut) {
    const harap = langkah(t); const bedaI = harap !== i;
    await page.keyboard.press(t); await tunggu(page, 100);
    i = harap;
    const teks = await info(page);
    if (teks !== nama(i)) { salah = { t, i, teks, harap: nama(i) }; break; }
    if (bedaI) {
      await tunggu(page, 100);
      const um = await pengumum(page);
      if (um !== nama(i)) { salah = { t, i, um, harap: nama(i), cabang: "pengumuman" }; break; }
    }
  }
  P.cek(`E ${urut.length} penekanan: keterangan dan pengumuman mengikuti oracle langkah`, salah === null, salah);

  const lepas = await page.evaluate(() => {
    const e = document.querySelector(".sk-papan");
    const dari = (init) => { const ev = new KeyboardEvent("keydown", { key: "ArrowLeft", bubbles: true, cancelable: true, ...init }); e.dispatchEvent(ev); return ev.defaultPrevented; };
    return { alt: dari({ altKey: true }), ctrl: dari({ ctrlKey: true }), meta: dari({ metaKey: true }), polos: dari({}) };
  });
  P.cek("E Alt, Ctrl, dan Meta bersama panah dilepas (milik peramban); panah polos ditelan", !lepas.alt && !lepas.ctrl && !lepas.meta && lepas.polos, lepas);
  const tombolLain = await page.evaluate(() => { const e = document.querySelector(".sk-papan"); const out = {}; for (const k of ["a", "Enter", " ", "Tab", "Escape"]) { const ev = new KeyboardEvent("keydown", { key: k, bubbles: true, cancelable: true }); e.dispatchEvent(ev); out[k] = ev.defaultPrevented; } return out; });
  P.cek("E tombol lain tidak ditelan (Tab, Enter, Esc, huruf)", Object.values(tombolLain).every((x) => x === false), tombolLain);
  await page.keyboard.press("ArrowRight");
  const ring = await page.evaluate(() => { const e = document.querySelector(".sk-papan"); const c = getComputedStyle(e); return { fv: e.matches(":focus-visible"), gaya: c.outlineStyle, lebar: parseFloat(c.outlineWidth) }; });
  P.cek("E cincin fokus terlihat saat dijelajah dengan papan ketik", ring.fv && ring.gaya !== "none" && ring.lebar >= 2, ring);
  await page.keyboard.press("Tab"); await tunggu(page, 80);
  P.cek("E Tab keluar dari kelompok, bukan terjebak", await page.evaluate(() => !document.activeElement?.closest(".sk-papan")));
  await foto(page, "E-papan-ketik");
  await s.tutup();
}

/* ------------------------------------------------ F gerak */
if (jalan("F")) {
  const hitung = (page) => page.evaluate(() => ({ anim: document.getAnimations().filter((a) => a.animationName === "sk-tumbuh").length, masuk: !!document.querySelector(".sk-masuk") }));
  const ukuranAkhir = {};
  for (const [gerak, reduce, harap] of [["penuh", false, true], ["halus", false, false], ["mati", false, false], ["penuh", true, false]]) {
    const s = await buka({ gerak, reduce }); const page = s.page;
    await page.locator(".meja-ritme").scrollIntoViewIfNeeded();
    await page.getByRole("button", { name: "Cakrawala", exact: true }).click();
    await page.waitForSelector(".sk-svg");
    const awal = await hitung(page);
    const nama = `${gerak}${reduce ? " + prefers-reduced-motion" : ""}`;
    P.cek(`F ${nama}: ${harap ? "batang dianimasikan masuk" : "tanpa animasi masuk"}`, harap ? awal.masuk && awal.anim >= 100 : !awal.masuk && awal.anim === 0, awal);
    if (harap) {
      // Deterministik, tanpa menebak waktu: jeda semua animasi di nol lalu baca transformnya. Batang pertama
      // (tanpa jeda) dan batang terakhir (jeda terpanjang) sama-sama harus berskala nol: yang terakhir hanya
      // begitu bila keadaan awalnya ditahan selama jeda (fill backwards), bukan baru berlaku saat gilirannya.
      const dari = await page.evaluate(() => {
        const anim = document.getAnimations().filter((a) => a.animationName === "sk-tumbuh");
        anim.forEach((a) => { a.pause(); a.currentTime = 0; });
        const g = [...document.querySelectorAll(".sk-b")];
        const t = (e) => getComputedStyle(e).transform;
        const terakhir = g.reduce((m, e) => (Number(e.dataset.i) > Number(m.dataset.i) ? e : m));
        const hasil = { pertama: t(g[0]), terakhir: t(terakhir) };
        anim.forEach((a) => a.play());
        return hasil;
      });
      P.cek("F penuh: animasi berangkat dari skala nol, juga selama batang menunggu gilirannya",
        /^matrix\(1, 0, 0, 0,/.test(dari.pertama) && /^matrix\(1, 0, 0, 0,/.test(dari.terakhir), dari);
    }
    await tunggu(page, 1800);
    const akhir = await hitung(page);
    P.cek(`F ${nama}: sesudah selesai tidak ada animasi tersisa`, akhir.anim === 0, akhir);
    const keadaan = await page.evaluate(() => ({
      transform: [...new Set([...document.querySelectorAll(".sk-b")].map((g) => getComputedStyle(g).transform))],
      tinggi: Object.fromEntries([...document.querySelectorAll(".sk-b")].slice(0, 60).map((g) => [g.dataset.i, Math.round(g.getBoundingClientRect().height * 100) / 100])),
    }));
    P.cek(`F ${nama}: keadaan akhir alami (tanpa transform tertinggal)`, keadaan.transform.length === 1 && keadaan.transform[0] === "none", keadaan.transform);
    ukuranAkhir[`${gerak}${reduce ? "+reduce" : ""}`] = keadaan.tinggi;
    await s.tutup();
  }
  P.cek("F ukuran akhir batang di gerak penuh sama dengan di gerak mati (animasi tidak mengubah keadaan alami)",
    JSON.stringify(ukuranAkhir.penuh) === JSON.stringify(ukuranAkhir.mati), { contoh: Object.entries(ukuranAkhir.penuh ?? {}).slice(0, 3) });

  // Gerak dinyalakan SESUDAH gambar tampil: tidak memutar ulang animasi masuk.
  const s = await buka({ gerak: "mati" }); const page = s.page;
  await kePanggung(page);
  await page.evaluate(() => { document.documentElement.dataset.gerak = "penuh"; try { localStorage.setItem("belajar.gerak", JSON.stringify("penuh")); } catch { /* tanpa ingatan */ } document.dispatchEvent(new Event("tampilan-berubah")); });
  await tunggu(page, 250);
  const lambat = await hitung(page);
  P.cek("F gerak dinyalakan setelah tampil: tidak memutar ulang animasi masuk", lambat.anim === 0 && !lambat.masuk, lambat);
  await s.tutup();
}

/* ------------------------------------------------ G kontras empat tema */
if (jalan("G")) {
  for (const tema of ["gelap", "malam", "terang", "kontras"]) {
    const s = await buka({ tema }); const page = s.page;
    await kePanggung(page);
    const teks = {
      bulan: await ukur(page, ".sk-bulan", "color"), info: await ukur(page, ".sk-info", "color"),
      dt: await ukur(page, ".sk-ringkas dt", "color"), dd: await ukur(page, ".sk-ringkas dd", "color"),
    };
    const rendah = Object.entries(teks).filter(([, v]) => v === null || v < 4.5);
    P.cek(`G ${tema}: teks cakrawala >= 4,5:1`, rendah.length === 0, teks);
    const garis = {
      t1: await ukur(page, ".sk-t1 .sk-atas", "stroke"), t2: await ukur(page, ".sk-t2 .sk-atas", "stroke"),
      t3: await ukur(page, ".sk-t3 .sk-atas", "stroke"), t0: await ukur(page, ".sk-t0 .sk-atas", "stroke"),
      aktif: await ukur(page, ".sk-aktif", "stroke"), kini: await ukur(page, ".sk-kini .sk-atas", "stroke"),
    };
    P.cek(`G ${tema}: garis sorot dan penanda hari ini >= 7:1`, garis.aktif >= 7 && garis.kini >= 7, garis);
    P.cek(`G ${tema}: tepi batang berisi XP >= 1,8:1 terhadap kartu (wujudnya terbaca)`, garis.t1 >= 1.8 && garis.t2 >= 1.8 && garis.t3 >= 1.8, garis);
    const tiga = await page.evaluate(() => {
      const rgba = (css) => { const c = document.createElement("canvas"); c.width = c.height = 1; const x = c.getContext("2d", { willReadFrequently: true }); x.fillStyle = css; x.fillRect(0, 0, 1, 1); return [...x.getImageData(0, 0, 1, 1).data].slice(0, 3); };
      const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
      const L = (c) => 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]);
      const w = (s) => L(rgba(getComputedStyle(document.querySelector(s)).fill));
      const r = (x, y) => Math.round(((Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05)) * 100) / 100;
      const a = w(".sk-t1 .sk-atas"), b = w(".sk-t2 .sk-atas"), c = w(".sk-t3 .sk-atas");
      const g = document.querySelector(".sk-t3"); const v = (k) => L(rgba(getComputedStyle(g.querySelector(k)).fill));
      return { t12: r(a, b), t23: r(b, c), atas: v(".sk-atas"), muka: v(".sk-muka"), sisi: v(".sk-sisi") };
    });
    P.cek(`G ${tema}: tiga tingkat puncak batang berbeda terang-gelapnya (>= 1,15:1 berturutan)`, tiga.t12 >= 1.15 && tiga.t23 >= 1.15, tiga);
    P.cek(`G ${tema}: puncak lebih terang dari muka depan, muka lebih terang dari sisi`, tiga.atas > tiga.muka && tiga.muka > tiga.sisi, tiga);
    await foto(page, `G-${tema}`);
    await s.tutup();
  }
}

/* ------------------------------------------------ H tata letak */
if (jalan("H")) {
  for (const [lebar, tinggi] of [[1440, 900], [1280, 800]]) {
    const s = await buka({ lebar, tinggi }); const page = s.page;
    await kePanggung(page);
    const t = await page.evaluate(() => {
      const r = (s) => { const b = document.querySelector(s).getBoundingClientRect(); return { x: b.x, y: b.y, w: b.width, h: b.height, r: b.right, b: b.bottom }; };
      const kartu = r(".meja-ritme .kartu"); const svg = r(".sk-svg"); const bidang = r(".sk-bidang");
      const labels = [...document.querySelectorAll(".sk-bulan")].map((e) => { const b = e.getBoundingClientRect(); return { teks: e.textContent, x: b.x, r: b.right, y: b.y, b: b.bottom }; });
      return { kartu, svg, bidang, labels, lebarHalaman: document.documentElement.scrollWidth, jendela: innerWidth, root: parseFloat(getComputedStyle(document.documentElement).fontSize) };
    });
    P.cek(`H ${lebar}: gambar di dalam kartu dan tidak lebih lebar dari 64rem`, t.svg.x >= t.kartu.x - 0.5 && t.svg.r <= t.kartu.r + 0.5 && t.svg.w <= 64 * t.root + 1, t);
    P.cek(`H ${lebar}: kartu selebar kolom beranda (satu kolom lentur, bukan menyusut)`, t.kartu.w > 700, { kartu: t.kartu.w });
    P.cek(`H ${lebar}: halaman tidak meluber ke samping`, t.lebarHalaman <= t.jendela, { halaman: t.lebarHalaman, jendela: t.jendela });
    P.cek(`H ${lebar}: label bulan di dalam bidang gambar`, t.labels.length >= 4 && t.labels.every((l) => l.x >= t.bidang.x - 1 && l.r <= t.bidang.r + 1 && l.b <= t.bidang.b + 1), t.labels);
    let tumpuk = null;
    for (let a = 0; a < t.labels.length; a++) for (let b = a + 1; b < t.labels.length; b++) {
      const p = t.labels[a]; const q = t.labels[b];
      if (p.x < q.r + 4 && q.x < p.r + 4 && p.y < q.b && q.y < p.b) tumpuk = [p.teks, q.teks];
    }
    P.cek(`H ${lebar}: label bulan tidak saling menimpa`, tumpuk === null, tumpuk);
    await foto(page, `H-${lebar}`);
    await s.tutup();
  }
  const s = await buka({ ukuranTeks: "sangat besar" }); const page = s.page;
  await kePanggung(page);
  const besar = await page.evaluate(() => {
    const bd = document.querySelector(".sk-bidang").getBoundingClientRect();
    return [...document.querySelectorAll(".sk-bulan")].map((e) => { const b = e.getBoundingClientRect(); return { teks: e.textContent, b: b.bottom, bidangB: bd.bottom, fs: parseFloat(getComputedStyle(e).fontSize) }; });
  });
  P.cek("H huruf sangat besar: label ikut membesar mengikuti rem", besar.length > 0 && besar.every((b) => b.fs >= 13), besar.slice(0, 2));
  P.cek("H huruf sangat besar: label bulan tetap di dalam bidang gambar", besar.every((b) => b.b <= b.bidangB + 0.5), besar.map((b) => [b.teks, Math.round(b.bidangB - b.b)]));
  await foto(page, "H-huruf-besar");
  await s.tutup();
}

/* ------------------------------------------------ I kebersihan */
if (jalan("I")) {
  const s = await buka({ gerak: "penuh" }); const page = s.page;
  await kePanggung(page);
  await page.focus(".sk-papan");
  for (const t of ["ArrowLeft", "Home", "End", "ArrowDown"]) await page.keyboard.press(t);
  await tunggu(page, 1500);
  const teks = await page.evaluate(() => document.querySelector(".sk-wadah").textContent + " " + document.querySelector(".sk-papan").getAttribute("aria-label"));
  P.cek("I teks cakrawala tanpa undefined, NaN, [object Object], atau null", !/undefined|NaN|\[object Object\]|\bnull\b/.test(teks), teks.slice(0, 120));
  P.cek("I tanpa dash di teks yang dilihat pelajar", !/[—–]/.test(teks));
  P.cek("I tidak ada <title> atau atribut title di dalam gambar (tooltip ganda dan hujan pembaca layar)", await page.evaluate(() => document.querySelectorAll(".sk-svg title, .sk-svg [title]").length === 0));
  P.cek("I tanpa galat atau peringatan konsol", s.konsol.length === 0, s.konsol);
  P.cek("I tidak ada permintaan tulis yang terkirim (semua non-GET digagalkan)", s.tulisDitolak.length === 0, s.tulisDitolak);
  await s.tutup();
}

/* ------------------------------------------------ J semua hari kosong (SIMULASI) */
if (jalan("J")) {
  const s = await buka(); const page = s.page;
  // SIMULASI: respons /api/dasbor diubah di sisi klien (heatmap nol semua, XP total tetap positif supaya
  // dasbor biasa tampil, bukan layar mulai). Server tidak ditulisi apa pun.
  await s.ctx.route(/\/api\/dasbor(\?|$)/, async (r) => {
    const resp = await r.fetch(); const j = await resp.json();
    j.heatmap = j.heatmap.map((h) => ({ ...h, xp: 0 })); j.xp = Math.max(j.xp, 100);
    await r.fulfill({ response: resp, body: JSON.stringify(j), contentType: "application/json" });
  });
  await page.reload({ waitUntil: "load" });
  await page.waitForSelector(".meja-ritme");
  await kePanggung(page);
  const hasil = await page.evaluate(() => ({
    info: document.querySelector(".sk-info").textContent,
    dd: [...document.querySelectorAll(".sk-ringkas dd")].map((e) => e.textContent),
    label: document.querySelector(".sk-papan").getAttribute("aria-label"),
    tinggi: [...new Set([...document.querySelectorAll(".sk-b")].map((g) => Math.round(g.getBBox().height * 100)))],
    batang: document.querySelectorAll(".sk-b").length,
    dinding: document.querySelectorAll(".sk-muka, .sk-sisi").length,
  }));
  P.cek("J semua hari kosong: gambar tetap tampil sebagai lantai rata tanpa dinding", hasil.batang >= 150 && hasil.tinggi.length === 1 && hasil.dinding === 0, hasil);
  P.cek("J ringkasan jujur: total nol, tersibuk dan rentetan belum ada", hasil.dd[0] === "0" && hasil.dd[1] === "belum ada" && hasil.dd[2] === "belum ada", hasil.dd);
  P.cek("J nama kelompok: belum ada hari ber-XP", /belum ada hari ber-XP/.test(hasil.label), hasil.label);
  P.cek("J keterangan hari ini menyebut 0 XP", /: 0 XP, hari ini$/.test(hasil.info), hasil.info);
  P.cek("J tanpa NaN atau undefined", !/NaN|undefined/.test(hasil.info + hasil.dd.join(" ") + hasil.label));
  P.cek("J tanpa galat konsol", s.konsol.length === 0, s.konsol);
  await foto(page, "J-kosong");
  await s.tutup();
}

P.selesai();
