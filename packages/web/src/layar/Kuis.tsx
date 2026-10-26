/* Layar kuis: persiapan, sesi soal, lalu hasil.
 *
 * Port `layarKuis` dari `webapp/statik/js/layar-kerja.js`.
 *
 * Tiga hal yang mengikat, dan ketiganya soal KEBENARAN, bukan tampilan:
 *
 * 1. **Muatan soal tidak membawa kunci jawaban.** `sesi.bersih()` di server
 *    sengaja memangkasnya, dan `penjelasan` datang dari RESPONS
 *    `/api/kuis/jawab` -- bukan dari muatan soal. Memindahkannya ke muatan soal
 *    "supaya hemat satu permintaan" berarti membocorkan jawabannya ke tab
 *    Network sebelum orangnya menjawab.
 * 2. **Index jawaban sudah dipetakan ulang di server** (`sesi._acak_soal`).
 *    Layar ini TIDAK mengacak apa pun sendiri dan tidak menerjemahkan index
 *    apa pun; ia cuma mengirim nomor opsi yang ditekan.
 * 3. **Jamnya berhenti saat tabnya di latar**, dan melanjutkan dari sisa detik
 *    yang sama. WCAG 2.2.2: detik yang habis sementara tabnya tidak terlihat
 *    adalah detik yang tidak pernah bisa dipakai siapa pun untuk menjawab.
 */

import { useCallback, useEffect, useRef, useState } from "react";

import { ambil, kirim } from "../api.ts";
import { rayakan, sorak, umumkan, type Hadiah } from "../sorak.tsx";
import { jamMundur } from "../waktu.ts";
import { Bilah } from "../komponen/Bilah.tsx";
import { Keadaan } from "../komponen/Keadaan.tsx";
import { Berkode } from "../komponen/Prosa.tsx";
import { SakelarBaris } from "../komponen/Sakelar.tsx";
import { jadwalRamah } from "./kerja-beda.ts";
import type { Konteks } from "../Cangkang.tsx";

const HURUF = "ABCDEFGHIJ";

/* ====================================================== bentuk jawaban API */

interface ButirKuis {
  judul: string;
  soal: number;
  total_soal: number;
  terbaik: number;
  pernah: boolean;
  percobaan: number;
  jadwal: string | null;
  jatuh_tempo: boolean;
  salah_tersisa: number;
  bookmark: boolean;
}
interface DataBahasa {
  key: string;
  label: string;
  kuis: ButirKuis[];
}

interface SoalSesi { nomor: number; q: string; options: string[] }
interface Sesi {
  sesi: string;
  judul: string;
  bahasa: string;
  mode: string;
  durasi: number;
  total: number;
  soal: SoalSesi[];
}
interface Jawaban {
  benar: boolean;
  jawaban_benar: number;
  pilihanmu: number;
  penjelasan: string;
  terjawab: number;
  total: number;
}
interface Rincian {
  nomor: number;
  asli: number;
  q: string;
  options: string[];
  jawaban_benar: number;
  pilihanmu: number | null;
  benar: boolean;
  penjelasan: string;
  baca_lagi?: { judul: string; indeks: number; terkunci: boolean } | null;
}
interface Rekap extends Hadiah {
  sesi_penuh: boolean;
  benar: number;
  total: number;
  total_asli: number;
  detik: number;
  terbaik: number;
  terakhir_sebelum: number | null;
  jadwal: string | null;
  salah_tersisa: number;
  rincian: Rincian[];
}

/* ================================================================ persiapan */

/** "Baca lagi: <materi>" untuk soal yang dijawab salah.
 *
 *  Materinya ditentukan server (`data/kuis_materi.py`, ditinjau soal demi
 *  soal). Materi di bab yang masih terkunci ditandai LEBIH DULU dan tidak
 *  dijadikan tautan: tombol yang berujung penolakan dilarang. */
