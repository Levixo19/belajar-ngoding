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

import copy

from inti import tema

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
# Kunci di awal baris boleh memuat tanda hubung, titik, dan garis miring:
# `runs-on`, `spring.jpa.open-in-view`, `app.kubernetes.io/name`.
_KUNCI_LANJUT = _HURUF_LANJUT | set(".-/")


class Aturan:
    """Deskripsi leksikal satu bahasa."""

    __slots__ = (
        "komentar_baris", "komentar_blok", "kutip", "kutip_mentah", "escape",
        "kunci", "tipe", "bawaan", "praprosesor", "variabel_dolar",
        "tanpa_bedakan_kapital", "pemisah_kunci",
    )

    def __init__(self, komentar_baris=(), komentar_blok=(), kutip=('"', "'"),
                 kutip_mentah=(), escape=True, kunci=(), tipe=(), bawaan=(),
                 praprosesor=False, variabel_dolar=False,
                 tanpa_bedakan_kapital=False, pemisah_kunci=()):
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
        # Pemisah yang menandai KUNCI di awal baris: ":" untuk YAML dan header
        # HTTP, "=" untuk ini, TOML, dan atribut HCL. Kosong = tidak ada.
        self.pemisah_kunci = tuple(pemisah_kunci)


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
    # Delapan bahasa di bawah lahir bersama 12 kurikulum tech stack dan
    # selama ini tampil TANPA warna sama sekali (94 blok). Kata kuncinya
    # DITURUNKAN dari kata yang benar-benar muncul di bloknya, bukan dari
    # daftar reserved word yang lengkap tapi tidak relevan -- itu sebabnya
    # `bawaan` Groovy berisi DSL Jenkins, dan `data.frame` (R) serta
    # `@import` (Zig) TIDAK didaftarkan: keduanya memuat karakter di luar
    # pola kata, jadi entrinya tidak akan pernah cocok.
    "swift": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=('"""', '"'),
        kunci=_kata("""
            actor as associatedtype async await break case catch class
            continue convenience default defer deinit do else enum extension
            fallthrough false fileprivate final for func guard if import in
            indirect init inout internal is lazy let mutating nil open
            operator override private protocol public repeat required rethrows
            return self Self some static struct subscript super switch throw
            throws true try typealias unowned var weak where while
        """),
        tipe=_kata("""
            Any AnyObject Array Bool Character Data Date Dictionary Double
            Error Float Int Int8 Int16 Int32 Int64 Never Optional Result Set
            String Text UInt URL View Void
        """),
        bawaan=_kata("""
            append compactMap count filter first insert isEmpty last map
            print reduce removeAll sorted
        """),
    ),
    "dart": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=("'''", '"""', '"', "'"),
        kunci=_kata("""
            abstract as assert async await break case catch class const
            continue covariant default deferred do dynamic else enum export
            extends extension external factory false final finally for get
            hide if implements import in interface is late library mixin new
            null on operator part required rethrow return set show static
            super switch sync this throw true try typedef var void while with
            yield
        """),
        tipe=_kata("""
            bool double Future int Iterable List Map num Object Set
            StatefulWidget StatelessWidget Stream String Text Widget
        """),
        bawaan=_kata("add forEach isEmpty length map print then toList where"),
    ),
    "lua": Aturan(
        komentar_baris=("--",), komentar_blok=(("--[[", "]]"),),
        kunci=_kata("""
            and break do else elseif end false for function goto if in local
            nil not or repeat return then true until while
        """),
        bawaan=_kata("""
            error getmetatable io ipairs math next os pairs pcall print
            rawget rawset require select setmetatable string table tonumber
            tostring type unpack
        """),
    ),
    "r": Aturan(
        komentar_baris=("#",),
        kunci=_kata("""
            break else FALSE for function if in Inf NA NaN next NULL repeat
            TRUE while
        """),
        tipe=_kata("""
            array character complex double factor integer list logical matrix
            numeric vector
        """),
        bawaan=_kata("""
            apply c cat colnames head lapply length library max mean min
            names ncol nrow order paste paste0 print rep require rownames
            round sapply seq sort str sum summary tail which
        """),
    ),
    "elixir": Aturan(
        komentar_baris=("#",),
        kutip=('"""', '"'),
        kunci=_kata("""
            after alias and case catch cond def defimpl defmacro defmodule
            defp defprotocol defstruct do else end false fn for if import in
            nil not or quote raise receive require rescue true try unless
            unquote use when with
        """),
        bawaan=_kata("""
            Agent apply Enum GenServer inspect IO Kernel List Map Process
            puts self send spawn String Task
        """),
    ),
    "haskell": Aturan(
        komentar_baris=("--",), komentar_blok=(("{-", "-}"),),
        kunci=_kata("""
            case class data default deriving do else foreign if import in
            infix infixl infixr instance let module newtype of then type
            where
        """),
        tipe=_kata("""
            Bool Char Double Either Float Int Integer IO Maybe Ordering
            String Word
        """),
        bawaan=_kata("""
            concat drop filter fmap foldl foldr getLine head Just Left length
            map mapM_ Nothing otherwise print product pure putStr putStrLn
            read return reverse Right show sum tail take zip
        """),
    ),
    "zig": Aturan(
        komentar_baris=("//",),
        kutip=('"',),
        kunci=_kata("""
            align and anytype asm async await break callconv catch comptime
            const continue defer else enum errdefer error export extern fn
            for if inline noalias nosuspend null opaque or orelse packed pub
            resume return struct suspend switch test threadlocal try union
            undefined unreachable usingnamespace var volatile while
        """),
        tipe=_kata("""
            anyerror bool c_int comptime_float comptime_int f16 f32 f64 f128
            i8 i16 i32 i64 i128 isize noreturn type u8 u16 u32 u64 u128 usize
            void
        """),
        bawaan=_kata("alloc append debug deinit free init len print std"),
    ),
    # Kelima blok "groovy" di kurikulum ini sebenarnya Jenkinsfile, jadi
    # DSL-nya ikut jadi bawaan -- tanpa itu yang tersorot cuma `def` dan
    # tanda kutipnya. Kutip tiga didaftarkan walau korpusnya belum memakainya:
    # ia STRUKTURAL, dan salah menebaknya membuat `sh '''...'''` terbaca
    # sebagai string kosong lalu string yang tidak pernah ditutup.
    "groovy": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=("'''", '"""', '"', "'"),
        kunci=_kata("""
            as assert break case catch class const continue def default do
            else enum extends false final finally for goto if implements
            import in instanceof interface new null package return super
            switch this throw throws trait true try var while
        """),
        tipe=_kata("Boolean Integer List Map Object String"),
        bawaan=_kata("""
            agent always any archiveArtifacts bat checkout docker echo
            environment failure input junit label node none options parallel
            parameters pipeline post script sh stage stages steps success
            tools triggers when withCredentials
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
    "csharp": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        praprosesor=True,   # #if, #region, #nullable
        kunci=_kata("""
            abstract as base bool break byte case catch char checked class
            const continue decimal default delegate do double else enum event
            explicit extern false finally fixed float for foreach goto if
            implicit in int interface internal is lock long namespace new null
            object operator out override params private protected public
            readonly ref return sbyte sealed short sizeof stackalloc static
            string struct switch this throw true try typeof uint ulong
            unchecked unsafe ushort using virtual void volatile while
            add and get global init nameof not or partial record remove
            required set value var when where with yield async await dynamic
            nint nuint file scoped
        """),
        tipe=_kata("""
            Console String Int32 Int64 Double Decimal Boolean Char Object
            List Dictionary HashSet Queue Stack Array IEnumerable ICollection
            IList IDictionary IReadOnlyList IComparable IEquatable IDisposable
            Exception ArgumentException ArgumentNullException Task ValueTask
            Func Action Predicate Nullable DateTime TimeSpan Guid StringBuilder
            Math File Directory Path Stream StreamReader StreamWriter Regex
            CultureInfo StringComparer LINQ Enumerable HashCode
        """),
        bawaan=_kata("""
            WriteLine Write ReadLine Read Length Count Add Remove RemoveAt
            Insert Clear Contains ContainsKey TryGetValue TryParse Parse
            ToString ToUpper ToLower Trim Substring IndexOf Split Join Replace
            StartsWith EndsWith Sort Reverse Where Select SelectMany OrderBy
            OrderByDescending ThenBy ThenByDescending GroupBy First
            FirstOrDefault Single Last Any All Sum Average Min Max Take Skip
            Distinct ToList ToArray Append Equals GetHashCode CompareTo
            Invoke Dispose Combine Round Abs Sqrt Pow Sign Floor Ceiling
        """),
    ),
    # Visual Basic tidak membedakan huruf besar-kecil, dan tanda kutip TUNGGAL
    # memulai KOMENTAR, bukan string. Menyalin bawaan dari bahasa lain di sini
    # akan membuat setiap komentar terbaca sebagai string yang tidak pernah
    # ditutup -- seluruh baris sesudahnya ikut berubah warna.
    # Daftarnya ditulis KAPITAL karena `tanpa_bedakan_kapital` membandingkan
    # `kata.upper()`; kode VB-nya sendiri tetap boleh ditulis campuran.
    "vb": Aturan(
        komentar_baris=("'",),
        kutip=('"',),
        tanpa_bedakan_kapital=True,
        kunci=_kata("""
            ADDHANDLER ADDRESSOF ALIAS AND ANDALSO AS BOOLEAN BYREF BYTE BYVAL
            CALL CASE CATCH CBOOL CBYTE CCHAR CDATE CDBL CDEC CHAR CINT CLASS
            CLNG COBJ CONST CONTINUE CSBYTE CSHORT CSNG CSTR CTYPE CUINT CULNG
            CUSHORT DATE DECIMAL DECLARE DEFAULT DELEGATE DIM DIRECTCAST DO
            DOUBLE EACH ELSE ELSEIF END ENDIF ENUM ERASE ERROR EVENT EXIT FALSE
            FINALLY FOR FRIEND FUNCTION GET GETTYPE GETXMLNAMESPACE GLOBAL
            GOTO HANDLES IF IMPLEMENTS IMPORTS IN INHERITS INTEGER INTERFACE
            IS ISNOT LET LIB LIKE LONG LOOP ME MOD MODULE MUSTINHERIT
            MUSTOVERRIDE MYBASE MYCLASS NAMESPACE NARROWING NEW NEXT NOT
            NOTHING NOTINHERITABLE NOTOVERRIDABLE OBJECT OF ON OPERATOR OPTION
            OPTIONAL OR ORELSE OVERLOADS OVERRIDABLE OVERRIDES PARAMARRAY
            PARTIAL PRIVATE PROPERTY PROTECTED PUBLIC RAISEEVENT READONLY
            REDIM REM REMOVEHANDLER RESUME RETURN SBYTE SELECT SET SHADOWS
            SHARED SHORT SINGLE STATIC STEP STOP STRING STRUCTURE SUB
            SYNCLOCK THEN THROW TO TRUE TRY TRYCAST TYPEOF UINTEGER ULONG
            USHORT USING VARIANT WEND WHEN WHILE WIDENING WITH WITHEVENTS
            WRITEONLY XOR ASYNC AWAIT ITERATOR YIELD
        """),
        tipe=_kata("""
            CONSOLE INTEGER STRING DOUBLE DECIMAL BOOLEAN CHAR OBJECT DATE
            LIST DICTIONARY HASHSET QUEUE STACK ARRAY EXCEPTION MATH
            STRINGBUILDER ENVIRONMENT CONVERT ENUMERABLE NULLABLE LONG SINGLE
            BYTE SHORT
        """),
        bawaan=_kata("""
            WRITELINE WRITE READLINE LENGTH COUNT ADD REMOVE REMOVEAT INSERT
            CLEAR CONTAINS CONTAINSKEY TRYGETVALUE TRYPARSE PARSE TOSTRING
            TOUPPER TOLOWER TRIM SUBSTRING INDEXOF SPLIT JOIN REPLACE SORT
            WHERE SELECT ORDERBY SUM AVERAGE MIN MAX ANY ALL TOLIST TOARRAY
            FORMAT PADLEFT PADRIGHT STARTSWITH ENDSWITH ABS SQRT ROUND
        """),
    ),
    # Kutip TUNGGAL sengaja tidak terdaftar: di Rust `&'a str` adalah lifetime,
    # dan memperlakukannya sebagai pembuka string membuat sisa barisnya ikut
    # berubah jadi string. Literal char 'x' jadi tidak disorot -- harga yang
    # jauh lebih murah daripada satu baris utuh yang salah warna.
    "rust": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=('"',),
        kunci=_kata("""
            as async await break const continue crate dyn else enum extern
            false fn for if impl in let loop match mod move mut pub ref return
            self Self static struct super trait true type unsafe use where
            while abstract become box do final macro override priv typeof
            unsized virtual yield union
        """),
        tipe=_kata("""
            bool char str String i8 i16 i32 i64 i128 isize u8 u16 u32 u64 u128
            usize f32 f64 Vec HashMap HashSet BTreeMap VecDeque Option Result
            Box Rc Arc RefCell Cell Mutex RwLock Iterator IntoIterator Clone
            Copy Debug Display Default PartialEq Eq PartialOrd Ord Hash Some
            None Ok Err
        """),
        bawaan=_kata("""
            println print eprintln format vec panic assert assert_eq write
            writeln len push pop insert remove get contains iter into_iter
            map filter collect fold sum count min max sorted sort sort_by
            unwrap expect unwrap_or unwrap_or_else is_some is_none ok_or
            and_then to_string to_owned as_str parse trim split lines chars
            bytes new from with_capacity clone matches enumerate zip rev take
            skip last first push_str
        """),
    ),
    "php": Aturan(
        komentar_baris=("//", "#"), komentar_blok=(("/*", "*/"),),
        kutip=('"', "'"),
        variabel_dolar=True,
        kunci=_kata("""
            abstract and array as break callable case catch class clone const
            continue declare default do echo else elseif empty enddeclare
            endfor endforeach endif endswitch endwhile enum extends final
            finally fn for foreach function global goto if implements include
            include_once instanceof insteadof interface isset list match
            namespace new or print private protected public readonly require
            require_once return static switch throw trait try unset use var
            while xor yield from true false null parent self this
        """),
        tipe=_kata("""
            int float string bool array object mixed void never iterable
            callable static self parent null false true ArrayObject Closure
            Generator Exception Throwable Error TypeError ValueError PDO
            DateTime DateTimeImmutable Stringable Countable JsonSerializable
        """),
        bawaan=_kata("""
            count strlen str_replace substr strpos strtolower strtoupper trim
            ltrim rtrim explode implode join sprintf printf number_format
            array_map array_filter array_reduce array_keys array_values
            array_merge array_slice array_sum in_array array_search sort rsort
            usort ksort asort krsort array_push array_pop array_shift
            array_unshift array_unique range max min abs round floor ceil
            intdiv json_encode json_decode var_dump print_r file_get_contents
            file_put_contents fopen fgets fclose is_array is_string is_int
            is_null isset unset date time str_repeat str_pad ucfirst
            preg_match preg_replace preg_split array_key_exists
        """),
    ),
    "ruby": Aturan(
        komentar_baris=("#",),
        kutip=('"', "'"),
        kunci=_kata("""
            alias and begin BEGIN break case class def defined? do else elsif
            end END ensure false for if in module next nil not or redo rescue
            retry return self super then true undef unless until when while
            yield require require_relative attr_accessor attr_reader
            attr_writer include extend prepend private protected public raise
            lambda proc new
        """),
        tipe=_kata("""
            String Symbol Integer Float Numeric Array Hash Range Struct Set
            Time Date Proc Method Comparable Enumerable Kernel Object Class
            Module Exception StandardError ArgumentError TypeError RuntimeError
            NameError IndexError KeyError ZeroDivisionError IO File Dir JSON
        """),
        bawaan=_kata("""
            puts print p pp gets chomp chop strip length size count first last
            push pop shift unshift map collect select filter reject reduce
            inject each each_with_index each_with_object times upto downto
            step sort sort_by min max min_by max_by sum group_by partition
            find detect include? empty? any? all? none? nil? zero? even? odd?
            to_s to_i to_f to_a to_sym to_h split join reverse uniq flatten
            compact freeze frozen? dup clone keys values fetch merge delete
            slice gsub sub match start_with? end_with? upcase downcase
            capitalize center ljust rjust format sprintf
        """),
    ),
    "kotlin": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=('"""', '"', "'"),
        kunci=_kata("""
            as break by catch class companion const constructor continue crossinline
            data do dynamic else enum external false field file finally for fun get
            if import in infix init inline inner interface internal is lateinit
            noinline null object open operator out override package param private
            property protected public receiver reified return sealed set setparam
            super suspend tailrec this throw true try typealias typeof val var
            vararg when where while it annotation abstract final actual expect
        """),
        tipe=_kata("""
            Any Unit Nothing Boolean Byte Short Int Long Float Double Char
            String Array List MutableList Map MutableMap Set MutableSet Pair
            Triple Sequence Iterable Comparable Number Regex Exception
            IllegalArgumentException IllegalStateException Throwable Result
            Deferred Job CoroutineScope Flow StringBuilder
        """),
        bawaan=_kata("""
            println print readLine listOf mutableListOf arrayListOf mapOf
            mutableMapOf setOf mutableSetOf arrayOf emptyList size indices
            first last add remove removeAt contains containsKey isEmpty
            isNotEmpty map filter flatMap forEach forEachIndexed fold reduce
            sumOf count any all none find firstOrNull lastOrNull sorted
            sortedBy sortedByDescending groupBy associate associateBy joinToString
            toList toMutableList toSet toMap toString toInt toDouble trim split
            substring indexOf replace startsWith endsWith uppercase lowercase
            let run apply also with require check error lazy launch async
            await delay repeat maxOf minOf
        """),
    ),
    "typescript": Aturan(
        komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
        kutip=('"', "'", "`"),
        kunci=_kata("""
            var let const function return if else for while do switch case
            break continue new delete typeof instanceof in of this class
            extends super import export default from try catch finally throw
            async await yield static get set null undefined true false void
            with debugger interface type enum namespace declare abstract
            implements private protected public readonly as is keyof infer
            satisfies override accessor module require asserts unique global
        """),
        tipe=_kata("""
            string number boolean bigint symbol object any unknown never void
            null undefined Array ReadonlyArray Record Partial Required Readonly
            Pick Omit Exclude Extract NonNullable ReturnType Parameters Awaited
            Map Set WeakMap WeakSet Promise Date RegExp Error JSON Math Object
            Function Iterable Iterator Generator Tuple
        """),
        bawaan=_kata("""
            console log warn error info table process fetch structuredClone
            parseInt parseFloat isNaN setTimeout setInterval push pop shift
            unshift slice splice map filter reduce forEach find findIndex some
            every includes indexOf join split length toString keys values
            entries stringify parse then catch finally resolve reject all
            allSettled race from of freeze assign hasOwnProperty trim replace
            startsWith endsWith padStart padEnd repeat toFixed sort reverse
            flat flatMap at
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
    # -------------------------------------------------------------- HTML
    #
    # Pemindai di berkas ini berbasis TOKEN, bukan tata bahasa: ia tidak tahu
    # apa itu tag, atribut, atau isi elemen. Untuk HTML itu ternyata sudah
    # cukup jauh — `<`, `>`, `/` jadi operator, nilai atribut jadi string, dan
    # nama tag dikenali lewat daftar di bawah. Yang tersisa satu kompromi:
    # kalau teks biasa di dalam halaman kebetulan memuat kata "table" atau
    # "form", kata itu ikut berwarna.
    #
    # Kompromi itu diambil dengan sadar. Alternatifnya pemindai kedua yang
    # mengerti tata bahasa HTML — dan karena statik/js/sorot.js WAJIB
    # menghasilkan token yang identik dengan berkas ini (lihat AGENTS.md),
    # harganya dua implementasi baru yang harus terus dijaga tetap sama. Satu
    # kata yang kelebihan warna jauh lebih murah daripada itu.
    #
    # Daftarnya ditulis KAPITAL karena `tanpa_bedakan_kapital` membandingkan
    # `kata.upper()`; markup-nya sendiri tetap boleh huruf kecil.
    "html": Aturan(
        komentar_blok=(("<!--", "-->"),),
        kutip=('"', "'"),
        escape=False,
        tanpa_bedakan_kapital=True,
        kunci=_kata("""
            HTML HEAD BODY TITLE META LINK SCRIPT STYLE BASE
            H1 H2 H3 H4 H5 H6 P BR HR SPAN DIV SECTION ARTICLE ASIDE NAV MAIN
            HEADER FOOTER ADDRESS BLOCKQUOTE PRE CODE EM STRONG SMALL MARK
            SUB SUP DEL INS ABBR CITE Q TIME
            UL OL LI DL DT DD
            TABLE THEAD TBODY TFOOT TR TH TD CAPTION COLGROUP COL
            FORM INPUT TEXTAREA BUTTON SELECT OPTION OPTGROUP LABEL FIELDSET
            LEGEND DATALIST OUTPUT PROGRESS METER
            A IMG PICTURE SOURCE FIGURE FIGCAPTION VIDEO AUDIO TRACK IFRAME
            CANVAS SVG AREA EMBED OBJECT PARAM
            DETAILS SUMMARY DIALOG TEMPLATE NOSCRIPT
        """),
        tipe=_kata("""
            DOCTYPE CLASS ID SRC HREF ALT LANG CHARSET NAME CONTENT
            TYPE VALUE PLACEHOLDER REQUIRED DISABLED CHECKED SELECTED READONLY
            WIDTH HEIGHT REL TARGET ACTION METHOD FOR COLSPAN ROWSPAN
            SRCSET SIZES LOADING AUTOCOMPLETE MAXLENGTH PATTERN
            MIN MAX STEP MULTIPLE ACCEPT DOWNLOAD HIDDEN TABINDEX ROLE
        """),
        bawaan=_kata("""
            STYLESHEET ICON PRELOAD VIEWPORT UTF CSS
            SUBMIT RESET CHECKBOX RADIO PASSWORD EMAIL NUMBER DATE FILE
            BLANK SELF PARENT TOP
        """),
    ),

    # --------------------------------------------------------------- CSS
    #
    # Properti CSS penuh tanda hubung, dan `-` bukan bagian dari sebuah kata
    # bagi pemindai ini — `background-color` sampai ke sini sebagai tiga token:
    # kata, operator, kata. Jadi yang didaftarkan POTONGAN KATANYA, bukan nama
    # properti utuhnya. Hasilnya justru lebih baik daripada mendaftar ratusan
    # nama lengkap: properti apa pun yang tersusun dari kata-kata ini ikut
    # berwarna, termasuk yang belum ada waktu daftar ini ditulis.
    "css": Aturan(
        komentar_blok=(("/*", "*/"),),
        kutip=('"', "'"),
        escape=False,
        tanpa_bedakan_kapital=True,
        kunci=_kata("""
            COLOR BACKGROUND IMAGE REPEAT ATTACHMENT
            FONT FAMILY SIZE WEIGHT STYLE LINE HEIGHT LETTER WORD SPACING
            TEXT ALIGN DECORATION TRANSFORM SHADOW INDENT WHITE SPACE
            MARGIN PADDING TOP RIGHT BOTTOM LEFT
            BORDER WIDTH RADIUS BOX SIZING
            DISPLAY POSITION INDEX FLOAT CLEAR OVERFLOW VISIBILITY OPACITY
            FLEX DIRECTION WRAP GROW SHRINK BASIS
            JUSTIFY CONTENT ITEMS SELF GAP
            GRID TEMPLATE COLUMNS ROWS COLUMN ROW AREA PLACE
            LIST TRANSITION ANIMATION CURSOR OUTLINE FILTER OBJECT FIT
        """),
        tipe=_kata("""
            BLOCK INLINE FLEX GRID NONE HIDDEN VISIBLE AUTO
            ABSOLUTE RELATIVE FIXED STICKY STATIC
            CENTER JUSTIFY START END BETWEEN AROUND EVENLY
            SOLID DASHED DOTTED DOUBLE BOLD NORMAL ITALIC UNDERLINE
            UPPERCASE LOWERCASE CAPITALIZE
            NOWRAP POINTER DEFAULT MOVE
            TRANSPARENT INHERIT INITIAL UNSET CURRENTCOLOR
            SANS SERIF MONOSPACE CURSIVE
        """),
        bawaan=_kata("""
            RGB RGBA HSL HSLA URL CALC VAR CLAMP
            IMPORTANT MEDIA SUPPORTS KEYFRAMES IMPORT CHARSET FACE ROOT
            HOVER FOCUS ACTIVE VISITED CHILD BEFORE AFTER NOT IS WHERE HAS
            SCREEN PRINT
        """),
    ),
}

# Alias yang mungkin dipakai pemanggil.
ATURAN["c++"] = ATURAN["cpp"]
ATURAN["js"] = ATURAN["javascript"]
ATURAN["py"] = ATURAN["python"]
ATURAN["sh"] = ATURAN["bash"]
ATURAN["shell"] = ATURAN["bash"]
ATURAN["htm"] = ATURAN["html"]
ATURAN["cs"] = ATURAN["csharp"]
ATURAN["c#"] = ATURAN["csharp"]
ATURAN["vb.net"] = ATURAN["vb"]
ATURAN["vbnet"] = ATURAN["vb"]
ATURAN["visualbasic"] = ATURAN["vb"]
ATURAN["rs"] = ATURAN["rust"]
ATURAN["rb"] = ATURAN["ruby"]
ATURAN["kt"] = ATURAN["kotlin"]
ATURAN["ts"] = ATURAN["typescript"]

# Fedora memakai aturan Bash, tapi sebagai objek TERSENDIRI, bukan alias.
# bahasa_didukung() membuang duplikat berdasarkan id() -- begitulah ia
# menyaring alias seperti "sh" dan "shell". Fedora adalah bahasa tersendiri di
# LANGUAGES, dan daftar dari fungsi itulah yang dikirim ke editor web lewat
# /api/awal. Kalau ia menunjuk objek yang sama dengan bash, Fedora lenyap dari
# daftar dan kodenya tampil polos tanpa satu pun pesan galat.
ATURAN["fedora"] = copy.copy(ATURAN["bash"])
# Git: alasan yang sama. Kodenya bash, tapi ia bahasa tersendiri di LANGUAGES.
ATURAN["git"] = copy.copy(ATURAN["bash"])

_POLOS = Aturan()


def aturan_untuk(bahasa):
    return ATURAN.get((bahasa or "").lower(), _POLOS)


def bahasa_didukung():
    """Nama kanonik semua bahasa yang punya aturan penyorotan.

    DITURUNKAN dari ATURAN, bukan ditulis ulang. Versi sebelumnya berupa daftar
    keras berisi delapan nama, dan akibatnya persis seperti yang bisa ditebak:
    menambahkan HTML dan CSS ke ATURAN tidak menyalakannya di editor web sama
    sekali — karena daftar INILAH yang dikirim ke sana lewat /api/awal, dan
    daftar itu tidak ikut diperbarui. Gejalanya pun tidak menuduh siapa-siapa:
    penyorotannya cuma "terlihat polos", tanpa satu pun error.

    Alias dibuang di sini (c++, js, py, sh, shell, htm): semuanya menunjuk
    objek Aturan yang SAMA dengan nama kanoniknya, jadi mengirimnya lagi cuma
    menggandakan muatan tanpa menambah apa pun. Dict Python menjaga urutan
    penyisipan, sehingga nama kanonik — yang selalu didefinisikan lebih dulu —
    yang menang.
    """
    kanonik = {}
    for nama, aturan in ATURAN.items():
        kanonik.setdefault(id(aturan), nama)
    return sorted(kanonik.values())


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


def _akhir_kunci(kode, i, pemisah):
    """Index tepat sesudah KUNCI yang dimulai di `i`, atau 0 kalau bukan kunci.

    Kunci = deretan huruf, angka, `_ . - /` yang berdiri di AWAL baris (boleh
    didahului indentasi dan penanda butir `- `) dan disusul salah satu
    `pemisah`. Dua pengaman supaya yang bukan kunci tidak ikut terwarnai:
    `:` hanya berlaku bila disusul spasi atau akhir baris (`http://x` bukan
    kunci), dan `=` tidak berlaku bila disusul `=` (`a == b` bukan penugasan).
    Pemindai ini murni leksikal: tanpa pengaman itu ia tidak punya cara lain
    membedakan `image: nginx` dari `curl http://host` di dalam blok skrip.
    """
    j = i - 1
    while j >= 0 and kode[j] != "\n":
        if kode[j] in " \t" or (kode[j] == "-" and kode[j + 1] in " \t"):
            j -= 1
        else:
            return 0
    n = len(kode)
    akhir = i + 1
    while akhir < n and kode[akhir] in _KUNCI_LANJUT:
        akhir += 1
    k = akhir
    while k < n and kode[k] in " \t":
        k += 1
    if k >= n or kode[k] not in pemisah:
        return 0
    sesudah = kode[k + 1:k + 2]
    if kode[k] == ":" and sesudah not in ("", " ", "\t", "\r", "\n"):
        return 0
    if kode[k] == "=" and sesudah == "=":
        return 0
    return akhir


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

        # -- kunci di awal baris -----------------------------------------------
        if aturan.pemisah_kunci and c in _HURUF_AWAL:
            akhir = _akhir_kunci(kode, i, aturan.pemisah_kunci)
            if akhir:
                buang()
                hasil.append(("kunci", kode[i:akhir]))
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


# ------------------------------------------------- bahasa yang dulu tanpa warna
#
# Menyusul belakangan, di ekor berkas. Kata kuncinya diturunkan dari kata yang
# BENAR-BENAR muncul di kurikulum, dan yang bentuknya juga muncul sebagai bagian
# URL atau prosa sengaja tidak didaftarkan: `http` tidak ada di nginx karena
# `proxy_pass http://toko_backend` akan mewarnai awal URL-nya, dan `index`
# tidak ada karena `index.php` akan ikut terwarnai sebagai direktif.
#
# YAML, TOML, ini, header HTTP, dan atribut HCL berbagi satu fitur pemindai,
# `pemisah_kunci`: kunci di awal baris. Pemindai leksikal tanpa fitur itu hanya
# bisa mewarnai komentar dan tanda kutip, dan berkas konfigurasi tetap tampak
# mati walau angka cakupannya naik.

ATURAN["yaml"] = Aturan(
    komentar_baris=("#",), pemisah_kunci=(":",),
    bawaan=_kata("true false null"),
)

ATURAN["toml"] = Aturan(
    komentar_baris=("#",),
    kutip=('"""', "'''", '"', "'"), kutip_mentah=("'", "'''"),
    pemisah_kunci=("=",), bawaan=_kata("true false"),
)

# ini juga dipakai untuk unit systemd, application.properties, dan
# postgresql.conf. `;` dan `#` sama-sama pembuka komentar di berkas itu.
ATURAN["ini"] = Aturan(
    komentar_baris=("#", ";"), pemisah_kunci=("=",), variabel_dolar=True,
    bawaan=_kata("true false yes no on off"),
)

ATURAN["http"] = Aturan(
    komentar_baris=("#",), kutip=('"',), pemisah_kunci=(":",),
    kunci=_kata("GET POST PUT PATCH DELETE HEAD OPTIONS CONNECT TRACE"),
    tipe=_kata("HTTP"), bawaan=_kata("true false null"),
)

ATURAN["nginx"] = Aturan(
    komentar_baris=("#",), variabel_dolar=True,
    kunci=_kata("""
        server location upstream events listen server_name root alias
        try_files return rewrite if set map include error_page proxy_pass
        proxy_set_header proxy_http_version proxy_buffering proxy_read_timeout
        proxy_send_timeout proxy_connect_timeout proxy_redirect proxy_cache
        proxy_cache_path proxy_cache_valid fastcgi_pass fastcgi_param
        fastcgi_index least_conn ip_hash hash keepalive client_max_body_size
        client_body_buffer_size expires add_header server_tokens autoindex
        limit_req_zone limit_req limit_req_status limit_conn access_log
        error_log log_format worker_processes worker_connections gzip
        gzip_types sendfile tcp_nopush keepalive_timeout ssl_certificate
        ssl_certificate_key ssl_protocols ssl_ciphers ssl_session_cache
        auth_basic auth_basic_user_file deny allow http2
    """),
    bawaan=_kata("""
        on off weight max_fails fail_timeout backup down default_server ssl
    """),
)

ATURAN["hcl"] = Aturan(
    komentar_baris=("#", "//"), komentar_blok=(("/*", "*/"),),
    kutip=('"',), pemisah_kunci=("=",),
    kunci=_kata("""
        resource data variable output module provider locals terraform
        required_providers required_version backend moved import check dynamic
        for_each depends_on lifecycle provisioner connection for in if else
    """),
    tipe=_kata("string number bool list map set object tuple any"),
    bawaan=_kata("true false null var local each self path"),
)

# Perintah Redis tidak membedakan huruf besar-kecil; daftarnya huruf besar
# karena pemindai membandingkan kata yang sudah dibesarkan.
ATURAN["redis"] = Aturan(
    komentar_baris=("#",), tanpa_bedakan_kapital=True,
    kunci=_kata("""
        SET GET GETSET GETDEL SETEX SETNX SETBIT GETBIT BITCOUNT BITOP MSET
        MGET APPEND STRLEN INCR INCRBY INCRBYFLOAT DECR DECRBY DEL UNLINK
        EXISTS EXPIRE EXPIREAT PEXPIRE TTL PTTL PERSIST KEYS SCAN TYPE RENAME
        LPUSH RPUSH LPOP RPOP LLEN LRANGE LINDEX LREM LTRIM LMOVE BLMOVE BLPOP
        BRPOP HSET HGET HMSET HMGET HGETALL HDEL HEXISTS HINCRBY HKEYS HVALS
        HLEN SADD SREM SMEMBERS SISMEMBER SCARD SPOP SUNION SINTER SDIFF ZADD
        ZREM ZRANGE ZREVRANGE ZRANGEBYSCORE ZSCORE ZRANK ZINCRBY ZCARD PUBLISH
        SUBSCRIBE UNSUBSCRIBE PSUBSCRIBE XADD XLEN XRANGE XREAD XREADGROUP
        XGROUP XACK XPENDING XCLAIM XTRIM MULTI EXEC DISCARD WATCH UNWATCH
        EVAL EVALSHA PING ECHO AUTH SELECT INFO FLUSHALL FLUSHDB DBSIZE SAVE
        BGSAVE CONFIG CLIENT MONITOR SLOWLOG PFADD PFCOUNT GEOADD GEODIST
        GEOSEARCH OBJECT
    """),
    bawaan=_kata("""
        EX PX EXAT NX XX KEEPTTL WITHSCORES COUNT MATCH STREAMS MKSTREAM GROUP
        CREATE LEFT RIGHT
    """),
)

ATURAN["perl"] = Aturan(
    komentar_baris=("#",), variabel_dolar=True,
    kunci=_kata("""
        my our local sub use no package require if elsif else unless while
        until for foreach last next redo return do eval die warn print say
        printf chomp chop push pop shift unshift splice keys values each
        delete exists defined scalar join split map grep sort reverse sprintf
        length substr index lc uc lcfirst ucfirst open close eof and or not
        eq ne lt gt le ge cmp qw BEGIN END
    """),
    bawaan=_kata("STDIN STDOUT STDERR ARGV ENV"),
)

ATURAN["scala"] = Aturan(
    komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
    kutip=('"""', '"', "'"),
    kunci=_kata("""
        abstract case catch class def do else enum export extends final
        finally for given if implicit import lazy match new object override
        package private protected return sealed super then this throw trait
        try type using val var while with yield true false null
    """),
    tipe=_kata("""
        Int Long Double Float Boolean Char String Unit Any AnyRef AnyVal
        Nothing List Map Set Seq Vector Array Option Some None Either Left
        Right Try Success Failure
    """),
)

ATURAN["solidity"] = Aturan(
    komentar_baris=("//",), komentar_blok=(("/*", "*/"),),
    kunci=_kata("""
        pragma import contract interface library abstract function modifier
        event error struct enum mapping constructor returns return public
        private internal external view pure payable virtual override memory
        storage calldata if else for while do break continue emit require
        revert assert new delete is using immutable constant indexed
        anonymous try catch unchecked assembly true false
    """),
    tipe=_kata("""
        address bool string bytes uint int uint8 uint16 uint32 uint64 uint128
        uint256 int8 int16 int32 int64 int128 int256 bytes1 bytes4 bytes32
    """),
    bawaan=_kata("msg block tx abi this"),
)

ATURAN["verilog"] = Aturan(
    komentar_baris=("//",), komentar_blok=(("/*", "*/"),), kutip=('"',),
    kunci=_kata("""
        module endmodule input output inout wire reg integer real time
        parameter localparam assign always initial begin end if else case
        casex casez endcase default for while forever repeat function
        endfunction task endtask generate endgenerate genvar posedge negedge
        or and not nand nor xor xnor buf signed
    """),
    bawaan=_kata("display monitor finish stop dumpfile dumpvars write strobe"),
)

# `'` sengaja tidak dipakai sebagai kutip: di F# ia penanda parameter tipe
# (`'a`) dan literal karakter.
ATURAN["fsharp"] = Aturan(
    komentar_baris=("//",), komentar_blok=(("(*", "*)"),),
    kutip=('"""', '"'),
    kunci=_kata("""
        let in rec and mutable if then else elif match with when function fun
        type of module namespace open do for to downto while yield return use
        new not true false begin end exception try finally raise inherit
        interface abstract member static override private public internal
        async lazy as
    """),
    tipe=_kata("""
        int string float bool unit char byte list array seq option Option
        Result decimal int64 uint32
    """),
    bawaan=_kata("""
        printfn printf sprintf failwith ignore Array List Seq Map String
        Some None Ok Error
    """),
)

ATURAN["nix"] = Aturan(
    komentar_baris=("#",), komentar_blok=(("/*", "*/"),), kutip=("''", '"'),
    kunci=_kata("""
        let in if then else with rec inherit import assert or throw abort
    """),
    bawaan=_kata("true false null builtins"),
)

# `'` sengaja tidak dipakai sebagai kutip: di MATLAB ia juga operator transpos
# (`A'`), dan sebagai kutip ia menelan sisa baris.
ATURAN["matlab"] = Aturan(
    komentar_baris=("%",), komentar_blok=(("%{", "%}"),), kutip=('"',),
    kunci=_kata("""
        function end if elseif else for while switch case otherwise break
        continue return try catch parfor global persistent classdef
        properties methods
    """),
    bawaan=_kata("true false pi inf nan eps"),
)

# Luau = Lua + `continue`, anotasi tipe, dan `export type`. Objek TERSENDIRI,
# bukan alias: bahasa_didukung() membuang duplikat berdasarkan id().
ATURAN["luau"] = copy.copy(ATURAN["lua"])
ATURAN["luau"].kunci = ATURAN["lua"].kunci | frozenset(("continue", "type", "export"))
ATURAN["luau"].tipe = ATURAN["lua"].tipe | frozenset(
    ("number", "string", "boolean", "any", "unknown", "never"))
