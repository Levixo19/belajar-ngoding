/* Layar Peta Karier: 21 profesi yang bisa dicapai dari kurikulum aplikasi ini.
 *
 * Empat bagian, satu pertanyaan masing-masing:
 *   1. Konstelasi + panel detail  — "profesi apa saja, dan seberapa siap aku?"
 *   2. Kuis kecocokan             — "yang mana yang cocok untukku?"
 *   3. Perencana perpindahan      — "dari sini ke sana lewat mana, kurang apa?"
 *   4. Indeks rumpun              — daftar utuh, untuk yang lebih suka membaca.
 *
 * Tidak ada satu angka pun yang dihitung di sini. Kesiapan, skor kuis, dan
 * jalur datang dari pelajar/karier.py lewat /api/karier*, persis yang dibaca
 * layar terminal. Layar ini cuma menggambar dan memilih.
 *
 * Memilih profesi TIDAK memicu router: alamatnya diganti lewat
 * history.replaceState supaya konstelasi yang sedang dilihat tidak digambar
 * ulang dan posisi gulir tidak lompat. Membuka #/karier/<id> langsung tetap
 * mendarat di profesi itu.
 *
 * Importir: aplikasi.js.
 */

import { api, h, isikan, bulat } from "./inti.js";
import { ikon } from "./ikon.js";

const NS = "http://www.w3.org/2000/svg";
// Tangga karier: BARIS adalah rumpun, KOLOM adalah jenjang (pemula,
// menengah, senior). Versi pertamanya konstelasi melingkar seperti proyek
// networking, dan di kanvas selebar ini (sekitar 680 px di samping panel)
// hasilnya benang kusut: garis lintas-rumpun bersilangan di tengah dan nama
// rumpun menimpa simpul. Kisi memberi tiap label tempat tetap, dan arah
// "naik" terbaca langsung sebagai gerak ke kanan.
const W = 860;
const KIRI = 168;
const ATAS = 48;
const BARIS = 84;
const KOLOM = (W - KIRI) / 3;
const LANGKAH = 25;
const JENJANG_KOLOM = { pemula: 0, menengah: 1, senior: 2 };

function tataLetak(data) {
  const pos = new Map();
  data.rumpun.forEach((r, i) => {
    for (const [jenjang, j] of Object.entries(JENJANG_KOLOM)) {
      const sel = data.profesi.filter((p) => p.rumpun === r.id && p.jenjang === jenjang);
      const tinggi = (sel.length - 1) * LANGKAH;
      sel.forEach((p, k) => {
        pos.set(p.id, {
          x: KIRI + j * KOLOM + 22,
          y: ATAS + i * BARIS + BARIS / 2 - tinggi / 2 + k * LANGKAH,
        });
      });
    }
  });
  return { pos, tinggi: ATAS + data.rumpun.length * BARIS + 12 };
}

function s(tag, sifat = {}, ...anak) {
  const el = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(sifat)) {
    if (v === null || v === undefined || v === false) continue;
    el.setAttribute(k, String(v));
  }
  for (const x of anak.flat()) if (x) el.append(x);
  return el;
}

/** Garis antar dua simpul: lengkung-S kalau beda kolom, busur ke kiri kalau
 *  satu kolom (supaya tidak menembus label di kanan simpul). */
function jalurGaris(a, b) {
  if (Math.abs(a.x - b.x) < 1) {
    // Dipatok 18 unit: lebih lebar dari itu, busurnya menembus nama rumpun.
    const lengkung = Math.min(18, 8 + Math.abs(a.y - b.y) * 0.05);
    return `M${a.x},${a.y.toFixed(1)} C${a.x - lengkung},${a.y.toFixed(1)} `
      + `${b.x - lengkung},${b.y.toFixed(1)} ${b.x},${b.y.toFixed(1)}`;
  }
  const tengah = (a.x + b.x) / 2;
  return `M${a.x},${a.y.toFixed(1)} C${tengah},${a.y.toFixed(1)} `
    + `${tengah},${b.y.toFixed(1)} ${b.x},${b.y.toFixed(1)}`;
}

const pendek = (nama) => nama.replace(/\s*\(.*?\)\s*/g, " ").replace(/ \/ .*$/, "").trim();

function persenTeks(p) { return `${bulat(p)}%`; }

