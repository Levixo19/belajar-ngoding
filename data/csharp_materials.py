CSHARP_MATERIALS = [
    {
        "title": "1. Pengenalan C# & .NET",
        "sections": [
            {
                "body": [
                    "Apa itu C#?",
                    "  - Bahasa buatan Microsoft, dirilis tahun 2000.",
                    "  - Dirancang Anders Hejlsberg, orang yang sama di balik",
                    "    Turbo Pascal, Delphi, dan belakangan TypeScript.",
                    "  - Statically typed: tipe diperiksa saat kompilasi.",
                    "  - Object-oriented, tapi sejak C# 3 juga sangat fungsional.",
                    "  - Managed: memori diurus garbage collector.",
                    "",
                    "C# dan .NET itu dua hal berbeda, dan membedakannya sejak",
                    "awal menghemat banyak kebingungan:",
                    "",
                    "  C#     bahasanya  - sintaks yang kamu ketik",
                    "  .NET   platformnya - runtime, library, dan tooling",
                    "",
                    "Kode C# dikompilasi bukan jadi instruksi prosesor, melainkan",
                    "jadi IL (Intermediate Language). Saat program dijalankan,",
                    "JIT compiler menerjemahkan IL itu ke instruksi mesin yang",
                    "sesuai dengan prosesor yang sedang dipakai. Itulah kenapa",
                    "satu hasil build bisa jalan di Windows, Linux, dan macOS.",
                    "",
                    "Sejarah singkat yang perlu kamu tahu supaya tidak tersesat",
                    "membaca tutorial lama:",
                    "  - .NET Framework  (2002-2019) Windows saja, versi 1-4.8.",
                    "  - .NET Core       (2016-2020) lintas platform, versi 1-3.1.",
                    "  - .NET            (2020-kini) penerus keduanya, versi 5, 6,",
                    "                    7, 8, 9, dan seterusnya. Tanpa kata Core.",
                    "",
                    "Kalau sebuah tutorial menyebut 'System.Web' atau 'Web Forms',",
                    "itu .NET Framework lama. Yang kita pakai di sini .NET modern.",
                    "",
                    "Dipakai membangun: Unity (game), ASP.NET Core (web),",
                    "MAUI (aplikasi mobile & desktop), Blazor, dan sebagian besar",
                    "sistem internal perusahaan besar.",
                    "",
                    "Instalasi:",
                    "  - Unduh SDK dari https://dotnet.microsoft.com/download",
                    "  - Fedora  : sudo dnf install dotnet-sdk-8.0",
                    "  - Cek     : dotnet --version",
                    "",
                    "Menjalankan program:",
                    "  dotnet new console -o latihan   buat proyek baru",
                    "  cd latihan && dotnet run        kompilasi & jalankan",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Halo Dunia!");
        Console.WriteLine("Aku sedang belajar C#.");
    }
}"""
            },
            {
                "body": [
                    "Penjelasan tiap bagian:",
                    "",
                    "  using System;",
                    "    Memberi tahu compiler: kalau aku menulis Console, carilah",
                    "    di namespace System. Tanpa baris ini kamu harus menulis",
                    "    System.Console.WriteLine setiap kali.",
                    "",
                    "  class Program",
                    "    Semua kode C# tinggal di dalam sebuah tipe. Tidak ada",
                    "    fungsi yang berdiri sendiri di luar class seperti di",
                    "    Python atau JavaScript.",
                    "",
                    "  static void Main()",
                    "    Titik masuk program. static berarti milik class-nya,",
                    "    bukan milik sebuah objek — masuk akal, karena saat",
                    "    program mulai belum ada objek apa pun yang dibuat.",
                    "",
                    "  Console.WriteLine(...)",
                    "    Cetak teks lalu pindah baris. Console.Write tanpa Line",
                    "    mencetak tanpa pindah baris.",
                    "",
                    "Aturan penting C#:",
                    "  1. Setiap pernyataan diakhiri titik koma.",
                    "  2. C# MEMBEDAKAN huruf besar-kecil. Console bukan console.",
                    "  3. Kurung kurawal boleh di baris mana pun; gaya resmi",
                    "     Microsoft menaruhnya di baris baru.",
                    "  4. Nama class dan method memakai PascalCase, variabel",
                    "     lokal memakai camelCase. Ini bukan aturan compiler,",
                    "     tapi dipatuhi hampir semua kode C# di dunia.",
                ]
            },
            {
                "heading": "Top-level statements: bentuk singkat sejak C# 9",
                "code": """// Program.cs -- tanpa class, tanpa Main
Console.WriteLine("Halo Dunia!");
Console.WriteLine("Aku sedang belajar C#.");"""
            },
            {
                "body": [
                    "Sejak C# 9 sebuah berkas boleh berisi pernyataan langsung",
                    "tanpa class dan tanpa Main. Compiler tetap membuatkan",
                    "keduanya di belakang layar — bentuk singkatnya saja yang",
                    "hilang, bukan aturannya.",
                    "",
                    "Syaratnya: hanya SATU berkas dalam proyek yang boleh",
                    "memakai bentuk ini, dan pernyataannya harus berada di",
                    "paling atas berkas, sebelum deklarasi class apa pun.",
                    "",
                    "Di materi ini bentuk panjang yang dipakai, karena bentuk",
                    "itu yang akan kamu lihat di hampir semua kode nyata dan",
                    "di seluruh contoh Unity. Tapi kalau kamu membuka proyek",
                    "baru hasil `dotnet new console` di .NET 6 ke atas, yang",
                    "muncul adalah bentuk singkat ini — jangan kaget.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Tipe Data & Konversi",
        "sections": [
            {
                "body": [
                    "Deklarasi variabel butuh tipe:",
                    "",
                    "  int umur = 20;",
                    "  string nama = \"Andi\";",
                    "  double tinggi = 172.5;",
                    "  bool lulus = true;",
                    "",
                    "Atau serahkan tipenya ke compiler dengan var:",
                    "",
                    "  var umur = 20;        compiler tahu ini int",
                    "  var nama = \"Andi\";    compiler tahu ini string",
                    "",
                    "var BUKAN tipe dinamis. Sekali compiler menyimpulkan int,",
                    "variabel itu int selamanya — menugaskan string ke situ",
                    "tetap error kompilasi. Yang hilang cuma ketikannya, bukan",
                    "pemeriksaan tipenya.",
                    "",
                    "var wajib diberi nilai awal. `var x;` tidak bisa dikompilasi",
                    "karena tidak ada yang bisa disimpulkan.",
                    "",
                    "Tipe bilangan bulat:",
                    "  byte     0 .. 255                         1 byte",
                    "  short    -32.768 .. 32.767                2 byte",
                    "  int      -2,1 miliar .. 2,1 miliar        4 byte  <- bawaan",
                    "  long     -9,2 triliun triliun .. positifnya 8 byte",
                    "",
                    "Tipe pecahan, dan ini yang paling sering salah pilih:",
                    "  float    ~7 digit presisi     ditulis 3.14f",
                    "  double   ~15 digit presisi    ditulis 3.14   <- bawaan",
                    "  decimal  ~28 digit presisi    ditulis 3.14m",
                    "",
                    "Aturan praktisnya satu kalimat: UANG memakai decimal,",
                    "sisanya double. double menyimpan pecahan dalam basis dua,",
                    "jadi 0.1 tidak pernah tersimpan persis 0.1 — dan selisih",
                    "sekecil itu menumpuk jadi rupiah yang hilang di laporan.",
                    "",
                    "Tipe lain:",
                    "  char     satu karakter Unicode, ditulis pakai kutip satu",
                    "  bool     true atau false, TIDAK bisa diisi angka",
                    "  string   deretan karakter, pakai kutip dua",
                    "",
                    "Di C#, `if (1)` adalah error. Kondisi wajib bertipe bool.",
                    "Aturan ini membuang seluruh kelas bug `if (x = 5)` yang",
                    "menghantui C dan C++.",
                ]
            },
            {
                "heading": "Melihat batas tipe sendiri",
                "code": """using System;

class Program
{
    static void Main()
    {
        Console.WriteLine($"int   : {int.MinValue} .. {int.MaxValue}");
        Console.WriteLine($"long  : {long.MinValue} .. {long.MaxValue}");
        Console.WriteLine($"byte  : {byte.MinValue} .. {byte.MaxValue}");

        const double PI = 3.14159;
        Console.WriteLine($"PI    : {PI}");

        // Bukti double tidak menyimpan 0.1 dengan persis
        Console.WriteLine(0.1 + 0.2 == 0.3);          // False
        Console.WriteLine(0.1m + 0.2m == 0.3m);       // True
    }
}"""
            },
            {
                "body": [
                    "const vs readonly, dua kata yang sering tertukar:",
                    "",
                    "  const   nilainya ditetapkan saat KOMPILASI, jadi hanya",
                    "          boleh angka, string, atau bool literal. Otomatis",
                    "          static. Nilainya disalin ke setiap tempat yang",
                    "          memakainya.",
                    "  readonly nilainya ditetapkan saat OBJEK DIBUAT, boleh",
                    "          hasil perhitungan, dan sesudah itu tidak bisa",
                    "          diubah lagi.",
                    "",
                    "Konversi tipe ada dua arah, dan namanya menjelaskan risikonya:",
                    "",
                    "  IMPLICIT (melebar, aman, otomatis)",
                    "    int i = 42;",
                    "    long l = i;        muat pasti, tidak perlu ditulis",
                    "    double d = i;      muat pasti",
                    "",
                    "  EXPLICIT (menyempit, berisiko, wajib ditulis)",
                    "    double d = 9.87;",
                    "    int i = (int)d;    hasilnya 9 -- DIPOTONG, bukan dibulatkan",
                    "",
                    "Yang sering mengejutkan: (int) memotong, bukan membulatkan.",
                    "9.87 jadi 9, dan -9.87 jadi -9. Kalau maksudmu membulatkan,",
                    "pakai Math.Round.",
                    "",
                    "Dari teks ke angka ada tiga cara, dan pilihannya penting:",
                    "",
                    "  int.Parse(\"42\")              melempar exception kalau gagal",
                    "  Convert.ToInt32(\"42\")        null jadi 0, sisanya exception",
                    "  int.TryParse(\"42\", out n)    mengembalikan bool, tidak melempar",
                    "",
                    "Untuk input dari pengguna, TryParse hampir selalu jawabannya.",
                    "Pengguna salah ketik itu kejadian normal, bukan keadaan luar",
                    "biasa — dan exception ongkosnya jauh lebih mahal daripada",
                    "sebuah bool.",
                ]
            },
            {
                "heading": "TryParse: pola yang dipakai di kode sungguhan",
                "code": """using System;

class Program
{
    static void Main()
    {
        string[] masukan = { "42", "3.5", "sembilan", "" };

        foreach (string teks in masukan)
        {
            if (int.TryParse(teks, out int angka))
                Console.WriteLine($"\\"{teks}\\" -> {angka}");
            else
                Console.WriteLine($"\\"{teks}\\" -> bukan bilangan bulat");
        }
    }
}"""
            },
            {
                "body": [
                    "Perhatikan `out int angka` yang dideklarasikan langsung di",
                    "dalam pemanggilan. Sebelum C# 7 kamu harus menulis",
                    "`int angka;` di baris terpisah lebih dulu. Bentuk baru ini",
                    "membuat variabelnya hidup persis di tempat ia berarti.",
                    "",
                    "Keluaran program di atas:",
                    "  \"42\" -> 42",
                    "  \"3.5\" -> bukan bilangan bulat",
                    "  \"sembilan\" -> bukan bilangan bulat",
                    "  \"\" -> bukan bilangan bulat",
                    "",
                    "\"3.5\" gagal karena yang diminta int, bukan karena teksnya",
                    "bukan angka. double.TryParse akan menerimanya.",
                ]
            },
        ],
    },
    {
        "title": "3. Operator & Ekspresi",
        "sections": [
            {
                "body": [
                    "Operator aritmetika:",
                    "  +   tambah          a + b",
                    "  -   kurang          a - b",
                    "  *   kali            a * b",
                    "  /   bagi            a / b",
                    "  %   sisa bagi       a % b",
                    "",
                    "Jebakan pertama setiap pemula C#: 7 / 2 hasilnya 3, bukan 3.5.",
                    "Kalau KEDUA sisinya bilangan bulat, pembagiannya pembagian",
                    "bulat dan sisanya dibuang. Supaya jadi 3.5, salah satu sisi",
                    "harus pecahan:",
                    "",
                    "  7 / 2         3",
                    "  7.0 / 2       3.5",
                    "  (double)7 / 2 3.5",
                    "  7 / 2.0       3.5",
                    "",
                    "Operator penugasan gabungan:",
                    "  +=  -=  *=  /=  %=",
                    "  x += 5  sama dengan  x = x + 5",
                    "",
                    "Tambah/kurang satu:",
                    "  i++   pakai nilainya DULU, baru tambah",
                    "  ++i   tambah DULU, baru pakai nilainya",
                    "",
                    "  int i = 5;",
                    "  Console.WriteLine(i++);   cetak 5, i jadi 6",
                    "  Console.WriteLine(++i);   i jadi 7, cetak 7",
                    "",
                    "Operator perbandingan menghasilkan bool:",
                    "  ==  !=  <  >  <=  >=",
                    "",
                    "Operator logika:",
                    "  &&  DAN, hubung-singkat",
                    "  ||  ATAU, hubung-singkat",
                    "  !   NEGASI",
                    "",
                    "Hubung-singkat (short-circuit) artinya sisi kanan TIDAK",
                    "dievaluasi kalau hasilnya sudah pasti dari sisi kiri.",
                    "Ini bukan optimasi kecil — ia yang membuat pola pengaman",
                    "di bawah ini aman:",
                    "",
                    "  if (nama != null && nama.Length > 0)",
                    "",
                    "Kalau nama null, sisi kanan tidak pernah dijalankan dan",
                    "NullReferenceException tidak terjadi. Dengan & (satu",
                    "ampersand) kedua sisi selalu dievaluasi, dan kode itu",
                    "akan meledak.",
                ]
            },
            {
                "heading": "Operator khas C# yang menghemat banyak baris",
                "code": """using System;

class Program
{
    static void Main()
    {
        int nilai = 78;

        // Ternary: kondisi ? kalau benar : kalau salah
        string status = nilai >= 75 ? "Lulus" : "Tidak Lulus";
        Console.WriteLine(status);

        // Null-coalescing: pakai kiri kalau bukan null, kalau null pakai kanan
        string? masukan = null;
        string nama = masukan ?? "Tanpa Nama";
        Console.WriteLine(nama);

        // Null-coalescing assignment: isi HANYA kalau masih null
        string? catatan = null;
        catatan ??= "belum ada catatan";
        Console.WriteLine(catatan);

        // Null-conditional: panggil HANYA kalau bukan null
        string? kosong = null;
        Console.WriteLine(kosong?.Length ?? -1);   // -1
    }
}"""
            },
            {
                "body": [
                    "Empat operator di atas yang membuat kode C# modern jauh",
                    "lebih pendek daripada C# lama:",
                    "",
                    "  ?:    ternary, sudah ada sejak awal",
                    "  ??    null-coalescing",
                    "  ??=   null-coalescing assignment",
                    "  ?.    null-conditional, sering disebut Elvis operator",
                    "",
                    "`a?.b` berarti: kalau a null, seluruh ekspresinya langsung",
                    "bernilai null tanpa memanggil apa pun. Rantainya ikut",
                    "berhenti, jadi `a?.b.c.d` aman seluruhnya, bukan cuma di",
                    "langkah pertama.",
                    "",
                    "Hasil `a?.b` selalu nullable. Itu sebabnya `kosong?.Length`",
                    "bertipe int? dan perlu `?? -1` supaya jadi int biasa.",
                    "",
                    "Urutan operasi, dari yang paling kuat:",
                    "  1. ()  tanda kurung",
                    "  2. ++  --  !  (tipe)  unary",
                    "  3. *  /  %",
                    "  4. +  -",
                    "  5. <  >  <=  >=",
                    "  6. ==  !=",
                    "  7. &&",
                    "  8. ||",
                    "  9. ?:  ??",
                    "  10. =  +=  -=  dan kawan-kawan",
                    "",
                    "Kalau ragu, pakai tanda kurung. Kode yang jelas lebih",
                    "berharga daripada kode yang membuktikan kamu hafal tabel ini.",
                ]
            },
        ],
    },
    {
        "title": "4. Input, Output & String",
        "sections": [
            {
                "body": [
                    "Mencetak ke layar:",
                    "  Console.Write(\"tanpa pindah baris\");",
                    "  Console.WriteLine(\"dengan pindah baris\");",
                    "",
                    "Membaca dari pengguna:",
                    "  string? baris = Console.ReadLine();",
                    "",
                    "ReadLine mengembalikan string? — dengan tanda tanya. Itu",
                    "bukan kerewelan: kalau masukan habis (misalnya input",
                    "dialirkan dari berkas dan berkasnya selesai), ReadLine",
                    "mengembalikan null. Compiler memaksamu memikirkan hal itu.",
                    "",
                    "Tiga cara menyusun teks, dan yang ketiga yang dipakai",
                    "kode modern:",
                    "",
                    "  1. Penggabungan",
                    "     \"Halo, \" + nama + \"! Umurmu \" + umur",
                    "",
                    "  2. Composite formatting",
                    "     string.Format(\"Halo, {0}! Umurmu {1}\", nama, umur)",
                    "",
                    "  3. String interpolation  (C# 6, paling jelas)",
                    "     $\"Halo, {nama}! Umurmu {umur}\"",
                    "",
                    "Tanda dolar di depan kutip yang mengaktifkannya. Di dalam",
                    "kurung kurawal boleh ekspresi apa pun, bukan cuma nama",
                    "variabel: $\"Total {harga * jumlah:N0}\" sah.",
                    "",
                    "Format setelah titik dua:",
                    "  {n:C}      mata uang       Rp1.234,00",
                    "  {n:N0}     angka, 0 desimal  1.234",
                    "  {n:F2}     pecahan, 2 desimal 1234,00",
                    "  {n:P1}     persen          12,3%",
                    "  {n:X}      heksadesimal    4D2",
                    "  {t:yyyy-MM-dd}  tanggal     2026-09-22",
                    "",
                    "Perataan memakai koma: {nama,-15} rata kiri selebar 15,",
                    "{harga,10} rata kanan selebar 10. Inilah cara membuat",
                    "tabel di konsol tanpa satu pun spasi diketik manual.",
                ]
            },
            {
                "heading": "Tabel rapi dengan perataan",
                "code": """using System;

class Program
{
    static void Main()
    {
        string[] nama = { "Keyboard", "Mouse", "Monitor" };
        int[] jumlah = { 3, 12, 2 };
        decimal[] harga = { 350000m, 85000m, 1750000m };

        Console.WriteLine($"{"Barang",-12}{"Qty",5}{"Harga",15}");
        Console.WriteLine(new string('-', 32));

        decimal total = 0;
        for (int i = 0; i < nama.Length; i++)
        {
            decimal sub = jumlah[i] * harga[i];
            total += sub;
            Console.WriteLine($"{nama[i],-12}{jumlah[i],5}{sub,15:N0}");
        }

        Console.WriteLine(new string('-', 32));
        Console.WriteLine($"{"TOTAL",-12}{"",5}{total,15:N0}");
    }
}"""
            },
            {
                "body": [
                    "Method string yang paling sering dipakai:",
                    "",
                    "  s.Length              panjang, PROPERTY bukan method",
                    "  s.ToUpper()           jadi huruf besar semua",
                    "  s.ToLower()           jadi huruf kecil semua",
                    "  s.Trim()              buang spasi di kedua ujung",
                    "  s.Substring(2, 4)     4 karakter mulai index 2",
                    "  s.IndexOf(\"abc\")      posisi pertama, -1 kalau tidak ada",
                    "  s.Contains(\"abc\")     true / false",
                    "  s.StartsWith(\"ab\")    true / false",
                    "  s.Replace(\"a\", \"b\")   ganti semua kemunculan",
                    "  s.Split(',')          pecah jadi array",
                    "  string.Join(\", \", a)  gabung array jadi satu string",
                    "",
                    "SATU HAL yang harus ditanam sekarang juga: string di C#",
                    "IMMUTABLE. s.ToUpper() TIDAK mengubah s — ia membuat string",
                    "baru dan mengembalikannya. Kalau hasilnya tidak ditampung,",
                    "tidak terjadi apa-apa:",
                    "",
                    "  nama.ToUpper();          tidak berguna, hasilnya dibuang",
                    "  nama = nama.ToUpper();   ini yang benar",
                    "",
                    "Memeriksa string kosong, dan bedanya penting:",
                    "  string.IsNullOrEmpty(s)        null atau \"\"",
                    "  string.IsNullOrWhiteSpace(s)   null, \"\", atau \"   \"",
                    "",
                    "Untuk memvalidasi masukan pengguna, IsNullOrWhiteSpace",
                    "hampir selalu yang kamu maksud — orang yang menekan spasi",
                    "lalu Enter tidak mengisi apa pun.",
                ]
            },
            {
                "heading": "Verbatim dan raw string: kabur dari backslash",
                "code": """using System;

class Program
{
    static void Main()
    {
        // Biasa: backslash harus digandakan
        string a = "C:\\\\Users\\\\Andi\\\\Dokumen";

        // Verbatim (@): apa adanya, backslash tidak istimewa
        string b = @"C:\\Users\\Andi\\Dokumen";

        // Verbatim juga menyimpan baris baru apa adanya
        string c = @"baris satu
baris dua";

        Console.WriteLine(a);
        Console.WriteLine(b);
        Console.WriteLine(c);
    }
}"""
            },
            {
                "body": [
                    "Tiga bentuk penulisan string:",
                    "",
                    "  \"biasa\"    escape berlaku: \\n baris baru, \\t tab,",
                    "              \\\" kutip, \\\\ backslash.",
                    "  @\"verbatim\" escape TIDAK berlaku. Berguna untuk path",
                    "              Windows dan pola regex. Untuk menulis kutip",
                    "              dua di dalamnya, gandakan: @\"dia bilang \"\"hai\"\"\"",
                    "  \"\"\"raw\"\"\"   sejak C# 11. Tiga kutip atau lebih, tidak",
                    "              perlu escape apa pun, indentasi penutup",
                    "              dipotong otomatis dari tiap baris.",
                    "",
                    "Keduanya bisa digabung dengan interpolasi: $@\"...\" atau",
                    "$\"\"\"...\"\"\".",
                    "",
                    "Menggabung string di dalam perulangan panjang adalah",
                    "kesalahan performa klasik. Karena string immutable, tiap",
                    "`s += x` membuat string BARU dan menyalin seluruh isinya.",
                    "Seribu penggabungan berarti seribu penyalinan yang makin",
                    "lama makin besar. Untuk itu ada StringBuilder:",
                    "",
                    "  var sb = new StringBuilder();",
                    "  for (int i = 0; i < 1000; i++) sb.Append(i).Append(' ');",
                    "  string hasil = sb.ToString();",
                    "",
                    "Untuk lima atau sepuluh penggabungan, jangan repot —",
                    "interpolasi lebih terbaca dan selisihnya tidak terukur.",
                ]
            },
        ],
    },
    {
        "title": "5. Percabangan: if, switch & Pattern Matching",
        "sections": [
            {
                "body": [
                    "Bentuk dasar:",
                    "",
                    "  if (nilai >= 75)",
                    "  {",
                    "      Console.WriteLine(\"Lulus\");",
                    "  }",
                    "  else if (nilai >= 60)",
                    "  {",
                    "      Console.WriteLine(\"Mengulang\");",
                    "  }",
                    "  else",
                    "  {",
                    "      Console.WriteLine(\"Tidak Lulus\");",
                    "  }",
                    "",
                    "Kurung kurawal boleh dihilangkan untuk SATU pernyataan,",
                    "tapi jangan. Bug paling terkenal dalam sejarah yang",
                    "disebabkan hal ini (goto fail; di Apple, 2014) terjadi",
                    "persis karena seseorang menambah baris kedua di bawah if",
                    "tanpa kurawal, dan baris itu ternyata selalu dijalankan.",
                    "",
                    "Kondisi WAJIB bool. Tidak ada 'nilai bukan nol berarti",
                    "benar' seperti di C. `if (5)` tidak bisa dikompilasi, dan",
                    "`if (x = 5)` juga tidak — karena hasil penugasan itu int,",
                    "bukan bool. Seluruh kelas bug itu hilang begitu saja.",
                    "",
                    "switch klasik, untuk mencocokkan satu nilai ke banyak",
                    "kemungkinan:",
                    "",
                    "  switch (hari)",
                    "  {",
                    "      case 1:",
                    "      case 2:",
                    "          Console.WriteLine(\"Awal pekan\");",
                    "          break;",
                    "      case 6:",
                    "      case 7:",
                    "          Console.WriteLine(\"Akhir pekan\");",
                    "          break;",
                    "      default:",
                    "          Console.WriteLine(\"Tengah pekan\");",
                    "          break;",
                    "  }",
                    "",
                    "break WAJIB di C#. Tidak seperti C atau Java, C# MENOLAK",
                    "kompilasi kalau sebuah case berisi kode tapi tidak diakhiri",
                    "break, return, atau goto case. Fall-through yang tidak",
                    "disengaja — sumber bug yang tak terhitung di C — dijadikan",
                    "error di sini.",
                    "",
                    "Case kosong yang ditumpuk (case 1: case 2:) tetap boleh,",
                    "karena di situ niatnya jelas.",
                ]
            },
            {
                "heading": "switch expression: bentuk modern sejak C# 8",
                "code": """using System;

class Program
{
    static string Grade(int nilai) => nilai switch
    {
        >= 85 => "A",
        >= 75 => "B",
        >= 60 => "C",
        >= 40 => "D",
        _     => "E",
    };

    static void Main()
    {
        int[] nilai = { 92, 78, 65, 45, 20 };
        foreach (int n in nilai)
            Console.WriteLine($"{n,3} -> {Grade(n)}");
    }
}"""
            },
            {
                "body": [
                    "Bedanya dengan switch klasik ada tiga, dan ketiganya",
                    "sengaja:",
                    "",
                    "  1. Ia EKSPRESI, jadi menghasilkan nilai. Bisa langsung",
                    "     dikembalikan atau ditugaskan ke variabel.",
                    "  2. Tidak ada break sama sekali. Tidak ada fall-through",
                    "     yang perlu dicegah karena tidak ada urutan eksekusi —",
                    "     hanya pencocokan.",
                    "  3. Compiler MEMPERINGATKAN kalau ada kemungkinan nilai",
                    "     yang tidak tertangani. `_` adalah penangkap sisanya,",
                    "     setara default.",
                    "",
                    "Yang di sebelah kiri `=>` disebut POLA (pattern), dan",
                    "polanya jauh lebih kaya daripada sekadar nilai:",
                    "",
                    "  Pola konstanta   0, \"halo\", true",
                    "  Pola relasional  >= 85, < 0",
                    "  Pola tipe        int n, string s",
                    "  Pola logika      > 0 and < 10, \"a\" or \"b\", not null",
                    "  Pola properti    { Length: 0 }, { Umur: >= 17 }",
                    "  Pola tuple       (0, 0), (var x, var y)",
                    "  Pola list        [], [_], [1, .., 9]   (C# 11)",
                ]
            },
            {
                "heading": "Pattern matching pada tipe dan properti",
                "code": """using System;

class Program
{
    static string Jelaskan(object o) => o switch
    {
        null                      => "tidak ada apa-apa",
        int n when n < 0          => $"bilangan negatif {n}",
        int n                     => $"bilangan {n}",
        string { Length: 0 }      => "teks kosong",
        string s                  => $"teks {s.Length} huruf",
        bool b                    => b ? "benar" : "salah",
        int[] { Length: > 3 }     => "array panjang",
        int[] a                   => $"array {a.Length} elemen",
        _                         => $"tipe lain: {o.GetType().Name}",
    };

    static void Main()
    {
        object[] contoh = { null, -5, 42, "", "halo", true,
                            new[] { 1, 2 }, new[] { 1, 2, 3, 4 }, 3.14 };
        foreach (object o in contoh)
            Console.WriteLine(Jelaskan(o));
    }
}"""
            },
            {
                "body": [
                    "Dua hal yang perlu diperhatikan di contoh di atas:",
                    "",
                    "  URUTAN BERARTI. `int n when n < 0` harus ditulis SEBELUM",
                    "  `int n`, karena pencocokan berhenti di pola pertama yang",
                    "  cocok. Kalau dibalik, cabang negatif tidak akan pernah",
                    "  tercapai — dan compiler memang akan memperingatkanmu.",
                    "",
                    "  `when` menambahkan syarat tambahan di atas polanya.",
                    "  Bedakan dari pola relasional: `int n when n < 0` dan",
                    "  `< 0` sama hasilnya di sini, tapi `when` bisa memuat",
                    "  ekspresi apa pun, termasuk memanggil method.",
                    "",
                    "Keluaran program:",
                    "  tidak ada apa-apa",
                    "  bilangan negatif -5",
                    "  bilangan 42",
                    "  teks kosong",
                    "  teks 5 huruf",
                    "  benar",
                    "  array 2 elemen",
                    "  array panjang",
                    "  tipe lain: Double",
                    "",
                    "Pattern matching adalah salah satu hal yang membuat C#",
                    "modern terasa berbeda dari C# 2005. Rantai if-else",
                    "bertingkat yang dulu panjang sekarang jadi satu ekspresi",
                    "yang bisa dibaca dari atas ke bawah seperti tabel.",
                ]
            },
        ],
    },
    {
        "title": "6. Perulangan: for, while, foreach",
        "sections": [
            {
                "body": [
                    "Empat bentuk perulangan, dan masing-masing punya tempat:",
                    "",
                    "  for       tahu persis berapa kali",
                    "  while     ulang selama syaratnya benar, mungkin nol kali",
                    "  do-while  sama, tapi dijamin jalan MINIMAL sekali",
                    "  foreach   telusuri setiap isi koleksi",
                    "",
                    "for:",
                    "  for (int i = 0; i < 5; i++)",
                    "  {",
                    "      Console.WriteLine(i);      cetak 0 1 2 3 4",
                    "  }",
                    "",
                    "Tiga bagiannya: nilai awal; syarat lanjut; langkah.",
                    "Ketiganya boleh kosong — `for (;;)` adalah perulangan",
                    "abadi yang sah.",
                    "",
                    "while:",
                    "  int sisa = 3;",
                    "  while (sisa > 0)",
                    "  {",
                    "      Console.WriteLine($\"sisa {sisa}\");",
                    "      sisa--;",
                    "  }",
                    "",
                    "do-while, perhatikan titik koma di akhir:",
                    "  do",
                    "  {",
                    "      Console.WriteLine(\"jalan minimal sekali\");",
                    "  } while (false);",
                    "",
                    "foreach, bentuk yang paling sering dipakai:",
                    "  foreach (string nama in daftar)",
                    "      Console.WriteLine(nama);",
                    "",
                    "Aturan keras foreach: variabel perulangannya TIDAK BISA",
                    "diubah, dan koleksinya tidak boleh ditambah atau dikurangi",
                    "selama perulangan berjalan. Melanggar yang kedua melempar",
                    "InvalidOperationException saat program jalan, bukan saat",
                    "kompilasi. Kalau perlu menghapus sambil menelusuri, buat",
                    "salinan dulu atau telusuri mundur dengan for.",
                    "",
                    "Mengendalikan perulangan:",
                    "  break     keluar dari perulangan TERDEKAT",
                    "  continue  lompat ke iterasi berikutnya",
                    "",
                    "C# tidak punya `break 2` seperti PHP. Untuk keluar dari",
                    "dua perulangan sekaligus, pindahkan bagian dalamnya ke",
                    "sebuah method lalu return — hampir selalu lebih terbaca",
                    "daripada label dan goto, yang juga ada tapi sebaiknya",
                    "tidak kamu pakai.",
                ]
            },
            {
                "heading": "Perulangan bersarang: tabel perkalian",
                "code": """using System;

class Program
{
    static void Main()
    {
        Console.Write("    ");
        for (int k = 1; k <= 9; k++) Console.Write($"{k,4}");
        Console.WriteLine();
        Console.WriteLine(new string('-', 40));

        for (int b = 1; b <= 9; b++)
        {
            Console.Write($"{b,2} |");
            for (int k = 1; k <= 9; k++)
                Console.Write($"{b * k,4}");
            Console.WriteLine();
        }
    }
}"""
            },
            {
                "body": [
                    "Perulangan bersarang: yang dalam selesai SELURUHNYA untuk",
                    "setiap satu putaran yang luar. Di contoh atas, 9 baris",
                    "kali 9 kolom = 81 kali badan perulangan dalam dijalankan.",
                    "",
                    "Kesalahan yang paling sering: `Console.WriteLine()` untuk",
                    "pindah baris diletakkan di dalam perulangan dalam. Hasilnya",
                    "81 baris, masing-masing satu angka.",
                    "",
                    "Dua pola perulangan yang layak dihafal karena muncul di",
                    "mana-mana:",
                    "",
                    "  AKUMULATOR — kumpulkan hasil",
                    "    int total = 0;",
                    "    foreach (int n in angka) total += n;",
                    "",
                    "  PENJAGA — cari yang pertama cocok lalu berhenti",
                    "    string? ketemu = null;",
                    "    foreach (string s in daftar)",
                    "        if (s.StartsWith(\"A\")) { ketemu = s; break; }",
                    "",
                    "Keduanya nanti punya bentuk satu barisnya di LINQ",
                    "(Sum dan FirstOrDefault), tapi memahami bentuk panjangnya",
                    "dulu membuat LINQ terasa seperti singkatan, bukan sihir.",
                ]
            },
        ],
    },
    {
        "title": "7. Array & Indeks",
        "sections": [
            {
                "body": [
                    "Array menyimpan sejumlah TETAP nilai bertipe sama.",
                    "Ukurannya ditetapkan saat dibuat dan tidak bisa berubah.",
                    "",
                    "Membuat array:",
                    "  int[] a = new int[5];              5 elemen, semua 0",
                    "  int[] b = { 10, 20, 30 };          langsung berisi",
                    "  int[] c = new int[] { 10, 20 };    bentuk panjangnya",
                    "  var d = new[] { 10, 20, 30 };      tipe disimpulkan",
                    "",
                    "Nilai awal elemen array selalu 'zero value' tipenya:",
                    "  angka  -> 0",
                    "  bool   -> false",
                    "  char   -> '\\0'",
                    "  tipe referensi (string, class) -> null",
                    "",
                    "Mengakses:",
                    "  a[0] = 7;              index dimulai dari NOL",
                    "  Console.WriteLine(a[0]);",
                    "  Console.WriteLine(a.Length);",
                    "",
                    "Index di luar jangkauan melempar IndexOutOfRangeException",
                    "saat program jalan. Array dengan 5 elemen punya index 0",
                    "sampai 4; a[5] adalah error, dan ini kesalahan nomor satu",
                    "sepanjang sejarah pemrograman.",
                    "",
                    "Index dari belakang, sejak C# 8:",
                    "  a[^1]     elemen TERAKHIR",
                    "  a[^2]     satu sebelum terakhir",
                    "",
                    "Baca ^ sebagai 'dari akhir'. a[^1] setara a[a.Length - 1],",
                    "tapi jauh lebih sulit ditulis salah.",
                    "",
                    "Rentang (range), juga C# 8:",
                    "  a[1..4]   elemen index 1, 2, 3   (batas atas EKSKLUSIF)",
                    "  a[..3]    tiga elemen pertama",
                    "  a[2..]    dari index 2 sampai habis",
                    "  a[..]     salinan seluruhnya",
                    "",
                    "Batas atas eksklusif itu konsisten dengan Substring dan",
                    "dengan cara berpikir 'panjangnya = akhir - awal'.",
                ]
            },
            {
                "heading": "Array, statistik, dan pengurutan",
                "code": """using System;

class Program
{
    static void Main()
    {
        int[] nilai = { 78, 92, 65, 88, 71, 95, 59 };

        int total = 0, tertinggi = nilai[0], terendah = nilai[0];
        foreach (int n in nilai)
        {
            total += n;
            if (n > tertinggi) tertinggi = n;
            if (n < terendah) terendah = n;
        }

        Console.WriteLine($"Jumlah data : {nilai.Length}");
        Console.WriteLine($"Total       : {total}");
        Console.WriteLine($"Rata-rata   : {(double)total / nilai.Length:F2}");
        Console.WriteLine($"Tertinggi   : {tertinggi}");
        Console.WriteLine($"Terendah    : {terendah}");

        int[] urut = (int[])nilai.Clone();
        Array.Sort(urut);
        Console.WriteLine($"Terurut     : {string.Join(", ", urut)}");
        Console.WriteLine($"Dua terbesar: {string.Join(", ", urut[^2..])}");
    }
}"""
            },
            {
                "body": [
                    "Perhatikan `(double)total / nilai.Length`. Tanpa (double),",
                    "dua int dibagi dan hasilnya dipotong jadi bilangan bulat.",
                    "Ini jebakan paling sering di perhitungan rata-rata.",
                    "",
                    "`nilai.Clone()` membuat SALINAN. Tanpa itu, Array.Sort",
                    "akan mengurutkan array aslinya — array adalah tipe",
                    "referensi, jadi `int[] urut = nilai;` cuma memberi nama",
                    "kedua untuk array yang sama, bukan salinan.",
                    "",
                    "Ini bedanya tipe nilai dan tipe referensi, dan array",
                    "adalah tempat pertama kamu menabraknya:",
                    "",
                    "  int a = 5; int b = a; b = 9;      a tetap 5",
                    "  int[] x = {1}; int[] y = x; y[0]=9;  x[0] JADI 9",
                    "",
                    "Method statis kelas Array yang berguna:",
                    "  Array.Sort(a)            urutkan menaik, mengubah a",
                    "  Array.Reverse(a)         balik urutannya, mengubah a",
                    "  Array.IndexOf(a, 5)      posisi pertama, -1 kalau tidak ada",
                    "  Array.Fill(a, 7)         isi semua elemen dengan 7",
                    "  Array.Resize(ref a, 10)  buat array baru lalu salin isinya",
                    "",
                    "Array.Resize namanya menipu: array tidak bisa diubah",
                    "ukurannya. Yang terjadi adalah array BARU dibuat, isi",
                    "lama disalin, lalu referensimu ditunjuk ke yang baru.",
                    "Kalau kamu sering perlu menambah dan menghapus, yang",
                    "kamu butuhkan bukan array melainkan List<T>.",
                ]
            },
            {
                "heading": "Array dua dimensi dan array bergerigi",
                "code": """using System;

class Program
{
    static void Main()
    {
        // Persegi panjang: satu blok memori, semua baris sama panjang
        int[,] kotak = new int[3, 4];
        kotak[0, 0] = 1;
        kotak[2, 3] = 9;
        Console.WriteLine($"baris {kotak.GetLength(0)}, kolom {kotak.GetLength(1)}");

        // Bergerigi (jagged): array berisi array, tiap baris bebas panjangnya
        int[][] gerigi = new int[3][];
        gerigi[0] = new[] { 1 };
        gerigi[1] = new[] { 1, 2 };
        gerigi[2] = new[] { 1, 2, 3 };

        foreach (int[] baris in gerigi)
            Console.WriteLine(string.Join(" ", baris));
    }
}"""
            },
            {
                "body": [
                    "Dua bentuk array bertingkat, dan tanda bacanya yang",
                    "membedakan:",
                    "",
                    "  int[,]   satu KOMA di dalam kurung -> dua dimensi",
                    "           persegi panjang. Satu objek, satu blok memori,",
                    "           semua baris wajib sama panjang.",
                    "  int[][]  dua pasang kurung -> array dari array.",
                    "           Setiap baris objek sendiri, panjangnya bebas.",
                    "",
                    "Aksesnya juga beda: kotak[1, 2] versus gerigi[1][2].",
                    "",
                    "Untuk matriks dan papan permainan, `int[,]` lebih tepat",
                    "dan lebih cepat. Untuk data yang tiap barisnya beda",
                    "panjang (daftar nilai tiap murid, misalnya), jagged yang",
                    "benar. Kalau salah pilih, yang rugi bukan cuma performa",
                    "melainkan seluruh kode yang membacanya jadi berbelit.",
                ]
            },
        ],
    },
    {
        "title": "8. List, Dictionary & Koleksi Generik",
        "sections": [
            {
                "body": [
                    "Array ukurannya tetap. Untuk koleksi yang tumbuh dan",
                    "menyusut, .NET menyediakan koleksi generik di namespace",
                    "System.Collections.Generic.",
                    "",
                    "Huruf T di List<T> berarti 'tipe apa pun yang kamu",
                    "tentukan'. List<int> menyimpan int, List<string>",
                    "menyimpan string, dan compiler memastikan tidak ada yang",
                    "salah masuk.",
                    "",
                    "List<T> — array yang bisa tumbuh:",
                    "  var nama = new List<string>();",
                    "  nama.Add(\"Andi\");",
                    "  nama.Add(\"Budi\");",
                    "  nama.Insert(0, \"Ani\");       sisipkan di index 0",
                    "  nama.Remove(\"Budi\");         hapus berdasarkan NILAI",
                    "  nama.RemoveAt(0);            hapus berdasarkan INDEX",
                    "  nama.Count                   jumlah isi (bukan Length!)",
                    "  nama.Contains(\"Andi\")        true / false",
                    "  nama.Sort();                 urutkan di tempat",
                    "  nama.Clear();                kosongkan",
                    "",
                    "Array pakai .Length, List pakai .Count. Tidak ada alasan",
                    "mendalam untuk perbedaan ini selain sejarah, dan setiap",
                    "programmer C# pernah salah menuliskannya.",
                    "",
                    "Dictionary<TKey, TValue> — pasangan kunci-nilai:",
                    "  var umur = new Dictionary<string, int>();",
                    "  umur[\"Andi\"] = 20;",
                    "  umur[\"Budi\"] = 22;",
                    "  umur.Add(\"Cici\", 19);   melempar kalau kunci sudah ada",
                    "  umur[\"Andi\"] = 21;      menimpa diam-diam",
                    "",
                    "Membaca kunci yang tidak ada dengan umur[\"Dedi\"] melempar",
                    "KeyNotFoundException. Dua cara amannya:",
                    "",
                    "  if (umur.TryGetValue(\"Dedi\", out int u)) ...",
                    "  if (umur.ContainsKey(\"Dedi\")) ...",
                    "",
                    "TryGetValue lebih baik: ContainsKey lalu mengambilnya",
                    "berarti mencari dua kali di tabel hash yang sama.",
                ]
            },
            {
                "heading": "Menghitung frekuensi kata",
                "code": """using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string kalimat = "satu dua dua tiga tiga tiga empat";
        string[] kata = kalimat.Split(' ');

        var hitung = new Dictionary<string, int>();
        foreach (string k in kata)
        {
            // Kunci baru otomatis dimulai dari 0 lewat out
            hitung.TryGetValue(k, out int n);
            hitung[k] = n + 1;
        }

        foreach (KeyValuePair<string, int> pasangan in hitung)
            Console.WriteLine($"{pasangan.Key,-6} : {pasangan.Value}");

        Console.WriteLine($"Kata unik  : {hitung.Count}");
        Console.WriteLine($"Total kata : {kata.Length}");
    }
}"""
            },
            {
                "body": [
                    "Pola `TryGetValue(k, out int n)` lalu `hitung[k] = n + 1`",
                    "adalah idiom penghitung frekuensi di C#. Kalau kuncinya",
                    "belum ada, TryGetValue mengembalikan false DAN mengisi n",
                    "dengan 0 — jadi n + 1 tetap benar tanpa satu pun if.",
                    "",
                    "Menelusuri Dictionary memberi KeyValuePair<TKey, TValue>",
                    "dengan properti .Key dan .Value. Sejak C# 7 kamu bisa",
                    "memecahnya langsung:",
                    "",
                    "  foreach (var (nama, umur) in kamus)",
                    "      Console.WriteLine($\"{nama} {umur}\");",
                    "",
                    "PENTING: urutan penelusuran Dictionary TIDAK DIJAMIN.",
                    "Ia kebetulan sering mengikuti urutan penyisipan, dan",
                    "itu jebakan — begitu ada penghapusan, urutannya berubah.",
                    "Kalau urutan penting, urutkan eksplisit dengan LINQ",
                    "(OrderBy) atau pakai SortedDictionary.",
                    "",
                    "Koleksi generik lain yang perlu kamu kenal:",
                    "",
                    "  HashSet<T>       himpunan, tanpa duplikat, cek cepat",
                    "  Queue<T>         antre: Enqueue masuk, Dequeue keluar (FIFO)",
                    "  Stack<T>         tumpuk: Push masuk, Pop keluar (LIFO)",
                    "  SortedDictionary selalu terurut berdasarkan kunci",
                    "  LinkedList<T>    sisip/hapus di tengah murah",
                    "",
                    "Aturan memilih: butuh index -> List. Butuh pencarian",
                    "berdasarkan nama -> Dictionary. Butuh 'sudah pernah",
                    "dilihat belum' -> HashSet. Sisanya jarang.",
                ]
            },
            {
                "heading": "HashSet, Queue, dan Stack dalam satu program",
                "code": """using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var unik = new HashSet<int> { 1, 2, 2, 3, 3, 3 };
        Console.WriteLine($"HashSet : {string.Join(",", unik)}");
        Console.WriteLine($"Add 2 lagi berhasil? {unik.Add(2)}");

        var antre = new Queue<string>();
        antre.Enqueue("Andi");
        antre.Enqueue("Budi");
        antre.Enqueue("Cici");
        Console.WriteLine($"Dilayani: {antre.Dequeue()}");
        Console.WriteLine($"Berikut : {antre.Peek()}");

        var tumpuk = new Stack<string>();
        tumpuk.Push("halaman-1");
        tumpuk.Push("halaman-2");
        tumpuk.Push("halaman-3");
        Console.WriteLine($"Kembali : {tumpuk.Pop()}");
        Console.WriteLine($"Sekarang: {tumpuk.Peek()}");
    }
}"""
            },
            {
                "body": [
                    "Keluaran program:",
                    "  HashSet : 1,2,3",
                    "  Add 2 lagi berhasil? False",
                    "  Dilayani: Andi",
                    "  Berikut : Budi",
                    "  Kembali : halaman-3",
                    "  Sekarang: halaman-2",
                    "",
                    "HashSet.Add mengembalikan bool: true kalau benar-benar",
                    "ditambahkan, false kalau sudah ada. Itu cara terpendek",
                    "menulis 'kerjakan hanya kalau belum pernah dilihat':",
                    "",
                    "  if (sudahDiproses.Add(id)) Proses(id);",
                    "",
                    "Queue = antrean kasir. Yang datang duluan dilayani duluan.",
                    "Stack = tumpukan piring. Yang ditaruh terakhir diambil",
                    "duluan — persis seperti tombol Back di browser, yang",
                    "memang diimplementasikan dengan stack.",
                    "",
                    "Peek melihat tanpa mengambil; Dequeue dan Pop mengambil.",
                    "Keduanya melempar InvalidOperationException kalau kosong,",
                    "jadi periksa .Count dulu atau pakai TryDequeue/TryPop.",
                ]
            },
        ],
    },
    {
        "title": "9. Method, Parameter & Overloading",
        "sections": [
            {
                "body": [
                    "Method adalah blok kode bernama yang bisa dipanggil ulang.",
                    "Bentuk lengkapnya:",
                    "",
                    "  [akses] [static] TipeKembalian Nama(parameter)",
                    "  {",
                    "      ...",
                    "      return nilai;",
                    "  }",
                    "",
                    "  static int Tambah(int a, int b)",
                    "  {",
                    "      return a + b;",
                    "  }",
                    "",
                    "void berarti tidak mengembalikan apa-apa. Di method void,",
                    "`return;` polos boleh dipakai untuk keluar lebih awal.",
                    "",
                    "Expression-bodied member, untuk method satu ekspresi:",
                    "  static int Tambah(int a, int b) => a + b;",
                    "",
                    "Tanda => di sini bukan lambda; ia cuma singkatan dari",
                    "{ return ...; }. Bentuk ini berlaku juga untuk property,",
                    "constructor, dan operator.",
                    "",
                    "Parameter opsional, dengan nilai bawaan:",
                    "  static void Sapa(string nama, string salam = \"Halo\")",
                    "  Sapa(\"Andi\");                 -> Halo, Andi",
                    "  Sapa(\"Budi\", \"Selamat pagi\"); -> Selamat pagi, Budi",
                    "",
                    "Parameter opsional wajib diletakkan SESUDAH yang wajib,",
                    "dan nilai bawaannya harus konstanta saat kompilasi.",
                    "",
                    "Argumen bernama, supaya pemanggilan terbaca:",
                    "  Sapa(salam: \"Hai\", nama: \"Cici\");",
                    "",
                    "Ini bukan kosmetik. `Gambar(true, false, true)` tidak",
                    "memberi tahu apa pun; `Gambar(tebal: true, miring: false,",
                    "garisBawah: true)` menjelaskan dirinya sendiri.",
                    "",
                    "params — jumlah argumen bebas:",
                    "  static int Total(params int[] angka)",
                    "  Total(1, 2, 3);        boleh",
                    "  Total();               boleh, array kosong",
                    "  Total(new[] {1, 2});   boleh juga",
                    "",
                    "params harus jadi parameter TERAKHIR, dan cuma boleh satu.",
                ]
            },
            {
                "heading": "ref, out, dan in: tiga cara mengoper",
                "code": """using System;

