/* Layar yang dipakai untuk MEMBACA: dasbor, halaman bahasa, pembaca materi,
 * pencarian, bookmark, dan catatan.
 *
 * Pertanyaan yang dijawab dasbor bukan "apa saja capaianku" melainkan "habis
 * ini ngapain". Aplikasi ini menyimpan 334 materi, 67 kuis, dan 159 latihan di
 * sebelas bahasa; buat orang yang baru mulai, daftar sepanjang itu bukan
 * kekayaan melainkan kelumpuhan. Bab bertingkat menjawab separuhnya — mana yang
 * boleh dibuka sekarang — dan Langkah Berikutnya menjawab sisanya. Karena itu blok pertama di bawah cincin level
 * adalah Langkah Berikutnya — antrean yang disusun `saran.py` dari progres
 * nyata, bukan sekadar daftar isi.
 *
 * Importir: aplikasi.js.
 */

import {
  api, h, bilah, bulat, angka, kosong, sorak, rayakan, salin, tanggalRamah,
  jamRamah, selisihHari, jendela, tandai, GalatApi,
} from "./inti.js";
import {
  animasi, masuk, ungkap, saatTampak, denyut, percikBara, adaGerak, berurut,
} from "./gerak.js";
import { ikon, ikonTipe } from "./ikon.js";
import { praKode } from "./sorot.js";

function pilTipe(t) {
  return t === "kuis" ? ".pil-ungu" : t === "latihan" ? ".pil-nyala" : ".pil-tenang";
}

/** Pil bertanda jenis isi: ikon + kata. Ikonnya membuat jenisnya terbaca
 *  sebelum katanya sempat dibaca — dan di daftar sepanjang dua puluh baris,
 *  "sebelum dibaca" itu selisih yang besar. */
export function pilJenis(tipe) {
  return h("span.pil.pil-jenis" + pilTipe(tipe), {},
    ikon(ikonTipe(tipe), { ukuran: 14, tebal: 1.9 }), tipe);
}

function potong(t, n) {
  return t && t.length > n ? t.slice(0, n - 1) + "…" : t;
}

/** Buang awalan penomoran dari judul.
 *
 *  Judul di kurikulum sudah membawa nomornya sendiri ("2. Variabel & Tipe
 *  Data"), dan tiap daftar di sini juga punya kolom nomor tersendiri — jadi
 *  yang terbaca "2  2. Variabel & Tipe Data". Di kolom selebar 250 px,
 *  pengulangan itu memakan ruang yang justru paling dibutuhkan judulnya.
 *  Nomornya dibuang di TAMPILAN saja; datanya tidak disentuh, karena judul
 *  itu juga dipakai sebagai kunci progres (lihat AGENTS.md — judul wajib unik
 *  per bahasa, dan mengubahnya berarti kehilangan progres). */
function tanpaNomor(judul) {
  return String(judul || "").replace(/^\s*\d+\.\s*/, "");
}

/* ================================================================ dasbor */

export async function layarDasbor() {
  const d = await api.ambil("/api/dasbor");
  const jam = new Date().getHours();
  const sapa = jam < 11 ? "Selamat pagi" : jam < 15 ? "Selamat siang"
             : jam < 19 ? "Selamat sore" : "Selamat malam";

  // Langkah PERTAMA diangkat keluar dari daftar dan diberi kartunya sendiri.
  // Inilah perubahan susunan yang paling menentukan di seluruh dasbor: yang
  // dibutuhkan orang yang belajar dari nol bukan ringkasan capaiannya,
  // melainkan satu kalimat yang menjawab "sekarang aku ngapain". Sisanya —
  // level, XP, bara enam bulan — tetap ada, tapi menunggu di bawahnya.
  const [utama, ...sisaLangkah] = d.langkah;

  const el = h("div.masuk-urut", {},
    h("header.sambut", {},
      h("span.mata", {}, new Date().toLocaleDateString("id-ID",
        { weekday: "long", day: "numeric", month: "long", year: "numeric" })),
      h("h1", {}, d.nama ? `${sapa}, ${d.nama}.` : `${sapa}.`),
      h("p.sambut-sub", {}, kalimatPembuka(d))),

    utama ? kartuLanjutkan(utama) : null,
    kartuBara(d),
    sisaLangkah.length ? blokLangkah(sisaLangkah) : null,
    d.tantangan ? blokTantangan(d.tantangan) : null,
    blokBahasa(d.bahasa),
    blokBara(d),
  );
  return { el, judul: "Dasbor", jejak: [{ label: "Dasbor" }] };
}

/** Kartu tindakan utama dasbor.
 *
 *  Satu-satunya benda di halaman ini yang memakai warna aksen sebagai LATAR,
 *  bukan sekadar garis. Itu batas yang dijaga ketat di seluruh aplikasi: kalau
 *  dua hal sama-sama memakai amber pekat, tidak ada lagi yang namanya "yang
 *  sedang kamu kerjakan". */
function kartuLanjutkan(s) {
  const jenis = { materi: "Baca materi", kuis: "Kerjakan kuis",
                  latihan: "Kerjakan latihan" }[s.tipe] || "Lanjutkan";
  return h("a.lanjutkan", { href: tautanLangkah(s) },
    h("div.lanjutkan-isi", {},
      h("span.mata", {}, jenis),
      h("h2", {}, `${s.label_bahasa} — ${s.judul}`),
      h("p", {}, s.alasan)),
    h("span.lanjutkan-tbl", {},
      h("span", {}, "Lanjutkan"),
      ikon("lanjut", { ukuran: 20 })));
}

function kalimatPembuka(d) {
  if (d.xp === 0) {
    return "Belum ada yang dimulai. Pilih satu langkah di bawah — cukup satu.";
  }
  if (d.xp_hari_ini >= d.target_harian) {
    return "Target hari ini sudah tercapai. Sisanya bonus.";
  }
  if (d.streak >= 2) {
    return `Sudah ${d.streak} hari berturut-turut. Jaga apinya tetap menyala.`;
  }
  if (d.xp_hari_ini > 0) {
    return `Kurang ${d.target_harian - d.xp_hari_ini} XP lagi untuk menutup hari ini.`;
  }
  return "Belum ada yang dikerjakan hari ini.";
}

function cincinLevel(d) {
  const R = 56;
  const keliling = 2 * Math.PI * R;
  const rasio = Math.max(0, Math.min(1, d.di_level / Math.max(1, d.butuh_level)));
  const panas = Math.max(0, Math.min(1, d.xp_hari_ini / Math.max(1, d.target_harian)));
  const NS = "http://www.w3.org/2000/svg";

  const svg = document.createElementNS(NS, "svg");
  svg.setAttribute("viewBox", "0 0 132 132");
  svg.setAttribute("aria-hidden", "true");

  const alur = document.createElementNS(NS, "circle");
  const isi = document.createElementNS(NS, "circle");
  for (const [c, kelas] of [[alur, "alur"], [isi, "isi"]]) {
    c.setAttribute("cx", "66");
    c.setAttribute("cy", "66");
    c.setAttribute("r", String(R));
    c.setAttribute("fill", "none");
    c.setAttribute("stroke-width", "7");
    c.setAttribute("class", kelas);
    svg.appendChild(c);
  }
  const akhir = keliling * (1 - rasio);
  isi.setAttribute("stroke-dasharray", String(keliling));
  // Nilai AKHIR dipasang langsung; animasinya cuma berangkat dari lingkaran
  // kosong. Kalau gerak dimatikan atau animasinya dibatalkan, yang tertinggal
  // tetap busur dengan panjang yang benar — bukan lingkaran kosong.
  isi.setAttribute("stroke-dashoffset", String(akhir));

  const cincin = h("div.cincin", {
    gaya: { "--panas": String(panas) },
    title: `${d.di_level} dari ${d.butuh_level} XP menuju level ${d.level + 1}`,
  }, svg, h("div.cincin-isi", {},
    h("div.cincin-angka", {}, String(d.level)),
    h("div.cincin-label", {}, "level")));

  // Busurnya baru digambar saat cincinnya benar-benar terlihat. Ini elemen
  // paling atas di dasbor, jadi hampir selalu langsung tampak — tapi kalau
  // dasbor dibuka sudah dalam keadaan tergulir, mengisi busur di luar layar
  // berarti membuang satu-satunya gerakan yang pantas dilihat di halaman ini.
  saatTampak(cincin, () => {
    animasi(isi, { strokeDashoffset: [String(keliling), String(akhir)] },
            { pegas: "panjang", durasi: 900 });
  }, { bagian: 0.35 });
  return cincin;
}

function kartuBara(d) {
  const kurang = Math.max(0, d.target_harian - d.xp_hari_ini);
  return h("div.kartu.kartu-level", {},
    cincinLevel(d),
    h("div.kartu-level-isi", {},
      h("h2", {}, d.gelar),
      h("div.kartu-level-ket", {},
        `${angka(d.xp)} XP total · ${d.di_level} dari ${d.butuh_level} `
        + `menuju level ${d.level + 1}`),
      bilah(d.di_level / Math.max(1, d.butuh_level) * 100),

      h("div.deret", { gaya: { marginTop: "var(--s5)" } },
        h("span.pil" + (d.streak ? ".pil-nyala" : ""), {},
          ikon("api", { ukuran: 14, tebal: 1.9 }),
          d.streak ? `${d.streak} hari beruntun` : "streak terputus"),
        h("span.pil", {}, `rekor ${d.streak_rekor} hari`),
        h("a.pil" + (d.badge_dimiliki ? ".pil-ungu" : ""),
          { href: "#/statistik" },
          ikon("bintang", { ukuran: 14, tebal: 1.9 }),
          `${d.badge_dimiliki}/${d.badge_total} badge`)),

      h("div.target", {},
        h("div.target-baris", {},
          h("span", {}, "Target hari ini"),
          h("b", { gaya: { color: kurang ? "var(--teks)" : "var(--tumbuh)" } },
            kurang ? `${d.xp_hari_ini}/${d.target_harian} XP` : "tercapai")),
        bilah(d.xp_hari_ini / Math.max(1, d.target_harian) * 100,
              kurang ? "" : "tumbuh"))));
}

