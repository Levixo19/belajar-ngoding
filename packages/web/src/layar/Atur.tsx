/* Layar Pengaturan. Port bagian `layarAtur` dari `layar-lain.js`.
 *
 * Satu pembagian yang dijaga apa adanya, dan ia yang menentukan seluruh bentuk
 * layar ini: **yang mengatur TAMPILAN disimpan di browser, yang mengatur
 * BELAJAR disimpan ke berkas.** Tema yang enak di satu mesin tidak harus sama
 * di mesin lain; target XP harian harus.
 *
 * Pilihan yang aktif ditandai TIGA hal: kelas `.terpilih` (garis aksen), satu
 * pil "dipakai" di dalam kartunya, dan `aria-pressed`. Warna saja tidak cukup
 * -- itu syarat WCAG 1.4.1, dan di halaman yang justru memuat tema kontras
 * tinggi, melanggarnya akan lucu sekaligus melelahkan.
 *
 * YANG BELUM DIPORT, dan dikatakan di layar alih-alih dihilangkan diam-diam:
 * suara, getar perangkat, dan pengingat istirahat mata (pemiliknya `suara.js`
 * dan `istirahat.js`), plus blok data dan blok bahaya (butuh dialog
 * konfirmasi). Setelan yang hilang tanpa penjelasan membuat orang mengira
 * fiturnya dibuang.
 */

import { useEffect, useRef, useState } from "react";

import { ambil, kirim } from "../api.ts";
import { adaGerak, tingkatGerak } from "../gerak.ts";
import { Keadaan } from "../komponen/Keadaan.tsx";
import {
  bacaTampilan,
  GERAK,
  TEMA,
  terapkanTampilan,
  type Tampilan,
} from "../lokal.ts";
import { sorak } from "../sorak.tsx";

const UKURAN: Array<[Tampilan["ukuran"], number]> = [
  ["kecil", 15],
  ["sedang", 16],
  ["besar", 18],
  ["sangat besar", 20],
];

interface Opsi {
  label: string;
  jenis: string;
  nilai: unknown;
  bawaan: unknown;
  pilihan: Array<{ nilai: string; label: string }>;
  minimum: number | null;
  maksimum: number | null;
  keterangan: string;
}

type Konfigurasi = Record<string, Opsi>;

interface Lokasi {
  progres: string;
  konfigurasi: string;
  catatan: string;
  kerja: string;
}

interface Awal {
  versi: string;
  versi_web: string;
  lokasi: Lokasi;
  batas: { waktu: number; memori_mb: number };
}

/** Kartu pilihan yang menandai keadaannya dengan tiga isyarat sekaligus. */
function KartuPilihan({
  nama,
  ket,
  aktif,
  onPilih,
}: {
  nama: string;
  ket: string;
  aktif: boolean;
  onPilih: (el: HTMLButtonElement) => void;
}) {
  return (
    <button
      type="button"
      className={"kartu kartu-rapat" + (aktif ? " terpilih" : "")}
      aria-pressed={aktif}
      style={{ textAlign: "left" }}
      onClick={(e) => onPilih(e.currentTarget)}
    >
      <div className="deret deret-rapat" style={{ marginBottom: "var(--s1)" }}>
        <b>{nama}</b>
        {aktif ? <span className="pil pil-nyala">dipakai</span> : null}
      </div>
      <span className="baris-sisi">{ket}</span>
    </button>
  );
}

function SakelarBaris({
  judul,
  ket,
  nyala,
  onUbah,
}: {
  judul: string;
  ket: string;
  nyala: boolean;
  onUbah: (v: boolean) => void;
}) {
  return (
    <button
      type="button"
      className={"sakelar" + (nyala ? " on" : "")}
      role="switch"
      aria-checked={nyala}
      onClick={() => onUbah(!nyala)}
    >
      <div className="isi">
        <b>{judul}</b>
        <span>{ket}</span>
      </div>
      <div className="knop" />
    </button>
  );
}

/** Medan teks yang mengirim HANYA kalau nilainya berubah.
 *
 *  Tanpa pembandingan itu, setiap `blur` mengirim satu permintaan -- termasuk
 *  blur yang terjadi karena orangnya cuma melihat-lihat lalu pindah fokus. */
