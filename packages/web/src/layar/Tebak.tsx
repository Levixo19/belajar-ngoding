/* Tebak keluarannya: latihan membaca kode dari contoh materi yang sudah dibaca.
 *
 * Port `webapp/statik/js/layar-tebak.js`. Pembagian tanggung jawabnya TIDAK
 * berubah, dan itu yang terpenting: pemilihan kartunya (yang terakhir salah
 * ditebak dulu, lalu yang belum pernah dicoba) dan kuncinya (keluaran NYATA
 * dari menjalankan contohnya) dua-duanya milik server -- `pelajar/tebak.py`
 * lewat `/api/tebak/kartu` dan `/api/tebak`.
 *
 * Layar ini cuma menampilkan dan mengirim tebakan. Tidak ada definisi "lulus"
 * di sini, dan ia tidak menyentuh `latihan_lulus`. Menghitung benar-salah di
 * sisi klien akan jadi definisi kedua, dan sejak saat itu dua permukaan bisa
 * berbeda pendapat tentang tebakan yang sama.
 */

import { useEffect, useRef, useState } from "react";

import { ambil, kirim } from "../api.ts";
import { Kode } from "../komponen/Kode.tsx";
import { Ikon } from "../komponen/Ikon.tsx";
import { Keadaan } from "../komponen/Keadaan.tsx";
import type { Token } from "../../../bersama/src/sorot.ts";

interface Kartu {
  indeks: number;
  bagian: number;
  judul: string;
  kode: string;
  token: Token[];
}

interface JawabanKartu {
  kartu: Kartu[];
  /** Berapa blok di kurikulum ini yang LAYAK ditebak, terbaca atau belum. */
  layak: number;
  /** Toolchain bahasanya terpasang di mesin ini. */
  siap: boolean;
}

interface BarisBeda {
  tanda: string;
  harapan: string | null;
  aktual: string | null;
}

interface JawabanTebak {
  benar: boolean;
  keluaran: string;
  beda: { ringkas?: string; baris?: BarisBeda[] } | null;
}

const tanpaNomor = (t: string) => t.replace(/^\s*\d+\.\s*/, "");

interface Props {
  bahasaKey: string;
  label: string;
}

