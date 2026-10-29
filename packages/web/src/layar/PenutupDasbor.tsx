/* Penutup dasbor ("Cakrawala"): layar penuh yang TERSINGKAP di bawah dasbor saat
 * digulir sampai habis. Isi dasbor naik, dan layar ini yang sudah menunggu di
 * bawahnya menjadi terlihat, bukan datang dari bawah.
 *
 * Gagasannya dari komponen "Motion Footer" (21st.dev; penulis Hossain Jahed,
 * bidang lisensinya KOSONG, jadi tidak ada kodenya yang disalin). Yang diambil
 * adalah CARA KERJANYA, dibaca dari bundelnya lewat REA, lalu ditulis ulang di
 * atas mesin gerak repo ini tanpa pustaka baru:
 *  - Penyingkapan: pembungkus ber-`clip-path` memuat lapisan `position: fixed`.
 *    Pembungkus ikut tergulir, lapisannya diam, dan `clip-path` hanya
 *    memperlihatkan bagian lapisan yang jatuh di dalam kotak pembungkus.
 *  - Latar berlapis: cahaya aurora yang "bernapas", kisi bertopeng, dan satu
 *    kata raksasa tembus pandang.
 *  - Strip teks miring yang berjalan terus. Isinya angka NYATA dari profil.
 *  - Pil kaca yang mengikuti kursor: `magnet()` dari `gerak.ts` (aslinya GSAP).
 *  - Kemunculan terhubung gulir: CSS `animation-timeline: view()`, tanpa
 *    pendengar gulir dan tanpa JS.
 *
 * Aturan yang gampang terbalik, semuanya tanpa satu pun error kalau salah:
 *  - Animasi tak berhingga (strip, aurora) hanya berjalan selagi pembungkus
 *    TERLIHAT (`data-tampak`) dan hanya di tingkat gerak penuh. Di luar itu
 *    mereka berhenti; keadaan diamnya adalah keadaan alami, jadi gerak yang
 *    dimatikan tidak menghilangkan apa pun.
 *  - Lapisan `fixed` yang dipotong tidak boleh menjebak papan ketik: tautan di
 *    dalamnya tetap bisa difokuskan, dan fokus yang masuk ke sana menggulir
 *    halaman sampai dasar supaya lapisannya benar-benar terlihat.
 *  - Satu layar satu tombol utama: penutup tidak punya tombol beraksen. Tombol
 *    "ke atas" membawa orang kembali ke kartu Lanjutkan.
 *  - Strip `aria-hidden` (ia berulang dan berjalan); ringkasannya dibacakan
 *    sekali lewat teks tersembunyi. */

import { useEffect, useRef, useState } from "react";

import { adaGerak, magnet } from "../gerak.ts";
import { Ikon } from "../komponen/Ikon.tsx";
import { useGerakPenuh } from "../komponen/gerak-penuh.ts";
import type { DataDasbor } from "./dasbor-teks.ts";
import {
  KATA_RAKSASA, TAUTAN_KECIL, TAUTAN_UTAMA,
  alisPenutup, butirStrip, judulPenutup, ringkasStrip,
} from "./penutup-teks.ts";

/** Kekuatan tarikan magnet (piksel): pil besar lebih berani daripada yang kecil. */
const KUAT_BESAR = 9;
const KUAT_KECIL = 6;
/** Berapa salinan kelompok butir dalam satu paruh strip, supaya paruhnya lebih lebar dari layar. */
const SALINAN = 4;

