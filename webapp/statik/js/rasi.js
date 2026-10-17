/* Peta rasi: progres belajar digambar sebagai langit.
 *
 * Satu materi = satu bintang. Satu bab = satu rasi, yang garisnya mengikuti
 * URUTAN materi (bentuknya dibangkitkan deterministik dari judul bab, jadi
 * rasi Python selalu berbentuk sama). Terang bintang = status materinya,
 * memakai kelas magnitudo dan rumus ukuran d3-celestial:
 *   selesai  -> magnitudo 1 (terang, bercahaya)
 *   sebagian -> magnitudo 3
 *   baru     -> magnitudo 5 (redup)
 *   terkunci -> titik berongga, tidak bisa diklik
 * Bintang berikutnya diberi reticle kuningan, bentuk yang sama dengan
 * braket kursor (kursor.js): satu bahasa untuk "sasaranmu".
 *
 * Keputusan "terkunci" TIDAK dibuat di sini: nilainya datang dari server
 * (bab.py lewat isi.daftar_materi). Layar ini cuma menggambar.
 *
 * Peta ini PELENGKAP. Daftar materi di bawahnya tetap jalan utama dan satu-
 * satunya yang wajib bisa dipakai lewat papan ketik; bintangnya tautan
 * ber-tabindex -1, dan petanya punya ringkasan teks. */

import { api, h, isikan } from "./inti.js";
import { tingkatGerak } from "./gerak.js";

const NS = "http://www.w3.org/2000/svg";
export const ROMAWI = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII",
  "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"];
const MAG = { selesai: 1, sebagian: 3, baru: 5 };
export const KATA_STATUS = { selesai: "sudah dibaca", sebagian: "dibaca sebagian", baru: "belum dibaca" };

export function s(tag, sifat = {}, ...anak) {
  const el = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(sifat)) {
    if (v === null || v === undefined || v === false) continue;
    el.setAttribute(k === "kelas" ? "class" : k, String(v));
  }
  for (const a of anak.flat(4)) {
    if (a === null || a === undefined || a === false) continue;
    el.appendChild(a instanceof Node ? a : document.createTextNode(String(a)));
  }
  return el;
}

export function hash(teks) {
  let x = 2166136261;
  for (const c of String(teks)) x = Math.imul(x ^ c.codePointAt(0), 16777619);
  return x >>> 0;
}