function BacaLagi({ d, kunciBahasa }: { d: Rincian; kunciBahasa: string }) {
  const m = d.baca_lagi;
  if (!m) return null;
  if (m.terkunci) {
    return (
      <div className="baca-lagi">
        {"Dibahas di "}<b>{m.judul}</b>{" (babnya belum terbuka)"}
      </div>
    );
  }
  return (
    <div className="baca-lagi">
      {"Baca lagi: "}
      <a href={`#/materi/${kunciBahasa}/${m.indeks}`}>{m.judul}</a>
    </div>
  );
}

function Persiapan({
  b, q, nomorKuis, acak, timer, setAcak, setTimer, onMulai,
}: {
  b: DataBahasa; q: ButirKuis; nomorKuis: number;
  acak: boolean; timer: boolean;
  setAcak: (v: boolean) => void; setTimer: (v: boolean) => void;
  onMulai: (mode: string) => void;
}) {
  const persen = q.total_soal ? (q.terbaik / q.total_soal) * 100 : 0;
  return (
    <>
      <header className="kepala-besar">
        <span className="mata">
          {`${b.label} · kuis ${nomorKuis + 1} dari ${b.kuis.length}`}
        </span>
        <h1>{q.judul}</h1>
        <p className="kepala-sub">
          {`${q.soal} soal pilihan ganda. Jawaban yang salah bukan kegagalan. `
            + "Ia yang memberi tahu bagian mana yang perlu dibaca ulang."}
        </p>
        <div className="kepala-aksi">
          <div className="deret deret-rapat">
            <span className="pil">{`${q.soal} soal`}</span>
            {q.pernah ? (
              <span className="pil">{`${q.percobaan}× dikerjakan`}</span>
            ) : null}
          </div>
        </div>
      </header>

      {q.pernah ? (
        <div className="kartu" style={{ marginBottom: "var(--s5)" }}>
          <div className="rinci-atas">
            <span>Skor terbaikmu</span>
            <b style={{ fontFamily: "var(--f-kode)" }}>
              {`${q.terbaik}/${q.total_soal}`}
            </b>
          </div>
          <Bilah persen={persen} kelas={persen >= 100 ? "tumbuh" : undefined} />
          <div className="deret deret-rapat" style={{ marginTop: "var(--s3)" }}>
            {q.jatuh_tempo ? (
              <span className="pil pil-ungu">sudah waktunya diulang</span>
            ) : q.jadwal ? (
              <span className="pil">{jadwalRamah(q.jadwal)}</span>
            ) : null}
            {q.salah_tersisa ? (
              <span className="pil">{`${q.salah_tersisa} soal untuk diulang`}</span>
            ) : null}
          </div>
        </div>
      ) : null}

      {/* Tindakan utama berdiri PALING ATAS, setelannya menyusul di balik panel
          yang dilipat. Dua sakelar selebar halaman yang harus dilewati sebelum
          sampai ke tombol Mulai mengubah layar pembuka kuis jadi formulir --
          padahal keduanya sudah punya nilai bawaan yang benar untuk hampir
          semua orang, hampir setiap kali. */}
      <div className="deret">
        <button type="button" className="tbl tbl-utama"
                onClick={() => onMulai("penuh")}>
          {q.pernah ? "Kerjakan lagi" : "Mulai kuis"}
        </button>
        {q.salah_tersisa ? (
          <button type="button" className="tbl" onClick={() => onMulai("salah")}>
            {`Ulangi ${q.salah_tersisa} soal yang masih salah`}
          </button>
        ) : null}
      </div>

      {q.salah_tersisa ? (
        <p className="baris-sisi" style={{ margin: "var(--s4) 0" }}>
          Mode ulangan tidak menyentuh skor terbaikmu; ia hanya mengurangi
          daftar soal yang masih salah.
        </p>
      ) : null}

      <details className="bantuan" style={{ marginTop: "var(--s5)" }}>
        <summary className="bantuan-kepala">
          <b>Setelan kuis</b>
          <span>{acak ? "soal diacak" : "urutan asli"}</span>
        </summary>
        <div className="bantuan-isi">
          <SakelarBaris
            judul="Acak urutan soal & opsi"
            ket="Supaya jawaban tidak bisa dihafal dari posisinya."
            nyala={acak}
            onUbah={setAcak}
          />
          <SakelarBaris
            judul="Mode timer"
            ket={"Beri batas waktu. Berguna menjelang ujian; melelahkan untuk "
              + "latihan harian."}
            nyala={timer}
            onUbah={setTimer}
          />
        </div>
      </details>
    </>
  );
}

