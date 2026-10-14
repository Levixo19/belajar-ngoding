/* Layar Pustaka: ribuan tautan belajar dari repo kurasi, bisa dicari dan
 * disaring per kurikulum, jenis, bahasa, dan sumber.
 *
 * Semua keputusan isi datang dari server (inti/pustaka.py lewat
 * /api/pustaka): urutan, cacah tiap penyaring, dan label-labelnya. Layar ini
 * cuma menggambar. Terminal memanggil fungsi inti yang sama, jadi kedua
 * antarmuka menampilkan tautan yang sama dalam urutan yang sama.
 *
 * Keadaan penyaring tinggal di ALAMAT (#/pustaka?kurikulum=python&jenis=buku),
 * bukan di memori layar. Dengan begitu tautan "Lihat semua bacaan Python" dari
 * halaman bahasa, tombol mundur browser, dan tab yang dibuka ulang semuanya
 * mendarat di saringan yang sama.
 *
 * Tautan keluar dibuka di tab baru dengan rel="noopener noreferrer": halaman
 * di luar sana tidak boleh bisa menyentuh jendela aplikasi ini lewat
 * window.opener, dan alamat lokal aplikasi tidak perlu ikut terkirim.
 *
 * Importir: aplikasi.js, layar-belajar.js.
 */

import { api, h, isikan, kosong, tandai, angka } from "./inti.js";
import { ikon } from "./ikon.js";
import { kepalaBersampul } from "./sampul.js";

const PENYARING = ["q", "kurikulum", "jenis", "bahasa", "sumber"];

function alamat(saring) {
  const q = new URLSearchParams();
  for (const k of PENYARING) if (saring[k]) q.set(k, saring[k]);
  const s = q.toString();
  return "#/pustaka" + (s ? "?" + s : "");
}

/** Satu baris tautan. Dipakai juga oleh tab Bacaan di halaman bahasa. */
export function barisTautan(e, labelJenis, kata) {
  const bagianKet = [
    e.catatan || null,
    e.topik && e.topik.length ? e.topik[0] : null,
  ].filter(Boolean).join(" · ");
  return h("a.baris", {
    href: e.url, target: "_blank", rel: "noopener noreferrer", title: e.url,
  },
    h("span.pil.pil-jenis", {}, labelJenis[e.jenis] || e.jenis),
    h("div.isi", {},
      h("div.judul", {}, kata ? tandai(e.judul, kata) : e.judul),
      bagianKet
        ? h("div.ket", {}, kata ? tandai(bagianKet, kata) : bagianKet)
        : null),
    e.bahasa === "id" ? h("span.pil.pil-tumbuh", {}, "Indonesia") : null,
    h("span.baris-panah", { "aria-hidden": "true" }, ikon("lanjut", { ukuran: 16 })));
}

/** Deret tombol pilihan untuk satu penyaring. Nilai bercacah nol tidak
 *  ditampilkan: tombol yang berujung "tidak ada hasil" adalah tombol yang
 *  berujung penolakan. */
function deretPilihan(nama, nilaiKini, segi, label, ganti) {
  const urutan = Object.keys(label).filter((k) => segi[k]);
  if (urutan.length < 2 && !nilaiKini) return null;
  const tombol = (nilai, teks, jumlah) => {
    const aktif = (nilai || "") === (nilaiKini || "");
    return h("button.tbl.tbl-kecil" + (aktif ? ".tbl-pilih" : ".tbl-hantu"), {
      type: "button", "aria-pressed": String(aktif),
      onclick: () => ganti({ [nama]: nilai }),
    }, teks, jumlah !== null ? h("span.tab-jumlah", {}, angka(jumlah)) : null);
  };
  return h("div.deret.deret-rapat", {
    role: "group", "aria-label": "Saring " + nama,
    gaya: { marginBottom: "var(--s3)" },
  },
    tombol("", "Semua", null),
    urutan.map((k) => tombol(k, label[k], segi[k])));
}

function pilihan(nama, nilaiKini, segi, label, teksSemua, ganti) {
  // Lebar dipatok di sini, bukan di gaya.css: `select` bawaan aplikasi ini
  // selebar wadahnya, dan dua pilihan yang masing-masing merentang 1000 px
  // mendorong daftar tautan satu layar ke bawah.
  const el = h("select", { "aria-label": teksSemua,
                           gaya: { width: "auto", flex: "0 1 15rem", minWidth: "0" } },
    h("option", { value: "" }, teksSemua),
    Object.keys(label).filter((k) => segi[k] || k === nilaiKini).map((k) =>
      h("option", { value: k, selected: k === nilaiKini },
        `${label[k]} (${angka(segi[k] || 0)})`)));
  el.addEventListener("change", () => ganti({ [nama]: el.value }));
  return el;
}