function tautanLangkah(s) {
  return `#/${s.tipe}/${s.bahasa}/${s.indeks}`;
}

function blokLangkah(langkah) {
  const senarai = h("div.senarai", {}, langkah.map((s) => h("a.baris", { href: tautanLangkah(s) },
      pilJenis(s.tipe),
      h("div.isi", {},
        h("div.judul", {}, `${s.label_bahasa} — ${s.judul}`),
        h("div.ket", {}, s.alasan)),
      h("span.baris-panah", {}, ikon("lanjut", { ukuran: 18 })))));
  ungkap(senarai, { per: 46, geser: 10 });
  return h("section", {},
    h("span.mata", {}, "Sesudah itu"),
    senarai);
}

function blokTantangan(t) {
  return h("section", {},
    h("span.mata", {}, "Tantangan hari ini"),
    h("a.kartu", { href: tautanLangkah(t),
      gaya: { display: "flex", gap: "16px", alignItems: "center",
              color: "inherit" } },
      h("div", { gaya: { flex: "1" } },
        h("h3", {}, `${t.label_bahasa} — ${t.judul}`),
        h("div", { gaya: { color: "var(--redup)", fontSize: ".87rem",
                           marginTop: "4px" } },
          "Berganti tiap hari, dan selalu sama untuk hari yang sama.")),
      // Sengaja BUKAN .tbl-utama. Dasbor sudah punya satu permukaan amber
      // penuh — kartu Lanjutkan di atas — dan menambah yang kedua tidak
      // membuat dua hal penting, ia membuat nol. Tantangan harian adalah
      // tawaran, bukan langkah berikutnya yang disarankan.
      h("span.tbl", {}, "Kerjakan", ikon("lanjut", { ukuran: 17 }))));
}

function blokBahasa(daftar) {
  const petak = h("div.petak.petak-3", {}, daftar.map((b) => h("a.kartu.kartu-rapat", {
      href: "#/bahasa/" + b.key, gaya: { color: "inherit" },
    },
      h("div", { gaya: { display: "flex", justifyContent: "space-between",
                         alignItems: "baseline", marginBottom: "9px" } },
        h("b", { gaya: { fontSize: ".97rem" } }, b.label),
        h("span", { gaya: { fontFamily: "var(--f-kode)", fontSize: ".8rem",
          color: b.persen >= 100 ? "var(--tumbuh)" : "var(--redup)" } },
          bulat(b.persen) + "%")),
      bilah(b.persen, b.persen >= 100 ? "tumbuh" : ""),
      h("div", { gaya: { marginTop: "9px", fontSize: ".76rem",
                         color: "var(--redup)", fontFamily: "var(--f-kode)" } },
        `${b.materi}/${b.total_materi} materi · ${b.kuis}/${b.total_kuis} kuis`
        + ` · ${b.latihan_lulus + b.latihan_manual}/${b.total_latihan} latihan`),
      b.siap ? null
             : h("div.pil.pil-salah", { gaya: { marginTop: "9px" } },
                 "toolchain belum ada"))));
  ungkap(petak, { per: 30, maks: 240, geser: 10 });
  return h("section", {},
    h("span.mata", {}, "Progres per bahasa"),
    petak);
}

/* Berapa banyak bara yang boleh menyala satu per satu.
 *
 * Angka ini pernah tidak ada, dan akibatnya terukur: seluruh 186 sel
 * dianimasikan sekaligus, 207 animasi hidup dalam satu frame, dan frame
 * terburuk melar sampai 255 md — tersendat persis di saat yang seharusnya
 * paling menyenangkan dilihat. Membatasinya bukan cuma lebih ringan, tapi juga
 * lebih benar: yang menarik perhatian di hamparan ini adalah hari-hari yang
 * MENYALA, bukan ratusan kotak dingin yang ikut berkedip masuk. */
const BARA_MAKS_ANIMASI = 48;

/** Kisi masuk sebagai satu kesatuan; bara yang menyala menyusul satu per satu,
 *  dari hari ini mundur ke belakang. Yang sedang dijalani lebih berarti
 *  daripada yang sudah lewat enam bulan lalu, jadi ia yang muncul lebih dulu. */
function nyalakanBara(petak, menyala) {
  if (!adaGerak()) return;
  const bara = menyala.slice(-BARA_MAKS_ANIMASI);
  const delay = berurut(bara.length, { per: 12, maks: 340, dari: "akhir" });

  for (const el of bara) el.style.opacity = "0";

  // Pengamannya harus MEMATIKAN pemicunya, bukan cuma mengembalikan opacity.
  // Kalau tidak, kisi yang sudah telanjur terlihat akan dianimasikan masuk
  // dari nol begitu akhirnya tergulir ke layar — dan itu kedipan, bukan
  // animasi. Alasan lengkapnya ada di JAGA_MD, gerak.js.
  let menyerah = false;
  let hentikan = () => {};
  const jaga = setTimeout(() => {
    menyerah = true;
    hentikan();
    for (const el of bara) el.style.opacity = "";
  }, 2500);

  hentikan = saatTampak(petak, () => {
    if (menyerah) return;
    clearTimeout(jaga);
    masuk(petak, { geser: 6, zum: 1 });
    bara.forEach((el, i) => {
      el.style.opacity = "";
      animasi(el, { opacity: [0, 1], transform: ["scale(.35)", "none"] },
              { pegas: "jawab", delay: delay(i) });
    });
  }, { bagian: 0.15 });
}

function blokBara(d) {
  const target = Math.max(1, d.target_harian);
  const petak = h("div.bara-petak");
  const hariIni = new Date().toISOString().slice(0, 10);

  // Sisipkan sel kosong supaya kolom pertama jatuh di hari yang benar. Tanpa
  // ini seluruh kisi bergeser dan barisnya tidak lagi berarti "Senin".
  const pertama = d.heatmap[0];
  if (pertama) {
    const hari = (new Date(pertama.tanggal + "T00:00:00").getDay() + 6) % 7;
    for (let i = 0; i < hari; i++) {
      petak.appendChild(h("div", { gaya: { width: "12px", height: "12px" } }));
    }
  }
  const menyala = [];
  for (const s of d.heatmap) {
    const tingkat = s.xp <= 0 ? 0 : s.xp < target * 0.5 ? 1 : s.xp < target ? 2 : 3;
    const sel = h("div.bara-sel" + (tingkat ? ".bara-" + tingkat : "")
      + (s.tanggal === hariIni ? ".bara-kini" : ""),
      { title: `${tanggalRamah(s.tanggal)} — ${s.xp} XP` });
    if (tingkat) menyala.push(sel);
    petak.appendChild(sel);
  }
  nyalakanBara(petak, menyala);

  const aktif = d.heatmap.filter((s) => s.xp > 0).length;
  return h("section", {},
    h("span.mata", {}, "Bara — enam bulan terakhir"),
    h("div.kartu", {},
      petak,
      h("div.bara-legenda", {},
        h("span", {}, `${aktif} hari menyala dari ${d.heatmap.length}`),
        h("span", { gaya: { marginLeft: "auto" } }, "dingin"),
        h("div.bara-sel"), h("div.bara-sel.bara-1"),
        h("div.bara-sel.bara-2"), h("div.bara-sel.bara-3"),
        h("span", {}, "panas"))));
}

/* ================================================================ bahasa */

