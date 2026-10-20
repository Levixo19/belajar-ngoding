"""Kurikulum tech stack: frontend, backend, database, mobile, DevOps, data & AI, dst.

Pemilik minta materi "semua tech stack yang ada sekarang tanpa terkecuali"
(2026-10-19). Kurikulum ranah ini dimuat dari SATU tempat supaya tiap
kurikulum tinggal di berkasnya sendiri dan bisa ditulis bersamaan tanpa
saling menimpa:

  data/<key>_materials.py  -> <KEY>_MATERIALS, dan <KEY>_BAB (spesifikasi bab)
  data/<key>_quizzes.py    -> <KEY>_QUIZZES, dan <KEY>_KUIS_MATERI
  data/<key>_exercises.py  -> <KEY>_EXERCISES
  data/visual/<key>.py     -> VISUAL (gambar konsep, lihat inti/visual.py)

`topik` dan `peta` di tiap entri adalah ruas topik dan slug roadmap.sh untuk
Pustaka (inti/pustaka.py); keduanya baru ikut dipetakan begitu kurikulumnya
terdaftar, karena peta Pustaka hanya boleh menunjuk kurikulum yang ada.

Sebuah kurikulum baru masuk LANGUAGES begitu KETIGA berkas datanya ada dan
tidak kosong; sebelum itu ia belum terdaftar sama sekali (bukan tampil
setengah jadi).

`<KEY>_BAB` sengaja berbentuk spesifikasi -- judul, keterangan, tingkat,
JUMLAH materi -- bukan rentang indeks yang diketik tangan. Rentangnya
dihitung di sini, dan jumlah yang tidak cocok dengan banyaknya materi
DITOLAK keras (ValueError), persis aturan generator data/bab.py.

`key` di sini tidak boleh diubah setelah rilis (kunci progres) dan sengaja
tanpa garis bawah: kunci progres berbentuk "<key>_<tipe>::<judul>".
"""

import importlib

from data.normalisasi import seimbangkan_kuis

TINGKAT = ("dasar", "menengah", "mahir")

