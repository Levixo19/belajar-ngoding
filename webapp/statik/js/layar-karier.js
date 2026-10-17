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
import { sampul } from "./sampul.js";
import { gerakPenuh } from "./gerak.js";
import { saatSiap } from "./layar-belajar.js";

const NS = "http://www.w3.org/2000/svg";
// Tangga karier: BARIS adalah rumpun, KOLOM adalah jenjang (pemula,
// menengah, senior). Versi pertamanya konstelasi melingkar, versi keduanya
// menggambar SEMUA sisi sekaligus sebagai kurva-S -- dua-duanya benang kusut:
// empat puluhan garis abu yang bersilangan, plus sisi antar-profesi SATU
// jenjang yang dirutekan menyusuri kolom simpul dan menembus label-label di
// bawahnya. Aturannya sekarang:
//   * Garis cuma digambar untuk profesi yang sedang dipilih/disorot. Peta
//     dalam keadaan diam adalah kisi nama yang tenang, bukan gulungan kabel.
//   * Garis selalu berangkat dari UJUNG label sumber dan tiba di sisi kiri
//     simpul tujuan, jadi tidak pernah melintasi huruf.
//   * Tetangga dalam satu kolom tidak digaris sama sekali; simpulnya diberi
//     cincin. Hubungan itu sudah dibawa daftar "dekat" di panel.
// Tinggi tiap baris dihitung dari sel terpadatnya, bukan dipatok: tiga
// profesi menengah di satu rumpun tidak lagi berdesakan dalam 84 unit.
const W = 1040;
const KIRI = 196;
const ATAS = 52;
const KOLOM = (W - KIRI) / 3;
const LANGKAH = 32;
const BARIS_MIN = 76;
const JENJANG_KOLOM = { pemula: 0, menengah: 1, senior: 2 };

