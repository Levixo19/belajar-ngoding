/* Langit di belakang seluruh aplikasi: peta bintang yang tenang.
 *
 * Bukan hiasan acak. Bentuknya meminjam konvensi atlas langit sungguhan:
 *   * graticule PROYEKSI KUTUB (lingkaran deklinasi konsentris + garis jam
 *     yang memancar dari kutub di atas layar), bukan kisi persegi CSS;
 *   * ukuran bintang mengikuti kelas magnitudo dengan rumus d3-celestial
 *     r = 7·e^(-0.28·(mag+2)), jadi bintang terang jarang dan yang redup
 *     banyak, seperti langit sungguhan;
 *   * pita Bimasakti tipis di tema gelap.
 * Posisinya deterministik (benih tetap): langitnya sama setiap kali dibuka,
 * jadi ia terasa "milikmu", bukan semburan titik baru tiap halaman.
 *
 * Gerak dibagi menurut tingkatGerak() (satu-satunya yang memutuskan):
 *   penuh : paralaks halus mengikuti kursor + kelip 30 bintang terang
 *           (12 fps), berhenti saat tab tersembunyi dan di layar baca/kerja;
 *   halus : langit diam (paralaks = gerak akibat interaksi, WCAG 2.3.3);
 *   mati  : langit diam.
 * Langitnya digambar SEKALI ke kanvas (ulang hanya saat ukuran/tema berubah);
 * paralaks cuma menggeser kanvas lewat transform. Warnanya dibaca dari token
 * CSS (--langit-*), jadi tema terang mendapat peta bertinta di atas kertas. */

import { tingkatGerak, saatGerakBerubah } from "./gerak.js";

const AMPLITUDO = 16;          // px geser paralaks maksimum
const KELIP_FPS = 12;
const LAYAR_TENANG = /^#\/(materi|latihan|coba)\b/;