class Program
{
    // ref  : boleh dibaca dan diubah, wajib sudah berisi sebelum dipanggil
    static void Tukar(ref int a, ref int b)
    {
        (a, b) = (b, a);
    }

    // out  : WAJIB diisi di dalam method, isi sebelumnya tidak dibaca
    static void Bagi(int a, int b, out int hasil, out int sisa)
    {
        hasil = a / b;
        sisa = a % b;
    }

    // in   : hanya dibaca, tidak boleh diubah
    static double Luas(in double sisi) => sisi * sisi;

    static void Main()
    {
        int x = 3, y = 8;
        Tukar(ref x, ref y);
        Console.WriteLine($"x={x} y={y}");

        Bagi(17, 5, out int h, out int s);
        Console.WriteLine($"17 / 5 = {h} sisa {s}");

        Console.WriteLine($"Luas = {Luas(2.5)}");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  x=8 y=3",
                    "  17 / 5 = 3 sisa 2",
                    "  Luas = 6.25",
                    "",
                    "Tanpa ref, `Tukar` tidak akan berpengaruh apa-apa: yang",
                    "dioper cuma SALINAN nilainya. Dengan ref, yang dioper",
                    "referensi ke variabel aslinya.",
                    "",
                    "Kapan memakai yang mana:",
                    "  ref   method perlu MENGUBAH variabel pemanggil",
                    "  out   method perlu mengembalikan LEBIH DARI SATU nilai",
                    "  in    parameter besar (struct) yang cuma dibaca; tanpa",
                    "        salinan, tapi dijamin tidak berubah",
                    "",
                    "Kata kuncinya wajib ditulis di KEDUA sisi: di deklarasi",
                    "dan di pemanggilan. Itu disengaja — pembaca kode di titik",
                    "pemanggilan langsung tahu variabelnya mungkin berubah.",
                    "",
                    "Untuk mengembalikan dua nilai, tuple sering lebih rapi",
                    "daripada out:",
                    "",
                    "  static (int hasil, int sisa) Bagi(int a, int b)",
                    "      => (a / b, a % b);",
                    "",
                    "  var (h, s) = Bagi(17, 5);",
                    "",
                    "Pakai out kalau salah satu keluarannya adalah 'berhasil",
                    "atau tidak' (pola TryXxx). Pakai tuple kalau keduanya",
                    "sama-sama hasil yang dicari.",
                ]
            },
            {
                "heading": "Overloading: satu nama, banyak bentuk",
                "code": """using System;

class Program
{
    static int Luas(int sisi) => sisi * sisi;
    static int Luas(int panjang, int lebar) => panjang * lebar;
    static double Luas(double jari) => 3.14159 * jari * jari;

    static void Main()
    {
        Console.WriteLine(Luas(5));          // 25   -> persegi
        Console.WriteLine(Luas(4, 6));       // 24   -> persegi panjang
        Console.WriteLine(Luas(2.0));        // 12.56636 -> lingkaran
    }
}"""
            },
            {
                "body": [
                    "Overloading: beberapa method bernama sama yang dibedakan",
                    "oleh JUMLAH atau TIPE parameternya. Compiler memilih",
                    "yang paling cocok saat kompilasi.",
                    "",
                    "Yang TIDAK membedakan overload:",
                    "  - Tipe kembalian. Dua method beda return type tapi",
                    "    parameternya sama adalah error.",
                    "  - Nama parameternya.",
                    "",
                    "Yang membedakan: jumlah, tipe, dan urutan parameter,",
                    "serta ref/out/in.",
                    "",
                    "Perhatikan `Luas(2.0)` — kalau ditulis `Luas(2)` compiler",
                    "memilih versi int dan hasilnya 4, bukan luas lingkaran.",
                    "Overload yang cuma dibedakan int/double adalah sumber",
                    "kebingungan; pertimbangkan nama yang berbeda.",
                    "",
                    "Rekursi — method memanggil dirinya sendiri:",
                    "",
                    "  static long Faktorial(int n)",
                    "      => n <= 1 ? 1 : n * Faktorial(n - 1);",
                    "",
                    "Setiap rekursi WAJIB punya kasus dasar (di sini n <= 1).",
                    "Tanpa itu, tumpukan pemanggilan habis dan program mati",
                    "dengan StackOverflowException — satu-satunya exception di",
                    ".NET yang TIDAK BISA ditangkap dengan try-catch.",
                ]
            },
        ],
    },
    {
        "title": "10. Nullable & Null-Safety",
        "sections": [
            {
                "body": [
                    "Null adalah 'tidak menunjuk apa-apa'. Mengakses anggota",
                    "dari null melempar NullReferenceException — error runtime",
                    "yang oleh penemunya sendiri, Tony Hoare, disebut",
                    "'kesalahan seharga satu miliar dolar'.",
                    "",
                    "C# membagi tipe jadi dua, dan pembagiannya menentukan",
                    "apakah null mungkin:",
                    "",
                    "  TIPE NILAI (value type)",
                    "    int, double, bool, char, struct, enum",
                    "    Disimpan langsung. TIDAK bisa null secara alami.",
                    "",
                    "  TIPE REFERENSI (reference type)",
                    "    string, array, class, interface, delegate",
                    "    Menyimpan alamat. Bisa null.",
                    "",
                    "Untuk membuat tipe nilai bisa null, tambahkan ?:",
                    "  int? umur = null;",
                    "  double? suhu = null;",
                    "",
                    "int? sebenarnya Nullable<int>, sebuah struct dengan dua",
                    "anggota: HasValue dan Value.",
                    "",
                    "  if (umur.HasValue) Console.WriteLine(umur.Value);",
                    "  int pasti = umur ?? 0;",
                    "  int juga = umur.GetValueOrDefault();",
                    "",
                    "Membaca .Value saat HasValue false melempar",
                    "InvalidOperationException. Karena itu ?? hampir selalu",
                    "pilihan yang lebih baik.",
                    "",
                    "NULLABLE REFERENCE TYPES (C# 8, aktif secara bawaan sejak",
                    ".NET 6) mengubah aturannya untuk tipe referensi juga:",
                    "",
                    "  string nama = null;    PERINGATAN: mungkin null",
                    "  string? nama = null;   sah, kamu bilang ini boleh null",
                    "",
                    "Yang penting dipahami: ini SEMUANYA analisis compiler.",
                    "Saat program jalan, string dan string? adalah tipe yang",
                    "sama persis. Tandanya tidak mencegah null masuk dari",
                    "JSON, database, atau library lama — ia cuma memaksamu",
                    "memikirkannya di tempat yang benar.",
                ]
            },
            {
                "heading": "Pola penanganan null yang dipakai kode nyata",
                "code": """using System;

class Program
{
    static string Rapikan(string? masukan)
    {
        // 1. Pulang lebih awal (guard clause)
        if (string.IsNullOrWhiteSpace(masukan))
            return "(kosong)";

        // Di sini compiler TAHU masukan bukan null lagi
        return masukan.Trim().ToUpper();
    }

    static void Main()
    {
        string?[] data = { "  andi ", null, "", "   ", "budi" };

        foreach (string? s in data)
            Console.WriteLine($"[{Rapikan(s)}]");

        // 2. Null-conditional + null-coalescing berantai
        string? kota = null;
        Console.WriteLine(kota?.Trim()?.ToUpper() ?? "TIDAK DIISI");

        // 3. Pattern matching terhadap null
        object? apa = null;
        Console.WriteLine(apa is null ? "null" : "ada isinya");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  [ANDI]",
                    "  [(kosong)]",
                    "  [(kosong)]",
                    "  [(kosong)]",
                    "  [BUDI]",
                    "  TIDAK DIISI",
                    "  null",
                    "",
                    "Yang paling berharga di contoh itu: setelah",
                    "`if (string.IsNullOrWhiteSpace(masukan)) return ...`,",
                    "compiler tahu sisanya pasti bukan null dan berhenti",
                    "memperingatkan. Itu namanya FLOW ANALYSIS, dan ia bekerja",
                    "juga untuk `if (x != null)`, `is not null`, dan pola lain.",
                    "",
                    "Operator ! (null-forgiving) mematikan peringatan:",
                    "  string pasti = mungkinNull!;",
                    "",
                    "Ia tidak memeriksa apa pun — cuma berkata kepada compiler",
                    "'percaya aku'. Setiap kali kamu menulisnya, kamu memindahkan",
                    "tanggung jawab dari compiler ke dirimu sendiri. Kadang itu",
                    "benar (misalnya sesudah pemeriksaan yang tidak dikenali",
                    "compiler), tapi kalau sebuah berkas penuh tanda seru, yang",
                    "sebenarnya terjadi adalah fiturnya dimatikan diam-diam.",
                    "",
                    "Bandingkan dengan `is null` dan `== null`: keduanya mirip,",
                    "tapi == bisa di-overload oleh class sehingga perilakunya",
                    "diubah. `is null` tidak bisa. Untuk pemeriksaan null,",
                    "`is null` dan `is not null` adalah pilihan yang lebih aman.",
                ]
            },
        ],
    },
    {
        "title": "11. Class & Objek",
        "sections": [
            {
                "body": [
                    "Class adalah CETAKAN; objek adalah barang yang dicetak",
                    "darinya. Satu class bisa melahirkan ribuan objek, masing-",
                    "masing dengan isi sendiri.",
                    "",
                    "Isi sebuah class:",
                    "  field        variabel milik objek",
                    "  property     akses terkendali ke data",
                    "  constructor  dipanggil saat objek dibuat",
                    "  method       perilaku",
                    "",
                    "Modifier akses, dari paling terbuka:",
                    "  public              siapa pun boleh",
                    "  internal            hanya di dalam assembly ini (BAWAAN",
                    "                      untuk class)",
                    "  protected           class ini dan turunannya",
                    "  private             hanya di dalam class ini (BAWAAN",
                    "                      untuk anggota class)",
                    "  protected internal  gabungan protected ATAU internal",
                    "  private protected   turunan yang ada di assembly ini saja",
                    "",
                    "Aturan praktis: mulai dari private. Buka hanya kalau ada",
                    "yang benar-benar perlu. Sesuatu yang sudah public tidak",
                    "bisa ditutup lagi tanpa merusak kode orang lain.",
                    "",
                    "Membuat objek:",
                    "  var p = new Murid(\"Andi\", 20);",
                    "  Murid q = new(\"Budi\", 21);    bentuk singkat C# 9",
                    "",
                    "`this` menunjuk objek yang sedang dikerjakan. Ia wajib",
                    "hanya kalau ada nama yang bertabrakan (parameter bernama",
                    "sama dengan field), dan boleh ditulis di tempat lain",
                    "untuk kejelasan.",
                ]
            },
            {
                "heading": "Class lengkap",
                "code": """using System;

class Murid
{
    // Field privat: data mentah, tidak boleh disentuh dari luar
    private readonly string _nama;
    private int _nilai;

    // Property: pintu masuk terkendali
    public string Nama => _nama;

    public int Nilai
    {
        get => _nilai;
        set
        {
            if (value < 0 || value > 100)
                throw new ArgumentOutOfRangeException(nameof(value),
                    "Nilai harus 0..100");
            _nilai = value;
        }
    }

    // Property terhitung: tidak menyimpan apa-apa
    public string Grade => _nilai switch
    {
        >= 85 => "A",
        >= 75 => "B",
        >= 60 => "C",
        _     => "D",
    };

    public Murid(string nama, int nilai)
    {
        _nama = nama;
        Nilai = nilai;          // lewat property supaya ikut divalidasi
    }

    public override string ToString() => $"{_nama,-8} {_nilai,3}  {Grade}";
}

class Program
{
    static void Main()
    {
        var kelas = new[]
        {
            new Murid("Andi", 92),
            new Murid("Budi", 78),
            new Murid("Cici", 64),
        };

        foreach (Murid m in kelas) Console.WriteLine(m);

        try
        {
            kelas[0].Nilai = 150;
        }
        catch (ArgumentOutOfRangeException e)
        {
            Console.WriteLine($"Ditolak: {e.ParamName}");
        }
    }
}"""
            },
            {
                "body": [
                    "Empat hal penting di class itu:",
                    "",
                    "  1. Field privat diawali garis bawah (_nama). Ini",
                    "     konvensi .NET, bukan aturan compiler, tapi hampir",
                    "     universal — ia membuat field langsung terbedakan",
                    "     dari parameter dan variabel lokal.",
                    "",
                    "  2. Setter memvalidasi. Inilah seluruh alasan property",
                    "     ada: kalau _nilai public, tidak ada yang bisa",
                    "     mencegah orang mengisinya 9999. Enkapsulasi bukan",
                    "     soal menyembunyikan, melainkan soal menjaga objek",
                    "     selalu berada dalam keadaan yang masuk akal.",
                    "",
                    "  3. Constructor memakai `Nilai = nilai`, bukan",
                    "     `_nilai = nilai`. Bedanya: lewat property berarti",
                    "     validasinya ikut jalan sejak objek pertama dibuat.",
                    "",
                    "  4. ToString di-override. Setiap objek .NET punya",
                    "     ToString bawaan yang cuma mencetak nama tipenya",
                    "     ('Murid'). Meng-override-nya membuat objek bisa",
                    "     langsung dicetak dan langsung berarti.",
                    "",
                    "nameof(value) menghasilkan string \"value\" — dan kalau",
                    "nanti nama parameternya berubah, nameof ikut berubah",
                    "sedangkan string literal tidak. Itu sebabnya nameof lebih",
                    "baik daripada mengetik nama di dalam kutip.",
                ]
            },
        ],
    },
    {
        "title": "12. Property, Constructor & Inisialisasi",
        "sections": [
            {
                "body": [
                    "Bentuk-bentuk property, dari yang paling ringkas:",
                    "",
                    "  AUTO-PROPERTY",
                    "    public string Nama { get; set; }",
                    "    Compiler membuatkan field tersembunyinya sendiri.",
                    "",
                    "  HANYA-BACA DARI LUAR",
                    "    public string Nama { get; private set; }",
                    "",
                    "  BENAR-BENAR HANYA-BACA",
                    "    public string Nama { get; }",
                    "    Hanya bisa diisi di constructor atau di deklarasinya.",
                    "",
                    "  INIT-ONLY  (C# 9)",
                    "    public string Nama { get; init; }",
                    "    Bisa diisi saat objek dibuat lewat object initializer,",
                    "    sesudah itu terkunci.",
                    "",
                    "  NILAI BAWAAN",
                    "    public int Jumlah { get; set; } = 1;",
                    "",
                    "  TERHITUNG (tidak menyimpan apa pun)",
                    "    public double Luas => Panjang * Lebar;",
                    "",
                    "  REQUIRED  (C# 11)",
                    "    public required string Nama { get; init; }",
                    "    Compiler MENOLAK pembuatan objek yang tidak mengisinya.",
                    "",
                    "Object initializer — mengisi property saat pembuatan:",
                    "",
                    "  var p = new Produk",
                    "  {",
                    "      Nama = \"Keyboard\",",
                    "      Harga = 350000m,",
                    "  };",
                    "",
                    "Ini berjalan SESUDAH constructor. Jadi validasi di",
                    "constructor tidak melihat nilai-nilai ini — alasan kuat",
                    "untuk memakai `required` dan `init` alih-alih mengandalkan",
                    "orang mengingat mengisi apa.",
                ]
            },
            {
                "heading": "Constructor: berantai, statis, dan primer",
                "code": """using System;

class Rekening
{
    private static int _urutan = 0;      // milik CLASS, bukan objek

    public string Nomor { get; }
    public string Pemilik { get; }
    public decimal Saldo { get; private set; }

    // Constructor utama
    public Rekening(string pemilik, decimal saldoAwal)
    {
        if (string.IsNullOrWhiteSpace(pemilik))
            throw new ArgumentException("Pemilik wajib diisi", nameof(pemilik));

        _urutan++;
        Nomor = $"AC{_urutan:D4}";
        Pemilik = pemilik;
        Saldo = saldoAwal;
    }

    // Constructor lain yang MEMANGGIL yang utama lewat : this(...)
    public Rekening(string pemilik) : this(pemilik, 0m) { }

    public void Setor(decimal jumlah)
    {
        if (jumlah <= 0) throw new ArgumentException("Harus positif");
        Saldo += jumlah;
    }

    public bool Tarik(decimal jumlah)
    {
        if (jumlah <= 0 || jumlah > Saldo) return false;
        Saldo -= jumlah;
        return true;
    }

    public override string ToString() => $"{Nomor} {Pemilik,-8} {Saldo,12:N0}";
}

class Program
{
    static void Main()
    {
        var a = new Rekening("Andi", 500000m);
        var b = new Rekening("Budi");

        a.Setor(250000m);
        Console.WriteLine($"Tarik 900rb dari Andi: {a.Tarik(900000m)}");
        Console.WriteLine($"Tarik 300rb dari Andi: {a.Tarik(300000m)}");
        b.Setor(100000m);

        Console.WriteLine(a);
        Console.WriteLine(b);
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Tarik 900rb dari Andi: False",
                    "  Tarik 300rb dari Andi: True",
                    "  AC0001 Andi          450,000",
                    "  AC0002 Budi          100,000",
                    "",
                    "Tiga hal yang layak diperhatikan:",
                    "",
                    "  `: this(pemilik, 0m)` — constructor berantai. Alih-alih",
                    "  menyalin isi constructor utama, yang pendek memanggil",
                    "  yang panjang. Kalau validasinya berubah, ia berubah di",
                    "  satu tempat saja.",
                    "",
                    "  `private static int _urutan` — anggota STATIS milik",
                    "  class, bukan objek. Ada satu untuk seluruh program,",
                    "  berapa pun rekening yang dibuat. Itu yang membuat",
                    "  penomoran otomatis bekerja.",
                    "",
                    "  `Saldo { get; private set; }` — dunia luar boleh",
                    "  MEMBACA saldo, tapi hanya class ini yang boleh",
                    "  mengubahnya, dan hanya lewat Setor/Tarik yang sudah",
                    "  memvalidasi. Kalau setternya public, seluruh aturan",
                    "  perbankan di class ini bisa dilewati dengan satu baris.",
                    "",
                    "Primary constructor (C# 12) memendekkan bentuk ini lagi:",
                    "",
                    "  class Titik(int x, int y)",
                    "  {",
                    "      public int X => x;",
                    "      public int Y => y;",
                    "  }",
                    "",
                    "Parameternya langsung tersedia di seluruh badan class.",
                    "Praktis untuk tipe kecil, tapi hati-hati: parameternya",
                    "bisa berubah diam-diam kalau ada method yang menugaskan",
                    "ke situ, sesuatu yang tidak bisa terjadi pada property",
                    "hanya-baca.",
                ]
            },
        ],
    },
    {
        "title": "13. Pewarisan & Polimorfisme",
        "sections": [
            {
                "body": [
                    "Pewarisan: sebuah class mengambil seluruh isi class lain",
                    "lalu menambah atau mengubah sebagian.",
                    "",
                    "  class Hewan { ... }",
                    "  class Kucing : Hewan { ... }",
                    "",
                    "Tanda titik dua dibaca 'turunan dari'. C# hanya mengizinkan",
                    "SATU class induk — pewarisan berganda seperti C++ tidak",
                    "ada, karena masalah 'diamond' yang ditimbulkannya lebih",
                    "besar daripada manfaatnya. Untuk berbagi perilaku dari",
                    "banyak sumber, pakai interface.",
                    "",
                    "Tiga kata kunci yang mengatur override:",
                    "",
                    "  virtual   di INDUK: 'method ini boleh diganti turunan'",
                    "  override  di TURUNAN: 'aku mengganti method induk'",
                    "  sealed    'berhenti di sini, tidak boleh diturunkan lagi'",
                    "",
                    "Di C#, method TIDAK virtual secara bawaan — berbeda dari",
                    "Java. Ini disengaja: sebuah method yang bisa di-override",
                    "adalah janji publik yang harus dipikirkan, bukan kecelakaan.",
                    "",
                    "Kalau turunan menulis method bernama sama tanpa override,",
                    "compiler memperingatkan dan menyarankan `new`. `new`",
                    "MENYEMBUNYIKAN, bukan mengganti — dan bedanya terlihat",
                    "hanya saat objek dipegang lewat tipe induknya:",
                    "",
                    "  Hewan h = new Kucing();",
                    "  h.Suara();   override -> versi Kucing",
                    "               new      -> versi Hewan",
                    "",
                    "Inilah kenapa `new` hampir selalu bug yang menunggu.",
                    "",
                    "base menunjuk induk:",
                    "  base.Suara();              panggil versi induk",
                    "  public Kucing(...) : base(...)   panggil constructor induk",
                    "",
                    "Constructor induk SELALU dijalankan lebih dulu, entah",
                    "kamu menulis `: base(...)` atau tidak. Kalau induk tidak",
                    "punya constructor tanpa parameter, kamu WAJIB menulisnya.",
                ]
            },
            {
                "heading": "Abstract class dan polimorfisme",
                "code": """using System;

abstract class Bangun
{
    public string Nama { get; }
    protected Bangun(string nama) => Nama = nama;

    // Tanpa badan: turunan WAJIB mengisinya
    public abstract double Luas();
    public abstract double Keliling();

    // Punya badan, tapi boleh diganti
    public virtual string Ringkas()
        => $"{Nama,-12} luas {Luas(),8:F2}  keliling {Keliling(),8:F2}";
}

class Persegi : Bangun
{
    private readonly double _sisi;
    public Persegi(double sisi) : base("Persegi") => _sisi = sisi;

    public override double Luas() => _sisi * _sisi;
    public override double Keliling() => 4 * _sisi;
}

class Lingkaran : Bangun
{
    private const double PI = 3.14159265;
    private readonly double _jari;
    public Lingkaran(double jari) : base("Lingkaran") => _jari = jari;

    public override double Luas() => PI * _jari * _jari;
    public override double Keliling() => 2 * PI * _jari;
    public override string Ringkas() => base.Ringkas() + $"  (r={_jari})";
}

class Program
{
    static void Main()
    {
        Bangun[] semua = { new Persegi(4), new Lingkaran(3), new Persegi(2.5) };

        double totalLuas = 0;
        foreach (Bangun b in semua)
        {
            Console.WriteLine(b.Ringkas());
            totalLuas += b.Luas();
        }
        Console.WriteLine($"{"TOTAL",-12} luas {totalLuas,8:F2}");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Persegi      luas    16.00  keliling    16.00",
                    "  Lingkaran    luas    28.27  keliling    18.85  (r=3)",
                    "  Persegi      luas     6.25  keliling    10.00",
                    "  TOTAL        luas    50.52",
                    "",
                    "(Pemisah desimalnya mengikuti setelan wilayah komputer;",
                    "di locale Indonesia koma, di locale Inggris titik.)",
                    "",
                    "Inilah POLIMORFISME, dan kalimat kuncinya satu:",
                    "`b.Luas()` di dalam foreach memanggil method yang BERBEDA",
                    "tiap putaran, padahal kodenya cuma satu baris dan tipe",
                    "variabelnya cuma Bangun. Yang memilih versinya bukan",
                    "compiler melainkan objek yang sedang dipegang, saat",
                    "program jalan.",
                    "",
                    "Akibat praktisnya: menambah bangun baru (Segitiga) tidak",
                    "menyentuh satu baris pun di Main. Itu ukuran keberhasilan",
                    "desain berorientasi objek — bukan jumlah class-nya,",
                    "melainkan berapa banyak kode lama yang TIDAK perlu",
                    "disunting saat ada yang baru.",
                    "",
                    "abstract class:",
                    "  - TIDAK BISA di-new langsung. `new Bangun(...)` error.",
                    "  - Boleh punya method tanpa badan (abstract) DAN method",
                    "    biasa, field, constructor.",
                    "  - Turunan wajib mengisi semua yang abstract, atau ikut",
                    "    dinyatakan abstract.",
                ]
            },
        ],
    },
    {
        "title": "14. Interface",
        "sections": [
            {
                "body": [
                    "Interface adalah KONTRAK: daftar kemampuan tanpa satu pun",
                    "penjelasan cara melakukannya.",
                    "",
                    "  interface IBisaSimpan",
                    "  {",
                    "      void Simpan(string berkas);",
                    "      bool Sudah { get; }",
                    "  }",
                    "",
                    "Konvensi .NET: nama interface diawali huruf I besar.",
                    "Bukan aturan compiler, tapi dipatuhi di seluruh .NET dan",
                    "melanggarnya membuat kodemu terasa asing.",
                    "",
                    "Anggota interface otomatis public dan abstract; menulis",
                    "`public` di dalamnya justru error di C# lama.",
                    "",
                    "Interface vs abstract class — pertanyaan wawancara abadi,",
                    "dan jawabannya sebenarnya sederhana:",
                    "",
                    "  Abstract class menjawab 'INI ADALAH APA'",
                    "    Kucing ADALAH Hewan. Satu induk, berbagi keadaan.",
                    "",
                    "  Interface menjawab 'INI BISA APA'",
                    "    Kucing BISA dibandingkan, BISA disimpan, BISA",
                    "    ditelusuri. Sebanyak yang perlu.",
                    "",
                    "Perbedaan teknisnya:",
                    "  - Sebuah class hanya boleh punya SATU induk, tapi",
                    "    boleh mengimplementasi BANYAK interface.",
                    "  - Interface tidak punya field, tidak punya constructor,",
                    "    tidak menyimpan keadaan apa pun.",
                    "  - Sejak C# 8 interface BOLEH punya implementasi bawaan",
                    "    (default interface method) — ditambahkan supaya",
                    "    interface yang sudah dirilis bisa ditambah anggota",
                    "    tanpa merusak kode yang sudah memakainya.",
                    "",
                    "  struct juga boleh mengimplementasi interface, sedangkan",
                    "  struct tidak bisa mewarisi class.",
                ]
            },
            {
                "heading": "Interface bawaan .NET yang akan kamu pakai",
                "code": """using System;
using System.Collections.Generic;

class Buku : IComparable<Buku>, IEquatable<Buku>
{
    public string Judul { get; }
    public int Tahun { get; }

    public Buku(string judul, int tahun) => (Judul, Tahun) = (judul, tahun);

    // IComparable: menentukan urutan bawaan -> dipakai Array.Sort & List.Sort
    public int CompareTo(Buku? lain)
    {
        if (lain is null) return 1;
        int t = Tahun.CompareTo(lain.Tahun);
        return t != 0 ? t : string.Compare(Judul, lain.Judul, StringComparison.Ordinal);
    }

    // IEquatable: menentukan arti "sama" -> dipakai Contains, HashSet, Distinct
    public bool Equals(Buku? lain)
        => lain is not null && Judul == lain.Judul && Tahun == lain.Tahun;

    public override bool Equals(object? o) => Equals(o as Buku);
    public override int GetHashCode() => HashCode.Combine(Judul, Tahun);
    public override string ToString() => $"{Tahun} {Judul}";
}

class Program
{
    static void Main()
    {
        var rak = new List<Buku>
        {
            new("Pemrograman C#", 2021),
            new("Algoritma", 2018),
            new("Basis Data", 2021),
        };

        rak.Sort();                       // memakai CompareTo
        foreach (Buku b in rak) Console.WriteLine(b);

        Console.WriteLine(rak.Contains(new Buku("Algoritma", 2018)));  // True
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  2018 Algoritma",
                    "  2021 Basis Data",
                    "  2021 Pemrograman C#",
                    "  True",
                    "",
                    "Yang terjadi: `rak.Sort()` tidak tahu apa-apa tentang buku.",
                    "Ia cuma memanggil CompareTo pada tiap pasangan. Dengan",
                    "mengimplementasi IComparable, class-mu menyambung ke",
                    "seluruh mesin pengurutan .NET tanpa satu baris kode",
                    "pengurutan pun.",
                    "",
                    "Aturan CompareTo:",
                    "  negatif  aku lebih dulu",
                    "  nol      sama posisinya",
                    "  positif  aku belakangan",
                    "",
                    "Aturan yang SERING dilanggar: kalau kamu meng-override",
                    "Equals, kamu WAJIB meng-override GetHashCode juga. Dua",
                    "objek yang sama menurut Equals HARUS punya hash yang",
                    "sama — kalau tidak, Dictionary dan HashSet akan gagal",
                    "menemukan barang yang jelas-jelas ada di dalamnya, tanpa",
                    "satu pun error. HashCode.Combine menangani ini untukmu.",
                    "",
                    "Interface penting lain di .NET:",
                    "  IEnumerable<T>  bisa di-foreach; syarat semua LINQ",
                    "  IDisposable     punya sumber daya yang harus dilepas",
                    "  IComparer<T>    aturan urutan yang TERPISAH dari objeknya",
                    "  IFormattable    tahu cara memformat dirinya",
                ]
            },
        ],
    },
    {
        "title": "15. Struct, Record & Tipe Nilai",
        "sections": [
            {
                "body": [
                    "Tiga cara membuat tipe di C#, dan pilihannya menentukan",
                    "perilaku paling mendasar: apa yang terjadi saat disalin.",
                    "",
                    "  class   tipe REFERENSI. Menyalin = menyalin alamatnya.",
                    "          Dua variabel menunjuk objek yang SAMA.",
                    "  struct  tipe NILAI. Menyalin = menyalin seluruh isinya.",
                    "          Dua variabel berisi data yang TERPISAH.",
                    "  record  class (atau struct) dengan kesetaraan berdasarkan",
                    "          NILAI dan sejumlah besar kode yang dibuatkan.",
                    "",
                    "struct cocok untuk benda kecil yang tidak berubah dan",
                    "berperilaku seperti angka: titik koordinat, rentang",
                    "tanggal, jumlah uang. Contoh bawaan .NET: int, double,",
                    "bool, DateTime, TimeSpan, Guid — semuanya struct.",
                    "",
                    "Aturan praktis memilih struct: ukurannya di bawah 16 byte,",
                    "isinya tidak berubah setelah dibuat, dan ia tidak akan",
                    "sering di-boxing. Kalau ragu, pakai class.",
                    "",
                    "record — sejak C# 9 — menjawab kebutuhan yang sangat sering",
                    "muncul: 'aku cuma butuh wadah data'. Satu baris ini:",
                    "",
                    "  record Titik(int X, int Y);",
                    "",
                    "menghasilkan class dengan constructor, dua property",
                    "init-only, Equals berbasis nilai, GetHashCode, ToString",
                    "yang enak dibaca, operator == dan !=, deconstructor,",
                    "dan method `with`.",
                    "",
                    "Kalau ditulis tangan, semua itu sekitar 60 baris yang",
                    "gampang salah satu-dua bagiannya.",
                ]
            },
            {
                "heading": "Melihat bedanya secara langsung",
                "code": """using System;

struct TitikS { public int X, Y; }
class  TitikC { public int X, Y; }

record Barang(string Nama, decimal Harga);

class Program
{
    static void Main()
    {
        // STRUCT: disalin isinya
        var s1 = new TitikS { X = 1, Y = 2 };
        var s2 = s1;
        s2.X = 99;
        Console.WriteLine($"struct : s1.X={s1.X}  s2.X={s2.X}");

        // CLASS: disalin alamatnya
        var c1 = new TitikC { X = 1, Y = 2 };
        var c2 = c1;
        c2.X = 99;
        Console.WriteLine($"class  : c1.X={c1.X}  c2.X={c2.X}");

        // RECORD: kesetaraan berbasis NILAI
        var b1 = new Barang("Kopi", 25000m);
        var b2 = new Barang("Kopi", 25000m);
        Console.WriteLine($"record == : {b1 == b2}");
        Console.WriteLine($"ToString  : {b1}");

        // with: salinan dengan sebagian diubah
        var b3 = b1 with { Harga = 27000m };
        Console.WriteLine($"with      : {b3}");

        var (nama, harga) = b1;            // deconstruct
        Console.WriteLine($"pecah     : {nama} / {harga}");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  struct : s1.X=1  s2.X=99",
                    "  class  : c1.X=99  c2.X=99",
                    "  record == : True",
                    "  ToString  : Barang { Nama = Kopi, Harga = 25000 }",
                    "  with      : Barang { Nama = Kopi, Harga = 27000 }",
                    "  pecah     : Kopi / 25000",
                    "",
                    "Baris kedua adalah sumber bug yang paling sering ditemui",
                    "pemula: mengubah c2 ternyata mengubah c1 juga, karena",
                    "keduanya nama untuk objek yang sama. Dengan class,",
                    "'menyalin' sebuah objek butuh usaha sadar (constructor",
                    "penyalin, method Clone, atau record + with).",
                    "",
                    "Baris ketiga: dua objek record berbeda dinyatakan sama",
                    "karena isinya sama. Kalau Barang sebuah class biasa,",
                    "hasilnya False — class membandingkan alamat.",
                    "",
                    "`with` membuat SALINAN dengan sebagian anggota diganti,",
                    "tanpa menyentuh yang asli. Ini pola yang sangat berguna",
                    "untuk data yang tidak boleh berubah: alih-alih mengubah",
                    "objek, kamu membuat versi berikutnya.",
                    "",
                    "Varian record:",
                    "  record            = record class, tipe referensi",
                    "  record class      = sama, ditulis eksplisit",
                    "  record struct     = tipe nilai, anggotanya bisa diubah",
                    "  readonly record struct = tipe nilai, benar-benar beku",
                    "",
                    "Kapan pakai record: DTO, hasil query, pesan, event,",
                    "konfigurasi — apa pun yang lebih tepat disebut 'data'",
                    "daripada 'benda dengan perilaku'.",
                ]
            },
        ],
    },
    {
        "title": "16. Enum & Konstanta Bernama",
        "sections": [
            {
                "body": [
                    "Enum adalah sekumpulan konstanta bernama bertipe sama.",
                    "Ia mengganti 'angka ajaib' yang tidak menjelaskan apa-apa.",
                    "",
                    "  enum Status { Draf, Terkirim, Disetujui, Ditolak }",
                    "",
                    "Di baliknya tetap angka: Draf = 0, Terkirim = 1, dan",
                    "seterusnya. Nilainya bisa ditetapkan sendiri:",
                    "",
                    "  enum Prioritas { Rendah = 1, Sedang = 5, Tinggi = 10 }",
                    "",
                    "Kenapa ini lebih baik daripada `int status = 2`:",
                    "  - Compiler menolak nilai yang bukan anggota enum",
                    "    (setidaknya tanpa cast eksplisit).",
                    "  - Nama anggotanya muncul di autocomplete.",
                    "  - switch atas enum diperiksa kelengkapannya oleh",
                    "    analyzer.",
                    "  - ToString memberi namanya, bukan angkanya.",
                    "",
                    "Operasi yang sering dipakai:",
                    "  Status s = Status.Terkirim;",
                    "  Console.WriteLine(s);              Terkirim",
                    "  Console.WriteLine((int)s);         1",
                    "  Status t = (Status)3;              Ditolak",
                    "  Enum.GetValues<Status>()           semua anggotanya",
                    "  Enum.TryParse(\"Draf\", out Status x)",
                    "  s.ToString()                       \"Terkirim\"",
                    "",
                    "PERINGATAN yang sering mengejutkan: cast dari angka",
                    "TIDAK divalidasi. `(Status)99` sah dan menghasilkan enum",
                    "bernilai 99 yang tidak punya nama. Kalau nilainya datang",
                    "dari luar (database, JSON, masukan pengguna), periksa",
                    "dengan Enum.IsDefined.",
                ]
            },
            {
                "heading": "Enum [Flags]: banyak pilihan dalam satu nilai",
                "code": """using System;

[Flags]
enum Izin
{
    Tidak  = 0,
    Baca   = 1,      // 0001
    Tulis  = 2,      // 0010
    Hapus  = 4,      // 0100
    Jalan  = 8,      // 1000
    Penuh  = Baca | Tulis | Hapus | Jalan,
}

class Program
{
    static void Main()
    {
        Izin editor = Izin.Baca | Izin.Tulis;

        Console.WriteLine(editor);                       // Baca, Tulis
        Console.WriteLine((int)editor);                  // 3
        Console.WriteLine(editor.HasFlag(Izin.Tulis));   // True
        Console.WriteLine(editor.HasFlag(Izin.Hapus));   // False

        editor |= Izin.Hapus;                            // tambah
        Console.WriteLine(editor);                       // Baca, Tulis, Hapus

        editor &= ~Izin.Baca;                            // buang
        Console.WriteLine(editor);                       // Tulis, Hapus

        Console.WriteLine(Izin.Penuh);                   // Penuh
    }
}"""
            },
            {
                "body": [
                    "Enum ber-[Flags] menyimpan BANYAK pilihan sekaligus dalam",
                    "satu angka, memanfaatkan bit. Syaratnya nilainya harus",
                    "pangkat dua (1, 2, 4, 8, 16, ...) supaya tiap anggota",
                    "menempati bit sendiri.",
                    "",
                    "Operasinya:",
                    "  a | b     gabungkan (tambah izin)",
                    "  a & b     irisan (apa yang sama-sama ada)",
                    "  a & ~b    buang b dari a",
                    "  a.HasFlag(b)  apakah b termasuk di a",
                    "",
                    "Atribut [Flags] sendiri TIDAK mengubah perilaku bitwise —",
                    "operator | dan & jalan pada enum apa pun. Yang diubahnya",
                    "cuma ToString: tanpa [Flags], `editor` di atas akan",
                    "dicetak sebagai '3', bukan 'Baca, Tulis'.",
                    "",
                    "Pola ini dipakai di seluruh .NET: FileAccess, RegexOptions,",
                    "BindingFlags, dan izin berkas di sistem operasi.",
                    "",
                    "Nilai 0 sebaiknya diberi nama seperti 'Tidak' atau 'None'.",
                    "HasFlag terhadap nilai 0 selalu true, jadi jangan pakai",
                    "HasFlag untuk memeriksa 'tidak punya izin apa pun' —",
                    "bandingkan langsung: `if (izin == Izin.Tidak)`.",
                ]
            },
        ],
    },
    {
        "title": "17. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "Exception adalah cara program memberi tahu bahwa sesuatu",
                    "yang tidak bisa ia tangani sendiri telah terjadi. Bedanya",
                    "dengan mengembalikan kode error: exception TIDAK BISA",
                    "diabaikan diam-diam.",
                    "",
                    "  try",
                    "  {",
                    "      ... kode yang mungkin gagal",
                    "  }",
                    "  catch (FormatException e)",
                    "  {",
                    "      ... tangani yang spesifik dulu",
                    "  }",
                    "  catch (Exception e)",
                    "  {",
                    "      ... jaring terakhir",
                    "  }",
                    "  finally",
                    "  {",
                    "      ... SELALU dijalankan, gagal maupun tidak",
                    "  }",
                    "",
                    "Urutan catch berarti: yang PALING SPESIFIK harus di atas.",
                    "Menulis `catch (Exception)` lebih dulu membuat catch di",
                    "bawahnya tidak pernah tercapai — dan compiler akan",
                    "menolaknya.",
                    "",
                    "Exception bawaan yang paling sering kamu temui:",
                    "",
                    "  NullReferenceException     mengakses anggota dari null",
                    "  IndexOutOfRangeException   index array di luar batas",
                    "  ArgumentException          argumen tidak masuk akal",
                    "  ArgumentNullException      argumen null padahal wajib",
                    "  ArgumentOutOfRangeException argumen di luar rentang",
                    "  InvalidOperationException  objek sedang tidak siap",
                    "  FormatException            teks tidak sesuai format",
                    "  OverflowException          hasil melewati batas tipe",
                    "  DivideByZeroException      pembagian BULAT oleh nol",
                    "  FileNotFoundException      berkas tidak ada",
                    "  KeyNotFoundException       kunci dictionary tidak ada",
                    "",
                    "Catatan halus: pembagian double oleh nol TIDAK melempar",
                    "apa-apa. Hasilnya double.Infinity atau double.NaN. Hanya",
                    "pembagian bilangan BULAT yang melempar.",
                ]
            },
            {
                "heading": "Melempar, menangkap, dan exception sendiri",
                "code": """using System;

class SaldoKurangException : Exception
{
    public decimal Kurang { get; }

    public SaldoKurangException(decimal kurang)
        : base($"Saldo kurang {kurang:N0}")
        => Kurang = kurang;
}

class Dompet
{
    public decimal Saldo { get; private set; }

    public Dompet(decimal awal) => Saldo = awal;

    public void Bayar(decimal jumlah)
    {
        if (jumlah <= 0)
            throw new ArgumentOutOfRangeException(nameof(jumlah),
                "Jumlah harus lebih dari nol");

        if (jumlah > Saldo)
            throw new SaldoKurangException(jumlah - Saldo);

        Saldo -= jumlah;
    }
}

class Program
{
    static void Main()
    {
        var d = new Dompet(50000m);
        decimal[] tagihan = { 20000m, -5m, 100000m, 30000m };

        foreach (decimal t in tagihan)
        {
            try
            {
                d.Bayar(t);
                Console.WriteLine($"Bayar {t,8:N0} -> sisa {d.Saldo,8:N0}");
            }
            catch (SaldoKurangException e)
            {
                Console.WriteLine($"Bayar {t,8:N0} -> GAGAL, kurang {e.Kurang:N0}");
            }
            catch (ArgumentOutOfRangeException)
            {
                Console.WriteLine($"Bayar {t,8:N0} -> DITOLAK, nilai tidak sah");
            }
        }
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Bayar   20,000 -> sisa   30,000",
                    "  Bayar       -5 -> DITOLAK, nilai tidak sah",
                    "  Bayar  100,000 -> GAGAL, kurang 70,000",
                    "  Bayar   30,000 -> sisa        0",
                    "",
                    "Exception buatan sendiri berguna kalau pemanggil perlu",
                    "MEMBEDAKAN kegagalan itu dari kegagalan lain, atau perlu",
                    "data tambahan (di sini: berapa kurangnya). Kalau tidak",
                    "ada keduanya, pakai yang bawaan.",
                    "",
                    "Aturan yang sering dilanggar, dan akibatnya mahal:",
                    "",
                    "  JANGAN `catch (Exception) { }` kosong. Itu menelan",
                    "  seluruh kesalahan termasuk yang tidak kamu duga, dan",
                    "  program berjalan terus dalam keadaan rusak. Bug seperti",
                    "  ini baru terlihat berjam-jam kemudian, jauh dari",
                    "  penyebabnya.",
                    "",
                    "  JANGAN `throw e;` untuk melempar ulang. Itu MENGHAPUS",
                    "  jejak tumpukan aslinya, sehingga yang tercatat di log",
                    "  adalah baris catch-mu, bukan baris yang benar-benar",
                    "  gagal. Tulis `throw;` polos.",
                    "",
                    "  JANGAN pakai exception untuk alur normal. Pengguna",
                    "  salah ketik itu normal — pakai TryParse. Berkas",
                    "  konfigurasi tidak ada saat pertama jalan itu normal —",
                    "  periksa File.Exists.",
                    "",
                    "  JANGAN menangkap apa yang tidak bisa kamu perbaiki.",
                    "  Membiarkan exception naik ke pemanggil yang tahu",
                    "  harus berbuat apa lebih baik daripada menanganinya",
                    "  setengah-setengah di tempat yang tidak tahu konteks.",
                    "",
                    "`when` menyaring catch tanpa menangkapnya:",
                    "  catch (HttpRequestException e) when (e.StatusCode == 404)",
                ]
            },
        ],
    },
    {
        "title": "18. Generic: Tipe sebagai Parameter",
        "sections": [
            {
                "body": [
                    "Generic membuat sebuah class atau method bekerja untuk",
                    "TIPE APA PUN tanpa kehilangan pemeriksaan tipe.",
                    "",
                    "Sebelum generic (C# 1), koleksi menyimpan object:",
                    "  ArrayList daftar = new ArrayList();",
                    "  daftar.Add(\"halo\");",
                    "  daftar.Add(42);              tidak ada yang mencegah",
                    "  int n = (int)daftar[0];      MELEDAK saat program jalan",
                    "",
                    "Dua kerugiannya: kesalahan baru ketahuan saat jalan, dan",
                    "setiap int yang masuk harus di-BOXING jadi objek di heap.",
                    "",
                    "Dengan generic:",
                    "  List<string> daftar = new List<string>();",
                    "  daftar.Add(42);              ERROR KOMPILASI",
                    "",
                    "Method generic:",
                    "  static T Terbesar<T>(T a, T b) where T : IComparable<T>",
                    "      => a.CompareTo(b) >= 0 ? a : b;",
                    "",
                    "  Terbesar(3, 9)             T disimpulkan int",
                    "  Terbesar(\"apel\", \"jeruk\")  T disimpulkan string",
                    "",
                    "CONSTRAINT (`where`) memberi tahu compiler apa yang boleh",
                    "kamu lakukan pada T. Tanpa `where T : IComparable<T>`,",
                    "compiler tidak tahu T punya CompareTo dan menolaknya.",
                    "",
                    "Daftar constraint:",
                    "  where T : class          harus tipe referensi",
                    "  where T : struct         harus tipe nilai",
                    "  where T : new()          harus punya constructor kosong",
                    "  where T : NamaKelas      harus turunan kelas itu",
                    "  where T : IAntarmuka     harus mengimplementasi itu",
                    "  where T : notnull        tidak boleh nullable",
                    "  where T : U              T harus turunan dari U",
                    "",
                    "Beberapa constraint dipisah koma:",
                    "  where T : class, IComparable<T>, new()",
                ]
            },
            {
                "heading": "Class generic sendiri",
                "code": """using System;
using System.Collections.Generic;

// Tumpukan berbatas: menolak isi kalau sudah penuh
class Kotak<T>
{
    private readonly List<T> _isi = new();
    private readonly int _muat;

    public Kotak(int muat) => _muat = muat;

    public int Jumlah => _isi.Count;
    public bool Penuh => _isi.Count >= _muat;

    public bool Masuk(T barang)
    {
        if (Penuh) return false;
        _isi.Add(barang);
        return true;
    }

    public T? Ambil()
    {
        if (_isi.Count == 0) return default;
        T barang = _isi[^1];
        _isi.RemoveAt(_isi.Count - 1);
        return barang;
    }

    public override string ToString()
        => $"Kotak<{typeof(T).Name}> [{string.Join(", ", _isi)}] {Jumlah}/{_muat}";
}

class Program
{
    static void Main()
    {
        var angka = new Kotak<int>(3);
        foreach (int n in new[] { 1, 2, 3, 4 })
            Console.WriteLine($"masuk {n}: {angka.Masuk(n)}");
        Console.WriteLine(angka);

        var kata = new Kotak<string>(2);
        kata.Masuk("apel");
        kata.Masuk("jeruk");
        Console.WriteLine(kata);
        Console.WriteLine($"diambil: {kata.Ambil()}");
        Console.WriteLine(kata);
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  masuk 1: True",
                    "  masuk 2: True",
                    "  masuk 3: True",
                    "  masuk 4: False",
                    "  Kotak<Int32> [1, 2, 3] 3/3",
                    "  Kotak<String> [apel, jeruk] 2/2",
                    "  diambil: jeruk",
                    "  Kotak<String> [apel] 1/2",
                    "",
                    "`default` adalah nilai bawaan T, apa pun T itu: 0 untuk",
                    "int, null untuk string, false untuk bool. Menuliskannya",
                    "sebagai `default` bekerja untuk semua tipe sekaligus —",
                    "tidak ada cara lain menulis 'nilai kosongnya T'.",
                    "",
                    "`typeof(T).Name` membaca nama tipe saat program jalan.",
                    "Berbeda dari Java, generic C# TIDAK dihapus saat kompilasi",
                    "(no type erasure): List<int> dan List<string> benar-benar",
                    "tipe yang berbeda di runtime, dan List<int> menyimpan int",
                    "langsung tanpa boxing. Ini bukan detail kecil — untuk",
                    "sejuta angka, selisihnya ratusan megabyte.",
                ]
            },
        ],
    },
    {
        "title": "19. Delegate, Event & Lambda",
        "sections": [
            {
                "body": [
                    "Delegate adalah TIPE yang isinya sebuah method. Ia yang",
                    "membuat method bisa disimpan di variabel, dioper sebagai",
                    "argumen, dan dikembalikan dari method lain.",
                    "",
                    "  delegate int Operasi(int a, int b);",
                    "  Operasi f = Tambah;          tanpa tanda kurung!",
                    "  Console.WriteLine(f(3, 4));",
                    "",
                    "Dalam praktik, kamu jarang mendeklarasikan delegate sendiri",
                    "karena .NET sudah menyediakan tiga yang menutupi hampir",
                    "semua kebutuhan:",
                    "",
                    "  Action            tanpa parameter, tanpa kembalian",
                    "  Action<T>         terima T, tanpa kembalian",
                    "  Action<T1,T2>     sampai 16 parameter",
                    "  Func<TResult>     tanpa parameter, kembalikan TResult",
                    "  Func<T,TResult>   terima T, kembalikan TResult",
                    "  Predicate<T>      terima T, kembalikan bool",
                    "",
                    "Aturan membacanya: di Func<...>, tipe TERAKHIR adalah",
                    "kembaliannya, sisanya parameter. Func<int, string, bool>",
                    "berarti (int, string) -> bool.",
                    "",
                    "Lambda — method tanpa nama:",
                    "  Func<int, int> kuadrat = x => x * x;",
                    "  Func<int, int, int> tambah = (a, b) => a + b;",
                    "  Action<string> cetak = s => Console.WriteLine(s);",
                    "  Func<int, bool> genap = x => x % 2 == 0;",
                    "",
                    "  // badan berkurawal untuk yang lebih dari satu baris",
                    "  Func<int, string> nilai = n =>",
                    "  {",
                    "      if (n >= 75) return \"Lulus\";",
                    "      return \"Mengulang\";",
                    "  };",
                    "",
                    "CLOSURE: lambda MENANGKAP variabel di sekitarnya, bukan",
                    "menyalin nilainya.",
                    "",
                    "  int batas = 10;",
                    "  Func<int, bool> kecil = x => x < batas;",
                    "  batas = 100;",
                    "  kecil(50);        TRUE -- membaca batas yang SEKARANG",
                    "",
                    "Ini sering mengejutkan, dan di dalam perulangan ia sumber",
                    "bug klasik. Untungnya sejak C# 5 variabel foreach dibuat",
                    "baru tiap putaran, jadi `foreach (var x in ...) aksi.Add(",
                    "() => Console.Write(x))` berperilaku seperti yang kamu",
                    "harapkan. Variabel `for` TIDAK — di situ masih satu",
                    "variabel yang sama untuk seluruh perulangan.",
                ]
            },
            {
                "heading": "Delegate sebagai parameter: perilaku yang dioper",
                "code": """using System;
using System.Collections.Generic;

class Program
{
    static List<int> Saring(List<int> data, Predicate<int> syarat)
    {
        var hasil = new List<int>();
        foreach (int n in data)
            if (syarat(n)) hasil.Add(n);
        return hasil;
    }

    static List<TOut> Ubah<TIn, TOut>(List<TIn> data, Func<TIn, TOut> ubah)
    {
        var hasil = new List<TOut>();
        foreach (TIn x in data) hasil.Add(ubah(x));
        return hasil;
    }

    static void Main()
    {
        var angka = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        Console.WriteLine(string.Join(" ", Saring(angka, n => n % 2 == 0)));
        Console.WriteLine(string.Join(" ", Saring(angka, n => n > 7)));
        Console.WriteLine(string.Join(" ", Ubah(angka, n => n * n)));
        Console.WriteLine(string.Join(" ", Ubah(angka, n => $"#{n}")));

        // Multicast: satu delegate memanggil BEBERAPA method
        Action<string> catat = s => Console.WriteLine($"[log] {s}");
        catat += s => Console.WriteLine($"[layar] {s}");
        catat("selesai");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  2 4 6 8 10",
                    "  8 9 10",
                    "  1 4 9 16 25 36 49 64 81 100",
                    "  #1 #2 #3 #4 #5 #6 #7 #8 #9 #10",
                    "  [log] selesai",
                    "  [layar] selesai",
                    "",
                    "Yang terjadi di Saring: method itu tidak tahu sama sekali",
                    "syarat apa yang sedang diuji. Ia cuma memanggil `syarat(n)`.",
                    "Seluruh keputusan dipindahkan ke pemanggil. Itulah inti",
                    "pemrograman fungsional: PERILAKU yang dioper, bukan cuma",
                    "data.",
                    "",
                    "Saring dan Ubah di atas persis apa yang dilakukan LINQ",
                    "dengan nama Where dan Select. Menulis sendiri sekali",
                    "membuat LINQ berhenti terasa ajaib.",
                    "",
                    "EVENT adalah delegate dengan pagar: dari luar class, ia",
                    "hanya boleh ditambah (+=) dan dikurangi (-=), tidak boleh",
                    "ditugaskan ulang (=) dan tidak boleh dipanggil.",
                    "",
                    "  public event Action<string>? Berubah;",
                    "  ...",
                    "  Berubah?.Invoke(\"nilai baru\");   dipanggil dari DALAM",
                    "",
                    "Tanpa pagar itu, satu baris `obj.Berubah = ...` di tempat",
                    "lain menghapus seluruh pendengar yang sudah terdaftar,",
                    "dan tidak ada yang tahu kenapa notifikasinya berhenti",
                    "sampai.",
                    "",
                    "`?.Invoke` bukan kerewelan: kalau belum ada satu pun",
                    "pendengar, event bernilai null dan memanggilnya langsung",
                    "melempar NullReferenceException.",
                ]
            },
        ],
    },
    {
        "title": "20. LINQ: Bertanya pada Data",
        "sections": [
            {
                "body": [
                    "LINQ (Language Integrated Query) adalah sekumpulan method",
                    "untuk menyaring, mengubah, mengelompokkan, dan meringkas",
                    "koleksi — dengan sintaks yang sama entah sumbernya List,",
                    "array, berkas, atau database.",
                    "",
                    "  using System.Linq;    wajib",
                    "",
                    "Dua bentuk penulisan, hasilnya identik:",
                    "",
                    "  METHOD SYNTAX (paling umum)",
                    "    var hasil = murid.Where(m => m.Nilai >= 75)",
                    "                     .OrderByDescending(m => m.Nilai)",
                    "                     .Select(m => m.Nama);",
                    "",
                    "  QUERY SYNTAX (mirip SQL)",
                    "    var hasil = from m in murid",
                    "                where m.Nilai >= 75",
                    "                orderby m.Nilai descending",
                    "                select m.Nama;",
                    "",
                    "Method syntax lebih sering dipakai karena tidak semua",
                    "method punya padanan kata kunci (Count, Any, Sum harus",
                    "tetap ditulis sebagai method).",
                    "",
                    "Operator penyaring dan pengubah:",
                    "  Where(p)          ambil yang memenuhi syarat",
                    "  Select(f)         ubah tiap elemen",
                    "  SelectMany(f)     ubah lalu ratakan jadi satu deret",
                    "  OrderBy(k)        urut menaik",
                    "  OrderByDescending(k)  urut menurun",
                    "  ThenBy(k)         kunci urutan kedua",
                    "  Take(n) / Skip(n) ambil / lewati n pertama",
                    "  Distinct()        buang duplikat",
                    "  Reverse()         balik urutan",
                    "",
                    "Operator yang menghasilkan SATU nilai:",
                    "  Count() / Sum() / Average() / Min() / Max()",
                    "  Any(p)            adakah yang cocok?",
                    "  All(p)            apakah SEMUA cocok?",
                    "  First(p)          yang pertama; MELEMPAR kalau tidak ada",
                    "  FirstOrDefault(p) yang pertama; null/0 kalau tidak ada",
                    "  Single(p)         tepat satu; melempar kalau 0 atau >1",
                    "  Aggregate(f)      lipat jadi satu nilai",
                    "",
                    "Pasangan First/FirstOrDefault ada di banyak method, dan",
                    "memilihnya adalah keputusan desain: pakai yang melempar",
                    "kalau 'tidak ada' berarti bug, pakai OrDefault kalau",
                    "'tidak ada' adalah hasil yang wajar.",
                ]
            },
            {
                "heading": "LINQ pada data nyata",
                "code": """using System;
using System.Collections.Generic;
using System.Linq;

record Murid(string Nama, string Kelas, int Nilai);

class Program
{
    static void Main()
    {
        var data = new List<Murid>
        {
            new("Andi",  "A", 88), new("Budi", "B", 72),
            new("Cici",  "A", 95), new("Dedi", "B", 64),
            new("Euis",  "A", 79), new("Fajar", "B", 91),
        };

        Console.WriteLine("-- Lulus, nilai tertinggi dulu --");
        foreach (var m in data.Where(m => m.Nilai >= 75)
                              .OrderByDescending(m => m.Nilai))
            Console.WriteLine($"  {m.Nama,-6} {m.Nilai}");

        Console.WriteLine($"\\nRata-rata : {data.Average(m => m.Nilai):F2}");
        Console.WriteLine($"Tertinggi : {data.Max(m => m.Nilai)}");
        Console.WriteLine($"Jumlah    : {data.Count(m => m.Nilai >= 75)} lulus");
        Console.WriteLine($"Ada yang <65? {data.Any(m => m.Nilai < 65)}");
        Console.WriteLine($"Semua >60?    {data.All(m => m.Nilai > 60)}");

        Console.WriteLine("\\n-- Per kelas --");
        foreach (var g in data.GroupBy(m => m.Kelas).OrderBy(g => g.Key))
            Console.WriteLine($"  Kelas {g.Key}: {g.Count()} murid, "
                            + $"rata-rata {g.Average(m => m.Nilai):F1}, "
                            + $"terbaik {g.OrderByDescending(m => m.Nilai).First().Nama}");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  -- Lulus, nilai tertinggi dulu --",
                    "    Cici   95",
                    "    Fajar  91",
                    "    Andi   88",
                    "    Euis   79",
                    "",
                    "  Rata-rata : 81,50",
                    "  Tertinggi : 95",
                    "  Jumlah    : 4 lulus",
                    "  Ada yang <65? True",
                    "  Semua >60?    True",
                    "",
                    "  -- Per kelas --",
                    "    Kelas A: 3 murid, rata-rata 87,3, terbaik Cici",
                    "    Kelas B: 3 murid, rata-rata 75,7, terbaik Fajar",
                    "",
                    "GroupBy menghasilkan deret IGrouping<TKey, TElement>:",
                    "sebuah koleksi yang sekaligus punya properti .Key. Itu",
                    "sebabnya g bisa di-Count() dan juga ditanya g.Key.",
                    "",
                    "DEFERRED EXECUTION — hal terpenting tentang LINQ, dan",
                    "yang paling sering menjebak:",
                    "",
                    "  var q = data.Where(m => m.Nilai > 80);  BELUM jalan",
                    "  data.Add(new(\"Gita\", \"A\", 99));",
                    "  foreach (var m in q) ...                BARU jalan",
                    "",
                    "Gita IKUT muncul, karena query baru dijalankan saat",
                    "ditelusuri, bukan saat ditulis. Kalau kamu ingin hasilnya",
                    "dibekukan saat itu juga, panggil .ToList() atau .ToArray().",
                    "",
                    "Akibat kedua yang lebih menyakitkan: menelusuri query yang",
                    "sama dua kali menjalankan seluruh penyaringan dua kali.",
                    "Kalau sumbernya database, itu dua kali perjalanan ke",
                    "server untuk pertanyaan yang sama.",
                    "",
                    "Aturan praktisnya: selesai menyusun query dan hasilnya",
                    "akan dipakai lebih dari sekali -> .ToList().",
                ]
            },
        ],
    },
    {
        "title": "21. Bekerja dengan Berkas",
        "sections": [
            {
                "body": [
                    "Namespace yang dibutuhkan: System.IO",
                    "",
                    "Cara paling singkat, untuk berkas yang muat di memori:",
                    "",
                    "  File.WriteAllText(path, isi);",
                    "  File.AppendAllText(path, isi);",
                    "  string isi = File.ReadAllText(path);",
                    "  string[] baris = File.ReadAllLines(path);",
                    "  File.WriteAllLines(path, baris);",
                    "",
                    "Untuk berkas besar, jangan pakai ReadAllLines — ia menarik",
                    "seluruh isi ke memori sekaligus. Pakai ReadLines, yang",
                    "membaca satu per satu sambil ditelusuri:",
                    "",
                    "  foreach (string b in File.ReadLines(path)) ...",
                    "",
                    "Bedanya cuma satu kata (All), dan untuk berkas 2 GB",
                    "bedanya adalah antara berjalan dan kehabisan memori.",
                    "",
                    "Memeriksa dan mengelola:",
                    "  File.Exists(path)          bool",
                    "  File.Delete(path)          diam saja kalau tidak ada",
                    "  File.Copy(a, b, true)      true = boleh menimpa",
                    "  File.Move(a, b)",
                    "  Directory.Exists(path)",
                    "  Directory.CreateDirectory(path)   aman kalau sudah ada",
                    "  Directory.GetFiles(path, \"*.txt\")",
                    "",
                    "MENYUSUN PATH: jangan pernah menyambung dengan tanda",
                    "garis miring sendiri. Pemisah path berbeda antar sistem",
                    "operasi, dan Path.Combine tahu yang benar:",
                    "",
                    "  string p = Path.Combine(folder, \"data\", \"murid.txt\");",
                    "",
                    "  Path.GetFileName(p)              murid.txt",
                    "  Path.GetFileNameWithoutExtension(p)  murid",
                    "  Path.GetExtension(p)             .txt",
                    "  Path.GetDirectoryName(p)         folder/data",
                    "  Path.GetFullPath(p)              path absolut",
                ]
            },
            {
                "heading": "Menulis, membaca, dan mengolah berkas CSV",
                "code": """using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        string berkas = Path.Combine(Path.GetTempPath(), "nilai-belajar.csv");

        string[] isi =
        {
            "nama,kelas,nilai",
            "Andi,A,88",
            "Budi,B,72",
            "Cici,A,95",
        };
        File.WriteAllLines(berkas, isi);

        var baris = File.ReadAllLines(berkas).Skip(1);      // lewati judul
        var data = baris.Select(b => b.Split(','))
                        .Select(k => (Nama: k[0], Kelas: k[1], Nilai: int.Parse(k[2])))
                        .ToList();

        foreach (var m in data.OrderByDescending(m => m.Nilai))
            Console.WriteLine($"{m.Nama,-6} {m.Kelas}  {m.Nilai,3}");

        Console.WriteLine($"Rata-rata: {data.Average(m => m.Nilai):F2}");

        File.Delete(berkas);
        Console.WriteLine($"Berkas masih ada? {File.Exists(berkas)}");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Cici   A   95",
                    "  Andi   A   88",
                    "  Budi   B   72",
                    "  Rata-rata: 85.00",
                    "  Berkas masih ada? False",
                    "",
                    "`(Nama: k[0], Kelas: k[1], Nilai: ...)` adalah TUPLE",
                    "bernama — wadah data sekali pakai tanpa perlu membuat",
                    "class. Berguna persis di situasi ini: bentuk datanya cuma",
                    "hidup di dalam satu method.",
                    "",
                    "PERINGATAN tentang CSV: `Split(',')` hanya benar kalau",
                    "tidak ada koma DI DALAM data. CSV sungguhan memperbolehkan",
                    "\"Jakarta, DKI\" sebagai satu kolom, dan Split akan",
                    "memecahnya jadi dua. Untuk data sungguhan pakai pustaka",
                    "CSV; untuk latihan seperti ini, Split cukup — asal kamu",
                    "tahu batasnya.",
                    "",
                    "Operasi berkas SELALU bisa gagal karena sebab di luar",
                    "kendalimu: berkas terkunci program lain, izin ditolak,",
                    "disk penuh, jalur tidak ada. Kode nyata membungkusnya:",
                    "",
                    "  try { ... }",
                    "  catch (FileNotFoundException) { ... }",
                    "  catch (UnauthorizedAccessException) { ... }",
                    "  catch (IOException e) { ... }",
                    "",
                    "Urutannya penting: FileNotFoundException adalah turunan",
                    "IOException, jadi kalau IOException ditulis lebih dulu,",
                    "ia menelan keduanya.",
                ]
            },
        ],
    },
    {
        "title": "22. IDisposable & using",
        "sections": [
            {
                "body": [
                    "Garbage collector mengurus MEMORI, dan hanya memori. Ia",
                    "tidak tahu apa-apa tentang berkas yang masih terbuka,",
                    "koneksi database yang masih dipegang, atau soket jaringan.",
                    "Sumber daya seperti itu harus dilepas EKSPLISIT.",
                    "",
                    "Objek yang memegang sumber daya mengimplementasi",
                    "IDisposable, yang isinya satu method: Dispose().",
                    "",
                    "Menulisnya dengan tangan:",
                    "",
                    "  StreamReader r = new StreamReader(path);",
                    "  try { ... }",
                    "  finally { r.Dispose(); }",
                    "",
                    "Pola itu begitu sering dipakai sampai C# memberinya kata",
                    "kunci sendiri:",
                    "",
                    "  using (var r = new StreamReader(path))",
                    "  {",
                    "      ...",
                    "  }   // Dispose() dipanggil di sini, GAGAL ATAU TIDAK",
                    "",
                    "Sejak C# 8 ada bentuk tanpa kurawal — using declaration.",
                    "Objeknya dilepas saat SCOPE-nya berakhir:",
                    "",
                    "  using var r = new StreamReader(path);",
                    "  ... sampai akhir method",
                    "",
                    "Bentuk ini menghemat satu tingkat indentasi, dan di method",
                    "yang membuka tiga berkas sekaligus selisihnya besar.",
                    "",
                    "KAPAN kamu butuh ini: setiap kali sebuah tipe punya",
                    "Dispose. Compiler dan analyzer akan memberi tahu (CA2000).",
                    "Yang paling sering: StreamReader, StreamWriter, FileStream,",
                    "HttpClient, SqlConnection, Bitmap, CancellationTokenSource.",
                ]
            },
            {
                "heading": "Menulis class ber-IDisposable sendiri",
                "code": """using System;
using System.IO;

class Pencatat : IDisposable
{
    private readonly StreamWriter _tulis;
    private bool _sudah;

    public Pencatat(string berkas)
    {
        _tulis = new StreamWriter(berkas, append: true);
        Catat("dibuka");
    }

    public void Catat(string pesan)
    {
        if (_sudah) throw new ObjectDisposedException(nameof(Pencatat));
        _tulis.WriteLine($"[catatan] {pesan}");
    }

    public void Dispose()
    {
        if (_sudah) return;          // Dispose WAJIB aman dipanggil dua kali
        Catat("ditutup");
        _tulis.Dispose();
        _sudah = true;
    }
}

class Program
{
    static void Main()
    {
        string berkas = Path.Combine(Path.GetTempPath(), "catatan-belajar.txt");
        File.Delete(berkas);

        using (var p = new Pencatat(berkas))
        {
            p.Catat("mulai menghitung");
            p.Catat("selesai");
        }

        foreach (string b in File.ReadAllLines(berkas))
            Console.WriteLine(b);

        File.Delete(berkas);
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  [catatan] dibuka",
                    "  [catatan] mulai menghitung",
                    "  [catatan] selesai",
                    "  [catatan] ditutup",
                    "",
                    "Dua aturan Dispose yang mengikat, dan keduanya ada di",
                    "kode di atas:",
                    "",
                    "  1. Dispose WAJIB aman dipanggil berkali-kali. Itu",
                    "     sebabnya ada penjaga `if (_sudah) return;`. Tanpa",
                    "     itu, `using` yang dipanggil setelah kamu sendiri",
                    "     sudah memanggil Dispose akan meledak.",
                    "",
                    "  2. Method lain harus MENOLAK bekerja sesudah Dispose,",
                    "     dengan ObjectDisposedException. Membiarkannya jalan",
                    "     menghasilkan kegagalan yang jauh lebih membingungkan",
                    "     di dalam StreamWriter yang sudah tertutup.",
                    "",
                    "`using` bekerja lewat try/finally, jadi Dispose tetap",
                    "dipanggil kalau blok di dalamnya melempar exception.",
                    "Itulah seluruh alasan ia ada: tanpa `using`, satu",
                    "exception di tengah membuat berkas tidak pernah tertutup",
                    "dan berkas terkunci sampai program mati.",
                    "",
                    "Untuk operasi async ada padanannya:",
                    "  await using var r = new StreamReader(path);",
                    "  yang memanggil DisposeAsync dari IAsyncDisposable.",
                ]
            },
        ],
    },
    {
        "title": "23. async & await",
        "sections": [
            {
                "body": [
                    "async/await menangani operasi yang MENUNGGU: membaca",
                    "berkas besar, memanggil API, query database. Selama",
                    "menunggu, thread-nya dibebaskan untuk mengerjakan hal",
                    "lain alih-alih berdiri diam.",
                    "",
                    "Yang sering disalahpahami sejak awal: async BUKAN tentang",
                    "membuat sesuatu berjalan lebih cepat, dan BUKAN tentang",
                    "membuat thread baru. Ia tentang tidak MEMBUANG thread yang",
                    "sedang menunggu jawaban dari luar.",
                    "",
                    "Tiga kata kuncinya:",
                    "",
                    "  Task            janji: 'nanti selesai, tanpa hasil'",
                    "  Task<T>         janji: 'nanti selesai, hasilnya T'",
                    "  async           menandai method yang boleh memakai await",
                    "  await           tunggu tanpa memblokir thread",
                    "",
                    "  static async Task<string> BacaAsync(string path)",
                    "  {",
                    "      string isi = await File.ReadAllTextAsync(path);",
                    "      return isi.ToUpper();",
                    "  }",
                    "",
                    "Aturan yang wajib dipatuhi:",
                    "",
                    "  1. Method async mengembalikan Task, Task<T>, atau",
                    "     ValueTask. JANGAN `async void` — kecuali untuk",
                    "     event handler UI. Exception di dalam async void",
                    "     TIDAK BISA ditangkap pemanggilnya dan langsung",
                    "     menjatuhkan seluruh proses.",
                    "",
                    "  2. Penamaan: akhiri dengan Async. Ini konvensi .NET",
                    "     yang dipatuhi seluruh pustaka standar.",
                    "",
                    "  3. JANGAN `.Result` atau `.Wait()` pada Task. Keduanya",
                    "     memblokir thread, dan di aplikasi UI atau ASP.NET",
                    "     lama menyebabkan DEADLOCK yang sangat sulit",
                    "     didiagnosis: thread yang menunggu adalah thread yang",
                    "     dibutuhkan untuk menyelesaikan tugasnya.",
                    "",
                    "  4. async menular ke atas. Kalau sebuah method memanggil",
                    "     method async, ia sendiri sebaiknya ikut async sampai",
                    "     ke Main. Sejak C# 7.1 `static async Task Main()` sah.",
                ]
            },
            {
                "heading": "Berurutan versus bersamaan",
                "code": """using System;
using System.Diagnostics;
using System.Threading.Tasks;

class Program
{
    static async Task<string> AmbilAsync(string nama, int ms)
    {
        await Task.Delay(ms);            // pura-pura memanggil jaringan
        return $"{nama} selesai ({ms}ms)";
    }

    static async Task Main()
    {
        var jam = Stopwatch.StartNew();

        // BERURUTAN: satu selesai, baru berikutnya mulai
        Console.WriteLine(await AmbilAsync("A", 200));
        Console.WriteLine(await AmbilAsync("B", 200));
        Console.WriteLine($"Berurutan  ~{jam.ElapsedMilliseconds / 100 * 100} ms");

        // BERSAMAAN: keduanya berjalan, lalu ditunggu bersama
        jam.Restart();
        Task<string> t1 = AmbilAsync("C", 200);
        Task<string> t2 = AmbilAsync("D", 200);
        string[] hasil = await Task.WhenAll(t1, t2);
        foreach (string h in hasil) Console.WriteLine(h);
        Console.WriteLine($"Bersamaan  ~{jam.ElapsedMilliseconds / 100 * 100} ms");
    }
}"""
            },
            {
                "body": [
                    "Keluaran (angkanya dibulatkan ke ratusan ms):",
                    "  A selesai (200ms)",
                    "  B selesai (200ms)",
                    "  Berurutan  ~400 ms",
                    "  C selesai (200ms)",
                    "  D selesai (200ms)",
                    "  Bersamaan  ~200 ms",
                    "",
                    "Inilah kesalahan async yang paling mahal dan paling",
                    "sering: menulis `await` di setiap baris sehingga panggilan",
                    "yang sebenarnya bisa berjalan bersamaan jadi berbaris",
                    "satu-satu. Lima panggilan API masing-masing 200 ms jadi",
                    "1 detik, padahal bisa 200 ms.",
                    "",
                    "Aturannya: MULAI dulu semua task-nya (tanpa await),",
                    "baru tunggu bersama dengan Task.WhenAll.",
                    "",
                    "Method Task yang berguna:",
                    "  Task.Delay(ms)          menunggu tanpa memblokir",
                    "  Task.WhenAll(tasks)     tunggu SEMUA selesai",
                    "  Task.WhenAny(tasks)     tunggu yang PERTAMA selesai",
                    "  Task.Run(() => ...)     jalankan kerja BERAT di thread",
                    "                          pool -- ini yang benar-benar",
                    "                          membuat thread baru",
                    "  Task.FromResult(x)      Task yang sudah selesai",
                    "",
                    "Bedanya Task.Delay dan Thread.Sleep: Delay melepaskan",
                    "thread, Sleep menahannya. Di dalam method async, memakai",
                    "Thread.Sleep membatalkan seluruh gunanya async.",
                    "",
                    "Pembatalan lewat CancellationToken:",
                    "  var cts = new CancellationTokenSource(",
                    "      TimeSpan.FromSeconds(5));",
                    "  await KerjaAsync(cts.Token);",
                    "",
                    "Token itu dioper ke bawah dan diperiksa berkala. Operasi",
                    "yang tidak bisa dibatalkan adalah operasi yang suatu hari",
                    "akan menggantung aplikasimu tanpa jalan keluar.",
                ]
            },
        ],
    },
    {
        "title": "24. Namespace, Assembly & Struktur Proyek",
        "sections": [
            {
                "body": [
                    "NAMESPACE mengelompokkan tipe supaya namanya tidak",
                    "bertabrakan. Ia murni soal penamaan, tidak berpengaruh",
                    "pada apa pun saat program jalan.",
                    "",
                    "  namespace Toko.Domain;      file-scoped, C# 10",
                    "",
                    "  class Produk { }            jadi Toko.Domain.Produk",
                    "",
                    "Bentuk lama memakai kurawal dan membuat seluruh berkas",
                    "menjorok satu tingkat:",
                    "",
                    "  namespace Toko.Domain",
                    "  {",
                    "      class Produk { }",
                    "  }",
                    "",
                    "Konvensinya: namespace mengikuti struktur folder.",
                    "Toko/Domain/Produk.cs berisi Toko.Domain.Produk.",
                    "",
                    "USING mengimpor namespace:",
                    "  using System.Collections.Generic;",
                    "  using Dict = System.Collections.Generic.Dictionary<string, int>;",
                    "  global using System;           berlaku SEKALI untuk",
                    "                                 seluruh proyek (C# 10)",
                    "  using static System.Math;      pakai Sqrt(x), bukan Math.Sqrt(x)",
                    "",
                    "ImplicitUsings di berkas .csproj mengaktifkan sekumpulan",
                    "global using bawaan (System, System.Linq, System.IO, dan",
                    "beberapa lagi). Itu sebabnya proyek .NET 6+ yang baru",
                    "sering tidak punya satu pun baris using di atas.",
                    "",
                    "ASSEMBLY adalah hasil kompilasi: satu berkas .dll atau",
                    ".exe. Satu proyek menghasilkan satu assembly. Modifier",
                    "`internal` berlaku di batas assembly, bukan namespace —",
                    "perbedaan yang sering tertukar.",
                ]
            },
            {
                "heading": "Struktur proyek yang lazim",
                "code": """TokoSaya/
├── TokoSaya.sln                 daftar proyek
├── src/
│   ├── Toko.Domain/             aturan bisnis, tanpa ketergantungan
│   │   ├── Toko.Domain.csproj
│   │   ├── Produk.cs
│   │   └── Pesanan.cs
│   ├── Toko.Data/               akses database
│   │   ├── Toko.Data.csproj
│   │   └── ProdukRepository.cs
│   └── Toko.App/                titik masuk
│       ├── Toko.App.csproj
│       └── Program.cs
└── tests/
    └── Toko.Tests/
        ├── Toko.Tests.csproj
        └── ProdukTests.cs"""
            },
            {
                "body": [
                    "Perintah dotnet yang dipakai sehari-hari:",
                    "",
                    "  dotnet new console -o Nama    proyek konsol baru",
                    "  dotnet new classlib -o Nama   pustaka",
                    "  dotnet new xunit -o Nama      proyek tes",
                    "  dotnet new sln                berkas solusi",
                    "  dotnet sln add src/A/A.csproj",
                    "  dotnet add reference ../B/B.csproj",
                    "  dotnet add package Newtonsoft.Json",
                    "  dotnet restore                unduh paket",
                    "  dotnet build                  kompilasi",
                    "  dotnet run                    kompilasi & jalankan",
                    "  dotnet test                   jalankan tes",
                    "  dotnet publish -c Release     paket siap sebar",
                    "  dotnet format                 rapikan kode",
                    "",
                    "ARAH KETERGANTUNGAN adalah keputusan arsitektur yang",
                    "paling menentukan, dan ia dijaga oleh berkas proyek:",
                    "",
                    "  Toko.App  ->  Toko.Data  ->  Toko.Domain",
                    "",
                    "Domain tidak boleh tahu apa-apa tentang database maupun",
                    "antarmuka. Kalau panah itu pernah dibalik — Domain",
                    "mereferensi Data — aturan bisnisnya jadi tidak bisa diuji",
                    "tanpa database, dan tidak bisa dipakai ulang di aplikasi",
                    "lain. Kabar baiknya, `dotnet add reference` akan MENOLAK",
                    "membuat lingkaran, jadi pelanggaran terbesarnya tertangkap",
                    "otomatis.",
                    "",
                    "Berkas .csproj modern sangat pendek — biasanya di bawah",
                    "sepuluh baris. Kalau kamu melihat berkas proyek sepanjang",
                    "ratusan baris dengan daftar setiap berkas .cs, itu format",
                    ".NET Framework lama.",
                ]
            },
        ],
    },
    {
        "title": "25. Unit Test & Debugging",
        "sections": [
            {
                "body": [
                    "Tes otomatis adalah kode yang memeriksa kode lain. Ia",
                    "menjawab satu pertanyaan yang tidak bisa dijawab dengan",
                    "membaca: 'apakah yang kuubah barusan merusak sesuatu?'",
                    "",
                    "Tiga kerangka tes utama di .NET:",
                    "  xUnit     paling umum di proyek baru",
                    "  NUnit     lama, matang, banyak dipakai",
                    "  MSTest    bawaan Microsoft",
                    "",
                    "Pola AAA yang dipakai di mana-mana:",
                    "",
                    "  [Fact]",
                    "  public void Tambah_DuaPositif_MengembalikanJumlah()",
                    "  {",
                    "      // Arrange -- siapkan",
                    "      var k = new Kalkulator();",
                    "",
                    "      // Act -- kerjakan SATU hal",
                    "      int hasil = k.Tambah(2, 3);",
                    "",
                    "      // Assert -- periksa",
                    "      Assert.Equal(5, hasil);",
                    "  }",
                    "",
                    "Nama tes yang baik memuat tiga bagian: apa yang diuji,",
                    "dalam kondisi apa, dan hasil yang diharapkan. Nama seperti",
                    "`Test1` tidak memberi tahu apa pun saat ia gagal di CI",
                    "tiga bulan kemudian.",
                    "",
                    "[Theory] menjalankan tes yang sama dengan banyak data:",
                    "",
                    "  [Theory]",
                    "  [InlineData(85, \"A\")]",
                    "  [InlineData(75, \"B\")]",
                    "  [InlineData(10, \"E\")]",
                    "  public void Grade_Benar(int nilai, string harap)",
                    "      => Assert.Equal(harap, Rapor.Grade(nilai));",
                    "",
                    "Assert yang sering dipakai:",
                    "  Assert.Equal(harap, aktual)   URUTANNYA: harapan dulu",
                    "  Assert.True(kondisi)",
                    "  Assert.Null(x) / NotNull(x)",
                    "  Assert.Contains(x, koleksi)",
                    "  Assert.Empty(koleksi)",
                    "  Assert.Throws<TException>(() => ...)",
                ]
            },
            {
                "heading": "Menguji tanpa kerangka apa pun",
                "code": """using System;

static class Rapor
{
    public static string Grade(int nilai) => nilai switch
    {
        < 0 or > 100 => throw new ArgumentOutOfRangeException(nameof(nilai)),
        >= 85 => "A",
        >= 75 => "B",
        >= 60 => "C",
        _     => "D",
    };
}

class Program
{
    static int gagal = 0;

    static void Periksa(string nama, object harap, object aktual)
    {
        bool ok = Equals(harap, aktual);
        if (!ok) gagal++;
        Console.WriteLine($"[{(ok ? "OK  " : "GAGAL")}] {nama,-28} "
                        + $"harap={harap} aktual={aktual}");
    }

    static void Main()
    {
        Periksa("nilai 85 -> A", "A", Rapor.Grade(85));
        Periksa("nilai 84 -> B", "B", Rapor.Grade(84));
        Periksa("nilai 60 -> C", "C", Rapor.Grade(60));
        Periksa("nilai  0 -> D", "D", Rapor.Grade(0));

        bool melempar = false;
        try { Rapor.Grade(101); }
        catch (ArgumentOutOfRangeException) { melempar = true; }
        Periksa("nilai 101 -> melempar", true, melempar);

        Console.WriteLine(gagal == 0 ? "SEMUA LULUS" : $"{gagal} GAGAL");
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  [OK  ] nilai 85 -> A                harap=A aktual=A",
                    "  [OK  ] nilai 84 -> B                harap=B aktual=B",
                    "  [OK  ] nilai 60 -> C                harap=C aktual=C",
                    "  [OK  ] nilai  0 -> D                harap=D aktual=D",
                    "  [OK  ] nilai 101 -> melempar        harap=True aktual=True",
                    "  SEMUA LULUS",
                    "",
                    "Perhatikan nilai yang dipilih: 85 dan 84, bukan 90 dan 50.",
                    "Menguji tepat DI BATAS adalah yang paling berharga, karena",
                    "di situlah `>=` versus `>` salah ketik. Nilai di tengah",
                    "rentang hampir tidak pernah menemukan bug.",
                    "",
                    "Ketika sesuatu salah, urutan pemeriksaannya:",
                    "",
                    "  1. BACA pesan errornya sampai habis. Tipe exception,",
                    "     pesan, dan nomor baris paling atas di stack trace",
                    "     biasanya sudah menjawab pertanyaannya.",
                    "  2. Cetak nilai variabel di titik-titik yang dicurigai.",
                    "     Console.WriteLine memang primitif, tapi ia selalu ada",
                    "     dan tidak pernah berbohong.",
                    "  3. Pasang BREAKPOINT lalu telusuri: F10 melangkah satu",
                    "     baris, F11 masuk ke dalam method, F5 lanjut.",
                    "  4. Sempitkan. Buang setengah kode, apakah masih salah?",
                    "     Ulangi. Sepuluh langkah membelah dua menyempitkan",
                    "     seribu baris jadi satu.",
                    "",
                    "Debug.Assert(kondisi) hanya aktif di build Debug dan",
                    "berguna untuk menyatakan hal yang menurutmu MUSTAHIL",
                    "salah. Kalau ia pernah berbunyi, asumsimulah yang keliru —",
                    "dan itu justru informasi yang paling berharga.",
                ]
            },
        ],
    },
    {
        "title": "26. Konvensi Kode & Kualitas",
        "sections": [
            {
                "body": [
                    "Konvensi penamaan .NET, dan hampir seluruh kode C# di",
                    "dunia mematuhinya:",
                    "",
                    "  PascalCase   class, interface, method, property,",
                    "               event, enum, namespace, konstanta",
                    "  camelCase    parameter, variabel lokal",
                    "  _camelCase   field privat",
                    "  IPascalCase  interface, diawali huruf I",
                    "",
                    "  class PesananPembelian          class",
                    "  interface IPenyimpanPesanan     interface",
                    "  public decimal TotalHarga       property",
                    "  private readonly int _jumlah    field privat",
                    "  void HitungTotal(int jumlahItem)  method + parameter",
                    "",
                    "Berbeda dari Java, KONSTANTA di C# memakai PascalCase",
                    "(MaxRetry), bukan SCREAMING_CASE (MAX_RETRY).",
                    "",
                    "Aturan penulisan lain:",
                    "  - Empat spasi untuk indentasi, bukan tab.",
                    "  - Satu tipe per berkas, nama berkas = nama tipe.",
                    "  - using diurutkan, System dulu.",
                    "  - Kurung kurawal di baris baru (gaya Allman).",
                    "  - var dipakai kalau tipenya sudah jelas dari sisi kanan.",
                    "",
                    "Yang lebih penting daripada gaya: KONSISTEN. Kode yang",
                    "seluruhnya memakai gaya yang 'salah' jauh lebih mudah",
                    "dibaca daripada kode yang setengahnya begini setengahnya",
                    "begitu.",
                    "",
                    "Berkas .editorconfig menyimpan aturan itu di repositori",
                    "sehingga setiap editor dan `dotnet format` mematuhinya",
                    "tanpa siapa pun perlu mengingatnya.",
                ]
            },
            {
                "heading": "Contoh .editorconfig minimal",
                "code": """root = true

[*.cs]
indent_style = space
indent_size = 4
end_of_line = lf
insert_final_newline = true
charset = utf-8

# Gaya
csharp_new_line_before_open_brace = all
csharp_style_var_when_type_is_apparent = true:suggestion
dotnet_sort_system_directives_first = true

# Naikkan dari saran jadi PERINGATAN supaya benar-benar terlihat
dotnet_diagnostic.CA2000.severity = warning   # objek IDisposable tak dilepas
dotnet_diagnostic.CA1062.severity = warning   # argumen publik tak diperiksa null
dotnet_diagnostic.CS8618.severity = warning   # field non-nullable tak diisi"""
            },
            {
                "body": [
                    "ANALYZER adalah pemeriksa yang berjalan saat kompilasi.",
                    "Ia menemukan hal yang benar secara sintaks tapi hampir",
                    "pasti bukan yang kamu maksud.",
                    "",
                    "Contoh yang sering ia tangkap:",
                    "  CA1806  hasil method diabaikan (s.Trim(); sendirian)",
                    "  CA2000  objek IDisposable tidak pernah dilepas",
                    "  CA1826  memakai LINQ di tempat indexer lebih tepat",
                    "  CS0168  variabel dideklarasikan tapi tidak dipakai",
                    "  CS8602  mungkin dereference null",
                    "",
                    "Menyalakannya di .csproj:",
                    "  <EnableNETAnalyzers>true</EnableNETAnalyzers>",
                    "  <AnalysisLevel>latest</AnalysisLevel>",
                    "  <TreatWarningsAsErrors>true</TreatWarningsAsErrors>",
                    "",
                    "Baris terakhir itu keputusan yang layak diambil sejak",
                    "proyek masih kecil. Peringatan yang dibiarkan menumpuk",
                    "akan berhenti dibaca sama sekali begitu jumlahnya lewat",
                    "seratus — dan sejak saat itu peringatan yang benar-benar",
                    "penting pun ikut tenggelam.",
                    "",
                    "Beberapa kebiasaan yang membuat kode C# enak dirawat:",
                    "",
                    "  - Kembalikan lebih awal (guard clause) alih-alih",
                    "    membungkus seluruh method dalam if bertingkat.",
                    "  - Buat field readonly kalau ia tidak pernah berubah",
                    "    sesudah constructor. Compiler akan menjaganya.",
                    "  - Jangan kembalikan null untuk koleksi — kembalikan",
                    "    koleksi kosong. Pemanggilnya jadi tidak perlu",
                    "    memeriksa apa pun sebelum foreach.",
                    "  - Satu method satu pekerjaan. Kalau namanya memuat",
                    "    kata 'dan', biasanya ia dua method.",
                ]
            },
        ],
    },
    {
        "title": "27. Membangun Aplikasi Konsol Utuh",
        "sections": [
            {
                "body": [
                    "Materi ini menggabungkan semuanya: class, interface,",
                    "koleksi, LINQ, exception, dan pemisahan tanggung jawab.",
                    "",
                    "Aplikasi yang dibangun: pencatat pengeluaran sederhana.",
                    "Yang penting bukan fiturnya, melainkan CARA bagiannya",
                    "dipisah — karena itulah yang membedakan program 200 baris",
                    "yang bisa dirawat dari yang tidak.",
                    "",
                    "Tiga lapisan, dan panah ketergantungannya satu arah:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "  (Main)         (aturan)      (data)",
                    "",
                    "  MODEL     apa itu sebuah pengeluaran. Tidak tahu",
                    "            apa-apa tentang layar maupun penyimpanan.",
                    "  LAYANAN   aturan: menambah, meringkas, menyaring.",
                    "            Tidak pernah memanggil Console.",
                    "  ANTARMUKA membaca masukan, memanggil layanan,",
                    "            menampilkan hasil. Tidak menghitung apa pun.",
                    "",
                    "Ujinya satu kalimat: kalau aplikasinya diubah jadi",
                    "aplikasi web, berapa banyak kode yang harus disentuh?",
                    "Jawaban yang benar: hanya lapisan antarmuka.",
                    "",
                    "Kesalahan yang paling sering di program pemula adalah",
                    "mencampur ketiganya — menghitung total di tengah",
                    "Console.WriteLine. Programnya jalan, dan tetap jalan",
                    "sampai hari ketika ada yang minta totalnya juga muncul",
                    "di tempat lain.",
                ]
            },
            {
                "heading": "Program utuh",
                "code": """using System;
using System.Collections.Generic;
using System.Linq;

// ---------------------------------------------------------------- MODEL
record Pengeluaran(string Keterangan, string Kategori, decimal Jumlah);

// -------------------------------------------------------------- LAYANAN
class BukuKas
{
    private readonly List<Pengeluaran> _catatan = new();

    public IReadOnlyList<Pengeluaran> Semua => _catatan;

    public void Tambah(Pengeluaran p)
    {
        if (string.IsNullOrWhiteSpace(p.Keterangan))
            throw new ArgumentException("Keterangan wajib diisi");
        if (p.Jumlah <= 0)
            throw new ArgumentOutOfRangeException(nameof(p),
                "Jumlah harus lebih dari nol");
        _catatan.Add(p);
    }

    public decimal Total() => _catatan.Sum(p => p.Jumlah);

    public IEnumerable<(string Kategori, decimal Total, int Banyak)> PerKategori()
        => _catatan.GroupBy(p => p.Kategori)
                   .Select(g => (g.Key, g.Sum(p => p.Jumlah), g.Count()))
                   .OrderByDescending(x => x.Item2);

    public Pengeluaran? Terbesar()
        => _catatan.OrderByDescending(p => p.Jumlah).FirstOrDefault();
}

// ------------------------------------------------------------ ANTARMUKA
class Program
{
    static void Main()
    {
        var kas = new BukuKas();

        var masukan = new[]
        {
            new Pengeluaran("Kopi pagi",   "Makan",     25000m),
            new Pengeluaran("Bensin",      "Transport", 100000m),
            new Pengeluaran("Makan siang", "Makan",     35000m),
            new Pengeluaran("Buku",        "Belajar",   120000m),
            new Pengeluaran("Ojek",        "Transport", 18000m),
        };

        foreach (var p in masukan) kas.Tambah(p);

        // Sengaja gagal, untuk menunjukkan validasinya bekerja
        try { kas.Tambah(new Pengeluaran("", "Lain", 1000m)); }
        catch (ArgumentException e) { Console.WriteLine($"Ditolak: {e.Message}"); }

        Console.WriteLine();
        Console.WriteLine($"{"Keterangan",-14}{"Kategori",-11}{"Jumlah",12}");
        Console.WriteLine(new string('-', 37));
        foreach (var p in kas.Semua)
            Console.WriteLine($"{p.Keterangan,-14}{p.Kategori,-11}{p.Jumlah,12:N0}");

        Console.WriteLine(new string('-', 37));
        Console.WriteLine($"{"TOTAL",-25}{kas.Total(),12:N0}");

        Console.WriteLine();
        Console.WriteLine("Rekap per kategori:");
        foreach (var (kategori, total, banyak) in kas.PerKategori())
            Console.WriteLine($"  {kategori,-11}{total,10:N0}  ({banyak} transaksi)");

        Console.WriteLine();
        Console.WriteLine($"Terbesar: {kas.Terbesar()?.Keterangan ?? "-"}");
    }
}"""
            },
            {
                "body": [
                    "Empat keputusan di program itu yang layak ditiru:",
                    "",
                    "  1. `IReadOnlyList<Pengeluaran> Semua` bukan",
                    "     `List<Pengeluaran>`. Kalau yang dikembalikan List,",
                    "     pemanggil bisa memanggil .Add dan melewati seluruh",
                    "     validasi di method Tambah. Tipe kembalian adalah",
                    "     bagian dari pagar, bukan sekadar anotasi.",
                    "",
                    "  2. Validasi tinggal di LAYANAN, bukan di antarmuka.",
                    "     Kalau nanti ada jalan masuk kedua (impor CSV, API),",
                    "     aturannya tidak perlu ditulis ulang — dan tidak bisa",
                    "     melenceng satu sama lain.",
                    "",
                    "  3. BukuKas tidak memanggil Console sama sekali. Itu yang",
                    "     membuatnya bisa diuji: tes memanggil Total() dan",
                    "     membandingkan angkanya, tanpa perlu membaca layar.",
                    "",
                    "  4. Main tidak menghitung apa pun. Ia cuma menyusun",
                    "     masukan, memanggil, dan mencetak.",
                    "",
                    "Langkah berikutnya kalau kamu ingin melanjutkannya",
                    "sendiri:",
                    "  - Simpan ke berkas JSON lewat System.Text.Json.",
                    "  - Pisahkan penyimpanan di balik interface IPenyimpan,",
                    "    sehingga BukuKas tidak tahu apakah datanya di berkas,",
                    "    di database, atau cuma di memori saat tes.",
                    "  - Tambahkan menu interaktif dan penyaringan tanggal.",
                    "  - Tulis tes xUnit untuk BukuKas — perhatikan bahwa ini",
                    "    langsung bisa dilakukan, tanpa mengubah satu baris pun,",
                    "    justru karena keputusan nomor 3.",
                ]
            },
        ],
    },
]
