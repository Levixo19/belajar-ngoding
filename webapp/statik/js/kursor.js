/* Reticle teleskop yang mengikuti kursor dan MENGUNCI sasaran.
 *
 * Empat braket sudut di sekitar ujung penunjuk. Saat penunjuk berada di atas
 * sesuatu yang bisa diklik, braketnya pindah membingkai elemen itu: tanda
 * "ini sasaranmu" yang sama dengan penanda bintang berikutnya di peta rasi,
 * jadi kursor dan peta berbicara dengan satu bahasa bentuk.
 *
 * Aturan yang mengikat (dari riset aksesibilitas, lihat AGENTS.md):
 *   * kursor ASLI tidak pernah disembunyikan: ukuran dan kontras pilihan
 *     pengguna di sistem operasi tetap berlaku; reticle cuma tambahan;
 *   * hanya untuk penunjuk halus (mouse/trackpad), pointer-events: none,
 *     aria-hidden;
 *   * tingkatGerak() yang memutuskan: "mati" = reticle tidak ada sama
 *     sekali; "halus" = reticle melompat tanpa pegas dan tanpa jejak;
 *     "penuh" = pegas + jejak meteor tipis saat penunjuk bergerak;
 *   * reticle juga mengunci elemen yang difokus lewat papan ketik, supaya
 *     pengguna Tab mendapat penanda yang sama dengan pengguna mouse;
 *   * hanya transform yang digerakkan (tidak ada width/height per frame);
 *     rAF berhenti saat reticle sudah diam di tempatnya. */

import { tingkatGerak, saatGerakBerubah } from "./gerak.js";

const INTERAKTIF = "a[href], button:not([disabled]), summary, select, label[for], "
  + "[role='button'], [role='tab'], input[type='range'], input[type='checkbox'], "
  + "input[type='radio'], .rasi-bintang";
const MENGETIK = "input:not([type='range']):not([type='checkbox']):not([type='radio']), "
  + "textarea, [contenteditable='true'], .editor";
const LUAS_MAKS = 170000;      // px²: kartu sebesar ini tidak dibingkai
const BEBAS = 22, JARAK = 5, UMUR_JEJAK = 180;

