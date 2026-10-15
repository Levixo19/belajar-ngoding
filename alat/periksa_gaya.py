#!/usr/bin/env python3
"""Menghitung pola tulisan-AI di prosa materi. Alat ukur, bukan penilai.

    python3 alat/periksa_gaya.py                  # ringkasan per kurikulum
    python3 alat/periksa_gaya.py html             # per materi di satu kurikulum
    python3 alat/periksa_gaya.py html "1. Apa"    # temuan rinci satu materi

Yang dibaca hanya PROSA: badan materi diurai dengan isi.blok_badan, pengurai
yang sama dengan yang menggambar halaman web, lalu cuma blok teks, catatan,
dan butir daftar yang diperiksa. Contoh kode, diagram, dan tabel berkolom
tidak ikut, karena di sana huruf kapital dan tanda panah memang isinya.

Pola yang dihitung adalah yang dilarang alat/panduan_gaya.md. Angka nol
tidak berarti tulisannya bagus; ia cuma berarti tidak ada pola yang bisa
dikenali mesin. Kejelasan untuk pemula tetap harus dibaca manusia.
"""

import os
import re
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from main import LANGUAGES  # noqa: E402
from webapp import isi  # noqa: E402

# Singkatan dan nama yang memang ditulis kapital. Kata kapital lain di prosa
# dihitung sebagai penekanan berhuruf besar.
AKRONIM = set("""
HTML CSS JS DOM API URL URI HTTP HTTPS SQL JSON XML YAML CSV TSV CLI GUI IDE
JDK JRE JVM GCC CPU RAM ROM GPU SSD HDD USB OS PC UTF ASCII ANSI ISO RFC IETF
IEEE TCP UDP IP DNS SSH SSL TLS FTP SMTP MIME PDF PNG JPG JPEG SVG GIF WEBP
NULL TRUE FALSE AND OR NOT NaN EOF EOL LF CRLF PATH HOME PWD UID GID PID
OOP MVC CRUD REST UI UX AI ID URLS APIS SDK NPM PIP PEP ECMAScript ES TS
LINQ ASP NET MSDN WPF WASM RGB RGBA HSL HEX ARIA WCAG SEO CDN CORS XSS CSRF
DBMS RDBMS ACID ORM DDL DML DCL JOIN SELECT FROM WHERE INSERT UPDATE DELETE
CREATE TABLE DROP ALTER INDEX VIEW GROUP BY ORDER HAVING LIMIT INTO VALUES
SET PRIMARY KEY FOREIGN UNIQUE CHECK DEFAULT AUTO_INCREMENT INNER LEFT RIGHT
OUTER FULL CROSS UNION ALL DISTINCT AS ON IN IS LIKE BETWEEN EXISTS CASE WHEN
THEN ELSE END COUNT SUM AVG MIN MAX BEGIN COMMIT ROLLBACK TRANSACTION
GRANT REVOKE TRIGGER PROCEDURE FUNCTION RETURNS DECLARE IF WITH RECURSIVE
CTE NOSQL SQLITE MYSQL POSIX GNU BSD MIT GPL LTS RPM DNF YUM SELINUX GRUB
UEFI BIOS LVM RAID NFS SMB VPN LAN WAN NAT DHCP MAC IPV4 IPV6 CIDR ICMP
ARP HEAD GET POST PUT PATCH OPTIONS UTC GMT IO FIFO LIFO BFS DFS DP RNG
UUID SHA MD5 GPG PGP SSO JWT OAUTH CSP SRI MDN W3C WHATWG BEM SASS SCSS
LESS PX EM REM VW VH DPI FPS TODO FIXME README CMS PHP
ABC GIL REPL LEGB MRO EAFP LBYL TOML INI BOM RAII STL OK EDIT
INFO ERROR WARNING DEBUG CRITICAL FATAL TRACE FAILED PASSED XPASS XFAIL SKIP
DOTALL IGNORECASE MULTILINE VERBOSE ASCII UNICODE STDIN STDOUT STDERR
""".split())