export async function layarBahasa({ key }, ctx) {
  const b = await api.ambil("/api/bahasa", { key });
  const s = b.statistik;

  const isi = h("div");
  const daftarTab = ["materi", "kuis", "latihan"];
  const kunciTab = "tab." + key;

  const tombolTab = daftarTab.map((t) => h("button.tbl.tbl-hantu", {
    onclick: () => pilih(t),
    data: { tab: t },
  }, ikon(ikonTipe(t), { ukuran: 17 }),
     `${t[0].toUpperCase()}${t.slice(1)}`,
     h("span.tab-jumlah", {}, String(b[t].length))));

  let tabKini = null;

  function pilih(t) {
    if (t === tabKini) return;
    const berganti = tabKini !== null;
    tabKini = t;
    ctx.ingat(kunciTab, t);
    for (const tb of tombolTab) {
      const ini = tb.dataset.tab === t;
      // .tbl-pilih, bukan .tbl-utama. Tab yang sedang terbuka adalah KEADAAN,
      // bukan tindakan yang disarankan — dan mewarnainya amber penuh membuat
      // ia bersaing dengan kartu Lanjutkan yang justru dimaksudkan untuk
      // ditekan.
      tb.classList.toggle("tbl-pilih", ini);
      tb.classList.toggle("tbl-hantu", !ini);
      tb.setAttribute("aria-pressed", String(ini));
    }
    const baru = t === "kuis" ? daftarKuis(b)
      : t === "latihan" ? daftarLatihan(b)
      : daftarMateri(b);

    // Berganti tab bukan berpindah halaman: daftarnya diganti di tempat, dan
    // gerakannya sengaja lebih pendek daripada pergantian layar supaya
    // perbedaan itu terbaca.
    isi.replaceChildren(baru);
    if (berganti) masuk(baru, { geser: 7, pegas: "jawab" });
  }

  const el = h("div.masuk", {},
    h("header.kepala-besar", {},
      h("span.mata", {}, "Bahasa"),
      h("h1", {}, b.label),
      h("p.kepala-sub", {}, kalimatBahasa(b, s)),
      barisFakta(b, s)),

    kartuLanjutBahasa(b, key),
    blokKemajuan(s),

    b.siap ? null : blokToolchain(b),
    b.catatan ? h("div.arti", {},
      h("b", {}, "Perlu diketahui"), h("div", {}, b.catatan)) : null,

    h("div.deret.tab-deret", {},
      tombolTab,
      // Dipisahkan dari tiga tab di sebelahnya, dan sengaja BUKAN .tbl-hantu:
      // dengan bentuk yang sama persis, ia terbaca sebagai "tab keempat yang
      // sedang tidak aktif" — padahal menekannya meninggalkan halaman ini.
      // Tab mengganti isi di bawahnya; ini pergi ke tempat lain, dan
      // perbedaan itu harus terlihat sebelum diklik.
      h("a.tbl.tbl-pergi.deret-kanan", { href: "#/coba?bahasa=" + b.runner },
        ikon("jalankan", { ukuran: 17 }), "Ruang coba " + b.label,
        ikon("lanjut", { ukuran: 15 }))),
    isi,
  );

  pilih(ctx.ingat(kunciTab) || "materi");
  return { el, judul: b.label, jejak: [{ label: b.label }] };
}

/** Satu kalimat yang menempatkan bahasa ini dalam gambar besar, sebelum angka
 *  apa pun muncul. Deretan "0/26 · 0/7 · 0/15" yang dulu berdiri di sini
 *  adalah jawaban atas pertanyaan yang belum ditanyakan siapa pun saat baru
 *  membuka sebuah halaman. */
function kalimatBahasa(b, s) {
  const total = s.total_materi + s.total_kuis + s.total_latihan;
  if (s.persen >= 100) {
    return `Semuanya sudah kamu selesaikan — ${total} bagian, tuntas.`;
  }
  if (s.persen <= 0) {
    return `Belum dimulai. Jalurnya ${s.total_materi} materi, diselingi `
      + `${s.total_kuis} kuis dan ${s.total_latihan} latihan.`;
  }
  return `Sudah ${bulat(s.persen)}% jalan. Lanjutkan dari tempat kamu berhenti.`;
}

/* Baris fakta di kepala halaman, dipinjam dari cara Codecademy membuka sebuah
   kursus: beberapa angka berikon yang menjawab "apa isinya, seberapa besar,
   dan apakah bisa dijalankan di komputerku" — sebelum ada satu pun daftar
   yang perlu dibaca. */
function barisFakta(b, s) {
  const fakta = [
    ["materi", `${s.total_materi} materi`],
    ["kuis", `${s.total_kuis} kuis`],
    ["latihan", `${s.total_latihan} latihan`],
    [b.siap ? "selesai" : "belum",
     b.siap ? "kode bisa dijalankan"
            : "butuh " + (b.hilang || []).join(", ")],
  ];
  return h("div.fakta", {}, fakta.map(([gambar, teks], i) =>
    h("div.fakta-butir" + (i === 3 && !b.siap ? ".fakta-kurang" : ""), {},
      ikon(gambar, { ukuran: 19 }), h("span", {}, teks))));
}

function blokKemajuan(s) {
  return h("div.kemajuan-baris", {},
    h("span", {}, "Kemajuan"),
    bilah(s.persen, s.persen >= 100 ? "tumbuh" : ""),
    h("b", {}, bulat(s.persen) + "%"));
}

/** Tindakan utama halaman bahasa: satu tautan menuju hal berikutnya.
 *
 *  Yang dipakai di sini hanya `status` yang SUDAH dikirim server — tidak ada
 *  satu pun keputusan "selesai" atau "lulus" yang dihitung ulang di browser.
 *  Aturan itu dipegang di seluruh antarmuka web (lihat AGENTS.md); yang
 *  dikerjakan fungsi ini murni memilih tautan mana yang paling masuk akal
 *  untuk ditawarkan lebih dulu. */
function kartuLanjutBahasa(b, key) {
  const materi = b.materi.find((m) => m.status !== "selesai");
  const kuis = b.kuis.find((q) => !q.pernah || q.jatuh_tempo);
  const latihan = b.latihan.find(
    (e) => e.status !== "lulus" && e.status !== "manual");

  let s = null;
  if (materi) {
    s = { tipe: "materi", indeks: materi.indeks, judul: materi.judul,
          mata: materi.status === "sebagian" ? "Lanjutkan bacaan"
                                             : "Mulai dari sini",
          ket: materi.status === "sebagian"
            ? "Kamu berhenti di tengah materi ini."
            : "Materi berikutnya yang belum dibaca." };
  } else if (kuis) {
    s = { tipe: "kuis", indeks: kuis.indeks, judul: kuis.judul,
          mata: "Uji pemahaman",
          ket: kuis.pernah ? "Sudah waktunya kuis ini diulang."
                           : "Semua materi terbaca — sekarang ujinya." };
  } else if (latihan) {
    s = { tipe: "latihan", indeks: latihan.indeks, judul: latihan.judul,
          mata: "Tulis kodenya",
          ket: "Bagian yang mengubah bacaan jadi kemampuan." };
  }

  if (!s) {
    return h("div.tuntas", {},
      ikon("selesai", { ukuran: 22 }),
      h("div", {},
        h("b", {}, "Tidak ada yang tersisa di sini."),
        h("span", {}, "Materi, kuis, dan latihannya sudah kamu selesaikan "
          + "semua. Kuisnya akan muncul lagi sendiri saat waktunya diulang.")));
  }

  return h("a.lanjutkan.lanjutkan-rapat",
    { href: `#/${s.tipe}/${key}/${s.indeks}` },
    h("div.lanjutkan-isi", {},
      h("span.mata", {}, s.mata),
      h("h2", {}, s.judul),
      h("p", {}, s.ket)),
    h("span.lanjutkan-tbl", {},
      h("span", {}, "Buka"), ikon("lanjut", { ukuran: 20 })));
}

function blokToolchain(b) {
  return h("div.kartu", { gaya: { marginBottom: "18px",
    borderColor: "color-mix(in srgb, var(--salah) 38%, transparent)" } },
    h("h3", { gaya: { color: "var(--salah)" } },
      `Kode ${b.label} belum bisa dijalankan di komputer ini`),
    h("p", { gaya: { marginTop: "8px", color: "var(--teks-2)" } },
      `Yang belum terpasang: ${b.hilang.join(", ")}. `
      + "Materi dan kuis tetap berjalan penuh; yang mati hanya penilaian "
      + "otomatis latihan — dan latihannya tetap bisa dikerjakan lalu "
      + "ditandai selesai sendiri."),
    b.pasang ? h("div.deret", {},
      h("div.pra", { gaya: { margin: "0", flex: "1", minWidth: "220px" } },
        b.pasang),
      h("button.tbl.tbl-kecil", {
        onclick: () => salin(b.pasang, "Perintah disalin. Tempel di terminal."),
      }, "Salin")) : null);
}

/* Ketiga daftar di bawah memakai ungkap(): isinya baru masuk saat benar-benar
   tergulir ke layar. Beberapa bahasa punya lebih dari dua puluh materi, dan
   menganimasikan dua puluh baris sekaligus — sebagian besar di luar layar —
   cuma memperpanjang urutannya tanpa ada yang melihat. Yang diungkap di
   daftar materi adalah BABnya, bukan barisnya; alasannya di bawah. */

/** Daftar materi, dikelompokkan per bab.
 *
 *  Senarai rata yang dipakai di sini sebelumnya menjawab "apa saja isinya",
 *  tapi tidak menjawab satu pun dari tiga pertanyaan yang sebenarnya dibawa
 *  orang ke halaman ini: mana yang harus lebih dulu, seberapa jauh lagi
 *  bagian yang sedang kukerjakan, dan apa yang menungguku sesudahnya. Bab
 *  menjawab ketiganya dengan satu kepala per kelompok.
 *
 *  Yang TIDAK dilakukan di sini: memutuskan sendiri sebuah bab terkunci atau
 *  tidak. Statusnya sudah jadi saat sampai — dihitung `bab.py` lalu dikirim
 *  server (lihat AGENTS.md: definisi kedua tentang "boleh dibuka" adalah cara
 *  tercepat membuat terminal dan web berbeda pendapat soal hal yang sama).
 *  Kode di bawah cuma menggambarnya. */
