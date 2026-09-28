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
  api, h, bilah, angka, sorak, konfirmasi, jendela, salin, keadaan,
  simpanLokal, ambilLokal, idBaru, medan,
} from "./inti.js";
import {
  ungkap, angkaKe, denyut, getar, tingkatGerak, adaGerak,
} from "./gerak.js";
import { ikon } from "./ikon.js";

export const TEMA = [
  ["gelap", "Gelap", "Ungu-tinta. Bawaan, untuk pemakaian sehari-hari."],
  ["malam", "Malam", "Serba hangat, kontras rendah. Untuk mata yang lelah."],
  ["terang", "Terang", "Kertas berkabut. Untuk ruangan yang benderang."],
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
   "Semua gerakan hidup: perpindahan berpegas, urutan masuk, denyut bara."],
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
      h("div.kartu.deret.deret-rapat", {}, (s.tangga_gelar || []).map((g) =>
        h("span.pil" + (s.level >= g.level ? ".pil-nyala" : ""), {},
          `Lv ${g.level} · ${g.nama}`)))),

    blokBadge(s, punya, belum),

    blokToolchainSemua(s),
    blokXp(s),
    blokData(),
  );
  return { el, judul: "Statistik" };
}

/** @param angkaMentah  kalau diisi, angkanya BERJALAN naik dari nol sampai ke
 *                      situ saat kartunya tergulir ke layar. Yang dilewatkan
 *                      sebagai `nilai` tetap dipakai apa adanya untuk bentuk
 *                      yang bukan angka tunggal ("3/22"). */
function angkaBesar(nilai, label, ket, angkaMentah) {
  const isi = h("div.angka-besar", {}, nilai);
  const el = h("div.kartu.kartu-rapat.kartu-angka", {},
    isi,
    h("div.mata", {}, label),
    ket ? h("div.ket", {}, ket) : null);

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
      h("div.rinci", {},
        s.bahasa.map((b) => h("div.rinci-baris", {},
          h("div.rinci-atas", {},
            h("a", { href: "#/bahasa/" + b.key }, b.label),
            h("span.rinci-angka", {},
              `${b.materi}/${b.total_materi} materi · `
              + `${b.kuis}/${b.total_kuis} kuis · `
              + `${b.latihan_lulus + b.latihan_manual}/${b.total_latihan} latihan`
              + (b.skor_maks ? ` · skor ${b.skor}/${b.skor_maks}` : ""))),
          bilah(b.persen, b.persen >= 100 ? "tumbuh" : ""))),
        h("div.rinci-total", {},
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
      h("div.rinci", {}, s.toolchain.map((t) => h("div.alat-baris", {},
        h("span.titik" + (t.siap ? ".selesai" : ".gagal"), {}),
        h("b", {}, t.label),
        t.siap
          ? h("span", { gaya: { color: "var(--tumbuh)" } }, "siap dipakai")
          : h("span.baris-sisi", {}, `butuh ${t.hilang.join(", ")}`),
        !t.siap && t.pasang ? h("code", {}, t.pasang) : null,
        !t.siap && t.pasang ? h("button.tbl.tbl-kecil.tbl-hantu", {
          onclick: () => salin(t.pasang, "Perintah disalin."),
        }, "Salin") : null))),
      h("p.baris-sisi", { gaya: { margin: "var(--s4) 0 0" } },
        "Toolchain itu opsional. Materi dan kuis berjalan penuh tanpa satu pun "
        + "compiler; yang mati hanya penilaian otomatis untuk bahasa itu.")));
}

