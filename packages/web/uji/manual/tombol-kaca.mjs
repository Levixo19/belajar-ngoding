/* Pemeriksaan tombol kaca (`.tbl-kaca` di gaya.css + `komponen/FilterKaca.tsx`), diukur di
 * peramban pada dua tombol utama dasbor: chip "Lanjutkan" (kartu Lanjutkan, butuh profil
 * BERPROGRES) dan chip "Mulai" (layar mulai, butuh profil BARU dengan XP 0).
 *
 *   A  struktur: satu filter di DOM, tersembunyi dari pembaca layar, tombol memakainya,
 *      bentuk pil, dan kaca tidak menggeser tata letak
 *   B  gerak: skala saat disorot lewat properti `scale` (BUKAN `transform`, milik umpan
 *      tekan WAAPI), mati di tingkat mati dan `prefers-reduced-motion`
 *   C  kontras huruf tombol dari piksel sungguhan, tiga tema berkaca, diam dan disorot
 *   D  tema kontras tinggi: kuningan pekat tanpa kaca
 *   E  chip "Mulai" di layar mulai (JALANKAN terhadap server berprofil BARU)
 *
 *   # bagian A sampai D: server berprofil berprogres
 *   HANYA=A,B,C,D BELAJAR_URL=http://127.0.0.1:7789/ node uji/manual/tombol-kaca.mjs
 *   # bagian E: server berprofil baru (XP 0)
 *   HANYA=E BELAJAR_URL=http://127.0.0.1:7788/ node uji/manual/tombol-kaca.mjs
 *
 * Jalankan terhadap server berprofil SEMENTARA (lihat `lib.mjs`); permintaan tulis dicegat dan
 * dihitung gagal. Peringatan "GPU stall due to ReadPixels" datang dari pengambilan tangkapan layar
 * oleh SwiftShader dan disaring dari pemeriksaan konsol.
 */

import { URL_DASAR, lum, mulai, pemeriksa } from "./lib.mjs";

if (new URL(URL_DASAR).port === "7777") {
  console.error("Menolak jalan terhadap port 7777 (server pemilik).");
  process.exit(2);
}

const P = pemeriksa("Tombol kaca");
const jalan = (huruf) => !process.env.HANYA || process.env.HANYA.split(",").includes(huruf);
const TEMA = ["gelap", "malam", "terang"];
const bukanGerutan = (k) => !/GPU stall|GL Driver Message/.test(k);
const tunggu = (page, ms) => page.waitForTimeout(ms);
const hampir = (a, b, t) => Math.abs(a - b) <= t;

const buka = (opsi = {}) => mulai({
  lebar: 1440, tinggi: 900, tema: "gelap", gerak: "penuh", hash: "#/dasbor", tunggu: ".lanjutkan-tbl", ...opsi,
});

const bacaWarna = (c) => {
  const n = c.match(/[\d.]+/g).slice(0, 3).map(Number);
  return c.startsWith("color(") ? n.map((v) => v * 255) : n; // `color(srgb ...)` berkomponen 0..1
};
async function rasioTerburuk(page, kotak, warnaTeks) {
  const png = await page.screenshot({ clip: kotak, type: "png" });
  const L = await page.evaluate(async ([b64]) => {
    const im = new Image(); im.src = "data:image/png;base64," + b64; await im.decode();
    const c = document.createElement("canvas"); c.width = im.width; c.height = im.height;
    const x = c.getContext("2d", { willReadFrequently: true }); x.drawImage(im, 0, 0);
    const d = x.getImageData(0, 0, c.width, c.height).data;
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    const a = [];
    for (let i = 0; i < d.length; i += 4) a.push(0.2126 * f(d[i]) + 0.7152 * f(d[i + 1]) + 0.0722 * f(d[i + 2]));
    a.sort((p, q) => p - q);
    const at = (pr) => a[Math.min(a.length - 1, Math.floor((a.length * pr) / 100))];
    return { gelap: at(1), terang: at(99) };
  }, [png.toString("base64")]);
  const lt = lum(warnaTeks);
  const r = (l) => (Math.max(lt, l) + 0.05) / (Math.min(lt, l) + 0.05);
  return Math.min(r(L.gelap), r(L.terang));
}