KURIKULUM = [
    {"key": "techstack", "label": "Tech Stack & Arsitektur", "runner": "python",
     "topik": ['software architecture', 'system design', 'design patterns', 'software engineering', 'system design, scalability, data handling', 'web development', 'development', 'open source ecosystem', 'platforms', 'load balancer', 'cache', 'computer science'],
     "peta": ['software-architect', 'software-design-architecture', 'system-design', 'full-stack', 'api-design', 'computer-science'],
     "run_info": ["Peta besar: apa itu tech stack, bagaimana bagiannya saling",
                  "terhubung, dan cara memilihnya. Latihannya Python murni yang",
                  "mensimulasikan konsep arsitektur (cache, antrean, versi)."]},
    {"key": "frontend", "label": "Frontend Modern", "runner": "javascript",
     "topik": ['front-end development', 'react', 'react.js', 'vue.js', 'svelte', 'next.js', 'angular', 'angularjs', 'jquery', 'redux', 'elm', 'ember.js', 'backbone.js', 'bootstrap', 'tailwind css', 'sass', 'web performance', 'd3.js', 'webpack', 'javascript'],
     "peta": ['frontend', 'frontend-beginner', 'react', 'vue', 'angular', 'nextjs', 'design-system'],
     "run_info": ["Contoh framework (React, Vue, Svelte, ...) butuh paket npm,",
                  "jadi dicoba di proyekmu sendiri. Latihannya JavaScript murni:",
                  "kamu membangun versi mini framework-nya untuk paham isinya.",
                  "Jalankan latihan: node nama_file.js"]},
    {"key": "backend", "label": "Backend & API", "runner": "python",
     "topik": ['back-end development', 'web frameworks', 'web apis', 'django', 'flask', 'fastapi', 'spring', 'spring boot', 'laravel', 'ruby on rails', 'rails', 'asp.net', 'asp.net core', 'nest.js', 'node.js', 'nodejs', 'graphql', 'authentication & authorization', 'authentication', 'rpc and rest calls comparison', 'http clients', 'orm', 'asynchronous programming'],
     "peta": ['backend', 'backend-beginner', 'nodejs', 'django', 'laravel', 'ruby-on-rails', 'spring-boot', 'aspnet-core', 'graphql', 'api-design'],
     "run_info": ["Contoh framework (Express, Django, Spring, Laravel, ...)",
                  "dicoba di proyekmu sendiri sesudah dipasang. Latihannya",
                  "Python murni: router, middleware, token, dan API versi mini.",
                  "Jalankan latihan: python3 nama_file.py"]},
    {"key": "database", "label": "Database & Penyimpanan Data", "runner": "python",
     "topik": ['databases', 'database', 'nosql', 'mongodb', 'redis', 'elastic', 'sql', 'mysql', 'postgresql', 'sqlite', 'orm', 'database drivers', 'big data', 'dbms'],
     "peta": ['postgresql-dba', 'mongodb', 'redis', 'elasticsearch', 'sql'],
     "run_info": ["Relasional, NoSQL, pencarian, vektor, dan analitik.",
                  "Latihannya Python murni (dan sqlite3 bawaan Python) yang",
                  "meniru cara kerja indeks, cache, dan kueri dokumen.",
                  "Jalankan latihan: python3 nama_file.py"]},
    {"key": "mobile", "label": "Mobile & Desktop", "runner": "javascript",
     "topik": ['flutter', 'dart', 'ios', 'swift', 'android', 'react native', 'gui development', 'graphical user interfaces', 'electron', 'objective-c'],
     "peta": ['android', 'ios', 'flutter', 'react-native', 'swift-ui'],
     "run_info": ["Android, iOS, lintas platform (Flutter, React Native, ...),",
                  "dan aplikasi desktop. Contoh tiap platform dicoba di alatnya",
                  "sendiri. Latihannya JavaScript murni: state, navigasi, dan",
                  "siklus hidup aplikasi versi mini. Jalankan: node nama_file.js"]},
    {"key": "game", "label": "Game & Grafis", "runner": "javascript",
     "topik": ['game development', 'graphics programming', 'gaming', 'games & comics'],
     "peta": ['game-developer', 'server-side-game-developer'],
     "run_info": ["Game engine (Godot, Unity, Unreal, ...), API grafis, dan XR.",
                  "Contoh engine dicoba di editornya sendiri. Latihannya",
                  "JavaScript murni: game loop, tabrakan, vektor, dan state.",
                  "Jalankan latihan: node nama_file.js"]},
    {"key": "iot", "label": "Embedded & IoT", "runner": "c",
     "topik": ['arduino', 'raspberry pi', 'embedded systems', 'robotics', 'hardware'],
     "peta": [],
     "run_info": ["Mikrokontroler, Arduino, ESP32, RTOS, dan protokol IoT.",
                  "Kode untuk papan dicoba di papannya sendiri. Latihannya C",
                  "murni yang mensimulasikan register, buffer, dan sensor.",
                  "Kompilasi: gcc nama_file.c -o program && ./program"]},
    {"key": "devops", "label": "DevOps & Cloud", "runner": "python",
     "topik": ['devops', 'devops tools', 'docker', 'containers', 'kubernetes', 'terraform', 'ansible', 'jenkins', 'cloud computing', 'aws', 'continuous integration', 'networking', 'domain name system', 'linux'],
     "peta": ['devops', 'devops-beginner', 'docker', 'kubernetes', 'terraform', 'aws', 'cloudflare', 'linux', 'network-engineer'],
     "run_info": ["Perintah docker, kubectl, terraform, dan cloud adalah SESI",
                  "TERMINAL: ketik sendiri di mesinmu, aplikasi tidak",
                  "menjalankannya. Latihannya Python murni yang mensimulasikan",
                  "log, konfigurasi, deploy, dan load balancer."]},
    {"key": "keamanan", "label": "Keamanan Siber", "runner": "python",
     "topik": ['security', 'security & privacy', 'cryptography', 'ctf capture the flag', 'anti-malware', 'authentication & authorization', 'authentication'],
     "peta": ['cyber-security', 'devsecops', 'ai-red-teaming'],
     "run_info": ["Keamanan aplikasi, jaringan, dan cloud dari sisi BERTAHAN.",
                  "Alat pemindai dan perintah serangan hanya untuk sistem",
                  "milikmu sendiri. Latihannya Python murni: hash, validasi",
                  "masukan, pemindai log, dan aturan akses versi mini."]},
    {"key": "data", "label": "Data & Analitik", "runner": "python",
     "topik": ['data science', 'data visualization', 'jupyter', 'big data', 'spark', 'data ingestion / etl', 'r', 'julia', 'open data', 'text analysis'],
     "peta": ['data-analyst', 'data-engineer', 'python-data-analysis', 'bi-analyst', 'power-bi', 'r-programming'],
     "run_info": ["Analisis data, rekayasa data (pipeline, ETL), dan BI.",
                  "Contoh pandas, Spark, dan dbt dicoba di proyekmu sendiri.",
                  "Latihannya Python murni: statistik, groupby, pembersihan",
                  "data, dan pipeline versi mini. Jalankan: python3 nama_file.py"]},
    {"key": "ai", "label": "AI & Machine Learning", "runner": "python",
     "topik": ['machine learning', 'artificial intelligence', 'generative ai', 'deep learning', 'ai and agents', 'computer vision', 'natural language processing', 'prompt engineering', 'pytorch', 'cuda'],
     "peta": ['ai-engineer', 'ai-agents', 'ai-data-scientist', 'machine-learning', 'mlops', 'prompt-engineering', 'inference-engineering'],
     "run_info": ["Machine learning, deep learning, LLM, RAG, dan agen AI.",
                  "Contoh scikit-learn, PyTorch, dan SDK LLM butuh paket pip,",
                  "jadi dicoba di proyekmu sendiri. Latihannya Python murni:",
                  "regresi, k-means, embedding, dan tokenizer versi mini."]},
    {"key": "bahasalain", "label": "Bahasa Pemrograman Lain", "runner": "python",
     "topik": ['programming languages', 'haskell', 'scala', 'dart', 'clojure', 'matlab', 'swift', 'perl', 'lua', 'lisp', 'ocaml', 'powershell', 'apl', 'elixir', 'prolog', 'solidity', 'fortran', 'assembly language', 'assembly', 'erlang', 'julia', 'pascal', 'j', 'scheme', 'ada', 'raku', 'cobol', 'objective-c', 'standard ml', 'ballerina', 'coffeescript', 'coldfusion', 'f#', 'forth', 'smalltalk', 'r', 'elm', 'programming paradigms', 'scratch', 'autoit'],
     "peta": ['scala', 'r', 'r-programming', 'blockchain'],
     "run_info": ["Peta bahasa yang belum punya kurikulum sendiri: Swift, Dart,",
                  "Scala, Elixir, Haskell, Lua, R, Julia, Zig, dan banyak lagi.",
                  "Latihannya membaca kode bahasa lain lalu menulis ulang",
                  "logikanya di Python. Jalankan: python3 nama_file.py"]},
]


