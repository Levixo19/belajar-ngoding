/* Statistik, pencapaian, pengaturan, dan pengelolaan data.
 *
 * Di sini juga tinggal `terapkanTampilan()` — satu-satunya tempat preferensi
 * tampilan (tema, ukuran huruf, saklar gerak, lebar baca) diubah jadi atribut
 * dan variabel CSS. Preferensi itu sengaja disimpan di localStorage, BUKAN di
 * berkas konfigurasi milik aplikasi terminal: keduanya menjawab pertanyaan
 * yang berbeda. "Tema apa yang enak di terminalku" dan "tema apa yang enak di
 * browserku" tidak harus punya jawaban sama, dan memaksakan satu nilai untuk
 * keduanya membuat mengubah salah satunya merusak yang lain.
 *
 * Yang benar-benar tentang BELAJAR — nama panggilan, target XP harian, durasi
 * timer kuis — tetap disimpan server ke ~/.belajar_ngoding_config.json, karena
 * itu memang harus sama di terminal maupun di web.
 *
 * Importir: aplikasi.js.
 */

import {
  api, h, bilah, angka, sorak, konfirmasi, jendela, salin,
  simpanLokal, ambilLokal, idBaru, medan,
} from "./inti.js";
import {
  masuk, ungkap, angkaKe, denyut, getar, tingkatGerak, adaGerak,
} from "./gerak.js";

export const TEMA = [
  ["gelap", "Gelap", "Biru-batu. Bawaan, untuk pemakaian sehari-hari."],
  ["malam", "Malam", "Serba hangat, kontras rendah. Untuk mata yang lelah."],
  ["terang", "Terang", "Kertas dingin. Untuk ruangan yang benderang."],
  ["kontras", "Kontras tinggi", "Warna dikuatkan, garis dipertebal."],
];

const UKURAN = [["kecil", 15], ["sedang", 16], ["besar", 18], ["sangat besar", 20]];

/* Tiga tingkat gerak, bukan saklar nyala/mati.
 *
 * Saklar dua posisi memaksa orang yang cuma terganggu oleh latar yang bergeser
 * untuk ikut membuang umpan balik tombol — padahal umpan balik tombol bukan
 * hiasan, melainkan cara tahu bahwa tekanannya sampai. Tingkat tengah memberi
 * jalan keluar: semua yang bergerak SENDIRI padam, semua yang bergerak karena
 * DISENTUH tetap ada, dengan jarak yang dipangkas. */
export const GERAK = [
  ["penuh", "Penuh",
   "Semua gerakan hidup: perpindahan berpegas, urutan masuk, bara di latar."],
  ["halus", "Halus",
   "Tidak ada yang bergerak sendiri. Umpan balik sentuhan tetap ada, "
   + "jaraknya dipendekkan. Pilihan yang tepat untuk sesi panjang."],
  ["mati", "Mati",
   "Tidak ada animasi sama sekali."],
];

/** Nilai lama di localStorage berupa boolean (true/false). Aplikasi ini
 *  dipakai tiap hari, jadi menerjemahkannya bukan kesopanan — tanpa ini,
 *  siapa pun yang pernah mematikan animasi akan mendapati animasinya menyala
 *  lagi sesudah pembaruan. */
function bacaGerak() {
  const n = ambilLokal("gerak", "penuh");
  if (n === true) return "penuh";
  if (n === false) return "mati";
  return GERAK.some((g) => g[0] === n) ? n : "penuh";
}

export function bacaTampilan() {
  return {
    tema: ambilLokal("tema", "gelap"),
    ukuran: ambilLokal("ukuran", "sedang"),
    gerak: bacaGerak(),
    lebarBaca: ambilLokal("lebarBaca", 72),
  };
}

export function terapkanTampilan(ubah) {
  const t = { ...bacaTampilan(), ...(ubah || {}) };
  for (const [k, v] of Object.entries(t)) simpanLokal(k, v);

  const akar = document.documentElement;
  akar.dataset.tema = t.tema;
  akar.dataset.gerak = t.gerak;
  const px = (UKURAN.find((u) => u[0] === t.ukuran) || UKURAN[1])[1];
  akar.style.setProperty("--ukuran-teks", px + "px");
  akar.style.setProperty("--baca", t.lebarBaca + "ch");
  return t;
}