/* ===================================================================== sesi */

function SesiKuis({
  sesi, onSelesai, onBatal,
}: {
  sesi: Sesi;
  onSelesai: (r: Rekap, kehabisanWaktu: boolean) => void;
  onBatal: () => void;
}) {
  const [nomor, setNomor] = useState(0);
  const [jawaban, setJawaban] = useState<Jawaban | null>(null);
  const [sisaDetik, setSisaDetik] = useState(sesi.durasi);
  const lanjutRef = useRef<HTMLButtonElement>(null);
  const soalRef = useRef<HTMLDivElement>(null);
  const selesaiRef = useRef(false);

  const selesai = useCallback(async (kehabisanWaktu: boolean) => {
    if (selesaiRef.current) return;
    selesaiRef.current = true;
    try {
      const r = await kirim<Rekap>("kuis/selesai", { sesi: sesi.sesi });
      onSelesai(r, kehabisanWaktu);
    } catch (e) {
      sorak((e as Error).message, "salah");
      onBatal();
    }
  }, [sesi.sesi, onSelesai, onBatal]);

  /* Jamnya BERHENTI saat tabnya di latar, dan melanjutkan dari sisa detik yang
     sama -- bukan menghitung ulang dari penuh, dan bukan terus berjalan di
     belakang punggung orangnya. WCAG 2.2.2 menelan batas waktu yang berhitung
     sendiri juga.

     `sisaDetik` tidak disentuh saat tabnya disembunyikan, dan itu seluruh
     triknya: yang dihentikan pencacahnya, bukan angkanya. */
  useEffect(() => {
    if (!sesi.durasi) return;
    let id = 0;
    const jalan = () => {
      if (id) return;
      id = setInterval(() => {
        setSisaDetik((d) => {
          if (d <= 1) {
            clearInterval(id);
            id = 0;
            void selesai(true);
            return 0;
          }
          return d - 1;
        });
      }, 1000) as unknown as number;
    };
    const berhenti = () => { if (id) { clearInterval(id); id = 0; } };
    const saatTampil = () => (document.hidden ? berhenti() : jalan());
    jalan();
    document.addEventListener("visibilitychange", saatTampil);
    return () => {
      berhenti();
      document.removeEventListener("visibilitychange", saatTampil);
    };
  }, [sesi.durasi, selesai]);

  const s = sesi.soal[nomor] as SoalSesi;

  const jawab = useCallback(async (pilihan: number) => {
    if (jawaban) return;
    try {
      const r = await kirim<Jawaban>("kuis/jawab",
        { sesi: sesi.sesi, nomor, pilihan });
      setJawaban(r);
      umumkan(r.benar ? "Benar." : "Belum tepat. " + (r.penjelasan || ""));
    } catch (e) {
      sorak((e as Error).message, "salah");
      onBatal();
    }
  }, [jawaban, sesi.sesi, nomor, onBatal]);

  const berikutnya = useCallback(() => {
    if (nomor + 1 >= sesi.total) { void selesai(false); return; }
    setNomor((n) => n + 1);
    setJawaban(null);
  }, [nomor, sesi.total, selesai]);

  /* Fokus mengikuti soal yang baru datang. Sesudah "Soal berikutnya" diklik,
     tombol itu sudah tidak ada di DOM dan fokus jatuh ke `<body>`: pembaca
     layar lalu membacakan ruang kosong, bukan pertanyaannya.

     `tabIndex={-1}` yang membuat sebuah `div` bisa menerima fokus sama sekali,
     dan `-1` (bukan `0`) menjaganya DI LUAR urutan Tab. `preventScroll`
     mengikuti konvensi rumah: memindahkan fokus tidak boleh sekaligus
     menggeser halaman. */
  useEffect(() => {
    soalRef.current?.focus({ preventScroll: true });
  }, [nomor]);

  useEffect(() => {
    if (jawaban) lanjutRef.current?.focus();
  }, [jawaban]);

  /* Pintasan angka dan huruf. Yang diperiksa medan masukan -- angka yang
     diketik di kotak teks adalah angka, bukan jawaban. */
  useEffect(() => {
    const saatTombol = (e: KeyboardEvent) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      const t = e.target as HTMLElement | null;
      if (t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA"
                || t.tagName === "SELECT")) return;
      if (jawaban) {
        if (e.key === "Enter") { e.preventDefault(); berikutnya(); }
        return;
      }
      const angka = parseInt(e.key, 10);
      const huruf = HURUF.indexOf(e.key.toUpperCase());
      const i = Number.isInteger(angka) && angka >= 1 ? angka - 1
        : huruf >= 0 ? huruf : -1;
      if (i >= 0 && i < s.options.length) {
        e.preventDefault();
        void jawab(i);
      }
    };
    document.addEventListener("keydown", saatTombol);
    return () => document.removeEventListener("keydown", saatTombol);
  }, [jawaban, berikutnya, jawab, s.options.length]);

  return (
    <>
      <div className="kuis-kemajuan">
        <span>{`${nomor + 1} / ${sesi.total}`}</span>
        <Bilah persen={(nomor / sesi.total) * 100} diam />
        <span className={"jam" + (sesi.durasi && sisaDetik <= 30 ? " menipis" : "")}>
          {sesi.durasi ? jamMundur(sisaDetik) : ""}
        </span>
        <button type="button" className="tbl tbl-kecil tbl-hantu"
                onClick={() => {
                  if (!globalThis.confirm(
                    "Hentikan kuis ini? Jawaban yang sudah masuk tidak akan "
                    + "dicatat.")) return;
                  kirim("kuis/batal", { sesi: sesi.sesi }).catch(() => {});
                  onBatal();
                }}>
          Hentikan
        </button>
      </div>

      <div>
        <div ref={soalRef} className="kuis-soal" tabIndex={-1}>
          <Berkode teks={s.q} />
        </div>
        <div className="opsi">
          {s.options.map((teks, i) => {
            /* Hurufnya dibungkus `<span>` sendiri supaya centang/silang bisa
               menggantikannya lewat `::after` saat jawabannya terungkap. Warna
               hijau dan merah saja tidak cukup untuk mata yang sulit
               membedakan keduanya, dan di layar ini dua warna itulah SELURUH
               umpan baliknya. */
            const kelas = !jawaban ? ""
              : i === jawaban.jawaban_benar ? " benar"
              : i === jawaban.pilihanmu ? " salah" : "";
            return (
              <button
                key={i}
                type="button"
                className={kelas.trim() || undefined}
                disabled={!!jawaban}
                onClick={() => { void jawab(i); }}
              >
                <span className="huruf"><span>{HURUF[i]}</span></span>
                <span><Berkode teks={teks} /></span>
              </button>
            );
          })}
        </div>

        {/* Penjelasannya berdiri TEPAT DI BAWAH daftar opsi. Di versi JS ia
            disisipkan di bawah opsi yang DIPILIH; di React opsi-opsinya sudah
            ditandai sendiri lewat kelas `.benar`/`.salah`, jadi jaraknya ke
            kegagalannya tetap pendek tanpa menyisipkan simpul di tengah
            daftar -- dan daftar yang tidak disisipi tetap satu daftar bagi
            pembaca layar. */}
        {jawaban ? (
          <div className="penjelasan">
            <b>{jawaban.benar ? "Benar. " : "Belum tepat. "}</b>
            <Berkode teks={jawaban.penjelasan
              || (jawaban.benar ? "" : "Jawaban yang benar disorot hijau.")} />
            <div className="deret" style={{ marginTop: "var(--s3)" }}>
              <button ref={lanjutRef} type="button" className="tbl tbl-utama"
                      onClick={berikutnya}>
                {nomor + 1 >= sesi.total ? "Lihat hasil" : "Soal berikutnya →"}
              </button>
            </div>
          </div>
        ) : (
          <p className="baris-sisi" style={{ marginTop: "var(--s4)" }}>
            {`Tekan 1-${s.options.length} atau A-${HURUF[s.options.length - 1]} `
              + "untuk menjawab."}
          </p>
        )}
      </div>
    </>
  );
}

