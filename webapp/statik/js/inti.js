/* Perkakas dasar: klien API, pembuat elemen, pemberitahuan, dan dialog.
 *
 * Tidak ada kerangka kerja apa pun di sini, dan itu disengaja. Seluruh
 * aplikasi terminalnya berdiri tanpa satu pun dependensi luar (lihat
 * AGENTS.md); versi webnya mengikuti janji yang sama. Yang dibutuhkan cuma
 * `python3 belajar-web.py` dan sebuah browser — tidak ada npm, tidak ada
 * langkah build, tidak ada berkas yang basi enam bulan lagi.
 *
 * Yang menggantikan kerangka kerja itu satu fungsi: `h()`. Ia membuat elemen
 * DOM dari pemerian ringkas. Selain lebih pendek daripada innerHTML, ia juga
 * lebih aman: teks selalu masuk sebagai text node, jadi judul materi yang
 * kebetulan memuat "<" tidak pernah bisa berubah jadi markup.
 *
 * Importir: seluruh berkas js/ lainnya.
 */

import {
  animasi, masuk, keluar, tata, saatTampak, percikBara, denyut, jepit,
  adaGerak, PEGAS,
} from "./gerak.js";

/* -------------------------------------------------------------------- API */

const TOKEN = window.TOKEN_BELAJAR || "";

export class GalatApi extends Error {
  constructor(pesan, kode) {
    super(pesan);
    this.kode = kode;
  }
}

async function panggil(url, opsi) {
  let jawab;
  try {
    jawab = await fetch(url, opsi);
  } catch (e) {
    // Penyebab tersering: server dimatikan dengan Ctrl+C sementara tab masih
    // terbuka. Katakan itu, jangan "Failed to fetch".
    throw new GalatApi(
      "Tidak bisa menghubungi server. Apakah jendela terminal tempat "
      + "`python3 belajar-web.py` berjalan masih terbuka?", 0);
  }
  let isi = null;
  try {
    isi = await jawab.json();
  } catch (e) { /* balasan tanpa badan JSON */ }

  if (!jawab.ok) {
    // Token hanya jadi tidak sah karena satu sebab: servernya dinyalakan ulang
    // sementara tab ini masih terbuka. Menyuruh "muat ulang halaman" lewat
    // pesan error saja tidak cukup — pesannya muncul di tengah hasil, jauh
    // dari tempat mata sedang melihat. Jadi tawarkan tombolnya sekalian.
    if (jawab.status === 403 && /token/i.test((isi && isi.galat) || "")) {
      tawarkanMuatUlang();
    }
    throw new GalatApi((isi && isi.galat) || `Kesalahan ${jawab.status}.`,
                       jawab.status);
  }
  return isi;
}

let tawaranTampil = false;

function tawarkanMuatUlang() {
  if (tawaranTampil) return;
  tawaranTampil = true;
  const kotak = sorak("", "nyala", 600);
  kotak.replaceChildren(
    h("span", {}, "Server dinyalakan ulang. Muat ulang halaman untuk lanjut."),
    h("button.tbl.tbl-kecil.tbl-utama",
      { onclick: () => location.reload() }, "Muat ulang"));
}

