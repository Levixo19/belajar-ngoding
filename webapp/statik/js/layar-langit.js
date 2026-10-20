/* Layar Langit (#/langit): seluruh kurikulum sebagai satu peta bintang.
 *
 * Tiap kurikulum satu rasi; tiap materinya satu bintang, terangnya mengikuti
 * status baca (rasi.js, magnitudo d3-celestial). Letak rasi bukan acak: ia
 * dikelompokkan menurut KELUARGA, seperti atlas mengelompokkan rasi menurut
 * wilayah langit. Keluarga di sini menjawab pertanyaan yang memang dibawa
 * pelajar: "kalau sudah bisa ini, apa yang paling dekat?".
 *
 * Dua cara menghubungkan rasi, dan keduanya data, bukan tebakan:
 *   * profesi Peta Karier: garis ditarik antar kurikulum bekalnya
 *     (data/karier.py lewat /api/langit). Kesiapannya TIDAK dihitung di sini;
 *     satu-satunya definisinya pelajar/karier.py, jadi layar ini menautkan ke
 *     Peta Karier, bukan menulis angka kedua;
 *   * konsep yang sama: materi yang judulnya memuat konsep itu menyala di
 *     semua kurikulum sekaligus ("perulangan" di Python, Java, Go, ...). */

import { h, isikan } from "./inti.js";
import {
  ambilLangit, bentukRasi, ruas, bintangSvg, jariBintang, magStatus, berikutDari, reticle,
  pasangTip, s, KATA_STATUS,
} from "./rasi.js";
import { tingkatGerak } from "./gerak.js";

const W = 1400, H = 1420;

/* Letak tiap kurikulum (pusat rasi) dan keluarganya. Kurikulum baru yang
   belum terdaftar di sini tetap muncul, di baris cadangan paling bawah. */
const TATA = {
  html: [170, 200, "web"], css: [330, 140, "web"], javascript: [300, 330, "web"],
  typescript: [470, 260, "web"], php: [150, 420, "web"],
  c: [700, 150, "sistem"], cpp: [860, 210, "sistem"], rust: [760, 350, "sistem"], go: [930, 380, "sistem"],
  java: [1090, 150, "jvm"], kotlin: [1270, 220, "jvm"], aplikasi: [1060, 350, "jvm"],
  csharp: [1270, 420, "jvm"], vb: [1120, 540, "jvm"],
  python: [430, 560, "skrip"], ruby: [250, 640, "skrip"], bash: [570, 700, "skrip"],
  git: [790, 600, "perkakas"], fedora: [980, 680, "perkakas"], sql: [1290, 680, "perkakas"],
  techstack: [150, 980, "tech"], frontend: [390, 1055, "tech"], backend: [630, 975, "tech"],
  database: [870, 1050, "tech"], devops: [1110, 975, "tech"], keamanan: [1310, 1065, "tech"],
  mobile: [150, 1235, "tech"], game: [390, 1300, "tech"], iot: [630, 1230, "tech"],
  data: [870, 1300, "tech"], ai: [1110, 1230, "tech"], bahasalain: [1310, 1310, "tech"],
};
const KELUARGA = {
  web: ["Web", 60, 60], sistem: ["Sistem", 640, 50], jvm: ["JVM & .NET", 1080, 50],
  skrip: ["Skrip", 60, 835], perkakas: ["Perkakas & data", 1110, 835],
  tech: ["Tech stack", 60, 1405],
};

const KONSEP = [
  ["Variabel & tipe", /variabel|tipe data|\bval\b|\bvar\b|konstanta/i],
  ["Percabangan", /percabangan|kendali alur|\bif\b|switch|\bwhen\b|select case|\bcase\b/i],
  ["Perulangan", /perulangan|loop|\bfor\b|while|iterasi|iterator/i],
  ["Fungsi", /fungsi|function|method|\bsub\b|prosedur|closure|lambda/i],
  ["Koleksi", /array|\blist\b|slice|koleksi|collection|\bmap\b|dict|hash|\bset\b|\bvec\b|tuple|stl/i],
  ["Teks & regex", /string|teks|regex|ekspresi reguler/i],
  ["Objek & class", /class|objek|oop|struct|record|interface|trait|pewarisan|inheritance|polymorph/i],
  ["Galat", /exception|galat|error|panic|\bresult\b/i],
  ["Berkas & I/O", /berkas|\bfile\b|i\/o|input|output|json|csv/i],
  ["Pengujian", /pengujian|\btest|\buji|debug/i],
  ["Konkurensi", /konkurensi|thread|goroutine|async|await|paralel|bersamaan|coroutine|race/i],
  ["Algoritma", /rekursi|algoritma|big-o|sorting|pengurutan|pencarian|kompleksitas/i],
  ["Modul & paket", /modul|paket|package|import|namespace|crate|dependensi|maven|gradle/i],
  ["Database", /database|\bsql\b|query|join|tabel|jdbc|pdo|transaksi/i],
];

