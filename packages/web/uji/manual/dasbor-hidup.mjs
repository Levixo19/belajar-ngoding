/* Pemeriksaan Dasbor susunan baru (`layar/Dasbor.tsx` MejaKerja, `AngkaHidup.tsx`, blok "dasbor
 * hidup" di gaya.css), diukur di peramban pada profil BERPROGRES (bagian H pada profil BARU).
 *
 *   A  tata letak di 1280x800, 1440x900, 1600x1000: urutan bagian, tiket selebar sapaan, tanpa
 *      meluber ke samping (kartu bara pernah meluber 40 px), tidak ada elemen melewati tepi konten
 *   B  rel bahasa: satu panel terbuka, yang lain 64 px dan `inert`; mouse membuka; fokus dan klik
 *      membuka; `aria-expanded` mengikuti; rasi hanya di panel terbuka; gerak penuh memuai bertahap,
 *      gerak mati langsung
 *   C  angka hidup: urutan nilai DIREKAM (MutationObserver) dari muat ulang; di gerak penuh angka
 *      naik monoton dan berakhir TEPAT di angka data; gerak mati, halus, dan prefers-reduced-motion
 *      hanya pernah menulis angka akhir; pembaca layar membaca angka akhir
 *   D  kontras teks kunci di empat tema dari piksel (opasitas leluhur dan alfa warna teks ikut dihitung)
 *   E  papan ketik: tiap perhentian di rel terlihat dan tidak tertutup; tautan panel yang tertutup
 *      tidak bisa dijangkau Tab; fokus pada tab membuka panelnya
 *   F  hover tiket dan kartu langkah lewat `translate`, bukan `transform`
 *   G  isi sama dengan data: jumlah kartu langkah, urutan rel, judul tiket, lencana, tanpa tulisan rusak
 *   H  profil baru (XP 0): tidak memakai susunan ini (layar mulai)
 *
 *   # A sampai G: server berprofil berprogres
 *   HANYA=A,B,C,D,E,F,G BELAJAR_URL=http://127.0.0.1:7790/ node uji/manual/dasbor-hidup.mjs
 *   # H: server berprofil baru (XP 0)
 *   HANYA=H BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/dasbor-hidup.mjs
 *
 * Jalankan terhadap server berprofil SEMENTARA (lihat `lib.mjs`); permintaan selain GET digagalkan
 * di sana. `FOTO=<direktori>` menyimpan tangkapan layar.
 */