export function nyalakanKursor() {
  if (typeof matchMedia !== "function" || !matchMedia("(pointer: fine)").matches) return;

  let akar = null, sudut = [], kanvas = null;
  let px = -200, py = -200, terakhirGerak = 0;
  let sasaran = null;
  const kini = { x: -200, y: -200, w: BEBAS, h: BEBAS };
  let raf = 0;
  let jejak = [];
  let rectLalu = "";

  function pasang() {
    if (akar) return;
    akar = document.createElement("div");
    akar.className = "kursor kursor-sembunyi";
    akar.setAttribute("aria-hidden", "true");
    sudut = [0, 1, 2, 3].map(() => {
      const s = document.createElement("span");
      s.className = "kursor-sudut";
      akar.appendChild(s);
      return s;
    });
    kanvas = document.createElement("canvas");
    kanvas.className = "kursor-jejak";
    kanvas.setAttribute("aria-hidden", "true");
    document.body.append(kanvas, akar);
    ukurKanvas();
  }

  function lepas() {
    if (!akar) return;
    cancelAnimationFrame(raf);
    raf = 0;
    akar.remove(); kanvas.remove();
    akar = null; kanvas = null; sudut = [];
  }

  function ukurKanvas() {
    if (!kanvas) return;
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    kanvas.width = Math.round(innerWidth * dpr);
    kanvas.height = Math.round(innerHeight * dpr);
    kanvas.getContext("2d").setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function tujuan() {
    if (sasaran && !sasaran.isConnected) {      // elemennya sudah dilepas dari DOM
      sasaran = null;
      if (akar) akar.classList.remove("kursor-kunci");
    }
    if (sasaran) {
      const r = sasaran.getBoundingClientRect();
      if (r.width && r.height) {
        return { x: r.left - JARAK, y: r.top - JARAK, w: r.width + JARAK * 2, h: r.height + JARAK * 2 };
      }
    }
    return { x: px - BEBAS / 2, y: py - BEBAS / 2, w: BEBAS, h: BEBAS };
  }

  function gambarJejak(waktu) {
    const c = kanvas.getContext("2d");
    c.clearRect(0, 0, innerWidth, innerHeight);
    jejak = jejak.filter((t) => waktu - t.t < UMUR_JEJAK);
    if (jejak.length < 2) return false;
    const warna = getComputedStyle(document.body).getPropertyValue("--nyala").trim() || "#e4b96b";
    c.lineCap = "round";
    c.strokeStyle = warna;
    for (let i = 1; i < jejak.length; i++) {
      const a = jejak[i - 1], b = jejak[i];
      const umur = 1 - (waktu - b.t) / UMUR_JEJAK;
      c.globalAlpha = umur * 0.5;
      c.lineWidth = 0.5 + umur * 1.5;
      c.beginPath(); c.moveTo(a.x, a.y); c.lineTo(b.x, b.y); c.stroke();
    }
    c.globalAlpha = 1;
    return true;
  }

  function bingkai(waktu) {
    raf = 0;
    if (!akar) return;
    const t = tujuan();
    const pegas = tingkatGerak() === "penuh" ? 0.3 : 1;
    let diam = true;
    for (const k of ["x", "y", "w", "h"]) {
      const beda = t[k] - kini[k];
      kini[k] = Math.abs(beda) < 0.1 ? t[k] : kini[k] + beda * pegas;
      if (Math.abs(t[k] - kini[k]) > 0.1) diam = false;
    }
    const titik = [[kini.x, kini.y, 0], [kini.x + kini.w, kini.y, 90],
                   [kini.x + kini.w, kini.y + kini.h, 180], [kini.x, kini.y + kini.h, 270]];
    titik.forEach(([x, y, r], i) => {
      sudut[i].style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0) rotate(${r}deg)`;
    });
    let adaJejak = false;
    if (tingkatGerak() === "penuh") adaJejak = gambarJejak(waktu);
    else if (jejak.length) { jejak = []; kanvas.getContext("2d").clearRect(0, 0, innerWidth, innerHeight); }
    // Frame berhenti begitu reticle diam dan sasarannya tidak bergeser.
    // Guliran dan perubahan ukuran membangunkannya lagi (lihat di bawah):
    // penunjuk yang diam di atas sebuah tombol tidak boleh menyalakan 60
    // frame per detik tanpa henti.
    const rect = `${t.x.toFixed(1)},${t.y.toFixed(1)},${t.w.toFixed(1)},${t.h.toFixed(1)}`;
    const bergeser = rect !== rectLalu;
    rectLalu = rect;
    if (!diam || adaJejak || bergeser) raf = requestAnimationFrame(bingkai);
  }

  function bangunkan() { if (akar && !raf) raf = requestAnimationFrame(bingkai); }

  function kunci(el) {
    if (el) {
      const r = el.getBoundingClientRect();
      if (r.width * r.height > LUAS_MAKS) el = null;
    }
    sasaran = el;
    if (akar) akar.classList.toggle("kursor-kunci", !!el);
    bangunkan();
  }

  document.addEventListener("pointermove", (e) => {
    if (e.pointerType && e.pointerType !== "mouse" && e.pointerType !== "pen") return;
    if (!akar) return;
    px = e.clientX; py = e.clientY; terakhirGerak = performance.now();
    akar.classList.remove("kursor-sembunyi");
    if (tingkatGerak() === "penuh") jejak.push({ x: px, y: py, t: terakhirGerak });
    bangunkan();
  }, { passive: true });

  document.addEventListener("pointerover", (e) => {
    if (!akar || !(e.target instanceof Element)) return;
    akar.classList.toggle("kursor-ketik", !!e.target.closest(MENGETIK));
    kunci(e.target.closest(INTERAKTIF));
  });

  document.addEventListener("pointerdown", () => akar && akar.classList.add("kursor-tekan"));
  document.addEventListener("pointerup", () => akar && akar.classList.remove("kursor-tekan"));
  document.documentElement.addEventListener("mouseleave", () => {
    if (!akar) return;
    akar.classList.add("kursor-sembunyi");
    kunci(null);
  });
  document.addEventListener("focusout", (e) => { if (e.target === sasaran) kunci(null); });
  window.addEventListener("scroll", bangunkan, { passive: true, capture: true });

  document.addEventListener("focusin", (e) => {
    if (!akar || !(e.target instanceof Element)) return;
    if (performance.now() - terakhirGerak < 600) return;   // fokus karena klik
    let terlihat = false;
    try { terlihat = e.target.matches(":focus-visible"); } catch { terlihat = false; }
    if (!terlihat) return;
    akar.classList.remove("kursor-sembunyi", "kursor-ketik");
    kunci(e.target.closest(MENGETIK) ? null : e.target);
  });

  window.addEventListener("resize", () => { ukurKanvas(); bangunkan(); });
  const atur = () => (tingkatGerak() === "mati" ? lepas() : pasang());
  saatGerakBerubah(atur);
  // saatGerakBerubah cuma mendengar setelan SISTEM; saklar Gerak di
  // Pengaturan menulis data-gerak di <html>. Yang memutuskan tetap
  // tingkatGerak(); pengamat ini cuma pemicunya.
  new MutationObserver(atur).observe(document.documentElement,
    { attributes: true, attributeFilter: ["data-gerak"] });
  atur();
}
