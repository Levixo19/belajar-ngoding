/* Cakrawala: tampilan tiga dimensi dari hamparan XP harian di kartu Bara.
 *
 * Dipilih pelajar lewat tombol di kepala kartu; tampilan datar tetap bawaan dan
 * tetap yang kanonik. Isi, angka, dan warna tingkatnya sama dengan hamparan
 * datar (`baraPetak`), jadi dua tampilan itu tidak pernah berbeda pendapat.
 * Logika dan geometrinya di `skyline-teks.ts`.
 *
 * Keputusan yang gampang terbalik tanpa satu pun error:
 *  - **Klik dan hover tidak menavigasi.** Hari yang disorot hanya mengganti
 *    baris keterangan di bawah gambar. Tooltip melayang akan menutupi batang
 *    tetangganya, dan tidak punya tempat tetap untuk pembaca layar.
 *  - **Satu kontrol yang bisa difokus, bukan 182.** Kelompoknya `tabIndex=0`
 *    dengan panah/Home/End/PageUp/PageDown; keterangannya diumumkan lewat
 *    `umumkan()` HANYA saat papan ketik yang berpindah. Hover yang ikut
 *    diumumkan akan menjadi hujan kalimat bagi pengguna pembaca layar yang
 *    kebetulan menyentuh tetikus.
 *  - **Gambarnya `aria-hidden`.** Informasinya ada di nama kelompok, baris
 *    keterangan, dan ringkasan tertulis di bawahnya.
 *  - **Gerak masuk hanya pada gerak penuh dan hanya sekali**, dibaca saat
 *    dipasang. Keadaan akhirnya adalah keadaan alami batang (animasinya
 *    berangkat dari `scaleY(0)`), jadi gerak yang dimatikan tidak pernah
 *    berarti ada batang yang hilang.
 *  - **Garis sorot digambar SESUDAH semua batang.** Ia melintasi batang yang
 *    menutupinya; itu disengaja, karena hari yang dipilih lewat papan ketik
 *    boleh saja tersembunyi di belakang batang yang lebih tinggi.
 */

import {
  useMemo, useState,
  type KeyboardEvent as TekanEvent, type PointerEvent as PenunjukEvent,
} from "react";

import { umumkan } from "../sorak.tsx";
import { useGerakPenuh } from "./gerak-penuh.ts";
import {
  bangunSkyline, kolomBaris, labelGrup, langkahSel, ringkasSkyline,
  teksHari, teksRentetan, teksTersibuk,
  type HariSkyline,
} from "./skyline-teks.ts";
import { angka } from "../util.ts";

/** Selang animasi masuk antar-minggu, dalam milidetik. */
const SELANG_MASUK = 16;
/** Kelas tingkat ditulis utuh, tidak dirakit dari awalan: pagar kelas di tes membaca literalnya. */
const KELAS_TINGKAT = ["sk-t0", "sk-t1", "sk-t2", "sk-t3"] as const;

export function Skyline({
  hari,
  kosong,
  target,
}: {
  hari: HariSkyline[];
  /** Sel kosong pembuka supaya kolom pertama jatuh di hari yang benar. */
  kosong: number;
  target: number;
}) {
  const tata = useMemo(() => bangunSkyline(hari, kosong, target), [hari, kosong, target]);
  const ringkas = useMemo(() => ringkasSkyline(hari), [hari]);
  const penuh = useGerakPenuh();
  // Dikunci saat dipasang: gerak yang dinyalakan SESUDAH gambar tampil tidak
  // boleh memutar ulang animasi masuk di depan mata orang yang sedang membaca.
  const [masuk] = useState(penuh);

  const terakhir = Math.max(0, hari.length - 1);
  const [pilihan, setPilihan] = useState(terakhir);
  const aktif = Math.min(pilihan, terakhir);
  const hariAktif = hari[aktif];

  const batangEl = useMemo(
    // Urutan `batang` sudah urutan gambar yang benar (belakang dulu): lihat `bangunSkyline`.
    () =>
      tata.batang.map((b) => (
        <g
          key={b.i}
          data-i={b.i}
          className={"sk-b " + (KELAS_TINGKAT[b.tingkat] ?? "sk-t0") + (b.kini ? " sk-kini" : "")}
          style={masuk ? { animationDelay: `${b.kolom * SELANG_MASUK}ms` } : undefined}
        >
          {b.sisi ? <polygon className="sk-sisi" points={b.sisi} /> : null}
          {b.muka ? <polygon className="sk-muka" points={b.muka} /> : null}
          <polygon className="sk-atas" points={b.atas} />
        </g>
      )),
    [tata, masuk],
  );

  if (hari.length === 0) {
    return <p className="sk-info">Belum ada hari yang tercatat.</p>;
  }

  const saatTombol = (e: TekanEvent<HTMLDivElement>) => {
    // Alt+Panah = Mundur/Maju peramban; Ctrl dan Meta milik pintasan lain.
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    const ke = langkahSel(aktif, e.key, kosong, hari.length);
    if (ke === null) return;
    e.preventDefault();
    if (ke === aktif) return;
    setPilihan(ke);
    const h = hari[ke];
    if (h) umumkan(teksHari(h, kolomBaris(ke, kosong).baris));
  };

  const saatPenunjuk = (e: PenunjukEvent<SVGSVGElement>) => {
    const g = (e.target as Element).closest("[data-i]");
    if (!g) return;
    const i = Number(g.getAttribute("data-i"));
    if (Number.isInteger(i) && i !== aktif) setPilihan(i);
  };

  const siluet = tata.batang[aktif]?.siluet ?? "";

  return (
    <div className="sk-wadah">
      <div
        className={"sk-papan" + (masuk ? " sk-masuk" : "")}
        tabIndex={0}
        role="group"
        aria-label={labelGrup(ringkas)}
        onKeyDown={saatTombol}
      >
        <div className="sk-bidang">
          <svg
            className="sk-svg"
            viewBox={`0 0 ${tata.lebar} ${tata.tinggi}`}
            aria-hidden="true"
            focusable="false"
            onPointerMove={saatPenunjuk}
            onPointerDown={saatPenunjuk}
          >
            {batangEl}
            {siluet ? <path className="sk-aktif" d={siluet} /> : null}
          </svg>
          {tata.bulan.map((b) => (
            <span
              key={b.kolom}
              className="sk-bulan"
              aria-hidden="true"
              style={{ left: `${b.x * 100}%`, top: `${b.y * 100}%` }}
            >
              {b.teks}
            </span>
          ))}
        </div>
      </div>

      <p className="sk-info">
        {hariAktif ? teksHari(hariAktif, kolomBaris(aktif, kosong).baris) : ""}
      </p>

      <dl className="sk-ringkas">
        <div>
          <dt>Total XP</dt>
          <dd>{angka(ringkas.total)}</dd>
        </div>
        <div>
          <dt>Hari tersibuk</dt>
          <dd>{teksTersibuk(ringkas)}</dd>
        </div>
        <div>
          <dt>Rentetan hari ber-XP terpanjang</dt>
          <dd>{teksRentetan(ringkas)}</dd>
        </div>
      </dl>
    </div>
  );
}