export async function layarLangit(_p, _ctx) {
  const d = await ambilLangit(true);
  const totalMateri = d.bahasa.reduce((a, b) => a + b.materi.length, 0);
  const menyala = d.bahasa.reduce((a, b) => a + b.materi.filter((m) => m.status === "selesai").length, 0);

  const kepala = h("header.kepala-besar.bimasakti-kepala", {},
    h("span.mata", {}, "Peta bintang"),
    h("h1", {}, "Langit"),
    h("p.kepala-sub", {}, `${d.bahasa.length} kurikulum, ${totalMateri} materi. Tiap materi satu bintang; `
      + (menyala ? `${menyala} sudah menyala karena sudah kamu baca.`
                 : "belum ada yang menyala. Baca satu materi untuk menyalakan yang pertama.")));

  const lapisJalur = s("g");
  const lapisBintang = s("g");
  const lapisLabel = s("g");
  const pusat = {};
  const bintangPer = {};
  let cadangan = 0;

  for (const [nama, x, y] of Object.values(KELUARGA)) {
    lapisLabel.appendChild(s("text", { kelas: "langit-keluarga", x, y }, nama));
  }

  d.bahasa.forEach((b, urut) => {
    const [cx, cy] = TATA[b.key] || [140 + (cadangan++) * 180, 820];
    pusat[b.key] = [cx, cy];
    const titik = bentukRasi(b.materi.length, "langit·" + b.key, 150, 112).map(([x, y]) => [cx + x, cy + y]);
    const kelompok = s("g", { kelas: "rasi-kelompok langit-rasi", "data-key": b.key });
    const r = b.materi.map((m) => jariBintang(magStatus(m), 0.62));
    const awalBab = new Set((b.bab || []).map((x) => x.materi[0]));
    bintangPer[b.key] = [];
    b.materi.forEach((m, i) => {
      // Garis putus di batas bab: tiap bab jadi rasi kecil di dalam rasi besar.
      if (i > 0 && !awalBab.has(i)) {
        const terang = b.materi[i - 1].status === "selesai" && m.status === "selesai";
        const g = ruas(titik[i - 1], titik[i], r[i - 1], r[i], terang ? "rasi-garis rasi-garis-terang" : "rasi-garis");
        if (g) kelompok.appendChild(g);
      }
      const bt = bintangSvg(m, titik[i][0], titik[i][1], r[i], `#/materi/${b.key}/${i}`);
      bt.dataset.key = b.key;
      bt.dataset.indeks = i;
      bt.style.setProperty("--i", urut * 3 + (i % 9));
      kelompok.appendChild(bt);
      bintangPer[b.key].push(bt);
    });
    const selesai = b.materi.filter((m) => m.status === "selesai").length;
    const berikut = berikutDari(b.materi);
    if (selesai && berikut !== null) lapisLabel.appendChild(reticle(titik[berikut][0], titik[berikut][1], r[berikut]));
    const label = s("a", { kelas: "langit-nama", href: "#/bahasa/" + b.key, "data-key": b.key,
                           "aria-label": `${b.label}: ${selesai} dari ${b.materi.length} materi sudah dibaca` },
      s("text", { x: cx, y: cy + 82, "text-anchor": "middle", kelas: "langit-nama-teks" }, b.label),
      s("text", { x: cx, y: cy + 100, "text-anchor": "middle", kelas: "langit-nama-angka" },
        `${selesai}/${b.materi.length}`));
    lapisBintang.appendChild(kelompok);
    lapisLabel.appendChild(label);
  });

  const svg = s("svg", { viewBox: `0 0 ${W} ${H}`, kelas: "rasi-svg langit-svg", preserveAspectRatio: "xMidYMid meet" },
    lapisJalur, lapisBintang, lapisLabel);
  const peta = h("div.rasi.langit-peta", {},
    h("p.rasi-ringkasan", {}, `Peta langit seluruh kurikulum: ${menyala} dari ${totalMateri} bintang menyala.`),
    svg);
  if (tingkatGerak() === "penuh") peta.classList.add("rasi-hidup");
  const tip = pasangTip(peta);
  const keterangan = h("p.langit-keterangan", { "aria-live": "polite" });

  svg.addEventListener("pointerover", (e) => {
    const bt = e.target.closest && e.target.closest(".rasi-bintang");
    if (!bt) return;
    const b = d.bahasa.find((x) => x.key === bt.dataset.key);
    const m = b.materi[Number(bt.dataset.indeks)];
    tip.tunjuk(bt, m.judul, `${b.label} · ${m.terkunci ? "masih terkunci" : KATA_STATUS[m.status] || ""}`);
  });
  svg.addEventListener("pointerleave", () => tip.sembunyi());

  // ---- profesi: garis antar rasi bekal
  function tandaiProfesi(id) {
    isikan(lapisJalur);
    svg.classList.remove("ada-profesi");
    for (const k of svg.querySelectorAll(".langit-terpilih")) k.classList.remove("langit-terpilih");
    const p = d.profesi.find((x) => x.id === id);
    if (!p) { keterangan.textContent = ""; return; }
    // Satu kelompok bekal = "salah satu dari". Kelompok berurutan disambung
    // seperti kipas: tiap pilihan di kelompok ini ke tiap pilihan berikutnya.
    const kelompok = p.bekal.map((g) => g.filter((k) => pusat[k])).filter((g) => g.length);
    for (let i = 1; i < kelompok.length; i++) {
      for (const ka of kelompok[i - 1]) {
        for (const kb of kelompok[i]) {
          const [a, b] = [pusat[ka], pusat[kb]];
          const mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2 - 40;
          lapisJalur.appendChild(s("path", { d: `M${a[0]},${a[1]} Q${mx},${my} ${b[0]},${b[1]}`,
            kelas: "langit-profesi-garis", fill: "none" }));
        }
      }
    }
    svg.classList.add("ada-profesi");
    for (const k of kelompok.flat()) {
      for (const el of svg.querySelectorAll(`[data-key="${k}"]`)) el.classList.add("langit-terpilih");
    }
    const label = (k) => (d.bahasa.find((b) => b.key === k) || {}).label || k;
    const bagian = kelompok.map((g) => (g.length > 1 ? `salah satu dari ${g.map(label).join(", ")}` : label(g[0])));
    keterangan.textContent = `${p.nama} berbekal ${bagian.join("; lalu ")}.`;
  }
  const pilihProfesi = h("select.langit-pilih", { "aria-label": "Hubungkan rasi lewat profesi" },
    h("option", { value: "" }, "Tanpa profesi"),
    d.profesi.map((p) => h("option", { value: p.id, selected: p.id === d.tujuan }, p.nama)));
  pilihProfesi.addEventListener("change", () => tandaiProfesi(pilihProfesi.value));

  // ---- konsep: materi sekonsep menyala di semua kurikulum
  let konsepKini = null;
  const tombolKonsep = KONSEP.map(([nama, pola]) => {
    const t = h("button.tbl.tbl-kecil.tbl-hantu.langit-konsep", { type: "button", "aria-pressed": "false" }, nama);
    t.addEventListener("click", () => {
      konsepKini = konsepKini === nama ? null : nama;
      for (const x of tombolKonsep) x.setAttribute("aria-pressed", String(x.textContent === konsepKini));
      let jumlah = 0;
      const kurikulum = new Set();
      for (const b of d.bahasa) {
        b.materi.forEach((m, i) => {
          const cocok = !!konsepKini && pola.test(m.judul.replace(/^\s*\d+\.\s*/, ""));
          bintangPer[b.key][i].classList.toggle("rasi-konsep", cocok);
          if (cocok) { jumlah++; kurikulum.add(b.label); }
        });
      }
      svg.classList.toggle("ada-konsep", !!konsepKini);
      keterangan.textContent = konsepKini
        ? `${konsepKini}: ${jumlah} materi di ${kurikulum.size} kurikulum. Konsepnya sama, cara menulisnya yang berbeda.`
        : "";
    });
    return t;
  });

  const legenda = h("div.langit-legenda", { "aria-hidden": "true" },
    [["selesai", "sudah dibaca"], ["sebagian", "dibaca sebagian"], ["baru", "belum dibaca"], ["terkunci", "terkunci"]]
      .map(([st, kata]) => {
        const m = { status: st === "terkunci" ? "baru" : st, terkunci: st === "terkunci" };
        return h("span.langit-legenda-butir", {},
          s("svg", { viewBox: "-10 -10 20 20", width: 20, height: 20 },
            s("circle", { r: jariBintang(magStatus(m), 0.9).toFixed(2), kelas: "rasi-titik rasi-" + st })), kata);
      }),
    h("span.langit-legenda-butir", {},
      s("svg", { viewBox: "-16 -16 32 32", width: 24, height: 24 }, reticle(0, 0, 2)), "berikutnya"));

  const el = h("div.bimasakti", {},
    kepala,
    h("div.langit-alat", {},
      h("label.langit-label", {}, "Hubungkan lewat profesi", pilihProfesi),
      h("a.tbl.tbl-kecil.tbl-hantu", { href: "#/karier" }, "Buka Peta Karier")),
    h("div.langit-konsep-deret", { role: "group", "aria-label": "Nyalakan konsep yang sama di semua kurikulum" },
      h("span.langit-label", {}, "Konsep yang sama"), tombolKonsep),
    keterangan,
    peta,
    legenda);
  if (d.tujuan) tandaiProfesi(d.tujuan);
  return { el, judul: "Langit" };
}