function MedanTeks({
  opsi,
  label,
  ket,
  onSimpan,
}: {
  opsi: Opsi;
  label: string;
  ket?: string;
  onSimpan: (v: string) => void;
}) {
  const awal = String(opsi.nilai ?? "");
  const [nilai, setNilai] = useState(awal);
  const terakhir = useRef(awal);
  const kirimKalauBeda = () => {
    if (nilai !== terakhir.current) {
      terakhir.current = nilai;
      onSimpan(nilai);
    }
  };
  return (
    <div className="medan">
      <label>{label}</label>
      {ket ? <div className="ket">{ket}</div> : null}
      <input
        type="text"
        value={nilai}
        onChange={(e) => setNilai(e.target.value)}
        onBlur={kirimKalauBeda}
        onKeyDown={(e) => {
          if (e.key === "Enter") kirimKalauBeda();
        }}
      />
    </div>
  );
}

function MedanAngka({
  opsi,
  label,
  onSimpan,
}: {
  opsi: Opsi;
  label: string;
  onSimpan: (v: number) => void;
}) {
  const awal = String(opsi.nilai ?? "");
  const [nilai, setNilai] = useState(awal);
  const terakhir = useRef(awal);
  const kirimKalauBeda = () => {
    if (nilai !== terakhir.current) {
      terakhir.current = nilai;
      onSimpan(Number(nilai));
    }
  };
  return (
    <div className="medan">
      <label>{label}</label>
      {opsi.keterangan ? <div className="ket">{opsi.keterangan}</div> : null}
      <input
        type="number"
        value={nilai}
        min={opsi.minimum ?? undefined}
        max={opsi.maksimum ?? undefined}
        onChange={(e) => setNilai(e.target.value)}
        onBlur={kirimKalauBeda}
      />
    </div>
  );
}

function MedanPilihan({
  opsi,
  label,
  onSimpan,
}: {
  opsi: Opsi;
  label: string;
  onSimpan: (v: string) => void;
}) {
  return (
    <div className="medan">
      <label>{label}</label>
      {opsi.keterangan ? <div className="ket">{opsi.keterangan}</div> : null}
      <select
        aria-label={label}
        defaultValue={String(opsi.nilai ?? "")}
        onChange={(e) => onSimpan(e.target.value)}
      >
        {opsi.pilihan.map((x) => (
          <option key={x.nilai} value={x.nilai}>
            {x.label}
          </option>
        ))}
      </select>
    </div>
  );
}

function BarisBerkas({ label, jalur }: { label: string; jalur: string }) {
  return (
    <div className="alat-baris">
      <b>{label}</b>
      <code>{jalur}</code>
    </div>
  );
}