import { URL_DASAR, lum, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Dasbor hidup");
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
const TEMA = ["gelap", "malam", "terang", "kontras"];
const bukanGerutan = (k) => !/GPU stall|GL Driver Message/.test(k);
const tunggu = (page, ms) => page.waitForTimeout(ms);
const hampir = (a, b, t) => Math.abs(a - b) <= t;
const idr = (n) => (Number(n) || 0).toLocaleString("id-ID");

const buka = (opsi = {}) => mulai({
  lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/dasbor", tunggu: ".ds-meja", ...opsi,
});
const keRel = async (page) => {
  await page.evaluate(() => document.querySelector(".ds-rel")?.scrollIntoView({ block: "center", behavior: "instant" }));
  await tunggu(page, 450);
};
const bacaWarna = (c) => {
  const n = c.match(/[\d.]+/g).slice(0, 3).map(Number);
  return c.startsWith("color(") ? n.map((v) => v * 255) : n;
};
const bacaAlpha = (c) => {
  const n = c.match(/[\d.]+/g).map(Number);
  if (n.length < 4) return 1;
  return /%/.test(c.split("/")[1] ?? "") ? n[3] / 100 : n[3];
};
const persentil = (nilai, p) => {
  const a = [...nilai].sort((x, y) => x - y);
  return a[Math.min(a.length - 1, Math.floor((a.length * p) / 100))];
};
const kontrasDua = (l1, l2) => (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);

/** Rasio teks: teks disembunyikan lebih dulu, lalu dikomposit di atas piksel latar median bila setengah transparan. */
async function rasioTeks(page, sel, indeks = 0) {
  const t = await page.evaluate(([s, i]) => {
    const el = document.querySelectorAll(s)[i];
    if (!el) return null;
    const jalan = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    let simpul = null;
    for (let n = jalan.nextNode(); n; n = jalan.nextNode()) { if (n.textContent.trim()) { simpul = n; break; } }
    if (!simpul) return null;
    const r = document.createRange(); r.selectNodeContents(simpul);
    const b = r.getBoundingClientRect();
    let opasitas = 1;
    for (let n = simpul.parentElement; n; n = n.parentElement) opasitas *= parseFloat(getComputedStyle(n).opacity);
    return { kotak: { x: b.x, y: b.y, width: b.width, height: b.height }, warna: getComputedStyle(simpul.parentElement).color, teks: simpul.textContent.trim().slice(0, 34), opasitas };
  }, [sel, indeks]);
  if (!t || t.kotak.width < 2 || t.kotak.height < 2) return { rasio: 0, teks: "(tidak ada)", opasitas: 0 };
  await page.evaluate(() => {
    const st = document.createElement("style"); st.id = "uji-teks-transparan";
    st.textContent = ".ds-meja *, .ds-meja *::before, .ds-meja *::after { color: transparent !important; -webkit-text-fill-color: transparent !important; text-shadow: none !important; }";
    document.head.appendChild(st);
  });
  const png = await page.screenshot({ clip: t.kotak, type: "png" });
  await page.evaluate(() => document.getElementById("uji-teks-transparan")?.remove());
  const piksel = await page.evaluate(async (b64) => {
    const im = new Image(); im.src = "data:image/png;base64," + b64; await im.decode();
    const c = document.createElement("canvas"); c.width = im.width; c.height = im.height;
    const x = c.getContext("2d", { willReadFrequently: true }); x.drawImage(im, 0, 0);
    const d = x.getImageData(0, 0, c.width, c.height).data;
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    const hasil = [];
    for (let i = 0; i < d.length; i += 4) hasil.push({ l: 0.2126 * f(d[i]) + 0.7152 * f(d[i + 1]) + 0.0722 * f(d[i + 2]), rgb: [d[i], d[i + 1], d[i + 2]] });
    return hasil;
  }, png.toString("base64"));
  const urut = [...piksel].sort((a, b) => a.l - b.l);
  const latar = urut[Math.floor(urut.length / 2)].rgb;
  const alfa = bacaAlpha(t.warna);
  const lt = lum(bacaWarna(t.warna).map((v, k) => alfa * v + (1 - alfa) * latar[k]));
  const semua = piksel.map((p) => p.l);
  const rasio = Math.min(kontrasDua(lt, persentil(semua, 1)), kontrasDua(lt, persentil(semua, 99)));
  return { rasio: Math.round(rasio * 100) / 100, teks: t.teks, opasitas: Math.round(t.opasitas * 1000) / 1000 };
}

/* ------------------------------------------------ A tata letak */
if (jalan("A")) {
  for (const [lebar, tinggi] of [[1280, 800], [1440, 900], [1600, 1000]]) {
    const s = await buka({ lebar, tinggi }); const page = s.page;
    await tunggu(page, 900);
    const a = await page.evaluate(() => {
      const k = (q) => { const e = document.querySelector(q); if (!e) return null; const b = e.getBoundingClientRect(); return { kiri: b.left, kanan: b.right, atas: b.top + scrollY, bawah: b.bottom + scrollY, w: b.width }; };
      const meja = document.querySelector(".ds-meja");
      const urut = [".ds-hero", ".ds-antrean", ".ds-rel", ".ds-ritme", ".ds-jelajah", ".pd-bungkus"].map((q) => k(q)?.atas ?? null);
      // Hanya anak langsung meja (penutup sengaja selebar layar); batas konten = tepi bagian pertama.
      const hero = k(".ds-hero");
      const lewat = meja && hero ? [...meja.children].filter((e) => !e.classList.contains("pd-bungkus")).filter((e) => e.getBoundingClientRect().right > hero.kanan + 1).map((e) => e.className) : [];
      return {
        ada: !!meja, urut, hero, tiket: k(".ds-tiket"), rel: k(".ds-rel-rak"), bara: k(".ds-ritme .meja-ritme"),
        kolomBara: getComputedStyle(document.querySelector(".ds-ritme .meja-ritme")).gridTemplateColumns,
        meluber: document.documentElement.scrollWidth - document.documentElement.clientWidth, lewat,
        stat: document.querySelectorAll(".ds-stat-butir").length, h1: document.querySelectorAll(".ds-sapa").length,
      };
    });
    const w = `${lebar}x${tinggi}`;
    P.cek(`A ${w}: susunan baru terpasang (satu h1 sapaan, tiga angka)`, a.ada && a.h1 === 1 && a.stat === 3, a);
    P.cek(`A ${w}: urutan bagian dari atas ke bawah: hero, habis ini, rel, ritme, jelajah, penutup`, a.urut.every((v) => v !== null) && a.urut.every((v, i) => i === 0 || v > a.urut[i - 1]), a.urut);
    P.cek(`A ${w}: tiket selebar sapaan dan angka (tepi kiri dan kanan sama)`, !!a.tiket && !!a.hero && hampir(a.tiket.kiri, a.hero.kiri, 1) && hampir(a.tiket.kanan, a.hero.kanan, 1), { tiket: a.tiket, hero: a.hero });
    P.cek(`A ${w}: rel, bara, dan bagian lain berhenti di tepi kanan konten (tidak meluber)`, !!a.rel && !!a.bara && !!a.hero && hampir(a.rel.kanan, a.hero.kanan, 1) && a.bara.kanan <= a.hero.kanan + 1 && a.lewat.length === 0, { rel: a.rel?.kanan, bara: a.bara?.kanan, hero: a.hero?.kanan, lewat: a.lewat });
    // Tanpa patok kolom, grid kartu bara berkolom dua dan kolom keduanya terjepit sampai 38 px; tepi
    // kanannya tetap rapi, jadi pemeriksaan luberan di atas saja tidak melihatnya.
    P.cek(`A ${w}: kartu bara satu kolom selebar kartunya (tidak ada kolom kedua yang terjepit)`, a.kolomBara.trim().split(/\s+/).length === 1, a.kolomBara);
    P.cek(`A ${w}: halaman tidak bisa digeser ke samping`, a.meluber <= 0, a.meluber);
    P.cek(`A ${w}: tanpa galat konsol (selain gerutan driver)`, s.konsol.filter(bukanGerutan).length === 0, s.konsol.filter(bukanGerutan));
    if (process.env.FOTO) await page.screenshot({ path: `${process.env.FOTO}/dasbor-${w}.png` });
    await s.tutup();
  }
}

/* ------------------------------------------------ B rel bahasa */
if (jalan("B")) {
  const info = (page) => page.evaluate(() => [...document.querySelectorAll(".ds-panel")].map((e) => ({
    buka: e.classList.contains("buka"), w: Math.round(e.getBoundingClientRect().width), nama: e.querySelector(".ds-panel-nama").textContent,
    inert: e.querySelector(".ds-panel-isi").inert, aria: e.querySelector(".ds-panel-tab").getAttribute("aria-expanded"),
    rasi: !!e.querySelector(".ds-panel-rasi svg"),
  })));
  const s = await buka(); const page = s.page;
  await keRel(page);
  const awal = await info(page);
  P.cek("B awal: tepat satu panel terbuka (yang pertama), lebar penuh, tidak inert, rasinya digambar", awal.filter((p) => p.buka).length === 1 && awal[0].buka && awal[0].w > 500 && !awal[0].inert && awal[0].rasi, awal);
  P.cek("B awal: panel lain 64 px (4rem), inert, tanpa rasi, aria-expanded false", awal.length >= 2 && awal.slice(1).every((p) => !p.buka && p.w === 64 && p.inert && !p.rasi && p.aria === "false") && awal[0].aria === "true", awal);
  // Rekam urutan panel terbuka per bingkai. Panel yang melebar menggeser panel lain ke bawah penunjuk
  // yang diam, dan peramban menjawabnya dengan pointerenter palsu: hover dulu melompat 3, 2, 3, 5
  // dan berhenti di panel yang tidak ditunjuk. Pemeriksaan keadaan akhir saja menangkapnya hanya
  // kadang-kadang (lulus sekali, lalu gagal lima kali berturut-turut), urutannya yang konsisten.
  await page.evaluate(() => {
    window.__rel = { luber: -999, urut: [] };
    document.addEventListener("pointermove", (e) => { window.__pos = [e.clientX, e.clientY]; }, true);
    const t0 = performance.now();
    const f = () => {
      const rak = document.querySelector(".ds-rel-rak").getBoundingClientRect();
      const ps = [...document.querySelectorAll(".ds-panel")];
      window.__rel.luber = Math.max(window.__rel.luber, Math.round(ps[ps.length - 1].getBoundingClientRect().right - rak.right));
      const a = ps.map((p) => (p.classList.contains("buka") ? "B" : "-")).join("");
      if (window.__rel.urut[window.__rel.urut.length - 1] !== a) window.__rel.urut.push(a);
      if (performance.now() - t0 < 1000) requestAnimationFrame(f);
    };
    requestAnimationFrame(f);
  });
  await page.hover(".ds-panel:nth-child(3) .ds-panel-tab");
  await tunggu(page, 1100);
  const rekam = await page.evaluate(() => window.__rel);
  const pola = (k, n) => Array.from({ length: n }, (_, i) => (i === k ? "B" : "-")).join("");
  P.cek("B hover tab ketiga: panel terbuka berpindah LANGSUNG dari pertama ke ketiga, tanpa lompatan perantara", JSON.stringify(rekam.urut) === JSON.stringify([pola(0, awal.length), pola(2, awal.length)]), rekam.urut);
  P.cek("B hover tab ketiga: panel terakhir tidak pernah melewati tepi kanan rak selama transisi", rekam.luber <= 0, rekam.luber);
  const hover = await info(page);
  P.cek("B mouse di atas panel ketiga: ia terbuka, yang lain tertutup", hover.length >= 3 && hover.filter((p) => p.buka).length === 1 && hover[2].buka && hover[2].w > 500 && hover[2].rasi && !hover[0].buka, hover);
  // Deterministik, tidak bergantung pada pewaktu peramban (urutan di atas bisa lolos kebetulan):
  // kirim pointerout/pointerover sintetis ke tab kedua dengan koordinat SAMA seperti yang dikirim
  // peramban saat panel bergeser di bawah penunjuk diam. React membaca pasangan itu sebagai
  // pointerenter. Yang palsu tidak boleh memindahkan hover; yang berkoordinat beda (gerakan nyata) harus.
  const palsu = await page.evaluate(async () => {
    const [x, y] = window.__pos;
    const t2 = document.querySelector(".ds-panel:nth-child(2) .ds-panel-tab");
    const t3 = document.querySelector(".ds-panel:nth-child(3) .ds-panel-tab");
    const terbuka = () => [...document.querySelectorAll(".ds-panel")].map((p) => (p.classList.contains("buka") ? "B" : "-")).join("");
    const masuk = (dari, ke, cx, cy) => {
      const ev = (jenis, rel) => new PointerEvent(jenis, { bubbles: true, composed: true, pointerType: "mouse", clientX: cx, clientY: cy, relatedTarget: rel });
      dari.dispatchEvent(ev("pointerout", ke));
      ke.dispatchEvent(ev("pointerover", dari));
    };
    const dua = () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
    masuk(t3, t2, x, y);
    await dua();
    const sesudahPalsu = terbuka();
    masuk(t3, t2, x + 3, y);
    await dua();
    return { sesudahPalsu, sesudahNyata: terbuka(), pos: [x, y] };
  });
  P.cek("B pointerenter palsu (koordinat sama) tidak memindahkan hover, yang berkoordinat beda (gerakan nyata) memindahkannya",
    palsu.sesudahPalsu === pola(2, awal.length) && palsu.sesudahNyata === pola(1, awal.length), palsu);
  await page.mouse.move(5, 5); await tunggu(page, 300);
  await page.focus(".ds-panel:nth-child(2) .ds-panel-tab"); await tunggu(page, 900);
  const fokus = await info(page);
  P.cek("B fokus papan ketik pada tab kedua membukanya", fokus.filter((p) => p.buka).length === 1 && fokus[1].buka && fokus[1].aria === "true", fokus);
  await page.click(".ds-panel:nth-child(1) .ds-panel-tab"); await page.mouse.move(5, 5); await tunggu(page, 900);
  const klik = await info(page);
  P.cek("B klik tab pertama membukanya lagi", klik[0].buka && klik.filter((p) => p.buka).length === 1, klik);
  // Gerak penuh memuai bertahap: sampel di tengah perpindahan lebarnya di antara 64 dan lebar penuh.
  await page.mouse.move(5, 5);
  const tengah = await page.evaluate(async () => {
    const tab = document.querySelector(".ds-panel:nth-child(4) .ds-panel-tab") ?? document.querySelector(".ds-panel:nth-child(3) .ds-panel-tab");
    const panel = tab.closest(".ds-panel");
    tab.focus();
    await new Promise((r) => setTimeout(r, 140));
    return panel.getBoundingClientRect().width;
  });
  P.cek(`B gerak penuh: 140 ms sesudah pindah, lebar panel baru masih di tengah jalan (${Math.round(tengah)} px, antara 64 dan penuh)`, tengah > 70 && tengah < 880, tengah);
  await s.tutup();

  const m = await buka({ gerak: "mati" });
  await keRel(m.page);
  await m.page.focus(".ds-panel:nth-child(3) .ds-panel-tab"); await tunggu(m.page, 60);
  const mati = await m.page.evaluate(() => ({ w: Math.round(document.querySelector(".ds-panel:nth-child(3)").getBoundingClientRect().width), buka: document.querySelector(".ds-panel:nth-child(3)").classList.contains("buka") }));
  P.cek("B gerak mati: panel langsung selebar penuh (tanpa memuai bertahap)", mati.buka && mati.w > 500, mati);
  await m.tutup();
}

/* ------------------------------------------------ C angka hidup */
if (jalan("C")) {
  const ambilData = (page) => page.evaluate(async () => {
    const j = await (await fetch("/api/dasbor", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR ?? "" } })).json();
    return { hari: j.xp_hari_ini, streak: j.streak, level: j.level };
  });
  const angkaDariTeks = (t) => Number(String(t).replace(/\./g, "").replace(/,/g, "."));
  /** Muat ulang dengan perekam: tiap penulisan ke tiga angka masuk `window.__rekam` sebagai [indeks, teks]. */
  const rekamDari = async (opsi) => {
    const s = await buka({ ...opsi, tunggu: ".ds-stat-angka" });
    await s.page.addInitScript(() => {
      window.__rekam = [];
      const pasang = () => {
        const el = document.querySelectorAll(".ds-stat-angka .angka-hidup > span:first-child");
        if (el.length < 3) return false;
        el.forEach((e, i) => {
          window.__rekam.push([i, e.textContent]);
          new MutationObserver(() => window.__rekam.push([i, e.textContent])).observe(e, { childList: true, characterData: true, subtree: true });
        });
        return true;
      };
      new MutationObserver((_, o) => { if (pasang()) o.disconnect(); }).observe(document, { childList: true, subtree: true });
    });
    await s.page.reload({ waitUntil: "load" });
    await s.page.waitForSelector(".ds-stat-angka", { timeout: 30000 });
    await tunggu(s.page, 2000);
    const rekam = await s.page.evaluate(() => window.__rekam);
    const data = await ambilData(s.page);
    const sr = await s.page.evaluate(() => [...document.querySelectorAll(".ds-stat-angka .ds-sr")].map((e) => e.textContent));
    const aria = await s.page.evaluate(() => [...document.querySelectorAll(".ds-stat-angka .angka-hidup > span:first-child")].map((e) => e.getAttribute("aria-hidden")));
    const akhir = await s.page.evaluate(() => [...document.querySelectorAll(".ds-stat-angka .angka-hidup > span:first-child")].map((e) => e.textContent));
    await s.tutup();
    return { rekam, data, sr, aria, akhir, harap: [idr(data.hari), idr(data.streak), idr(data.level)] };
  };
  const urutan = (rekam, i) => rekam.filter((r) => r[0] === i).map((r) => r[1]);

  const p = await rekamDari({ gerak: "penuh" });
  P.cek("C gerak penuh: sesudah animasi, tiga angka TEPAT sama dengan data (/api/dasbor)", p.akhir.join("|") === p.harap.join("|"), { akhir: p.akhir, harap: p.harap });
  P.cek("C pembaca layar: angka akhir ada sebagai teks, yang berubah-ubah aria-hidden", p.sr.join("|") === p.harap.join("|") && p.aria.every((a) => a === "true"), { sr: p.sr, aria: p.aria });
  const urut = [0, 1, 2].map((i) => urutan(p.rekam, i));
  P.cek("C gerak penuh: tiap angka berakhir di nilai akhirnya dan urutan nilainya tidak pernah turun", urut.every((u, i) => u.length >= 1 && u[u.length - 1] === p.harap[i] && u.every((v, k) => k === 0 || angkaDariTeks(v) >= angkaDariTeks(u[k - 1]))), urut);
  const besar = [0, 1, 2].filter((i) => angkaDariTeks(p.harap[i]) >= 5);
  P.cek(`C gerak penuh: angka bernilai besar benar-benar berangkat dari bawah nilainya (kandidat ${besar.length}) dan lewat beberapa nilai`, besar.length > 0 && besar.every((i) => angkaDariTeks(urut[i][0]) < angkaDariTeks(p.harap[i]) && new Set(urut[i]).size >= 3), besar.map((i) => urut[i]));

  for (const [judul, opsi] of [["gerak mati", { gerak: "mati" }], ["gerak halus", { gerak: "halus" }], ["prefers-reduced-motion", { gerak: "penuh", reduce: true }]]) {
    const m = await rekamDari(opsi);
    const u = [0, 1, 2].map((i) => [...new Set(urutan(m.rekam, i))]);
    P.cek(`C ${judul}: angka hanya pernah tertulis sebagai angka akhir (tanpa hitungan naik)`, u.every((v, i) => v.length === 1 && v[0] === m.harap[i]), { u, harap: m.harap });
  }
}