/** Kotak huruf pertama di dalam tombol (Range pada simpul teksnya), dan warna teks tombol. */
const teksTombol = (page, selektor) => page.evaluate((sel) => {
  const el = document.querySelector(sel);
  const teks = [...el.querySelectorAll("*")].find((n) => n.childNodes.length && [...n.childNodes].some((c) => c.nodeType === 3 && c.textContent.trim()))
    ?? el;
  const r = document.createRange(); r.selectNodeContents(teks);
  const b = r.getBoundingClientRect();
  return { kotak: { x: b.x, y: b.y, width: b.width, height: b.height }, warna: getComputedStyle(teks).color, teks: teks.textContent.trim() };
}, selektor);

async function ukurKontras(page, selektor, keadaan) {
  const t = await teksTombol(page, selektor);
  await page.evaluate(() => {
    const st = document.createElement("style"); st.id = "uji-teks-transparan";
    st.textContent = ".tbl-kaca, .tbl-kaca * { color: transparent !important; text-shadow: none !important; }";
    document.head.appendChild(st);
  });
  const r = await rasioTerburuk(page, t.kotak, bacaWarna(t.warna));
  await page.evaluate(() => document.getElementById("uji-teks-transparan")?.remove());
  return { rasio: Math.round(r * 100) / 100, teks: t.teks, keadaan };
}

