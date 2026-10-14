/* Beranda (dasbor berjalan): bagian-bagian baru dan gerak gulirnya.
 *
 * Susunannya dari arahan gpt-taste (undian deterministik, 2026-10-14):
 * hero Editorial Split, bento tanpa celah, kalimat yang menyala kata demi
 * kata saat digulir, akordeon horizontal untuk bahasa yang sedang dijalani,
 * dan marquee pelan berisi seluruh kurikulum.
 *
 * Semua ANGKA datang dari /api/dasbor. Tidak ada persen, XP, atau status yang
 * dihitung di sini; modul ini cuma merangkai kalimat dan bentuk.
 *
 * GERAK. Satu-satunya yang memutuskan boleh bergerak atau tidak adalah
 * gerakPenuh() dari gerak.js (prefers-reduced-motion selalu menang di sana).
 * Setiap animasi berangkat DARI tempat lain MENUJU keadaan alami elemennya,
 * jadi kalau GSAP gagal dimuat, gerak dimatikan, atau pemicu gulir tidak
 * pernah menyala, isinya tetap terlihat utuh. gerakBeranda() WAJIB dipanggil
 * sesudah layar menempel (lewat saatSiap di pemanggilnya): ScrollTrigger
 * mengukur posisi saat dibuat. Pembersih yang dikembalikannya membunuh semua
 * pemicu saat layar ditinggal.
 *
 * Importir: layar-belajar.js.
 */

import { h } from "./inti.js";
import { ikon } from "./ikon.js";
import { gerakPenuh } from "./gerak.js";
import { sampul } from "./sampul.js";

/** Kalimat ringkas perjalanan pelajar. Hanya merangkai angka dari server. */
export function kalimatGulir(d) {
  const aktif = d.bahasa.filter((b) => b.materi > 0);
  const materi = aktif.reduce((n, b) => n + b.materi, 0);
  const bagian = [
    `Sejauh ini kamu sudah menuntaskan ${materi} materi`,
    aktif.length > 1 ? `di ${aktif.length} bahasa` : aktif.length ? `di ${aktif[0].label}` : "",
    `dan mengumpulkan ${d.xp} XP.`,
    "Setiap materi yang selesai membuka bab berikutnya,",
    "setiap kuis yang diulang membuatnya menempel lebih lama,",
    "dan setiap latihan yang lulus adalah kode yang benar-benar jalan.",
  ].filter(Boolean);
  return h("section.beranda-kalimat", { "aria-label": "Ringkasan perjalanan" },
    h("p.beranda-kalimat-isi", {}, bagian.join(" ")));
}

/** Akordeon horizontal: satu irisan per bahasa yang sedang dijalani. Irisan
 *  yang disorot atau difokus melebar; lebarnya digerakkan CSS lewat
 *  flex-grow saja (satu properti, satu mesin). */
export function akordeonBahasa(daftar) {
  if (!daftar.length) return null;
  return h("section.beranda-akordeon-bagian", { "aria-label": "Bahasa yang sedang kamu jalani" },
    h("h2.beranda-judul-bagian", {}, "Yang sedang kamu jalani"),
    h("div.akordeon", {}, daftar.map((b, i) => h("a.akordeon-iris", {
      href: "#/bahasa/" + b.key,
    },
      h("span.akordeon-sampul", {}, sampul(b.key, { bahasa: b.key, lebar: 720, tinggi: 320 })),
      h("span.akordeon-nomor", {}, String(i + 1).padStart(2, "0")),
      h("span.akordeon-nama", {}, b.label),
      h("span.akordeon-isi", {},
        h("b.akordeon-persen", {}, `${Math.round(b.persen)}%`),
        h("span", {}, `${b.materi} dari ${b.total_materi} materi`),
        h("span.akordeon-bilah", {}, h("i", { gaya: { width: `${Math.min(100, b.persen)}%` } })),
        h("span.akordeon-pergi", {}, "Buka", ikon("lanjut", { ukuran: 16 })))))));
}

/** Marquee seluruh kurikulum. Isinya digandakan sekali (salinannya
 *  aria-hidden dan tak terjangkau Tab) supaya putarannya mulus; animasinya
 *  CSS murni, jadi aturan gerak global di kaki gaya.css mematikannya. */
export function marqueeBahasa(bahasa) {
  const baris = (sembunyi) => h("div.marquee-baris", sembunyi ? { "aria-hidden": "true" } : {},
    bahasa.map((b) => h("a.marquee-butir", {
      href: "#/bahasa/" + b.key, tabindex: sembunyi ? "-1" : null,
    }, b.label)));
  return h("section.marquee", { "aria-label": "Semua kurikulum" },
    h("div.marquee-jalur", {}, baris(false), baris(true)));
}

/** Pasang gerak gulir beranda. Mengembalikan pembersih. */
export function gerakBeranda(akar) {
  const g = window.gsap;
  const ST = window.ScrollTrigger;
  if (!g || !ST || !gerakPenuh()) return () => {};
  g.registerPlugin(ST);
  const mati = [];
  let split = null;

  // Image Scale & Fade: kartu hero tumbuh dari 0,94 ke ukuran aslinya saat
  // masuk, lalu meredup tipis saat keluar dari atas. Opasitas terendahnya
  // .55, bukan 0: kartu ini tindakan utama layar, ia tidak boleh hilang.
  const kartu = akar.querySelector(".beranda-hero .lanjutkan");
  if (kartu) {
    mati.push(g.fromTo(kartu, { scale: 0.94 }, {
      scale: 1, ease: "none",
      scrollTrigger: { trigger: kartu, start: "top 95%", end: "top 55%", scrub: 0.6 },
    }));
    mati.push(g.to(kartu, {
      opacity: 0.55, ease: "none",
      scrollTrigger: { trigger: kartu, start: "bottom 45%", end: "bottom top", scrub: 0.6 },
    }));
  }

  // Scrubbing Text Reveal: kata menyala satu per satu mengikuti gulir.
  const kalimat = akar.querySelector(".beranda-kalimat-isi");
  if (kalimat && window.SplitText) {
    g.registerPlugin(window.SplitText);
    split = window.SplitText.create(kalimat, { type: "words", aria: "auto" });
    mati.push(g.fromTo(split.words, { opacity: 0.16 }, {
      opacity: 1, stagger: 0.08, ease: "none",
      scrollTrigger: { trigger: kalimat, start: "top 82%", end: "bottom 40%", scrub: 0.5 },
    }));
  }

  // Bento TIDAK dianimasikan di sini: from(opacity: 0) yang menunggu pemicu
  // gulir berarti sel yang tak pernah tergulir tetap tersembunyi. Pemanggil
  // memakai ungkap() dari gerak.js, yang punya pengaman waktunya sendiri.

  return () => {
    for (const t of mati) {
      if (t.scrollTrigger) t.scrollTrigger.kill();
      t.kill();
    }
    if (split) split.revert();
    if (kartu) g.set(kartu, { clearProps: "transform,opacity" });
  };
}