/* ------------------------------------------------ D kontras */
if (jalan("D")) {
  for (const tema of TEMA) {
    const s = await buka({ tema, gerak: "mati" }); const page = s.page;
    await tunggu(page, 700);
    const ambang = tema === "kontras" ? 7 : 4.5;
    for (const [nama, sel] of [
      ["sapaan", ".ds-sapa"], ["angka hari ini", ".ds-stat-angka"], ["satuan angka", ".ds-stat-satuan"], ["keterangan angka", ".ds-stat-ket"],
      ["judul tiket", ".ds-tiket-isi h2"], ["alasan tiket", ".ds-tiket-alasan"], ["judul langkah", ".ds-langkah-judul"], ["keterangan langkah", ".ds-langkah-ket"],
    ]) {
      const r = await rasioTeks(page, sel);
      P.cek(`D ${tema}: ${nama} "${r.teks}" >= ${ambang}:1 (terukur ${r.rasio}) dan tanpa peredupan opacity (efektif ${r.opasitas})`, r.rasio >= ambang && r.opasitas >= 0.999, r);
    }
    await keRel(page);
    for (const [nama, sel, i] of [["nama panel tertutup", ".ds-panel:not(.buka) .ds-panel-nama", 0], ["persen panel tertutup", ".ds-panel:not(.buka) .ds-panel-persen", 0], ["persen panel terbuka", ".ds-panel.buka .ds-panel-ket b", 0], ["tautan panel terbuka", ".ds-panel.buka .ds-panel-tautan", 0]]) {
      const r = await rasioTeks(page, sel, i);
      P.cek(`D ${tema}: ${nama} "${r.teks}" >= ${ambang}:1 (terukur ${r.rasio}) dan tanpa peredupan opacity (efektif ${r.opasitas})`, r.rasio >= ambang && r.opasitas >= 0.999, r);
    }
    if (process.env.FOTO) await page.screenshot({ path: `${process.env.FOTO}/dasbor-kontras-${tema}.png` });
    await s.tutup();
  }
}