export function Atur() {
  const [konfig, setKonfig] = useState<Konfigurasi | null>(null);
  const [awal, setAwal] = useState<Awal | null>(null);
  const [galat, setGalat] = useState<string | null>(null);
  const [tampilan, setTampilan] = useState<Tampilan>(bacaTampilan);

  useEffect(() => {
    let dibatalkan = false;
    Promise.all([ambil<Konfigurasi>("konfigurasi"), ambil<Awal>("awal")])
      .then(([k, a]) => {
        if (dibatalkan) return;
        setKonfig(k);
        setAwal(a);
      })
      .catch((e: Error) => {
        if (!dibatalkan) setGalat(e.message);
      });
    return () => {
      dibatalkan = true;
    };
  }, []);

  async function simpanKonfig(kunci: string, nilai: unknown) {
    try {
      const r = await kirim<{ konfigurasi?: Konfigurasi }>("konfigurasi", {
        [kunci]: nilai,
      });
      if (r.konfigurasi) setKonfig(r.konfigurasi);
      sorak("Tersimpan.", "tumbuh", 1.6);
    } catch (e) {
      sorak((e as Error).message, "salah");
    }
  }

  function gantiTema(nilai: Tampilan["tema"]) {
    // Warna seluruh halaman berganti dalam satu frame. Kelas `alih-tema`
    // memberinya transisi 260 md supaya yang terjadi terbaca sebagai
    // pergantian, bukan kedipan.
    if (adaGerak()) {
      document.documentElement.classList.add("alih-tema");
      setTimeout(
        () => document.documentElement.classList.remove("alih-tema"),
        320,
      );
    }
    setTampilan(terapkanTampilan({ tema: nilai }));
  }

  if (galat) {
    return <Keadaan jenis="salah" judul="Gagal memuat pengaturan" ket={galat} />;
  }
  if (!konfig || !awal) {
    return (
      <div className="deret">
        <div className="pusaran" />
        <span>Memuat pengaturan…</span>
      </div>
    );
  }

  // Sistem yang menyetel "kurangi gerak" membuat pilihan di sini tak berarti.
  // Katakan itu terus terang alih-alih membiarkan kartunya tampak berfungsi.
  const ditahanSistem = tingkatGerak() === "mati" && tampilan.gerak !== "mati";

  const opsi = (k: string): Opsi | null => konfig[k] ?? null;

  return (
    <div className="masuk-urut">
      <header className="kepala">
        <span className="mata">Sesuaikan</span>
        <h1>Pengaturan</h1>
        <p className="kepala-sub">
          Yang mengatur TAMPILAN disimpan di browser ini saja. Yang mengatur
          BELAJAR disimpan ke berkas.
        </p>
      </header>

      <section>
        <span className="mata">Tampilan, hanya untuk browser ini</span>
        <div className="kartu">
          <div className="medan">
            <label>Tema warna</label>
            <div className="petak petak-2">
              {TEMA.map(([nilai, nama, ket]) => (
                <KartuPilihan
                  key={nilai}
                  nama={nama}
                  ket={ket}
                  aktif={tampilan.tema === nilai}
                  onPilih={() => gantiTema(nilai)}
                />
              ))}
            </div>
          </div>

          <div className="medan">
            <label>Ukuran huruf</label>
            <div className="deret deret-rapat">
              {UKURAN.map(([nilai, px]) => {
                const aktif = tampilan.ukuran === nilai;
                return (
                  <button
                    key={nilai}
                    type="button"
                    className={
                      "tbl tbl-kecil " + (aktif ? "tbl-pilih" : "tbl-hantu")
                    }
                    aria-pressed={aktif}
                    onClick={() =>
                      setTampilan(terapkanTampilan({ ukuran: nilai }))
                    }
                  >
                    {`${nilai} · ${px}px`}
                  </button>
                );
              })}
            </div>
          </div>

          <div className="medan">
            <label htmlFor="atur-lebar">
              {`Lebar kolom baca: ${tampilan.lebarBaca} karakter`}
            </label>
            <div className="ket">
              Baris yang terlalu panjang membuat mata kehilangan awal baris
              berikutnya. 60-75 karakter biasanya paling nyaman.
            </div>
            <input
              id="atur-lebar"
              type="range"
              min={50}
              max={100}
              value={tampilan.lebarBaca}
              onChange={(e) =>
                setTampilan(
                  terapkanTampilan({ lebarBaca: Number(e.target.value) }),
                )
              }
            />
          </div>

          <div className="medan">
            <label>Gerak</label>
            <div className="ket">
              Setelan sistem “kurangi gerak” selalu menang atas pilihan di sini:
              kalau sistemmu sudah memintanya, tidak ada yang bergerak apa pun
              yang kamu pilih.
            </div>
            <div className="petak petak-3">
              {GERAK.map(([nilai, nama, ket]) => (
                <KartuPilihan
                  key={nilai}
                  nama={nama}
                  ket={ket}
                  aktif={tampilan.gerak === nilai}
                  onPilih={(el) => {
                    setTampilan(terapkanTampilan({ gerak: nilai }));
                    // Peragaan dijalankan SESUDAH tingkatnya dipasang, jadi
                    // yang terlihat memang gerakan pada tingkat yang barusan
                    // dipilih. "Mati" memang diam, dan diam tidak bisa
                    // dibedakan dari rusak -- jadi ia dikatakan dengan kata.
                    if (nilai === "mati") {
                      sorak("Gerak dimatikan.", "", 1.6);
                    } else if (adaGerak()) {
                      el.animate(
                        { transform: ["none", "scale(.975)", "none"] },
                        { duration: 320, easing: "cubic-bezier(.32,.72,.36,1)" },
                      );
                    }
                  }}
                />
              ))}
            </div>
            {ditahanSistem ? (
              <Keadaan
                jenis="kunci"
                judul="Sedang ditahan sistem"
                ket="Sistem operasimu menyetel “kurangi gerak”, jadi gerak tetap mati sampai setelan itu diubah."
              />
            ) : null}
          </div>

          <div className="medan">
            {/* Suara, getar, dan pengingat istirahat mata pemiliknya
                `suara.js` dan `istirahat.js`, dan keduanya belum diport.
                Membuat pembaca KEDUA untuk kunci localStorage yang sama akan
                membuat nilai rusak jatuh ke bawaan yang berbeda tergantung
                siapa yang membacanya lebih dulu. */}
            <Keadaan
              judul="Suara, getar, dan istirahat mata masih di antarmuka lama"
              ket={
                "Ketiganya dikendalikan modul tersendiri yang belum diport. " +
                "Setelannya tetap berlaku di antarmuka ini karena tersimpan di " +
                "browser yang sama; yang belum ada cuma saklarnya di halaman ini."
              }
            />
          </div>
        </div>
      </section>

      <section>
        <span className="mata">Belajar, berlaku juga di antarmuka lama</span>
        <div className="kartu" style={{ display: "grid", gap: "var(--s1)" }}>
          {/* Berdiri PALING ATAS, dan itu disengaja: dua layar lain
              menjanjikannya dengan kalimat "buka semua bab di Pengaturan",
              jadi orang yang tiba di sini datang untuk satu saklar tertentu.
              Menaruhnya di tengah daftar berarti menyuruh mereka mencari
              sesuatu yang baru saja dijanjikan. */}
          {opsi("buka_semua_bab") ? (
            <SakelarBaris
              judul={opsi("buka_semua_bab")!.label}
              ket={opsi("buka_semua_bab")!.keterangan}
              nyala={Boolean(opsi("buka_semua_bab")!.nilai)}
              onUbah={(v) => simpanKonfig("buka_semua_bab", v)}
            />
          ) : null}
          <div style={{ height: "var(--s2)" }} />
          {opsi("nama") ? (
            <MedanTeks
              opsi={opsi("nama")!}
              label="Nama panggilan"
              ket="Dipakai untuk menyapamu di dasbor. Boleh dikosongkan."
              onSimpan={(v) => simpanKonfig("nama", v)}
            />
          ) : null}
          {opsi("tujuan_karier") ? (
            <MedanPilihan
              opsi={opsi("tujuan_karier")!}
              label="Profesi tujuan"
              onSimpan={(v) => simpanKonfig("tujuan_karier", v)}
            />
          ) : null}
          {opsi("target_xp_harian") ? (
            <MedanAngka
              opsi={opsi("target_xp_harian")!}
              label="Target XP harian"
              onSimpan={(v) => simpanKonfig("target_xp_harian", v)}
            />
          ) : null}
          {opsi("detik_per_soal") ? (
            <MedanAngka
              opsi={opsi("detik_per_soal")!}
              label="Detik per soal saat mode timer"
              onSimpan={(v) => simpanKonfig("detik_per_soal", v)}
            />
          ) : null}
          {opsi("acak_bawaan") ? (
            <SakelarBaris
              judul={opsi("acak_bawaan")!.label}
              ket={opsi("acak_bawaan")!.keterangan}
              nyala={Boolean(opsi("acak_bawaan")!.nilai)}
              onUbah={(v) => simpanKonfig("acak_bawaan", v)}
            />
          ) : null}
          <div style={{ height: "var(--s2)" }} />
          {opsi("konfirmasi_jawaban") ? (
            <SakelarBaris
              judul={opsi("konfirmasi_jawaban")!.label}
              ket={opsi("konfirmasi_jawaban")!.keterangan}
              nyala={Boolean(opsi("konfirmasi_jawaban")!.nilai)}
              onUbah={(v) => simpanKonfig("konfirmasi_jawaban", v)}
            />
          ) : null}
        </div>
      </section>

      <section>
        <span className="mata">Letak berkas</span>
        <div className="kartu" style={{ display: "grid", gap: "var(--s2)" }}>
          <BarisBerkas label="Progres belajar" jalur={awal.lokasi.progres} />
          <BarisBerkas label="Pengaturan" jalur={awal.lokasi.konfigurasi} />
          <BarisBerkas label="Catatan pribadi" jalur={awal.lokasi.catatan} />
          <BarisBerkas label="Kode jawabanmu" jalur={awal.lokasi.kerja} />
        </div>
      </section>

      <section>
        <span className="mata">Data belajarmu</span>
        <Keadaan
          judul="Masih di antarmuka lama"
          ket={
            "Laporan kemajuan, ekspor, impor, cadangkan, dan reset progres " +
            "belum diport karena semuanya butuh dialog konfirmasi. Reset " +
            "progres khususnya TIDAK akan dipasang tanpa dialognya: ia " +
            "menghapus catatan belajar sungguhan, dan tombol semacam itu tidak " +
            "boleh pernah bisa ditekan karena salah sasaran."
          }
        />
      </section>

      <section>
        <span className="mata">Tentang</span>
        <div className="kartu">
          <p>
            {`belajar-codingV2 versi ${awal.versi} (antarmuka web ${awal.versi_web}). ` +
              "Tanpa dependensi luar: cukup Python 3.8+ dan sebuah browser."}
          </p>
          <p className="baris-sisi" style={{ margin: 0 }}>
            {`Kode yang kamu jalankan dibatasi ${awal.batas.waktu} detik dan ` +
              `${awal.batas.memori_mb} MB memori. Ini bukan sandbox keamanan: ` +
              "kode berjalan dengan hak akses yang sama denganmu, jadi jangan " +
              "menjalankan kode dari sumber yang tidak kamu percaya."}
          </p>
        </div>
      </section>
    </div>
  );
}