function daftarMateri(b) {
  const daftar = b.bab || [];
  const wadah = h("div", {},
    b.bab_kalimat || b.buka_semua_bab
      ? h("div.bab-ringkas", {},
          b.bab_kalimat ? h("p", {}, b.bab_kalimat) : null,
          // Saat saklarnya menyala, yang perlu dijawab halaman ini bukan
          // "kenapa bab ini terbuka" melainkan "kenapa TIDAK ADA yang
          // terkunci" — dan pertanyaan itu datang berbulan-bulan sesudah
          // saklarnya dipindahkan, ketika alasannya sudah lama lupa.
          // Tanpa baris ini, satu-satunya cara mengetahuinya adalah menebak.
          b.buka_semua_bab
            ? h("p.bab-bebas", {}, "Penguncian bab sedang dimatikan — semua "
                + "bab terbuka tanpa syarat. ",
                h("a", { href: "#/atur" }, "Ubah di Pengaturan"), ".")
            : null)
      : null);

  // Satu bab saja berarti tidak ada yang dikelompokkan: bahasa itu belum
  // punya pembagian bab, dan kepala "Semua materi" di atas seluruh daftarnya
  // cuma satu lapis tambahan yang tidak menjawab apa pun. Batas yang sama
  // dipakai bab.kalimat_ringkas(), yang juga diam kalau babnya cuma satu.
  if (daftar.length < 2) {
    wadah.appendChild(ungkapSenarai(
      h("div.senarai", {}, b.materi.map((m) => barisMateri(b, m)))));
    return wadah;
  }

  const materi = new Map(b.materi.map((m) => [m.indeks, m]));
  // Bab terkunci PERTAMA adalah satu-satunya pintu yang benar-benar dihadapi
  // orang sekarang; sisanya menunggu di belakangnya. Jalan pintas ke
  // Pengaturan ditempel di situ saja — tawaran yang sama persis diulang tiga
  // kali di satu layar berhenti terbaca sebagai tawaran, dan mulai terbaca
  // sebagai bujukan untuk melewati jalurnya.
  const pintu = daftar.find((x) => x.status === "terkunci");
  const sedang = daftar.find((x) => x.status === "terbuka");

  const petak = h("div.bab-daftar", {}, daftar.map((bab) => h(
    "section.bab"
      + (bab.status === "terkunci" ? ".bab-terkunci"
         : bab.status === "tuntas" ? ".bab-tuntas" : "")
      + (bab === sedang ? ".bab-kini" : ""),
    { "aria-label": `Bab ${bab.nomor}: ${bab.judul}` },
    kepalaBab(bab),
    bab.status === "terkunci" ? catatanKunci(bab, bab === pintu) : null,
    h("div.senarai", {}, bab.materi
      .map((i) => materi.get(i))
      .filter(Boolean)
      .map((m) => barisMateri(b, m))))));

  // Yang diungkap sekarang BAB-nya, bukan tiap barisnya. Sesudah
  // dikelompokkan, satuan yang berarti di halaman ini adalah bab — dan
  // mengungkapkan dua puluh baris satu per satu di dalam kepala bab yang
  // sudah berdiri duluan cuma memperpanjang urutannya tanpa menambah arti.
  ungkap(petak, { per: 40, maks: 240, geser: 9, pegas: "jawab" });
  wadah.appendChild(petak);
  return wadah;
}

/** Kepala satu bab: nomor, tingkat, judul, satu kalimat isi, dan kemajuan.
 *
 *  Tingkat memakai warnanya sendiri (sage → langit → ungu) dan sengaja BUKAN
 *  amber, walau tangga kesulitan latihan memakainya. Di halaman ini ada satu
 *  bab yang sedang dikerjakan, dan amber sudah dipakai untuk menandai bab itu;
 *  memberi warna yang sama kepada setiap pil "Menengah" berarti membuat
 *  penanda itu hilang di tengah keramaian. */
function kepalaBab(bab) {
  const tanda = bab.status === "tuntas" ? "selesai"
    : bab.status === "terkunci" ? "belum" : "sedang";
  return h("header.bab-kepala", {},
    ikon(tanda, { ukuran: 20, kelas: "bab-tanda" }),
    h("div.bab-teks", {},
      h("div.bab-atas", {},
        h("span.bab-nomor", {}, "Bab " + bab.nomor),
        h("span.pil.bab-tingkat.bab-" + bab.tingkat,
          { title: "Tingkat " + bab.label_tingkat.toLowerCase() },
          bab.label_tingkat),
        bab.status === "terkunci"
          ? h("span.pil.bab-cap", {}, "belum terbuka") : null,
        bab.status === "tuntas"
          ? h("span.pil.pil-tumbuh", {}, "tuntas") : null),
      h("h3.bab-judul", {}, bab.judul),
      bab.ket ? h("p.bab-ket", {}, bab.ket) : null),
    h("div.bab-maju", {},
      h("span.bab-angka", {}, `${bab.selesai}/${bab.jumlah} materi`),
      bilah(bab.persen, bab.status === "tuntas" ? "tumbuh" : "")));
}

/** Kenapa sebuah bab masih terkunci, dan — sekali saja — jalan keluarnya.
 *
 *  Kalimatnya datang utuh dari `bab.py`; ia sudah menyebut berapa materi lagi
 *  yang kurang dan di bab mana. Menyusun ulang kalimat itu di sini berarti
 *  aturan yang sama dijelaskan dengan dua cara berbeda di dua antarmuka. */
function catatanKunci(bab, tawarkanJalan) {
  return h("div.bab-kunci", {},
    h("span", {}, bab.alasan),
    tawarkanJalan
      ? h("a.bab-kunci-jalan", { href: "#/atur" },
          "Sudah pernah belajar bahasa ini? Buka semua bab di Pengaturan.")
      : null);
}

/** Satu baris materi. Yang terkunci tetap ditampilkan utuh — judulnya,
 *  nomornya, panjangnya — tapi bukan sebagai tautan.
 *
 *  Sengaja <div>, bukan <a> yang dimatikan lewat CSS: baris yang tidak bisa
 *  dibuka juga tidak boleh disinggahi Tab, dan pembaca layar tidak boleh
 *  mengumumkannya sebagai tautan. Menyembunyikannya sama sekali bukan
 *  pilihan — orang perlu tahu apa yang menantinya, dan itu justru seluruh
 *  alasan bab ini ada. */
function barisMateri(b, m) {
  const isi = [
    h("span.nomor", {}, String(m.indeks + 1)),
    h("span.titik" + (m.status === "selesai" ? ".selesai"
      : m.status === "sebagian" ? ".sedang" : ""), {}),
    h("div.isi", {},
      h("div.judul", {}, tanpaNomor(m.judul)),
      m.status === "sebagian"
        ? h("div.ket", {}, "berhenti di tengah — belum dihitung selesai") : null),
    m.bookmark ? h("span.pil.pil-nyala", {}, "ditandai") : null,
    h("span.sembunyi-hp", { gaya: { color: "var(--redup)", fontSize: ".76rem",
                                    fontFamily: "var(--f-kode)" } },
      `${m.bagian} bagian`),
  ];
  if (m.terkunci) return h("div.baris.baris-terkunci", {}, isi);
  return h("a.baris", {
    href: `#/materi/${b.key}/${m.indeks}`,
    kelas: m.status === "selesai" ? "selesai" : "",
  }, isi);
}

function ungkapSenarai(el) {
  ungkap(el, { per: 24, maks: 260, geser: 8, pegas: "jawab" });
  return el;
}

function daftarKuis(b) {
  return ungkapSenarai(h("div.senarai", {}, b.kuis.map((q) => {
    const persen = q.total_soal ? q.terbaik / q.total_soal * 100 : 0;
    const hari = selisihHari(q.jadwal);
    return h("a.baris", { href: `#/kuis/${b.key}/${q.indeks}` },
      h("span.nomor", {}, String(q.indeks + 1)),
      h("span.titik" + (q.pernah && q.terbaik === q.total_soal ? ".selesai"
        : q.pernah ? ".sedang" : ""), {}),
      h("div.isi", {},
        h("div.judul", {}, q.judul),
        h("div.ket", {}, q.pernah
          ? `Terbaik ${q.terbaik}/${q.total_soal} · ${q.percobaan}× dikerjakan`
            + (q.terakhir_waktu ? ` · terakhir ${jamRamah(q.terakhir_waktu)}` : "")
          : `${q.soal} soal · belum pernah dikerjakan`)),
      q.jatuh_tempo ? h("span.pil.pil-ungu", {}, "saatnya diulang")
        : (q.pernah && hari !== null && hari > 0
            ? h("span.pil.sembunyi-hp", {}, `ulang ${hari} hari lagi`) : null),
      q.salah_tersisa
        ? h("span.pil.pil-salah", {}, `${q.salah_tersisa} masih salah`) : null,
      q.pernah ? h("span.sembunyi-hp", { gaya: { width: "56px", flex: "none" } },
        bilah(persen, persen >= 100 ? "tumbuh" : "")) : null);
  })));
}

function daftarLatihan(b) {
  return ungkapSenarai(h("div.senarai", {}, b.latihan.map((e) => h("a.baris", {
    href: `#/latihan/${b.key}/${e.indeks}`,
    kelas: e.status === "lulus" || e.status === "manual" ? "selesai" : "",
  },
    h("span.nomor", {}, String(e.indeks + 1)),
    h("span.titik" + (e.status === "lulus" || e.status === "manual" ? ".selesai"
      : e.status === "dibuka" ? ".sedang" : ""), {}),
    h("div.isi", {},
      h("div.judul", {}, e.judul),
      e.status === "lulus" ? h("div.ket", {}, "lulus dengan kodemu sendiri")
        : e.status === "manual" ? h("div.ket", {}, "ditandai selesai manual")
        : !e.dinilai && e.alasan ? h("div.ket", {}, e.alasan) : null),
    h("span.pil.t-" + e.tingkat, {}, e.tingkat),
    !e.dinilai ? h("span.pil.sembunyi-hp", {}, "tanpa nilai otomatis") : null))));
}

