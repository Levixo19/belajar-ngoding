/** Reticle teleskop yang mengikuti kursor dan MENGUNCI sasaran.
 *
 *  Port `webapp/statik/js/kursor.js`. Empat braket sudut di sekitar ujung
 *  penunjuk; saat penunjuk berada di atas sesuatu yang bisa diklik,
 *  braketnya pindah membingkai elemen itu. Tanda "ini sasaranmu" yang SAMA
 *  dengan penanda bintang berikutnya di peta rasi, jadi kursor dan peta
 *  berbicara dengan satu bahasa bentuk.
 *
 *  Aturan yang mengikat, dan semuanya dari riset aksesibilitas:
 *
 *  * **Kursor ASLI tidak pernah disembunyikan.** Ukuran dan kontras yang
 *    dipilih pengguna di sistem operasinya tetap berlaku; reticle ini cuma
 *    tambahan di atasnya.
 *  * Hanya untuk penunjuk halus (mouse/trackpad), `pointer-events: none`,
 *    `aria-hidden`.
 *  * `tingkatGerak()` yang memutuskan: "mati" = reticle TIDAK ADA sama
 *    sekali; "halus" = melompat tanpa pegas dan tanpa jejak; "penuh" =
 *    pegas plus jejak meteor tipis.
 *  * Reticle ikut mengunci elemen yang difokus lewat PAPAN KETIK, supaya
 *    pengguna Tab mendapat penanda yang sama dengan pengguna mouse.
 *  * Hanya `transform` yang digerakkan, dan rAF BERHENTI begitu reticle
 *    diam: penunjuk yang menganggur di atas sebuah tombol tidak boleh
 *    menyalakan 60 frame per detik tanpa henti.
 *
 *  Satu penyimpangan dari aslinya, dan ia wajib: versi JS memasang pendengar
 *  dokumen SELAMANYA dan tidak pernah melepasnya. Di React itu berarti dua
 *  reticle begitu `StrictMode` memasang efeknya dua kali, dan dua lagi tiap
 *  kali cangkangnya dipasang ulang. Jadi semuanya dicatat dan dilepas.
 */

import { saatGerakBerubah, tingkatGerak } from "./gerak.ts";

const INTERAKTIF = "a[href], button:not([disabled]), summary, select, label[for], "
  + "[role='button'], [role='tab'], input[type='range'], input[type='checkbox'], "
  + "input[type='radio'], .rasi-bintang";
const MENGETIK = "input:not([type='range']):not([type='checkbox']):not([type='radio']), "
  + "textarea, [contenteditable='true'], .editor";
const LUAS_MAKS = 170000; // px persegi: kartu sebesar ini tidak dibingkai
const BEBAS = 22;
const JARAK = 5;
const UMUR_JEJAK = 180;

interface TitikJejak { x: number; y: number; t: number }