export const api = {
  ambil(jalur, params) {
    const q = new URLSearchParams(params || {}).toString();
    return panggil(jalur + (q ? "?" + q : ""),
                   { headers: { "X-Belajar-Token": TOKEN } });
  },
  kirim(jalur, muatan) {
    return panggil(jalur, {
      method: "POST",
      headers: {
        "X-Belajar-Token": TOKEN,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(muatan || {}),
    });
  },
};

/* ------------------------------------------------------------- elemen DOM */

/** h("div.kartu#id", {onclick, title, ...}, anak, anak, ...) -> Element
 *
 *  Anak boleh berupa string (jadi text node), Element, array, atau null yang
 *  dilewati — supaya `kondisi && h(...)` bisa ditulis apa adanya.
 */
export function h(pemerian, sifat, ...anak) {
  const [tagKelas, id] = String(pemerian).split("#");
  const bagian = tagKelas.split(".");
  const tag = bagian[0] || "div";
  const el = document.createElement(tag);
  if (bagian.length > 1) el.className = bagian.slice(1).join(" ");
  if (id) el.id = id;

  for (const [k, v] of Object.entries(sifat || {})) {
    if (v === null || v === undefined || v === false) continue;
    if (k === "kelas") el.className = [el.className, v].filter(Boolean).join(" ");
    else if (k === "gaya") Object.assign(el.style, v);
    else if (k === "data") for (const [dk, dv] of Object.entries(v)) el.dataset[dk] = dv;
    else if (k.startsWith("on") && typeof v === "function") {
      el.addEventListener(k.slice(2), v);
    } else if (k in el && typeof v !== "object") {
      el[k] = v;
    } else {
      el.setAttribute(k, v === true ? "" : v);
    }
  }
  // Setiap medan isian dapat id, walau tidak ada yang merujuknya. Semuanya
  // sudah punya label atau aria-label — jadi ini bukan soal aksesibilitas,
  // melainkan soal browser: tanpa id maupun name, Chrome menolak mengingat
  // isian dan mencatat keluhan di konsol. Konsol yang penuh peringatan yang
  // sudah "diketahui aman" adalah konsol yang berhenti dibaca, dan peringatan
  // berikutnya yang benar-benar penting ikut tenggelam di situ.
  if (!el.id && (tag === "input" || tag === "textarea" || tag === "select")) {
    el.id = idBaru(tag);
  }

  tambah(el, anak);
  return el;
}

export function tambah(induk, anak) {
  for (const a of anak.flat(4)) {
    if (a === null || a === undefined || a === false || a === "") continue;
    induk.appendChild(a instanceof Node ? a : document.createTextNode(String(a)));
  }
  return induk;
}

export function kosongkan(el) {
  while (el.firstChild) el.removeChild(el.firstChild);
  return el;
}

/* Penomoran id untuk menghubungkan <label> dengan medan isiannya.
 *
 * Kelihatan sepele, tapi tanpa hubungan itu label-nya cuma teks di sebelah
 * kotak: pembaca layar mengumumkan "edit teks, kosong" tanpa menyebut apa yang
 * harus diisi, dan mengeklik labelnya tidak memindahkan fokus ke medannya —
 * sasaran klik yang hilang begitu saja. Chrome melaporkan keduanya sebagai
 * masalah di konsol, dan memang benar. */
let nomorId = 0;

export function idBaru(awalan = "medan") {
  nomorId += 1;
  return `${awalan}-${nomorId}`;
}

/** <label> dan medannya, sudah tersambung. */
export function medan(label, isian, ket) {
  const id = isian.id || idBaru();
  isian.id = id;
  return h("div.medan", {},
    h("label", { for: id }, label),
    ket ? h("div.ket", {}, ket) : null,
    isian);
}

export const $ = (sel, akar = document) => akar.querySelector(sel);
export const $$ = (sel, akar = document) => [...akar.querySelectorAll(sel)];

/** Bagi teks pada kemunculan `kata` dan bungkus yang cocok dengan <mark>.
 *  Memakai pencarian string, bukan regex, supaya karakter khas regex di dalam
 *  kata pencarian tidak perlu di-escape dan tidak bisa meledak. */
export function tandai(teks, kata) {
  const wadah = document.createDocumentFragment();
  if (!kata) {
    wadah.appendChild(document.createTextNode(teks));
    return wadah;
  }
  const rendah = String(teks).toLowerCase();
  const cari = kata.toLowerCase();
  let i = 0;
  for (;;) {
    const pos = rendah.indexOf(cari, i);
    if (pos < 0) break;
    if (pos > i) wadah.appendChild(document.createTextNode(teks.slice(i, pos)));
    wadah.appendChild(h("mark", {}, teks.slice(pos, pos + cari.length)));
    i = pos + cari.length;
  }
  wadah.appendChild(document.createTextNode(teks.slice(i)));
  return wadah;
}

/* ----------------------------------------------------------------- format */

export const bulat = (n) => Math.round(Number(n) || 0);

export function angka(n) {
  return (Number(n) || 0).toLocaleString("id-ID");
}

export function jamMundur(detik) {
  const d = Math.max(0, Math.floor(detik));
  return `${String(Math.floor(d / 60)).padStart(2, "0")}:`
       + `${String(d % 60).padStart(2, "0")}`;
}

export function tanggalRamah(iso) {
  if (!iso) return "";
  const t = new Date(iso);
  if (isNaN(t)) return iso;
  return t.toLocaleDateString("id-ID",
    { day: "numeric", month: "short", year: "numeric" });
}

export function jamRamah(iso) {
  if (!iso) return "";
  const t = new Date(iso);
  if (isNaN(t)) return iso;
  return t.toLocaleString("id-ID",
    { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
}

export function selisihHari(iso) {
  if (!iso) return null;
  const t = new Date(iso + "T00:00:00");
  if (isNaN(t)) return null;
  const kini = new Date();
  kini.setHours(0, 0, 0, 0);
  return Math.round((t - kini) / 86400000);
}

export function tunda(fn, ms = 220) {
  let id = 0;
  return (...a) => {
    clearTimeout(id);
    id = setTimeout(() => fn(...a), ms);
  };
}

/* ----------------------------------------------------- penyimpanan lokal
 * Hanya untuk preferensi yang murni soal TAMPILAN di browser ini (tema,
 * ukuran huruf, saklar gerak). Semua yang berupa capaian belajar disimpan
 * server ke berkas progres, supaya membersihkan data situs tidak akan pernah
 * bisa menghapus hasil belajar. */

export function simpanLokal(kunci, nilai) {
  try { localStorage.setItem("belajar." + kunci, JSON.stringify(nilai)); }
  catch (e) { /* mode penyamaran atau kuota penuh: abaikan */ }
}

export function ambilLokal(kunci, bawaan) {
  try {
    const mentah = localStorage.getItem("belajar." + kunci);
    return mentah === null ? bawaan : JSON.parse(mentah);
  } catch (e) { return bawaan; }
}

/* ------------------------------------------------------------------ sorak */

export function sorak(pesan, jenis = "", detik = 3.4) {
  const wadah = $("#sorak");
  const kotak = h("div.sorak" + (jenis ? ".sorak-" + jenis : ""), {}, pesan);

  // Yang sudah ada digeser dengan FLIP, bukan dibiarkan melompat: kalau dua
  // pemberitahuan datang beruntun, lompatan itulah yang membuat mata
  // kehilangan yang pertama sebelum sempat terbaca.
  tata([...wadah.children], () => wadah.appendChild(kotak), { pegas: "jawab" });
  masuk(kotak, { geser: 18, zum: 0.94, pegas: "lentur" });

  setTimeout(() => {
    const sisa = [...wadah.children].filter((x) => x !== kotak);
    keluar(kotak, { geser: 10 }).selesai.then(() => {
      tata(sisa, () => kotak.remove(), { pegas: "jawab" });
    });
  }, detik * 1000);
  return kotak;
}

/* ---------------------------------------------------------------- jendela */

let tutupJendela = null;
/* Nomor urut dialog. Dipakai supaya pembersihan dialog yang sedang beranjak
   pergi tidak sampai menghapus dialog baru yang dibuka di atas tirai yang
   sama — pola yang cukup sering terjadi: "Batal" pada satu dialog yang
   langsung membuka dialog berikutnya. */
let nomorJendela = 0;

/** Dialog. Return janji yang selesai dengan nilai tombol yang ditekan, atau
 *  null kalau ditutup lewat Esc / klik di luar. */
export function jendela({ judul, isi, aksi = [], lebar = false, saatBuka }) {
  return new Promise((selesai) => {
    const tirai = $("#tirai");
    const sebelumnya = document.activeElement;

    const giliran = ++nomorJendela;

    const tutup = (nilai) => {
      document.removeEventListener("keydown", saatTombol, true);
      tirai.onclick = null;
      tutupJendela = null;
      if (sebelumnya && sebelumnya.focus) sebelumnya.focus();
      // Janjinya diselesaikan SEKARANG, bukan setelah animasinya habis: yang
      // memanggil sering langsung mengirim sesuatu ke server, dan menahannya
      // 140 md demi animasi berarti membayar animasi itu dua kali.
      selesai(nilai);

      const pergi = keluar(kotak, { geser: -10, durasi: 140 }).selesai;
      animasi(tirai, { opacity: [1, 0] },
              { durasi: 140, easing: "ease-in", isi: "forwards" });
      pergi.then(() => {
        // Dialog lain sudah terlanjur dibuka di atas tirai yang sama:
        // membersihkannya sekarang akan menutup dialog yang salah.
        if (giliran !== nomorJendela) return;
        tirai.hidden = true;
        tirai.style.opacity = "";
        kosongkan(tirai);
      });
    };
    tutupJendela = tutup;

    const saatTombol = (e) => {
      if (e.key === "Escape") {
        e.preventDefault(); e.stopPropagation(); tutup(null);
      }
      if (e.key === "Tab") jeratFokus(kotak, e);
    };

    const kotak = h("div.jendela" + (lebar ? ".jendela-lebar" : ""),
      { role: "dialog", "aria-modal": "true", "aria-label": judul || "Dialog" },
      judul && h("div.jendela-kepala", {},
        h("h2", {}, judul),
        h("button.ikon-tombol", {
          onclick: () => tutup(null), title: "Tutup (Esc)",
          "aria-label": "Tutup",
        }, "✕")),
      h("div.jendela-badan", {}, isi),
      aksi.length ? h("div.jendela-kaki", {},
        aksi.map((a) => h("button.tbl" + (a.kelas ? "." + a.kelas : ""),
          { onclick: () => tutup(a.nilai !== undefined ? a.nilai : true) },
          a.label))) : null,
    );

    kosongkan(tirai).appendChild(kotak);
    tirai.hidden = false;
    tirai.style.opacity = "";
    tirai.onclick = (e) => { if (e.target === tirai) tutup(null); };
    document.addEventListener("keydown", saatTombol, true);

    // Animasi memudar milik dialog SEBELUMNYA harus dibatalkan lebih dulu.
    // Ia dipasang dengan fill "forwards", jadi kalau dibiarkan ia akan tetap
    // menahan opacity tirai di 0 sesudah animasi masuk yang baru selesai — dan
    // dialog yang baru dibuka jadi tak terlihat sama sekali. Ini bukan kasus
    // langka: "Batal" yang langsung membuka dialog berikutnya adalah pola yang
    // dipakai di Reset progres dan di Lihat jawaban.
    for (const a of tirai.getAnimations()) a.cancel();
    animasi(tirai, { opacity: [0, 1] }, { durasi: 160 });
    masuk(kotak, { geser: -14, zum: 0.982, pegas: "lentur" });

    if (saatBuka) saatBuka(kotak, tutup);
    else {
      const fokus = kotak.querySelector(
        "input, textarea, button.tbl-utama, button.tbl, [tabindex]");
      if (fokus) fokus.focus();
    }
  });
}

/** Kurung fokus di dalam dialog. Tanpa ini Tab bisa membawa fokus ke halaman
 *  di belakang tirai, yang bagi pemakai papan ketik berarti dialognya seolah
 *  lenyap begitu saja. */
function jeratFokus(kotak, e) {
  const bisa = [...kotak.querySelectorAll(
    'a[href], button:not([disabled]), textarea, input, select,'
    + ' [tabindex]:not([tabindex="-1"])')]
    .filter((el) => el.offsetParent !== null);
  if (!bisa.length) return;
  const awal = bisa[0];
  const akhir = bisa[bisa.length - 1];
  if (e.shiftKey && document.activeElement === awal) {
    e.preventDefault(); akhir.focus();
  } else if (!e.shiftKey && document.activeElement === akhir) {
    e.preventDefault(); awal.focus();
  }
}

export function jendelaTerbuka() { return tutupJendela !== null; }
export function tutupJendelaKini() { if (tutupJendela) tutupJendela(null); }

export function konfirmasi(pesan, { judul = "Yakin?", labelYa = "Ya, lanjutkan",
                                    bahaya = false } = {}) {
  return jendela({
    judul,
    isi: h("p", { gaya: { margin: "0" } }, pesan),
    aksi: [
      { label: "Batal", nilai: false },
      { label: labelYa, nilai: true, kelas: bahaya ? "tbl-bahaya" : "tbl-utama" },
    ],
  }).then((n) => n === true);
}

/* ------------------------------------------------------------- perayaan */

/** Tampilkan hadiah dari sebuah tindakan: XP, badge baru, kenaikan level.
 *
 *  Dipanggil dari mana pun progres bertambah. Aturannya: satu peristiwa, satu
 *  perayaan. Menumpuk tiga pemberitahuan untuk satu latihan yang lulus membuat
 *  yang penting (badge baru) tenggelam di antara yang biasa (+25 XP).
 */
export function rayakan(hadiah, { diam = false } = {}) {
  if (!hadiah) return;

  if (hadiah.naik_level) {
    tampilNaikLevel(hadiah);
  } else if (hadiah.xp_tambah > 0 && !diam) {
    sorak(`+${hadiah.xp_tambah} XP`, "nyala", 2.2);
  }

  for (const b of hadiah.badge || []) {
    sorak(`Badge baru — ${b.nama}: ${b.deskripsi}`, "nyala", 6);
  }

  document.dispatchEvent(new CustomEvent("progres-berubah", { detail: hadiah }));
}

/** Cahaya lampu kerja menguat sesaat dari bawah layar, lalu kembali tenang.
 *  Kalau diberi sebuah elemen, bara ikut memercik dari sana — jadi perayaannya
 *  menempel pada BENDA yang baru saja berhasil, bukan melayang di ruang
 *  kosong. */
export function kilau(dari) {
  if (!adaGerak()) return;
  const el = h("div.kilau");
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1600);
  if (dari) percikBara(dari);
}

function tampilNaikLevel(hadiah) {
  const angkaEl = h("div.angka", {}, String(hadiah.level));
  const kotak = h("div.isi", {},
    h("div.mata", {}, "Naik level"),
    angkaEl,
    h("div", { gaya: { fontSize: "1.1rem", marginTop: "6px" } }, hadiah.gelar));
  const el = h("div.naik-level", {}, kotak);
  document.body.appendChild(el);

  masuk(kotak, { geser: 14, zum: 0.9, pegas: "lentur" });
  // Angkanya sendiri datang sepersekian detik belakangan dan sedikit lebih
  // besar. Itu satu-satunya hal di layar yang benar-benar berubah, jadi ia
  // yang boleh bergerak paling terakhir.
  animasi(angkaEl, {
    opacity: [0, 1],
    transform: ["scale(.72)", "none"],
  }, { pegas: "lentur", delay: 110 });

  kilau();
  percikBara(kotak, { jumlah: 26 });

  setTimeout(() => {
    keluar(el, { geser: 0, durasi: 380 }).selesai.then(() => el.remove());
  }, 2100);
}

/* ------------------------------------------------------------- potongan */

/** Bilah kemajuan yang MENGISI saat pertama terlihat, lalu bergerak berpegas
 *  tiap kali nilainya berubah lewat `.setel()`.
 *
 *  Pengisiannya ditunda sampai bilahnya benar-benar tergulir ke layar. Kalau
 *  tidak, sembilan bilah bahasa di dasbor sudah selesai bergerak sebelum
 *  sempat dilihat, dan yang tersisa cuma sembilan bilah diam — tepat kebalikan
 *  dari yang diinginkan.
 *
 *  Lebarnya SELALU disetel ke nilai akhirnya di gaya inline; animasinya cuma
 *  berangkat dari 0. Jadi kalau gerak dimatikan, atau animasinya dibatalkan di
 *  tengah, yang tertinggal tetap angka yang benar. */
export function bilah(persen, kelas = "") {
  const p = jepit(Number(persen) || 0, 0, 100);
  const isi = h("i", { gaya: { width: p + "%" } });
  const el = h("div.bilah" + (kelas ? "." + kelas : ""),
    { role: "progressbar", "aria-valuenow": String(bulat(p)),
      "aria-valuemin": "0", "aria-valuemax": "100" }, isi);

  el.setel = (baru) => {
    const q = jepit(Number(baru) || 0, 0, 100);
    const dari = isi.style.width || "0%";
    isi.style.width = q + "%";
    el.setAttribute("aria-valuenow", String(bulat(q)));
    animasi(isi, { width: [dari, q + "%"] }, { pegas: "panjang" });
    return el;
  };

  saatTampak(el, () => {
    animasi(isi, { width: ["0%", p + "%"] }, { pegas: "panjang" });
  }, { bagian: 0.2 });
  return el;
}

export function kosong(judul, ket, aksi) {
  return h("div.kosong", {}, h("b", {}, judul), ket && h("div", {}, ket), aksi);
}

export function memuat(baris = 3) {
  return h("div.memuat-blok", {},
    Array.from({ length: baris }, (_, i) =>
      h("div.denyut", { gaya: { width: [38, 74, 60, 82, 50][i % 5] + "%" } })));
}

/** @param sumber  elemen blok kode yang disalin; ia berkilat sekali di
 *                  tepinya, supaya umpan baliknya menempel pada benda yang
 *                  ditekan dan bukan cuma muncul di ujung layar. */
export function salin(teks, pesan = "Kode disalin.", sumber = null) {
  const selesai = () => {
    sorak(pesan, "tumbuh", 1.8);
    const blok = sumber && sumber.closest(".blok-kode, .editor");
    if (blok && adaGerak()) {
      blok.classList.remove("tersalin");
      void blok.offsetWidth;                 // paksa mulai ulang animasinya
      blok.classList.add("tersalin");
      setTimeout(() => blok.classList.remove("tersalin"), 700);
    }
  };
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(teks)
      .then(selesai, () => cadanganSalin(teks, selesai));
  } else {
    // http://127.0.0.1 tidak selalu dihitung sebagai konteks aman oleh semua
    // browser, dan tanpa cadangan ini tombol Salin diam-diam tidak berbuat apa
    // pun — kegagalan paling menjengkelkan karena tak ada tandanya.
    cadanganSalin(teks, selesai);
  }
}

export { denyut, masuk, keluar, percikBara, PEGAS };

function cadanganSalin(teks, selesai) {
  const ta = h("textarea", { value: teks, "aria-hidden": "true", tabIndex: -1,
    gaya: { position: "fixed", top: "-1000px", opacity: "0" } });
  document.body.appendChild(ta);
  ta.select();
  try { document.execCommand("copy"); selesai(); }
  catch (e) { sorak("Browser ini tidak mengizinkan penyalinan otomatis.", "salah"); }
  ta.remove();
}