export function temaBerikutnya() {
  const kini = bacaTampilan().tema;
  const i = TEMA.findIndex((t) => t[0] === kini);
  const berikut = TEMA[(i + 1) % TEMA.length];
  terapkanTampilan({ tema: berikut[0] });
  return berikut[1];
}

/* =============================================================== statistik */

export async function layarStatistik() {
  const s = await api.ambil("/api/statistik");
  const punya = s.semua_badge.filter((b) => b.punya);
  const belum = s.semua_badge.filter((b) => !b.punya);

  const el = h("div.masuk-urut", {},
    h("header.kepala-besar", {},
      h("span.mata", {}, "Sejauh ini"),
      h("h1", {}, "Statistik"),
      h("p.kepala-sub", {},
        `Level ${s.level} — ${s.gelar}. ${angka(s.xp)} XP terkumpul dari `
        + `${s.streak_total} hari belajar.`)),

    h("div.petak.petak-4", {},
      angkaBesar(angka(s.xp), "XP total", null, s.xp),
      angkaBesar(String(s.level), s.gelar, null, s.level),
      angkaBesar(String(s.streak), "hari beruntun",
                 `rekor ${s.streak_rekor} hari`, s.streak),
      angkaBesar(`${s.badge_dimiliki}/${s.badge_total}`, "badge terbuka")),

    blokRingkasan(s),

    h("section", {},
      h("span.mata", {}, "Tangga gelar"),
      h("div.kartu.deret", {}, (s.tangga_gelar || []).map((g) =>
        h("span.pil" + (s.level >= g.level ? ".pil-nyala" : ""), {},
          `Lv ${g.level} · ${g.nama}`)))),

    blokBadge(s, punya, belum),

    blokToolchainSemua(s),
    blokXp(s),
    blokData(),
  );
  return { el, judul: "Statistik", jejak: [{ label: "Statistik" }] };
}

/** @param angkaMentah  kalau diisi, angkanya BERJALAN naik dari nol sampai ke
 *                      situ saat kartunya tergulir ke layar. Yang dilewatkan
 *                      sebagai `nilai` tetap dipakai apa adanya untuk bentuk
 *                      yang bukan angka tunggal ("3/22"). */
function angkaBesar(nilai, label, ket, angkaMentah) {
  const isi = h("div", { gaya: { fontFamily: "var(--f-judul)",
    fontSize: "2rem", fontWeight: "700", lineHeight: "1",
    letterSpacing: "-.03em", fontVariantNumeric: "tabular-nums" } }, nilai);
  const el = h("div.kartu.kartu-rapat", { gaya: { textAlign: "center" } },
    isi,
    h("div.mata", { gaya: { margin: "8px 0 0" } }, label),
    ket ? h("div", { gaya: { color: "var(--redup)", fontSize: ".76rem" } }, ket)
        : null);

  if (angkaMentah !== undefined && adaGerak()) {
    saatKartuTampak(el, () => angkaKe(isi, angkaMentah, {
      dari: 0, durasi: 900, format: (n) => angka(Math.round(n)) }));
  }
  return el;
}

/* Pengamat sekali pakai untuk satu elemen. Dipisah supaya tidak ada satu pun
   pengamat yang tertinggal hidup setelah layarnya diganti. */
function saatKartuTampak(el, fn) {
  if (typeof IntersectionObserver === "undefined") { fn(); return; }
  const o = new IntersectionObserver((c) => {
    if (c.some((x) => x.isIntersecting)) { o.disconnect(); fn(); }
  }, { threshold: 0.3 });
  o.observe(el);
}

