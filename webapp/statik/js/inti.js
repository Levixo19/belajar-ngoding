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
  adaGerak, gerakPenuh, PEGAS,
} from "./gerak.js";
import { ikon } from "./ikon.js";
/* Saluran non-visual. Berkas ini SATU-SATUNYA yang memuatnya — sama seperti
   bahasa gerak, pintunya cuma satu supaya tidak pernah ada layar yang
   mengarang bunyinya sendiri. Yang diteruskan ke layar Pengaturan cuma
   pembaca dan penulis preferensinya, lewat re-ekspor di kaki berkas ini. */
import {
  isyarat, sentuhPerangkat, bacaSuara, bacaGetar, setelSuara,
  tandaiPreferensi, adaHaptik, SUARA,
} from "./suara.js";

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
  isikan(kotak,
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
    if (v === null || v === undefined || (v === false && !(k in el))) continue;  // properti DOM (spellcheck) butuh false-nya
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

/* Ganti seluruh isi sebuah elemen — versi `tambah()` dari `replaceChildren`.
 *
 * Bedanya cuma satu, dan itu bukan kenyamanan melainkan pencegah bug yang
 * SUDAH pernah terjadi: `replaceChildren` bawaan DOM mengubah `null` jadi
 * simpul teks berbunyi "null". Pola yang dipakai di seluruh berkas ini —
 * `syarat ? h(...) : null` — karena itu aman di dalam `h()` (yang menyaringnya
 * lewat `tambah`) tapi bocor ke layar begitu dipasang langsung sebagai
 * argumen `replaceChildren`. Yang terlihat pelajar adalah kata "null"
 * mengambang di halaman kuis dan bookmark, tanpa satu pun error di konsol.
 *
 * Aturannya: di luar berkas ini, jangan pernah panggil `replaceChildren`
 * sendiri. Dijaga tests/test_web.TestBerkasStatik. */
export function isikan(el, ...anak) {
  return tambah(kosongkan(el), anak);
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

/** Urai ISO dari server menjadi Date LOKAL. Satu-satunya pintu; jangan
 *  memanggil `new Date(iso)` langsung di mana pun lagi.
 *
 *  Spesifikasi ECMAScript mengurai dua bentuk dengan aturan yang BERBEDA, dan
 *  perbedaan itu tidak pernah memberi pesan galat:
 *
 *    "2026-09-28"            (date-only, 10 karakter) -> tengah malam **UTC**
 *    "2026-09-28T07:15:00"   (tanpa offset)           -> tengah malam **LOKAL**
 *
 *  Server ini menulis keduanya: `date.today().isoformat()` untuk tanggal
 *  (riwayat harian, jadwal kuis, tanggal streak) dan
 *  `datetime.now().isoformat(timespec="seconds")` untuk cap waktu (catatan,
 *  kuis terakhir). Keduanya bermaksud waktu SETEMPAT — tidak satu pun membawa
 *  offset. Jadi yang perlu ditolong cuma bentuk pertama, dan pertolongannya
 *  adalah memindahkannya ke cabang parser yang satunya.
 *
 *  Terukur sebelum diperbaiki: `tanggalRamah("2026-09-28")` mengembalikan
 *  27/9/2026 di TZ=Pacific/Niue. Cap waktu tidak boleh ikut disentuh — ia
 *  sudah benar, dan menambahi apa pun padanya akan menggesernya. */
export function tanggalLokal(iso) {
  if (!iso) return null;
  const s = String(iso);
  const t = new Date(s.length === 10 ? s + "T00:00:00" : s);
  return isNaN(t) ? null : t;
}

/** Tanggal hari ini menurut jam DINDING orang yang memakainya.
 *
 *  `new Date().toISOString().slice(0, 10)` memberi tanggal UTC, jadi di
 *  Asia/Makassar (UTC+8) ia masih menyebut kemarin sampai pukul 08:00 pagi.
 *  Dipakai untuk menandai sel "hari ini" dan menamai berkas ekspor. */
export function hariIniISO() {
  const t = new Date();
  const dua = (n) => String(n).padStart(2, "0");
  return `${t.getFullYear()}-${dua(t.getMonth() + 1)}-${dua(t.getDate())}`;
}

export function tanggalRamah(iso) {
  const t = tanggalLokal(iso);
  if (!t) return iso ? String(iso) : "";
  return t.toLocaleDateString("id-ID",
    { day: "numeric", month: "short", year: "numeric" });
}

export function jamRamah(iso) {
  const t = tanggalLokal(iso);
  if (!t) return iso ? String(iso) : "";
  return t.toLocaleString("id-ID",
    { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
}

/** Selisih HARI dari hari ini. Masa depan positif, masa lalu NEGATIF.
 *
 *  Tandanya adalah bagian dari kontraknya: `jadwalRamah()` membaca `<= 0`
 *  sebagai "sudah waktunya", dan `celahBelajar()` membalikkannya jadi "N hari
 *  lalu". Membalik arahnya suatu hari nanti akan menukar kedua kalimat itu
 *  tanpa satu pun tes lain menyadarinya -- karena itu ia dikunci tes sendiri. */
export function selisihHari(iso) {
  const t = tanggalLokal(iso);
  if (!t) return null;
  // Cap waktu dibulatkan ke tengah malam juga: yang dihitung HARI, bukan jam.
  t.setHours(0, 0, 0, 0);
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

/** Penanda "momen ini sudah pernah dirayakan di peramban ini".
 *
 *  Sengaja di localStorage, BUKAN di berkas progres dan bukan di server.
 *  Berkas progres adalah catatan belajar orang sungguhan; sebuah upacara sekali
 *  seumur hidup bukan capaian belajar, ia cuma keadaan tampilan. Konsekuensinya
 *  jujur dan disengaja: membersihkan data situs membuat perayaannya TERLEWAT,
 *  bukan dobel dan bukan galat -- dan tidak ada satu pun XP yang hilang.
 *
 *  `sudahPernah()` menulis sekaligus membaca dengan sengaja: pemanggilnya
 *  adalah jalur yang mau merayakan, dan dua baris "cek lalu tandai" yang
 *  terpisah adalah dua tempat untuk lupa. */
export function sudahPernah(kunci) {
  const penuh = "upacara." + kunci;
  if (ambilLokal(penuh, false) === true) return true;
  simpanLokal(penuh, true);
  return false;
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

/** Tingkat perayaan, DISIMPULKAN dari isi `hadiah` — bukan dari parameter.
 *
 *  Ketiganya sudah lama ada di sini sebagai perilaku, cuma belum punya nama:
 *
 *    acara  : naik level, atau badge baru. Yang paling jarang terjadi, dan
 *             satu-satunya yang memakai partikel (percikBara di dalam
 *             tampilNaikLevel, dan itu sendiri sudah dipagari gerakPenuh).
 *    capai  : XP bertambah dan pemanggilnya tidak meminta diam. Satu toast --
 *             dan, HANYA kalau pemanggil menyerahkan `dari`, satu denyut plus
 *             tujuh bara pada benda itu.
 *    sentuh : sisanya — progres tercatat, tapi tidak ada yang dirayakan.
 *             Ini yang dipakai pemanggil ber-`diam: true`.
 *
 *  Namanya disimpulkan, bukan diminta, karena keempat pemanggil `rayakan()`
 *  hari ini ada di layar-*.js dan tidak boleh disentuh dari sini. Menambah
 *  parameter berarti menambah sesuatu yang tidak ada yang mengisinya. */
export function tingkatRayakan(hadiah, { diam = false } = {}) {
  if (!hadiah) return "sentuh";
  if (hadiah.naik_level || (hadiah.badge || []).length) return "acara";
  if (hadiah.xp_tambah > 0 && !diam) return "capai";
  return "sentuh";
}

/** Tampilkan hadiah dari sebuah tindakan: XP, badge baru, kenaikan level.
 *
 *  Dipanggil dari mana pun progres bertambah. Aturannya: satu peristiwa, satu
 *  perayaan. Menumpuk tiga pemberitahuan untuk satu latihan yang lulus membuat
 *  yang penting (badge baru) tenggelam di antara yang biasa (+25 XP).
 */
export function rayakan(hadiah, { diam = false, dari = null } = {}) {
  if (!hadiah) return; if (hadiah.simpan_gagal) sorak("Progres gagal disimpan ke disk. Cek ruang disk, lalu coba lagi.", "salah", 8);

  const tingkat = tingkatRayakan(hadiah, { diam });

  /* Alur di bawah SENGAJA dibiarkan seperti semula, bukan dipetakan ulang ke
     `tingkat`. Sebabnya satu: hari ini toast badge berdiri DI LUAR if/else,
     jadi sebuah hadiah yang membawa badge sekaligus XP memunculkan keduanya.
     Menjadikan "acara" mematikan cabang XP akan menelan satu toast yang hari
     ini muncul — perubahan perilaku yang tidak diminta siapa pun.

     `tingkat` karena itu dipakai sebagai KETERANGAN, bukan sebagai saklar:
     ia ikut di event supaya layar yang mau menanggapi bisa membacanya tanpa
     menyimpulkan ulang dari isi hadiah. */
  if (hadiah.naik_level) {
    tampilNaikLevel(hadiah);
  } else if (hadiah.xp_tambah > 0 && !diam) {
    sorak(`+${hadiah.xp_tambah} XP`, "nyala", 2.2);
  }

  /* Tingkat `capai` boleh menempel pada BENDA yang baru saja berhasil, bukan
     cuma melayang sebagai toast di pojok — tapi hanya kalau pemanggilnya
     menyerahkan bendanya. Itu syarat, bukan hiasan: keempat pemanggil hari ini
     tidak mengoper `dari`, jadi perilaku mereka nol berubah, dan tidak ada
     tebakan "elemen mana yang dimaksud" yang dibuat dari sini.

     Bukan `kilau()`: kilau adalah seluruh layar menguat, dan itu porsi `acara`.
     Yang di sini seukuran capaian — satu denyut pada bendanya, dan tujuh bara,
     bukan enam belas. `percikBara` memagari dirinya sendiri di `gerakPenuh`
     (gerak.js:801) dan `denyut` ikut `skala()`, jadi tingkat gerak diputuskan
     di satu tempat seperti biasanya. Keduanya berhenti sendiri. */
  if (tingkat === "capai" && dari) {
    denyut(dari);
    percikBara(dari, { jumlah: 7 });
  }

  /* Saluran NON-VISUAL, dan ia menempel DI SINI alih-alih di tiap layar
     karena `tingkatRayakan()` di atas sudah memutuskan tingkatnya. Kalau
     pengait ini dipasang di layar-layar, tiap layar akan menyimpulkan ulang
     "ini peristiwa sebesar apa" dari isi hadiah — dan suatu hari dua di
     antaranya menyimpulkan beda.
     Haptik ikut HANYA pada `acara`. Yang dikonfirmasi getar adalah peristiwa
     yang jarang; satu sentakan tiap kali XP bertambah berarti telepon yang
     berdenyut dua puluh kali per sesi belajar, dan itu berhenti berarti
     apa-apa pada denyut ketiga. Keduanya memagari dirinya sendiri lewat
     `bacaSuara()`/`bacaGetar()` — bawaannya mati, jadi pemanggilan tanpa
     syarat di sini tetap berujung diam sampai orangnya memilih sebaliknya. */
  if (tingkat === "acara") {
    isyarat("acara");
    sentuhPerangkat();
  } else if (tingkat === "capai") {
    isyarat("capai");
  }

  for (const b of hadiah.badge || []) {
    sorak(`Badge baru, ${b.nama}: ${b.deskripsi}`, "nyala", 6);
  }

  document.dispatchEvent(new CustomEvent("progres-berubah",
    { detail: { ...hadiah, tingkat } }));
}

/** Cahaya lampu kerja menguat sesaat dari bawah layar, lalu kembali tenang.
 *  Kalau diberi sebuah elemen, bara ikut memercik dari sana — jadi perayaannya
 *  menempel pada BENDA yang baru saja berhasil, bukan melayang di ruang
 *  kosong. */
export function kilau(dari) {
  if (!gerakPenuh()) return;  // bergerak sendiri: tingkat "halus" menjanjikan diam
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
    h("div", { gaya: { fontSize: "1.1rem", marginTop: "6px" } }, hadiah.gelar_baru ? "Gelar baru: " + hadiah.gelar : hadiah.gelar));
  const el = h("div.naik-level", {}, kotak); sorak(`Naik ke level ${hadiah.level}` + (hadiah.gelar_baru ? `, gelar baru: ${hadiah.gelar}` : ""), "nyala", 4);
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
export function bilah(persen, kelas = "", { diam = false } = {}) {
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

  // `diam` untuk bilah yang tinggal di perkakas tetap — strip konteks. Di
  // sana ia digambar ulang SETIAP kali halaman berganti, dan bilah yang
  // mengisi dari nol pada tiap perpindahan bukan lagi umpan balik melainkan
  // kedipan di sudut mata orang yang sedang membaca. Nilainya tetap benar;
  // yang dilepas cuma gerakan masuknya.
  if (!diam) {
    saatTampak(el, () => {
      animasi(isi, { width: ["0%", p + "%"] }, { pegas: "panjang" });
    }, { bagian: 0.2 });
  }
  return el;
}

/** Satu komponen untuk EMPAT keadaan: kosong, berhasil, gagal, terkunci.
 *
 *  Sebelumnya keempatnya punya bentuknya sendiri-sendiri — `.kosong`
 *  bergaris putus-putus, `.tuntas` berbingkai hijau, kegagalan muat berupa
 *  kepala halaman biasa, dan layar penolakan 403 berupa kartu bab. Empat
 *  bentuk untuk satu pekerjaan yang sama ("tidak ada apa-apa di sini, dan
 *  inilah sebabnya") berarti pelajar harus belajar membacanya empat kali —
 *  dan tiga dari empat itu cuma muncul sekali-sekali, persis frekuensi yang
 *  membuat sebuah bentuk tidak pernah sempat dikenali.
 *
 *  @param jenis  "" | "tuntas" | "salah" | "kunci" | "kosong"
 *  @param gambar nama ikon dari ikon.js; boleh kosong.
 *  @param aksi   daftar elemen tombol; boleh kosong.
 */
export function keadaan({ jenis = "", gambar = "", judul, ket = "", aksi = [] }) {
  // `.masuk-mandiri` adalah util entrance dari S01, bukan mesin baru. Ia
  // dipasang di sini supaya keempat keadaan (kosong/berhasil/gagal/terkunci)
  // datang dengan satu bahasa yang sama, tanpa satu pun layar menulis
  // koreografinya sendiri. Bentuk geraknya diatur gaya.css: yang lahir dari
  // proses async memudar TANPA bergeser, yang permanen boleh bergeser.
  return h("div.keadaan.masuk-mandiri" + (jenis ? ".keadaan-" + jenis : ""), {},
    gambar ? ikon(gambar, { ukuran: 22 }) : null,
    h("div.keadaan-isi", {},
      h("b", {}, judul),
      ket ? h("p", {}, ket) : null,
      aksi.length ? h("div.deret", {}, aksi) : null));
}

/** Keadaan kosong — bentuk khusus `keadaan()` yang ditengahkan, untuk ruang
 *  yang seharusnya berisi sebuah daftar. */
export function kosong(judul, ket, aksi) {
  return keadaan({
    jenis: "kosong",
    judul,
    ket,
    aksi: aksi ? (Array.isArray(aksi) ? aksi : [aksi]) : [],
  });
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

/* Satu-satunya pintu saluran non-visual yang dibuka ke layar.
 *
 * Yang diteruskan sengaja cuma pembaca dan penulis preferensinya plus satu
 * peragaan — BUKAN `isyarat()` sendiri. Layar yang bisa memanggil `isyarat()`
 * langsung adalah layar yang bisa mengarang bunyi barunya sendiri, dan pada
 * saat itu "tiga tingkat" berhenti menggambarkan apa pun yang sebenarnya
 * terdengar. */
export { bacaSuara, bacaGetar, setelSuara, tandaiPreferensi, adaHaptik, SUARA };

/** Peragakan satu saluran non-visual, untuk kartu pilihan di Pengaturan.
 *
 *  Kartunya harus BERBUNYI (atau menyentak) saat ditekan, sama seperti tiga
 *  kartu tingkat gerak di sebelahnya memperagakan geraknya. Kalau tidak,
 *  satu-satunya cara tahu apa arti "halus" adalah memilihnya, keluar dari
 *  Pengaturan, belajar sampai naik level, dan mencoba mengingat rasanya — dan
 *  tidak ada orang yang akan melakukan itu tiga kali untuk membandingkan.
 *
 *  SATU fungsi untuk dua saluran, dan parameternya saluran — bukan dua fungsi.
 *  Dua pintu peragaan adalah dua tempat yang bisa berbeda pendapat tentang
 *  syarat mana yang berlaku, dan satu-satunya hal yang membuat "bawaan mati"
 *  bisa dipercaya adalah bahwa setiap jalur menuju bunyi melewati pemeriksaan
 *  yang sama.
 *
 *  Tingkat suaranya DIBACA dari preferensi yang baru dipasang, bukan diterima
 *  sebagai argumen: kartu yang memperagakan tingkat yang belum berlaku
 *  memperagakan sesuatu yang bohong. "mati" karena itu memang hening — itu
 *  jawaban yang benar, dan layar yang memanggil ini bertanggung jawab
 *  mengatakannya dengan kata-kata. */
export function mainkanContoh(saluran = "suara") {
  if (saluran === "getar") return sentuhPerangkat();
  const tingkat = bacaSuara();
  return isyarat(tingkat === "halus" ? "acara" : "contoh");
}

function cadanganSalin(teks, selesai) {
  const ta = h("textarea", { value: teks, "aria-hidden": "true", tabIndex: -1,
    gaya: { position: "fixed", top: "-1000px", opacity: "0" } });
  document.body.appendChild(ta);
  ta.select();
  try { document.execCommand("copy"); selesai(); }
  catch (e) { sorak("Browser ini tidak mengizinkan penyalinan otomatis.", "salah"); }
  ta.remove();
}