/* ==================================================================== hasil */

function Hasil({
  r, kehabisanWaktu, b, kunciBahasa, onUlangi, onUlangiSalah,
}: {
  r: Rekap; kehabisanWaktu: boolean; b: DataBahasa; kunciBahasa: string;
  onUlangi: () => void; onUlangiSalah: () => void;
}) {
  const persen = r.total ? (r.benar / r.total) * 100 : 0;
  const sempurna = r.benar === r.total && r.total > 0;

  const kalimat = sempurna ? "Sempurna. Semua benar."
    : persen >= 80 ? "Bagus. Tinggal sedikit yang perlu dirapikan."
    : persen >= 50 ? "Separuh jalan. Baca ulang bagian yang salah, lalu "
                     + "ulangi soal itu saja."
    : "Ini tanda materinya belum menempel, dan itu wajar. Baca ulang "
      + "materinya dulu, jangan langsung mengulang kuisnya.";

  useEffect(() => {
    globalThis.scrollTo({ top: 0, behavior: "instant" });
  }, []);

  return (
    <div className="masuk">
      <header className="kepala-besar">
        <span className="mata">{kehabisanWaktu ? "Waktu habis" : "Hasil"}</span>
        <h1>{`${r.benar} dari ${r.total} benar`}</h1>
        <p className="kepala-sub">{kalimat}</p>
      </header>

      <div className="kartu" style={{ marginBottom: "var(--s5)" }}>
        <Bilah persen={persen} kelas={persen >= 100 ? "tumbuh" : undefined} />
        <div className="deret deret-rapat" style={{ marginTop: "var(--s3)" }}>
          {(r.xp_tambah || 0) > 0 ? (
            <span className="pil pil-nyala">{`+${r.xp_tambah} XP`}</span>
          ) : null}
          {r.sesi_penuh ? (
            <span className="pil">{`Terbaik ${r.terbaik}/${r.total_asli}`}</span>
          ) : null}
          {/* Pembanding dengan percobaan SEBELUMNYA -- bukan dengan rekor,
              yang sudah diurus pil di atas. Penyebutnya `total_asli`: pada mode
              ulangan `total` adalah jumlah soal yang diulang, dan membandingkan
              `benar` sebuah subset dengan skor penuh adalah membandingkan dua
              hal yang lain.

              Dua syarat, dan keduanya punya alasan yang sama pentingnya:
              `sesi_penuh`, karena sesi ulangan sengaja tidak menyentuh skor;
              dan `terakhir_sebelum !== null`, karena `null` berarti belum ada
              percobaan sebelumnya -- dan "naik dari 0" untuk orang yang baru
              pertama menyelesaikan kuis terbaca sebagai penghukuman. */}
          {r.sesi_penuh && r.terakhir_sebelum !== null ? (
            <span className="pil">
              {(r.benar > r.terakhir_sebelum ? "naik dari "
                : r.benar < r.terakhir_sebelum ? "sebelumnya "
                : "sama dengan ") + `${r.terakhir_sebelum}/${r.total_asli}`}
            </span>
          ) : null}
          {/* Percobaan PERTAMA tidak punya pembanding, dan diamnya layar di
              situ terbaca sebagai ketiadaan -- bukan sebagai permulaan. */}
          {r.sesi_penuh && r.terakhir_sebelum === null ? (
            <span className="pil">percobaan pertamamu</span>
          ) : null}
          <span className="pil">{`${Math.round(r.detik)} detik`}</span>
          {r.jadwal ? (
            <span className="pil pil-ungu">{jadwalRamah(r.jadwal)}</span>
          ) : null}
          {r.salah_tersisa ? (
            <span className="pil">{`${r.salah_tersisa} soal untuk diulang`}</span>
          ) : (
            <span className="pil pil-tumbuh">tidak ada soal tersisa</span>
          )}
        </div>
        {!r.sesi_penuh ? (
          <p className="baris-sisi" style={{ margin: "var(--s3) 0 0" }}>
            Ini sesi ulangan, jadi skor terbaikmu sengaja tidak disentuh.
          </p>
        ) : null}
      </div>

      {/* Tindakan berikutnya berdiri SEBELUM daftar tinjauan, bukan sesudahnya.
          Tinjauan lima belas soal bisa sepanjang dua layar penuh, dan tombol
          "Kerjakan lagi" yang tertimbun di dasarnya adalah tombol yang harus
          dicari -- padahal ia jawaban paling umum atas layar ini. */}
      <div className="deret" style={{ marginBottom: "var(--s6)" }}>
        <button type="button" className="tbl tbl-utama" onClick={onUlangi}>
          Kerjakan lagi
        </button>
        {r.salah_tersisa ? (
          <button type="button" className="tbl" onClick={onUlangiSalah}>
            {`Ulangi ${r.salah_tersisa} yang masih salah`}
          </button>
        ) : null}
        <a className="tbl tbl-hantu" href={"#/bahasa/" + kunciBahasa}>
          {"Kembali ke " + b.label}
        </a>
      </div>

      <span className="mata">Tinjau jawaban</span>
      <div style={{ display: "grid", gap: "var(--s2)" }}>
        {r.rincian.map((d, i) => {
          const punya = d.pilihanmu !== null && d.pilihanmu !== undefined;
          return (
            <div key={i} className={"uji " + (d.benar ? "lulus" : "gagal")}>
              <div className="uji-kepala">
                <span className="uji-cap">{d.benar ? "BENAR" : "SALAH"}</span>
                <span className="uji-nama">
                  {`${i + 1}. `}<Berkode teks={d.q} />
                </span>
              </div>
              {!d.benar ? (
                <div className="uji-badan">
                  <div style={{ fontSize: "var(--t-ui)" }}>
                    <div style={{ color: "var(--salah)" }}>
                      {"Jawabanmu: "}
                      {punya ? <Berkode teks={d.options[d.pilihanmu as number]
                        ?? ""} /> : "(tidak dijawab)"}
                    </div>
                    <div style={{ color: "var(--tumbuh)" }}>
                      {"Seharusnya: "}
                      <Berkode teks={d.options[d.jawaban_benar] ?? ""} />
                    </div>
                  </div>
                  {d.penjelasan ? (
                    <div className="arti">
                      <b>Kenapa</b>
                      <div><Berkode teks={d.penjelasan} /></div>
                    </div>
                  ) : null}
                  <BacaLagi d={d} kunciBahasa={kunciBahasa} />
                </div>
              ) : null}
            </div>
          );
        })}
      </div>
    </div>
  );
}