function blokRingkasan(s) {
  const jml = (f) => s.bahasa.reduce((a, b) => a + b[f], 0);
  return h("section", {},
    h("span.mata", {}, "Rincian per bahasa"),
    h("div.kartu", {},
      h("div", { gaya: { display: "grid", gap: "13px" } },
        s.bahasa.map((b) => h("div", {},
          h("div", { gaya: { display: "flex", justifyContent: "space-between",
                             fontSize: ".88rem", marginBottom: "5px",
                             flexWrap: "wrap", gap: "8px" } },
            h("a", { href: "#/bahasa/" + b.key,
                     gaya: { fontWeight: "600", color: "var(--teks)" } }, b.label),
            h("span", { gaya: { color: "var(--redup)", fontSize: ".78rem",
                                fontFamily: "var(--f-kode)" } },
              `${b.materi}/${b.total_materi} materi · `
              + `${b.kuis}/${b.total_kuis} kuis · `
              + `${b.latihan_lulus + b.latihan_manual}/${b.total_latihan} latihan`
              + (b.skor_maks ? ` · skor ${b.skor}/${b.skor_maks}` : ""))),
          bilah(b.persen, b.persen >= 100 ? "tumbuh" : ""))),
        h("div", { gaya: { borderTop: "1px solid var(--garis)",
                           paddingTop: "13px", color: "var(--teks-2)",
                           fontSize: ".88rem" } },
          `Total: ${jml("materi")} dari ${jml("total_materi")} materi dibaca, `
          + `${jml("latihan_lulus")} latihan lulus dengan kode sendiri, dan `
          + (s.skor_kuis.maks
              ? `${s.skor_kuis.benar} dari ${s.skor_kuis.maks} soal kuis benar.`
              : "belum ada kuis yang dikerjakan.")))));
}

/* Badge yang sudah didapat muncul satu per satu saat petaknya tergulir ke
   layar; yang masih terkunci ikut di belakangnya. Urutan itu penting: yang
   dilihat lebih dulu adalah yang sudah dikerjakan, bukan daftar panjang yang
   belum. */
function blokBadge(s, punya, belum) {
  const petak = h("div.petak.petak-2", {}, punya.map(medali), belum.map(medali));
  ungkap(petak, { per: 26, maks: 320, geser: 8 });
  return h("section", {},
    h("span.mata", {}, `Badge — ${punya.length} dari ${s.semua_badge.length}`),
    petak);
}

function medali(b) {
  return h("div.medali" + (b.punya ? ".punya" : ".terkunci"), {},
    h("div.cap", {}, b.punya ? "★" : "·"),
    h("div", {}, h("b", {}, b.nama), h("span", {}, b.deskripsi)));
}

function blokToolchainSemua(s) {
  return h("section", {},
    h("span.mata", {}, "Ketersediaan toolchain"),
    h("div.kartu", {},
      h("div", { gaya: { display: "grid", gap: "10px" } },
        s.toolchain.map((t) => h("div", { gaya: { display: "flex", gap: "12px",
          alignItems: "baseline", flexWrap: "wrap" } },
          h("span.titik" + (t.siap ? ".selesai" : ".gagal"), {}),
          h("b", { gaya: { minWidth: "110px", fontSize: ".9rem" } }, t.label),
          t.siap
            ? h("span", { gaya: { color: "var(--tumbuh)", fontSize: ".85rem" } },
                "siap dipakai")
            : h("span", { gaya: { color: "var(--redup)", fontSize: ".85rem" } },
                `butuh ${t.hilang.join(", ")}`),
          !t.siap && t.pasang
            ? h("code", { gaya: { color: "var(--tenang)", fontSize: ".8rem" } },
                t.pasang) : null,
          !t.siap && t.pasang ? h("button.tbl.tbl-kecil.tbl-hantu", {
            onclick: () => salin(t.pasang, "Perintah disalin."),
          }, "Salin") : null))),
      h("p", { gaya: { margin: "14px 0 0", color: "var(--redup)",
                       fontSize: ".84rem" } },
        "Toolchain itu opsional. Materi dan kuis berjalan penuh tanpa satu pun "
        + "compiler; yang mati hanya penilaian otomatis untuk bahasa itu.")));
}

function blokXp(s) {
  const t = s.xp_tarif;
  return h("section", {},
    h("span.mata", {}, "Dari mana XP datang"),
    h("div.kartu.deret", {},
      h("span.pil", {}, `Materi tuntas +${t.materi}`),
      h("span.pil", {}, `Latihan dibuka +${t.latihan_dilihat}`),
      h("span.pil.pil-nyala", {}, `Latihan lulus +${t.latihan_lulus}`),
      h("span.pil", {}, `Latihan ditandai manual +${t.latihan_manual}`),
      h("span.pil", {}, `Tiap jawaban kuis benar +${t.per_jawaban_benar}`),
      h("span.pil.pil-tumbuh", {}, `Kuis sempurna +${t.bonus_kuis_sempurna}`)));
}

