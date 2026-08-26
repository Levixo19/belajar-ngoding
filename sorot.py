"""Penyorot sintaks untuk 8 bahasa, tanpa dependensi apa pun.

Sebelum ini semua contoh kode dicetak satu warna hijau datar. Untuk pemula itu
justru menyulitkan: string, komentar, kata kunci, dan nama variabel terlihat
sama persis, padahal justru MEMBEDAKAN keempatnya itulah yang sedang dipelajari.

Ini bukan parser. Ini pemindai token satu lintasan yang cukup pintar untuk
komentar, string (termasuk kutip tiga Python dan kutip terbalik Go/JS), angka,
kata kunci, tipe, dan nama fungsi -- dan cukup bodoh untuk tidak pernah gagal:
apa pun yang tidak dikenali dicetak sebagai teks biasa. Kode rusak sekalipun
tetap tampil utuh.

Kontrak penting: `sorot_baris()` mengembalikan daftar baris yang masing-masing
SUDAH lengkap kode warnanya (dibuka dan ditutup di baris yang sama). Itu wajib
karena paginasi memotong per baris; kode warna yang menggantung antar baris
akan bocor ke seluruh layar.
"""

import tema

# Jenis token -> peran warna di tema.
_PERAN = {
    "komentar": "kode_komentar",
    "string": "kode_string",
    "angka": "kode_angka",
    "kunci": "kode_kunci",
    "tipe": "kode_tipe",
    "bawaan": "kode_bawaan",
    "fungsi": "kode_fungsi",
    "operator": "kode_operator",
    "khusus": "kode_khusus",
    "teks": "kode_teks",
}

_HURUF_AWAL = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")
_HURUF_LANJUT = _HURUF_AWAL | set("0123456789")
_ANGKA = set("0123456789")
_OPERATOR = set("+-*/%=<>!&|^~?:;,.()[]{}@")


class Aturan:
    """Deskripsi leksikal satu bahasa."""

    __slots__ = (
        "komentar_baris", "komentar_blok", "kutip", "kutip_mentah", "escape",
        "kunci", "tipe", "bawaan", "praprosesor", "variabel_dolar",
        "tanpa_bedakan_kapital",
    )

    def __init__(self, komentar_baris=(), komentar_blok=(), kutip=('"', "'"),
                 kutip_mentah=(), escape=True, kunci=(), tipe=(), bawaan=(),
                 praprosesor=False, variabel_dolar=False,
                 tanpa_bedakan_kapital=False):
        self.komentar_baris = tuple(komentar_baris)
        self.komentar_blok = tuple(komentar_blok)
        # Diurutkan dari yang terpanjang supaya '"""' menang atas '"'.
        self.kutip = tuple(sorted(kutip, key=len, reverse=True))
        self.kutip_mentah = frozenset(kutip_mentah)
        self.escape = escape
        self.kunci = frozenset(kunci)
        self.tipe = frozenset(tipe)
        self.bawaan = frozenset(bawaan)
        self.praprosesor = praprosesor
        self.variabel_dolar = variabel_dolar
        self.tanpa_bedakan_kapital = tanpa_bedakan_kapital


def _kata(teks):
    return tuple(teks.split())


_C_UMUM = _kata("""
    auto break case char const continue default do double else enum extern
    float for goto if inline int long register restrict return short signed
    sizeof static struct switch typedef union unsigned void volatile while
""")