function tataLetak(data) {
  const pos = new Map();
  const baris = [];
  let y = ATAS;
  for (const r of data.rumpun) {
    const sel = Object.keys(JENJANG_KOLOM).map((jenjang) =>
      data.profesi.filter((p) => p.rumpun === r.id && p.jenjang === jenjang));
    const tinggi = Math.max(BARIS_MIN, Math.max(...sel.map((x) => x.length)) * LANGKAH + 28);
    sel.forEach((isi, j) => {
      const blok = (isi.length - 1) * LANGKAH;
      isi.forEach((p, k) => pos.set(p.id, {
        x: KIRI + j * KOLOM + 24,
        y: y + tinggi / 2 - blok / 2 + k * LANGKAH,
        kolom: j,
        R: p.jenjang === "senior" ? 8 : p.jenjang === "menengah" ? 7 : 6,
      }));
    });
    baris.push({ id: r.id, label: r.label, y, tinggi });
    y += tinggi;
  }
  return { pos, baris, tinggi: y + 12 };
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

/** Garis dari ujung label simpul KIRI ke sisi kiri simpul KANAN, dirutekan
 *  seperti peta metro: mendatar ke BATANG di talang sesudah kolom simpul
 *  kiri, tegak di sepanjang batang itu, lalu mendatar masuk ke simpul kanan.
 *  Semua garis dari satu simpul berbagi batang yang sama, jadi sepuluh
 *  hubungan terbaca sebagai satu pohon bercabang, bukan sepuluh kurva yang
 *  saling melintas. Sudutnya dibulatkan dengan radius R_SUDUT. */
const R_SUDUT = 9;
function jalurGaris(kiri, ujungLabel, kanan, geser = 0) {
  const x1 = ujungLabel + 14;
  const x2 = kanan.x - kanan.R - 9;
  const talang = KIRI + (kiri.kolom + 1) * KOLOM + 24 - 30 + geser;
  const xt = Math.min(Math.max(talang, x1 + R_SUDUT + 4), x2 - R_SUDUT - 4);
  const y1 = kiri.y;
  const y2 = kanan.y;
  const f = (n) => n.toFixed(1);
  const dy = y2 - y1;
  if (Math.abs(dy) < 1) return `M${f(x1)},${f(y1)} H${f(x2)}`;
  const r = Math.min(R_SUDUT, Math.abs(dy) / 2);
  const arah = Math.sign(dy);
  return `M${f(x1)},${f(y1)} H${f(xt - r)} Q${f(xt)},${f(y1)} ${f(xt)},${f(y1 + arah * r)} `
    + `V${f(y2 - arah * r)} Q${f(xt)},${f(y2)} ${f(xt + r)},${f(y2)} H${f(x2)}`;
}

/** Nama rumpun yang panjang dipecah dua baris di batas kata terdekat dari
 *  tengahnya, supaya tidak menabrak kolom pemula. */
function labelRumpun(teks, x, yTengah, sifat) {
  if (teks.length <= 18) {
    return s("text", { ...sifat, x, y: yTengah, dy: "0.35em" }, document.createTextNode(teks));
  }
  const spasi = [...teks.matchAll(/ /g)].map((m) => m.index);
  const potong = spasi.reduce((a, b) => (Math.abs(b - teks.length / 2) < Math.abs(a - teks.length / 2) ? b : a));
  return s("text", { ...sifat, x, y: yTengah },
    s("tspan", { x, dy: "-0.25em" }, document.createTextNode(teks.slice(0, potong))),
    s("tspan", { x, dy: "1.2em" }, document.createTextNode(teks.slice(potong + 1))));
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
  const { pos, baris: barisRumpun, tinggi: H } = tataLetak(data);
  const tetangga = new Map(data.profesi.map((p) => [p.id, new Set()]));
  for (const e of data.sisi) {
    tetangga.get(e.a).add(e.b);
    tetangga.get(e.b).add(e.a);
  }

  const jenisSisi = new Map();
  for (const e of data.sisi) {
    jenisSisi.set(e.a + "|" + e.b, e.jenis);
    jenisSisi.set(e.b + "|" + e.a, e.jenis);
  }
  // Diisi ulang tiap kali sorotan berpindah; lihat gambarGaris().
  const lapisGaris = s("g", { class: "kr-lapis-garis" });

  const simpul = data.profesi.map((p) => {
    const t = pos.get(p.id);
    const R = t.R;
    const keliling = 2 * Math.PI * (R + 4);
    const g = s("g", {
      class: "kr-simpul", tabindex: 0, role: "button",
      "data-id": p.id, "data-rumpun": p.rumpun,
      "aria-label": `${p.nama}, kesiapan ${bulat(p.kesiapan)} persen`,
      transform: `translate(${t.x.toFixed(1)},${t.y.toFixed(1)})`,
    },
      s("rect", { x: -R - 8, y: -LANGKAH / 2 + 2, width: KOLOM - 20, height: LANGKAH - 4,
                  rx: 8, class: "kr-sasaran" }),
      s("circle", { r: R + 9, class: "kr-halo" }),
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
  const pita = barisRumpun.map((r, i) => s("rect", {
    x: 0, y: r.y, width: W, height: r.tinggi,
    class: "kr-pita" + (i % 2 ? " kr-pita-genap" : ""), "data-rumpun": r.id,
  }));
  const label = barisRumpun.map((r) => labelRumpun(r.label, 22, r.y + r.tinggi / 2,
    { class: "kr-rumpun", "data-rumpun": r.id }));
  const kepalaKolom = Object.keys(JENJANG_KOLOM).map((j, i) => s("text", {
    class: "kr-kolom", x: KIRI + i * KOLOM + 16, y: 30,
  }, document.createTextNode(data.jenjang[j].startsWith("Bisa") ? "Pemula"
    : j === "menengah" ? "Menengah" : "Senior")));

  const svg = s("svg", {
    viewBox: `0 0 ${W} ${H}`, class: "kr-graf", role: "group",
    "aria-label": "Konstelasi profesi. Pilih satu untuk melihat rinciannya.",
  }, s("g", {}, pita), s("g", {}, kepalaKolom), s("g", {}, label),
     lapisGaris, s("g", {}, simpul));

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
      // Tetangga SEJENJANG tidak digaris (lihat gambarGaris); lingkar putus-
      // putus di LUAR cincin kesiapannya yang membawa hubungan itu.
      g.classList.toggle("sejajar", dekat.has(ini) && pos.get(ini).kolom === pos.get(fokus).kolom);
      g.setAttribute("aria-pressed", String(ini === terpilih.id));
    }
    gambarGaris(fokus, dekat);
    for (const t of [...label, ...pita]) {
      const jauh = tersaring(t.dataset.rumpun);
      t.classList.toggle("redup", jauh);
    }
  }

  // Ujung label diukur dari teksnya sendiri (getComputedTextLength), sekali
  // per simpul. Gambar PERTAMA terjadi sebelum layar menempel (pilih() di
  // bawah), jadi di sana yang ada cuma perkiraan per huruf -- perkiraan itu
  // tidak disimpan, `perkiraan` menandai gambarnya, dan saatSiap di akhir
  // layar menggambar ulang dengan ukuran sungguhan. Tanpa itu garis pertama
  // yang dilihat orang bisa menempel ke huruf terakhir label.
  const ujungLabel = new Map();
  let perkiraan = false;
  const simpulPer = new Map(simpul.map((g) => [g.dataset.id, g]));
  function ujung(pid) {
    if (ujungLabel.has(pid)) return ujungLabel.get(pid);
    const t = pos.get(pid);
    const teks = simpulPer.get(pid).querySelector(".kr-label");
    const panjang = teks.isConnected ? teks.getComputedTextLength() : 0;
    const x = t.x + t.R + 10 + (panjang || pendek(perId.get(pid).nama).length * 7.6);
    if (panjang) ujungLabel.set(pid, x);
    else perkiraan = true;
    return x;
  }

  let fokusGaris = null;
  function gambarGaris(fokus, dekat) {
    if (fokus === fokusGaris && !perkiraan && lapisGaris.childElementCount) return;
    fokusGaris = fokus;
    perkiraan = false;
    const baru = [];
    for (const lain of dekat) {
      const a = pos.get(fokus);
      const b = pos.get(lain);
      if (a.kolom === b.kolom) continue;  // satu jenjang: cincin, bukan garis
      const [kiri, kanan] = a.kolom < b.kolom ? [fokus, lain] : [lain, fokus];
      const jenis = jenisSisi.get(fokus + "|" + lain);
      if (tersaring(perId.get(lain).rumpun)) continue;
      const garis = s("path", {
        d: jalurGaris(pos.get(kiri), ujung(kiri), pos.get(kanan), jenis === "naik" ? 0 : -8),
        class: "kr-sisi kr-sisi-" + jenis, pathLength: jenis === "naik" ? 1 : null,
      });
      const t = pos.get(kanan);
      baru.push(garis, s("circle", {
        class: "kr-ujung kr-ujung-" + jenis, r: 2.6,
        cx: (t.x - t.R - 9).toFixed(1), cy: t.y.toFixed(1),
      }));
      // Garis "naik" ditarik dari kiri ke kanan. Keadaan akhirnya keadaan
      // alami (dashoffset 0), jadi gerak yang dimatikan tidak menyembunyikan
      // apa pun.
      if (jenis === "naik" && gerakPenuh()) {
        garis.setAttribute("stroke-dasharray", "1");
        garis.animate({ strokeDashoffset: [1, 0] },
          { duration: 420, easing: "cubic-bezier(.2,.7,.2,1)" });
      }
    }
    isikan(lapisGaris, ...baru);
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
  if (data.tujuan && perId.get(data.tujuan)) pilihKe.value = data.tujuan;
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
    h("header.kepala-besar.kr-kepala.kepala-bersampul", {},
      h("div.kepala-teks", {},
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
      // Orbit: profesi yang berputar di sekitar satu pusat -- kurikulummu.
      h("div.kepala-sampul", {}, sampul("karier", { ragam: "orbit", lebar: 560, tinggi: 400 }))),

    saring,
    h("div.kr-utama", {},
      h("figure.kr-kanvas", {},
        svg,
        h("figcaption.kr-legenda", {},
          h("span", {}, h("i.kr-leg-naik"), "Jalur naik"),
          h("span", {}, h("i.kr-leg-dekat"), "Keahlian beririsan"),
          h("span", {}, h("i.kr-leg-sejajar"), "Sejenjang & beririsan"),
          h("span", {}, h("i.kr-leg-siap"), "Kesiapanmu"),
          h("span", {}, "Garis muncul untuk profesi yang dipilih. Makin ke kanan, makin senior."))),
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
  saatSiap(el, () => { if (perkiraan) gambarGaris(terpilih.id, tetangga.get(terpilih.id)); });
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

  // Rona sampulnya rona kurikulum bekal PERTAMA profesi itu, jadi profesi
  // yang bertumpu pada bahasa yang sama terlihat sekerabat.
  return h("div.kr-panel-isi", {},
    h("div.kr-sampul", {}, sampul("karier/" + p.id,
      { bahasa: p.kelompok[0] ? p.kelompok[0].wakil : null, lebar: 720, tinggi: 200 })),
    h("div.kr-panel-kepala", {},
      h("div", {},
        h("span.mata", {}, rumpun.label),
        h("h2", {}, p.nama),
        h("span.pil", {}, data.jenjang[p.jenjang]),
        tombolTujuan(p, data)),
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

/** "Jadikan tujuanku": menyimpan profesi tujuan ke konfigurasi (tujuan_karier).
 *  Dasbor dan perencana perpindahan membacanya; tanpa ini keduanya menebak
 *  dari kesiapan tertinggi. Setelan yang sama ada di Pengaturan. */
function tombolTujuan(p, data) {
  const label = () => (data.tujuan === p.id ? "Tujuanmu" : "Jadikan tujuanku");
  const tbl = h("button.tbl.tbl-kecil.kr-tujuan", { type: "button", "aria-pressed": String(data.tujuan === p.id) },
    ikon("bintang", { ukuran: 15 }), h("span", {}, label()));
  tbl.addEventListener("click", async () => {
    const baru = data.tujuan === p.id ? "" : p.id;
    try {
      await api.kirim("/api/konfigurasi", { tujuan_karier: baru });
      data.tujuan = baru;
      tbl.setAttribute("aria-pressed", String(data.tujuan === p.id));
      isikan(tbl, ikon("bintang", { ukuran: 15 }), h("span", {}, label()));
    } catch (e) { /* tombolnya tetap; setelan ada juga di Pengaturan */ }
  });
  return tbl;
}