/* ------------------------------------------------ E papan ketik */
if (jalan("E")) {
  const s = await buka({ gerak: "mati" }); const page = s.page;
  await keRel(page);
  await page.focus(".ds-panel:nth-child(1) .ds-panel-tab");
  const rinci = [];
  for (let n = 0; n < 14; n++) {
    const d = await page.evaluate(() => {
      const a = document.activeElement;
      if (!a?.closest(".ds-rel")) return null;
      const r = a.getBoundingClientRect();
      const cs = getComputedStyle(a);
      const tepat = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
      return {
        nama: (a.textContent || "").trim().slice(0, 18), kelas: a.className.slice(0, 18),
        terlihat: r.width > 0 && r.height > 0 && r.right > 0 && r.left < window.innerWidth,
        tidakTertutup: !!tepat && a.contains(tepat),
        cincin: cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) >= 2,
        panelTerbuka: a.closest(".ds-panel")?.classList.contains("buka") ?? false,
      };
    });
    if (!d) break;
    rinci.push(d);
    await page.keyboard.press("Tab");
  }
  const tab = rinci.filter((r) => r.kelas.startsWith("ds-panel-tab"));
  const tautan = rinci.filter((r) => r.kelas.startsWith("ds-panel-tautan"));
  P.cek(`E setiap perhentian terlihat penuh, tidak tertutup, bercincin fokus (${rinci.length} perhentian)`, rinci.length >= 5 && rinci.every((r) => r.terlihat && r.tidakTertutup && r.cincin), rinci.filter((r) => !(r.terlihat && r.tidakTertutup && r.cincin)));
  P.cek("E tab panel yang sedang difokus selalu berpanel terbuka (fokus membuka)", tab.length >= 1 && tab.every((r) => r.panelTerbuka), tab);
  P.cek("E tautan hanya terjangkau di panel yang terbuka (isi panel tertutup inert)", tautan.length >= 1 && tautan.every((r) => r.panelTerbuka), tautan);
  await s.tutup();
}

