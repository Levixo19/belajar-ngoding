#!/usr/bin/env python3
"""Memanen tautan belajar dari repo kurasi menjadi data Pustaka.

    python3 alat/panen_pustaka.py /home/vi/folder_materi/materi-belajar

Hasilnya satu berkas JSON per sumber di `data/pustaka/`, ditulis ulang utuh
setiap kali skrip ini jalan. Berkas itu DIHASILKAN, bukan diketik: kalau ada
yang salah, perbaiki pengurai di sini lalu jalankan ulang -- jangan menyunting
JSON-nya dengan tangan, karena panen berikutnya akan menimpanya diam-diam.

Hanya stdlib. Aplikasi ini tidak punya dependensi, dan alat pembangun datanya
pun tidak boleh jadi pengecualian.

LISENSI menentukan apa yang boleh diambil, bukan selera. Tabelnya di
`SUMBER` di bawah, dan aturannya dua:

  * Menautkan selalu sah; MENYALIN tunduk pada lisensi. Repo tanpa lisensi
    (getting-a-gig, build-your-own-x) dan repo proprietary (developer-roadmap)
    tidak disalin daftarnya. Yang masuk cuma tautan ke situs atau repo itu
    sendiri, dengan keterangan yang ditulis di sini.
  * Isi kurikulum freeCodeCamp berhak cipta freeCodeCamp.org (README repo
    itu sendiri yang menyatakannya; lisensi BSD-3 cuma untuk kodenya). Yang
    masuk hanya tautan ke halaman sertifikasinya.

coding-interview-university berlisensi CC BY-SA 4.0. Daftar tautannya ditaruh
di berkasnya SENDIRI yang ikut berlisensi CC BY-SA 4.0, terpisah dari data
lain, supaya ShareAlike-nya tidak menular ke seluruh aplikasi.
"""

import importlib.util
import json
import os
import re
import subprocess
import sys
from urllib.parse import urlsplit

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KELUAR = os.path.join(AKAR, "data", "pustaka")

# URL boleh memuat SATU tingkat kurung bersarang (ada tiga kasus nyata,
# misalnya artikel Wikipedia "..._(computer_science)").
URL = re.compile(r"https?://(?:[^\s()<>]|\([^\s()<>]*\))+")
JUDUL_BUTIR = re.compile(r"^(\s*)[*-]\s+(.*)$")
# Pagar penutup heading ("## Judul ##") wajib didahului spasi. Tanpa syarat
# itu "### C#" kehilangan pagarnya sendiri dan jadi topik "C".
KEPALA = re.compile(r"^(#{1,6})\s+(.*?)(?:\s+#+)?\s*$")
JANGKAR_HTML = re.compile(r"<a\s+[^>]*>\s*</a>|<a\s+[^>]*>|</a>", re.I)
TAUTAN_MD = re.compile(r"\[([^\]]*)\]\([^)]*\)")

# Heading yang isinya daftar isi, catatan kontribusi, atau lisensi -- bukan
# bahan belajar. Dicocokkan pada heading yang sudah dikecilkan.
KEPALA_LEWATI = {
    "index", "contents", "table of contents", "daftar isi", "license",
    "lisensi", "contributing", "contribution", "contributors", "sponsors",
    "sponsor", "footnotes", "credits", "related", "related lists",
    "license and copyright", "contact info", "contribute",
    "how to contribute", "translations", "translation",
}

