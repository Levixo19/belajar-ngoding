/* Gambar konsep di materi: spesifikasi dari inti/visual.py -> SVG.
 *
 * Satu spesifikasi digambar dua kali: di sini sebagai SVG, di terminal
 * sebagai teks berbingkai (inti/visual.baris). Isinya (judul, label, nilai)
 * wajib sama di keduanya; yang boleh berbeda cuma bentuknya.
 *
 * Gayanya garis atlas langit: garis rambut, satu warna kuningan untuk yang
 * DISOROT, verdigris untuk yang "jadi/arah", sisanya tinta. Warna tidak
 * pernah ditulis di sini, cuma kelas (`v-*`) yang digayai gaya.css lewat
 * token tema, jadi keempat tema ikut tanpa satu baris pun di berkas ini.
 *
 * Ukuran dihitung dari panjang teks dengan lebar huruf mono tetap (LH),
 * bukan diukur dari DOM: gambar dibangun sebelum ditempel, dan apa pun yang
 * mengukur tata letak di situ harus lewat saatSiap(). Teks di dalam kotak
 * memakai huruf kode, jadi tebakan lebarnya memang tepat.
 *
 * Tiap bentuk punya atribut presentasi cadangan (fill="none",
 * stroke="currentColor") supaya gambar tetap terbaca kalau aturan CSS-nya
 * tidak berlaku. */

import { h } from "./inti.js";
import { tingkatGerak } from "./gerak.js";

const NS = "http://www.w3.org/2000/svg";
const LH = 7.9;          // lebar satu huruf mono pada 13px
const LU = 7.4;          // perkiraan lebar huruf antarmuka pada 13px
const PAD = 14;