function prng(benih) {
  return () => {
    benih |= 0; benih = (benih + 0x6d2b79f5) | 0;
    let t = Math.imul(benih ^ (benih >>> 15), 1 | benih);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export const jariBintang = (mag, skala = 1) => Math.max(1.1, 7 * Math.exp(-0.28 * (mag + 2)) * skala);
export const magStatus = (m) => (m.terkunci ? 6 : MAG[m.status] || 5);

/** Titik-titik sebuah rasi berisi `n` bintang, dinormalkan ke kotak w×h. */
export function bentukRasi(n, benih, w, h) {
  if (n <= 1) return [[0, 0]];
  const acak = prng(hash(benih));
  const titik = [[0, 0]];
  let sudut = acak() * Math.PI * 2;
  for (let i = 1; i < n; i++) {
    // Belokan tajam dan langkah tak seragam: rasi sungguhan bukan garis
    // berkelok rata, ia gugus yang jaraknya berselang-seling.
    sudut += (acak() - 0.5) * 2.7;
    const langkah = 0.45 + acak() * 1.05;
    const [x, y] = titik[i - 1];
    titik.push([x + Math.cos(sudut) * langkah, y + Math.sin(sudut) * langkah]);
  }
  const xs = titik.map((p) => p[0]), ys = titik.map((p) => p[1]);
  const x0 = Math.min(...xs), x1 = Math.max(...xs), y0 = Math.min(...ys), y1 = Math.max(...ys);
  const skala = Math.min(w / Math.max(0.001, x1 - x0), h / Math.max(0.001, y1 - y0));
  const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
  return titik.map(([x, y]) => [(x - cx) * skala, (y - cy) * skala]);
}

/** Garis antar dua bintang yang berhenti sebelum menyentuh keduanya. */
export function ruas(a, b, ra, rb, kelas) {
  const dx = b[0] - a[0], dy = b[1] - a[1];
  const d = Math.hypot(dx, dy);
  if (d < ra + rb + 4) return null;
  const ux = dx / d, uy = dy / d;
  return s("line", { x1: (a[0] + ux * (ra + 3)).toFixed(1), y1: (a[1] + uy * (ra + 3)).toFixed(1),
                     x2: (b[0] - ux * (rb + 3)).toFixed(1), y2: (b[1] - uy * (rb + 3)).toFixed(1),
                     // Garis jalur putus-putus: tanpa pathLength (lihat visual.js).
                     kelas, pathLength: /jalur/.test(kelas) ? null : 1 });
}

export function berikutDari(materi) {
  const i = materi.findIndex((m) => m.status !== "selesai" && !m.terkunci);
  return i < 0 ? null : i;
}

export function reticle(x, y, r) {
  const R = r + 7;
  // Dua lapis: luar memegang POSISI (atribut transform), dalam boleh diputar
  // CSS. Memutar lapis luar lewat CSS akan menimpa translate-nya.
  return s("g", { kelas: "rasi-reticle", transform: `translate(${x.toFixed(1)},${y.toFixed(1)})` },
    s("g", { kelas: "rasi-reticle-putar" },
      s("circle", { r: R, fill: "none" }),
      ...[0, 90, 180, 270].map((d) => s("line", { x1: 0, y1: -R - 5, x2: 0, y2: -R + 1,
        transform: `rotate(${d})` }))));
}

/** Satu bintang (titik + cahaya + sasaran klik) sebagai <a> atau <g>. */
export function bintangSvg(m, x, y, r, href) {
  const kelas = m.terkunci ? "rasi-terkunci" : "rasi-" + (MAG[m.status] ? m.status : "baru");
  const isi = [
    m.status === "selesai" && !m.terkunci ? s("circle", { kelas: "rasi-cahaya", cx: x.toFixed(1), cy: y.toFixed(1), r: (r * 3.2).toFixed(1) }) : null,
    s("circle", { kelas: "rasi-titik " + kelas, cx: x.toFixed(1), cy: y.toFixed(1), r: r.toFixed(2) }),
    // Sasaran klik lebih besar daripada titiknya: bintang redup berjari-jari
    // satu piksel mustahil dikenai mouse.
    s("circle", { kelas: "rasi-sasaran", cx: x.toFixed(1), cy: y.toFixed(1), r: 10 }),
  ];
  const label = `${m.judul}, ${m.terkunci ? "masih terkunci" : KATA_STATUS[m.status] || ""}`;
  return m.terkunci || !href
    ? s("g", { kelas: "rasi-bintang rasi-bintang-kunci", "aria-label": label }, isi)
    : s("a", { kelas: "rasi-bintang", href, tabindex: -1, "aria-label": label }, isi);
}

/** Tip melayang yang dipakai bersama oleh semua bintang dalam satu peta. */
export function pasangTip(wadah) {
  const tip = h("div.rasi-tip");
  wadah.appendChild(tip);
  return {
    tunjuk(el, judul, ket) {
      isikan(tip, h("b", {}, judul), ket ? h("span", {}, ket) : null);
      tip.classList.add("rasi-tip-tampil");
      const kotak = wadah.getBoundingClientRect();
      const r = el.getBoundingClientRect();
      tip.style.left = Math.min(kotak.width - 260, Math.max(0, r.left - kotak.left - 24)) + "px";
      tip.style.top = (r.bottom - kotak.top + 10) + "px";
    },
    sembunyi() { tip.classList.remove("rasi-tip-tampil"); },
  };
}

/** Peta rasi satu kurikulum.
 *  data: {key, label, materi: [{judul, status, terkunci}], bab: [{nomor, judul, materi: [indeks]}]} */
export function petaRasi(data, { tinggi = 250 } = {}) {
  const W = 1000, H = tinggi;
  const bab = (data.bab && data.bab.length) ? data.bab
    : [{ nomor: 1, judul: data.label, materi: data.materi.map((_m, i) => i) }];
  const berikut = berikutDari(data.materi);
  const lebarRasi = W / bab.length;
  // Label bergantian atas-bawah, jadi tiap label boleh selebar DUA rasi.
  const batasLabel = Math.max(10, Math.min(30, Math.floor((lebarRasi * 2) / 6.8)));
  const posisi = [];
  const jalur = [];
  const lapisGaris = s("g");
  const lapisBintang = s("g");
  const lapisLabel = s("g");
  let urutan = 0;

  bab.forEach((b, i) => {
    const cx = (i + 0.5) * lebarRasi;
    const cy = H * 0.46 + Math.sin(i * 1.7 + (hash(data.key) % 7)) * H * 0.13;
    const kotakW = Math.min(lebarRasi * 0.74, 150), kotakH = H * 0.42;
    const titik = bentukRasi(b.materi.length, data.key + "·" + b.judul, kotakW, kotakH)
      .map(([x, y]) => [cx + x, cy + y]);
    const kelompok = s("g", { kelas: "rasi-kelompok" });
    b.materi.forEach((idx, j) => {
      const m = data.materi[idx];
      if (!m) return;
      const r = jariBintang(magStatus(m), 0.9);
      posisi[idx] = { p: titik[j], r };
      if (j > 0 && posisi[b.materi[j - 1]]) {
        const kiri = data.materi[b.materi[j - 1]];
        const terang = kiri.status === "selesai" && m.status === "selesai";
        const g = ruas(titik[j - 1], titik[j], posisi[b.materi[j - 1]].r, r,
          terang ? "rasi-garis rasi-garis-terang" : "rasi-garis");
        if (g) { g.style.setProperty("--i", urutan); kelompok.appendChild(g); }
      }
      const bt = bintangSvg(m, titik[j][0], titik[j][1], r, `#/materi/${data.key}/${idx}`);
      bt.dataset.indeks = idx;
      bt.style.setProperty("--i", urutan++);
      kelompok.appendChild(bt);
    });
    lapisBintang.appendChild(kelompok);
    const bawah = i % 2 === 0;
    // Label di ujung kiri/kanan dijangkarkan ke dalam supaya tidak terpotong.
    const jangkar = bab.length > 2 && i === 0 ? "start" : bab.length > 2 && i === bab.length - 1 ? "end" : "middle";
    const lx = jangkar === "start" ? 6 : jangkar === "end" ? W - 6 : cx;
    lapisLabel.appendChild(s("text", { kelas: "rasi-label-bab", x: lx.toFixed(1),
      y: (bawah ? cy + kotakH / 2 + 24 : cy - kotakH / 2 - 14).toFixed(1), "text-anchor": jangkar },
      s("tspan", { kelas: "rasi-nomor" }, (ROMAWI[b.nomor] || b.nomor) + "  "),
      b.judul.length > batasLabel ? b.judul.slice(0, batasLabel - 1) + "…" : b.judul));
    const lanjut = bab[i + 1];
    if (lanjut && b.materi.length && lanjut.materi.length) {
      jalur.push([b.materi[b.materi.length - 1], lanjut.materi[0]]);
    }
  });
  // Jalur antar rasi: bintang terakhir bab ke bintang pertama bab berikutnya.
  // Putus-putus, karena itu jalan yang ditempuh, bukan bagian rasinya.
  for (const [a, b] of jalur) {
    if (!posisi[a] || !posisi[b]) continue;
    const g = ruas(posisi[a].p, posisi[b].p, posisi[a].r, posisi[b].r, "rasi-garis rasi-garis-jalur");
    if (g) lapisGaris.appendChild(g);
  }
  if (berikut !== null && posisi[berikut]) {
    lapisLabel.appendChild(reticle(posisi[berikut].p[0], posisi[berikut].p[1], posisi[berikut].r));
  }

  const svg = s("svg", { viewBox: `0 0 ${W} ${H}`, kelas: "rasi-svg", preserveAspectRatio: "xMidYMid meet" },
    lapisGaris, lapisBintang, lapisLabel);
  const selesai = data.materi.filter((m) => m.status === "selesai").length;
  const wadah = h("div.rasi", {},
    h("p.rasi-ringkasan", {}, `Peta langit ${data.label}: ${selesai} dari ${data.materi.length} bintang menyala.`
      + (berikut !== null ? ` Berikutnya: ${data.materi[berikut].judul}.` : "")),
    svg);
  const tip = pasangTip(wadah);
  const lepasSorot = () => { for (const x of svg.querySelectorAll(".rasi-sorot")) x.classList.remove("rasi-sorot"); };
  svg.addEventListener("pointerover", (e) => {
    const b = e.target.closest && e.target.closest(".rasi-bintang");
    if (!b) return;
    const m = data.materi[Number(b.dataset.indeks)];
    lepasSorot();
    const k = b.closest(".rasi-kelompok");
    if (k) k.classList.add("rasi-sorot");
    tip.tunjuk(b, m.judul, m.terkunci ? "Masih terkunci" : (KATA_STATUS[m.status] || ""));
  });
  svg.addEventListener("pointerleave", () => { tip.sembunyi(); lepasSorot(); });
  if (tingkatGerak() === "penuh") wadah.classList.add("rasi-hidup");
  return wadah;
}

/** Data /api/bahasa -> bentuk yang dipakai petaRasi. */
export function dariBahasa(b) {
  return {
    key: b.key, label: b.label,
    materi: b.materi.map((m) => ({ judul: m.judul, status: m.status, terkunci: m.terkunci })),
    bab: (b.bab || []).map((x) => ({ nomor: x.nomor, judul: x.judul, materi: x.materi })),
  };
}

let singgahLangit = null;
export function ambilLangit(segar = false) {
  if (!singgahLangit || segar) {
    singgahLangit = api.ambil("/api/langit").catch((e) => { singgahLangit = null; throw e; });
  }
  return singgahLangit;
}

/** Panel "Langitmu" di dasbor: rasi kurikulum yang sedang dijalani. */
export function panelLangitMeja(key) {
  const isi = h("div.meja-langit-isi");
  const el = h("section.meja-langit", { "aria-label": "Peta langit belajarmu" },
    h("div.meja-langit-kepala", {},
      h("h2.meja-judul", {}, "Langitmu"),
      h("span.meja-langit-ket", {}, "Satu materi, satu bintang. Yang sudah kamu baca menyala."),
      h("a.meja-langit-tautan", { href: "#/langit" }, "Seluruh langit")),
    isi);
  ambilLangit(true).then((d) => {
    const bhs = d.bahasa.find((x) => x.key === key)
      || d.bahasa.find((x) => x.materi.some((m) => m.status !== "baru"));
    if (!bhs) { el.remove(); return; }
    isikan(isi, petaRasi(bhs, { tinggi: 230 }));
  }).catch(() => el.remove());
  return el;
}