/* ================================================================ materi */

export async function layarMateri({ key, indeks }, ctx) {
  // Dua permintaan sekaligus, bukan berurutan: daftar materi bahasa ini
  // dipakai untuk kolom kiri, dan menunggunya setelah materinya sendiri
  // selesai berarti membayar dua kali perjalanan untuk satu layar.
  //
  // allSettled, bukan all: materi yang babnya belum terbuka dijawab 403, dan
  // 403 di sini BUKAN kegagalan — ia jawaban yang punya layarnya sendiri.
  // Dengan Promise.all, penolakan yang pertama membuat permintaan bahasa yang
  // sudah telanjur jalan jadi penolakan tanpa penangkap, dan justru data
  // itulah yang dibutuhkan untuk menjelaskan apa yang sedang terkunci.
  const [jawabMateri, jawabBahasa] = await Promise.allSettled([
    api.ambil("/api/materi", { key, indeks }),
    api.ambil("/api/bahasa", { key }),
  ]);
  const b = jawabBahasa.status === "fulfilled" ? jawabBahasa.value : null;

  if (jawabMateri.status === "rejected") {
    const galat = jawabMateri.reason;
    // 403 juga dipakai untuk token yang sudah tidak sah (servernya dinyalakan
    // ulang sementara tab ini terbuka), dan pembedanya sederhana: penguncian
    // bab cuma berlaku untuk satu materi, jadi permintaan bahasanya pasti
    // tetap berhasil. Kalau KEDUANYA ditolak, yang tertutup bukan babnya
    // melainkan sesinya — dan itu punya penanganannya sendiri di inti.js.
    if (b && galat instanceof GalatApi && galat.kode === 403) {
      return layarMateriTerkunci(key, indeks, galat.message, b, ctx);
    }
    throw galat;
  }
  if (!b) throw jawabBahasa.reason;

  const m = jawabMateri.value;
  let status = m.status;

  // Dibuka tapi belum tuntas dicatat sebagai "sebagian" — tanpa XP. Aturannya
  // milik progress.py: materi dihitung selesai HANYA kalau dibaca sampai
  // habis, dan antarmuka ini tidak berhak melonggarkannya.
  if (status === "baru") {
    api.kirim("/api/materi/selesai", { key, indeks, tuntas: false }).catch(() => {});
    status = "sebagian";
  }

  const capSelesai = h("span.pil" + (status === "selesai" ? ".pil-tumbuh" : ""), {},
    status === "selesai" ? "sudah dibaca tuntas" : "belum tuntas");
  // Bukan .tbl-utama: di kaki halaman ia berdiri tepat di sebelah tombol
  // "materi berikutnya", dan dua tombol amber bersebelahan membuat keduanya
  // sama-sama tidak terbaca sebagai pilihan utama. Lagi pula tombol ini
  // hampir selalu sudah tidak perlu ditekan — membaca sampai bawah sudah
  // menandainya sendiri.
  const tblSelesai = h("button.tbl", { onclick: () => tandaiSelesai(false) },
    status === "selesai" ? "Sudah selesai ✓" : "Tandai selesai");

  async function tandaiSelesai(pindah) {
    if (status !== "selesai") {
      status = "selesai";
      capSelesai.textContent = "sudah dibaca tuntas";
      capSelesai.classList.add("pil-tumbuh");
      tblSelesai.textContent = "Sudah selesai ✓";
      rayakan(await api.kirim("/api/materi/selesai",
                              { key, indeks, tuntas: true }));
    }
    if (pindah && m.sesudah) location.hash = `#/materi/${key}/${m.indeks + 1}`;
    else await tawarkanPintuBaru();
  }

  /** Tawarkan materi berikutnya kalau bab yang memuatnya BARU SAJA terbuka.
   *
   *  Saat halaman ini digambar, tetangga di bab yang masih terkunci sengaja
   *  dikosongkan server — jadi materi terakhir sebuah bab datang tanpa tombol
   *  "berikutnya". Yang menuntaskan bab itu justru pembacaan halaman ini
   *  sendiri, dan tanpa langkah di bawah orang yang baru saja menyelesaikan
   *  sebuah bab berdiri di halaman yang satu-satunya jalannya ke BELAKANG,
   *  tepat pada momen yang seharusnya jadi hadiahnya.
   *
   *  Yang TIDAK dilakukan di sini: menyimpulkan sendiri bahwa babnya sudah
   *  terbuka. "Ini materi terakhir bab, berarti bab berikutnya terbuka" adalah
   *  definisi KEDUA tentang penguncian, dan begitu ada dua, terminal dan web
   *  akan berbeda pendapat tentang pintu yang sama (lihat AGENTS.md).
   *  Jawabannya ditanyakan ulang ke server dan cuma dibacakan. */
  // Penanda "sedang bertanya". Tanpa ini, pengamat yang menyalakan penandaan
  // tuntas dan tombol "Tandai selesai" yang ditekan sepersekian detik sesudahnya
  // sama-sama sampai ke sini sebelum jawaban pertama tiba -- dan kakinya dapat
  // DUA tombol yang menawarkan materi yang sama.
  let bertanya = false;

  async function tawarkanPintuBaru() {
    if (bertanya || m.sesudah || m.indeks + 1 >= m.jumlah
        || kaki.querySelector(".tbl-pintu")) {
      return;
    }
    bertanya = true;
    let baru;
    // Gagal bertanya = tidak menawarkan apa-apa. Tombol yang muncul karena
    // tebakan lebih buruk daripada tombol yang tidak muncul: yang pertama
    // mengantar ke layar "belum terbuka" sesudah menjanjikan kebalikannya.
    try {
      baru = await api.ambil("/api/bahasa", { key });
    } catch (e) {
      bertanya = false;
      return;
    }

    const lanjut = (baru.materi || []).find((x) => x.indeks === m.indeks + 1);
    if (!lanjut || lanjut.terkunci) {
      bertanya = false;      // masih terkunci: boleh ditanyakan lagi nanti
      return;
    }

    segarkanKunci(baru);
    const bb = (baru.bab || []).find((x) => (x.materi || []).includes(lanjut.indeks));
    const tbl = h("a.tbl.tbl-utama.tbl-pintu",
      { href: `#/materi/${key}/${lanjut.indeks}` },
      bb ? `Bab ${bb.nomor} terbuka: ${potong(tanpaNomor(lanjut.judul), 22)}`
         : potong(tanpaNomor(lanjut.judul), 26),
      ikon("lanjut", { ukuran: 17 }));
    kaki.appendChild(tbl);
    // masuk(), bukan animasi ber-fill: keadaan akhirnya keadaan alami tombol
    // itu, jadi gerak yang dimatikan berarti tombolnya langsung ada — bukan
    // hilang selamanya.
    masuk(tbl, { geser: 7, pegas: "jawab" });
  }

  /** Buka kunci butir-butir kolom kiri yang sudah tidak terkunci lagi.
   *
   *  Kolom itu digambar sekali, dari keadaan saat halaman dibuka. Membiarkannya
   *  berarti tombol di kaki halaman mengumumkan "Bab 3 terbuka" sementara
   *  seluruh Bab 3 di sebelahnya masih tertulis "terkunci" — dua jawaban
   *  berbeda untuk pertanyaan yang sama, di satu layar.
   *
   *  Digambar ulang di tempat, BUKAN dibangun ulang: `kolomMateri()` menggulir
   *  butir yang sedang dibaca ke tengah pandangan, dan menjalankannya lagi
   *  berarti merenggut posisi baca orang yang baru saja sampai di dasar
   *  halaman. */
  function segarkanKunci(baru) {
    for (const x of baru.materi || []) {
      const a = kolom.querySelector(`a[data-indeks="${x.indeks}"]`);
      if (!a || x.terkunci || !a.classList.contains("terkunci")) continue;
      a.classList.remove("terkunci");
      a.removeAttribute("title");
      a.href = `#/materi/${key}/${x.indeks}`;
    }
    for (const x of baru.bab || []) {
      const ang = kolom.querySelector(`[data-bab="${x.nomor}"] .materi-rel-bab-angka`);
      if (!ang || x.status === "terkunci") continue;
      ang.classList.remove("kunci");
      ang.textContent = `${x.selesai}/${x.jumlah}`;
    }
  }

  // Sampai di ujung halaman = benar-benar dibaca habis. Ini padanan web dari
  // paginasi terminal, yang juga hanya menandai tuntas kalau halaman
  // terakhirnya dilewati.
  const penanda = h("div", { gaya: { height: "1px" } });
  const pengamat = new IntersectionObserver((catatan) => {
    if (catatan.some((c) => c.isIntersecting) && status !== "selesai") {
      tandaiSelesai(false);
    }
  }, { rootMargin: "0px 0px -40px 0px" });

  const jumlahKode = m.bagian.filter((b) => b.jenis === "kode").length;

  const artikel = artikelMateri(m, key);
  const peta = petaBagian(m, artikel);
  // Dipegang di variabel, bukan ditulis langsung di dalam pohonnya: keduanya
  // masih berubah SESUDAH halaman jadi, saat materi ini ditandai tuntas dan
  // bab berikutnya ikut terbuka (lihat tawarkanPintuBaru()).
  const kolom = kolomMateri(m, b, key);
  const kaki = h("nav.materi-kaki", {},
    // `sebelum`/`sesudah` sengaja dikosongkan server kalau tetangganya
    // ada di bab yang masih terkunci. Memakai `m.indeks > 0` saja pernah
    // cukup; sekarang tidak lagi — tombol tanpa nama yang mengantar ke
    // 403 adalah cara paling membingungkan untuk memberi tahu bahwa
    // sesuatu belum boleh dibuka.
    m.indeks > 0 && m.sebelum
      ? h("a.tbl.tbl-hantu", { href: `#/materi/${key}/${m.indeks - 1}` },
          ikon("kembali", { ukuran: 17 }), potong(m.sebelum, 26))
      : h("a.tbl.tbl-hantu", { href: "#/bahasa/" + key },
          ikon("kembali", { ukuran: 17 }), "Daftar materi"),
    h("span.deret-kanan"),
    tblSelesai,
    m.sesudah
      ? h("button.tbl.tbl-utama", { onclick: () => tandaiSelesai(true) },
          potong(m.sesudah, 26), ikon("lanjut", { ukuran: 17 }))
      : null);

  const el = h("div.masuk.materi-tata", {},
    kolom,

    h("div.materi-utama", {},
      h("header.kepala-besar.kepala-materi", {},
        h("span.mata", {},
          `${m.label_bahasa} · materi ${m.indeks + 1} dari ${m.jumlah}`),
        h("h1", {}, m.judul),
        h("div.kepala-aksi", {},
          h("div.deret", {},
            capSelesai,
            h("span.pil", {}, ikon("bagian", { ukuran: 14, tebal: 1.9 }),
              `${m.bagian.length} bagian`),
            jumlahKode
              ? h("span.pil", {}, ikon("latihan", { ukuran: 14, tebal: 1.9 }),
                  `${jumlahKode} contoh kode`)
              : null,
            // Bab tempat halaman ini berdiri. Sedang membaca adalah keadaan
            // yang paling mudah membuat orang kehilangan gambar besarnya —
            // dan "Bab 2 · OOP" mengembalikannya dalam satu pil, tanpa harus
            // kembali ke daftar untuk memeriksanya.
            // Batas yang sama dipakai daftarMateri(), kolomMateri(), dan
            // bab.kalimat_ringkas(): satu bab berarti tidak ada yang
            // dikelompokkan, dan pil "Bab 1 · Semua materi" cuma menamai
            // seluruh kurikulum bahasa itu dengan kata yang tidak membedakan
            // apa pun.
            m.bab && (b.bab || []).length > 1
              ? h("span.pil.bab-tingkat.bab-" + m.bab.tingkat,
                  { title: `Tingkat ${m.bab.label_tingkat.toLowerCase()} · `
                    + `${m.bab.selesai} dari ${m.bab.jumlah} materi bab ini `
                    + "sudah dibaca tuntas" },
                  `Bab ${m.bab.nomor} · ${m.bab.judul}`)
              : null),
          h("div.deret", {},
            tombolBookmark(key, "materi", indeks, m.bookmark),
            tombolCatatan(m.kunci, m.catatan, m.judul)))),

      artikel,

      kaki,
      penanda),

    peta.el,
  );

  setTimeout(() => pengamat.observe(penanda), 80);

  return {
    el,
    judul: m.judul,
    jejak: [{ label: m.label_bahasa, href: "#/bahasa/" + key }, { label: m.judul }],
    saatKeluar: () => { pengamat.disconnect(); peta.bersihkan(); },
  };
}