SUMBER = {
    "fpb": {
        "nama": "free-programming-books",
        "pemilik": "EbookFoundation",
        "repo": "https://github.com/EbookFoundation/free-programming-books",
        "lisensi": "CC BY 4.0",
        "atribusi": ("Daftar dari free-programming-books oleh EbookFoundation "
                     "dan kontributornya, CC BY 4.0. Disaring ke bahasa "
                     "Indonesia dan Inggris, dikelompokkan ulang."),
        "folder": "01-free-programming-books",
    },
    "proyek": {
        "nama": "project-based-learning",
        "pemilik": "practical-tutorials",
        "repo": "https://github.com/practical-tutorials/project-based-learning",
        "lisensi": "MIT",
        "atribusi": ("Daftar dari project-based-learning, Copyright (c) 2021 "
                     "practical-tutorials, lisensi MIT."),
        "folder": "02-project-based-learning",
    },
    "awesome": {
        "nama": "awesome",
        "pemilik": "Sindre Sorhus",
        "repo": "https://github.com/sindresorhus/awesome",
        "lisensi": "CC0 1.0",
        "atribusi": "Daftar dari awesome oleh Sindre Sorhus, CC0 1.0.",
        "folder": "05-awesome",
    },
    "api": {
        "nama": "public-apis",
        "pemilik": "public-apis",
        "repo": "https://github.com/public-apis/public-apis",
        "lisensi": "MIT",
        "atribusi": ("Katalog dari public-apis, Copyright (c) 2022 "
                     "public-apis, lisensi MIT."),
        "folder": "06-public-apis",
    },
    "fcc": {
        "nama": "freeCodeCamp",
        "pemilik": "freeCodeCamp.org",
        "repo": "https://www.freecodecamp.org/learn",
        "lisensi": "tautan saja",
        "atribusi": ("Tautan ke sertifikasi gratis freeCodeCamp.org. Isi "
                     "kurikulumnya berhak cipta freeCodeCamp.org dan tidak "
                     "disalin. Tidak ada dukungan resmi dari freeCodeCamp."),
        "folder": "07-freeCodeCamp",
    },
    "desain": {
        "nama": "system-design-primer",
        "pemilik": "Donne Martin",
        "repo": "https://github.com/donnemartin/system-design-primer",
        "lisensi": "CC BY 4.0",
        "atribusi": ("Bacaan dari The System Design Primer oleh Donne Martin, "
                     "CC BY 4.0."),
        "folder": "08-system-design-primer",
    },
    "peta": {
        "nama": "roadmap.sh",
        "pemilik": "roadmap.sh",
        "repo": "https://roadmap.sh",
        "lisensi": "tautan saja",
        "atribusi": ("Tautan ke peta belajar di roadmap.sh. Isinya hak cipta "
                     "roadmap.sh dan tidak disalin; lisensinya hanya "
                     "mengizinkan membagikan tautan."),
        "folder": "09-developer-roadmap",
    },
    "ciu": {
        "nama": "coding-interview-university",
        "pemilik": "John Washam",
        "repo": "https://github.com/jwasham/coding-interview-university",
        "lisensi": "CC BY-SA 4.0",
        "atribusi": ("Daftar dari Coding Interview University oleh John Washam "
                     "dan kontributornya, CC BY-SA 4.0. Berkas data ini, "
                     "sebagai turunannya, juga berlisensi CC BY-SA 4.0."),
        "folder": "10-coding-interview-university",
    },
    "python": {
        "nama": "awesome-python",
        "pemilik": "Vinta Chen",
        "repo": "https://github.com/vinta/awesome-python",
        "lisensi": "CC BY 4.0",
        "atribusi": "Daftar dari awesome-python oleh Vinta Chen, CC BY 4.0.",
        "folder": "11-awesome-python",
    },
    "rujukan": {
        "nama": "Repo tanpa lisensi terbuka",
        "pemilik": "-",
        "repo": "",
        "lisensi": "tautan saja",
        "atribusi": ("Dua repo yang tidak mencantumkan lisensi, sehingga "
                     "isinya hak cipta penuh penulisnya. Hanya tautan ke "
                     "repo itu sendiri yang dicantumkan."),
        "folder": None,
    },
}

# Berkas free-programming-books yang dipanen: hanya Indonesia dan Inggris,
# karena dua bahasa itulah yang bisa dibaca pelajar aplikasi ini.
FPB_BERKAS = [
    ("books/free-programming-books-id.md", "buku", "id"),
    ("books/free-programming-books-langs.md", "buku", "en"),
    ("books/free-programming-books-subjects.md", "buku", "en"),
    ("courses/free-courses-id.md", "kursus", "id"),
    ("courses/free-courses-en.md", "kursus", "en"),
    ("casts/free-podcasts-screencasts-id.md", "podcast", "id"),
    ("casts/free-podcasts-screencasts-en.md", "podcast", "en"),
    ("more/free-programming-interactive-tutorials-en.md", "tutorial", "en"),
    ("more/free-programming-cheatsheets.md", "contekan", "en"),
    ("more/free-programming-playgrounds.md", "playground", "en"),
    ("more/problem-sets-competitive-programming.md", "soal", "en"),
]

