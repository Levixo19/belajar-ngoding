/* Penampil pohon berkas untuk blok kode multi-berkas di halaman materi.
 *
 * Pohon folder di kiri, kode berkas yang dipilih di kanan. Sebelumnya blok
 * seperti ini (25 di kurikulum: struktur project Python, modul JavaScript,
 * header C, testing Go dan PHP) tampil sebagai SATU blok panjang berisi
 * komentar penanda, dan pelajar harus memecahnya sendiri di kepala. Logikanya
 * di `pohon-teks.ts`; gagasannya dari "Tree Code Viewer" (21st.dev), ditulis
 * ulang tanpa Tailwind, shadcn, maupun pustaka ikon.
 *
 * Keputusan yang gampang terbalik tanpa satu pun error:
 *  - **Satu perhentian Tab, pola WAI-ARIA tree**: baris yang berfokus
 *    `tabIndex=0`, sisanya -1 (roving). Panah memindahkan fokus, kanan dan kiri
 *    membuka dan menutup folder, Enter atau Spasi memilih berkas. Tab keluar
 *    dari pohon, tidak menyusuri tiap baris.
 *  - **Klik hanya memilih dan membuka**: tidak ada navigasi, tidak ada
 *    pembukaan materi, tidak ada penulisan progres.
 *  - **Semua folder terbuka sejak awal.** Isi sebuah contoh paling banyak
 *    enam berkas; folder yang tertutup menyembunyikan justru yang sedang dicari.
 *  - **Warna tiap berkas dari EKSTENSINYA**, bukan dari bahasa blok: blok
 *    CSS memuat `index.html`, blok JavaScript memuat `package.json`. Ekstensi
 *    yang tidak dikenal hanya mendapat pewarnaan dasar (string, angka,
 *    operator, pemanggilan fungsi), tidak ada kata kunci bahasa yang bisa salah.
 *  - **Isi tidak hilang.** Penanda berkas dihapus dari isi karena namanya sudah
 *    jadi baris pohon dan kepala panel; yang bukan penanda tetap ada, dan
 *    komentar pembuka (langkah menyiapkan folder) tampil di atas penampil.
 */

import {
  useEffect, useMemo, useRef, useState,
  type CSSProperties, type KeyboardEvent as TekanEvent,
} from "react";

import { salin } from "../sorak.tsx";
import { angka } from "../util.ts";
import { Ikon } from "./Ikon.tsx";
import { Kode } from "./Kode.tsx";
import {
  bangunPohon, barisTampak, jalurBerkas, labelBaris, langkahPohon, semuaFolder, sorotBerkas,
  type BerkasPecah,
} from "./pohon-teks.ts";

export function PohonBerkas({
  catatan,
  berkas,
}: {
  catatan: string;
  berkas: BerkasPecah[];
}) {
  const pohon = useMemo(() => bangunPohon(berkas.map((b) => b.nama)), [berkas]);
  const [terbuka, setTerbuka] = useState<ReadonlySet<string>>(() => new Set(semuaFolder(pohon)));
  const [dipilih, setDipilih] = useState(0);
  const baris = useMemo(() => barisTampak(pohon, terbuka), [pohon, terbuka]);
  const [fokus, setFokus] = useState(() => {
    const awal = barisTampak(pohon, new Set(semuaFolder(pohon)));
    return Math.max(0, awal.findIndex((b) => !b.simpul.folder && b.simpul.berkas === 0));
  });
  const fokusAman = Math.min(fokus, Math.max(0, baris.length - 1));
  const pegangan = useRef<Array<HTMLDivElement | null>>([]);
  // Fokus dipindah program HANYA sesudah tombol papan ketik; klik dan fokus
  // masuk lewat Tab tidak boleh merebut fokus yang baru saja diberikan orang.
  const perluFokus = useRef(false);

  useEffect(() => {
    if (!perluFokus.current) return;
    perluFokus.current = false;
    pegangan.current[fokusAman]?.focus();
  }, [fokusAman, terbuka]);

  const alih = (kunci: string, buka: boolean) =>
    setTerbuka((sebelum) => {
      const baru = new Set(sebelum);
      if (buka) baru.add(kunci);
      else baru.delete(kunci);
      return baru;
    });

  const saatTombol = (e: TekanEvent<HTMLDivElement>) => {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    const a = langkahPohon(baris, fokusAman, e.key, terbuka);
    if (a === null) return;
    e.preventDefault();
    perluFokus.current = true;
    setFokus(a.fokus);
    if (a.buka) alih(a.buka, true);
    if (a.tutup) alih(a.tutup, false);
    if (a.pilih) {
      const s = baris[a.fokus]?.simpul;
      if (s && !s.folder) setDipilih(s.berkas);
    }
  };

  const ini = berkas[dipilih] ?? berkas[0];
  if (!ini) return null;
  const jalur = jalurBerkas(ini.nama);

  return (
    <div className="pb-wadah">
      {catatan ? <Kode kode={catatan} bahasa="" kelas="pb-catatan" /> : null}
      <div className="pb-badan">
        <div
          className="pb-pohon"
          role="tree"
          aria-label="Berkas dalam contoh ini"
          onKeyDown={saatTombol}
        >
          {baris.map((b, i) => {
            const s = b.simpul;
            return (
              <div
                key={s.kunci}
                ref={(el) => { pegangan.current[i] = el; }}
                role="treeitem"
                tabIndex={i === fokusAman ? 0 : -1}
                aria-level={b.kedalaman + 1}
                aria-posinset={b.posisi}
                aria-setsize={b.ukuran}
                aria-expanded={s.folder ? terbuka.has(s.kunci) : undefined}
                aria-selected={s.folder ? undefined : s.berkas === dipilih}
                aria-label={labelBaris(b, berkas)}
                className={"pb-baris " + (s.folder ? "pb-folder" : "pb-berkas")}
                style={{ "--pb-dalam": b.kedalaman } as CSSProperties}
                onFocus={() => setFokus(i)}
                onClick={() => {
                  setFokus(i);
                  if (s.folder) alih(s.kunci, !terbuka.has(s.kunci));
                  else setDipilih(s.berkas);
                }}
              >
                {s.folder ? (
                  <span className="pb-panah" aria-hidden="true" />
                ) : (
                  <Ikon nama="berkas" ukuran={14} />
                )}
                <span className="pb-nama">{s.label}</span>
              </div>
            );
          })}
        </div>

        <div className="pb-isi" role="region" aria-label={"Isi " + ini.nama}>
          <div className="pb-kepala">
            <span className="pb-jalur">
              <span className="pb-jalur-folder">{jalur.folder}</span>
              {jalur.berkas}
            </span>
            <span className="pb-meta">
              {ini.baris === 0 ? "kosong" : `${angka(ini.baris)} baris`}
            </span>
            <button
              type="button"
              className="tbl tbl-kecil tbl-hantu"
              onClick={() => { void salin(ini.isi); }}
            >
              Salin berkas ini
            </button>
          </div>
          {ini.isi === "" ? (
            <p className="pb-kosong">Berkas ini kosong di contohnya.</p>
          ) : (
            <Kode kode={ini.isi} bahasa={sorotBerkas(ini.nama)} />
          )}
        </div>
      </div>
    </div>
  );
}