ATURAN = {
    "java": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kunci=_kata("""
            abstract assert boolean break byte case catch char class const
            continue default do double else enum extends final finally float
            for goto if implements import instanceof int interface long native
            new package private protected public return short static strictfp
            super switch synchronized this throw throws transient try var void
            volatile while record sealed permits yield true false null
        """),
        tipe=_kata("""
            String Integer Double Boolean Character Long Float Short Byte
            Object Number List ArrayList LinkedList Map HashMap TreeMap Set
            HashSet TreeSet Arrays Collections Optional Stream Exception
            RuntimeException Thread Runnable StringBuilder BigDecimal
        """),
        bawaan=_kata("""
            System out err in println print printf format length equals
            hashCode toString valueOf parseInt parseDouble charAt substring
            indexOf split trim replace contains startsWith endsWith Scanner
            nextInt nextLine nextDouble Math abs max min pow sqrt round random
        """),
    ),
    "python": Aturan(
        komentar_baris=("#",),
        kutip=('"""', "'''", '"', "'"),
        kunci=_kata("""
            False None True and as assert async await break class continue def
            del elif else except finally for from global if import in is lambda
            nonlocal not or pass raise return try while with yield match case
        """),
        tipe=_kata("int float str bool list dict set tuple bytes complex frozenset object type"),
        bawaan=_kata("""
            print input len range sum min max abs sorted reversed enumerate zip
            map filter open isinstance issubclass round format repr id hash iter
            next any all divmod pow chr ord bin hex oct super staticmethod
            classmethod property append extend insert remove pop clear copy keys
            values items get join split strip replace startswith endswith upper
            lower title count index find self
        """),
    ),
    "javascript": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=('"', "'", "`"),
        kunci=_kata("""
            var let const function return if else for while do switch case
            break continue new delete typeof instanceof in of this class
            extends super import export default from try catch finally throw
            async await yield static get set null undefined true false void
            with debugger
        """),
        tipe=_kata("""
            Object Array String Number Boolean Symbol BigInt Function Promise
            Map Set WeakMap WeakSet Date RegExp Error JSON Math
        """),
        bawaan=_kata("""
            console log warn error info table document window fetch alert
            parseInt parseFloat isNaN require module exports setTimeout
            setInterval push pop shift unshift slice splice map filter reduce
            forEach find includes indexOf join split length toString keys
            values entries stringify parse then catch finally
        """),
    ),
    "c": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        praprosesor=True,
        kunci=_C_UMUM + _kata("_Bool _Complex bool true false NULL"),
        tipe=_kata("""
            size_t ssize_t FILE int8_t int16_t int32_t int64_t
            uint8_t uint16_t uint32_t uint64_t
        """),
        bawaan=_kata("""
            printf scanf sprintf sscanf fprintf fgets fputs puts putchar
            getchar malloc calloc realloc free memset memcpy memcmp strlen
            strcpy strncpy strcmp strncmp strcat strchr strstr atoi atof exit
            fopen fclose fread fwrite abs sqrt pow floor ceil rand srand qsort
        """),
    ),
    "cpp": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        praprosesor=True,
        kunci=_C_UMUM + _kata("""
            class namespace template typename public private protected virtual
            override final new delete this try catch throw using operator
            friend explicit constexpr consteval nullptr bool true false
            static_cast dynamic_cast const_cast reinterpret_cast decltype
            noexcept mutable export concept requires co_await co_return co_yield
        """),
        tipe=_kata("""
            std string wstring vector map unordered_map set unordered_set list
            deque queue stack pair tuple array shared_ptr unique_ptr weak_ptr
            ostream istream stringstream size_t int64_t uint64_t optional
        """),
        bawaan=_kata("""
            cout cin cerr endl push_back pop_back emplace_back begin end size
            empty clear insert erase find count sort reverse accumulate max min
            swap move make_pair make_shared make_unique to_string stoi stod
            getline printf scanf
        """),
    ),
    "bash": Aturan(
        komentar_baris=("#",),
        kutip=('"', "'"),
        kutip_mentah=("'",),   # kutip tunggal di shell TIDAK mengenal escape
        variabel_dolar=True,
        kunci=_kata("""
            if then else elif fi for while until do done case esac function in
            select time coproc return local export readonly declare typeset let
            shift break continue exit source trap set unset eval exec
        """),
        bawaan=_kata("""
            echo printf read cd pwd ls cat grep egrep sed awk cut sort uniq wc
            head tail mkdir rmdir rm cp mv touch test chmod chown find xargs tr
            date sleep expr basename dirname seq tee which command type mapfile
            readarray true false
        """),
    ),
    "go": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=('"', "'", "`"),
        kutip_mentah=("`",),
        kunci=_kata("""
            break case chan const continue default defer else fallthrough for
            func go goto if import interface map package range return select
            struct switch type var nil true false iota
        """),
        tipe=_kata("""
            bool string error any byte rune int int8 int16 int32 int64 uint
            uint8 uint16 uint32 uint64 uintptr float32 float64 complex64
            complex128 Time Duration Reader Writer
        """),
        bawaan=_kata("""
            make new len cap append copy delete panic recover print println
            close fmt Println Printf Sprintf Sprint Print Errorf Scan Scanln
            Scanf strings strconv Itoa Atoi Split Join Contains ToUpper ToLower
            TrimSpace Replace sort math os bufio errors New
        """),
    ),
    "sql": Aturan(
        komentar_baris=("--", "#"), komentar_blok=(("/*", "*/"),),
        kutip=('"', "'", "`"),
        tanpa_bedakan_kapital=True,
        kunci=_kata("""
            SELECT FROM WHERE INSERT INTO VALUES UPDATE SET DELETE CREATE TABLE
            DROP ALTER ADD COLUMN RENAME PRIMARY KEY FOREIGN REFERENCES NOT
            NULL UNIQUE DEFAULT CHECK CONSTRAINT INDEX VIEW TRIGGER JOIN INNER
            LEFT RIGHT FULL OUTER CROSS NATURAL USING ON AS AND OR IN BETWEEN
            LIKE GLOB IS EXISTS ORDER BY GROUP HAVING LIMIT OFFSET DISTINCT
            UNION INTERSECT EXCEPT ALL CASE WHEN THEN ELSE END ASC DESC BEGIN
            COMMIT ROLLBACK TRANSACTION WITH RECURSIVE AUTOINCREMENT IF
            REPLACE PRAGMA EXPLAIN CAST COLLATE
        """),
        tipe=_kata("""
            INTEGER INT SMALLINT BIGINT TEXT VARCHAR CHAR REAL FLOAT DOUBLE
            DECIMAL NUMERIC BLOB BOOLEAN DATE TIME DATETIME TIMESTAMP SERIAL
        """),
        bawaan=_kata("""
            COUNT SUM AVG MIN MAX ROUND ABS LENGTH UPPER LOWER SUBSTR TRIM
            COALESCE IFNULL NULLIF STRFTIME JULIANDAY RANDOM GROUP_CONCAT
            ROW_NUMBER RANK DENSE_RANK OVER PARTITION
        """),
    ),
}