# Nama yang dirapikan untuk peta roadmap.sh. Yang tidak ada di sini memakai
# slug-nya sendiri dengan huruf besar di awal kata -- nama itu FAKTA (alamat
# halaman), bukan isi roadmap-nya.
NAMA_PETA = {
    "ai-engineer": "AI Engineer", "ai-data-scientist": "AI & Data Scientist",
    "api-design": "API Design", "aspnet-core": "ASP.NET Core", "aws": "AWS",
    "bi-analyst": "BI Analyst", "cpp": "C++", "css": "CSS", "devops": "DevOps",
    "devsecops": "DevSecOps", "graphql": "GraphQL", "html": "HTML",
    "ios": "iOS", "javascript": "JavaScript", "mlops": "MLOps",
    "mongodb": "MongoDB", "nodejs": "Node.js", "php": "PHP",
    "postgresql-dba": "PostgreSQL DBA", "qa": "QA", "react": "React",
    "react-native": "React Native", "sql": "SQL", "typescript": "TypeScript",
    "ux-design": "UX Design", "vue": "Vue", "nextjs": "Next.js",
    "ai-agents": "AI Agents", "ai-red-teaming": "AI Red Teaming",
    "ai-product-builder": "AI Product Builder", "claude-code": "Claude Code",
    "golang": "Go", "git-github": "Git & GitHub", "linux": "Linux",
    "full-stack": "Full Stack", "data-engineer": "Data Engineer",
    "cyber-security": "Cyber Security", "system-design": "System Design",
    "software-design-architecture": "Software Design & Architecture",
    "computer-science": "Computer Science", "code-review": "Code Review",
    "datastructures-and-algorithms": "Data Structures & Algorithms",
    "prompt-engineering": "Prompt Engineering", "shell-bash": "Shell / Bash",
    "spring-boot": "Spring Boot", "kubernetes": "Kubernetes",
    "docker": "Docker", "terraform": "Terraform", "flutter": "Flutter",
    "kotlin": "Kotlin", "rust": "Rust", "java": "Java", "python": "Python",
    "angular": "Angular", "android": "Android", "backend": "Backend",
    "frontend": "Frontend", "redis": "Redis", "cloudflare": "Cloudflare",
    "blockchain": "Blockchain", "game-developer": "Game Developer",
    "server-side-game-developer": "Server Side Game Developer",
    "technical-writer": "Technical Writer", "devrel": "DevRel",
    "product-manager": "Product Manager",
    "engineering-manager": "Engineering Manager",
    "software-architect": "Software Architect",
    "network-engineer": "Network Engineer", "data-analyst": "Data Analyst",
    "machine-learning": "Machine Learning",
    "backend-beginner": "Backend (pemula)", "frontend-beginner": "Frontend (pemula)",
    "devops-beginner": "DevOps (pemula)",
    "full-stack-beginner": "Full Stack (pemula)", "laravel": "Laravel",
    "django": "Django", "wordpress": "WordPress",
    "elasticsearch": "Elasticsearch", "kafka": "Kafka", "openai": "OpenAI",
}


# ------------------------------------------------------------- utilitas teks

def _rapikan(teks):
    teks = teks.replace(" ", " ")
    teks = JANGKAR_HTML.sub("", teks)
    for lolos in ("\\|", "\\#", "\\[", "\\]", "\\_", "\\*", "\\(", "\\)", "\\`"):
        teks = teks.replace(lolos, lolos[1])
    return re.sub(r"\s+", " ", teks).strip()


def _slug(teks):
    """Jangkar ala GitHub, sama dengan yang dipakai daftar isi repo-repo ini."""
    s = _rapikan(teks).lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s", "-", s.strip())


def _ambil_tautan(teks):
    """'[judul](url) sisa' -> (judul, url, sisa), atau None.

    Kurung siku dihitung berimbang: ada judul yang memuat [..] tanpa escape,
    dan `[^\\]]+` akan memotongnya di tengah.
    """
    if not teks.startswith("["):
        return None
    dalam = 0
    sebelumnya = ""
    for i, ch in enumerate(teks):
        if sebelumnya == "\\":
            sebelumnya = ""
            continue
        sebelumnya = ch
        if ch == "[":
            dalam += 1
        elif ch == "]":
            dalam -= 1
            if dalam == 0:
                break
    else:
        return None
    judul = teks[1:i]
    sisa = teks[i + 1:]
    if not sisa.startswith("("):
        return None
    awal = 1
    while awal < len(sisa) and sisa[awal] == " ":
        awal += 1       # "( http..." -- spasi nyasar setelah kurung buka
    m = URL.match(sisa, awal)
    if not m:
        return None
    ujung = m.end()
    while ujung < len(sisa) and sisa[ujung] == " ":
        ujung += 1
    if ujung >= len(sisa) or sisa[ujung] != ")":
        return None
    judul = _rapikan(TAUTAN_MD.sub(r"\1", judul)).replace("**", "").replace("`", "")
    return judul, m.group(0), sisa[ujung + 1:]