function s(tag, sifat = {}, ...anak) {
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

/* pathLength=1 dipakai animasi garis-tergambar (gaya.css, .v-hidup). Garis
   putus-putus tidak boleh memakainya: dasharray ikut diukur dalam satuan
   pathLength, jadi "4 4" berubah jadi satu garis utuh. */
const putus = (kelas) => (/putus/.test(kelas) ? null : 1);

const lebarTeks = (t, satuan = LH) => String(t ?? "").length * satuan;

function teks(x, y, isi, kelas = "v-teks", sifat = {}) {
  return s("text", { x, y, kelas, "dominant-baseline": "middle", fill: "currentColor", ...sifat },
    String(isi ?? ""));
}
const tengah = { "text-anchor": "middle" };

function kotak(x, y, w, t, kelas = "v-kotak", rx = 3) {
  return s("rect", { x, y, width: w, height: t, rx, kelas: kelas + " v-gambar",
                     fill: "none", stroke: "currentColor", pathLength: putus(kelas) });
}

function garis(x1, y1, x2, y2, kelas = "v-garis") {
  return s("line", { x1, y1, x2, y2, kelas: kelas + " v-gambar", stroke: "currentColor",
                     pathLength: putus(kelas) });
}

function jalur(d, kelas = "v-garis") {
  return s("path", { d, kelas: kelas + " v-gambar", fill: "none", stroke: "currentColor",
                     pathLength: putus(kelas) });
}

/** Kepala panah terbuka di (x,y) yang menghadap sudut `sudut` (radian). */
function kepalaSudut(x, y, sudut, kelas) {
  const p = 7, l = 0.48;
  const a = [x - p * Math.cos(sudut - l), y - p * Math.sin(sudut - l)];
  const b = [x - p * Math.cos(sudut + l), y - p * Math.sin(sudut + l)];
  return s("path", { d: `M${a[0]},${a[1]} L${x},${y} L${b[0]},${b[1]}`, kelas: kelas + " v-ujung-panah",
                     fill: "none", stroke: "currentColor" });
}

function panah(x1, y1, x2, y2, kelas = "v-panah") {
  return s("g", {}, garis(x1, y1, x2, y2, kelas),
    kepalaSudut(x2, y2, Math.atan2(y2 - y1, x2 - x1), kelas));
}

const ARAH = { kanan: 0, bawah: Math.PI / 2, kiri: Math.PI, atas: -Math.PI / 2 };
const kepala = (x, y, arah, kelas = "v-panah") => kepalaSudut(x, y, ARAH[arah], kelas);

/* ------------------------------------------------------------ penggambar */

function gVariabel(sp) {
  const namaW = Math.max(...sp.isi.map((b) => lebarTeks(b[0]))) + 4;
  const nilaiW = Math.max(60, Math.max(...sp.isi.map((b) => lebarTeks(b[1]))) + 28);
  const sorot = new Set(sp.sorot || []);
  const t = 34, jarak = 14;
  const simpul = [];
  sp.isi.forEach((b, i) => {
    const y = PAD + i * (t + jarak), tg = y + t / 2;
    const kx = PAD + namaW + 48;
    simpul.push(teks(PAD + namaW, tg, b[0], "v-teks v-nama", { "text-anchor": "end" }));
    simpul.push(panah(PAD + namaW + 8, tg, kx - 6, tg));
    simpul.push(kotak(kx, y, nilaiW, t, sorot.has(b[0]) ? "v-kotak v-sorot" : "v-kotak"));
    simpul.push(teks(kx + nilaiW / 2, tg, b[1], "v-teks", tengah));
    if (b[2]) simpul.push(teks(kx + nilaiW + 10, tg, b[2], "v-label"));
  });
  const tipeW = Math.max(0, ...sp.isi.map((b) => (b[2] ? lebarTeks(b[2], LU) + 14 : 0)));
  return { w: PAD * 2 + namaW + 48 + nilaiW + tipeW, h: PAD * 2 + sp.isi.length * (t + jarak) - jarak, simpul };
}

function gLarik(sp) {
  const sel = Math.max(42, Math.max(...sp.isi.map((v) => lebarTeks(v))) + 22);
  const t = 40;
  const atas = PAD + (sp.nama ? 24 : 0);
  const sorot = new Set(sp.sorot || []);
  const simpul = [];
  if (sp.nama) simpul.push(teks(PAD, PAD + 8, sp.nama, "v-teks v-nama"));
  sp.isi.forEach((v, i) => {
    const x = PAD + i * sel;
    simpul.push(kotak(x, atas, sel, t, sorot.has(i) ? "v-kotak v-sorot" : "v-kotak", 0));
    simpul.push(teks(x + sel / 2, atas + t / 2, v, "v-teks", tengah));
    simpul.push(teks(x + sel / 2, atas + t + 14, i, sorot.has(i) ? "v-label v-label-sorot" : "v-label", tengah));
  });
  let bawah = atas + t + 28;
  if (sp.rentang) {
    const [a, z] = sp.rentang;
    const x1 = PAD + a * sel + 4, x2 = PAD + z * sel - 4;
    simpul.push(jalur(`M${x1},${bawah - 4} v8 H${x2} v-8`, "v-garis v-garis-tumbuh"));
    simpul.push(teks((x1 + x2) / 2, bawah + 18, `[${a}:${z}]`, "v-label v-label-tumbuh", tengah));
    bawah += 30;
  }
  const penunjuk = Object.entries(sp.penunjuk || {});
  penunjuk.forEach(([lbl, i]) => {
    const x = PAD + i * sel + sel / 2;
    simpul.push(panah(x, bawah + 24, x, bawah + 2, "v-panah v-panah-sorot"));
    simpul.push(teks(x, bawah + 36, lbl, "v-teks v-nama-sorot", tengah));
  });
  if (penunjuk.length) bawah += 44;
  return { w: PAD * 2 + sp.isi.length * sel, h: bawah + PAD - 12, simpul };
}

function bentukAlur(l, x, y, w, t) {
  const kls = l.jenis === "keputusan" ? "v-kotak v-sorot" : "v-kotak";
  if (l.jenis === "mulai" || l.jenis === "selesai") return kotak(x, y, w, t, kls + " v-ujung", t / 2);
  if (l.jenis === "masukan" || l.jenis === "keluaran") {
    return jalur(`M${x + 10},${y} H${x + w} L${x + w - 10},${y + t} H${x} Z`, kls);
  }
  if (l.jenis === "keputusan") {
    return jalur(`M${x + 14},${y} H${x + w - 14} L${x + w},${y + t / 2} L${x + w - 14},${y + t} `
      + `H${x + 14} L${x},${y + t / 2} Z`, kls);
  }
  return kotak(x, y, w, t, kls, 2);
}

function gAlur(sp) {
  const L = sp.langkah;
  const t = 36, jarak = 30;
  const lebar = L.map((l) => lebarTeks(l.teks, LU) + (l.jenis === "keputusan" ? 54 : 36));
  const kolom = Math.max(...lebar);
  const cx = PAD + 70 + kolom / 2;
  const y = (i) => PAD + i * (t + jarak);
  const simpul = [];
  let lajurKanan = 0, lajurKiri = 0;
  const tepiKanan = (i) => cx + lebar[i] / 2;
  const tepiKiri = (i) => cx - lebar[i] / 2;

  L.forEach((l, i) => {
    simpul.push(bentukAlur(l, cx - lebar[i] / 2, y(i), lebar[i], t));
    simpul.push(teks(cx, y(i) + t / 2, l.teks, "v-teks v-teks-ui", tengah));
  });

  function belok(dari, ke, label, sisi) {
    const yd = y(dari) + t / 2, yk = y(ke) + t / 2;
    if (sisi === "kanan") {
      const x = cx + kolom / 2 + 24 + 18 * lajurKanan++;
      simpul.push(jalur(`M${tepiKanan(dari)},${yd} H${x} V${yk} H${tepiKanan(ke) + 2}`));
      simpul.push(kepala(tepiKanan(ke) + 2, yk, "kiri"));
      if (label) simpul.push(teks(tepiKanan(dari) + 6, yd - 9, label, "v-label"));
    } else {
      const x = cx - kolom / 2 - 24 - 16 * lajurKiri++;
      simpul.push(jalur(`M${tepiKiri(dari)},${yd} H${x} V${yk} H${tepiKiri(ke) - 2}`, "v-garis v-garis-tumbuh"));
      simpul.push(kepala(tepiKiri(ke) - 2, yk, "kanan", "v-panah v-panah-tumbuh"));
      if (label) simpul.push(teks(x - 4, (yd + yk) / 2, label, "v-label v-label-tumbuh", { "text-anchor": "end" }));
    }
  }

  L.forEach((l, i) => {
    if (l.jenis === "selesai") return;
    const lurus = () => simpul.push(panah(cx, y(i) + t, cx, y(i + 1) - 2));
    if (l.jenis === "keputusan") {
      const ya = l.ya ?? i + 1;
      if (ya === i + 1) {
        lurus();
        simpul.push(teks(cx + 8, y(i) + t + jarak / 2, "ya", "v-label"));
      } else belok(i, ya, "ya", ya < i ? "kiri" : "kanan");
      belok(i, l.tidak, "tidak", l.tidak < i ? "kiri" : "kanan");
      return;
    }
    if (l.ke !== undefined && l.ke !== null) {
      if (l.ke === i + 1) lurus();
      else belok(i, l.ke, l.ke < i ? "ulangi" : "", l.ke < i ? "kiri" : "kanan");
    } else if (i + 1 < L.length) lurus();
  });
  return { w: cx + kolom / 2 + 40 + 18 * lajurKanan + PAD + 30, h: PAD * 2 + L.length * (t + jarak) - jarak, simpul };
}

function gTumpukan(sp) {
  const simpul = [];
  const w = Math.max(100, Math.max(...sp.isi.map((v) => lebarTeks(v))) + 32);
  const t = 34;
  let atas = PAD + (sp.label ? 22 : 0);
  if (sp.label) simpul.push(teks(PAD, PAD + 7, sp.label, "v-label"));
  if (sp.mode === "antrean") {
    const x0 = PAD + 70;
    if (sp.operasi) {
      simpul.push(teks(x0 + sp.isi.length * w + 14, atas + 4, sp.operasi, "v-label v-label-sorot"));
      atas += 20;
    }
    sp.isi.forEach((v, i) => {
      simpul.push(kotak(x0 + i * w, atas, w, t, i === 0 ? "v-kotak v-sorot" : "v-kotak", 0));
      simpul.push(teks(x0 + i * w + w / 2, atas + t / 2, v, "v-teks", tengah));
    });
    simpul.push(panah(x0 - 6, atas + t / 2, PAD + 8, atas + t / 2, "v-panah v-panah-sorot"));
    simpul.push(teks(PAD, atas + t + 16, "depan (keluar)", "v-label"));
    const xb = x0 + sp.isi.length * w;
    simpul.push(panah(xb + 56, atas + t / 2, xb + 6, atas + t / 2));
    simpul.push(teks(xb + 8, atas + t + 16, "belakang (masuk)", "v-label"));
    return { w: xb + Math.max(130, sp.operasi ? lebarTeks(sp.operasi, LU) + 24 : 0) + PAD, h: atas + t + 26 + PAD, simpul };
  }
  if (sp.operasi) {
    simpul.push(teks(PAD + w / 2, atas + 6, sp.operasi, "v-label v-label-sorot", tengah));
    simpul.push(panah(PAD + w / 2, atas + 15, PAD + w / 2, atas + 32, "v-panah v-panah-sorot"));
    atas += 38;
  }
  const n = sp.isi.length;
  [...sp.isi].reverse().forEach((v, j) => {
    const y = atas + j * t;
    simpul.push(kotak(PAD, y, w, t, j === 0 ? "v-kotak v-sorot" : "v-kotak", 0));
    simpul.push(teks(PAD + w / 2, y + t / 2, v, "v-teks", tengah));
  });
  simpul.push(panah(PAD + w + 46, atas + t / 2, PAD + w + 8, atas + t / 2, "v-panah v-panah-sorot"));
  simpul.push(teks(PAD + w + 52, atas + t / 2, "puncak", "v-label v-label-sorot"));
  simpul.push(jalur(`M${PAD - 6},${atas - 6} V${atas + n * t + 6} H${PAD + w + 6} V${atas - 6}`, "v-garis v-garis-redup"));
  return { w: PAD * 2 + w + 110, h: atas + n * t + 8 + PAD, simpul };
}

function gPohon(sp) {
  const simpul = [];
  const t = 30, jarakY = 28, jarakX = 14;
  const lebarSimpul = (n) => Math.max(46, lebarTeks(n.teks) + 22);
  const daun = (n) => ((n.anak || []).length ? n.anak.reduce((a, c) => a + daun(c), 0) : 1);
  let maksW = 0;
  (function ukur(n) { maksW = Math.max(maksW, lebarSimpul(n)); (n.anak || []).forEach(ukur); })(sp.akar);
  const kolom = maksW + jarakX;
  let dalam = 0;
  const garisan = [], kotakan = [];
  function letak(n, kiri, tingkat) {
    dalam = Math.max(dalam, tingkat);
    const x = kiri + (daun(n) * kolom) / 2;
    const y = PAD + tingkat * (t + jarakY);
    let k = kiri;
    for (const a of n.anak || []) {
      const p = letak(a, k, tingkat + 1);
      k += daun(a) * kolom;
      garisan.push(jalur(`M${x},${y + t} V${y + t + jarakY / 2} H${p.x} V${p.y}`, "v-garis"));
    }
    const w = lebarSimpul(n);
    kotakan.push(kotak(x - w / 2, y, w, t, tingkat === 0 ? "v-kotak v-sorot" : "v-kotak", 3));
    kotakan.push(teks(x, y + t / 2, n.teks, "v-teks", tengah));
    return { x, y };
  }
  letak(sp.akar, PAD, 0);
  simpul.push(...garisan, ...kotakan);
  return { w: PAD * 2 + daun(sp.akar) * kolom, h: PAD * 2 + (dalam + 1) * (t + jarakY) - jarakY, simpul };
}

function gTabel(sp) {
  const simpul = [];
  let y = PAD, lebarMaks = 0;
  const t = 28;
  sp.tabel.forEach((tb, ti) => {
    if (ti && sp.panah) {
      simpul.push(panah(PAD + 22, y - 2, PAD + 22, y + 24, "v-panah v-panah-sorot"));
      simpul.push(teks(PAD + 36, y + 11, sp.panah, "v-label v-label-sorot"));
      lebarMaks = Math.max(lebarMaks, 36 + lebarTeks(sp.panah, LU));
      y += 36;
    }
    if (tb.nama) { simpul.push(teks(PAD, y + 8, tb.nama, "v-teks v-nama")); y += 22; }
    // Sel None digambar KOSONG, sama dengan terminal (inti/visual._s). Kalau
    // yang dimaksud NULL SQL, datanya menulis "NULL" sebagai teks.
    const w = tb.kolom.map((c, i) => Math.max(lebarTeks(c), ...tb.baris.map((r) => lebarTeks(r[i] ?? ""))) + 22);
    const sk = new Set(tb.sorot_kolom || []);
    const sb = new Set(tb.sorot_baris || []);
    let x = PAD;
    tb.kolom.forEach((c, i) => {
      simpul.push(kotak(x, y, w[i], t, sk.has(c) ? "v-kepala v-sorot" : "v-kepala", 0));
      simpul.push(teks(x + 11, y + t / 2, c, "v-teks v-teks-tebal"));
      x += w[i];
    });
    tb.baris.forEach((r, ri) => {
      let xx = PAD;
      const yy = y + t * (ri + 1);
      r.forEach((v, i) => {
        const kls = sb.has(ri) ? "v-kotak v-sorot" : sk.has(tb.kolom[i]) ? "v-kotak v-sorot-lembut" : "v-kotak";
        simpul.push(kotak(xx, yy, w[i], t, kls, 0));
        simpul.push(teks(xx + 11, yy + t / 2, v ?? "", "v-teks"));
        xx += w[i];
      });
    });
    lebarMaks = Math.max(lebarMaks, w.reduce((a, b) => a + b, 0));
    y += t * (tb.baris.length + 1) + 16;
  });
  return { w: PAD * 2 + lebarMaks, h: y + PAD - 16, simpul };
}

function gUrutan(sp) {
  const simpul = [];
  const lebarPesan = Math.max(...sp.pesan.filter((m) => m[0] !== m[1]).map((m) => lebarTeks(`${m[2]}  00`, LU)), 0) + 40;
  const jarak = Math.max(170, lebarPesan);
  const kotakW = (p) => Math.max(88, lebarTeks(p, LU) + 28);
  const x = (i) => PAD + kotakW(sp.pelaku[0]) / 2 + i * jarak;
  const t = 32, baris = 42;
  const bawah = PAD + t + 18 + sp.pesan.length * baris + 8;
  sp.pelaku.forEach((p, i) => {
    simpul.push(garis(x(i), PAD + t, x(i), bawah, "v-garis v-garis-putus"));
    simpul.push(kotak(x(i) - kotakW(p) / 2, PAD, kotakW(p), t, "v-kotak v-sorot", 3));
    simpul.push(teks(x(i), PAD + t / 2, p, "v-teks v-teks-ui", tengah));
  });
  let lebarDiri = 0;
  sp.pesan.forEach(([a, b, isi], k) => {
    const y = PAD + t + 18 + k * baris + 20;
    if (a === b) {
      simpul.push(jalur(`M${x(a)},${y - 8} h28 v16 h-24`, "v-garis"));
      simpul.push(kepala(x(a) + 4, y + 8, "kiri"));
      simpul.push(teks(x(a) + 36, y, `${k + 1}. ${isi}`, "v-label"));
      lebarDiri = Math.max(lebarDiri, (a === sp.pelaku.length - 1 ? 40 + lebarTeks(isi, LU) : 0));
      return;
    }
    const kanan = b > a;
    simpul.push(panah(x(a) + (kanan ? 4 : -4), y, x(b) + (kanan ? -5 : 5), y, kanan ? "v-panah" : "v-panah v-panah-tumbuh"));
    simpul.push(teks((x(a) + x(b)) / 2, y - 11, `${k + 1}. ${isi}`, "v-label", tengah));
  });
  const akhir = sp.pelaku.length - 1;
  return { w: x(akhir) + Math.max(kotakW(sp.pelaku[akhir]) / 2, lebarDiri) + PAD + 10, h: bawah + PAD, simpul };
}

function gKotak(sp) {
  const simpul = [];
  const lapis = [["margin", sp.margin, "v-garis-putus"], ["border", sp.border, "v-sorot"],
                 ["padding", sp.padding, "v-sorot-lembut"]];
  const isiW = Math.max(160, lebarTeks(`isi: ${sp.isi}`) + 32);
  const tebal = 30;
  const atas = PAD + (sp.label ? 22 : 0);
  if (sp.label) simpul.push(teks(PAD, PAD + 7, sp.label, "v-teks v-nama"));
  const total = isiW + lapis.length * 2 * tebal;
  const tinggiIsi = 46;
  lapis.forEach(([nama, nilai, kls], i) => {
    const x = PAD + i * tebal, y = atas + i * tebal;
    simpul.push(kotak(x, y, total - i * 2 * tebal, tinggiIsi + (lapis.length - i) * 2 * tebal, "v-kotak " + kls, 2));
    simpul.push(teks(x + 9, y + 15, `${nama} ${nilai}`, "v-label"));
  });
  const xi = PAD + lapis.length * tebal, yi = atas + lapis.length * tebal;
  simpul.push(kotak(xi, yi, isiW, tinggiIsi, "v-kotak v-isi", 2));
  simpul.push(teks(xi + isiW / 2, yi + tinggiIsi / 2, `isi: ${sp.isi}`, "v-teks", tengah));
  return { w: PAD * 2 + total, h: atas + tinggiIsi + lapis.length * 2 * tebal + PAD, simpul };
}

function gTata(sp) {
  const simpul = [];
  const item = sp.item.map((it) => (Array.isArray(it) ? it : [it, 1]));
  if (sp.mode === "grid") {
    const kol = sp.kolom;
    const selW = Math.max(92, Math.max(...item.map(([isi, span]) => (lebarTeks(isi) + 24) / span)));
    const t = 40, celah = 8, atas = PAD + 22;
    simpul.push(teks(PAD, PAD + 7, `grid-template-columns: repeat(${kol}, 1fr)`, "v-label"));
    let r = 0, c = 0;
    const kotakan = [];
    item.forEach(([isi, span]) => {
      if (c + span > kol) { r += 1; c = 0; }
      const x = PAD + c * (selW + celah), y = atas + r * (t + celah);
      const w = span * selW + (span - 1) * celah;
      kotakan.push(kotak(x, y, w, t, span > 1 ? "v-kotak v-sorot" : "v-kotak", 3));
      kotakan.push(teks(x + w / 2, y + t / 2, isi, "v-teks", tengah));
      c += span;
    });
    const tinggi = atas + (r + 1) * (t + celah) - celah;
    for (let k = 1; k < kol; k++) {
      const x = PAD + k * (selW + celah) - celah / 2;
      simpul.push(garis(x, atas - 6, x, tinggi + 6, "v-garis v-garis-putus"));
    }
    simpul.push(...kotakan);
    return { w: PAD * 2 + kol * (selW + celah) - celah, h: tinggi + PAD + 6, simpul };
  }
  const kolom = (sp.arah || "row") === "column";
  const lebar = item.map(([isi]) => Math.max(56, lebarTeks(isi) + 26));
  const tinggiItem = item.map((_x, i) => 32 + (i % 3) * 12);
  const utamaTotal = kolom ? tinggiItem.reduce((a, b) => a + b, 0) : lebar.reduce((a, b) => a + b, 0);
  const wadahW = kolom ? Math.max(240, Math.max(...lebar) + 140) : Math.max(440, utamaTotal + 140);
  const wadahT = kolom ? Math.max(260, utamaTotal + 90) : 110;
  const x0 = PAD, y0 = PAD + 36;
  simpul.push(teks(PAD, PAD + 7, [`flex-direction: ${sp.arah || "row"}`, sp.justify && `justify-content: ${sp.justify}`,
    sp.align && `align-items: ${sp.align}`].filter(Boolean).join("; "), "v-label"));
  simpul.push(kotak(x0, y0, wadahW, wadahT, "v-kotak v-garis-putus", 4));
  const sisa = (kolom ? wadahT : wadahW) - 20 - utamaTotal;
  const n = item.length;
  let mulai = 10, sela = 0;
  switch (sp.justify) {
    case "center": mulai = 10 + sisa / 2; break;
    case "flex-end": case "end": mulai = 10 + sisa; break;
    case "space-between": sela = n > 1 ? sisa / (n - 1) : 0; break;
    case "space-around": sela = sisa / n; mulai = 10 + sela / 2; break;
    case "space-evenly": sela = sisa / (n + 1); mulai = 10 + sela; break;
    default: break;
  }
  let pos = mulai;
  item.forEach(([isi], i) => {
    const w = kolom ? Math.max(...lebar) : lebar[i];
    const t = tinggiItem[i];
    const silang = kolom ? wadahW : wadahT, ukSilang = kolom ? w : t;
    let off = 10;
    if (sp.align === "center") off = (silang - ukSilang) / 2;
    else if (sp.align === "flex-end" || sp.align === "end") off = silang - ukSilang - 10;
    else if (sp.align === "stretch" && !kolom) off = 10;
    const x = kolom ? x0 + off : x0 + pos;
    const y = kolom ? y0 + pos : y0 + off;
    const tinggiTampil = sp.align === "stretch" && !kolom ? wadahT - 20 : t;
    simpul.push(kotak(x, y, w, tinggiTampil, "v-kotak v-sorot", 3));
    simpul.push(teks(x + w / 2, y + tinggiTampil / 2, isi, "v-teks", tengah));
    pos += (kolom ? t : w) + sela;
  });
  if (kolom) {
    simpul.push(panah(x0 + wadahW + 20, y0 + 8, x0 + wadahW + 20, y0 + wadahT - 8, "v-panah v-panah-tumbuh"));
    simpul.push(teks(x0 + wadahW + 28, y0 + wadahT / 2, "sumbu utama", "v-label v-label-tumbuh"));
  } else {
    simpul.push(panah(x0 + 8, y0 + wadahT + 16, x0 + wadahW - 8, y0 + wadahT + 16, "v-panah v-panah-tumbuh"));
    simpul.push(teks(x0 + wadahW / 2, y0 + wadahT + 30, "sumbu utama", "v-label v-label-tumbuh", tengah));
  }
  const labelW = lebarTeks(simpul[0].textContent, LU);
  return { w: Math.max(PAD * 2 + wadahW + (kolom ? 120 : 0), PAD * 2 + labelW), h: y0 + wadahT + (kolom ? 4 : 40) + PAD, simpul };
}

function gGit(sp) {
  const simpul = [];
  const cabang = [];
  sp.commit.forEach((c) => { if (!cabang.includes(c.cabang)) cabang.push(c.cabang); });
  const namaW = Math.max(...cabang.map((b) => lebarTeks(b, LU))) + 26;
  const langkah = Math.max(72, ...sp.commit.map((c) => (c.pesan ? lebarTeks(c.pesan, 6.4) + 12 : 0)));
  const lajur = 70;
  const tumpuk = {};
  Object.values(sp.label || {}).forEach((cid) => { tumpuk[cid] = (tumpuk[cid] || 0) + 1; });
  const atas = PAD + 30 + 22 * (Math.max(1, ...Object.values(tumpuk)) - 1);
  const pos = {};
  sp.commit.forEach((c, i) => {
    pos[c.id] = { x: PAD + namaW + 24 + i * langkah, y: atas + cabang.indexOf(c.cabang) * lajur };
  });
  const garisan = [];
  cabang.forEach((b, j) => simpul.push(teks(PAD, atas + j * lajur, b, "v-label v-label-cabang")));
  sp.commit.forEach((c) => {
    (c.induk || []).forEach((p) => {
      const a = pos[p], b = pos[c.id];
      if (a.y === b.y) garisan.push(garis(a.x + 8, a.y, b.x - 8, b.y, "v-garis v-garis-tebal"));
      else {
        const mx = (a.x + b.x) / 2;
        garisan.push(jalur(`M${a.x + 7},${a.y} C${mx},${a.y} ${mx},${b.y} ${b.x - 8},${b.y}`, "v-garis v-garis-tebal"));
      }
    });
  });
  simpul.push(...garisan);
  const ujung = new Set(Object.values(sp.label || {}));
  sp.commit.forEach((c) => {
    const p = pos[c.id];
    const gabung = (c.induk || []).length > 1;
    simpul.push(s("circle", { cx: p.x, cy: p.y, r: gabung ? 9 : 7, kelas: ujung.has(c.id) ? "v-bintang v-sorot" : "v-bintang",
                              fill: "none", stroke: "currentColor" }));
    simpul.push(teks(p.x, p.y + 22, c.id, "v-teks", tengah));
    if (c.pesan) simpul.push(teks(p.x, p.y + 38, c.pesan, "v-label v-label-kecil", tengah));
  });
  const terpakai = {};
  Object.entries(sp.label || {}).forEach(([nama, cid]) => {
    const p = pos[cid];
    const k = (terpakai[cid] = (terpakai[cid] || 0) + 1) - 1;
    const w = lebarTeks(nama, LU) + 18, y = p.y - 32 - k * 22;
    const head = sp.head === nama;
    simpul.push(kotak(p.x - w / 2, y - 9, w, 18, head ? "v-label-kotak v-sorot" : "v-label-kotak", 9));
    simpul.push(teks(p.x, y, nama, "v-label", tengah));
    if (head) simpul.push(teks(p.x + w / 2 + 6, y, "HEAD", "v-label v-label-sorot"));
  });
  if (sp.head && !(sp.head in (sp.label || {})) && pos[sp.head]) {
    simpul.push(teks(pos[sp.head].x, pos[sp.head].y - 30, "HEAD", "v-label v-label-sorot", tengah));
  }
  return { w: PAD * 2 + namaW + 60 + sp.commit.length * langkah, h: atas + (cabang.length - 1) * lajur + 48 + PAD, simpul };
}

function gMemori(sp) {
  const simpul = [];
  const heap = sp.heap || [];
  const namaW = Math.max(...sp.tumpukan.map((b) => lebarTeks(b[0]))) + 22;
  const nilaiW = Math.max(72, ...sp.tumpukan.map((b) => (String(b[1]).startsWith("@") ? 44 : lebarTeks(b[1]) + 24)));
  const t = 32, atas = PAD + 24;
  simpul.push(teks(PAD, PAD + 7, sp.label_tumpukan || "stack", "v-label"));
  const heapX = PAD + namaW + nilaiW + 96;
  const heapW = Math.max(120, ...heap.map((o) => lebarTeks(o.isi) + 28));
  if (heap.length) simpul.push(teks(heapX, PAD + 7, sp.label_heap || "heap", "v-label"));
  const posHeap = {};
  let catatanW = 0;
  heap.forEach((o, i) => {
    const y = atas + i * (t + 18);
    posHeap[o.id] = y + t / 2;
    // Penunjuk boleh datang dari variabel ("@id") atau dari isi objek heap
    // lain (node linked list); sama dengan inti/visual._dirujuk.
    const kata = new RegExp("(^|[^\\w])" + o.id.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "([^\\w]|$)");
    const dirujuk = sp.tumpukan.some((b) => String(b[1]) === "@" + o.id)
      || heap.some((lain) => lain !== o && kata.test(lain.isi));
    simpul.push(kotak(heapX, y, heapW, t, dirujuk ? "v-kotak v-sorot-lembut" : "v-kotak v-redup", 3));
    simpul.push(teks(heapX + 11, y + t / 2, o.isi, dirujuk ? "v-teks" : "v-teks v-redup"));
    const cat = dirujuk ? o.id : `${o.id} (tanpa penunjuk)`;
    simpul.push(teks(heapX + heapW + 9, y + t / 2, cat, "v-label v-label-kecil"));
    catatanW = Math.max(catatanW, lebarTeks(cat, 6.4) + 16);
  });
  const panahan = [];
  sp.tumpukan.forEach(([nama, nilai], i) => {
    const y = atas + i * t;
    simpul.push(kotak(PAD, y, namaW, t, "v-kepala", 0));
    simpul.push(teks(PAD + 11, y + t / 2, nama, "v-teks v-nama"));
    simpul.push(kotak(PAD + namaW, y, nilaiW, t, "v-kotak", 0));
    const v = String(nilai);
    if (v.startsWith("@")) {
      const cx = PAD + namaW + nilaiW / 2, cy = y + t / 2, ty = posHeap[v.slice(1)];
      simpul.push(s("circle", { cx, cy, r: 4, kelas: "v-titik", fill: "currentColor" }));
      const mx = (cx + heapX) / 2;
      panahan.push(jalur(`M${cx + 5},${cy} C${mx},${cy} ${mx},${ty} ${heapX - 3},${ty}`, "v-panah"));
      panahan.push(kepala(heapX - 3, ty, "kanan"));
    } else {
      simpul.push(teks(PAD + namaW + nilaiW / 2, y + t / 2, v, "v-teks", tengah));
    }
  });
  simpul.push(...panahan);
  const tinggi = Math.max(sp.tumpukan.length * t, heap.length * (t + 18) - 18);
  return { w: heap.length ? heapX + heapW + catatanW + PAD : PAD * 2 + namaW + nilaiW, h: atas + tinggi + PAD, simpul };
}

function gBit(sp) {
  const simpul = [];
  const lebar = sp.lebar || 8;
  const bit = sp.angka.toString(2).padStart(lebar, "0");
  const sel = lebar > 8 ? 38 : 46;
  const atas = PAD + (sp.label ? 22 : 0);
  if (sp.label) simpul.push(teks(PAD, PAD + 7, sp.label, "v-label"));
  [...bit].forEach((b, i) => {
    const x = PAD + i * sel;
    simpul.push(teks(x + sel / 2, atas + 8, 2 ** (lebar - 1 - i), "v-label v-label-kecil", tengah));
    simpul.push(kotak(x, atas + 18, sel, 40, b === "1" ? "v-kotak v-sorot" : "v-kotak", 0));
    simpul.push(teks(x + sel / 2, atas + 38, b, b === "1" ? "v-teks v-teks-tebal" : "v-teks v-redup", tengah));
  });
  const jumlah = [...bit].map((b, i) => (b === "1" ? 2 ** (lebar - 1 - i) : null)).filter((x) => x !== null);
  const kalimat = `${jumlah.length ? jumlah.join(" + ") : "0"} = ${sp.angka}`;
  simpul.push(teks(PAD, atas + 78, kalimat, "v-teks"));
  return { w: Math.max(PAD * 2 + lebar * sel, PAD * 2 + lebarTeks(kalimat)), h: atas + 92 + PAD, simpul };
}

const RUMUS = {
  "1": () => 1, "log n": (n) => Math.log2(n), "n": (n) => n,
  "n log n": (n) => n * Math.log2(n), "n^2": (n) => n * n, "2^n": (n) => 2 ** n,
};

function gKurva(sp) {
  const simpul = [];
  const W = 440, H = 230, x0 = PAD + 56, y0 = PAD + 12;
  const nMaks = 16, yMaks = 64;
  simpul.push(garis(x0, y0, x0, y0 + H, "v-garis"));
  simpul.push(garis(x0, y0 + H, x0 + W, y0 + H, "v-garis"));
  simpul.push(teks(x0 + W, y0 + H + 30, "n (ukuran masukan)", "v-label", { "text-anchor": "end" }));
  simpul.push(teks(x0 - 8, y0 + 4, "langkah", "v-label", { "text-anchor": "end" }));
  for (let k = 4; k <= nMaks; k += 4) {
    const x = x0 + (k / nMaks) * W;
    simpul.push(garis(x, y0 + H, x, y0 + H + 5, "v-garis"));
    simpul.push(teks(x, y0 + H + 15, k, "v-label v-label-kecil", tengah));
  }
  const labelY = [];
  sp.kurva.forEach((c) => {
    const f = RUMUS[c];
    const titik = [];
    for (let n = 1; n <= nMaks; n += 0.25) {
      const v = f(n);
      if (v > yMaks) { titik.push([x0 + ((n - 0.25 + 0.25 * (yMaks - f(n - 0.25)) / (v - f(n - 0.25))) / nMaks) * W, y0]); break; }
      titik.push([x0 + (n / nMaks) * W, y0 + H - (v / yMaks) * H]);
    }
    const akhir = titik[titik.length - 1];
    const sorot = c === sp.sorot;
    simpul.push(jalur("M" + titik.map((p) => p.map((v) => v.toFixed(1)).join(",")).join(" L"),
      sorot ? "v-garis v-kurva-sorot" : "v-garis v-kurva"));
    let ly = Math.max(y0 + 6, akhir[1]);
    while (labelY.some((y) => Math.abs(y - ly) < 13)) ly += 13;
    labelY.push(ly);
    simpul.push(teks(akhir[0] + 7, ly, `O(${c})`, sorot ? "v-label v-label-sorot" : "v-label"));
  });
  return { w: x0 + W + 96, h: y0 + H + 40 + PAD, simpul };
}

const PENGGAMBAR = {
  variabel: gVariabel, larik: gLarik, alur: gAlur, tumpukan: gTumpukan, pohon: gPohon,
  tabel: gTabel, urutan: gUrutan, kotak: gKotak, tata: gTata, git: gGit, memori: gMemori,
  bit: gBit, kurva: gKurva,
};

/** Spesifikasi gambar -> <figure> berisi SVG dan keterangannya. */
export function gambarVisual(sp) {
  const fn = PENGGAMBAR[sp && sp.jenis];
  if (!fn) return null;
  let hasil;
  try {
    hasil = fn(sp);
  } catch (e) {
    // Data rusak tidak boleh menjatuhkan seluruh halaman materi; pagar
    // tests/test_visual.py yang wajib menangkapnya lebih dulu.
    console.warn("gambar konsep gagal digambar:", sp.jenis, e);
    return null;
  }
  const w = Math.ceil(hasil.w), t = Math.ceil(hasil.h);
  const svg = s("svg", { viewBox: `0 0 ${w} ${t}`, width: w, role: "img", "aria-label": sp.judul,
                         kelas: "visual-svg", preserveAspectRatio: "xMinYMin meet" }, hasil.simpul);
  svg.style.maxWidth = w + "px";
  const fig = h("figure.visual", { data: { jenis: sp.jenis } },
    h("div.visual-kanvas", {}, svg),
    h("figcaption.visual-judul", {},
      h("span.visual-nomor", {}, "Gambar " + (sp.nomor || "")),
      h("span.visual-teks", {}, sp.judul),
      sp.ket ? h("span.visual-ket", {}, sp.ket) : null));
  hidupkan(fig);
  return fig;
}

/* Garisnya tergambar saat gambar pertama kali tergulir ke layar, hanya di
 * tingkat gerak penuh. Keadaan alaminya TERGAMBAR UTUH: kelas `v-hidup`
 * cuma memasang animasi yang berangkat dari kosong, jadi kalau pengamatnya
 * tidak pernah menyala, gambarnya tetap lengkap. */
let pengamat = null;
function hidupkan(fig) {
  if (tingkatGerak() !== "penuh" || typeof IntersectionObserver === "undefined") return;
  if (!pengamat) {
    pengamat = new IntersectionObserver((entri) => {
      for (const e of entri) {
        if (!e.isIntersecting) continue;
        pengamat.unobserve(e.target);
        // Dipicu SEBELUM masuk layar (rootMargin bawah). Gambar yang sudah
        // terlihat saat pertama diamati tidak dianimasikan: mengosongkan garis
        // yang sedang dibaca lalu menggambarnya ulang adalah kedipan.
        if (e.boundingClientRect.top < window.innerHeight) continue;
        e.target.classList.add("v-hidup");
      }
    }, { rootMargin: "0px 0px 25% 0px", threshold: 0 });
  }
  pengamat.observe(fig);
}