export function Tebak({ bahasaKey, label }: Props) {
  const [data, setData] = useState<JawabanKartu | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [nomor, setNomor] = useState(0);
  const [benar, setBenar] = useState(0);

  useEffect(() => {
    let dibatalkan = false;
    setData(null);
    setGalat(null);
    setNomor(0);
    setBenar(0);
    ambil<JawabanKartu>("tebak/kartu", { key: bahasaKey })
      .then((d) => {
        if (!dibatalkan) setData(d);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    // Pembatalan ini bukan kehati-hatian berlebihan: berpindah bahasa sebelum
    // permintaan pertama selesai akan membuat jawaban yang LAMA tiba
    // belakangan dan menimpa yang baru, dan yang terlihat kartu dari bahasa
    // yang sudah ditinggalkan.
    return () => {
      dibatalkan = true;
    };
  }, [bahasaKey]);

  const kepala = (
    <header className="kepala">
      <span className="mata">Latih baca kode · {label}</span>
      <h1>Tebak keluarannya</h1>
      <p className="kepala-sub">
        Baca contohnya, tulis apa yang menurutmu tercetak, lalu periksa.
        Kuncinya keluaran asli dari menjalankan kode itu.
      </p>
    </header>
  );

  if (galat) {
    return (
      <div>
        {kepala}
        <Keadaan jenis="salah" judul="Gagal memuat kartu" ket={galat} />
      </div>
    );
  }
  if (!data) {
    return (
      <div>
        {kepala}
        <div className="deret">
          <div className="pusaran" />
          <span>Memuat contoh…</span>
        </div>
      </div>
    );
  }

  if (!data.kartu.length) {
    const alasan = !data.siap
      ? `${label} belum terpasang di komputermu, jadi contohnya belum bisa ` +
        `dijalankan.`
      : data.layak
        ? "Belum ada contoh dari materi yang sudah kamu baca. Baca satu-dua " +
          "materi dulu, contohnya akan muncul di sini."
        : `Kurikulum ${label} tidak punya contoh program yang bisa ditebak ` +
          `keluarannya.`;
    return (
      <div>
        {kepala}
        <Keadaan
          jenis="kosong"
          judul="Belum ada yang bisa ditebak"
          ket={alasan}
          aksi={
            <a className="tbl" href={`#/bahasa/${bahasaKey}`}>
              Ke halaman {label}
            </a>
          }
        />
      </div>
    );
  }

  if (nomor >= data.kartu.length) {
    return (
      <div>
        {kepala}
        <div className="tebak-isi">
          <section className="kartu tebak-kartu">
            <span className="mata">Selesai</span>
            <h2>
              {benar} dari {data.kartu.length} tebakan tepat
            </h2>
            <p>
              {benar === data.kartu.length
                ? "Semua tepat. Contoh yang sudah kamu kuasai akan muncul lebih jarang."
                : "Contoh yang tadi meleset akan muncul lebih dulu di sesi berikutnya."}
            </p>
            <div className="deret">
              <button
                type="button"
                className="tbl tbl-utama"
                onClick={() => {
                  setNomor(0);
                  setBenar(0);
                }}
              >
                Sesi lagi
              </button>
              <a className="tbl" href={`#/bahasa/${bahasaKey}`}>
                Kembali ke {label}
              </a>
            </div>
          </section>
        </div>
      </div>
    );
  }

  const k = data.kartu[nomor] as Kartu;
  return (
    <div>
      {kepala}
      <div className="tebak-isi">
        <KartuTebak
          // Kunci-nya indeks kartu, bukan `nomor`: tanpa itu React memakai
          // ulang simpul yang sama untuk kartu berikutnya, dan textarea yang
          // sudah terisi tebakan lama ikut terbawa.
          key={`${k.indeks}-${k.bagian}`}
          bahasaKey={bahasaKey}
          kartu={k}
          nomor={nomor}
          total={data.kartu.length}
          onBenar={() => setBenar((n) => n + 1)}
          onLanjut={() => setNomor((n) => n + 1)}
        />
      </div>
    </div>
  );
}

interface PropsKartu {
  bahasaKey: string;
  kartu: Kartu;
  nomor: number;
  total: number;
  onBenar: () => void;
  onLanjut: () => void;
}

function KartuTebak({
  bahasaKey,
  kartu,
  nomor,
  total,
  onBenar,
  onLanjut,
}: PropsKartu) {
  const [tebakan, setTebakan] = useState("");
  const [sedang, setSedang] = useState(false);
  const [hasil, setHasil] = useState<JawabanTebak | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const areaRef = useRef<HTMLTextAreaElement>(null);
  const lanjutRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    areaRef.current?.focus();
  }, []);

  // Fokus pindah ke tombol lanjut begitu hasilnya datang, sama seperti versi
  // JS-nya. Tanpa itu orang yang memakai papan ketik harus men-Tab melewati
  // seluruh kartu untuk sampai ke satu-satunya tindakan yang tersisa.
  useEffect(() => {
    if (hasil) lanjutRef.current?.focus();
  }, [hasil]);

  async function periksa() {
    setSedang(true);
    setGalat(null);
    try {
      const r = await kirim<JawabanTebak>("tebak", {
        key: bahasaKey,
        indeks: kartu.indeks,
        kode: kartu.kode,
        tebakan,
      });
      setHasil(r);
      if (r.benar) onBenar();
    } catch (e) {
      setGalat((e as Error).message);
      setSedang(false);
    }
  }

  return (
    <section className="kartu tebak-kartu">
      <div className="tebak-kepala">
        <span className="mata">
          Kartu {nomor + 1} dari {total}
        </span>
        <a href={`#/materi/${bahasaKey}/${kartu.indeks}`}>
          dari materi {tanpaNomor(kartu.judul)}
        </a>
      </div>

      <div className="blok-sarung">
        <Kode token={kartu.token} />
      </div>

      <label className="tebak-label" htmlFor="tebak-area">
        Menurutmu, apa yang tercetak?
      </label>
      <textarea
        id="tebak-area"
        ref={areaRef}
        className="tebak-tebakan"
        rows={5}
        spellCheck={false}
        placeholder="Tulis keluarannya di sini, baris demi baris."
        value={tebakan}
        readOnly={hasil !== null}
        onChange={(e) => setTebakan(e.target.value)}
      />

      {hasil === null ? (
        <div className="deret">
          <button
            type="button"
            className="tbl tbl-utama"
            disabled={sedang}
            onClick={periksa}
          >
            Periksa tebakan
          </button>
        </div>
      ) : null}

      <div className="tebak-hasil" role="status">
        {sedang && !hasil ? (
          <div className="deret">
            <div className="pusaran" />
            <span>Menjalankan contohnya…</span>
          </div>
        ) : null}
        {galat ? <p className="tebak-vonis tebak-belum">{galat}</p> : null}
        {hasil ? (
          <>
            <p
              className={
                "tebak-vonis " + (hasil.benar ? "tebak-benar" : "tebak-belum")
              }
            >
              {hasil.benar
                ? "Tepat. Kamu membaca kodenya dengan benar."
                : "Belum tepat. Bandingkan dengan keluaran aslinya:"}
            </p>
            {hasil.benar ? null : <TabelBeda beda={hasil.beda} />}
            <div className="tebak-asli">
              <span className="mata">Keluaran asli</span>
              <pre className="terminal">{hasil.keluaran}</pre>
            </div>
            <div className="deret">
              <button
                ref={lanjutRef}
                type="button"
                className={"tbl" + (hasil.benar ? " tbl-utama" : "")}
                onClick={onLanjut}
              >
                {nomor + 1 < total ? "Kartu berikutnya" : "Lihat hasil"}
                <Ikon nama="lanjut" ukuran={16} />
              </button>
            </div>
          </>
        ) : null}
      </div>
    </section>
  );
}

/** Perbandingan baris demi baris, dari `beda.bandingkan` di server. */
function TabelBeda({ beda }: { beda: JawabanTebak["beda"] }) {
  if (!beda || !beda.baris) return null;
  return (
    <div className="tebak-beda">
      {beda.ringkas ? <p>{beda.ringkas}</p> : null}
      <table className="tebak-tabel">
        <thead>
          <tr>
            <th>Asli</th>
            <th>Tebakanmu</th>
          </tr>
        </thead>
        <tbody>
          {beda.baris.map((r, i) => (
            <tr key={i} className={r.tanda === "=" ? "" : "tebak-beda-baris"}>
              <td>
                <code>{r.harapan ?? ""}</code>
              </td>
              <td>
                <code>{r.aktual ?? ""}</code>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