POLA = [
    ("dash", re.compile(r"[—–]| -- ")),
    ("bukan-melainkan", re.compile(
        r"\bbukan\b[^.;:!?]{0,90}?\b(melainkan|tetapi|tapi)\b", re.I)),
    ("bukan-sekadar", re.compile(r"\bbukan (sekadar|cuma|hanya)\b", re.I)),
    ("penguat", re.compile(
        r"\b(sangat|benar-benar|sebenarnya|sesungguhnya|pada dasarnya|"
        r"tentu saja|jelas sekali|sungguh)\b", re.I)),
    ("pembuka-kosong", re.compile(
        r"\b(satu hal yang|perlu dicatat|yang perlu diingat|penting untuk "
        r"(dicatat|diingat|dipahami)|perlu diperhatikan|mari kita|ayo kita|"
        r"inilah|itulah sebabnya|itu sebabnya)\b", re.I)),
    ("puitis", re.compile(
        r"\b(membuka mata|kunci(nya)? (utama|sukses)|krusial|fundamental|"
        r"yang menang|berteriak|diam-diam|seluruh gunanya|katalog|"
        r"jantung(nya)?|senjata|ajaib|magis)\b", re.I)),
    ("tanya-retoris", re.compile(
        r"(\?\s+(Karena|Jawabannya|Sebab)\b)|^(Kenapa|Mengapa)( begitu| demikian)?\?$")),
]
KATA_KAPITAL = re.compile(r"\b[A-Z][A-Z\-]{2,}\b")
KALIMAT = re.compile(r"[^.!?]+[.!?]?")
PANJANG_KALIMAT = 30


def teks_prosa(body):
    """Daftar paragraf prosa (sudah disambung) dari satu body."""
    keluar = []

    def jelajah(blok):
        for b in blok:
            if b["jenis"] in ("teks", "catatan"):
                keluar.append(b["teks"])
            elif b["jenis"] == "daftar":
                for butir in b["butir"]:
                    keluar.append(butir["teks"])
                    jelajah(butir.get("blok") or [])
                    if butir.get("anak"):
                        # `anak` daftar bersarang: {"urut", "butir"} tanpa "jenis".
                        jelajah([{"jenis": "daftar", **butir["anak"]}])
    jelajah(isi.blok_badan(body))
    return keluar


def periksa_teks(paragraf):
    temuan = []
    for p in paragraf:
        for nama, pola in POLA:
            for m in pola.finditer(p):
                temuan.append((nama, m.group(0), p))
        for kata in KATA_KAPITAL.findall(p):
            if kata.strip("-") not in AKRONIM and re.search(r"[AIUEO]", kata):
                temuan.append(("kapital", kata, p))
        for k in KALIMAT.findall(p):
            if len(k.split()) > PANJANG_KALIMAT:
                temuan.append(("kalimat-panjang", f"{len(k.split())} kata", k))
    return temuan


def periksa_materi(m):
    paragraf = []
    for s in m["sections"]:
        paragraf += teks_prosa(s.get("body") or [])
    kata = sum(len(p.split()) for p in paragraf)
    return periksa_teks(paragraf), kata


def skor(temuan, kata):
    return round(1000 * len(temuan) / max(kata, 1), 1)


def main():
    args = sys.argv[1:]
    per_key = {l["key"]: l for l in LANGUAGES}
    if not args:
        total_t = total_k = 0
        print(f"{'kurikulum':12} {'kata':>7} {'temuan':>7} {'/1000':>6}")
        for l in LANGUAGES:
            t = k = 0
            for m in l["materials"]:
                tm, km = periksa_materi(m)
                t += len(tm)
                k += km
            total_t += t
            total_k += k
            print(f"{l['key']:12} {k:7} {t:7} {1000 * t / max(k, 1):6.1f}")
        print(f"{'TOTAL':12} {total_k:7} {total_t:7} {1000 * total_t / max(total_k, 1):6.1f}")
        return
    l = per_key[args[0]]
    if len(args) == 1:
        for m in l["materials"]:
            tm, km = periksa_materi(m)
            jenis = {}
            for n, _, _ in tm:
                jenis[n] = jenis.get(n, 0) + 1
            print(f"{skor(tm, km):6.1f}  {len(tm):3}  {m['title'][:46]:46} {jenis}")
        return
    for m in l["materials"]:
        if m["title"].startswith(args[1]):
            tm, km = periksa_materi(m)
            print(f"{m['title']}: {len(tm)} temuan, {km} kata, {skor(tm, km)}/1000")
            for nama, cocok, konteks in tm:
                print(f"  [{nama}] {cocok!r}  <- {konteks[:110]}")


if __name__ == "__main__":
    main()