def _catatan(sisa):
    sisa = TAUTAN_MD.sub(r"\1", sisa)
    sisa = re.sub(r":[a-z0-9_+-]+:", "", sisa)               # :construction:
    sisa = re.sub(r"(?<!\w)(\*\*|\*|__|_)(\S.*?\S|\S)\1(?!\w)", r"\2", sisa)
    # Sisa bintang yang tidak berpasangan ("*(RedGate)", "(*in process)*"):
    # di catatan tidak ada bintang yang bermakna, jadi semuanya dibuang.
    sisa = sisa.replace("`", "").replace("*", "")
    sisa = re.sub(r"\(\s+", "(", sisa)
    sisa = re.sub(r"\s+\)", ")", sisa)
    sisa = _rapikan(sisa)
    sisa = re.sub(r"^[-–:,]\s*", "", sisa)
    if len(sisa) > 220:
        sisa = sisa[:217].rstrip() + "..."
    return sisa


def _kunci_url(url):
    p = urlsplit(url.strip())
    path = p.path.rstrip("/") if p.path not in ("", "/") else ""
    return "|".join((p.scheme.lower(), p.netloc.lower(), path, p.query))


# ------------------------------------------------------- pengurai markdown

def _peta_daftar_isi(baris):
    """Jangkar -> jalur topik, diambil dari blok daftar isi ('Index').

    Hierarki topik TIDAK boleh disimpulkan dari tingkat heading: di
    free-courses-en.md, Astro dan Nest.js ditulis sejajar JavaScript padahal
    maksudnya anak JavaScript. Daftar isinya yang benar.
    """
    peta = {}
    tumpukan = []
    di_isi = False
    for b in baris:
        k = KEPALA.match(b)
        if k:
            nama = _rapikan(k.group(2)).lower().rstrip(":")
            if nama in ("index", "contents", "table of contents", "daftar isi"):
                di_isi = True
                continue
            if di_isi and peta:
                break
            continue
        if not di_isi:
            continue
        m = re.match(r"^(\s*)[*-]\s+\[(.+?)\]\(#([^)]+)\)", b)
        if not m:
            continue
        tingkat = len(m.group(1).replace("\t", "    ")) // 2
        nama = _rapikan(m.group(2))
        while tumpukan and tumpukan[-1][0] >= tingkat:
            tumpukan.pop()
        tumpukan.append((tingkat, nama))
        peta[m.group(3).lower()] = [n for _, n in tumpukan]
    return peta