/** Layar untuk alamat materi yang babnya belum terbuka (403 dari server).
 *
 *  Pesan error mentah di tengah layar gagal akan benar sekaligus tidak
 *  berguna: yang dibutuhkan orang yang baru saja menekan sebuah tautan bukan
 *  "Kesalahan 403" melainkan tiga hal — apa yang tadi diminta, kenapa belum
 *  boleh, dan ke mana sekarang. Ketiganya ada di layar ini, dan yang ketiga
 *  dibuat paling besar karena itulah satu-satunya yang bisa ditindaklanjuti.
 *
 *  Kalimat `pesan` datang utuh dari `bab.py` lewat server. Ia sudah menyebut
 *  berapa materi lagi yang kurang dan di bab mana; menulis ulang di sini
 *  berarti aturan yang sama dijelaskan dengan dua cara berbeda. */
function layarMateriTerkunci(key, indeks, pesan, b, ctx) {
  const nomor = Number(indeks);
  const label = b ? b.label : key;
  const m = b ? (b.materi || []).find((x) => x.indeks === nomor) : null;
  const bab = b ? (b.bab || []).find(
    (x) => (x.materi || []).includes(nomor)) : null;

  const el = h("div.masuk", {},
    h("header.kepala-besar", {},
      h("span.mata", {}, "Belum terbuka"),
      h("h1", {}, m ? tanpaNomor(m.judul) : "Materi ini belum terbuka"),
      // Kalimat aturannya datang dari server, bukan ditulis ulang di sini:
      // ia tinggal di bab.py bersama logika yang menegakkannya, jadi terminal
      // dan browser mustahil menjelaskan aturan yang sama dengan dua rumusan
      // berbeda.
      h("p.kepala-sub", {}, (ctx && ctx.awal && ctx.awal.aturan_bab
        ? ctx.awal.aturan_bab.aturan
        : "Bab ini belum terbuka."))),

    bab ? h("div.bab.bab-terkunci", {},
      kepalaBab(bab),
      h("div.bab-kunci", {}, h("span", {}, pesan))) : h("div.arti", {},
        h("b", {}, "Kenapa belum bisa dibuka"), h("div", {}, pesan)),

    h("div.deret", { gaya: { marginTop: "var(--s5)" } },
      h("a.tbl.tbl-utama", { href: "#/bahasa/" + key },
        ikon("kembali", { ukuran: 17 }), "Kembali ke " + label),
      h("a.tbl.tbl-hantu", { href: "#/atur" },
        "Buka semua bab di Pengaturan")));

  return {
    el,
    judul: "Belum terbuka",
    jejak: [{ label, href: "#/bahasa/" + key }, { label: "Belum terbuka" }],
  };
}

/** Kolom kiri: seluruh materi bahasa ini, dengan yang sedang dibuka disorot.
 *
 *  Ini pinjaman paling langsung dari The Odin Project, dan alasannya sama:
 *  saat sedang membaca, pertanyaan "ini bagian ke berapa dari berapa, dan apa
 *  sesudahnya" muncul terus-menerus. Menjawabnya lewat tombol Kembali berarti
 *  membuang tempat membaca untuk memeriksa peta.
 *
 *  Babnya ikut masuk sebagai sub-judul di antara butir-butirnya. Bentuknya
 *  satu daftar, bukan beberapa daftar bertumpuk, dan itu bukan soal rapi: di
 *  layar sempit kolom ini berubah jadi satu jalur yang digulir mendatar, dan
 *  memecahnya jadi empat jalur terpisah berarti empat penggulir kecil
 *  bertumpuk di atas bacaan — persis di tempat yang paling sedikit ruangnya. */
function kolomMateri(m, b, key) {
  // Peta nomor -> bab. Tiap materi cuma membawa nomor babnya, sedangkan yang
  // perlu digambar di sub-judul adalah judul, kemajuan, dan alasan kuncinya.
  const daftarBab = b.bab || [];
  const bab = new Map(daftarBab.map((x) => [x.nomor, x]));
  // Satu bab saja = tidak ada yang dikelompokkan; lihat daftarMateri().
  const berbab = daftarBab.length > 1;
  let babKini = null;

  const butir = [];
  for (const x of b.materi) {
    if (berbab && x.bab !== babKini) {
      babKini = x.bab;
      const bb = bab.get(babKini);
      if (bb) {
        const kunci = bb.status === "terkunci";
        // `data-bab` dan `data-indeks` di bawah bukan hiasan: keduanya jalan
        // yang dipakai layarMateri() untuk membuka kunci butir-butir di sini
        // begitu babnya terbuka, tanpa membangun ulang seluruh kolomnya.
        butir.push(h("li.materi-rel-bab", { data: { bab: String(bb.nomor) } },
          h("span.materi-rel-bab-judul", {}, `Bab ${bb.nomor} · ${bb.judul}`),
          // Angkanya ditandai berbeda saat babnya terkunci karena keduanya
          // tidak sama pentingnya: di layar sempit "3/7" boleh mengalah demi
          // judul yang utuh, sedangkan "terkunci" adalah satu-satunya
          // keterangan yang menjelaskan kenapa butir di bawahnya tidak bisa
          // ditekan. Yang menyembunyikannya ada di gaya.css.
          h("span.materi-rel-bab-angka" + (kunci ? ".kunci" : ""), {},
            kunci ? "terkunci" : `${bb.selesai}/${bb.jumlah}`)));
      }
    }

    const kini = x.indeks === m.indeks;
    // Yang terkunci tetap ditulis dengan bentuk yang sama persis — jalurnya
    // harus terbaca utuh — tapi TANPA href. <a> tanpa href bukan tautan bagi
    // siapa pun: tidak bisa diklik, tidak disinggahi Tab, dan tidak
    // diumumkan pembaca layar sebagai tautan.
    const a = h("a" + (kini ? ".kini" : "") + (x.terkunci ? ".terkunci" : ""), {
      data: { indeks: String(x.indeks) },
      href: x.terkunci ? null : `#/materi/${key}/${x.indeks}`,
      title: x.terkunci && bab.get(x.bab) ? bab.get(x.bab).alasan : null,
      "aria-current": kini ? "page" : null,
    },
      h("span.materi-rel-nomor", {}, String(x.indeks + 1)),
      h("span.materi-rel-judul", {}, tanpaNomor(x.judul)),
      x.status === "selesai"
        ? ikon("selesai", { ukuran: 16, kelas: "materi-rel-tanda" })
        : x.status === "sebagian"
          ? ikon("sedang", { ukuran: 16, kelas: "materi-rel-tanda" })
          : null);
    butir.push(h("li", {}, a));
  }

  const daftar = h("ol.materi-rel-daftar", {}, butir);

  const el = h("aside.materi-rel", {},
    h("a.materi-balik", { href: "#/bahasa/" + key },
      ikon("kembali", { ukuran: 17 }), b.label),
    h("div.mata", {}, `Materi · ${b.statistik.materi}/${b.statistik.total_materi}`),
    daftar);

  // Kolomnya menggulir sendiri dan tingginya dibatasi tinggi layar. Tanpa
  // baris ini, membuka materi ke-20 dari 26 menampilkan kolom yang tergulir di
  // paling atas — butir yang sedang dibaca ada di luar pandangan, dan yang
  // terlihat justru daftar materi yang sudah lama dilewati.
  requestAnimationFrame(() => {
    const kini = daftar.querySelector("a.kini");
    if (kini) kini.scrollIntoView({ block: "center", behavior: "auto" });
  });
  return el;
}

