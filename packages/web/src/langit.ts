/** Langit di belakang seluruh aplikasi: peta bintang yang tenang.
 *
 *  Port `webapp/statik/js/langit.js`. Bukan hiasan acak -- bentuknya meminjam
 *  konvensi atlas langit sungguhan: graticule PROYEKSI KUTUB (lingkaran
 *  deklinasi konsentris plus garis jam yang memancar dari kutub di atas
 *  layar), ukuran bintang mengikuti kelas magnitudo, dan pita Bimasakti tipis
 *  di tema gelap.
 *
 *  Gerak dibagi menurut `tingkatGerak()`, satu-satunya yang memutuskan:
 *  "penuh" memberi paralaks halus mengikuti kursor plus kelip 30 bintang
 *  terang pada 12 fps, dan ia berhenti saat tab tersembunyi dan di layar
 *  baca/kerja; "halus" dan "mati" membuat langitnya DIAM. Paralaks adalah
 *  gerak akibat interaksi (WCAG 2.3.3), jadi ia memang tidak boleh ada di
 *  tingkat tengah.
 *
 *  Imperatif-kanvas, dan sengaja TIDAK dipaksa deklaratif: ia menggambar
 *  sekali ke kanvas dan hanya menggeser `transform`-nya sesudah itu. AGENTS
 *  menulis aturannya -- modul peng-ukur DOM dibungkus `useRef`/`useEffect`,
 *  bukan diterjemahkan jadi state.
 */

import { saatGerakBerubah, tingkatGerak } from "./gerak.ts";
import { bangkitkanBintang, bintangTerang, jariMag, prng } from "./langit-bentuk.ts";
import type { Bintang } from "./langit-bentuk.ts";

const AMPLITUDO = 16; // px geser paralaks maksimum
const KELIP_FPS = 12;
const LAYAR_TENANG = /^#\/(materi|latihan|coba)\b/;

/* Pendorong "arahkan ulang", dipasang oleh langit yang sedang hidup.
   Bawaannya tidak melakukan apa-apa, jadi memanggilnya sebelum langitnya
   menyala -- atau sesudah dilepas -- aman dan diam. */
let arahkanUlang: () => void = () => {};

/** Arahkan langit ulang, seperti instrumen yang diputar ke sasaran baru.
 *
 *  Dipanggil router saat rutenya berganti. Ia TIDAK menggambar ulang apa pun
 *  dan tidak membuat animasi baru: ia cuma menggeser sasaran paralaks yang
 *  sudah ada, jadi ongkosnya nol di luar peredam yang memang sudah jalan. */
export function arahkanLangit(): void {
  arahkanUlang();
}

function token(nama: string, cadangan: string): string {
  const v = getComputedStyle(document.body).getPropertyValue(nama).trim();
  return v || cadangan;
}

/** Pasang langit ke `#latar`. Mengembalikan pelepasnya.
 *
 *  Pelepas itu BUKAN kerapian: tanpa melepas pendengar `pointermove`,
 *  `resize`, dan kedua `MutationObserver`, setiap pemasangan ulang di
 *  pengembangan menumpuk satu langit lagi di belakang yang lama -- dan
 *  `StrictMode` memasang efek dua kali, jadi penumpukannya mulai dari
 *  pemuatan pertama.
 */