function blokXp(s) {
  const t = s.xp_tarif;
  return h("section", {},
    h("span.mata", {}, "Dari mana XP datang"),
    h("div.kartu.deret.deret-rapat", {},
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
      h("p.kepala-sub", { gaya: { margin: "0 0 var(--s3)" } },
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
      const r = await api.kirim("/api/konfigurasi", { [kunci]: nilai });
      // Salinan konfigurasi yang dipegang ctx diambil sekali saat aplikasi
      // dimuat. Tanpa baris ini ia basi sampai halaman dimuat ulang — dan
      // layar kuis yang membaca "acak bawaan" dari situ akan memakai nilai
      // yang baru saja diubah orangnya, tapi belum ia lihat berlaku.
      if (r && r.konfigurasi) ctx.awal.konfigurasi = r.konfigurasi;
      sorak("Tersimpan.", "tumbuh", 1.6);
      ctx.segarkanUkuran();
    } catch (e) {
      sorak(e.message, "salah");
    }
  }

  /* Pilihan yang sedang aktif ditandai TIGA hal: kelas `.terpilih` (garis
     aksen), sebuah pil bertanda centang di dalam kartunya, dan `aria-pressed`.
     Warna saja tidak cukup — itu syarat WCAG 1.4.1, dan di halaman yang justru
     memuat tema kontras tinggi, melanggarnya akan lucu sekaligus melelahkan.
     Versi sebelumnya menandai pilihan dengan menulis `style.borderColor`
     langsung: satu isyarat, cuma warna, dan tak terbaca pembaca layar. */
  function kartuPilihan(nilai, nama, ket, saatPilih) {
    const tanda = h("span.pil.pil-nyala", { hidden: true },
      ikon("selesai", { ukuran: 13, tebal: 2 }), "dipakai");
    const kartu = h("button.kartu.kartu-rapat", {
      data: { pilihan: nilai },
      gaya: { textAlign: "left" },
      onclick: () => saatPilih(kartu),
    },
      h("div.deret.deret-rapat", { gaya: { marginBottom: "var(--s1)" } },
        h("b", {}, nama), tanda),
      h("span.baris-sisi", {}, ket));
    kartu.tanda = tanda;
    return kartu;
  }

  function tandaiPilihan(petak, kini) {
    for (const kt of petak.children) {
      if (!kt.dataset || !kt.dataset.pilihan) continue;
      const ini = kt.dataset.pilihan === kini;
      kt.classList.toggle("terpilih", ini);
      kt.setAttribute("aria-pressed", String(ini));
      if (kt.tanda) kt.tanda.hidden = !ini;
    }
  }

  const petakTema = h("div.petak.petak-2", {}, TEMA.map(([nilai, nama, ket]) =>
    kartuPilihan(nilai, nama, ket, () => {
      // Warna seluruh halaman berganti dalam satu frame. Kelas alih-tema
      // memberinya transisi 260 md supaya yang terjadi terbaca sebagai
      // pergantian, bukan kedipan.
      if (adaGerak()) {
        document.documentElement.classList.add("alih-tema");
        setTimeout(
          () => document.documentElement.classList.remove("alih-tema"), 320);
      }
      tampilan = terapkanTampilan({ tema: nilai });
      tandaiPilihan(petakTema, tampilan.tema);
    })));
  tandaiPilihan(petakTema, tampilan.tema);

  const deretUkuran = h("div.deret.deret-rapat", {}, UKURAN.map(([nilai, px]) =>
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
      b.classList.toggle("tbl-pilih", ini);
      b.classList.toggle("tbl-hantu", !ini);
      b.setAttribute("aria-pressed", String(ini));
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

  /* Tiga kartu tingkat gerak, dan tiap kartu MEMPERAGAKAN pilihannya.
   *
   * Menekan sebuah kartu langsung menjalankan gerakan contoh di titik itu
   * juga. Kalau tidak, satu-satunya cara tahu apa arti "halus" adalah
   * memilihnya, keluar dari Pengaturan, dan mencoba mengingat rasanya yang
   * tadi — dan tidak ada orang yang mau melakukan itu tiga kali untuk
   * membandingkan. */
  const petakGerak = h("div.petak.petak-3", {}, GERAK.map(([nilai, nama, ket]) =>
    kartuPilihan(nilai, nama, ket, (kartu) => {
      tampilan = terapkanTampilan({ gerak: nilai });
      tandaiPilihan(petakGerak, bacaTampilan().gerak);
      // Peragaan dijalankan SESUDAH tingkatnya dipasang, jadi yang terlihat
      // memang gerakan pada tingkat yang barusan dipilih.
      if (nilai === "mati") sorak("Gerak dimatikan.", "", 1.6);
      else denyut(kartu);
    })));
  tandaiPilihan(petakGerak, tampilan.gerak);

  // Sistem yang menyetel "kurangi gerak" membuat pilihan di sini tak berarti.
  // Katakan itu terus terang alih-alih membiarkan kartunya tampak berfungsi.
  const tahanGerak = tingkatGerak() === "mati" && bacaTampilan().gerak !== "mati"
    ? keadaan({
        jenis: "kunci",
        gambar: "belum",
        judul: "Sedang ditahan sistem",
        ket: "Sistem operasimu menyetel “kurangi gerak”, jadi gerak "
          + "tetap mati sampai setelan itu diubah.",
      })
    : null;

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
            "Setelan sistem “kurangi gerak” selalu menang atas "
            + "pilihan di sini: kalau sistemmu sudah memintanya, tidak ada "
            + "yang bergerak apa pun yang kamu pilih."),
          petakGerak,
          tahanGerak))),

    h("section", {},
      h("span.mata", {}, "Belajar — berlaku juga di aplikasi terminal"),
      h("div.kartu", { gaya: { display: "grid", gap: "var(--s1)" } },
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
        h("div", { gaya: { height: "var(--s2)" } }),
        medanTeks(konfig.nama, "Nama panggilan",
          "Dipakai untuk menyapamu di dasbor. Boleh dikosongkan.",
          (v) => simpanKonfig("nama", v)),
        medanAngka(konfig.target_xp_harian, "Target XP harian",
          (v) => simpanKonfig("target_xp_harian", v)),
        medanAngka(konfig.detik_per_soal, "Detik per soal saat mode timer",
          (v) => simpanKonfig("detik_per_soal", v)),
        sakelarBaris(konfig.acak_bawaan.label, konfig.acak_bawaan.keterangan,
          konfig.acak_bawaan.nilai, (v) => simpanKonfig("acak_bawaan", v)),
        h("div", { gaya: { height: "var(--s2)" } }),
        sakelarBaris(konfig.konfirmasi_jawaban.label,
          konfig.konfirmasi_jawaban.keterangan,
          konfig.konfirmasi_jawaban.nilai,
          (v) => simpanKonfig("konfirmasi_jawaban", v)),
        h("div", { gaya: { height: "var(--s2)" } }),
        medanTeks(konfig.editor, "Editor teks untuk aplikasi terminal",
          "Kosongkan untuk memakai $EDITOR. Tidak berpengaruh di browser.",
          (v) => simpanKonfig("editor", v)))),

    h("section", {},
      h("span.mata", {}, "Letak berkas"),
      h("div.kartu", { gaya: { display: "grid", gap: "var(--s2)" } },
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
        h("p.baris-sisi", { gaya: { margin: "0" } },
          `Kode yang kamu jalankan dibatasi ${ctx.awal.batas.waktu} detik dan `
          + `${ctx.awal.batas.memori_mb} MB memori. Ini bukan sandbox `
          + "keamanan: kode berjalan dengan hak akses yang sama denganmu, jadi "
          + "jangan menjalankan kode dari sumber yang tidak kamu percaya."))),
  );

  return { el, judul: "Pengaturan" };
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
  const isian = h("input", { type: "text", value: opsi.nilai || "" });
  let terakhir = isian.value;
  const kirim = () => {
    if (isian.value !== terakhir) {
      terakhir = isian.value;
      saatSimpan(isian.value);
    }
  };
  isian.addEventListener("blur", kirim);
  isian.addEventListener("keydown", (e) => { if (e.key === "Enter") isian.blur(); });
  return medan(label, isian, ket);
}