export function PenutupDasbor({ d }: { d: DataDasbor }) {
  const bungkus = useRef<HTMLElement>(null);
  const isi = useRef<HTMLDivElement>(null);
  const [tampak, setTampak] = useState(false);
  // Tingkat penuh = tersingkap saat digulir + gerak berjalan. Selain itu bagian statis biasa di
  // dasar halaman: membajak gulir adalah gerak akibat interaksi (WCAG 2.3.3), dan `prefers-
  // reduced-motion` selalu menang karena `useGerakPenuh` mendengarkannya.
  const penuh = useGerakPenuh();
  const butir = butirStrip(d);

  // Animasi tak berhingga hanya berjalan selagi penutup terlihat.
  useEffect(() => {
    const el = bungkus.current;
    if (!el) return;
    const pengamat = new IntersectionObserver(
      ([e]) => setTampak(e?.isIntersecting ?? false),
      { threshold: 0.12 },
    );
    pengamat.observe(el);
    return () => pengamat.disconnect();
  }, []);

  // Pil mengikuti kursor. `magnet()` sendiri membaca `gerakPenuh()` tiap peristiwa dan mati di
  // layar sentuh; pembersihnya WAJIB dipanggil (StrictMode memasang dua kali).
  useEffect(() => {
    const el = isi.current;
    if (!el) return;
    const lepas = [...el.querySelectorAll<HTMLElement>("[data-tarik]")]
      .map((e) => magnet(e, { kuat: e.dataset.tarik === "besar" ? KUAT_BESAR : KUAT_KECIL }));
    return () => lepas.forEach((f) => f());
  }, []);

  /** Tab menjatuhkan fokus ke tautan di lapisan yang masih terpotong: gulir ke dasar supaya terlihat. */
  const saatFokus = () => {
    const b = bungkus.current;
    if (!b || b.getBoundingClientRect().top <= 8) return;
    window.scrollTo({ top: document.documentElement.scrollHeight, behavior: adaGerak() ? "smooth" : "auto" });
  };
  const keAtas = () => window.scrollTo({ top: 0, behavior: adaGerak() ? "smooth" : "auto" });

  return (
    <section
      ref={bungkus}
      className="pd-bungkus"
      data-tampak={tampak ? "ya" : "tidak"}
      data-penuh={penuh ? "ya" : "tidak"}
      aria-labelledby="pd-judul"
    >
      <div ref={isi} className="pd-isi" onFocus={saatFokus}>
        <div className="pd-aurora" aria-hidden="true" />
        <div className="pd-kisi" aria-hidden="true" />
        <div className="pd-raksasa" aria-hidden="true">{KATA_RAKSASA}</div>

        <div className="pd-strip" aria-hidden="true">
          <div className="pd-jalur">
            {[0, 1].map((paruh) => (
              <div key={paruh} className="pd-paruh">
                {Array.from({ length: SALINAN }, (_, k) => (
                  <ul key={k} className="pd-kelompok">
                    {butir.map((b) => <li key={b}>{b}</li>)}
                  </ul>
                ))}
              </div>
            ))}
          </div>
        </div>
        <p className="pd-sr">{ringkasStrip(d)}</p>

        <div className="pd-tengah">
          <span className="pd-alis">{alisPenutup(d)}</span>
          <h2 id="pd-judul" className="pd-judul">{judulPenutup(d)}</h2>

          <div className="pd-aksi">
            {TAUTAN_UTAMA.map((t) => (
              <a key={t.href} className="pd-pil pd-pil-besar" href={t.href} data-tarik="besar">
                <span className="pd-inti">
                  <Ikon nama={t.ikon} ukuran={20} />
                  <span>{t.label}</span>
                  <span className="pd-bulat" aria-hidden="true">
                    <Ikon nama="lanjut" ukuran={16} />
                  </span>
                </span>
              </a>
            ))}
          </div>
          <div className="pd-kecil">
            {TAUTAN_KECIL.map((t) => (
              <a key={t.href} className="pd-pil pd-pil-kecil" href={t.href} data-tarik="kecil">
                <Ikon nama={t.ikon} ukuran={16} />
                <span>{t.label}</span>
              </a>
            ))}
          </div>
        </div>

        <div className="pd-kaki">
          <p className="pd-catatan">Progres tersimpan di komputer ini, tidak dikirim ke mana pun.</p>
          <button
            type="button" className="pd-pil pd-atas" data-tarik="kecil"
            aria-label="Kembali ke atas" onClick={keAtas}
          >
            <Ikon nama="lanjut" ukuran={20} />
          </button>
        </div>
      </div>
    </section>
  );
}