def urai_daftar(teks, jenis, bahasa, tingkat_awal=2, pakai_isi=True,
                lewati_sebelum=None):
    """Butir '* [judul](url) ...' di bawah heading -> entri.

    `tingkat_awal`: heading paling atas yang dianggap topik. Heading di atasnya
    (judul berkas) diabaikan.
    """
    baris = teks.splitlines()
    peta = _peta_daftar_isi(baris) if pakai_isi else {}
    jalur = []          # [(tingkat, nama)]
    lewati = False
    mulai = lewati_sebelum is None
    hasil = []
    rusak = []
    # GitHub membedakan jangkar kembar dengan akhiran -1, -2, ... menurut
    # urutan munculnya. "C" dan "C++" sama-sama berjangkar "c"; tanpa
    # penghitung ini seluruh buku C++ tercatat sebagai buku C.
    slug_terlihat = {}
    for nomor, b in enumerate(baris, 1):
        if not mulai:
            if re.match(lewati_sebelum, b):
                mulai = True
            else:
                continue
        k = KEPALA.match(b)
        if k:
            tingkat = len(k.group(1))
            nama = _rapikan(k.group(2))
            lewati = nama.lower().rstrip(":") in KEPALA_LEWATI
            if tingkat < tingkat_awal:
                jalur = []
                continue
            if lewati:
                jalur = [(t, n) for t, n in jalur if t < tingkat]
                continue
            dasar = _slug(nama)
            ke = slug_terlihat.get(dasar, 0)
            slug_terlihat[dasar] = ke + 1
            # Heading boleh menamai jangkarnya sendiri: '<a id="cpp"></a>C++'.
            # Kalau ada, itulah yang dirujuk daftar isi, bukan slug judulnya.
            eksplisit = re.search(r'<a\s+id="([^"]+)"', k.group(2))
            dari_isi = (peta.get(eksplisit.group(1).lower()) if eksplisit else None) \
                or peta.get(dasar if ke == 0 else f"{dasar}-{ke}")
            if dari_isi:
                jalur = [(i + tingkat_awal, n) for i, n in enumerate(dari_isi)]
            else:
                jalur = [(t, n) for t, n in jalur if t < tingkat]
                jalur.append((tingkat, nama))
            continue
        if lewati or b.lstrip().startswith(">"):
            continue
        m = JUDUL_BUTIR.match(b)
        if not m:
            continue
        isi = re.sub(r"^\[[ xX]\]\s+", "", m.group(2).strip())
        if isi.startswith("[") and "](#" in isi[:300]:
            continue        # tautan daftar isi
        hasil_tautan = _ambil_tautan(isi)
        if not hasil_tautan:
            if isi.startswith("[") and URL.search(isi):
                rusak.append((nomor, b.strip()[:120]))
            continue
        judul, url, sisa = hasil_tautan
        if not judul:
            continue
        if judul == url:
            rusak.append((nomor, "judul = URL: " + url[:100]))
        topik = " › ".join(n for _, n in jalur) if jalur else ""
        hasil.append({
            "judul": judul, "url": url, "jenis": jenis, "bahasa": bahasa,
            "topik": [topik] if topik else [], "catatan": _catatan(sisa),
        })
    return hasil, rusak


def urai_tabel_api(teks):
    """Baris tabel public-apis: | [Nama](url) | Deskripsi | Auth | HTTPS | CORS |."""
    hasil = []
    kategori = ""
    sesudah_isi = False
    for b in teks.splitlines():
        k = KEPALA.match(b)
        if k:
            nama = _rapikan(k.group(2))
            if len(k.group(1)) == 2:
                # Iklan sponsor ada SEBELUM daftar isi; katalognya sesudahnya.
                sesudah_isi = sesudah_isi or nama.lower() == "index"
            elif len(k.group(1)) == 3 and sesudah_isi:
                kategori = nama
            continue
        if not b.startswith("| [") or not kategori:
            continue
        sel = [s.strip() for s in b.strip().strip("|").split(" | ")]
        if len(sel) < 5:
            continue
        t = _ambil_tautan(sel[0])
        if not t:
            continue
        judul, url, _ = t
        auth = sel[2].strip("`")
        rincian = ["tanpa kunci API" if auth.lower() == "no" else "butuh " + auth]
        if sel[3].lower() == "yes":
            rincian.append("HTTPS")
        if sel[4].lower() == "yes":
            rincian.append("CORS")
        catatan = _rapikan(sel[1])
        hasil.append({
            "judul": judul, "url": url, "jenis": "api", "bahasa": "en",
            "topik": [kategori],
            "catatan": (catatan + " · " + ", ".join(rincian)).strip(" ·"),
        })
    return hasil


# ------------------------------------------------------------- tiap sumber