function medanAngka(opsi, label, saatSimpan) {
  const isian = h("input", {
    type: "number", value: String(opsi.nilai),
    min: opsi.minimum === null ? "" : String(opsi.minimum),
    max: opsi.maksimum === null ? "" : String(opsi.maksimum),
  });
  let terakhir = isian.value;
  const kirim = () => {
    if (isian.value !== terakhir) {
      terakhir = isian.value;
      saatSimpan(Number(isian.value));
    }
  };
  isian.addEventListener("blur", kirim);
  isian.addEventListener("keydown", (e) => { if (e.key === "Enter") isian.blur(); });
  return medan(label, isian, opsi.keterangan);
}

function barisBerkas(label, jalur) {
  return h("div.jalur-baris", {},
    h("span", {}, label),
    h("code", {}, jalur),
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
      h("p", { gaya: { color: "var(--teks-2)", fontSize: "var(--t-ui)" } },
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
    "Ini menghapus XP, level, streak, badge, dan seluruh riwayat di sebelas "
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
  ["Ctrl B", "Buka / tutup menu (hanya di layar sempit)"],
  ["Ctrl J", "Ganti tema"],
  ["G lalu D", "Ke dasbor"],
  ["G lalu C", "Ke ruang coba"],
  ["G lalu S", "Ke statistik"],
  ["G lalu B", "Ke bookmark"],
  ["G lalu N", "Ke catatanku"],
  ["G lalu P", "Ke pengaturan"],
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
    isi: h("div", { gaya: { display: "grid", gap: "var(--s2)" } },
      PINTASAN.map(([tombol, arti]) =>
        h("div.pintasan-baris", {},
          h("kbd", {}, tombol),
          h("span", {}, arti)))),
    aksi: [{ label: "Tutup", nilai: null, kelas: "tbl-utama" }],
  });
}