/* ------------------------------------------------ A struktur dan tata letak */
if (jalan("A")) {
  for (const tema of TEMA) {
    const s = await buka({ tema }); const page = s.page;
    await tunggu(page, 500);
    const a = await page.evaluate(() => {
      const svg = document.querySelector(".tbl-kaca-filter");
      const f = document.getElementById("tbl-kaca");
      const tombol = [...document.querySelectorAll(".tbl-kaca")];
      const cs = (e) => getComputedStyle(e);
      const t = tombol[0];
      // Tanpa tombol berkaca (kelasnya terbuang) pemeriksaan di bawah harus GAGAL, bukan mati karena TypeError.
      if (!t) return { jumlahFilter: document.querySelectorAll("#tbl-kaca").length, jumlahSvg: document.querySelectorAll(".tbl-kaca-filter").length, jumlahTombol: 0, bf: [], dengan: [], tanpa: [], turbulensi: false, svgUkuran: [], bg: "", bgGambar: "" };
      const b = t.getBoundingClientRect();
      const ukur = () => { const r = t.getBoundingClientRect(); return [Math.round(r.left * 10) / 10, Math.round(r.top * 10) / 10, Math.round(r.width * 10) / 10, Math.round(r.height * 10) / 10]; };
      // Gaya dibaca SEBELUM kelas dicopot: sesudahnya `background` bertransisi dan terbaca
      // di tengah jalan (warna `oklab` tanpa alfa). Pemeriksaan tembus pandang pernah gagal karenanya.
      const gaya = {
        transisi: cs(t).transitionProperty, bg: cs(t).backgroundColor, bgGambar: cs(t).backgroundImage.slice(0, 40),
        bayang: cs(t).boxShadow.length, pos: cs(t).position, isolasi: cs(t).isolation,
        radius: parseFloat(cs(t).borderTopLeftRadius),
      };
      const dengan = ukur();
      t.classList.remove("tbl-kaca");
      const tanpa = ukur();
      t.classList.add("tbl-kaca");
      return {
        jumlahFilter: document.querySelectorAll("#tbl-kaca").length, jumlahSvg: document.querySelectorAll(".tbl-kaca-filter").length,
        svgAria: svg?.getAttribute("aria-hidden"), svgUkuran: [svg?.getAttribute("width"), svg?.getAttribute("height")],
        svgPos: svg && cs(svg).position, svgPE: svg && cs(svg).pointerEvents,
        jumlahTombol: tombol.length, bf: tombol.map((e) => cs(e).backdropFilter),
        tinggi: b.height, dengan, tanpa, ...gaya,
        turbulensi: !!f?.querySelector("feTurbulence"), geser: f?.querySelector("feDisplacementMap")?.getAttribute("scale"),
      };
    });
    P.cek(`A ${tema}: tepat satu filter #tbl-kaca di DOM, dari komponen yang dipasang sekali`, a.jumlahFilter === 1 && a.jumlahSvg === 1 && a.turbulensi, [a.jumlahFilter, a.jumlahSvg]);
    P.cek(`A ${tema}: filter tersembunyi dari pembaca layar, tidak menangkap penunjuk, 0x0 tetapi digambar (bukan display none)`,
      a.svgAria === "true" && a.svgPE === "none" && a.svgPos === "absolute" && a.svgUkuran.join() === "0,0", a);
    P.cek(`A ${tema}: tombol memakai pembiasan lewat url(#tbl-kaca)`, a.jumlahTombol >= 1 && a.bf.length >= 1 && a.bf.every((v) => /url\(.*#tbl-kaca/.test(v)), a.bf);
    P.cek(`A ${tema}: pil (radius penuh), bertinta tembus pandang, ada bevel, terisolasi`,
      a.radius >= a.tinggi / 2 && /\/ 0?\.\d+\)$/.test(a.bg) && a.bgGambar.startsWith("linear-gradient") && a.bayang > 120 && a.pos === "relative" && a.isolasi === "isolate",
      { radius: a.radius, tinggi: a.tinggi, bg: a.bg, bayang: a.bayang });
    P.cek(`A ${tema}: pergeseran pembiasan kecil (tombol setinggi 44 sampai 52 px, bukan 70)`, Number(a.geser) > 0 && Number(a.geser) <= 30, a.geser);
    P.cek(`A ${tema}: kaca tidak menggeser tombol (kotak sama dengan atau tanpa kelas)`, a.dengan.length === 4 && a.dengan.every((v, i) => hampir(v, a.tanpa[i], 0.6)), [a.dengan, a.tanpa]);
    P.cek(`A ${tema}: tanpa galat konsol (selain gerutan driver)`, s.konsol.filter(bukanGerutan).length === 0, s.konsol.filter(bukanGerutan));
    if (process.env.FOTO) {
      const b = await page.evaluate(() => { const r = document.querySelector(".tbl-kaca").getBoundingClientRect(); return [r.left, r.top]; });
      await page.screenshot({ path: `${process.env.FOTO}/tombol-${tema}.png`, clip: { x: Math.max(0, b[0] - 40), y: Math.max(0, b[1] - 40), width: 640, height: 140 } });
    }
    await s.tutup();
  }
}

/* ------------------------------------------------ B gerak: scale, bukan transform */
if (jalan("B")) {
  const s = await buka({ gerak: "penuh" }); const page = s.page;
  await tunggu(page, 400);
  const awal = await page.evaluate(() => { const c = getComputedStyle(document.querySelector(".lanjutkan-tbl")); return { scale: c.scale, transform: c.transform, transisi: c.transitionProperty }; });
  P.cek("B diam: skala 1 (tidak ada), tidak ada transform", (awal.scale === "none" || awal.scale === "1") && awal.transform === "none", awal);
  P.cek("B transisi memuat scale dan TIDAK memuat transform (umpan tekan WAAPI memegang transform)", /\bscale\b/.test(awal.transisi) && !/\btransform\b/.test(awal.transisi), awal.transisi);
  await page.hover(".lanjutkan-tbl");
  await tunggu(page, 700);
  const sorot = await page.evaluate(() => { const c = getComputedStyle(document.querySelector(".lanjutkan-tbl")); return { scale: c.scale, transform: c.transform }; });
  P.cek("B disorot di gerak penuh: scale 1,04 dan transform tetap kosong", Number(sorot.scale) === 1.04 && sorot.transform === "none", sorot);
  await s.tutup();

  for (const [judul, opsi] of [["gerak mati", { gerak: "mati" }], ["prefers-reduced-motion", { gerak: "penuh", reduce: true }]]) {
    const m = await buka(opsi);
    await tunggu(m.page, 400);
    await m.page.hover(".lanjutkan-tbl");
    await tunggu(m.page, 500);
    const c = await m.page.evaluate(() => getComputedStyle(document.querySelector(".lanjutkan-tbl")).scale);
    P.cek(`B ${judul}: disorot TIDAK membesar`, c === "none" || Number(c) === 1, c);
    await m.tutup();
  }
}

/* ------------------------------------------------ C kontras huruf tombol */
if (jalan("C")) {
  for (const tema of TEMA) {
    const s = await buka({ tema, gerak: "mati" }); const page = s.page;
    await tunggu(page, 500);
    const diam = await ukurKontras(page, ".lanjutkan-tbl", "diam");
    await page.hover(".lanjutkan-tbl");
    await tunggu(page, 300);
    const sorot = await ukurKontras(page, ".lanjutkan-tbl", "disorot");
    const terburuk = Math.min(diam.rasio, sorot.rasio);
    // 5,0 (4,5 mutlak ditambah margin 0,5): yang di belakang tombol berupa sampul generatif yang berganti per langkah.
    P.cek(`C ${tema}: huruf "${diam.teks}" >= 5,0:1 diam dan disorot (terburuk ${terburuk})`, terburuk >= 5.0, { diam: diam.rasio, sorot: sorot.rasio });
    await s.tutup();
  }
}

/* ------------------------------------------------ D tema kontras tinggi */
if (jalan("D")) {
  const s = await buka({ tema: "kontras", gerak: "mati" }); const page = s.page;
  await tunggu(page, 400);
  const k = await page.evaluate(() => {
    const cs = getComputedStyle(document.querySelector(".lanjutkan-tbl"));
    return { bg: cs.backgroundColor, bgGambar: cs.backgroundImage, bf: cs.backdropFilter, bayang: cs.boxShadow };
  });
  P.cek("D kontras: kuningan pekat tanpa kaca (alfa 1, tanpa backdrop-filter, tanpa bayangan dalam)",
    /^rgb\(/.test(k.bg) && (k.bf === "none" || k.bf === "") && k.bayang === "none", k);
  const r = await ukurKontras(page, ".lanjutkan-tbl", "diam");
  P.cek(`D kontras: huruf tombol >= 7:1 (terukur ${r.rasio})`, r.rasio >= 7, r.rasio);
  await s.tutup();
}

/* ------------------------------------------------ E chip "Mulai" (profil BARU, XP 0) */
if (jalan("E")) {
  for (const tema of TEMA) {
    const s = await buka({ tema, gerak: "mati", tunggu: ".tbl-utama.tbl-besar" }); const page = s.page;
    await tunggu(page, 500);
    const a = await page.evaluate(() => {
      const t = document.querySelector(".tbl-besar.tbl-kaca");
      // Tanpa chip berkaca (kelasnya terbuang) pemeriksaan harus GAGAL, bukan mati karena TypeError.
      if (!t) return { teks: "(tidak ada)", bf: "", utama: false, jumlah: 0 };
      const cs = getComputedStyle(t);
      return { teks: t.textContent.trim(), bf: cs.backdropFilter, utama: t.classList.contains("tbl-utama"), jumlah: document.querySelectorAll(".tbl-utama.tbl-kaca").length };
    });
    P.cek(`E ${tema}: chip "${a.teks}" tetap tbl-utama, satu-satunya tombol utama berkaca di layar ini, dengan pembiasan`,
      a.teks.startsWith("Mulai") && a.utama && a.jumlah === 1 && /url\(.*#tbl-kaca/.test(a.bf), a);
    const r = a.jumlah === 0 ? { rasio: 0 } : await ukurKontras(page, ".tbl-besar.tbl-kaca", "diam");
    P.cek(`E ${tema}: huruf chip Mulai >= 5,0:1 (terukur ${r.rasio})`, r.rasio >= 5.0, r.rasio);
    await s.tutup();
  }
}

P.selesai();