/* ======================================================= pengelolaan data */

function blokData() {
  return h("section", {},
    h("span.mata", {}, "Data belajarmu"),
    h("div.kartu.deret", {},
      h("button.tbl.tbl-hantu", { onclick: lihatLaporan },
        "Laporan kemajuan (Markdown)"),
      h("button.tbl.tbl-hantu", { onclick: ekspor }, "Ekspor progres"),
      h("button.tbl.tbl-hantu", { onclick: impor }, "Impor progres"),
      h("button.tbl.tbl-hantu", { onclick: async () => {
        const r = await api.kirim("/api/data/cadangkan", {});
        sorak(r.cadangan ? "Cadangan dibuat: " + r.cadangan
                         : "Belum ada progres untuk dicadangkan.",
              r.cadangan ? "tumbuh" : "");
      } }, "Buat cadangan")));
}

async function lihatLaporan() {
  const r = await api.ambil("/api/laporan");
  const pilih = await jendela({
    judul: "Laporan kemajuan",
    lebar: true,
    isi: h("div", {},
      h("p", { gaya: { color: "var(--redup)", fontSize: ".88rem" } },
        "Format Markdown, siap ditempel ke mana pun."),
      h("div.pra", { gaya: { maxHeight: "50vh", overflow: "auto" } },
        r.markdown)),
    aksi: [{ label: "Salin", nilai: "salin" },
           { label: "Unduh .md", nilai: "unduh" },
           { label: "Tutup", nilai: null, kelas: "tbl-utama" }],
  });
  if (pilih === "salin") salin(r.markdown, "Laporan disalin.");
  if (pilih === "unduh") unduh(r.markdown, "laporan-belajar.md", "text/markdown");
}

async function ekspor() {
  const r = await api.ambil("/api/data/ekspor");
  const nama = "progres-belajar-" + new Date().toISOString().slice(0, 10) + ".json";
  unduh(JSON.stringify(r.progres, null, 2), nama, "application/json");
  sorak("Progres diekspor ke " + nama, "tumbuh");
}

