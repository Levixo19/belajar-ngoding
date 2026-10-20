/* "Lihat jalannya": langkah demi langkah sebuah contoh Python.
 *
 * Port `jejak.js`. Datanya dari `POST /api/jejak` (`inti/jejak.py`): tiap
 * langkah membawa baris yang AKAN dijalankan, peristiwanya, isi seluruh
 * tumpukan pemanggilan, dan panjang keluaran sejauh itu. Panel ini cuma
 * memutar ulang rekaman itu; tidak ada eksekusi di browser dan tidak ada yang
 * menyentuh progres.
 *
 * Yang sengaja diperlihatkan, karena di situ pemula paling sering salah
 * bayangan:
 *   * baris yang baru saja jalan (redup) dan yang akan jalan (kuningan);
 *   * variabel yang BERUBAH di langkah ini ditandai;
 *   * dua nama yang memegang objek yang SAMA diberi nomor objek yang sama,
 *     jadi "kok list-ku ikut berubah" terjawab dengan melihat, bukan dengan
 *     dijelaskan.
 */

import { useEffect, useRef, useState } from "react";

import { kirim } from "../api.ts";
import { umumkan } from "../sorak.tsx";
import {
  kalimat, tokenPerBaris, type Langkah, type Rekaman, type Token,
} from "./jejak-teks.ts";

const JEDA_PUTAR = 750;

function BarisKode({ pasangan }: { pasangan: Token[] }) {
  return (
    <code>
      {pasangan.map(([jenis, teks], i) =>
        (jenis === "teks" ? teks : <span key={i} className={"tk-" + jenis}>{teks}</span>))}
    </code>
  );
}