# Alias yang mungkin dipakai pemanggil.
ATURAN["c++"] = ATURAN["cpp"]
ATURAN["js"] = ATURAN["javascript"]
ATURAN["py"] = ATURAN["python"]
ATURAN["sh"] = ATURAN["bash"]
ATURAN["shell"] = ATURAN["bash"]

_POLOS = Aturan()


def aturan_untuk(bahasa):
    return ATURAN.get((bahasa or "").lower(), _POLOS)


def bahasa_didukung():
    return sorted({"java", "python", "javascript", "c", "cpp", "bash", "go", "sql"})


# ---------------------------------------------------------------- pemindai

def _akhir_string(kode, i, pembuka, aturan):
    """Cari index tepat SESUDAH string yang dimulai di `i` dengan `pembuka`."""
    mentah = pembuka in aturan.kutip_mentah or not aturan.escape
    j = i + len(pembuka)
    n = len(kode)
    # Kutip tunggal biasa tidak boleh melintasi baris; kutip tiga dan kutip
    # terbalik boleh.
    satu_baris = len(pembuka) == 1 and pembuka != "`"

    while j < n:
        c = kode[j]
        if not mentah and c == "\\":
            j += 2
            continue
        if kode.startswith(pembuka, j):
            return j + len(pembuka)
        if satu_baris and c == "\n":
            return j
        j += 1
    return n


def _akhir_angka(kode, i):
    n = len(kode)
    j = i
    if kode[j] == "0" and j + 1 < n and kode[j + 1] in "xXbBoO":
        j += 2
        while j < n and kode[j] in _HURUF_LANJUT:
            j += 1
        return j

    lihat_titik = False
    while j < n:
        c = kode[j]
        if c in _ANGKA or c == "_":
            j += 1
        elif c == "." and not lihat_titik and j + 1 < n and kode[j + 1] in _ANGKA:
            lihat_titik = True
            j += 1
        elif c in "eE" and j + 1 < n and (kode[j + 1] in _ANGKA or kode[j + 1] in "+-"):
            j += 2
        elif c in "fFlLdDuU":       # sufiks literal C/Java
            j += 1
        else:
            break
    return j


def _di_awal_baris(kode, i):
    j = i - 1
    while j >= 0 and kode[j] in " \t":
        j -= 1
    return j < 0 or kode[j] == "\n"