function unduh(isi, nama, tipe) {
  const url = URL.createObjectURL(new Blob([isi], { type: tipe }));
  const a = h("a", { href: url, download: nama });
  document.body.appendChild(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

async function impor() {
  const berkas = h("input", { type: "file", accept: ".json,application/json",
                              "aria-label": "Berkas progres untuk diimpor" });
  const pilih = await jendela({
    judul: "Impor progres",
    isi: h("div", {},
      h("p", {}, "Progres yang sekarang akan DIGANTI. Salinannya dicadangkan "
        + "otomatis lebih dulu, di sebelah berkas aslinya."),
      berkas),
    aksi: [{ label: "Batal", nilai: false },
           { label: "Impor", nilai: true, kelas: "tbl-bahaya" }],
  });
  if (pilih !== true || !berkas.files[0]) return;

  try {
    const teks = await berkas.files[0].text();
    const r = await api.kirim("/api/data/impor", { progres: JSON.parse(teks) });
    sorak("Progres diimpor. Cadangan lama: " + r.cadangan, "tumbuh", 6);
    setTimeout(() => location.reload(), 900);
  } catch (e) {
    sorak("Gagal mengimpor: " + e.message, "salah", 6);
  }
}

/* ============================================================== pengaturan */

export async function layarAtur(_params, ctx) {
  const konfig = await api.ambil("/api/konfigurasi");
  let tampilan = bacaTampilan();

  async function simpanKonfig(kunci, nilai) {
    try {
      await api.kirim("/api/konfigurasi", { [kunci]: nilai });
      sorak("Tersimpan.", "tumbuh", 1.6);
      ctx.segarkanUkuran();
    } catch (e) {
      sorak(e.message, "salah");
    }
  }

  const petakTema = h("div.petak.petak-2", {}, TEMA.map(([nilai, nama, ket]) =>
    h("button.kartu.kartu-rapat", {
      data: { temaPilihan: nilai },
      gaya: { textAlign: "left" },
      onclick: () => {
        // Warna seluruh halaman berganti dalam satu frame. Kelas alih-tema
        // memberinya transisi 260 md supaya yang terjadi terbaca sebagai
        // pergantian, bukan kedipan.
        if (adaGerak()) {
          document.documentElement.classList.add("alih-tema");
          setTimeout(
            () => document.documentElement.classList.remove("alih-tema"), 320);
        }
        tampilan = terapkanTampilan({ tema: nilai });
        tandaiTema();
      },
    },
      h("b", { gaya: { display: "block", fontSize: ".95rem" } }, nama),
      h("span", { gaya: { color: "var(--redup)", fontSize: ".82rem" } }, ket))));

  function tandaiTema() {
    for (const kt of petakTema.children) {
      const ini = kt.dataset.temaPilihan === tampilan.tema;
      kt.style.borderColor = ini ? "var(--nyala)" : "var(--garis)";
      kt.style.boxShadow = ini ? "var(--cahaya)" : "var(--bayang)";
    }
  }
  tandaiTema();

  const deretUkuran = h("div.deret", {}, UKURAN.map(([nilai, px]) =>
    h("button.tbl.tbl-kecil", {
      data: { ukuran: nilai },
      onclick: () => {
        tampilan = terapkanTampilan({ ukuran: nilai });
        tandaiUkuran();
      },
    }, `${nilai} · ${px}px`)));

  function tandaiUkuran() {
    for (const b of deretUkuran.children) {
      const ini = b.dataset.ukuran === tampilan.ukuran;
      b.classList.toggle("tbl-utama", ini);
      b.classList.toggle("tbl-hantu", !ini);
    }
  }
  tandaiUkuran();

  const idLebar = idBaru("lebar-baca");
  const labelLebar = h("label", { for: idLebar },
    "Lebar kolom baca: " + tampilan.lebarBaca + " karakter");
  const geser = h("input", {
    id: idLebar,
    type: "range", min: "50", max: "100", value: String(tampilan.lebarBaca),
  });
  geser.addEventListener("input", () => {
    tampilan = terapkanTampilan({ lebarBaca: Number(geser.value) });
    labelLebar.textContent = "Lebar kolom baca: " + geser.value + " karakter";
  });

  const el = h("div.masuk-urut", {},
    h("header.kepala-besar", {},
      h("span.mata", {}, "Sesuaikan"),
      h("h1", {}, "Pengaturan"),
      h("p.kepala-sub", {}, "Yang mengatur TAMPILAN disimpan di browser ini "
        + "saja. Yang mengatur BELAJAR disimpan ke berkas, jadi berlaku juga "
        + "di aplikasi terminal.")),

    h("section", {},
      h("span.mata", {}, "Tampilan — hanya untuk browser ini"),
      h("div.kartu", {},
        h("div.medan", {}, h("label", {}, "Tema warna"), petakTema),
        h("div.medan", {}, h("label", {}, "Ukuran huruf"), deretUkuran),
        h("div.medan", {}, labelLebar,
          h("div.ket", {}, "Baris yang terlalu panjang membuat mata kehilangan "
            + "awal baris berikutnya. 60–75 karakter biasanya paling nyaman."),
          geser),
        h("div.medan", {},
          h("label", {}, "Gerak"),
          h("div.ket", {},
            "Setelan sistem \u201ckurangi gerak\u201d selalu menang atas "
            + "pilihan di sini: kalau sistemmu sudah memintanya, tidak ada "
            + "yang bergerak apa pun yang kamu pilih."),
          petakGerak(tampilan, (t) => { tampilan = t; })))),

    h("section", {},
      h("span.mata", {}, "Belajar — berlaku juga di aplikasi terminal"),
      h("div.kartu", { gaya: { display: "grid", gap: "4px" } },
        // Berdiri PALING ATAS di kartu ini, dan itu disengaja. Dua layar lain
        // menjanjikannya dengan kalimat "buka semua bab di Pengaturan" — bab
        // yang terkunci dan layar penolakan 403 — jadi orang yang tiba di sini
        // datang untuk satu saklar tertentu. Menaruhnya di tengah daftar
        // berarti menyuruh mereka mencari sesuatu yang baru saja dijanjikan.
        h("div", { id: "atur-bab" },
          sakelarBaris(konfig.buka_semua_bab.label,
            konfig.buka_semua_bab.keterangan,
            konfig.buka_semua_bab.nilai,
            (v) => simpanKonfig("buka_semua_bab", v))),
        h("div", { gaya: { height: "9px" } }),
        medanTeks(konfig.nama, "Nama panggilan",
          "Dipakai untuk menyapamu di dasbor. Boleh dikosongkan.",
          (v) => simpanKonfig("nama", v)),
        medanAngka(konfig.target_xp_harian, "Target XP harian",
          (v) => simpanKonfig("target_xp_harian", v)),
        medanAngka(konfig.detik_per_soal, "Detik per soal saat mode timer",
          (v) => simpanKonfig("detik_per_soal", v)),
        sakelarBaris(konfig.acak_bawaan.label, konfig.acak_bawaan.keterangan,
          konfig.acak_bawaan.nilai, (v) => simpanKonfig("acak_bawaan", v)),
        h("div", { gaya: { height: "9px" } }),
        sakelarBaris(konfig.konfirmasi_jawaban.label,
          konfig.konfirmasi_jawaban.keterangan,
          konfig.konfirmasi_jawaban.nilai,
          (v) => simpanKonfig("konfirmasi_jawaban", v)),
        h("div", { gaya: { height: "9px" } }),
        medanTeks(konfig.editor, "Editor teks untuk aplikasi terminal",
          "Kosongkan untuk memakai $EDITOR. Tidak berpengaruh di browser.",
          (v) => simpanKonfig("editor", v)))),

    h("section", {},
      h("span.mata", {}, "Letak berkas"),
      h("div.kartu", { gaya: { display: "grid", gap: "9px",
                               fontSize: ".85rem" } },
        barisBerkas("Progres belajar", ctx.awal.lokasi.progres),
        barisBerkas("Pengaturan", ctx.awal.lokasi.konfigurasi),
        barisBerkas("Catatan pribadi", ctx.awal.lokasi.catatan),
        barisBerkas("Kode jawabanmu", ctx.awal.lokasi.kerja))),

    blokData(),
    blokBahaya(ctx),

    h("section", {},
      h("span.mata", {}, "Tentang"),
      h("div.kartu", {},
        h("p", {}, `Belajar Ngoding versi ${ctx.awal.versi} `
          + `(antarmuka web ${ctx.awal.versi_web}). Tanpa dependensi luar — `
          + "cukup Python 3.8+ dan sebuah browser."),
        h("p", { gaya: { margin: "0", color: "var(--redup)",
                         fontSize: ".87rem" } },
          `Kode yang kamu jalankan dibatasi ${ctx.awal.batas.waktu} detik dan `
          + `${ctx.awal.batas.memori_mb} MB memori. Ini bukan sandbox `
          + "keamanan: kode berjalan dengan hak akses yang sama denganmu, jadi "
          + "jangan menjalankan kode dari sumber yang tidak kamu percaya."))),
  );

  return { el, judul: "Pengaturan", jejak: [{ label: "Pengaturan" }] };
}

/** Tiga kartu tingkat gerak, dan tiap kartu MEMPERAGAKAN pilihannya.
 *
 *  Menekan sebuah kartu langsung menjalankan gerakan contoh di titik itu juga.
 *  Kalau tidak, satu-satunya cara tahu apa arti "halus" adalah memilihnya,
 *  keluar dari Pengaturan, dan mencoba mengingat rasanya yang tadi — dan tidak
 *  ada orang yang mau melakukan itu tiga kali untuk membandingkan. */
function petakGerak(tampilan, saatUbah) {
  const petak = h("div.petak.petak-3", {}, GERAK.map(([nilai, nama, ket]) => {
    const titik = h("span", { gaya: {
      width: "13px", height: "13px", borderRadius: "50%", flex: "none",
      background: "var(--nyala)", display: "block" } });

    const kartu = h("button.kartu.kartu-rapat", {
      data: { gerakPilihan: nilai },
      gaya: { textAlign: "left" },
      onclick: () => {
        saatUbah(terapkanTampilan({ gerak: nilai }));
        tandai();
        // Peragaan dijalankan SESUDAH tingkatnya dipasang, jadi yang terlihat
        // memang gerakan pada tingkat yang barusan dipilih.
        if (nilai === "mati") sorak("Gerak dimatikan.", "", 1.6);
        else denyut(kartu);
      },
    },
      h("div.deret", { gaya: { marginBottom: "6px" } },
        titik,
        h("b", { gaya: { fontSize: ".95rem" } }, nama)),
      h("span", { gaya: { color: "var(--redup)", fontSize: ".82rem" } }, ket));
    return kartu;
  }));

  function tandai() {
    const kini = bacaTampilan().gerak;
    for (const kt of petak.children) {
      const ini = kt.dataset.gerakPilihan === kini;
      kt.style.borderColor = ini ? "var(--nyala)" : "var(--garis)";
      kt.style.boxShadow = ini ? "var(--cahaya)" : "var(--bayang)";
      const t = kt.querySelector("span");
      t.style.background = ini ? "var(--nyala)" : "var(--garis-kuat)";
      t.style.boxShadow = ini ? "0 0 10px -1px var(--nyala)" : "none";
    }
  }
  tandai();

  // Sistem yang menyetel "kurangi gerak" membuat pilihan di sini tak berarti.
  // Katakan itu terus terang alih-alih membiarkan kartunya tampak berfungsi.
  if (tingkatGerak() === "mati" && bacaTampilan().gerak !== "mati") {
    petak.appendChild(h("div.arti", { gaya: { gridColumn: "1 / -1" } },
      h("b", {}, "Sedang ditahan sistem"),
      h("div", {}, "Sistem operasimu menyetel \u201ckurangi gerak\u201d, jadi "
        + "gerak tetap mati sampai setelan itu diubah.")));
  }
  return petak;
}

function sakelarBaris(judul, ket, awal, saatUbah) {
  let nyala = Boolean(awal);
  const tbl = h("button.sakelar" + (nyala ? ".on" : ""), {
    role: "switch", "aria-checked": String(nyala),
    onclick: () => {
      nyala = !nyala;
      tbl.classList.toggle("on", nyala);
      tbl.setAttribute("aria-checked", String(nyala));
      saatUbah(nyala);
    },
  }, h("div.isi", {}, h("b", {}, judul), h("span", {}, ket)), h("div.knop", {}));
  return tbl;
}

function medanTeks(opsi, label, ket, saatSimpan) {
  const masuk = h("input", { type: "text", value: opsi.nilai || "" });
  let terakhir = masuk.value;
  const kirim = () => {
    if (masuk.value !== terakhir) {
      terakhir = masuk.value;
      saatSimpan(masuk.value);
    }
  };
  masuk.addEventListener("blur", kirim);
  masuk.addEventListener("keydown", (e) => { if (e.key === "Enter") masuk.blur(); });
  return medan(label, masuk, ket);
}

function medanAngka(opsi, label, saatSimpan) {
  const masuk = h("input", {
    type: "number", value: String(opsi.nilai),
    min: opsi.minimum === null ? "" : String(opsi.minimum),
    max: opsi.maksimum === null ? "" : String(opsi.maksimum),
  });
  let terakhir = masuk.value;
  const kirim = () => {
    if (masuk.value !== terakhir) {
      terakhir = masuk.value;
      saatSimpan(Number(masuk.value));
    }
  };
  masuk.addEventListener("blur", kirim);
  masuk.addEventListener("keydown", (e) => { if (e.key === "Enter") masuk.blur(); });
  return medan(label, masuk, opsi.keterangan);
}

function barisBerkas(label, jalur) {
  return h("div", { gaya: { display: "flex", gap: "12px", flexWrap: "wrap",
                            alignItems: "center" } },
    h("span", { gaya: { color: "var(--redup)", minWidth: "140px" } }, label),
    h("code", { gaya: { flex: "1", minWidth: "200px", wordBreak: "break-all" } },
      jalur),
    h("button.tbl.tbl-kecil.tbl-hantu",
      { onclick: () => salin(jalur, "Path disalin.") }, "Salin"));
}

function blokBahaya(ctx) {
  const pilih = h("select", { "aria-label": "Bahasa yang direset",
                              gaya: { width: "auto" } },
    ctx.awal.bahasa.map((b) => h("option", { value: b.key }, b.label)));

  return h("section", {},
    h("span.mata", {}, "Menghapus progres"),
    h("div.kartu", { gaya: {
      borderColor: "color-mix(in srgb, var(--salah) 32%, transparent)" } },
      h("p", { gaya: { color: "var(--teks-2)", fontSize: ".89rem" } },
        "Cadangan otomatis dibuat sebelum menghapus, di sebelah berkas "
        + "progresnya. Catatan pribadimu tidak ikut terhapus — ia tinggal di "
        + "berkas yang lain."),
      h("div.deret", {},
        pilih,
        h("button.tbl.tbl-bahaya", { onclick: async () => {
          const nama = pilih.options[pilih.selectedIndex].text;
          if (!await konfirmasi(
            `Hapus SELURUH progres ${nama}? Materi, kuis, dan latihannya `
            + "kembali ke nol. Ini tidak bisa dibatalkan.",
            { judul: "Reset " + nama, labelYa: "Hapus progres " + nama,
              bahaya: true })) return;
          const r = await api.kirim("/api/data/reset",
            { bagian: pilih.value, konfirmasi: "HAPUS" });
          sorak(`Progres ${nama} dihapus. Cadangan: ${r.cadangan || "-"}`,
                "tumbuh", 6);
          setTimeout(() => location.reload(), 900);
        } }, "Reset satu bahasa"),
        h("span.deret-kanan"),
        h("button.tbl.tbl-bahaya", { onclick: resetSemua },
          "Reset SEMUA progres"))));
}

async function resetSemua() {
  if (!await konfirmasi(
    "Ini menghapus XP, level, streak, badge, dan seluruh riwayat di sembilan "
    + "bahasa sekaligus.",
    { judul: "Reset seluruh progres", labelYa: "Lanjut", bahaya: true })) return;

  const ketikan = h("input", { type: "text", placeholder: "HAPUS",
                              "aria-label": "Ketik HAPUS untuk mengonfirmasi" });
  const lagi = await jendela({
    judul: "Konfirmasi terakhir",
    isi: h("div", {},
      h("p", {}, "Ketik HAPUS di bawah untuk mengonfirmasi. Cadangan dibuat "
        + "lebih dulu, tapi jangan mengandalkan itu."),
      ketikan),
    aksi: [{ label: "Batal", nilai: false },
           { label: "Hapus semuanya", nilai: true, kelas: "tbl-bahaya" }],
  });
  if (lagi !== true) return;
  if (ketikan.value.trim() !== "HAPUS") {
    getar(ketikan);
    sorak("Kata konfirmasi tidak cocok. Tidak ada yang dihapus.", "salah");
    return;
  }
  const r = await api.kirim("/api/data/reset",
                            { bagian: "semua", konfirmasi: "HAPUS" });
  sorak("Semua progres dihapus. Cadangan: " + (r.cadangan || "-"), "tumbuh", 6);
  setTimeout(() => location.reload(), 1200);
}

/* ================================================================= bantuan */

export const PINTASAN = [
  ["Ctrl K", "Palet perintah — lompat ke mana saja"],
  ["Ctrl B", "Sembunyikan / tampilkan panel kiri"],
  ["Ctrl J", "Ganti tema"],
  ["G lalu D", "Ke dasbor"],
  ["G lalu C", "Ke ruang coba"],
  ["G lalu S", "Ke statistik"],
  ["G lalu B", "Ke bookmark"],
  ["?", "Tampilkan daftar ini"],
  ["Esc", "Tutup dialog"],
  ["1–9 atau A–J", "Menjawab soal kuis"],
  ["Ctrl ⏎", "Jalankan kode di editor"],
  ["Ctrl ⇧ ⏎", "Periksa jawaban latihan"],
  ["Ctrl S", "Simpan kode"],
  ["Ctrl /", "Komentari baris di editor"],
  ["Tab atau ⇧ Tab", "Tambah atau kurangi indentasi"],
];

export function tampilkanBantuan() {
  return jendela({
    judul: "Pintasan papan ketik",
    isi: h("div", { gaya: { display: "grid", gap: "7px" } },
      PINTASAN.map(([tombol, arti]) =>
        h("div", { gaya: { display: "flex", gap: "14px",
                           alignItems: "center" } },
          h("kbd", { gaya: { minWidth: "104px", textAlign: "center" } }, tombol),
          h("span", { gaya: { fontSize: ".9rem" } }, arti)))),
    aksi: [{ label: "Tutup", nilai: null, kelas: "tbl-utama" }],
  });
}