/** Cincin kesiapan untuk panel. */
function cincin(persen, ukuran) {
  const r = ukuran / 2 - 4;
  const keliling = 2 * Math.PI * r;
  return s("svg", { class: "kr-cincin", width: ukuran, height: ukuran,
                    viewBox: `0 0 ${ukuran} ${ukuran}`, "aria-hidden": "true" },
    s("circle", { cx: ukuran / 2, cy: ukuran / 2, r, class: "kr-cincin-alas" }),
    persen > 0 ? s("circle", {
      cx: ukuran / 2, cy: ukuran / 2, r, class: "kr-cincin-isi",
      "stroke-dasharray": `${(keliling * persen / 100).toFixed(2)} ${keliling.toFixed(2)}`,
      transform: `rotate(-90 ${ukuran / 2} ${ukuran / 2})`,
    }) : null);
}

export async function layarKarier({ key: id }) {
  const data = await api.ambil("/api/karier");
  const perId = new Map(data.profesi.map((p) => [p.id, p]));
  const kur = data.kurikulum;

  const urutSiap = [...data.profesi].sort((a, b) => b.kesiapan - a.kesiapan);
  const palingSiap = urutSiap[0];
  let terpilih = (id && perId.get(id)) || (palingSiap.kesiapan > 0 ? palingSiap
    : perId.get("frontend-developer")) || data.profesi[0];
  let saringRumpun = "semua";

  /* ------------------------------------------------------- konstelasi */
  const { pos, tinggi: H } = tataLetak(data);
  const tetangga = new Map(data.profesi.map((p) => [p.id, new Set()]));
  for (const e of data.sisi) {
    tetangga.get(e.a).add(e.b);
    tetangga.get(e.b).add(e.a);
  }

  const garis = data.sisi.map((e) => {
    return s("path", {
      d: jalurGaris(pos.get(e.a), pos.get(e.b)),
      class: "kr-sisi kr-sisi-" + e.jenis, pathLength: 1,
      "data-a": e.a, "data-b": e.b,
    });
  });

  const simpul = data.profesi.map((p) => {
    const t = pos.get(p.id);
    const R = p.jenjang === "senior" ? 8 : p.jenjang === "menengah" ? 7 : 6;
    const keliling = 2 * Math.PI * (R + 4);
    const g = s("g", {
      class: "kr-simpul", tabindex: 0, role: "button",
      "data-id": p.id, "data-rumpun": p.rumpun,
      "aria-label": `${p.nama}, kesiapan ${bulat(p.kesiapan)} persen`,
      transform: `translate(${t.x.toFixed(1)},${t.y.toFixed(1)})`,
    },
      s("rect", { x: -R - 8, y: -LANGKAH / 2, width: KOLOM - 14, height: LANGKAH,
                  rx: 6, class: "kr-sasaran" }),
      s("circle", { r: R + 4, class: "kr-cincin-alas" }),
      p.kesiapan > 0 ? s("circle", {
        r: R + 4, class: "kr-cincin-isi",
        "stroke-dasharray": `${(keliling * p.kesiapan / 100).toFixed(2)} ${keliling.toFixed(2)}`,
        transform: "rotate(-90)",
      }) : null,
      s("circle", { r: R, class: "kr-inti" }),
      s("text", { class: "kr-label", x: R + 10, y: 0, dy: "0.35em" },
        document.createTextNode(pendek(p.nama))));
    g.addEventListener("click", () => pilih(p.id, true));
    g.addEventListener("keydown", (ev) => {
      if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); pilih(p.id, true); }
    });
    g.addEventListener("pointerenter", () => sorot(p.id));
    g.addEventListener("pointerleave", () => sorot(null));
    g.addEventListener("focus", () => sorot(p.id));
    g.addEventListener("blur", () => sorot(null));
    return g;
  });

  // Pita baris selang-seling + nama rumpun di kiri + judul jenjang di atas.
  const pita = data.rumpun.map((r, i) => s("rect", {
    x: 0, y: ATAS + i * BARIS, width: W, height: BARIS,
    class: "kr-pita" + (i % 2 ? " kr-pita-genap" : ""), "data-rumpun": r.id,
  }));
  const label = data.rumpun.map((r, i) => s("text", {
    class: "kr-rumpun", x: 20, y: ATAS + i * BARIS + BARIS / 2, dy: "0.35em",
    "data-rumpun": r.id,
  }, document.createTextNode(r.label)));
  const kepalaKolom = Object.keys(JENJANG_KOLOM).map((j, i) => s("text", {
    class: "kr-kolom", x: KIRI + i * KOLOM + 14, y: 28,
  }, document.createTextNode(data.jenjang[j].startsWith("Bisa") ? "Pemula"
    : j === "menengah" ? "Menengah" : "Senior")));

  const svg = s("svg", {
    viewBox: `0 0 ${W} ${H}`, class: "kr-graf", role: "group",
    "aria-label": "Konstelasi profesi. Pilih satu untuk melihat rinciannya.",
  }, s("g", {}, pita), s("g", {}, kepalaKolom), s("g", {}, label),
     s("g", {}, garis), s("g", {}, simpul));

  // Dihitung di luar classList.toggle: pemanen kelas di test_web membaca
  // setiap literal di dalam panggilan itu sebagai nama kelas.
  const tersaring = (rumpun) => saringRumpun !== "semua" && rumpun !== saringRumpun;

  function sorot(pid) {
    const fokus = pid || terpilih.id;
    const dekat = tetangga.get(fokus);
    for (const g of simpul) {
      const ini = g.dataset.id;
      const jauh = (ini !== fokus && !dekat.has(ini)) || tersaring(g.dataset.rumpun);
      g.classList.toggle("redup", jauh);
      g.classList.toggle("dipilih", ini === terpilih.id);
      // Label hanya untuk yang sedang dibicarakan: dua puluh satu nama
      // sekaligus di kanvas selebar ini saling menimpa.
      g.classList.toggle("tampak", ini === fokus || ini === terpilih.id || dekat.has(ini));
      g.setAttribute("aria-pressed", String(ini === terpilih.id));
    }
    for (const p of garis) {
      const kena = p.dataset.a === fokus || p.dataset.b === fokus;
      p.classList.toggle("nyala", kena);
      p.classList.toggle("redup", !kena);
    }
    for (const t of [...label, ...pita]) {
      const jauh = tersaring(t.dataset.rumpun);
      t.classList.toggle("redup", jauh);
    }
  }

  /* ----------------------------------------------------- panel detail */
  const panel = h("aside.kr-panel", { "aria-live": "polite" });

  function pilih(pid, dariPengguna) {
    const p = perId.get(pid);
    if (!p) return;
    terpilih = p;
    isikan(panel, panelDetail(p, data, pilih));
    panel.scrollTop = 0;
    sorot(null);
    perbaruiTransisi();
    if (dariPengguna) {
      // replaceState, bukan location.hash: router tidak perlu menggambar
      // ulang halaman yang sedang dilihat hanya karena satu simpul dipilih.
      try { history.replaceState(null, "", "#/karier/" + pid); } catch (e) { /* abaikan */ }
    }
  }

  const saring = h("div.kr-saring", { role: "radiogroup", "aria-label": "Saring rumpun" });
  for (const r of [{ id: "semua", label: "Semua" }, ...data.rumpun]) {
    const b = h("button.kr-chip", {
      type: "button", role: "radio", "aria-checked": String(r.id === "semua"),
      onclick: () => {
        saringRumpun = r.id;
        for (const x of saring.children) x.setAttribute("aria-checked", String(x === b));
        sorot(null);
      },
    }, r.label);
    saring.append(b);
  }

  /* ---------------------------------------------------- kuis kecocokan */
  const jawaban = data.kuis.map(() => null);
  const hasilKuis = h("div.kr-hasil-kuis", { "aria-live": "polite" });
  const tblKuis = h("button.tbl.tbl-utama", { type: "button", disabled: true },
    "Lihat yang cocok", ikon("lanjut", { ukuran: 16 }));
  const soal = data.kuis.map((q, i) => h("fieldset.kr-soal", {},
    h("legend", {}, h("span.kr-soal-no", {}, String(i + 1).padStart(2, "0")), q.q),
    h("div.kr-opsi", {}, q.opsi.map((o, j) => h("button.kr-pilihan", {
      type: "button", "aria-pressed": "false",
      onclick: (ev) => {
        jawaban[i] = j;
        for (const b of ev.currentTarget.parentElement.children) {
          b.setAttribute("aria-pressed", String(b === ev.currentTarget));
        }
        tblKuis.disabled = jawaban.filter((x) => x !== null).length < 3;
      },
    }, o)))));

  const keKonstelasi = () => svg.scrollIntoView({ block: "center" });

  tblKuis.addEventListener("click", async () => {
    tblKuis.disabled = true;
    try {
      const r = await api.ambil("/api/karier/kuis", {
        pilihan: jawaban.map((x) => (x === null ? "" : String(x))).join(","),
      });
      isikan(hasilKuis, r.hasil.length
        ? h("ol.kr-juara", {}, r.hasil.map((x, i) => {
            const p = perId.get(x.id);
            return h("li", {},
              h("span.kr-juara-no", {}, String(i + 1)),
              h("div.isi", {},
                h("div.judul", {}, p.nama),
                h("div.ket", {}, "Cocok karena: "
                  + x.cocok.map((k) => data.keahlian[k] || k).join(", "))),
              h("button.tbl.tbl-hantu.tbl-kecil", {
                type: "button", onclick: () => { pilih(p.id, true); keKonstelasi(); },
              }, "Lihat profesi"));
          }))
        : h("p.kr-catatan", {}, "Jawabanmu belum cukup condong ke satu arah. "
            + "Coba jawab semua soal."));
    } finally {
      tblKuis.disabled = false;
    }
  });

  /* ----------------------------------------------- perencana transisi */
  const pilihDari = h("select", { "aria-label": "Profesi asal" },
    data.profesi.map((p) => h("option", { value: p.id }, p.nama)));
  pilihDari.value = (palingSiap.kesiapan > 0 ? palingSiap : perId.get("qa-engineer")).id;
  const pilihKe = h("select", { "aria-label": "Profesi tujuan" },
    data.profesi.map((p) => h("option", { value: p.id }, p.nama)));
  const hasilJalur = h("div.kr-jalur", { "aria-live": "polite" });
  let nomorJalur = 0;

  async function hitungJalur() {
    const nomor = ++nomorJalur;
    if (pilihDari.value === pilihKe.value) {
      isikan(hasilJalur, h("p.kr-catatan", {}, "Asal dan tujuannya sama. Pilih profesi lain."));
      return;
    }
    const r = await api.ambil("/api/karier/jalur", { dari: pilihDari.value, ke: pilihKe.value });
    if (nomor !== nomorJalur) return;
    if (!r.jalur.length) {
      isikan(hasilJalur, h("p.kr-catatan", {}, "Belum ada jalur yang tercatat di antara keduanya."));
      return;
    }
    isikan(hasilJalur,
      h("ol.kr-langkah", {}, r.jalur.map((pid, i) => h("li", {},
        h("button.kr-langkah-tbl", { type: "button", onclick: () => pilih(pid, true) },
          h("span.kr-langkah-no", {},
            i === 0 ? "sekarang" : i === r.jalur.length - 1 ? "tujuan" : "lewat"),
          h("span", {}, perId.get(pid).nama))))),
      r.celah.length
        ? h("div.kr-celah", {},
            h("h3", {}, "Bekal yang perlu ditambah"),
            h("ul", {}, r.celah.map((grup) => h("li", {},
              grup.map((k, i) => [
                i ? h("span.kr-atau", {}, "atau") : null,
                h("a", { href: "#/bahasa/" + k }, kur[k].label,
                  h("span.kr-persen", {}, persenTeks(kur[k].persen))),
              ])))))
        : h("p.kr-catatan", {}, "Bekal profesi tujuan sudah tercakup bekal profesi asal. "
            + "Yang membedakan tinggal pengalaman dan kedalaman."));
  }

  function perbaruiTransisi() {
    pilihKe.value = terpilih.id;
    hitungJalur();
  }
  pilihDari.addEventListener("change", hitungJalur);
  pilihKe.addEventListener("change", () => pilih(pilihKe.value, true));

  /* ---------------------------------------------------- indeks rumpun */
  const indeks = h("div.kr-indeks", {}, data.rumpun.map((r) => h("section.kr-rumpun-kartu", {},
    h("h3", {}, r.label),
    h("p", {}, r.ket),
    h("ul", {}, data.profesi.filter((p) => p.rumpun === r.id).map((p) => h("li", {},
      h("button", { type: "button", onclick: () => { pilih(p.id, true); keKonstelasi(); } },
        h("span", {}, p.nama),
        h("span.kr-persen", {}, persenTeks(p.kesiapan)))))))));

  /* ------------------------------------------------------------ rangka */
  const el = h("div.masuk", {},
    h("header.kepala-besar.kr-kepala", {},
      h("span.mata", {}, "Peta karier"),
      h("h1", {}, `${data.profesi.length} profesi, satu jalan belajar.`),
      h("p.kepala-sub", {},
        "Kesiapan tiap profesi dihitung dari kurikulum yang sudah kamu kerjakan "
        + "di aplikasi ini. Arahkan kursor ke sebuah profesi untuk melihat ke mana "
        + "ia terhubung, lalu pilih untuk membaca rinciannya."),
      h("div.kr-aksi", {},
        h("button.tbl.tbl-utama", {
          type: "button",
          onclick: () => document.getElementById("kr-cocok").scrollIntoView({ block: "start" }),
        }, "Cari yang cocok", ikon("lanjut", { ukuran: 16 })),
        palingSiap.kesiapan > 0
          ? h("button.kr-tautan", { type: "button", onclick: () => pilih(palingSiap.id, true) },
              `Paling siap: ${pendek(palingSiap.nama)} (${persenTeks(palingSiap.kesiapan)})`)
          : null)),

    saring,
    h("div.kr-utama", {},
      h("figure.kr-kanvas", {},
        svg,
        h("figcaption.kr-legenda", {},
          h("span", {}, h("i.kr-leg-naik"), "Jalur naik"),
          h("span", {}, h("i.kr-leg-dekat"), "Keahlian beririsan"),
          h("span", {}, h("i.kr-leg-siap"), "Kesiapanmu"),
          h("span", {}, "Makin ke kanan, makin senior perannya."))),
      panel),

    h("section.kr-bagian#kr-cocok", { "aria-labelledby": "kr-judul-cocok" },
      h("div.kr-bagian-kepala", {},
        h("span.mata", {}, "Kuis kecocokan"),
        h("h2#kr-judul-cocok", {}, "Mana yang cocok denganmu?"),
        h("p", {}, "Enam pertanyaan tentang apa yang membuatmu betah bekerja. "
          + "Tidak ada jawaban yang salah; hasilnya cuma titik mulai.")),
      h("div.kr-soal-kisi", {}, soal),
      h("div.kr-aksi", {}, tblKuis),
      hasilKuis),

    h("section.kr-bagian", { "aria-labelledby": "kr-judul-pindah" },
      h("div.kr-bagian-kepala", {},
        h("span.mata", {}, "Perencana perpindahan"),
        h("h2#kr-judul-pindah", {}, "Dari sini ke sana, lewat mana?"),
        h("p", {}, "Jalur dihitung dari hubungan antarprofesi. Peran senior "
          + "dihindari sebagai batu loncatan, karena jarang ada yang menjadi "
          + "arsitek hanya untuk pindah ke peran lain.")),
      h("div.kr-pilih-jalur", {},
        h("label", {}, h("span", {}, "Sekarang"), pilihDari),
        h("span.kr-panah", { "aria-hidden": "true" }, ikon("lanjut", { ukuran: 20 })),
        h("label", {}, h("span", {}, "Ingin menjadi"), pilihKe)),
      hasilJalur),

    h("section.kr-bagian", { "aria-labelledby": "kr-judul-rumpun" },
      h("div.kr-bagian-kepala", {},
        h("span.mata", {}, "Indeks"),
        h("h2#kr-judul-rumpun", {}, `${data.rumpun.length} rumpun, dibaca utuh.`)),
      indeks),
  );

  pilih(terpilih.id, false);
  return { el, judul: "Peta Karier" };
}