/* ==================================================================== layar */

type Tahap =
  | { t: "persiapan" }
  | { t: "sesi"; sesi: Sesi }
  | { t: "hasil"; r: Rekap; kehabisanWaktu: boolean };

export function Kuis({
  kunciBahasa, indeks, acakBawaan, onKonteks,
}: {
  kunciBahasa: string;
  indeks: number;
  /** Setelan "Acak bawaan" dari `/api/awal`. */
  acakBawaan: boolean;
  onKonteks: (k: Konteks | undefined) => void;
}) {
  const [b, setB] = useState<DataBahasa | null>(null);
  const [galat, setGalat] = useState("");
  const [tahap, setTahap] = useState<Tahap>({ t: "persiapan" });
  /* Setelan "Acak bawaan" ADA di Pengaturan dan berlaku di terminal, tapi layar
     ini dulu memakunya ke `true` -- jadi mematikannya mengubah persis NOL hal
     di browser. Setelan yang tampak berfungsi tapi tidak mengubah apa pun lebih
     buruk daripada setelan yang tidak ada. */
  const [acak, setAcak] = useState(acakBawaan);
  const [timer, setTimer] = useState(false);

  useEffect(() => {
    let dibatalkan = false;
    setB(null); setGalat(""); setTahap({ t: "persiapan" });
    (async () => {
      try {
        const d = await ambil<DataBahasa>("bahasa", { key: kunciBahasa });
        if (dibatalkan) return;
        const q = d.kuis[indeks];
        if (!q) { setGalat("Kuis tidak ditemukan."); return; }
        setB(d);
        onKonteks({
          balik: { label: d.label, href: "#/bahasa/" + kunciBahasa },
          bab: "Kuis",
          judul: q.judul,
          posisi: `${indeks + 1} / ${d.kuis.length}`,
          langkah: true,
          ...(indeks > 0 ? { sebelum: `#/kuis/${kunciBahasa}/${indeks - 1}` } : {}),
          ...(indeks + 1 < d.kuis.length
            ? { sesudah: `#/kuis/${kunciBahasa}/${indeks + 1}` } : {}),
        });
      } catch (e) {
        if (!dibatalkan) setGalat((e as Error).message);
      }
    })();
    return () => { dibatalkan = true; };
  }, [kunciBahasa, indeks, onKonteks]);

  const mulai = useCallback(async (mode: string) => {
    try {
      const s = await kirim<Sesi>("kuis/mulai",
        { key: kunciBahasa, indeks, mode, acak, timer });
      setTahap({ t: "sesi", sesi: s });
    } catch (e) {
      sorak((e as Error).message, "salah");
    }
  }, [kunciBahasa, indeks, acak, timer]);

  const saatSelesai = useCallback((r: Rekap, kehabisanWaktu: boolean) => {
    // `diam: true`: perayaan XP-nya sudah diwakili pil `+N XP` di kartu skor,
    // dan toast kedua di atasnya cuma mengulang angka yang sama.
    rayakan(r, { diam: true });
    setTahap({ t: "hasil", r, kehabisanWaktu });
  }, []);

  if (galat) {
    return <Keadaan jenis="salah" judul="Kuis tidak terbuka" ket={galat} />;
  }
  if (!b) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat kuis…</span>
      </div>
    );
  }
  const q = b.kuis[indeks] as ButirKuis;

  return (
    <div className="masuk">
      <div className="kuis-panggung">
        {tahap.t === "persiapan" ? (
          <Persiapan
            b={b} q={q} nomorKuis={indeks}
            acak={acak} timer={timer} setAcak={setAcak} setTimer={setTimer}
            onMulai={(mode) => { void mulai(mode); }}
          />
        ) : tahap.t === "sesi" ? (
          <SesiKuis
            sesi={tahap.sesi}
            onSelesai={saatSelesai}
            onBatal={() => setTahap({ t: "persiapan" })}
          />
        ) : (
          <Hasil
            r={tahap.r}
            kehabisanWaktu={tahap.kehabisanWaktu}
            b={b}
            kunciBahasa={kunciBahasa}
            onUlangi={() => setTahap({ t: "persiapan" })}
            onUlangiSalah={() => { void mulai("salah"); }}
          />
        )}
      </div>
    </div>
  );
}