def _baca(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def panen_fpb(akar):
    semua, rusak = [], []
    for rel, jenis, bahasa in FPB_BERKAS:
        hasil, r = urai_daftar(_baca(os.path.join(akar, rel)), jenis, bahasa,
                               tingkat_awal=3)
        semua += hasil
        rusak += [(rel, n, b) for n, b in r]
    return semua, rusak


def panen_proyek(akar):
    """project-based-learning lewat parser resminya sendiri (MIT, stdlib)."""
    path = os.path.join(akar, "scripts", "check_readme.py")
    spec = importlib.util.spec_from_file_location("_cek_readme", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    dok = mod.parse_readme(_baca(os.path.join(akar, "README.md")))
    status = {}
    path_status = os.path.join(akar, ".github", "link-rot-state.json")
    if os.path.exists(path_status):
        with open(path_status, encoding="utf-8") as f:
            status = json.load(f)
    hasil, mati = [], []
    # Induk sebuah butir menjorok kadang TEKS POLOS ("- Tiny 3D graphics
    # projects"), dan parser resminya cuma mengembalikan butir bertaut. Jadi
    # induknya dibaca dari baris mentah: butir tak-menjorok terdekat di atasnya.
    mentah = _baca(os.path.join(akar, "README.md")).splitlines()

    def _induk(nomor):
        for i in range(nomor - 2, -1, -1):
            b = mentah[i]
            if b.startswith("- "):
                return _rapikan(TAUTAN_MD.sub(r"\1", b[2:]).split(" - ")[0])
            if b.startswith("#"):
                return ""
        return ""

    for e in dok.entries:
        judul = _rapikan(e.title)
        if e.depth > 0:
            # "Part 6" tidak berarti apa-apa tanpa seri yang memuatnya.
            induk = _induk(e.line)
            if induk and induk != judul:
                judul = induk + " · " + judul
        kelas = (status.get(_kunci_url(e.url)) or {}).get("last_class")
        if kelas == "HARD_DEAD":
            mati.append(("mati", e.url))
            continue
        hasil.append({
            "judul": judul, "url": e.url, "jenis": "proyek",
            "bahasa": "en", "topik": [_rapikan(e.section)] if e.section else [],
            "catatan": _catatan(e.tail or ""),
        })
    return hasil, mati


def panen_awesome(akar):
    return urai_daftar(_baca(os.path.join(akar, "readme.md")), "daftar", "en",
                       tingkat_awal=2, pakai_isi=False)


def panen_api(akar):
    return urai_tabel_api(_baca(os.path.join(akar, "README.md"))), []


def panen_fcc(akar):
    """Hanya tautan sertifikasi dari README (nama + alamat = fakta)."""
    hasil = []
    pola = re.compile(r"\[([^\]]+)\]\((https://www\.freecodecamp\.org/learn/[^)\s]+)\)")
    terlihat = set()
    for b in _baca(os.path.join(akar, "README.md")).splitlines():
        for judul, url in pola.findall(b):
            if url in terlihat:
                continue
            terlihat.add(url)
            hasil.append({
                "judul": _rapikan(judul), "url": url, "jenis": "kursus",
                "bahasa": "en", "topik": ["Sertifikasi freeCodeCamp"],
                "catatan": "Kursus interaktif gratis bersertifikat, berbahasa Inggris.",
            })
    return hasil, []


def panen_desain(akar):
    return urai_daftar(_baca(os.path.join(akar, "README.md")), "bacaan", "en",
                       tingkat_awal=2, pakai_isi=False,
                       lewati_sebelum=r"^## System design topics: start here")


def panen_peta(akar):
    folder = os.path.join(akar, "roadmaps")
    hasil = []
    for slug in sorted(os.listdir(folder)):
        if not os.path.isdir(os.path.join(folder, slug)):
            continue
        nama = NAMA_PETA.get(slug) or " ".join(k.capitalize() for k in slug.split("-"))
        hasil.append({
            "judul": "Peta belajar " + nama, "url": "https://roadmap.sh/" + slug,
            "jenis": "peta", "bahasa": "en", "topik": ["Peta belajar"],
            "catatan": "Peta topik interaktif di roadmap.sh, berbahasa Inggris.",
        })
    return hasil, []


def panen_ciu(akar):
    return urai_daftar(_baca(os.path.join(akar, "README.md")), "bacaan", "en",
                       tingkat_awal=2, pakai_isi=False,
                       lewati_sebelum=r"^## Choose a Programming Language")


def panen_python(akar):
    return urai_daftar(_baca(os.path.join(akar, "README.md")), "pustaka", "en",
                       tingkat_awal=2, pakai_isi=False)


def panen_rujukan(_akar):
    return [
        {"judul": "Getting a Gig: panduan mencari kerja developer",
         "url": "https://github.com/cassidoo/getting-a-gig", "jenis": "daftar",
         "bahasa": "en", "topik": ["Karier"],
         "catatan": ("Kumpulan tautan tentang CV, portofolio, dan wawancara "
                     "oleh Cassidy Williams. Repo tanpa lisensi, jadi dibuka "
                     "langsung di GitHub.")},
        {"judul": "Build Your Own X: bangun ulang teknologi dari nol",
         "url": "https://github.com/codecrafters-io/build-your-own-x",
         "jenis": "daftar", "bahasa": "en", "topik": ["Proyek"],
         "catatan": ("Tutorial membangun Git, Docker, database, shell, dan "
                     "lainnya sendiri. Repo tanpa lisensi, jadi dibuka "
                     "langsung di GitHub.")},
    ], []


PEMANEN = {
    "fpb": panen_fpb, "proyek": panen_proyek, "awesome": panen_awesome,
    "api": panen_api, "fcc": panen_fcc, "desain": panen_desain,
    "peta": panen_peta, "ciu": panen_ciu, "python": panen_python,
    "rujukan": panen_rujukan,
}


# Ruas jalur topik yang cuma wadah, bukan topik: dibuang dari jalurnya.
RUAS_WADAH = {"projects", "source(s) and further reading"}


def _rapikan_topik(entri):
    """Buang ruas wadah dan titik dua di ujung; buang entri sponsor."""
    keluar = []
    for e in entri:
        jalur_baru = []
        sponsor = False
        for jalur in e["topik"]:
            ruas = []
            for r in jalur.split(" › "):
                r = r.strip("*").strip().rstrip(":").strip()
                rendah = r.lower()
                if "sponsor" in rendah:
                    sponsor = True
                if rendah in RUAS_WADAH or rendah.startswith("source(s) and further reading"):
                    continue
                if r:
                    ruas.append(r)
            if ruas and " › ".join(ruas) not in jalur_baru:
                jalur_baru.append(" › ".join(ruas))
        if sponsor:
            continue
        e["topik"] = jalur_baru
        keluar.append(e)
    return keluar


def _gabung_kembar(entri):
    """Satu URL, satu entri. Topik dari kemunculan lain digabung ke situ."""
    per_url = {}
    urutan = []
    for e in entri:
        k = _kunci_url(e["url"])
        if k in per_url:
            ada = per_url[k]
            for t in e["topik"]:
                if t not in ada["topik"]:
                    ada["topik"].append(t)
            if not ada["catatan"] and e["catatan"]:
                ada["catatan"] = e["catatan"]
            continue
        per_url[k] = e
        urutan.append(e)
    return urutan


def _commit(folder):
    try:
        return subprocess.run(["git", "-C", folder, "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def main(argv):
    if len(argv) not in (2, 3):
        print("pakai: python3 alat/panen_pustaka.py <folder materi-belajar> [folder keluaran]")
        return 2
    akar_materi = argv[1]
    # Folder keluaran opsional dipakai tes: memanen ulang ke folder sementara
    # lalu membandingkannya dengan data/pustaka/ membuktikan berkas di repo
    # memang hasil skrip ini, bukan suntingan tangan.
    keluar = argv[2] if len(argv) == 3 else KELUAR
    os.makedirs(keluar, exist_ok=True)
    total = 0
    for kunci, pemanen in PEMANEN.items():
        meta = dict(SUMBER[kunci])
        folder = meta.pop("folder")
        akar = os.path.join(akar_materi, folder) if folder else akar_materi
        entri, catatan_rusak = pemanen(akar)
        for e in entri:
            # Satu pembersih judul untuk SEMUA pemanen, termasuk yang memakai
            # parser milik repo sumbernya. "A* Pathfinding" sah, jadi yang
            # dibuang cuma penanda tebal dan kode, bukan bintang tunggal.
            e["judul"] = re.sub(r"\(:([a-z]{2}):\)", r"(\1)", e["judul"])
            e["judul"] = _rapikan(e["judul"].replace("**", "").replace("`", " "))
        entri = _rapikan_topik(entri)
        sebelum = len(entri)
        entri = _gabung_kembar(entri)
        meta["kunci"] = kunci
        meta["commit"] = _commit(akar) if folder else ""
        with open(os.path.join(keluar, kunci + ".json"), "w", encoding="utf-8") as f:
            json.dump({"sumber": meta, "entri": entri}, f, ensure_ascii=False,
                      indent=0, separators=(",", ":"))
            f.write("\n")
        total += len(entri)
        print(f"{kunci:8s} {len(entri):5d} entri  (kembar digabung: {sebelum - len(entri)})")
        for r in catatan_rusak[:12]:
            print("         lewati:", r)
        if len(catatan_rusak) > 12:
            print(f"         ... dan {len(catatan_rusak) - 12} lagi")
    print(f"total    {total:5d} entri -> {keluar}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