def _modul(key, jenis):
    """Modul data kurikulum, atau None kalau berkasnya memang belum ada."""
    nama = f"data.{key}_{jenis}"
    try:
        return importlib.import_module(nama)
    except ModuleNotFoundError as e:
        if e.name == nama:
            return None
        raise


def _isi(key):
    """(materi, kuis, latihan, modul_materi, modul_kuis) atau None kalau belum lengkap."""
    besar = key.upper()
    m, q, x = (_modul(key, j) for j in ("materials", "quizzes", "exercises"))
    if not (m and q and x):
        return None
    materi = getattr(m, f"{besar}_MATERIALS", None)
    kuis = getattr(q, f"{besar}_QUIZZES", None)
    latihan = getattr(x, f"{besar}_EXERCISES", None)
    if not (materi and kuis and latihan):
        return None
    return materi, kuis, latihan, m, q


def entri():
    """Entri LANGUAGES untuk kurikulum tech yang datanya sudah lengkap."""
    keluar = []
    for k in KURIKULUM:
        isi = _isi(k["key"])
        if isi is None:
            continue
        materi, kuis, latihan, _m, _q = isi
        keluar.append({
            "key": k["key"], "label": k["label"], "runner": k["runner"],
            "tematik": True, "ranah": "tech",
            "materials": materi, "quizzes": seimbangkan_kuis(kuis),
            "exercises": latihan, "run_info": list(k["run_info"]),
        })
    return keluar


def bab():
    """{key: [entri bab dengan awal/akhir]} dari spesifikasi <KEY>_BAB."""
    hasil = {}
    for k in KURIKULUM:
        isi = _isi(k["key"])
        if isi is None:
            continue
        materi, _kuis, _latihan, m, _q = isi
        spek = getattr(m, f"{k['key'].upper()}_BAB", None)
        if not spek:
            continue
        awal, daftar, tingkat_lalu = 0, [], 0
        for b in spek:
            if b["tingkat"] not in TINGKAT:
                raise ValueError(f"{k['key']}: tingkat {b['tingkat']!r} tidak sah")
            t = TINGKAT.index(b["tingkat"])
            if t < tingkat_lalu:
                raise ValueError(f"{k['key']}: tingkat turun di bab {b['judul']!r}")
            tingkat_lalu = t
            if not isinstance(b["jumlah"], int) or b["jumlah"] < 1:
                raise ValueError(f"{k['key']}: jumlah bab {b['judul']!r} tidak sah")
            daftar.append({"judul": b["judul"], "ket": b["ket"], "tingkat": b["tingkat"],
                           "awal": awal, "akhir": awal + b["jumlah"]})
            awal += b["jumlah"]
        if awal != len(materi):
            raise ValueError(f"{k['key']}: bab menghitung {awal} materi, "
                             f"padahal ada {len(materi)}")
        hasil[k["key"]] = daftar
    return hasil


def terdaftar():
    """Entri KURIKULUM yang datanya lengkap (yang memang masuk LANGUAGES)."""
    return [k for k in KURIKULUM if _isi(k["key"]) is not None]


def kuis_materi():
    """{key: {judul_kuis: [judul materi tanpa nomor per soal]}}."""
    hasil = {}
    for k in KURIKULUM:
        isi = _isi(k["key"])
        if isi is None:
            continue
        peta = getattr(isi[4], f"{k['key'].upper()}_KUIS_MATERI", None)
        if peta:
            hasil[k["key"]] = peta
    return hasil
