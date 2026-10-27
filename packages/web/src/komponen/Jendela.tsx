/** Dialog modal: tirai, jerat fokus, Escape, dan janji yang membawa nilainya.
 *
 *  Padanan `jendela()` dan `konfirmasi()` di `webapp/statik/js/inti.js`, dengan
 *  SATU penyimpangan yang sengaja. Versi JS memudarkan tirai dengan
 *  `fill: "forwards"`, jadi animasi itu menahan opacity 0 SELAMANYA dan harus
 *  dibatalkan saat dialog berikutnya dibuka -- kalau lupa, dialog baru berdiri
 *  di atas tirai tak terlihat. AGENTS.md mencatatnya sebagai bug yang sudah
 *  pernah terjadi, dan pemicunya ("Batal lalu buka dialog berikutnya") dipakai
 *  di Reset progres.
 *
 *  Di sini sumber masalahnya dibuang, bukan gejalanya ditambal: tirai keluar
 *  dengan `opacity: 0` dipasang lebih dulu sebagai keadaan ALAMI-nya, dan
 *  animasinya cuma berangkat dari `1`. Tanpa `forwards` tidak ada yang perlu
 *  dibatalkan. Itu persis aturan "keadaan akhir sebuah animasi harus sama
 *  dengan keadaan alami elemennya" di AGENTS.md. Penjaga `giliran`/
 *  `nomorJendela` ikut lenyap karena kehadiran tirai di sini TURUNAN state,
 *  bukan sesuatu yang dibersihkan callback animasi yang kebetulan menang.
 */

import { createContext, useCallback, useContext, useEffect, useMemo,
         useRef, useState } from "react";
import type { ReactNode } from "react";
import { createPortal } from "react-dom";
import { adaGerak } from "../gerak.ts";
import { bisaFokus } from "./fokus-dialog.ts";

export interface AksiJendela {
  label: string;
  /** Nilai yang dibawa janjinya. Bawaannya `true`. */
  nilai?: unknown;
  kelas?: string;
}

export interface PintaJendela {
  judul?: string;
  isi: ReactNode;
  aksi?: AksiJendela[];
  lebar?: boolean;
}

type Penjawab = (nilai: unknown) => void;

interface Tugas extends PintaJendela {
  id: number;
  jawab: Penjawab;
}

interface IsiKonteks {
  tanya: (pinta: PintaJendela) => Promise<unknown>;
  konfirmasi: (pesan: ReactNode, pilihan?: {
    judul?: string; labelYa?: string; bahaya?: boolean;
  }) => Promise<boolean>;
  adaJendela: boolean;
}

const Konteks = createContext<IsiKonteks | null>(null);

function Tirai({ tugas, tutup }: { tugas: Tugas; tutup: Penjawab }) {
  const tirai = useRef<HTMLDivElement>(null);
  const kotak = useRef<HTMLDivElement>(null);
  const sebelumnya = useRef<Element | null>(null);
  // Lihat `PembungkusModal`: seretan dari dalam kotak tidak boleh menutupnya.
  const mulaiDiTirai = useRef(false);

  // Fokus dikembalikan ke tempat asalnya. Tanpa ini pemakai papan ketik
  // mendarat di awal halaman setiap kali sebuah dialog ditutup.
  useEffect(() => {
    sebelumnya.current = document.activeElement;
    const el = kotak.current;
    if (el) {
      const awal = el.querySelector<HTMLElement>(
        "input, textarea, button.tbl-utama, button.tbl, [tabindex]");
      (awal ?? el).focus();
    }
    return () => {
      const asal = sebelumnya.current;
      if (asal instanceof HTMLElement) asal.focus();
    };
  }, []);

  // Escape menutup, Tab terjerat. Dipasang di fase CAPTURE supaya pintasan
  // papan ketik cangkang (Ctrl+K dkk.) tidak menang lebih dulu.
  useEffect(() => {
    const saatTombol = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        e.preventDefault();
        e.stopPropagation();
        tutup(null);
        return;
      }
      if (e.key !== "Tab" || !kotak.current) return;
      const bisa = bisaFokus(kotak.current);
      if (!bisa.length) return;
      const awal = bisa[0]!;
      const akhir = bisa[bisa.length - 1]!;
      if (e.shiftKey && document.activeElement === awal) {
        e.preventDefault();
        akhir.focus();
      } else if (!e.shiftKey && document.activeElement === akhir) {
        e.preventDefault();
        awal.focus();
      }
    };
    document.addEventListener("keydown", saatTombol, true);
    return () => document.removeEventListener("keydown", saatTombol, true);
  }, [tutup]);

  // Animasi MASUK saja. Keadaan alami tirai adalah opacity 1, jadi gerak yang
  // dimatikan atau animasi yang tidak pernah jalan tetap menampilkannya.
  useEffect(() => {
    if (!adaGerak()) return;
    tirai.current?.animate({ opacity: [0, 1] }, { duration: 160 });
    kotak.current?.animate(
      { opacity: [0, 1], transform: ["translateY(-14px) scale(.982)", "none"] },
      { duration: 220, easing: "cubic-bezier(.22,1,.36,1)" });
  }, []);

  return (
    <div
      id="tirai"
      ref={tirai}
      onPointerDown={(e) => { mulaiDiTirai.current = e.target === tirai.current; }}
      onClick={(e) => {
        if (mulaiDiTirai.current && e.target === tirai.current) tutup(null);
        mulaiDiTirai.current = false;
      }}
    >
      <div
        className={"jendela" + (tugas.lebar ? " jendela-lebar" : "")}
        ref={kotak}
        role="dialog"
        aria-modal="true"
        aria-label={tugas.judul || "Dialog"}
        tabIndex={-1}
      >
        {tugas.judul ? (
          <div className="jendela-kepala">
            <h2>{tugas.judul}</h2>
            <button
              className="ikon-tombol"
              onClick={() => tutup(null)}
              title="Tutup (Esc)"
              aria-label="Tutup"
            >
              ✕
            </button>
          </div>
        ) : null}
        <div className="jendela-badan">{tugas.isi}</div>
        {tugas.aksi?.length ? (
          <div className="jendela-kaki">
            {tugas.aksi.map((a, i) => (
              <button
                key={i}
                className={"tbl" + (a.kelas ? " " + a.kelas : "")}
                onClick={() => tutup(a.nilai !== undefined ? a.nilai : true)}
              >
                {a.label}
              </button>
            ))}
          </div>
        ) : null}
      </div>
    </div>
  );
}