def token(kode, bahasa):
    """Pecah `kode` jadi urutan (jenis, teks). Gabungannya = kode aslinya.

    Sifat itu diuji: tidak boleh ada satu karakter pun yang hilang atau
    berubah, apa pun bahasanya dan seburuk apa pun kodenya.
    """
    aturan = aturan_untuk(bahasa)
    hasil = []
    simpanan = []
    i = 0
    n = len(kode)

    def buang():
        if simpanan:
            hasil.append(("teks", "".join(simpanan)))
            simpanan.clear()

    while i < n:
        c = kode[i]

        # -- shebang ----------------------------------------------------------
        if i == 0 and kode.startswith("#!"):
            akhir = kode.find("\n", i)
            akhir = n if akhir < 0 else akhir
            hasil.append(("komentar", kode[i:akhir]))
            i = akhir
            continue

        # -- praprosesor C/C++ -------------------------------------------------
        if aturan.praprosesor and c == "#" and _di_awal_baris(kode, i):
            akhir = kode.find("\n", i)
            akhir = n if akhir < 0 else akhir
            buang()
            hasil.append(("khusus", kode[i:akhir]))
            i = akhir
            continue

        # -- komentar blok -----------------------------------------------------
        cocok_blok = next(((b, t) for b, t in aturan.komentar_blok if kode.startswith(b, i)), None)
        if cocok_blok:
            buka, tutup = cocok_blok
            akhir = kode.find(tutup, i + len(buka))
            akhir = n if akhir < 0 else akhir + len(tutup)
            buang()
            hasil.append(("komentar", kode[i:akhir]))
            i = akhir
            continue

        # -- komentar baris ----------------------------------------------------
        if next((p for p in aturan.komentar_baris if kode.startswith(p, i)), None):
            akhir = kode.find("\n", i)
            akhir = n if akhir < 0 else akhir
            buang()
            hasil.append(("komentar", kode[i:akhir]))
            i = akhir
            continue

        # -- string ------------------------------------------------------------
        pembuka = next((q for q in aturan.kutip if kode.startswith(q, i)), None)
        if pembuka:
            akhir = _akhir_string(kode, i, pembuka, aturan)
            buang()
            hasil.append(("string", kode[i:akhir]))
            i = akhir
            continue

        # -- variabel shell ------------------------------------------------------
        if aturan.variabel_dolar and c == "$":
            j = i + 1
            if j < n and kode[j] == "{":
                tutup = kode.find("}", j)
                j = n if tutup < 0 else tutup + 1
            elif j < n and kode[j] == "(":
                j += 1
            else:
                while j < n and kode[j] in _HURUF_LANJUT:
                    j += 1
                if j == i + 1 and j < n:       # $1, $@, $?, $#
                    j += 1
            buang()
            hasil.append(("khusus", kode[i:j]))
            i = j
            continue

        # -- angka ---------------------------------------------------------------
        if c in _ANGKA:
            akhir = _akhir_angka(kode, i)
            buang()
            hasil.append(("angka", kode[i:akhir]))
            i = akhir
            continue

        # -- pengenal ------------------------------------------------------------
        if c in _HURUF_AWAL:
            j = i + 1
            while j < n and kode[j] in _HURUF_LANJUT:
                j += 1
            kata = kode[i:j]
            bandingan = kata.upper() if aturan.tanpa_bedakan_kapital else kata

            if bandingan in aturan.kunci:
                jenis = "kunci"
            elif bandingan in aturan.tipe:
                jenis = "tipe"
            elif bandingan in aturan.bawaan:
                jenis = "bawaan"
            else:
                k = j
                while k < n and kode[k] in " \t":
                    k += 1
                jenis = "fungsi" if k < n and kode[k] == "(" else "teks"

            if jenis == "teks":
                simpanan.append(kata)
            else:
                buang()
                hasil.append((jenis, kata))
            i = j
            continue

        # -- operator & sisanya ----------------------------------------------------
        if c in _OPERATOR:
            buang()
            hasil.append(("operator", c))
            i += 1
            continue

        simpanan.append(c)
        i += 1

    buang()
    return _gabung(hasil)


def _gabung(token_list):
    """Satukan token berdampingan yang sejenis.

    Tanpa ini `System.out.println(` menghasilkan lima token operator terpisah,
    masing-masing dibungkus kode warna sendiri -- keluarannya jadi berkali-kali
    lipat lebih panjang dari kodenya, padahal tampilannya sama persis.
    """
    padat = []
    for jenis, teks in token_list:
        if padat and padat[-1][0] == jenis:
            padat[-1][1].append(teks)
        else:
            padat.append((jenis, [teks]))
    return [(jenis, "".join(bagian)) for jenis, bagian in padat]


# ------------------------------------------------------------------ keluaran

def _warnai(jenis, teks):
    return tema.cat(teks, _PERAN.get(jenis, "kode_teks"))


def sorot_baris(kode, bahasa, awalan=""):
    """Kode tersorot sebagai daftar baris, masing-masing lengkap kode warnanya.

    `awalan` ditempel di depan setiap baris SEBELUM pewarnaan, berguna untuk
    indentasi tampilan tanpa mengubah indentasi kode aslinya.
    """
    baris = []
    kini = [awalan] if awalan else []

    for jenis, teks in token(kode, bahasa):
        potongan = teks.split("\n")
        for idx, p in enumerate(potongan):
            if idx > 0:
                baris.append("".join(kini))
                kini = [awalan] if awalan else []
            if p:
                kini.append(_warnai(jenis, p))

    baris.append("".join(kini))
    return baris


def sorot(kode, bahasa, awalan=""):
    """Versi satu string dari `sorot_baris`."""
    return "\n".join(sorot_baris(kode, bahasa, awalan))


def polos(kode, bahasa):
    """Rangkai ulang kode dari token tanpa warna.

    Dipakai pengujian: kalau hasilnya tidak sama persis dengan masukan, berarti
    pemindai menelan karakter dan penyorotan tidak boleh dipercaya.
    """
    return "".join(t for _, t in token(kode, bahasa))

# Modul "Bikin Aplikasi" memakai contoh kode Java, jadi aturan leksikalnya sama.
ATURAN["aplikasi"] = ATURAN["java"]