/* ------------------------------------------------ F hover */
if (jalan("F")) {
  const s = await buka({ gerak: "penuh" }); const page = s.page;
  await tunggu(page, 700);
  await page.hover(".ds-tiket"); await tunggu(page, 700);
  const t = await page.evaluate(() => { const c = getComputedStyle(document.querySelector(".ds-tiket")); return { translate: c.translate, transform: c.transform }; });
  P.cek("F tiket disorot: terangkat lewat `translate` (-2 px) dan `transform` tetap kosong", /-2px/.test(t.translate) && t.transform === "none", t);
  await page.evaluate(() => document.querySelector(".ds-antrean").scrollIntoView({ block: "center", behavior: "instant" })); await tunggu(page, 400);
  await page.hover(".ds-langkah"); await tunggu(page, 700);
  const l = await page.evaluate(() => { const c = getComputedStyle(document.querySelector(".ds-langkah")); return { translate: c.translate, transform: c.transform }; });
  P.cek("F kartu langkah disorot: terangkat lewat `translate`, `transform` kosong", /-2px/.test(l.translate) && l.transform === "none", l);
  await s.tutup();
  const m = await buka({ gerak: "mati" });
  await tunggu(m.page, 400);
  await m.page.hover(".ds-tiket"); await tunggu(m.page, 400);
  const x = await m.page.evaluate(() => getComputedStyle(document.querySelector(".ds-tiket")).transitionDuration);
  P.cek("F gerak mati: tidak ada transisi pada tiket", /^0s(, 0s)*$/.test(x), x);
  await m.tutup();
}