/** Satu bingkai tumpukan: namanya, lalu tabel variabelnya. */
function Bingkai({
  f, sebelum, atas,
}: {
  f: Langkah["tumpukan"][number];
  /** Isi bingkai yang SAMA di langkah sebelumnya, untuk menandai yang berubah. */
  sebelum: Record<string, { r: string }> | null;
  atas: boolean;
}) {
  const isi = Object.entries(f.isi);
  return (
    <div className={"jejak-satu" + (atas ? " jejak-atas" : "")}>
      <div className="jejak-nama">{f.nama}</div>
      {isi.length ? (
        <table>
          <tbody>
            {isi.map(([k, v]) => {
              const lama = sebelum ? sebelum[k] : undefined;
              const berubah = !!sebelum && (!lama || lama.r !== v.r);
              return (
                <tr key={k} className={berubah ? "jejak-berubah" : undefined}>
                  <th scope="row">{k}</th>
                  <td>
                    <code>{v.r}</code>
                    {v.id ? (
                      <span
                        className="jejak-objek"
                        title="Nama dengan nomor objek yang sama memegang objek yang sama"
                      >
                        {"objek " + v.id}
                      </span>
                    ) : null}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      ) : (
        <p className="jejak-kosong">belum ada variabel</p>
      )}
    </div>
  );
}

export function Jejak({
  kode,
  token,
  onTutup,
}: {
  kode: string;
  /** Token server, hanya kalau kodenya masih yang asli. `null` = tanpa warna. */
  token?: Token[] | null;
  onTutup: () => void;
}) {
  const [rekaman, setRekaman] = useState<Rekaman | null>(null);
  const [galat, setGalat] = useState("");
  const [kini, setKini] = useState(0);
  const [putar, setPutar] = useState(false);
  const panelRef = useRef<HTMLElement>(null);
  const daftarRef = useRef<HTMLOListElement>(null);

  useEffect(() => {
    let dibatalkan = false;
    (async () => {
      try {
        const r = await kirim<Rekaman>("/api/jejak", { bahasa: "python", kode });
        if (dibatalkan) return;
        if (!r.langkah.length) {
          setGalat(r.galat || "Tidak ada langkah yang tercatat.");
          return;
        }
        setRekaman(r);
        setKini(0);
        umumkan(`Rekaman siap: ${r.langkah.length} langkah. `
          + "Panah kiri dan kanan untuk berpindah langkah.");
      } catch (e) {
        if (!dibatalkan) setGalat((e as Error).message);
      }
    })();
    return () => { dibatalkan = true; };
  }, [kode]);

  // Fokus dipindah ke panel sekali, SESUDAH rekamannya ada: panel yang masih
  // berisi pusaran tidak punya apa pun untuk dibacakan, dan memindahkan fokus
  // ke situ cuma membuang tempat orang berada sebelumnya.
  useEffect(() => {
    if (rekaman) panelRef.current?.focus({ preventScroll: true });
  }, [rekaman]);

  const n = rekaman ? rekaman.langkah.length : 0;

  useEffect(() => {
    if (!putar || !n) return;
    const id = setInterval(() => {
      setKini((k) => {
        // Berhenti sendiri di ujung. Pengatur waktu yang terus hidup di
        // langkah terakhir tidak kelihatan, tapi ia tetap membangunkan React
        // tiap 750 ms selama panelnya terbuka.
        if (k >= n - 1) { setPutar(false); return k; }
        return k + 1;
      });
    }, JEDA_PUTAR);
    return () => clearInterval(id);
  }, [putar, n]);

  /* Jalur kodenya digulir lewat `scrollTop`, BUKAN `scrollIntoView`.
   *
   * `scrollIntoView` menggulir setiap leluhur yang bisa digulir, termasuk
   * dokumen -- jadi melompat ke langkah yang barisnya jauh di bawah akan ikut
   * memindahkan halamannya, dan contoh kode yang sedang dibaca orangnya hilang
   * dari pandangan. Aturan yang sama dengan `bawaKeTengah()` di pembaca
   * materi. */
  useEffect(() => {
    const daftar = daftarRef.current;
    if (!daftar || !rekaman) return;
    const l = rekaman.langkah[kini];
    if (!l) return;
    const li = daftar.children[l.baris - 1] as HTMLElement | undefined;
    if (li) daftar.scrollTop = Math.max(0, li.offsetTop - daftar.clientHeight / 2);
  }, [kini, rekaman]);

  const ke = (nomor: number) => {
    setPutar(false);
    setKini(Math.max(0, Math.min(n - 1, nomor)));
  };

  if (galat) {
    return (
      <section className="jejak" aria-label="Jalannya program">
        <p className="jejak-galat">{galat}</p>
      </section>
    );
  }
  if (!rekaman) {
    return (
      <section className="jejak" aria-label="Jalannya program">
        <div className="deret">
          <div className="pusaran" />
          <span>Merekam jalannya program…</span>
        </div>
      </section>
    );
  }

  const baris: Token[][] = token
    ? tokenPerBaris(token)
    : kode.split("\n").map((t) => [["teks", t] as Token]);

  const l = rekaman.langkah[kini] as Langkah;
  const lalu = kini > 0 ? (rekaman.langkah[kini - 1] as Langkah) : null;
  const akhir = kini === n - 1;

  let teks = kalimat(l, !akhir);
  if (akhir && rekaman.terpotong) {
    teks += " Rekaman berhenti di sini karena programnya terlalu panjang.";
  }
  if (akhir && rekaman.galat) teks += ` Program berhenti: ${rekaman.galat}`;

  const tbl = (label: string, judul: string, fn: () => void) => (
    <button
      type="button"
      className="tbl tbl-kecil tbl-hantu"
      title={judul}
      aria-label={judul}
      onClick={fn}
    >
      {label}
    </button>
  );

  return (
    <section
      ref={panelRef}
      className="jejak"
      aria-label="Jalannya program"
      tabIndex={-1}
      onKeyDown={(e) => {
        if ((e.target as HTMLElement).classList.contains("jejak-geser")) return;
        if (e.key === "ArrowRight") { e.preventDefault(); ke(kini + 1); }
        else if (e.key === "ArrowLeft") { e.preventDefault(); ke(kini - 1); }
      }}
    >
      <div className="jejak-kepala">
        <b>Jalannya program</b>
        <span className="jejak-hitung">{`Langkah ${kini + 1} dari ${n}`}</span>
        <button type="button" className="tbl tbl-kecil tbl-hantu" onClick={onTutup}>
          Tutup
        </button>
      </div>

      <div className="jejak-tata">
        <ol ref={daftarRef} className="jejak-kode">
          {baris.map((p, i) => (
            <li
              key={i}
              data-baris={i + 1}
              className={
                i + 1 === l.baris ? "jejak-kini"
                  : lalu && i + 1 === lalu.baris ? "jejak-lalu" : undefined
              }
            >
              <span className="jejak-nomor">{i + 1}</span>
              <BarisKode pasangan={p} />
            </li>
          ))}
        </ol>
        <div className="jejak-kanan">
          <div className="jejak-label">Variabel</div>
          <div className="jejak-bingkai">
            {l.tumpukan.map((f, i) => {
              const bingkaiLalu = lalu ? lalu.tumpukan[i] : undefined;
              return (
                <Bingkai
                  key={i}
                  f={f}
                  sebelum={bingkaiLalu && bingkaiLalu.nama === f.nama
                    ? bingkaiLalu.isi : null}
                  atas={i === l.tumpukan.length - 1}
                />
              );
            })}
          </div>
          <div className="jejak-label">Keluaran sejauh ini</div>
          <pre className="terminal jejak-keluaran">
            {rekaman.keluaran.slice(0, akhir ? rekaman.keluaran.length : l.keluar) || " "}
          </pre>
        </div>
      </div>

      {/* Selama diputar, kalimat tiap langkah tidak dibacakan satu per satu:
          pembaca layar akan mengantrekannya tanpa henti tiap 750 ms. */}
      <p className="jejak-ket" aria-live={putar ? "off" : "polite"}>{teks}</p>

      <div className="jejak-alat">
        {tbl("⏮", "Ke awal", () => ke(0))}
        {tbl("◀", "Mundur satu langkah", () => ke(kini - 1))}
        <button
          type="button"
          className="tbl tbl-kecil tbl-hantu"
          title="Putar otomatis"
          onClick={() => {
            if (putar) { setPutar(false); return; }
            if (kini >= n - 1) setKini(0);
            setPutar(true);
          }}
        >
          {putar ? "Jeda" : "Putar"}
        </button>
        {tbl("▶", "Maju satu langkah", () => ke(kini + 1))}
        {tbl("⏭", "Ke akhir", () => ke(n - 1))}
        <input
          className="jejak-geser"
          type="range"
          min={0}
          max={n - 1}
          value={kini}
          aria-label="Pilih langkah"
          onChange={(e) => ke(Number(e.target.value))}
        />
      </div>
    </section>
  );
}