/** Pasang reticle. Mengembalikan pelepasnya. */
export function nyalakanKursor(): () => void {
  if (typeof matchMedia !== "function"
      || !matchMedia("(pointer: fine)").matches) {
    return () => {};
  }

  let akar: HTMLDivElement | null = null;
  let sudut: HTMLSpanElement[] = [];
  let kanvas: HTMLCanvasElement | null = null;
  let px = -200, py = -200, terakhirGerak = 0;
  let sasaran: Element | null = null;
  const kini = { x: -200, y: -200, w: BEBAS, h: BEBAS };
  let raf = 0;
  let jejak: TitikJejak[] = [];
  let rectLalu = "";

  function pasang() {
    if (akar) return;
    akar = document.createElement("div");
    akar.className = "kursor kursor-sembunyi";
    akar.setAttribute("aria-hidden", "true");
    sudut = [0, 1, 2, 3].map(() => {
      const s = document.createElement("span");
      s.className = "kursor-sudut";
      akar!.appendChild(s);
      return s;
    });
    kanvas = document.createElement("canvas");
    kanvas.className = "kursor-jejak";
    kanvas.setAttribute("aria-hidden", "true");
    document.body.append(kanvas, akar);
    ukurKanvas();
  }

  function lepasReticle() {
    if (!akar) return;
    cancelAnimationFrame(raf);
    raf = 0;
    akar.remove();
    kanvas?.remove();
    akar = null;
    kanvas = null;
    sudut = [];
  }

  function ukurKanvas() {
    if (!kanvas) return;
    const dpr = Math.min(2, window.devicePixelRatio || 1);
    kanvas.width = Math.round(innerWidth * dpr);
    kanvas.height = Math.round(innerHeight * dpr);
    kanvas.getContext("2d")?.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function tujuan() {
    if (sasaran && !sasaran.isConnected) { // elemennya sudah dilepas dari DOM
      sasaran = null;
      akar?.classList.remove("kursor-kunci");
    }
    if (sasaran) {
      const r = sasaran.getBoundingClientRect();
      if (r.width && r.height) {
        return { x: r.left - JARAK, y: r.top - JARAK,
                 w: r.width + JARAK * 2, h: r.height + JARAK * 2 };
      }
    }
    return { x: px - BEBAS / 2, y: py - BEBAS / 2, w: BEBAS, h: BEBAS };
  }

  function gambarJejak(waktu: number): boolean {
    const c = kanvas?.getContext("2d");
    if (!c) return false;
    c.clearRect(0, 0, innerWidth, innerHeight);
    jejak = jejak.filter((t) => waktu - t.t < UMUR_JEJAK);
    if (jejak.length < 2) return false;
    const warna = getComputedStyle(document.body)
      .getPropertyValue("--nyala").trim() || "#e4b96b";
    c.lineCap = "round";
    c.strokeStyle = warna;
    for (let i = 1; i < jejak.length; i++) {
      const a = jejak[i - 1]!, b = jejak[i]!;
      const umur = 1 - (waktu - b.t) / UMUR_JEJAK;
      c.globalAlpha = umur * 0.5;
      c.lineWidth = 0.5 + umur * 1.5;
      c.beginPath();
      c.moveTo(a.x, a.y);
      c.lineTo(b.x, b.y);
      c.stroke();
    }
    c.globalAlpha = 1;
    return true;
  }

  function bingkai(waktu: number) {
    raf = 0;
    if (!akar) return;
    const t = tujuan();
    // "halus" memakai faktor 1: reticle MELOMPAT ke tempatnya, tidak
    // memantul. Yang padam di tingkat tengah hanya yang bergerak sendiri.
    const pegas = tingkatGerak() === "penuh" ? 0.3 : 1;
    let diam = true;
    for (const k of ["x", "y", "w", "h"] as const) {
      const beda = t[k] - kini[k];
      kini[k] = Math.abs(beda) < 0.1 ? t[k] : kini[k] + beda * pegas;
      if (Math.abs(t[k] - kini[k]) > 0.1) diam = false;
    }
    const titik: Array<[number, number, number]> = [
      [kini.x, kini.y, 0],
      [kini.x + kini.w, kini.y, 90],
      [kini.x + kini.w, kini.y + kini.h, 180],
      [kini.x, kini.y + kini.h, 270],
    ];
    titik.forEach(([x, y, r], i) => {
      const s = sudut[i];
      if (s) {
        s.style.transform =
          `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0) rotate(${r}deg)`;
      }
    });
    let adaJejak = false;
    if (tingkatGerak() === "penuh") {
      adaJejak = gambarJejak(waktu);
    } else if (jejak.length) {
      jejak = [];
      kanvas?.getContext("2d")?.clearRect(0, 0, innerWidth, innerHeight);
    }
    /* Frame BERHENTI begitu reticle diam dan sasarannya tidak bergeser.
       Guliran dan perubahan ukuran membangunkannya lagi: penunjuk yang
       menganggur di atas sebuah tombol tidak boleh menyalakan 60 frame per
       detik tanpa henti. */
    const rect = `${t.x.toFixed(1)},${t.y.toFixed(1)},`
      + `${t.w.toFixed(1)},${t.h.toFixed(1)}`;
    const bergeser = rect !== rectLalu;
    rectLalu = rect;
    if (!diam || adaJejak || bergeser) raf = requestAnimationFrame(bingkai);
  }

  function bangunkan() {
    if (akar && !raf) raf = requestAnimationFrame(bingkai);
  }

  function kunci(el: Element | null) {
    let sasar = el;
    if (sasar) {
      const r = sasar.getBoundingClientRect();
      // Kartu raksasa tidak dibingkai: braket yang melingkari separuh layar
      // berhenti berarti "ini sasaranmu".
      if (r.width * r.height > LUAS_MAKS) sasar = null;
    }
    sasaran = sasar;
    akar?.classList.toggle("kursor-kunci", !!sasar);
    bangunkan();
  }

  /* ----------------------------------------------- pendengar, semua dicatat */
  const lepasan: Array<() => void> = [];
  const dengar = (
    sasar: Document | Window | HTMLElement, jenis: string,
    fn: EventListenerOrEventListenerObject, opsi?: AddEventListenerOptions,
  ) => {
    sasar.addEventListener(jenis, fn, opsi);
    lepasan.push(() => sasar.removeEventListener(jenis, fn, opsi));
  };

  dengar(document, "pointermove", ((e: PointerEvent) => {
    if (e.pointerType && e.pointerType !== "mouse" && e.pointerType !== "pen") return;
    if (!akar) return;
    px = e.clientX;
    py = e.clientY;
    terakhirGerak = performance.now();
    akar.classList.remove("kursor-sembunyi");
    if (tingkatGerak() === "penuh") jejak.push({ x: px, y: py, t: terakhirGerak });
    bangunkan();
  }) as EventListener, { passive: true });

  dengar(document, "pointerover", ((e: PointerEvent) => {
    if (!akar || !(e.target instanceof Element)) return;
    akar.classList.toggle("kursor-ketik", !!e.target.closest(MENGETIK));
    kunci(e.target.closest(INTERAKTIF));
  }) as EventListener);

  dengar(document, "pointerdown",
         (() => akar?.classList.add("kursor-tekan")) as EventListener);
  dengar(document, "pointerup",
         (() => akar?.classList.remove("kursor-tekan")) as EventListener);
  dengar(document.documentElement, "mouseleave", (() => {
    if (!akar) return;
    akar.classList.add("kursor-sembunyi");
    kunci(null);
  }) as EventListener);
  dengar(document, "focusout", ((e: FocusEvent) => {
    if (e.target === sasaran) kunci(null);
  }) as EventListener);
  dengar(window, "scroll", bangunkan as EventListener,
         { passive: true, capture: true });

  dengar(document, "focusin", ((e: FocusEvent) => {
    if (!akar || !(e.target instanceof Element)) return;
    // Fokus yang datang karena KLIK tidak perlu penanda papan ketik: braket
    // sudah ada di sana karena penunjuknya memang di situ.
    if (performance.now() - terakhirGerak < 600) return;
    let terlihat = false;
    try { terlihat = e.target.matches(":focus-visible"); } catch { terlihat = false; }
    if (!terlihat) return;
    akar.classList.remove("kursor-sembunyi", "kursor-ketik");
    kunci(e.target.closest(MENGETIK) ? null : e.target);
  }) as EventListener);

  dengar(window, "resize", (() => { ukurKanvas(); bangunkan(); }) as EventListener);

  const atur = () => (tingkatGerak() === "mati" ? lepasReticle() : pasang());
  const lepasGerak = saatGerakBerubah(atur);
  /* `saatGerakBerubah` cuma mendengar setelan SISTEM; saklar Gerak di
     Pengaturan menulis `data-gerak` di `<html>`. Yang memutuskan tetap
     `tingkatGerak()`; pengamat ini cuma pemicunya. */
  const amat = new MutationObserver(atur);
  amat.observe(document.documentElement,
               { attributes: true, attributeFilter: ["data-gerak"] });
  atur();

  return () => {
    for (const l of lepasan) l();
    lepasGerak();
    amat.disconnect();
    lepasReticle();
  };
}