/* ------------------------------------------------ G isi sama dengan data */
if (jalan("G")) {
  const s = await buka({ gerak: "mati" }); const page = s.page;
  await tunggu(page, 800);
  const g = await page.evaluate(async () => {
    const j = await (await fetch("/api/dasbor", { headers: { "X-Belajar-Token": window.TOKEN_BELAJAR ?? "" } })).json();
    const sisa = j.langkah.slice(1);
    const harapKartu = Math.min(3, sisa.length) + (j.tantangan ? 1 : 0);
    const posisi = j.posisi ? j.posisi.key : null;
    const jalani = j.bahasa.map((b, i) => ({ b, i })).filter((x) => x.b.persen > 0);
    jalani.sort((x, y) => (Number(y.b.key === posisi) - Number(x.b.key === posisi)) || (y.b.persen - x.b.persen) || (x.i - y.i));
    return {
      kartu: document.querySelectorAll(".ds-langkah").length, harapKartu,
      rel: [...document.querySelectorAll(".ds-panel-nama")].map((e) => e.textContent), harapRel: jalani.slice(0, 6).map((x) => x.b.label),
      judulTiket: document.querySelector(".ds-tiket-isi h2")?.textContent ?? "", harapTiket: (j.langkah[0]?.judul ?? "").replace(/^\s*\d+\.\s*/, ""),
      teks: document.querySelector(".ds-meja").innerText, lencana: document.querySelector(".ds-stat-lencana")?.textContent ?? "", harapLencana: `${j.badge_dimiliki}/${j.badge_total} lencana`,
    };
  });
  P.cek("G jumlah kartu 'Habis ini' = tiga langkah teratas ditambah tantangan", g.kartu === g.harapKartu, g);
  P.cek("G urutan rel = dijalani, posisi sekarang dulu, lalu persen terbesar (maksimal enam)", JSON.stringify(g.rel) === JSON.stringify(g.harapRel), { rel: g.rel, harap: g.harapRel });
  P.cek("G judul tiket = judul langkah pertama tanpa nomor, tanda lencana = data", g.judulTiket === g.harapTiket && g.lencana === g.harapLencana, { t: g.judulTiket, h: g.harapTiket, l: g.lencana });
  P.cek("G tidak ada tulisan rusak (undefined, NaN, null, [object], dash)", !/undefined|NaN|null|\[object|\u2014|\u2013/.test(g.teks), g.teks.slice(0, 200));
  await s.tutup();
}

/* ------------------------------------------------ H profil baru */
if (jalan("H")) {
  const s = await mulai({ lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/dasbor", tunggu: ".tbl-utama.tbl-besar" });
  const h = await s.page.evaluate(() => ({ meja: document.querySelectorAll(".ds-meja").length, rel: document.querySelectorAll(".ds-rel").length, stat: document.querySelectorAll(".ds-stat").length }));
  P.cek("H profil baru (XP 0): memakai layar mulai, tanpa susunan hero, rel, atau angka hari ini", h.meja === 0 && h.rel === 0 && h.stat === 0, h);
  await s.tutup();
}

P.selesai();