export async function layarPustaka(params) {
  const saring = {};
  for (const k of PENYARING) saring[k] = params[k] || "";
  const kirim = {};
  for (const k of PENYARING) if (saring[k]) kirim[k] = saring[k];
  const data = await api.ambil("/api/pustaka", kirim);
  const label = data.label;
  label.sumber = Object.fromEntries(data.sumber.map((s) => [s.kunci, s.nama]));
  const kata = saring.q.trim();

  const ganti = (ubah) => { location.hash = alamat({ ...saring, ...ubah }); };

  const medan = h("input", {
    // type "text", bukan "search": gaya medan isian aplikasi ini menyasar
    // input[type="text"], dan "search" tampil sebagai kotak polos browser.
    type: "text", enterkeyhint: "search", value: saring.q,
    placeholder: `Cari di ${angka(data.semua)} tautan: judul, topik, penulis…`,
    "aria-label": "Cari di Pustaka",
    gaya: { fontSize: "var(--t-baca)", flex: "1 1 18rem", minWidth: "0" },
  });
  medan.addEventListener("keydown", (e) => {
    if (e.key === "Enter") ganti({ q: medan.value.trim() });
  });

  const senarai = h("div.senarai", {},
    data.hasil.map((e) => barisTautan(e, label.jenis, kata)));

  let halaman = data.halaman;
  const tersisa = () => data.total - halaman * data.per_halaman;
  const tblLagi = h("button.tbl.tbl-hantu", { type: "button" });
  const segarkanLagi = () => {
    const sisa = tersisa();
    tblLagi.hidden = sisa <= 0;
    isikan(tblLagi, `Tampilkan ${angka(Math.min(sisa, data.per_halaman))} lagi`,
           h("span.tab-jumlah", {}, `sisa ${angka(Math.max(sisa, 0))}`));
  };
  tblLagi.addEventListener("click", async () => {
    tblLagi.disabled = true;
    try {
      const lanjut = await api.ambil("/api/pustaka", { ...kirim, hal: halaman + 1 });
      halaman = lanjut.halaman;
      for (const e of lanjut.hasil) senarai.append(barisTautan(e, label.jenis, kata));
    } finally {
      tblLagi.disabled = false;
      segarkanLagi();
    }
  });
  segarkanLagi();

  const adaSaringan = PENYARING.some((k) => saring[k]);
  const ringkas = data.total === data.semua
    ? `${angka(data.total)} tautan dari ${data.sumber.length} sumber.`
    : `${angka(data.total)} dari ${angka(data.semua)} tautan cocok.`;

  const el = h("div.masuk", {},
    kepalaBersampul("pustaka", { ragam: "kisi" },
      h("span.mata", {}, "Pustaka"),
      h("h1", {}, "Bacaan, kursus, dan proyek"),
      h("p.kepala-sub", {},
        "Buku, kursus, tutorial, proyek praktik, peta belajar, dan API publik "
        + "dari repo kurasi terbuka. Yang berbahasa Indonesia selalu tampil "
        + "lebih dulu. Semua tautan dibuka di tab baru.")),

    h("div.deret", { gaya: { marginBottom: "var(--s4)" } },
      medan,
      h("button.tbl.tbl-utama", {
        type: "button", onclick: () => ganti({ q: medan.value.trim() }),
      }, ikon("cari", { ukuran: 16 }), "Cari"),
      pilihan("kurikulum", saring.kurikulum, data.segi.kurikulum,
              label.kurikulum, "Semua kurikulum", ganti),
      pilihan("sumber", saring.sumber, data.segi.sumber,
              label.sumber, "Semua sumber", ganti)),

    deretPilihan("jenis", saring.jenis, data.segi.jenis, label.jenis, ganti),
    deretPilihan("bahasa", saring.bahasa, data.segi.bahasa, label.bahasa, ganti),

    h("div.baris-sisi", { gaya: { margin: "var(--s3) 0" } },
      ringkas,
      adaSaringan
        ? h("a", { href: "#/pustaka", gaya: { marginLeft: "var(--s3)" } },
            "Hapus semua saringan")
        : null),

    data.total
      ? h("div", {}, senarai,
          h("div.deret", { gaya: { marginTop: "var(--s4)" } }, tblLagi))
      : kosong(kata ? `Tidak ada yang cocok dengan "${kata}"` : "Tidak ada tautan",
          "Coba kata yang lebih pendek, atau hapus salah satu saringan."),

    blokSumber(data.sumber),
  );

  if (!("ontouchstart" in window)) setTimeout(() => medan.focus(), 40);
  // Judul tab membawa saringan kurikulumnya: dua tab "Pustaka" yang isinya
  // berbeda tidak bisa dibedakan di baris tab.
  const judul = saring.kurikulum && label.kurikulum[saring.kurikulum]
    ? "Pustaka " + label.kurikulum[saring.kurikulum] : "Pustaka";
  return { el, judul };
}

/** Lisensi dan atribusi tiap sumber. Ini bukan hiasan: CC BY dan MIT
 *  mewajibkannya, dan pelajar berhak tahu dari mana tautan ini berasal. */
function blokSumber(sumber) {
  return h("details.bantuan-isi", { gaya: { marginTop: "var(--s7)" } },
    h("summary", {}, "Sumber dan lisensi"),
    h("div.senarai", {}, sumber.map((s) => h(s.repo ? "a.baris" : "div.baris", {
      href: s.repo || null, target: s.repo ? "_blank" : null,
      rel: s.repo ? "noopener noreferrer" : null,
    },
      h("span.pil", {}, s.lisensi),
      h("div.isi", {},
        h("div.judul", {}, `${s.nama} · ${angka(s.jumlah)} tautan`),
        h("div.ket", {}, s.atribusi
          + (s.commit ? ` Dipanen dari commit ${s.commit}.` : ""))),
      s.repo ? h("span.baris-panah", { "aria-hidden": "true" },
                 ikon("lanjut", { ukuran: 16 })) : null))));
}