/** Tirai untuk dialog yang isinya digambar sendiri (Bantuan, Palet, catatan,
 *  contoh solusi, banding, ubah catatan).
 *
 *  `.jendela` TIDAK punya posisi sendiri: yang menaruhnya di tengah layar
 *  adalah `#tirai { position: fixed }`. Dialog yang menulis `<div className=
 *  "jendela">` langsung tergambar inline (`position: static`) di tempat
 *  pemanggilnya: menimpa konten, merusak tata letak induknya, dan halaman di
 *  belakangnya tetap bisa digulir. Dibungkus di sini ia modal sungguhan,
 *  lewat portal ke `document.body` supaya leluhur bertransform tidak
 *  menjepit `position: fixed`; klik di luar kotak menutupnya.
 *
 *  Fokus, Escape, dan jerat Tab TIDAK diurus di sini: itu tugas
 *  `useFokusDialog` milik dialognya sendiri. Dialog yang cuma butuh
 *  pertanyaan dan tombol memakai `useJendela().tanya`. */
export function PembungkusModal({ onTutup, children }: {
  onTutup: () => void;
  children: ReactNode;
}) {
  const tirai = useRef<HTMLDivElement>(null);
  // Menutup hanya kalau tekanannya DIMULAI di tirai juga. Menyeret seleksi
  // teks dari dalam kotak catatan lalu melepasnya di atas tirai menghasilkan
  // `click` yang targetnya tirai, dan dulu itu menutup dialog serta membuang
  // teks yang sedang diketik.
  const mulaiDiTirai = useRef(false);
  return createPortal(
    <div
      id="tirai"
      ref={tirai}
      onPointerDown={(e) => { mulaiDiTirai.current = e.target === tirai.current; }}
      onClick={(e) => {
        if (mulaiDiTirai.current && e.target === tirai.current) onTutup();
        mulaiDiTirai.current = false;
      }}
    >
      {children}
    </div>,
    document.body,
  );
}

export function PenyediaJendela({ children }: { children: ReactNode }) {
  const [tugas, setTugas] = useState<Tugas | null>(null);
  const nomor = useRef(0);

  const tanya = useCallback((pinta: PintaJendela) => (
    new Promise<unknown>((jawab) => {
      setTugas({ ...pinta, id: ++nomor.current, jawab });
    })
  ), []);

  // Janjinya diselesaikan SEKARANG, bukan sesudah animasi keluar habis: yang
  // memanggil hampir selalu langsung mengirim sesuatu ke server, dan menahannya
  // 140 md demi animasi berarti membayar animasi itu dua kali.
  const tutup = useCallback((nilai: unknown) => {
    setTugas((kini) => {
      if (!kini) return null;
      kini.jawab(nilai);
      return null;
    });
  }, []);

  const konfirmasi = useCallback(async (pesan: ReactNode, pilihan: {
    judul?: string; labelYa?: string; bahaya?: boolean;
  } = {}) => {
    const n = await tanya({
      judul: pilihan.judul ?? "Yakin?",
      isi: <p style={{ margin: 0 }}>{pesan}</p>,
      aksi: [
        { label: "Batal", nilai: false },
        {
          label: pilihan.labelYa ?? "Ya, lanjutkan",
          nilai: true,
          kelas: pilihan.bahaya ? "tbl-bahaya" : "tbl-utama",
        },
      ],
    });
    return n === true;
  }, [tanya]);

  const nilai = useMemo<IsiKonteks>(
    () => ({ tanya, konfirmasi, adaJendela: tugas !== null }),
    [tanya, konfirmasi, tugas]);

  return (
    <Konteks.Provider value={nilai}>
      {children}
      {tugas
        ? createPortal(
            <Tirai key={tugas.id} tugas={tugas} tutup={tutup} />,
            document.body)
        : null}
    </Konteks.Provider>
  );
}

export function useJendela(): IsiKonteks {
  const k = useContext(Konteks);
  if (!k) throw new Error("useJendela di luar PenyediaJendela");
  return k;
}