/** Kalimat pertama sebuah bagian prosa, dipendekkan jadi label peta. */
function kalimatPertama(bg) {
  const blok = (bg.blok || []).find(
    (x) => x.jenis !== "pra" && (x.teks || (x.butir && x.butir.length)));
  if (!blok) return "";
  const teks = String(blok.teks || (blok.butir && blok.butir[0]) || "").trim();
  if (!teks) return "";
  // Berhenti di tanda baca akhir kalimat pertama kalau ada; kalau tidak,
  // potong di batas kata supaya tidak ada kata yang terbelah.
  const titik = teks.search(/[.!?](\s|$)/);
  const awal = titik > 12 ? teks.slice(0, titik) : teks;
  return potong(awal.replace(/\s+/g, " "), 46);
}

/** Kolom kanan: peta bagian di halaman ini, dengan penanda yang mengikuti
 *  posisi baca.
 *
 *  Bedanya dengan daftar isi biasa: penandanya BERGERAK. Di materi sepanjang
 *  empat bagian itu mungkin berlebihan; di materi yang panjang, ia satu-satunya
 *  hal yang menjawab "aku sudah sampai mana" tanpa harus menggulir balik. */
function petaBagian(m, artikel) {
  // Sebagian besar bagian prosa di kurikulum ini tidak punya judul sendiri —
  // penulisnya memang menulis mengalir, bukan berjudul-judul. Peta yang cuma
  // memuat bagian berjudul jadi hampir selalu kosong dan tidak berguna.
  // Kalimat pertamanya dipakai sebagai gantinya: ia sudah ada, sudah ditulis
  // manusia, dan hampir selalu memang merangkum bagian itu.
  const butir = [];
  m.bagian.forEach((bg, i) => {
    let judul = bg.judul;
    if (!judul && bg.jenis === "kode") {
      judul = (bg.petunjuk && bg.petunjuk.nama) || "Contoh kode";
    }
    if (!judul && bg.jenis === "prosa") judul = kalimatPertama(bg);
    if (!judul) return;
    butir.push({ i, judul, jenis: bg.jenis });
  });

  if (butir.length < 2) {
    return { el: h("aside.materi-peta.materi-peta-kosong"), bersihkan() {} };
  }

  const tautan = butir.map((x) => h("a", {
    href: "#",
    onclick: (e) => {
      e.preventDefault();
      const sasaran = artikel.children[x.i];
      if (sasaran) {
        sasaran.scrollIntoView({
          behavior: adaGerak() ? "smooth" : "auto", block: "start" });
      }
    },
  },
    ikon(x.jenis === "kode" ? "latihan" : "bagian", { ukuran: 14, tebal: 1.9 }),
    h("span", {}, x.judul)));

  const el = h("aside.materi-peta", {},
    h("div.mata", {}, "Di halaman ini"),
    h("nav.materi-peta-daftar", {}, tautan));

  // Bagian yang sedang dibaca = bagian TERAKHIR yang tepinya sudah melewati
  // sepertiga atas layar. Aturan "yang paling banyak terlihat" terdengar lebih
  // benar tapi terasa gelisah: penandanya melompat bolak-balik tiap kali dua
  // bagian pendek bergantian mengisi layar.
  let hentikan = () => {};
  if (typeof IntersectionObserver !== "undefined") {
    const pengamat = new IntersectionObserver(() => {
      let aktif = -1;
      butir.forEach((x, n) => {
        const anak = artikel.children[x.i];
        if (anak && anak.getBoundingClientRect().top <= window.innerHeight * 0.34) {
          aktif = n;
        }
      });
      tautan.forEach((a, n) => a.classList.toggle("kini", n === aktif));
    }, { rootMargin: "-30% 0px -55% 0px", threshold: [0, 1] });

    for (const x of butir) {
      const anak = artikel.children[x.i];
      if (anak) pengamat.observe(anak);
    }
    hentikan = () => pengamat.disconnect();
  }
  return { el, bersihkan: hentikan };
}

/** Bagian-bagian materi muncul saat tergulir ke tempatnya.
 *
 *  Ini satu-satunya tempat di aplikasi yang gerakannya benar-benar mengikuti
 *  kecepatan MEMBACA, bukan kecepatan mengeklik. Jaraknya kecil dan urutannya
 *  pendek: yang dicari kesan halaman yang terbuka mengikuti mata, bukan
 *  pertunjukan yang menuntut ditonton sebelum boleh membaca. */
function artikelMateri(m, key) {
  const artikel = h("article.prosa", {},
    m.bagian.map((b, i) => bagianMateri(b, i, m, key)));
  ungkap(artikel, { per: 30, maks: 180, geser: 9, pegas: "halus" });
  return artikel;
}

function bagianMateri(b, i, m, key) {
  if (b.jenis === "prosa") {
    return h("section", {},
      b.judul ? h("h3", {}, b.judul) : null,
      b.blok.map((blk) => {
        if (blk.jenis === "pra") return h("div.pra", {}, blk.teks);
        if (blk.jenis === "daftar") {
          return h(blk.urut ? "ol" : "ul", {}, blk.butir.map((x) => h("li", {}, x)));
        }
        return h("div.par", {}, blk.teks);
      }));
  }
  return blokKode(b, i, m, key);
}

function blokKode(b, i, m, key) {
  const p = b.petunjuk;
  const lencana = {
    program: "berkas utuh", potongan: "potongan", sesi: "sesi",
    multi: "beberapa berkas", ilustrasi: "ilustrasi",
  }[p.jenis] || p.jenis;

  return h("div.blok-kode", {},
    h("div.blok-kepala", {},
      p.nama ? h("span.berkas", {}, p.nama)
             : h("span", {}, b.judul || p.instruksi),
      h("span.lencana", {}, lencana),
      h("div.blok-alat", {},
        p.bisa_dijalankan ? h("button.tbl.tbl-kecil.tbl-hantu", {
          title: "Buka di ruang coba lalu jalankan",
          onclick: () => {
            location.hash = `#/coba?key=${key}&materi=${m.indeks}&bagian=${i}`;
          },
        }, "Coba jalankan") : null,
        h("button.tbl.tbl-kecil.tbl-hantu", {
          onclick: (e) => salin(b.kode, "Kode disalin.", e.currentTarget),
        }, "Salin"))),
    praKode(b.token),
    p.perintah.length
      ? h("div.blok-kaki", {}, "Jalankan: ",
          h("span.perintah", {}, p.perintah.join("   lalu   ")))
      : p.keterangan ? h("div.blok-kaki", {}, p.keterangan)
      : (p.instruksi && !p.nama) ? h("div.blok-kaki", {}, p.instruksi) : null);
}

/* ========================================================= bagian bersama */

export function tombolBookmark(key, tipe, indeks, aktif) {
  const tbl = h("button.tbl.tbl-hantu", {
    title: "Simpan ke bookmark",
    onclick: async () => {
      const r = await api.kirim("/api/bookmark", { key, tipe, indeks });
      tbl.textContent = r.bookmark ? "★ Ditandai" : "☆ Tandai";
      tbl.classList.toggle("tbl-pilih", r.bookmark);
      tbl.classList.toggle("tbl-hantu", !r.bookmark);
      // Hanya saat DITANDAI. Melepas tanda tidak dirayakan — perayaan untuk
      // membatalkan sesuatu membingungkan, bukan menyenangkan.
      if (r.bookmark) { denyut(tbl); percikBara(tbl, { jumlah: 6 }); }
      sorak(r.bookmark ? "Masuk bookmark." : "Dihapus dari bookmark.", "", 1.8);
    },
  }, aktif ? "★ Ditandai" : "☆ Tandai");
  // .tbl-pilih, bukan .tbl-utama: "sudah ditandai" adalah KEADAAN, dan
  // mewarnainya amber penuh membuatnya bersaing dengan tindakan yang benar-
  // benar disarankan di halaman itu. Aturan yang sama dipakai untuk tab.
  if (aktif) { tbl.classList.add("tbl-pilih"); tbl.classList.remove("tbl-hantu"); }
  return tbl;
}