/* ----------------------------------------------------------- panel isi */

function panelDetail(p, data, pilih) {
  const kur = data.kurikulum;
  const blok = (judul, ...isi) => h("section.kr-blok", {}, h("h3", {}, judul), ...isi);
  const daftar = (butir) => h("ul.kr-daftar", {}, butir.map((b) => h("li", {}, b)));
  const chip = (ids) => h("div.kr-chip-deret", {}, ids.map((pid) => {
    const q = data.profesi.find((x) => x.id === pid);
    return q ? h("button.kr-chip", { type: "button", onclick: () => pilih(pid, true) },
                 pendek(q.nama)) : null;
  }));
  const rumpun = data.rumpun.find((r) => r.id === p.rumpun) || {};

  return h("div.kr-panel-isi", {},
    h("div.kr-panel-kepala", {},
      h("div", {},
        h("span.mata", {}, rumpun.label),
        h("h2", {}, p.nama),
        h("span.pil", {}, data.jenjang[p.jenjang])),
      h("div.kr-siap", {}, cincin(p.kesiapan, 68),
        h("span.kr-siap-angka", {}, persenTeks(p.kesiapan)),
        h("span.kr-siap-ket", {}, "siap"))),
    h("p.kr-ringkas", {}, p.ringkas),

    blok("Bekal dari aplikasi ini",
      h("ul.kr-bekal", {}, p.kelompok.map((k) => h("li", {},
        h("div.kr-bekal-nama", {},
          k.pilihan.length > 1
            ? [h("span.kr-atau", {}, "salah satu"), k.pilihan.map((x) => h("a", {
                href: "#/bahasa/" + x, kelas: x === k.wakil ? "wakil" : "",
              }, kur[x].label))]
            : h("a", { href: "#/bahasa/" + k.wakil }, kur[k.wakil].label)),
        h("div.kr-bekal-bilah", { role: "img", "aria-label": `${bulat(k.persen)} persen` },
          h("i", { gaya: { width: `${Math.max(0, Math.min(100, k.persen))}%` } })),
        h("span.kr-persen", {}, persenTeks(k.persen))))),
      p.pelengkap.length
        ? h("p.kr-catatan", {}, "Pelengkap: ",
            p.pelengkap.map((x, i) => [i ? ", " : "", h("a", { href: "#/bahasa/" + x }, kur[x].label)]))
        : null),

    blok("Sehari-hari", daftar(p.harian)),
    blok("Keahlian", h("div.kr-tag-deret", {},
      p.keahlian.map((k) => h("span.kr-tag", {}, data.keahlian[k] || k)))),
    blok("Alat yang sering dipakai", h("div.kr-tag-deret", {},
      p.alat.map((a) => h("span.kr-tag.kr-tag-kode", {}, a)))),

    p.gaji
      ? blok("Gaji di Indonesia",
          h("p.kr-gaji", {}, p.gaji.rentang),
          h("p.kr-catatan", {}, p.gaji.konteks, " Sumber: ",
            h("a", { href: p.gaji.url, target: "_blank", rel: "noopener noreferrer" },
              p.gaji.sumber), `, diperiksa ${p.gaji.diperiksa}.`))
      : blok("Gaji di Indonesia", h("p.kr-catatan", {},
          "Belum ada sumber publik yang angkanya bisa diperiksa untuk peran ini, "
          + "jadi sengaja tidak ditebak.")),

    blok("Sertifikasi", p.sertifikasi.length
      ? h("ul.kr-daftar", {}, p.sertifikasi.map((x) => h("li", {},
          x.nama, h("span.kr-catatan", {}, ` · ${x.penerbit} · ${x.tingkat}`))))
      : h("p.kr-catatan", {}, "Tidak ada sertifikasi yang diakui luas untuk peran ini. "
          + "Portofolio dan kontribusi nyata yang berbicara.")),

    blok("Jalan masuk", h("p", {}, p.masuk)),
    blok("Proyek untuk portofolio", daftar(p.proyek)),
    p.naik.length ? blok("Langkah berikutnya", chip(p.naik)) : null,
    blok("Profesi yang dekat", chip(p.dekat)),
    blok("Bacaan lanjut",
      h("ul.kr-daftar.kr-tautan-luar", {},
        p.peta.map((slug) => h("li", {}, h("a", {
          href: "https://roadmap.sh/" + slug, target: "_blank", rel: "noopener noreferrer",
        }, "roadmap.sh/" + slug))),
        p.sumber.map((x) => h("li", {}, h("a", {
          href: x.url, target: "_blank", rel: "noopener noreferrer",
        }, x.judul))),
        h("li", {}, h("a", {
          href: "#/pustaka?kurikulum=" + p.kelompok[0].wakil,
        }, `Pustaka: bacaan ${kur[p.kelompok[0].wakil].label}`)))),
  );
}