function prng(benih) {         // mulberry32
  return () => {
    benih |= 0; benih = (benih + 0x6d2b79f5) | 0;
    let t = Math.imul(benih ^ (benih >>> 15), 1 | benih);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const jariMag = (mag) => 7 * Math.exp(-0.28 * (mag + 2));

function token(nama, cadangan) {
  const v = getComputedStyle(document.body).getPropertyValue(nama).trim();
  return v || cadangan;
}

export function nyalakanLangit() {
  const latar = document.getElementById("latar");
  if (!latar || latar.querySelector(".langit")) return;
  const kanvas = document.createElement("canvas");
  kanvas.className = "langit";
  const kelip = document.createElement("canvas");
  kelip.className = "langit-kelip";
  for (const k of [kanvas, kelip]) k.setAttribute("aria-hidden", "true");
  latar.append(kanvas, kelip);

  let bintang = [], terang = [], lebar = 0, tinggi = 0, dpr = 1;
  let tx = 0, ty = 0, sx = 0, sy = 0, rafGeser = 0, timerKelip = 0;

  function ukur() {
    dpr = Math.min(2, window.devicePixelRatio || 1);
    lebar = window.innerWidth + AMPLITUDO * 2;
    tinggi = window.innerHeight + AMPLITUDO * 2;
    for (const k of [kanvas, kelip]) {
      k.width = Math.round(lebar * dpr);
      k.height = Math.round(tinggi * dpr);
      k.style.width = lebar + "px";
      k.style.height = tinggi + "px";
    }
  }

  function bangkitkan() {
    const acak = prng(1801);    // tahun Uranographia
    const jumlah = Math.round((lebar * tinggi) / 5200);
    bintang = [];
    for (let i = 0; i < jumlah; i++) {
      // Distribusi magnitudo condong ke redup: kelas 6 paling banyak.
      const u = acak();
      const mag = u < 0.02 ? 1 : u < 0.06 ? 2 : u < 0.14 ? 3 : u < 0.30 ? 4 : u < 0.58 ? 5 : 6;
      bintang.push({ x: acak() * lebar, y: acak() * tinggi, mag, fase: acak() * Math.PI * 2,
                     hangat: acak() < 0.18 });
    }
    terang = bintang.filter((b) => b.mag <= 2).slice(0, 30);
  }

  function gambar() {
    const c = kanvas.getContext("2d");
    c.setTransform(dpr, 0, 0, dpr, 0, 0);
    c.clearRect(0, 0, lebar, tinggi);
    const warnaBintang = token("--langit-bintang", "#e8e4d6");
    const warnaHangat = token("--langit-hangat", "#e4b96b");
    const warnaGaris = token("--langit-garis", "rgba(140,150,190,.10)");
    const warnaKabut = token("--langit-kabut", "");
    const warnaLabel = token("--langit-label", "rgba(140,150,190,.35)");

    // Graticule proyeksi kutub: kutubnya di atas layar, sedikit ke kanan.
    const kx = lebar * 0.62, ky = -tinggi * 0.95;
    c.strokeStyle = warnaGaris;
    c.lineWidth = 1;
    const langkahR = tinggi * 0.32;
    for (let r = langkahR * 2; r < tinggi * 3.2; r += langkahR) {
      c.beginPath(); c.arc(kx, ky, r, 0, Math.PI * 2); c.stroke();
    }
    for (let jam = 0; jam < 24; jam++) {
      const sudut = (jam / 24) * Math.PI * 2;
      if (Math.sin(sudut) < 0.05) continue;    // garis yang menjauh dari layar
      c.beginPath();
      c.moveTo(kx + Math.cos(sudut) * langkahR * 2, ky + Math.sin(sudut) * langkahR * 2);
      c.lineTo(kx + Math.cos(sudut) * tinggi * 4, ky + Math.sin(sudut) * tinggi * 4);
      c.stroke();
    }
    // Label jam di tepi bawah, kecil seperti di tepi lembar atlas.
    c.fillStyle = warnaLabel;
    c.font = "9px 'Atkinson Hyperlegible Mono', monospace";
    for (let jam = 0; jam < 24; jam++) {
      const sudut = (jam / 24) * Math.PI * 2;
      const sin = Math.sin(sudut), cos = Math.cos(sudut);
      if (sin < 0.2) continue;
      const x = kx + cos * ((tinggi - 10 - ky) / sin);
      if (x < 30 || x > lebar - 40) continue;
      c.fillText(`${jam}h`, x + 4, tinggi - AMPLITUDO - 8);
    }

    // Bimasakti: ribuan titik sangat redup di sekitar satu kurva lebar.
    if (warnaKabut) {
      const acak = prng(1610);   // Sidereus Nuncius
      c.fillStyle = warnaKabut;
      for (let i = 0; i < 2600; i++) {
        const t = acak();
        const pusat = tinggi * (0.82 - 0.62 * t) + Math.sin(t * 5) * 30;
        const g = (acak() + acak() + acak() - 1.5) * tinggi * 0.13;
        c.globalAlpha = 0.22 + acak() * 0.4;
        c.fillRect(t * lebar + (acak() - 0.5) * 30, pusat + g, 1, 1);
      }
      c.globalAlpha = 1;
    }

    for (const b of bintang) {
      const r = Math.max(0.45, jariMag(b.mag) * 0.42);
      c.globalAlpha = b.mag >= 6 ? 0.45 : b.mag === 5 ? 0.6 : 0.85;
      c.fillStyle = b.hangat ? warnaHangat : warnaBintang;
      c.beginPath(); c.arc(Math.round(b.x) + 0.5, Math.round(b.y) + 0.5, r, 0, Math.PI * 2); c.fill();
      if (b.mag <= 2) {
        // Bintang terang mendapat paku difraksi tipis, seperti di foto teleskop.
        c.globalAlpha = 0.22;
        c.fillRect(b.x - r * 4, b.y, r * 8, 0.6);
        c.fillRect(b.x, b.y - r * 4, 0.6, r * 8);
      }
    }
    c.globalAlpha = 1;
    kelip.getContext("2d").clearRect(0, 0, kelip.width, kelip.height);
  }

  function pasangGeser() {
    const t = `translate3d(${(-AMPLITUDO + sx).toFixed(2)}px, ${(-AMPLITUDO + sy).toFixed(2)}px, 0)`;
    kanvas.style.transform = t;
    kelip.style.transform = t;
  }

  function langkahGeser() {
    sx += (tx - sx) * 0.08;
    sy += (ty - sy) * 0.08;
    pasangGeser();
    rafGeser = Math.abs(tx - sx) + Math.abs(ty - sy) > 0.05 ? requestAnimationFrame(langkahGeser) : 0;
  }

  function saatPenunjuk(e) {
    if (tingkatGerak() !== "penuh" || e.pointerType === "touch") return;
    if (LAYAR_TENANG.test(location.hash)) return;   // layar baca: langit diam
    tx = (0.5 - e.clientX / window.innerWidth) * AMPLITUDO;
    ty = (0.5 - e.clientY / window.innerHeight) * AMPLITUDO;
    if (!rafGeser) rafGeser = requestAnimationFrame(langkahGeser);
  }

  function kelipSatu(waktu) {
    const c = kelip.getContext("2d");
    c.setTransform(dpr, 0, 0, dpr, 0, 0);
    c.clearRect(0, 0, lebar, tinggi);
    c.fillStyle = token("--langit-bintang", "#e8e4d6");
    for (const b of terang) {
      c.globalAlpha = (0.5 + 0.5 * Math.sin(waktu / 900 + b.fase)) * 0.55;
      c.beginPath(); c.arc(b.x, b.y, jariMag(b.mag) * 0.8, 0, Math.PI * 2); c.fill();
    }
    c.globalAlpha = 1;
  }

  function aturKelip() {
    const tenang = LAYAR_TENANG.test(location.hash);
    const boleh = tingkatGerak() === "penuh" && !document.hidden && !tenang;
    if (boleh && !timerKelip) {
      timerKelip = setInterval(() => kelipSatu(performance.now()), 1000 / KELIP_FPS);
    } else if (!boleh && timerKelip) {
      clearInterval(timerKelip);
      timerKelip = 0;
      kelip.getContext("2d").clearRect(0, 0, kelip.width, kelip.height);
    }
    if (tingkatGerak() !== "penuh" || tenang) { tx = ty = sx = sy = 0; pasangGeser(); }
    document.body.classList.toggle("langit-tenang", tenang);
  }

  function semua() { ukur(); bangkitkan(); gambar(); pasangGeser(); aturKelip(); }

  let tundaUkur = 0;
  window.addEventListener("resize", () => { clearTimeout(tundaUkur); tundaUkur = setTimeout(semua, 200); });
  window.addEventListener("pointermove", saatPenunjuk, { passive: true });
  window.addEventListener("hashchange", aturKelip);
  document.addEventListener("visibilitychange", aturKelip);
  saatGerakBerubah(aturKelip);
  // Saklar Gerak di Pengaturan (data-gerak) juga harus sampai ke sini.
  new MutationObserver(aturKelip)
    .observe(document.documentElement, { attributes: true, attributeFilter: ["data-gerak"] });
  // Tema berganti lewat atribut di <html>: warna langit ikut digambar ulang.
  new MutationObserver(() => requestAnimationFrame(gambar))
    .observe(document.documentElement, { attributes: true, attributeFilter: ["data-tema"] });
  semua();
}