export function nyalakanLangit(): () => void {
  const latar = document.getElementById("latar");
  if (!latar || latar.querySelector(".langit")) return () => {};

  const kanvas = document.createElement("canvas");
  kanvas.className = "langit";
  const kelip = document.createElement("canvas");
  kelip.className = "langit-kelip";
  for (const k of [kanvas, kelip]) k.setAttribute("aria-hidden", "true");
  latar.append(kanvas, kelip);

  let bintang: Bintang[] = [];
  let terang: Bintang[] = [];
  let lebar = 0;
  let tinggi = 0;
  let dpr = 1;
  let tx = 0, ty = 0, sx = 0, sy = 0;
  let rafGeser = 0;
  let timerKelip: ReturnType<typeof setInterval> | 0 = 0;
  let putaran = 1;

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
    bintang = bangkitkanBintang(lebar, tinggi);
    terang = bintangTerang(bintang);
  }

  function gambar() {
    const c = kanvas.getContext("2d");
    if (!c) return;
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
      c.beginPath();
      c.arc(kx, ky, r, 0, Math.PI * 2);
      c.stroke();
    }
    for (let jam = 0; jam < 24; jam++) {
      const sudut = (jam / 24) * Math.PI * 2;
      if (Math.sin(sudut) < 0.05) continue; // garis yang menjauh dari layar
      c.beginPath();
      c.moveTo(kx + Math.cos(sudut) * langkahR * 2,
               ky + Math.sin(sudut) * langkahR * 2);
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
      const acak = prng(1610); // Sidereus Nuncius
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
      c.beginPath();
      c.arc(Math.round(b.x) + 0.5, Math.round(b.y) + 0.5, r, 0, Math.PI * 2);
      c.fill();
      if (b.mag <= 2) {
        // Paku difraksi tipis, seperti di foto teleskop.
        c.globalAlpha = 0.22;
        c.fillRect(b.x - r * 4, b.y, r * 8, 0.6);
        c.fillRect(b.x, b.y - r * 4, 0.6, r * 8);
      }
    }
    c.globalAlpha = 1;
    kelip.getContext("2d")?.clearRect(0, 0, kelip.width, kelip.height);
  }

  function pasangGeser() {
    const t = `translate3d(${(-AMPLITUDO + sx).toFixed(2)}px, `
      + `${(-AMPLITUDO + sy).toFixed(2)}px, 0)`;
    kanvas.style.transform = t;
    kelip.style.transform = t;
  }

  function langkahGeser() {
    sx += (tx - sx) * 0.08;
    sy += (ty - sy) * 0.08;
    pasangGeser();
    rafGeser = Math.abs(tx - sx) + Math.abs(ty - sy) > 0.05
      ? requestAnimationFrame(langkahGeser)
      : 0;
  }

  function saatPenunjuk(e: PointerEvent) {
    if (tingkatGerak() !== "penuh" || e.pointerType === "touch") return;
    if (LAYAR_TENANG.test(location.hash)) return; // layar baca: langit diam
    tx = (0.5 - e.clientX / window.innerWidth) * AMPLITUDO;
    ty = (0.5 - e.clientY / window.innerHeight) * AMPLITUDO;
    if (!rafGeser) rafGeser = requestAnimationFrame(langkahGeser);
  }

  function kelipSatu(waktu: number) {
    const c = kelip.getContext("2d");
    if (!c) return;
    c.setTransform(dpr, 0, 0, dpr, 0, 0);
    c.clearRect(0, 0, lebar, tinggi);
    c.fillStyle = token("--langit-bintang", "#e8e4d6");
    for (const b of terang) {
      c.globalAlpha = (0.5 + 0.5 * Math.sin(waktu / 900 + b.fase)) * 0.55;
      c.beginPath();
      c.arc(b.x, b.y, jariMag(b.mag) * 0.8, 0, Math.PI * 2);
      c.fill();
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
      kelip.getContext("2d")?.clearRect(0, 0, kelip.width, kelip.height);
    }
    if (tingkatGerak() !== "penuh" || tenang) {
      tx = ty = sx = sy = 0;
      pasangGeser();
    }
    document.body.classList.toggle("langit-tenang", tenang);
  }

  /* Arahkan ulang: dorong SASARAN paralaks, bukan transformnya.
     Paralaks sudah memegang `transform` kedua kanvas lewat `pasangGeser()`,
     dan menambahkan animasi WAAPI di properti yang sama berarti dua mesin
     mengejar satu properti -- gerakan tersendat yang paling sulit
     didiagnosis, dan aturan yang sudah tertulis di AGENTS.md. Jadi yang
     didorong `tx`/`ty`, dan peredam di `langkahGeser()` yang mengendapkannya.

     Gratis ikut tunduk pada tingkat gerak: `langkahGeser` cuma dipanggil
     lewat jalur yang sudah dipagari, dan `aturKelip()` menolkan sasaran di
     tingkat selain "penuh" maupun di layar baca. */
  arahkanUlang = () => {
    if (tingkatGerak() !== "penuh") return;
    if (LAYAR_TENANG.test(location.hash)) return;
    // Arahnya BERGANTIAN, bukan acak: dua perpindahan berurutan ke arah yang
    // sama terbaca sebagai hanyut, sementara bergantian terbaca sebagai
    // instrumen yang diputar lalu dikembalikan.
    putaran = -putaran;
    tx = putaran * AMPLITUDO * 0.75;
    ty = putaran * AMPLITUDO * 0.3;
    if (!rafGeser) rafGeser = requestAnimationFrame(langkahGeser);
  };

  function semua() {
    ukur();
    bangkitkan();
    gambar();
    pasangGeser();
    aturKelip();
  }

  let tundaUkur: ReturnType<typeof setTimeout> | 0 = 0;
  const saatUkuran = () => {
    if (tundaUkur) clearTimeout(tundaUkur);
    tundaUkur = setTimeout(semua, 200);
  };
  window.addEventListener("resize", saatUkuran);
  window.addEventListener("pointermove", saatPenunjuk, { passive: true });
  window.addEventListener("hashchange", aturKelip);
  document.addEventListener("visibilitychange", aturKelip);
  const lepasGerak = saatGerakBerubah(aturKelip);
  // Saklar Gerak di Pengaturan (`data-gerak`) juga harus sampai ke sini: ia
  // atribut, bukan media query, jadi `saatGerakBerubah` tidak melihatnya.
  const amatGerak = new MutationObserver(aturKelip);
  amatGerak.observe(document.documentElement,
                    { attributes: true, attributeFilter: ["data-gerak"] });
  // Tema berganti lewat atribut di <html>: warna langit ikut digambar ulang.
  const amatTema = new MutationObserver(() => requestAnimationFrame(gambar));
  amatTema.observe(document.documentElement,
                   { attributes: true, attributeFilter: ["data-tema"] });
  semua();

  return () => {
    // Pendorong dilepas LEBIH DULU: langit yang sudah dicabut dari DOM tapi
    // pendorongnya masih hidup berarti rute berikutnya memanggil fungsi yang
    // menulis ke kanvas yang tidak ada lagi.
    arahkanUlang = () => {};
    window.removeEventListener("resize", saatUkuran);
    window.removeEventListener("pointermove", saatPenunjuk);
    window.removeEventListener("hashchange", aturKelip);
    document.removeEventListener("visibilitychange", aturKelip);
    lepasGerak();
    amatGerak.disconnect();
    amatTema.disconnect();
    if (tundaUkur) clearTimeout(tundaUkur);
    if (timerKelip) clearInterval(timerKelip);
    if (rafGeser) cancelAnimationFrame(rafGeser);
    kanvas.remove();
    kelip.remove();
  };
}