export function tombolCatatan(kunci, catatan, judul) {
  const ada = Boolean(catatan && catatan.teks);
  const tbl = h("button.tbl.tbl-hantu", {
    title: "Catatan pribadimu untuk halaman ini",
    onclick: () => bukaCatatan(kunci, judul, tbl),
  }, ada ? "✎ Catatan tersimpan" : "✎ Catatan");
  if (ada) { tbl.classList.add("tbl-pilih"); tbl.classList.remove("tbl-hantu"); }
  return tbl;
}

export async function bukaCatatan(kunci, judul, tbl) {
  const kini = await api.ambil("/api/catatan", { kunci });
  const area = h("textarea", {
    "aria-label": "Catatan pribadimu untuk " + judul,
    value: kini.teks || "",
    placeholder: "Tulis dengan kalimatmu sendiri: apa inti halaman ini, dan "
      + "bagian mana yang tadi sempat membingungkan.",
    gaya: { minHeight: "220px" },
  });

  const pilih = await jendela({
    judul: "Catatan — " + judul,
    isi: h("div", {},
      h("p", { gaya: { color: "var(--redup)", fontSize: ".86rem" } },
        "Menuliskan ulang dengan bahasa sendiri adalah cara paling murah "
        + "untuk tahu apakah kamu benar-benar paham."),
      area,
      kini.diubah ? h("div", { gaya: { marginTop: "8px", color: "var(--redup)",
                                       fontSize: ".8rem" } },
        "Terakhir diubah " + jamRamah(kini.diubah)) : null),
    aksi: [{ label: "Batal", nilai: false },
           { label: "Simpan", nilai: true, kelas: "tbl-utama" }],
  });
  if (pilih !== true) return null;

  const hasil = await api.kirim("/api/catatan", { kunci, teks: area.value });
  if (tbl) {
    const ada = Boolean(hasil.teks);
    tbl.textContent = ada ? "✎ Catatan tersimpan" : "✎ Catatan";
    tbl.classList.toggle("tbl-pilih", ada);
    tbl.classList.toggle("tbl-hantu", !ada);
  }
  sorak(hasil.teks ? "Catatan disimpan." : "Catatan dikosongkan.", "tumbuh", 2);
  return hasil;
}

/* ============================================================== bookmark */

export async function layarBookmark() {
  const isi = h("div");

  async function segarkan() {
    const b = await api.ambil("/api/bookmark");
    isi.replaceChildren(
      b.daftar.length
        ? ungkapSenarai(h("div.senarai", {}, b.daftar.map((x) => h("a.baris", {
            href: `#/${x.tipe}/${x.bahasa}/${x.indeks}`,
          },
            pilJenis(x.tipe),
            h("div.isi", {},
              h("div.judul", {}, x.judul),
              h("div.ket", {}, x.label_bahasa))))))
        : kosong("Belum ada bookmark",
            "Tekan ☆ Tandai di halaman materi, kuis, atau latihan mana pun."),
      b.basi ? h("div.deret", { gaya: { marginTop: "16px" } },
        h("span", { gaya: { color: "var(--redup)", fontSize: ".87rem" } },
          `${b.basi} bookmark menunjuk halaman yang sudah tidak ada.`),
        h("button.tbl.tbl-kecil", { onclick: async () => {
          const r = await api.kirim("/api/bookmark/bersihkan", {});
          sorak(`${r.dibuang} bookmark basi dibuang.`, "tumbuh");
          segarkan();
        } }, "Bersihkan")) : null);
  }
  await segarkan();

  return {
    el: h("div.masuk", {},
      h("header.kepala-besar", {},
        h("span.mata", {}, "Tersimpan"),
        h("h1", {}, "Bookmark"),
        h("p.kepala-sub", {}, "Halaman yang kamu tandai untuk dibuka lagi.")),
      isi),
    judul: "Bookmark",
    jejak: [{ label: "Bookmark" }],
  };
}

/* =============================================================== catatan */

export async function layarCatatan() {
  const isi = h("div");

  async function segarkan() {
    const c = await api.ambil("/api/catatan/semua");
    isi.replaceChildren(
      h("p.sub", { gaya: { color: "var(--redup)", marginBottom: "18px" } },
        `${c.daftar.length} catatan. Disimpan terpisah dari progres, jadi `
        + "menghapus progres tidak ikut menghapus tulisanmu."),
      c.daftar.length
        ? h("div.senarai", {}, c.daftar.map((x) => h("div.kartu", {},
            h("div.deret", { gaya: { marginBottom: "9px" } },
              x.basi ? h("span.pil.pil-salah", {}, "halaman sudah tidak ada")
                     : h("a.pil" + pilTipe(x.tipe),
                         { href: `#/${x.tipe}/${x.bahasa}/${x.indeks}` },
                         `${x.label_bahasa} · ${x.judul}`),
              h("span.deret-kanan", { gaya: { color: "var(--redup)",
                                              fontSize: ".78rem" } },
                jamRamah(x.diubah)),
              h("button.tbl.tbl-kecil.tbl-hantu", {
                onclick: async () => {
                  if (await bukaCatatan(x.kunci, x.judul)) segarkan();
                },
              }, "Ubah")),
            h("div.par", { gaya: { margin: "0", color: "var(--teks-2)" } },
              x.teks))))
        : kosong("Belum ada catatan",
            "Buka materi mana pun, lalu tekan ✎ Catatan."));
  }
  await segarkan();

  return {
    el: h("div.masuk", {},
      h("header.kepala-besar", {},
        h("span.mata", {}, "Milikmu sendiri"),
        h("h1", {}, "Catatanku"),
        h("p.kepala-sub", {}, "Menuliskan ulang dengan bahasamu sendiri "
          + "adalah cara paling murah untuk tahu apakah kamu benar-benar "
          + "paham.")),
      isi),
    judul: "Catatanku",
    jejak: [{ label: "Catatanku" }],
  };
}

/* ================================================================== cari */

export async function layarCari({ q, tipe }) {
  const kata = q || "";
  const saring = tipe || "semua";
  const hasil = kata.length >= 2
    ? (await api.ambil("/api/cari", { q: kata, tipe: saring })).hasil : [];

  const medan = h("input", {
    type: "text", value: kata, placeholder: "Cari di 11 bahasa sekaligus…",
    "aria-label": "Kata yang dicari",
    gaya: { fontSize: "1.05rem", padding: "13px 17px" },
  });
  medan.addEventListener("keydown", (e) => {
    if (e.key === "Enter") ganti(medan.value, saring);
  });

  function ganti(k, t) {
    location.hash = "#/cari?q=" + encodeURIComponent(k)
      + (t !== "semua" ? "&tipe=" + t : "");
  }

  const el = h("div.masuk", {},
    h("header.kepala-besar", {},
      h("span.mata", {}, "Pencarian"),
      h("h1", {}, "Cari"),
      h("p.kepala-sub", {}, "Menjangkau judul, isi materi, soal kuis, dan "
        + "solusi latihan di sebelas bahasa sekaligus.")),
    medan,
    h("div.deret", { gaya: { margin: "14px 0 20px" } },
      ["semua", "materi", "kuis", "latihan"].map((t) =>
        h("button.tbl.tbl-kecil" + (t === saring ? ".tbl-utama" : ".tbl-hantu"),
          { onclick: () => ganti(medan.value, t) },
          t[0].toUpperCase() + t.slice(1)))),

    kata.length < 2
      ? kosong("Ketik minimal dua huruf",
          "Coba: pointer, rekursi, JOIN, closure, malloc, interface.")
      : hasil.length
        ? h("div", {},
            h("div", { gaya: { color: "var(--redup)", fontSize: ".87rem",
                               marginBottom: "12px" } },
              `${hasil.length} hasil untuk "${kata}"`),
            // Penanda "terkunci" dipasang SEBELUM diklik, bukan sesudah.
            // Tautannya sengaja tetap hidup: menekannya mendarat di layar yang
            // menjelaskan apa yang kurang, dan itu jawaban yang lebih berguna
            // daripada baris yang tidak bisa ditekan sama sekali. Yang tidak
            // boleh terjadi cuma satu — orang mengklik tanpa satu pun isyarat
            // lebih dulu.
            ungkapSenarai(h("div.senarai", {}, hasil.map((r) => h("a.baris", {
              href: `#/${r.tipe}/${r.bahasa}/${r.indeks}`,
            },
              pilJenis(r.tipe),
              h("div.isi", {},
                h("div.judul", {}, tandai(r.judul, kata)),
                h("div.ket", {}, r.label_bahasa,
                  r.cuplikan ? " — " : "",
                  r.cuplikan ? tandai(r.cuplikan, kata) : "")),
              r.terkunci ? h("span.pil.pil-kunci", {}, "terkunci") : null)))))
        : kosong(`Tidak ada yang cocok dengan "${kata}"`,
            "Coba kata yang lebih pendek, atau matikan saringan tipe."),
  );

  setTimeout(() => {
    medan.focus();
    medan.setSelectionRange(medan.value.length, medan.value.length);
  }, 40);
  return { el, judul: "Cari", jejak: [{ label: "Cari" }] };
}
