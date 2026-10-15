CSHARP_MATERIALS = [
    {
        "title": "1. Pengenalan C# & .NET",
        "sections": [
            {
                "body": [
                    "C# (dibaca \"si-sharp\") adalah bahasa pemrograman buatan Microsoft yang",
                    "dirilis tahun 2000. Perancangnya Anders Hejlsberg, orang yang dulu",
                    "juga bikin Turbo Pascal dan Delphi, dan belakangan TypeScript.",
                    "",
                    "Beberapa sifat C# yang bakal sering kamu temui:",
                    "  - Statically typed. Artinya tipe tiap variabel dicek waktu",
                    "    kompilasi, sebelum programnya jalan. Salah tipe ketahuan duluan.",
                    "  - Object-oriented, yaitu kode disusun dalam class dan objek. Sejak",
                    "    C# 3, gaya fungsional (fungsi dioper ke fungsi lain) juga banyak",
                    "    dipakai.",
                    "  - Managed. Memori diurus garbage collector, bagian runtime yang",
                    "    membersihkan objek yang udah nggak dipakai. Kamu nggak perlu",
                    "    membebaskan memori sendiri kayak di C.",
                    "",
                    "C# dan .NET itu dua hal yang beda. Kalau dari awal kamu bisa",
                    "membedakannya, banyak tutorial jadi lebih gampang dipahami:",
                    "",
                    "  C#     bahasanya  : sintaks yang kamu ketik",
                    "  .NET   platformnya: runtime, library, dan tooling",
                    "",
                    "Kode C# nggak langsung dikompilasi jadi instruksi prosesor. Hasilnya",
                    "IL (Intermediate Language), semacam bahasa perantara. Waktu program",
                    "dijalankan, JIT compiler menerjemahkan IL itu ke instruksi mesin yang",
                    "cocok dengan prosesor yang lagi dipakai. Makanya satu hasil build bisa",
                    "jalan di Windows, Linux, dan macOS.",
                    "",
                    "Sejarahnya perlu kamu tahu sedikit, supaya nggak tersesat waktu",
                    "membaca tutorial lama:",
                    "  - .NET Framework  (2002-2019) Windows saja, versi 1-4.8.",
                    "  - .NET Core       (2016-2020) lintas platform, versi 1-3.1.",
                    "  - .NET            (2020-kini) penerus keduanya, versi 5, 6,",
                    "                    7, 8, 9, dan seterusnya. Tanpa kata Core.",
                    "",
                    "Kalau sebuah tutorial nyebut 'System.Web' atau 'Web Forms', itu .NET",
                    "Framework yang lama. Di sini kita pakai .NET modern.",
                    "",
                    "C# dipakai untuk bikin game di Unity, situs web dengan ASP.NET Core,",
                    "aplikasi mobile dan desktop dengan MAUI, aplikasi web dengan Blazor,",
                    "dan banyak sistem internal di perusahaan besar.",
                    "",
                    "Cara memasangnya:",
                    "  - Unduh SDK dari https://dotnet.microsoft.com/download",
                    "  - Fedora  : sudo dnf install dotnet-sdk-8.0",
                    "  - Cek     : dotnet --version",
                    "",
                    "Cara menjalankan program:",
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
                    "Kita bahas bagian demi bagian:",
                    "",
                    "  using System;",
                    "    Ngasih tahu compiler: kalau aku nulis Console, carinya di",
                    "    namespace System. Namespace itu semacam folder untuk nama-nama",
                    "    class. Tanpa baris ini kamu harus nulis System.Console.WriteLine",
                    "    tiap kali.",
                    "",
                    "  class Program",
                    "    Semua kode C# tinggal di dalam sebuah tipe. Nggak ada fungsi",
                    "    yang berdiri sendiri di luar class seperti di Python atau",
                    "    JavaScript.",
                    "",
                    "  static void Main()",
                    "    Titik masuk program, tempat program mulai jalan. static artinya",
                    "    method ini milik class-nya, bukan milik sebuah objek. Masuk akal,",
                    "    karena waktu program baru mulai belum ada objek apa pun.",
                    "",
                    "  Console.WriteLine(...)",
                    "    Cetak teks lalu pindah baris. Console.Write (tanpa Line) mencetak",
                    "    tanpa pindah baris.",
                    "",
                    "Aturan dasar C#:",
                    "  1. Setiap pernyataan diakhiri titik koma.",
                    "  2. Huruf besar dan kecil dibedakan. Console dan console itu dua",
                    "     nama yang beda.",
                    "  3. Kurung kurawal boleh ditaruh di baris mana aja. Gaya resmi",
                    "     Microsoft menaruhnya di baris baru.",
                    "  4. Nama class dan method pakai PascalCase (HurufBesarTiapKata),",
                    "     variabel lokal pakai camelCase (hurufKecilDiAwal). Compiler",
                    "     nggak memaksa, tapi hampir semua kode C# ditulis begitu.",
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
                    "Sejak C# 9, satu berkas boleh berisi pernyataan langsung, tanpa class",
                    "dan tanpa Main. Bentuk ini namanya top-level statements. Compiler",
                    "tetap bikinin class dan Main di belakang layar. Yang hilang cuma",
                    "tulisannya, aturannya tetap sama.",
                    "",
                    "Syaratnya, cuma satu berkas dalam proyek yang boleh pakai bentuk ini.",
                    "Pernyataannya juga harus ada di paling atas berkas, sebelum deklarasi",
                    "class apa pun.",
                    "",
                    "Di materi ini kita pakai bentuk panjang, karena bentuk itu yang bakal",
                    "kamu lihat di hampir semua kode nyata dan di semua contoh Unity. Tapi",
                    "kalau kamu bikin proyek baru pakai `dotnet new console` di .NET 6 ke",
                    "atas, yang muncul bentuk singkat ini. Jadi jangan kaget.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Tipe Data & Konversi",
        "sections": [
            {
                "body": [
                    "Variabel itu tempat menyimpan nilai, dan di C# setiap variabel harus",
                    "punya tipe. Tipe ditulis di depan namanya:",
                    "",
                    "  int umur = 20;",
                    "  string nama = \"Andi\";",
                    "  double tinggi = 172.5;",
                    "  bool lulus = true;",
                    "",
                    "Kalau malas nulis tipenya, pakai var. Compiler yang menyimpulkan",
                    "tipenya dari nilai awal:",
                    "",
                    "  var umur = 20;        compiler tahu ini int",
                    "  var nama = \"Andi\";    compiler tahu ini string",
                    "",
                    "Hati-hati, var itu bukan tipe dinamis. Begitu compiler menyimpulkan",
                    "int, variabel itu tetap int selamanya. Mengisinya dengan string tetap",
                    "error waktu kompilasi. Yang hilang cuma ketikan tipenya, pemeriksaan",
                    "tipenya tetap jalan.",
                    "",
                    "var juga wajib dikasih nilai awal. `var x;` nggak bisa dikompilasi,",
                    "karena nggak ada nilai yang bisa dipakai untuk menyimpulkan tipenya.",
                    "",
                    "Tipe bilangan bulat:",
                    "  byte     0 .. 255                         1 byte",
                    "  short    -32.768 .. 32.767                2 byte",
                    "  int      -2,1 miliar .. 2,1 miliar        4 byte  <- bawaan",
                    "  long     -9,2 juta triliun .. positifnya  8 byte",
                    "",
                    "Tipe pecahan. Di sini orang paling sering salah pilih:",
                    "  float    ~7 digit presisi     ditulis 3.14f",
                    "  double   ~15 digit presisi    ditulis 3.14   <- bawaan",
                    "  decimal  ~28 digit presisi    ditulis 3.14m",
                    "",
                    "Aturan praktisnya: uang pakai decimal, sisanya double. double",
                    "menyimpan pecahan dalam basis dua, jadi 0.1 nggak pernah tersimpan",
                    "persis 0.1. Selisihnya kecil, tapi kalau dijumlahkan ribuan kali,",
                    "selisih itu jadi rupiah yang hilang di laporan.",
                    "",
                    "Tipe lain:",
                    "  char     satu karakter Unicode, ditulis pakai kutip satu",
                    "  bool     true atau false, TIDAK bisa diisi angka",
                    "  string   deretan karakter, pakai kutip dua",
                    "",
                    "Di C#, `if (1)` itu error. Kondisi wajib bertipe bool. Gara-gara aturan",
                    "ini, salah ketik `if (x = 5)` yang sering bikin bug di C dan C++ nggak",
                    "bisa lolos kompilasi.",
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
                    "const dan readonly sering ketuker. Dua-duanya bikin nilai yang nggak",
                    "bisa diubah, bedanya di kapan nilai itu ditetapkan:",
                    "",
                    "  const   nilainya ditetapkan saat KOMPILASI, jadi hanya",
                    "          boleh angka, string, atau bool literal. Otomatis",
                    "          static. Nilainya disalin ke setiap tempat yang",
                    "          memakainya.",
                    "  readonly nilainya ditetapkan saat OBJEK DIBUAT, boleh",
                    "          hasil perhitungan, dan sesudah itu tidak bisa",
                    "          diubah lagi.",
                    "",
                    "Konversi tipe, yaitu mengubah nilai dari satu tipe ke tipe lain, ada",
                    "dua arah. Namanya udah ngasih tahu risikonya:",
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
                    "Yang sering bikin kaget: (int) memotong angka di belakang koma, nggak",
                    "membulatkan. 9.87 jadi 9, dan -9.87 jadi -9. Kalau maksudmu",
                    "membulatkan, pakai Math.Round.",
                    "",
                    "Untuk mengubah teks jadi angka ada tiga cara, dan pilihannya penting:",
                    "",
                    "  int.Parse(\"42\")              melempar exception kalau gagal",
                    "  Convert.ToInt32(\"42\")        null jadi 0, sisanya exception",
                    "  int.TryParse(\"42\", out n)    mengembalikan bool, tidak melempar",
                    "",
                    "Exception itu sinyal error yang menghentikan program kalau nggak",
                    "ditangkap. Untuk input dari pengguna, hampir selalu pakai TryParse.",
                    "Pengguna salah ketik itu kejadian biasa, dan menangani exception jauh",
                    "lebih mahal daripada ngecek sebuah bool.",
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
                    "Coba lihat `out int angka` yang dideklarasikan langsung di dalam",
                    "pemanggilan TryParse. Sebelum C# 7, kamu harus nulis `int angka;` di",
                    "baris terpisah dulu. Bentuk yang baru ini bikin variabelnya lahir",
                    "persis di tempat dia dipakai.",
                    "",
                    "Keluaran program di atas:",
                    "  \"42\" -> 42",
                    "  \"3.5\" -> bukan bilangan bulat",
                    "  \"sembilan\" -> bukan bilangan bulat",
                    "  \"\" -> bukan bilangan bulat",
                    "",
                    "\"3.5\" gagal karena yang diminta int. Teksnya sendiri angka, cuma",
                    "bukan bilangan bulat. Kalau pakai double.TryParse, \"3.5\" bakal",
                    "diterima.",
                ]
            },
        ],
    },
    {
        "title": "3. Operator & Ekspresi",
        "sections": [
            {
                "body": [
                    "Operator itu simbol untuk menghitung atau membandingkan nilai. Yang",
                    "paling dasar operator aritmetika:",
                    "  +   tambah          a + b",
                    "  -   kurang          a - b",
                    "  *   kali            a * b",
                    "  /   bagi            a / b",
                    "  %   sisa bagi       a % b",
                    "",
                    "Jebakan: 7 / 2 hasilnya 3, bukan 3.5. Hampir semua pemula C# kena ini.",
                    "Kalau dua-duanya bilangan bulat, yang dipakai pembagian bulat, dan",
                    "angka di belakang koma dibuang. Supaya hasilnya 3.5, salah satu sisi",
                    "harus pecahan:",
                    "",
                    "  7 / 2         3",
                    "  7.0 / 2       3.5",
                    "  (double)7 / 2 3.5",
                    "  7 / 2.0       3.5",
                    "",
                    "Operator penugasan gabungan, singkatan untuk mengubah isi variabel:",
                    "  +=  -=  *=  /=  %=",
                    "  x += 5  sama dengan  x = x + 5",
                    "",
                    "Untuk menambah atau mengurangi satu ada ++ dan --. Letaknya",
                    "berpengaruh:",
                    "  i++   pakai nilainya DULU, baru tambah",
                    "  ++i   tambah DULU, baru pakai nilainya",
                    "",
                    "  int i = 5;",
                    "  Console.WriteLine(i++);   cetak 5, i jadi 6",
                    "  Console.WriteLine(++i);   i jadi 7, cetak 7",
                    "",
                    "Operator perbandingan menghasilkan bool, yaitu true atau false:",
                    "  ==  !=  <  >  <=  >=",
                    "",
                    "Operator logika untuk menggabungkan beberapa kondisi:",
                    "  &&  DAN, hubung-singkat",
                    "  ||  ATAU, hubung-singkat",
                    "  !   NEGASI",
                    "",
                    "Hubung-singkat (short-circuit) artinya sisi kanan nggak dievaluasi",
                    "kalau hasilnya udah pasti dari sisi kiri. Misalnya di &&, kalau sisi",
                    "kiri false, hasilnya pasti false, jadi sisi kanan dilewati. Sifat ini",
                    "yang bikin pola pengaman ini aman:",
                    "",
                    "  if (nama != null && nama.Length > 0)",
                    "",
                    "Kalau nama null, nama.Length nggak pernah dijalankan, jadi",
                    "NullReferenceException (error karena memakai sesuatu yang isinya null)",
                    "nggak terjadi. Kalau kamu pakai & (satu ampersand), kedua sisi selalu",
                    "dievaluasi, dan kode itu bakal error.",
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
                    "Empat operator di atas bikin kode C# modern jauh lebih pendek daripada",
                    "C# lama:",
                    "",
                    "  ?:    ternary, sudah ada sejak awal",
                    "  ??    null-coalescing",
                    "  ??=   null-coalescing assignment",
                    "  ?.    null-conditional, sering disebut Elvis operator",
                    "",
                    "`a?.b` artinya: kalau a null, seluruh ekspresinya langsung bernilai",
                    "null tanpa memanggil apa pun. Sisa rantainya ikut berhenti. Jadi di",
                    "`a?.b.c.d`, kalau a null, .b, .c, dan .d nggak ada yang dipanggil.",
                    "",
                    "Hasil `a?.b` selalu nullable, artinya boleh berisi null. Makanya",
                    "`kosong?.Length` bertipe int?, bukan int, dan perlu `?? -1` supaya",
                    "jadi int biasa.",
                    "",
                    "Urutan operasi, dari yang dikerjakan paling dulu:",
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
                    "Kalau ragu, pakai tanda kurung. Kode yang gampang dibaca lebih",
                    "berguna daripada kode yang cuma bisa dipahami orang yang hafal tabel",
                    "ini.",
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
                    "Membaca ketikan pengguna:",
                    "  string? baris = Console.ReadLine();",
                    "",
                    "Perhatikan tanda tanya di string?. Artinya ReadLine bisa",
                    "mengembalikan null. Itu terjadi kalau masukannya habis, misalnya",
                    "input dialirkan dari berkas dan berkasnya udah selesai dibaca. Tanda",
                    "tanya itu cara compiler ngingetin kamu supaya kemungkinan null ini",
                    "ikut dipikirin.",
                    "",
                    "Ada tiga cara menyusun teks. Kode modern biasanya pakai yang ketiga:",
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
                    "Tanda dolar di depan kutip yang menyalakan interpolasi. Di dalam",
                    "kurung kurawal kamu boleh nulis ekspresi apa aja, nggak harus nama",
                    "variabel. Jadi $\"Total {harga * jumlah:N0}\" itu sah.",
                    "",
                    "Sesudah titik dua kamu bisa nulis format:",
                    "  {n:C}      mata uang       Rp1.234,00",
                    "  {n:N0}     angka, 0 desimal  1.234",
                    "  {n:F2}     pecahan, 2 desimal 1234,00",
                    "  {n:P1}     persen          12,3%",
                    "  {n:X}      heksadesimal    4D2",
                    "  {t:yyyy-MM-dd}  tanggal     2026-09-22",
                    "",
                    "Untuk perataan, pakai koma. {nama,-15} artinya rata kiri selebar 15,",
                    "{harga,10} artinya rata kanan selebar 10. Dengan cara ini kamu bisa",
                    "bikin tabel di konsol tanpa ngetik spasi satu per satu.",
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
                    "Ingat: string di C# itu immutable, artinya isinya nggak bisa diubah",
                    "sesudah dibuat. s.ToUpper() nggak mengubah s. Dia bikin string baru",
                    "lalu mengembalikannya. Kalau hasilnya nggak kamu tampung, nggak",
                    "terjadi apa-apa:",
                    "",
                    "  nama.ToUpper();          tidak berguna, hasilnya dibuang",
                    "  nama = nama.ToUpper();   ini yang benar",
                    "",
                    "Untuk ngecek string kosong ada dua method, dan bedanya penting:",
                    "  string.IsNullOrEmpty(s)        null atau \"\"",
                    "  string.IsNullOrWhiteSpace(s)   null, \"\", atau \"   \"",
                    "",
                    "Untuk memeriksa masukan pengguna, biasanya yang kamu perlukan",
                    "IsNullOrWhiteSpace. Orang yang cuma menekan spasi lalu Enter juga",
                    "belum mengisi apa-apa.",
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
                    "Ada tiga bentuk penulisan string:",
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
                    "Escape itu kode berawalan backslash untuk karakter khusus, misalnya",
                    "\\n untuk baris baru. Bentuk verbatim dan raw bisa digabung dengan",
                    "interpolasi: $@\"...\" atau $\"\"\"...\"\"\".",
                    "",
                    "Menggabung string di dalam perulangan yang panjang bikin program",
                    "lambat. Karena string immutable, tiap `s += x` bikin string baru dan",
                    "menyalin seluruh isinya. Seribu kali menggabung berarti seribu kali",
                    "menyalin, dan yang disalin makin lama makin besar. Untuk kasus begini",
                    "ada StringBuilder:",
                    "",
                    "  var sb = new StringBuilder();",
                    "  for (int i = 0; i < 1000; i++) sb.Append(i).Append(' ');",
                    "  string hasil = sb.ToString();",
                    "",
                    "Kalau cuma lima atau sepuluh kali menggabung, nggak usah repot.",
                    "Interpolasi lebih gampang dibaca, dan bedanya nggak kerasa.",
                ]
            },
        ],
    },
    {
        "title": "5. Percabangan: if, switch & Pattern Matching",
        "sections": [
            {
                "body": [
                    "Percabangan bikin program memilih jalan berdasarkan sebuah kondisi.",
                    "Bentuk dasarnya if:",
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
                    "Kalau isinya cuma satu pernyataan, kurung kurawal boleh dihilangkan.",
                    "Tapi jangan. Bug \"goto fail;\" di Apple tahun 2014 terjadi persis",
                    "karena ini. Seseorang menambah baris kedua di bawah if tanpa kurawal,",
                    "dan baris itu ternyata selalu dijalankan, apa pun kondisinya.",
                    "",
                    "Kondisinya wajib bertipe bool. Di C, angka selain nol dianggap benar.",
                    "Di C# aturan itu nggak ada. `if (5)` nggak bisa dikompilasi, begitu",
                    "juga `if (x = 5)`, karena hasil penugasan itu int. Jadi bug gara-gara",
                    "salah ketik = untuk == nggak mungkin lolos.",
                    "",
                    "switch klasik dipakai untuk mencocokkan satu nilai dengan banyak",
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
                    "Aturan: di C#, break itu wajib. Beda dengan C atau Java, C# menolak",
                    "mengompilasi case yang berisi kode tapi nggak diakhiri break, return,",
                    "atau goto case. Di C, lupa break bikin program terus jalan ke case",
                    "berikutnya (namanya fall-through), dan itu sumber banyak bug. C#",
                    "menjadikannya error.",
                    "",
                    "Case kosong yang ditumpuk seperti case 1: case 2: tetap boleh, karena",
                    "maksudnya jelas: dua nilai itu ditangani dengan cara yang sama.",
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
                    "Ada tiga beda dengan switch klasik, dan semuanya disengaja:",
                    "",
                    "  1. Switch expression itu ekspresi, jadi menghasilkan nilai. Hasilnya",
                    "     bisa langsung dikembalikan atau disimpan ke variabel.",
                    "  2. Nggak ada break sama sekali. Fall-through nggak perlu dicegah,",
                    "     karena di sini nggak ada urutan perintah yang dijalankan. Yang",
                    "     ada cuma pencocokan.",
                    "  3. Compiler ngasih peringatan kalau ada kemungkinan nilai yang belum",
                    "     ditangani. `_` menangkap semua sisanya, sama seperti default.",
                    "",
                    "Bagian di sebelah kiri `=>` disebut pola (pattern). Pola bisa jauh",
                    "lebih dari sekadar satu nilai:",
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
                    "Ada dua hal yang perlu kamu lihat di contoh tadi.",
                    "",
                    "Ingat: urutan pola itu berpengaruh. `int n when n < 0` harus ditulis",
                    "sebelum `int n`, karena pencocokan berhenti di pola pertama yang",
                    "cocok. Kalau dibalik, cabang bilangan negatif nggak akan pernah",
                    "kepakai, dan compiler bakal protes.",
                    "",
                    "`when` menambahkan syarat di atas polanya. Di contoh ini `int n when",
                    "n < 0` hasilnya sama dengan pola relasional `< 0`. Bedanya, `when`",
                    "boleh berisi ekspresi apa aja, termasuk memanggil method.",
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
                    "Pattern matching ini salah satu yang bikin C# modern terasa beda dari",
                    "C# tahun 2005. Rantai if-else bertingkat yang dulu panjang sekarang",
                    "bisa jadi satu ekspresi, yang dibaca dari atas ke bawah seperti tabel.",
                ]
            },
        ],
    },
    {
        "title": "6. Perulangan: for, while, foreach",
        "sections": [
            {
                "body": [
                    "Perulangan dipakai untuk menjalankan kode yang sama berkali-kali. C#",
                    "punya empat bentuk, masing-masing untuk keperluan sendiri:",
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
                    "Di dalam kurung for ada tiga bagian: nilai awal; syarat lanjut;",
                    "langkah. Ketiganya boleh dikosongkan. `for (;;)` itu perulangan tanpa",
                    "akhir yang sah.",
                    "",
                    "while:",
                    "  int sisa = 3;",
                    "  while (sisa > 0)",
                    "  {",
                    "      Console.WriteLine($\"sisa {sisa}\");",
                    "      sisa--;",
                    "  }",
                    "",
                    "do-while. Perhatikan titik koma di bagian paling akhir:",
                    "  do",
                    "  {",
                    "      Console.WriteLine(\"jalan minimal sekali\");",
                    "  } while (false);",
                    "",
                    "foreach, bentuk yang paling sering dipakai:",
                    "  foreach (string nama in daftar)",
                    "      Console.WriteLine(nama);",
                    "",
                    "Aturan foreach ada dua. Variabel perulangannya nggak bisa diubah.",
                    "Koleksinya juga nggak boleh ditambah atau dikurangi selama perulangan",
                    "jalan. Kalau aturan kedua dilanggar, program melempar",
                    "InvalidOperationException waktu jalan, bukan waktu kompilasi. Kalau",
                    "kamu perlu menghapus sambil menelusuri, bikin salinan dulu, atau",
                    "telusuri mundur pakai for.",
                    "",
                    "Untuk mengendalikan perulangan:",
                    "  break     keluar dari perulangan TERDEKAT",
                    "  continue  lompat ke iterasi berikutnya",
                    "",
                    "C# nggak punya `break 2` seperti PHP. Kalau mau keluar dari dua",
                    "perulangan sekaligus, pindahkan perulangan dalamnya ke sebuah method,",
                    "lalu pakai return. Cara ini hampir selalu lebih gampang dibaca",
                    "daripada label dan goto. Label dan goto memang ada di C#, tapi",
                    "sebaiknya nggak kamu pakai.",
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
                    "Di perulangan bersarang, perulangan dalam selesai seluruhnya untuk",
                    "setiap satu putaran perulangan luar. Di contoh atas ada 9 baris kali",
                    "9 kolom, jadi badan perulangan dalam dijalankan 81 kali.",
                    "",
                    "Kesalahan yang paling sering: `Console.WriteLine()` untuk pindah baris",
                    "ditaruh di dalam perulangan dalam. Hasilnya 81 baris, masing-masing",
                    "cuma berisi satu angka.",
                    "",
                    "Ada dua pola perulangan yang bakal kamu temui di mana-mana:",
                    "",
                    "  AKUMULATOR: kumpulkan hasil",
                    "    int total = 0;",
                    "    foreach (int n in angka) total += n;",
                    "",
                    "  PENJAGA: cari yang pertama cocok lalu berhenti",
                    "    string? ketemu = null;",
                    "    foreach (string s in daftar)",
                    "        if (s.StartsWith(\"A\")) { ketemu = s; break; }",
                    "",
                    "Nanti di LINQ dua pola ini punya versi satu baris, yaitu Sum dan",
                    "FirstOrDefault. Kalau kamu paham bentuk panjangnya dulu, LINQ bakal",
                    "terasa seperti singkatan, dan kamu tahu apa yang dikerjakannya.",
                ]
            },
        ],
    },
    {
        "title": "7. Array & Indeks",
        "sections": [
            {
                "body": [
                    "Array menyimpan sejumlah nilai bertipe sama, dan jumlahnya tetap.",
                    "Ukurannya ditentukan waktu array dibuat dan nggak bisa berubah lagi.",
                    "",
                    "Cara membuat array:",
                    "  int[] a = new int[5];              5 elemen, semua 0",
                    "  int[] b = { 10, 20, 30 };          langsung berisi",
                    "  int[] c = new int[] { 10, 20 };    bentuk panjangnya",
                    "  var d = new[] { 10, 20, 30 };      tipe disimpulkan",
                    "",
                    "Elemen array yang belum diisi otomatis berisi nilai kosong tipenya",
                    "(zero value):",
                    "  angka  -> 0",
                    "  bool   -> false",
                    "  char   -> '\\0'",
                    "  tipe referensi (string, class) -> null",
                    "",
                    "Cara mengakses:",
                    "  a[0] = 7;              index dimulai dari NOL",
                    "  Console.WriteLine(a[0]);",
                    "  Console.WriteLine(a.Length);",
                    "",
                    "Jebakan: index di luar jangkauan melempar IndexOutOfRangeException",
                    "waktu program jalan. Array 5 elemen punya index 0 sampai 4, jadi a[5]",
                    "itu error. Ini kesalahan yang paling sering dibuat programmer, di",
                    "bahasa apa pun.",
                    "",
                    "Sejak C# 8, kamu bisa menghitung index dari belakang:",
                    "  a[^1]     elemen TERAKHIR",
                    "  a[^2]     satu sebelum terakhir",
                    "",
                    "Baca ^ sebagai \"dari akhir\". a[^1] sama dengan a[a.Length - 1], tapi",
                    "jauh lebih susah salah tulis.",
                    "",
                    "Rentang (range), juga sejak C# 8:",
                    "  a[1..4]   elemen index 1, 2, 3   (batas atas EKSKLUSIF)",
                    "  a[..3]    tiga elemen pertama",
                    "  a[2..]    dari index 2 sampai habis",
                    "  a[..]     salinan seluruhnya",
                    "",
                    "Batas atas eksklusif artinya index terakhir itu nggak ikut diambil.",
                    "Untungnya, panjang rentang selalu akhir dikurangi awal: a[1..4] berisi",
                    "4 - 1 = 3 elemen.",
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
                    "Perhatikan `(double)total / nilai.Length`. Tanpa (double), yang dibagi",
                    "dua int, dan hasilnya dipotong jadi bilangan bulat. Ini jebakan yang",
                    "paling sering muncul waktu menghitung rata-rata.",
                    "",
                    "`nilai.Clone()` bikin salinan. Tanpa itu, Array.Sort bakal",
                    "mengurutkan array aslinya. Array itu tipe referensi, jadi",
                    "`int[] urut = nilai;` cuma ngasih nama kedua untuk array yang sama.",
                    "Nggak ada salinan yang dibuat.",
                    "",
                    "Ini beda tipe nilai dan tipe referensi, dan array biasanya tempat",
                    "pertama kamu ketemu masalah ini. Variabel bertipe nilai menyimpan",
                    "isinya sendiri. Variabel bertipe referensi cuma menyimpan alamat",
                    "menuju isinya:",
                    "",
                    "  int a = 5; int b = a; b = 9;      a tetap 5",
                    "  int[] x = {1}; int[] y = x; y[0]=9;  x[0] JADI 9",
                    "",
                    "Method statis di kelas Array yang sering berguna:",
                    "  Array.Sort(a)            urutkan menaik, mengubah a",
                    "  Array.Reverse(a)         balik urutannya, mengubah a",
                    "  Array.IndexOf(a, 5)      posisi pertama, -1 kalau tidak ada",
                    "  Array.Fill(a, 7)         isi semua elemen dengan 7",
                    "  Array.Resize(ref a, 10)  buat array baru lalu salin isinya",
                    "",
                    "Nama Array.Resize itu menipu, karena ukuran array nggak bisa diubah.",
                    "Yang terjadi: array baru dibuat, isi lama disalin ke sana, lalu",
                    "variabelmu diarahkan ke array baru itu. Kalau kamu sering perlu",
                    "menambah dan menghapus isi, yang kamu butuhkan itu List<T>.",
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
                    "Array bertingkat ada dua bentuk, dan yang membedakan cuma tanda",
                    "bacanya:",
                    "",
                    "  int[,]   satu KOMA di dalam kurung -> dua dimensi",
                    "           persegi panjang. Satu objek, satu blok memori,",
                    "           semua baris wajib sama panjang.",
                    "  int[][]  dua pasang kurung -> array dari array.",
                    "           Setiap baris objek sendiri, panjangnya bebas.",
                    "",
                    "Cara mengaksesnya juga beda: kotak[1, 2] dan gerigi[1][2].",
                    "",
                    "Untuk matriks dan papan permainan, `int[,]` lebih cocok, karena semua",
                    "barisnya memang sama panjang. Untuk data yang panjang tiap barisnya",
                    "beda, misalnya daftar nilai tiap murid, pakai jagged. Kalau salah",
                    "pilih, kode yang membacanya jadi berbelit.",
                ]
            },
        ],
    },
    {
        "title": "8. List, Dictionary & Koleksi Generik",
        "sections": [
            {
                "body": [
                    "Ukuran array itu tetap. Untuk koleksi yang bisa tumbuh dan menyusut,",
                    ".NET menyediakan koleksi generik di namespace",
                    "System.Collections.Generic.",
                    "",
                    "Huruf T di List<T> artinya \"tipe apa aja yang kamu tentukan\".",
                    "List<int> menyimpan int, List<string> menyimpan string, dan compiler",
                    "memastikan nggak ada nilai bertipe lain yang nyasar masuk.",
                    "",
                    "List<T> itu array yang bisa tumbuh:",
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
                    "Array pakai .Length, List pakai .Count. Bedanya cuma karena sejarah,",
                    "dan hampir semua programmer C# pernah salah nulis.",
                    "",
                    "Dictionary<TKey, TValue> menyimpan pasangan kunci dan nilai, seperti",
                    "kamus: kamu cari kuncinya, kamu dapat nilainya.",
                    "  var umur = new Dictionary<string, int>();",
                    "  umur[\"Andi\"] = 20;",
                    "  umur[\"Budi\"] = 22;",
                    "  umur.Add(\"Cici\", 19);   melempar kalau kunci sudah ada",
                    "  umur[\"Andi\"] = 21;      menimpa tanpa peringatan",
                    "",
                    "Membaca kunci yang nggak ada, misalnya umur[\"Dedi\"], melempar",
                    "KeyNotFoundException. Ada dua cara aman:",
                    "",
                    "  if (umur.TryGetValue(\"Dedi\", out int u)) ...",
                    "  if (umur.ContainsKey(\"Dedi\")) ...",
                    "",
                    "TryGetValue lebih baik. Kalau pakai ContainsKey lalu mengambil",
                    "nilainya, kamu mencari dua kali di tabel hash yang sama.",
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
                    "Pasangan `TryGetValue(k, out int n)` lalu `hitung[k] = n + 1` itu cara",
                    "yang biasa dipakai di C# untuk menghitung frekuensi. Kalau kuncinya",
                    "belum ada, TryGetValue mengembalikan false dan sekaligus mengisi n",
                    "dengan 0. Jadi n + 1 tetap benar tanpa perlu if sama sekali.",
                    "",
                    "Kalau kamu menelusuri Dictionary pakai foreach, yang kamu dapat",
                    "KeyValuePair<TKey, TValue>, dengan properti .Key dan .Value. Sejak",
                    "C# 7 kamu bisa langsung memecahnya jadi dua variabel:",
                    "",
                    "  foreach (var (nama, umur) in kamus)",
                    "      Console.WriteLine($\"{nama} {umur}\");",
                    "",
                    "Jebakan: urutan penelusuran Dictionary nggak dijamin. Urutannya",
                    "sering kebetulan sama dengan urutan waktu dimasukkan, dan justru itu",
                    "yang menjebak. Begitu ada isi yang dihapus lalu ditambah lagi,",
                    "urutannya bisa berubah. Kalau urutan penting, urutkan sendiri pakai",
                    "LINQ (OrderBy), atau pakai SortedDictionary.",
                    "",
                    "Koleksi generik lain yang perlu kamu kenal:",
                    "",
                    "  HashSet<T>       himpunan, tanpa duplikat, cek cepat",
                    "  Queue<T>         antre: Enqueue masuk, Dequeue keluar (FIFO)",
                    "  Stack<T>         tumpuk: Push masuk, Pop keluar (LIFO)",
                    "  SortedDictionary selalu terurut berdasarkan kunci",
                    "  LinkedList<T>    sisip/hapus di tengah murah",
                    "",
                    "Cara memilihnya: butuh index, pakai List. Butuh mencari berdasarkan",
                    "nama, pakai Dictionary. Butuh tahu \"yang ini udah pernah dilihat",
                    "belum\", pakai HashSet. Sisanya jarang dipakai.",
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
                    "HashSet.Add mengembalikan bool: true kalau nilainya berhasil",
                    "ditambahkan, false kalau nilainya udah ada. Dengan itu, \"kerjakan cuma",
                    "kalau belum pernah dilihat\" bisa ditulis dalam satu baris:",
                    "",
                    "  if (sudahDiproses.Add(id)) Proses(id);",
                    "",
                    "Queue itu kayak antrean kasir. Yang datang duluan dilayani duluan.",
                    "Stack itu kayak tumpukan piring. Yang ditaruh terakhir diambil duluan,",
                    "sama seperti tombol Back di browser, yang memang memakai stack.",
                    "",
                    "Peek cuma melihat isi paling depan tanpa mengambilnya. Dequeue dan Pop",
                    "mengambilnya. Dua-duanya melempar InvalidOperationException kalau",
                    "koleksinya kosong, jadi cek .Count dulu, atau pakai TryDequeue dan",
                    "TryPop.",
                ]
            },
        ],
    },
    {
        "title": "9. Method, Parameter & Overloading",
        "sections": [
            {
                "body": [
                    "Method itu blok kode yang dikasih nama, supaya bisa dipanggil",
                    "berulang kali tanpa ditulis ulang. Bentuk lengkapnya:",
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
                    "Parameter itu nilai yang dikirim ke method waktu dipanggil, di sini a",
                    "dan b. Tipe kembalian itu tipe nilai yang dikirim balik lewat return.",
                    "Kalau tipenya void, method itu nggak mengembalikan apa-apa. Di method",
                    "void kamu boleh nulis `return;` polos untuk keluar lebih awal.",
                    "",
                    "Kalau isi method cuma satu ekspresi, ada bentuk pendeknya, namanya",
                    "expression-bodied member:",
                    "  static int Tambah(int a, int b) => a + b;",
                    "",
                    "Tanda => di sini bukan lambda. Dia cuma singkatan dari",
                    "{ return ...; }. Bentuk ini juga bisa dipakai untuk property,",
                    "constructor, dan operator.",
                    "",
                    "Parameter opsional punya nilai bawaan, jadi boleh nggak diisi:",
                    "  static void Sapa(string nama, string salam = \"Halo\")",
                    "  Sapa(\"Andi\");                 -> Halo, Andi",
                    "  Sapa(\"Budi\", \"Selamat pagi\"); -> Selamat pagi, Budi",
                    "",
                    "Aturan: parameter opsional wajib ditaruh sesudah parameter yang",
                    "wajib, dan nilai bawaannya harus konstanta yang udah diketahui waktu",
                    "kompilasi.",
                    "",
                    "Argumen bernama bikin pemanggilan lebih gampang dibaca:",
                    "  Sapa(salam: \"Hai\", nama: \"Cici\");",
                    "",
                    "Gunanya kerasa di pemanggilan seperti `Gambar(true, false, true)`.",
                    "Dari situ kamu nggak tahu apa arti tiap true dan false. Bandingkan",
                    "dengan `Gambar(tebal: true, miring: false, garisBawah: true)`, yang",
                    "langsung jelas.",
                    "",
                    "params bikin jumlah argumennya bebas:",
                    "  static int Total(params int[] angka)",
                    "  Total(1, 2, 3);        boleh",
                    "  Total();               boleh, array kosong",
                    "  Total(new[] {1, 2});   boleh juga",
                    "",
                    "params harus jadi parameter terakhir, dan cuma boleh ada satu.",
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
                    "Tanpa ref, `Tukar` nggak berpengaruh apa-apa, karena yang dikirim ke",
                    "method cuma salinan nilainya. Dengan ref, yang dikirim adalah rujukan",
                    "ke variabel aslinya, jadi perubahan di dalam method ikut kena ke",
                    "variabel pemanggil.",
                    "",
                    "Kapan pakai yang mana:",
                    "  ref   method perlu MENGUBAH variabel pemanggil",
                    "  out   method perlu mengembalikan LEBIH DARI SATU nilai",
                    "  in    parameter besar (struct) yang cuma dibaca; tanpa",
                    "        salinan, tapi dijamin tidak berubah",
                    "",
                    "Kata kuncinya wajib ditulis di dua tempat: di deklarasi method dan di",
                    "pemanggilan. Ini disengaja. Orang yang membaca baris pemanggilan",
                    "langsung tahu bahwa variabelnya mungkin berubah.",
                    "",
                    "Untuk mengembalikan dua nilai, tuple sering lebih rapi daripada out.",
                    "Tuple itu beberapa nilai yang dibungkus jadi satu:",
                    "",
                    "  static (int hasil, int sisa) Bagi(int a, int b)",
                    "      => (a / b, a % b);",
                    "",
                    "  var (h, s) = Bagi(17, 5);",
                    "",
                    "Pakai out kalau salah satu keluarannya berarti \"berhasil atau nggak\",",
                    "seperti pola TryXxx (misalnya TryParse). Pakai tuple kalau dua-duanya",
                    "sama-sama hasil yang kamu cari.",
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
                    "Overloading artinya beberapa method punya nama yang sama, tapi jumlah",
                    "atau tipe parameternya beda. Compiler memilih yang paling cocok waktu",
                    "kompilasi.",
                    "",
                    "Yang nggak bisa membedakan overload:",
                    "  - Tipe kembalian. Dua method yang parameternya sama tapi tipe",
                    "    kembaliannya beda itu error.",
                    "  - Nama parameternya.",
                    "",
                    "Yang bisa membedakan: jumlah, tipe, dan urutan parameter, juga ada",
                    "atau nggaknya ref, out, atau in. Tapi dua method yang bedanya cuma ref",
                    "lawan out (atau in) nggak boleh.",
                    "",
                    "Perhatikan `Luas(2.0)`. Kalau ditulis `Luas(2)`, compiler memilih",
                    "versi int dan hasilnya 4, padahal yang kamu mau luas lingkaran.",
                    "Overload yang cuma beda int dan double gampang bikin bingung. Lebih",
                    "baik kasih nama yang beda.",
                    "",
                    "Rekursi artinya method memanggil dirinya sendiri:",
                    "",
                    "  static long Faktorial(int n)",
                    "      => n <= 1 ? 1 : n * Faktorial(n - 1);",
                    "",
                    "Jebakan: setiap rekursi wajib punya kasus dasar, yaitu kondisi untuk",
                    "berhenti (di sini n <= 1). Tanpa itu, tumpukan pemanggilan habis dan",
                    "program mati dengan StackOverflowException. Exception ini nggak bisa",
                    "ditangkap pakai try-catch, jadi programnya langsung berhenti.",
                ]
            },
        ],
    },
    {
        "title": "10. Nullable & Null-Safety",
        "sections": [
            {
                "body": [
                    "Null artinya \"nggak nunjuk ke apa-apa\". Bayangin kertas alamat yang",
                    "masih kosong: kertasnya ada, tapi nggak ada rumah yang bisa didatangi.",
                    "",
                    "Kalau kamu mengakses anggota dari sesuatu yang null, program melempar",
                    "NullReferenceException. Itu error runtime, yaitu error yang baru muncul",
                    "waktu program jalan. Tony Hoare, orang yang pertama kali memperkenalkan",
                    "null, menyebutnya \"kesalahan seharga satu miliar dolar\".",
                    "",
                    "C# membagi tipe jadi dua golongan. Golongan itu yang menentukan",
                    "apakah sebuah variabel bisa null:",
                    "",
                    "  Tipe nilai (value type)",
                    "    int, double, bool, char, struct, enum",
                    "    Disimpan langsung. Secara alami tidak bisa null.",
                    "",
                    "  Tipe referensi (reference type)",
                    "    string, array, class, interface, delegate",
                    "    Menyimpan alamat. Bisa null.",
                    "",
                    "Tipe nilai menyimpan isinya langsung di variabel. Tipe referensi cuma",
                    "menyimpan alamat objeknya, dan alamat itu boleh kosong.",
                    "",
                    "Supaya tipe nilai bisa null, tambahkan tanda tanya di belakang tipenya:",
                    "  int? umur = null;",
                    "  double? suhu = null;",
                    "",
                    "int? itu nama pendek untuk Nullable<int>. Nullable<int> adalah struct",
                    "dengan dua anggota: HasValue (ada isinya atau nggak) dan Value",
                    "(isinya).",
                    "",
                    "  if (umur.HasValue) Console.WriteLine(umur.Value);",
                    "  int pasti = umur ?? 0;",
                    "  int juga = umur.GetValueOrDefault();",
                    "",
                    "Operator ?? artinya \"pakai nilai di kiri, tapi kalau nilai itu null,",
                    "pakai nilai di kanan\". GetValueOrDefault melakukan hal yang mirip, dan",
                    "untuk int nilai cadangannya 0.",
                    "",
                    "Jebakan: membaca .Value waktu HasValue bernilai false melempar",
                    "InvalidOperationException. Makanya ?? hampir selalu jadi pilihan yang",
                    "lebih aman.",
                    "",
                    "Nullable reference types",
                    "",
                    "C# 8 menambahkan fitur bernama nullable reference types. Di proyek",
                    "baru sejak .NET 6, fitur ini nyala secara bawaan (lewat setelan",
                    "<Nullable>enable</Nullable> di .csproj). Dengan fitur ini, aturan",
                    "tanda tanya tadi berlaku juga untuk tipe referensi:",
                    "",
                    "  string nama = null;    PERINGATAN: mungkin null",
                    "  string? nama = null;   sah, kamu bilang ini boleh null",
                    "",
                    "Jadi string tanpa tanda tanya dianggap nggak boleh null. Kalau kamu",
                    "mengisinya dengan null, compiler ngasih peringatan.",
                    "",
                    "Ingat: semua ini cuma pemeriksaan compiler. Waktu program jalan, string",
                    "dan string? itu tipe yang persis sama. Tanda tanyanya nggak mencegah",
                    "null masuk dari JSON, database, atau library lama. Gunanya memaksa kamu",
                    "memikirkan null di tempat yang tepat.",
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
                    "Bagian paling berguna dari contoh itu ada di method Rapikan. Sesudah",
                    "baris `if (string.IsNullOrWhiteSpace(masukan)) return ...`, compiler",
                    "tahu masukan pasti nggak null di sisa method, jadi dia berhenti ngasih",
                    "peringatan.",
                    "",
                    "Kemampuan ini namanya flow analysis. Compiler mengikuti alur program",
                    "untuk tahu nilai apa yang mungkin ada di tiap baris. Cara ini juga",
                    "jalan untuk `if (x != null)`, `is not null`, dan pola lain.",
                    "",
                    "Operator ! (namanya null-forgiving) mematikan peringatan itu:",
                    "  string pasti = mungkinNull!;",
                    "",
                    "Operator ini nggak memeriksa apa pun. Dia cuma bilang ke compiler",
                    "\"percaya aja sama aku\". Tiap kali kamu menulisnya, tanggung jawab",
                    "ngecek null pindah dari compiler ke kamu.",
                    "",
                    "Kadang itu memang perlu, misalnya sesudah pemeriksaan yang nggak",
                    "dikenali compiler. Tapi kalau satu berkas penuh tanda seru, artinya",
                    "fitur null-safety di berkas itu udah dimatikan tanpa ada yang sadar.",
                    "",
                    "Terakhir, soal `is null` dan `== null`. Hasilnya biasanya sama. Bedanya,",
                    "operator == bisa di-overload, artinya sebuah class boleh mengganti cara",
                    "kerja == untuk dirinya sendiri. `is null` nggak bisa diganti. Jadi untuk",
                    "ngecek null, `is null` dan `is not null` lebih aman.",
                ]
            },
        ],
    },
    {
        "title": "11. Class & Objek",
        "sections": [
            {
                "body": [
                    "Class itu cetakan, objek itu barang hasil cetakannya. Bayangin cetakan",
                    "kue: dari satu cetakan kamu bisa bikin banyak kue, dan tiap kue boleh",
                    "punya topping sendiri. Begitu juga satu class bisa menghasilkan ribuan",
                    "objek, masing-masing dengan isinya sendiri.",
                    "",
                    "Isi sebuah class:",
                    "  field        variabel milik objek",
                    "  property     akses terkendali ke data",
                    "  constructor  dipanggil saat objek dibuat",
                    "  method       perilaku",
                    "",
                    "Modifier akses menentukan siapa yang boleh memakai sebuah anggota.",
                    "Urutannya dari yang paling terbuka:",
                    "",
                    "  public              siapa pun boleh",
                    "  internal            hanya di dalam assembly ini (bawaan",
                    "                      untuk class)",
                    "  protected           class ini dan turunannya",
                    "  private             hanya di dalam class ini (bawaan",
                    "                      untuk anggota class)",
                    "  protected internal  gabungan protected ATAU internal",
                    "  private protected   turunan yang ada di assembly ini saja",
                    "",
                    "Assembly itu hasil kompilasi satu proyek, biasanya berupa satu berkas",
                    ".dll atau .exe.",
                    "",
                    "Aturan praktisnya: mulai dari private, lalu buka cuma kalau memang",
                    "perlu. Sesuatu yang udah public nggak bisa ditutup lagi tanpa merusak",
                    "kode orang lain yang terlanjur memakainya.",
                    "",
                    "Objek dibuat pakai new:",
                    "  var p = new Murid(\"Andi\", 20);",
                    "  Murid q = new(\"Budi\", 21);    bentuk singkat C# 9",
                    "",
                    "Kata `this` menunjuk objek yang sedang dikerjakan. Kamu wajib",
                    "menulisnya cuma kalau ada nama yang bentrok, misalnya parameter yang",
                    "namanya sama dengan field. Di tempat lain boleh ditulis supaya kodenya",
                    "lebih jelas.",
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
                    "Ada empat hal yang perlu kamu perhatikan di class itu:",
                    "  1. Field privat diawali garis bawah, misalnya _nama. Compiler nggak",
                    "     mewajibkannya, ini cuma kebiasaan di .NET. Hampir semua kode C#",
                    "     mengikutinya, karena field jadi langsung beda dari parameter dan",
                    "     variabel lokal.",
                    "  2. Setter-nya memvalidasi. Di dalam set, value adalah nilai yang",
                    "     sedang dimasukkan. Ini alasan utama property ada: kalau _nilai",
                    "     dibuat public, nggak ada yang bisa mencegah orang mengisinya",
                    "     9999.",
                    "     Enkapsulasi artinya menjaga objek supaya selalu dalam keadaan yang",
                    "     masuk akal. Menyembunyikan data cuma caranya.",
                    "  3. Constructor menulis `Nilai = nilai`, dan sengaja nggak menulis",
                    "     `_nilai = nilai`. Lewat property, validasinya ikut jalan sejak",
                    "     objek pertama dibuat.",
                    "  4. ToString di-override, artinya diganti dengan versi buatan sendiri.",
                    "     Tiap objek .NET punya ToString bawaan yang cuma mencetak nama",
                    "     tipenya ('Murid'). Dengan menggantinya, objek bisa langsung dicetak",
                    "     dan hasilnya ada artinya.",
                    "",
                    "nameof(value) menghasilkan string \"value\". Bedanya dengan mengetik",
                    "\"value\" langsung: kalau nanti nama parameternya diganti, nameof ikut",
                    "berubah, sedangkan string biasa nggak. Makanya nameof lebih aman",
                    "daripada mengetik nama di dalam tanda kutip.",
                ]
            },
        ],
    },
    {
        "title": "12. Property, Constructor & Inisialisasi",
        "sections": [
            {
                "body": [
                    "Di dalam kurung kurawal property, get artinya boleh dibaca dan set",
                    "artinya boleh diisi. Dari situ property punya beberapa bentuk. Ini",
                    "urutannya dari yang paling ringkas:",
                    "",
                    "  Auto-property",
                    "    public string Nama { get; set; }",
                    "    Compiler membuatkan field tersembunyinya sendiri.",
                    "",
                    "  Hanya-baca dari luar",
                    "    public string Nama { get; private set; }",
                    "",
                    "  Hanya-baca sepenuhnya",
                    "    public string Nama { get; }",
                    "    Hanya bisa diisi di constructor atau di deklarasinya.",
                    "",
                    "  Init-only  (C# 9)",
                    "    public string Nama { get; init; }",
                    "    Bisa diisi saat objek dibuat lewat object initializer,",
                    "    sesudah itu terkunci.",
                    "",
                    "  Nilai bawaan",
                    "    public int Jumlah { get; set; } = 1;",
                    "",
                    "  Terhitung (tidak menyimpan apa pun)",
                    "    public double Luas => Panjang * Lebar;",
                    "",
                    "  Required  (C# 11)",
                    "    public required string Nama { get; init; }",
                    "    Compiler menolak pembuatan objek yang tidak mengisinya.",
                    "",
                    "Object initializer adalah cara mengisi property langsung waktu objek",
                    "dibuat:",
                    "",
                    "  var p = new Produk",
                    "  {",
                    "      Nama = \"Keyboard\",",
                    "      Harga = 350000m,",
                    "  };",
                    "",
                    "Jebakan: isi kurung kurawal itu baru dijalankan sesudah constructor",
                    "selesai. Jadi validasi di constructor nggak melihat nilai-nilai ini.",
                    "Itu alasan kuat untuk memakai `required` dan `init`, daripada berharap",
                    "orang ingat mengisi semua yang perlu.",
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
                    "Ada tiga hal yang layak diperhatikan:",
                    "  - `: this(pemilik, 0m)` itu constructor berantai. Constructor yang",
                    "    pendek nggak menyalin isi constructor utama. Dia memanggilnya. Jadi",
                    "    kalau validasinya berubah, kamu cukup mengubahnya di satu tempat.",
                    "  - `private static int _urutan` adalah anggota statis. Anggota statis",
                    "    dimiliki class, dan nggak dimiliki tiap objek. Cuma ada satu",
                    "    _urutan untuk seluruh program, berapa pun rekening yang dibuat. Itu",
                    "    yang bikin penomoran otomatisnya jalan.",
                    "  - `Saldo { get; private set; }` artinya dunia luar boleh membaca",
                    "    saldo, tapi cuma class ini yang boleh mengubahnya. Itu pun cuma",
                    "    lewat Setor dan Tarik, yang udah memvalidasi jumlahnya. Kalau",
                    "    setternya public, seluruh aturan perbankan di class ini bisa",
                    "    dilewati dengan satu baris.",
                    "",
                    "Primary constructor (C# 12) bikin bentuk ini lebih pendek lagi:",
                    "",
                    "  class Titik(int x, int y)",
                    "  {",
                    "      public int X => x;",
                    "      public int Y => y;",
                    "  }",
                    "",
                    "Parameter x dan y langsung bisa dipakai di seluruh badan class.",
                    "Praktis untuk tipe kecil.",
                    "",
                    "Hati-hati: parameter primary constructor bisa diubah. Kalau ada method",
                    "yang menugaskan nilai baru ke x, isinya ikut berubah tanpa peringatan.",
                    "Property hanya-baca nggak bisa kena masalah ini.",
                ]
            },
        ],
    },
    {
        "title": "13. Pewarisan & Polimorfisme",
        "sections": [
            {
                "body": [
                    "Pewarisan artinya sebuah class mengambil seluruh isi class lain, lalu",
                    "menambah atau mengubah sebagiannya. Class yang diwarisi disebut induk,",
                    "yang mewarisi disebut turunan.",
                    "",
                    "  class Hewan { ... }",
                    "  class Kucing : Hewan { ... }",
                    "",
                    "Tanda titik dua di situ dibaca \"turunan dari\". C# cuma mengizinkan satu",
                    "class induk. Pewarisan berganda seperti di C++ nggak ada, karena",
                    "masalah \"diamond\" yang ditimbulkannya lebih besar daripada manfaatnya.",
                    "Masalah diamond muncul kalau dua induk sama-sama mewarisi satu class",
                    "yang sama, lalu sama-sama mengubah method yang sama. Turunannya jadi",
                    "nggak tahu harus memakai versi yang mana.",
                    "",
                    "Kalau kamu butuh berbagi perilaku dari banyak sumber, pakai interface.",
                    "Interface dibahas di materi berikutnya.",
                    "",
                    "Tiga kata kunci mengatur override, yaitu mengganti method induk dengan",
                    "versi milik turunan:",
                    "",
                    "  virtual   di induk: 'method ini boleh diganti turunan'",
                    "  override  di turunan: 'aku mengganti method induk'",
                    "  sealed    'berhenti di sini, tidak boleh diturunkan lagi'",
                    "",
                    "Di C#, method secara bawaan nggak virtual. Ini beda dari Java, dan",
                    "memang disengaja. Method yang bisa di-override adalah janji ke orang",
                    "yang memakai class-mu, jadi harus dipilih dengan sadar.",
                    "",
                    "Kalau turunan menulis method dengan nama yang sama tanpa override,",
                    "compiler ngasih peringatan dan menyarankan kata `new`. Kata `new` cuma",
                    "menyembunyikan method induk, dan nggak menggantinya. Bedanya baru",
                    "kelihatan kalau objeknya dipegang lewat variabel bertipe induk:",
                    "",
                    "  Hewan h = new Kucing();",
                    "  h.Suara();   override -> versi Kucing",
                    "               new      -> versi Hewan",
                    "",
                    "Jebakan: karena itu, `new` hampir selalu bug yang tinggal nunggu waktu.",
                    "Kamu mengira method Kucing yang jalan, padahal yang jalan versi Hewan.",
                    "",
                    "base menunjuk induk:",
                    "  base.Suara();              panggil versi induk",
                    "  public Kucing(...) : base(...)   panggil constructor induk",
                    "",
                    "Ingat: constructor induk selalu dijalankan lebih dulu, entah kamu",
                    "menulis `: base(...)` atau nggak. Kalau induk nggak punya constructor",
                    "tanpa parameter, kamu wajib menulis `: base(...)` sendiri.",
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
                    "Pemisah desimalnya ikut setelan wilayah komputer. Di locale Indonesia",
                    "pemisahnya koma, di locale Inggris titik.",
                    "",
                    "Yang barusan kamu lihat namanya polimorfisme: satu panggilan yang bisa",
                    "menjalankan method berbeda-beda. Di dalam foreach, `b.Luas()` memanggil",
                    "method yang beda di tiap putaran. Padahal kodenya cuma satu baris, dan",
                    "tipe variabelnya cuma Bangun.",
                    "",
                    "Siapa yang memilih versinya? Objek yang sedang dipegang, waktu program",
                    "jalan. Compiler nggak ikut memilih.",
                    "",
                    "Akibatnya, kalau kamu menambah bangun baru, misalnya Segitiga, nggak",
                    "ada satu baris pun di Main yang perlu disentuh. Begitulah cara mengukur",
                    "desain berorientasi objek yang berhasil: hitung berapa banyak kode lama",
                    "yang nggak perlu disunting waktu ada yang baru. Jumlah class-nya nggak",
                    "jadi ukuran.",
                    "",
                    "Soal abstract class:",
                    "  - Nggak bisa dibuat langsung pakai new. `new Bangun(...)` itu error.",
                    "  - Boleh punya method tanpa badan (abstract), dan juga method biasa,",
                    "    field, dan constructor.",
                    "  - Turunan wajib mengisi semua method abstract, atau ikut dinyatakan",
                    "    abstract.",
                ]
            },
        ],
    },
    {
        "title": "14. Interface",
        "sections": [
            {
                "body": [
                    "Interface adalah kontrak: daftar kemampuan yang wajib dimiliki sebuah",
                    "class, tanpa penjelasan cara melakukannya.",
                    "",
                    "  interface IBisaSimpan",
                    "  {",
                    "      void Simpan(string berkas);",
                    "      bool Sudah { get; }",
                    "  }",
                    "",
                    "Nama interface di .NET diawali huruf I besar. Compiler nggak",
                    "mewajibkannya. Tapi seluruh .NET mengikuti kebiasaan ini, dan kode",
                    "yang melanggarnya terasa asing.",
                    "",
                    "Anggota interface otomatis public dan abstract. Di C# versi lama,",
                    "menulis `public` di dalam interface malah error.",
                    "",
                    "Interface atau abstract class? Ini pertanyaan wawancara yang selalu",
                    "muncul, dan jawabannya sederhana:",
                    "",
                    "  Abstract class menjawab 'ini adalah apa'",
                    "    Kucing adalah Hewan. Satu induk, berbagi keadaan.",
                    "",
                    "  Interface menjawab 'ini bisa apa'",
                    "    Kucing bisa dibandingkan, bisa disimpan, bisa",
                    "    ditelusuri. Sebanyak yang perlu.",
                    "",
                    "Keadaan maksudnya data yang disimpan objek, misalnya isi field-nya.",
                    "",
                    "Perbedaan teknisnya:",
                    "  - Sebuah class cuma boleh punya satu induk, tapi boleh",
                    "    mengimplementasi banyak interface. Mengimplementasi artinya mengisi",
                    "    semua kemampuan yang dijanjikan interface itu.",
                    "  - Interface nggak punya field milik objek dan nggak punya",
                    "    constructor. Jadi interface nggak menyimpan keadaan apa pun.",
                    "  - Sejak C# 8, interface boleh punya implementasi bawaan (default",
                    "    interface method). Fitur ini ditambahkan supaya interface yang udah",
                    "    dirilis bisa ditambah anggota baru tanpa merusak kode yang udah",
                    "    memakainya.",
                    "  - struct juga boleh mengimplementasi interface, padahal struct nggak",
                    "    bisa mewarisi class.",
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
                    "Yang terjadi di sini: `rak.Sort()` nggak tahu apa-apa soal buku. Dia",
                    "cuma memanggil CompareTo untuk tiap pasangan buku yang dibandingkan.",
                    "Dengan mengimplementasi IComparable, class-mu langsung nyambung ke",
                    "seluruh mesin pengurutan .NET. Kamu nggak perlu menulis satu baris",
                    "kode pengurutan pun.",
                    "",
                    "Arti nilai yang dikembalikan CompareTo:",
                    "  negatif  aku lebih dulu",
                    "  nol      sama posisinya",
                    "  positif  aku belakangan",
                    "",
                    "Aturan: kalau kamu meng-override Equals, kamu juga wajib meng-override",
                    "GetHashCode. Hash adalah angka ringkas yang dipakai Dictionary dan",
                    "HashSet untuk mencari barang dengan cepat. Dua objek yang sama menurut",
                    "Equals harus punya hash yang sama.",
                    "",
                    "Kalau aturan itu dilanggar, Dictionary dan HashSet gagal menemukan",
                    "barang yang jelas ada di dalamnya, dan nggak ada error apa pun.",
                    "HashCode.Combine mengurus hal ini untukmu.",
                    "",
                    "Interface penting lain di .NET:",
                    "  IEnumerable<T>  bisa di-foreach; syarat semua LINQ",
                    "  IDisposable     punya sumber daya yang harus dilepas",
                    "  IComparer<T>    aturan urutan yang terpisah dari objeknya",
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
                    "C# punya tiga cara bikin tipe sendiri. Pilihannya menentukan hal yang",
                    "paling dasar: apa yang terjadi waktu sebuah nilai disalin ke variabel",
                    "lain.",
                    "",
                    "  class   tipe referensi. Menyalin = menyalin alamatnya.",
                    "          Dua variabel menunjuk objek yang sama.",
                    "  struct  tipe nilai. Menyalin = menyalin seluruh isinya.",
                    "          Dua variabel berisi data yang terpisah.",
                    "  record  class (atau struct) dengan kesetaraan berdasarkan",
                    "          nilai dan sejumlah besar kode yang dibuatkan.",
                    "",
                    "Kesetaraan berdasarkan nilai artinya dua objek dianggap sama kalau",
                    "isinya sama.",
                    "",
                    "struct cocok untuk benda kecil yang isinya nggak berubah dan",
                    "perilakunya mirip angka: titik koordinat, rentang tanggal, jumlah",
                    "uang. Tipe bawaan .NET seperti int, double, bool, DateTime, TimeSpan,",
                    "dan Guid semuanya struct.",
                    "",
                    "Aturan praktis memilih struct: ukurannya di bawah 16 byte, isinya",
                    "nggak berubah setelah dibuat, dan dia nggak bakal sering di-boxing.",
                    "Boxing artinya tipe nilai dibungkus jadi objek supaya bisa diperlakukan",
                    "sebagai object, dan itu makan memori tambahan. Kalau ragu, pakai class.",
                    "",
                    "record ada sejak C# 9. Dia menjawab kebutuhan yang sering banget",
                    "muncul: \"aku cuma butuh wadah data\". Satu baris ini:",
                    "",
                    "  record Titik(int X, int Y);",
                    "",
                    "udah menghasilkan class lengkap dengan:",
                    "  - constructor;",
                    "  - dua property init-only;",
                    "  - Equals yang membandingkan nilai, beserta GetHashCode;",
                    "  - ToString yang enak dibaca;",
                    "  - operator == dan !=;",
                    "  - deconstructor, untuk memecah objek jadi beberapa variabel;",
                    "  - dukungan untuk `with`.",
                    "",
                    "Kalau ditulis tangan, semua itu sekitar 60 baris, dan gampang salah di",
                    "satu-dua bagiannya.",
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
                    "Baris kedua keluaran itu sumber bug yang paling sering ditemui pemula.",
                    "Mengubah c2 ternyata ikut mengubah c1, karena dua-duanya cuma nama",
                    "lain untuk objek yang sama. Dengan class, menyalin sebuah objek butuh",
                    "usaha sendiri: constructor penyalin, method Clone, atau record",
                    "ditambah with.",
                    "",
                    "Baris ketiga: dua objek record yang berbeda dianggap sama karena",
                    "isinya sama. Kalau Barang itu class biasa, hasilnya False, karena class",
                    "membandingkan alamat.",
                    "",
                    "`with` bikin salinan dengan sebagian anggota diganti, dan objek aslinya",
                    "nggak disentuh. Pola ini berguna banget untuk data yang nggak boleh",
                    "berubah. Daripada mengubah objeknya, kamu bikin versi berikutnya.",
                    "",
                    "Varian record:",
                    "  record            = record class, tipe referensi",
                    "  record class      = sama, ditulis eksplisit",
                    "  record struct     = tipe nilai, anggotanya bisa diubah",
                    "  readonly record struct = tipe nilai, benar-benar beku",
                    "",
                    "Kapan pakai record? Untuk DTO (data transfer object, yaitu wadah data",
                    "yang dikirim antarbagian program), hasil query, pesan, event, dan",
                    "konfigurasi. Pokoknya apa pun yang lebih pas disebut \"data\" daripada",
                    "\"benda yang punya perilaku\".",
                ]
            },
        ],
    },
    {
        "title": "16. Enum & Konstanta Bernama",
        "sections": [
            {
                "body": [
                    "Enum adalah sekumpulan konstanta bernama yang tipenya sama. Gunanya",
                    "mengganti angka yang nggak jelas artinya di tengah kode. Programmer",
                    "menyebut angka kayak gitu magic number.",
                    "",
                    "  enum Status { Draf, Terkirim, Disetujui, Ditolak }",
                    "",
                    "Di baliknya, enum tetap angka: Draf = 0, Terkirim = 1, dan seterusnya.",
                    "Nilainya juga bisa kamu tentukan sendiri:",
                    "",
                    "  enum Prioritas { Rendah = 1, Sedang = 5, Tinggi = 10 }",
                    "",
                    "Kenapa ini lebih baik daripada `int status = 2`?",
                    "  - Compiler menolak nilai yang bukan anggota enum, setidaknya selama",
                    "    kamu nggak memakai cast eksplisit.",
                    "  - Nama anggotanya muncul di autocomplete editor.",
                    "  - switch atas enum diperiksa kelengkapannya oleh analyzer, yaitu alat",
                    "    pemeriksa kode yang jalan bareng compiler.",
                    "  - ToString ngasih namanya, bukan angkanya.",
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
                    "Jebakan: cast dari angka nggak divalidasi. `(Status)99` itu sah, dan",
                    "hasilnya enum bernilai 99 yang nggak punya nama. Kalau nilainya datang",
                    "dari luar program (database, JSON, masukan pengguna), periksa dulu",
                    "pakai Enum.IsDefined.",
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
                    "Enum yang diberi atribut [Flags] bisa menyimpan banyak pilihan",
                    "sekaligus dalam satu angka. Caranya lewat bit, yaitu digit 0 dan 1 di",
                    "bentuk biner angka itu. Syaratnya, nilai anggotanya harus pangkat dua",
                    "(1, 2, 4, 8, 16, ...), supaya tiap anggota punya bit sendiri. Lihat",
                    "komentar 0001, 0010, 0100, dan 1000 di kode tadi.",
                    "",
                    "Operasinya:",
                    "  a | b     gabungkan (tambah izin)",
                    "  a & b     irisan (apa yang sama-sama ada)",
                    "  a & ~b    buang b dari a",
                    "  a.HasFlag(b)  apakah b termasuk di a",
                    "",
                    "Atribut [Flags] sendiri nggak mengubah cara kerja operasi bit. Operator",
                    "| dan & jalan di enum apa pun. Yang diubah [Flags] cuma ToString. Tanpa",
                    "[Flags], `editor` di atas dicetak sebagai '3'. Dengan [Flags],",
                    "hasilnya 'Baca, Tulis'.",
                    "",
                    "Pola ini dipakai di banyak tempat di .NET, misalnya FileAccess,",
                    "RegexOptions, dan BindingFlags. Izin berkas di sistem operasi juga",
                    "memakai cara yang sama.",
                    "",
                    "Nilai 0 sebaiknya diberi nama, misalnya 'Tidak' atau 'None'.",
                    "",
                    "Jebakan: HasFlag terhadap nilai 0 selalu true. Jadi jangan pakai",
                    "HasFlag untuk ngecek \"nggak punya izin apa pun\". Bandingkan langsung:",
                    "`if (izin == Izin.Tidak)`.",
                ]
            },
        ],
    },
    {
        "title": "17. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "Exception adalah cara program bilang \"ada masalah yang nggak bisa aku",
                    "atasi sendiri\". Bedanya dengan mengembalikan kode error: exception",
                    "nggak bisa diabaikan begitu aja. Kalau nggak ada yang menangkapnya,",
                    "programnya berhenti.",
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
                    "Cara bacanya:",
                    "  - try berisi kode yang mungkin gagal.",
                    "  - catch menangkap exception dengan tipe tertentu.",
                    "  - finally selalu dijalankan, entah tadi gagal atau nggak.",
                    "",
                    "Urutan catch ada artinya: yang paling spesifik harus di atas. Kalau",
                    "`catch (Exception)` ditulis lebih dulu, catch di bawahnya nggak pernah",
                    "tercapai, dan compiler menolak kode itu.",
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
                    "Catatan: pembagian double dengan nol nggak melempar apa-apa. Hasilnya",
                    "double.PositiveInfinity, double.NegativeInfinity, atau double.NaN",
                    "(untuk 0.0 / 0.0). DivideByZeroException cuma dilempar oleh pembagian",
                    "bilangan bulat dan decimal.",
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
                    "Exception buatan sendiri dibuat dengan mewarisi class Exception, lalu",
                    "meneruskan pesannya lewat `: base(...)`. Gunanya kalau pemanggil perlu",
                    "membedakan kegagalan itu dari kegagalan lain, atau butuh data tambahan,",
                    "misalnya berapa kurangnya saldo di contoh ini. Kalau nggak butuh",
                    "dua-duanya, pakai exception bawaan aja.",
                    "",
                    "Ada empat kebiasaan buruk yang sering kejadian, dan akibatnya mahal:",
                    "  - catch kosong, seperti `catch (Exception) { }`. Ini menelan semua",
                    "    kesalahan, termasuk yang nggak kamu duga, dan program jalan terus",
                    "    dalam keadaan rusak. Bug kayak gini bisa baru kelihatan",
                    "    berjam-jam kemudian, jauh dari penyebabnya.",
                    "  - `throw e;` untuk melempar ulang. Cara ini menghapus jejak tumpukan",
                    "    (stack trace) aslinya, yaitu catatan urutan pemanggilan sampai",
                    "    error terjadi. Akibatnya log menunjuk baris catch-mu, dan baris",
                    "    yang gagal nggak tercatat. Tulis `throw;` polos.",
                    "  - Exception untuk alur normal. Pengguna salah ketik itu hal biasa,",
                    "    jadi pakai TryParse. Berkas konfigurasi belum ada waktu program",
                    "    pertama kali jalan juga hal biasa, jadi cek dulu pakai File.Exists.",
                    "  - Menangkap exception yang nggak bisa kamu perbaiki. Biarkan",
                    "    exception naik ke pemanggil yang tahu harus berbuat apa. Itu lebih",
                    "    baik daripada ditangani setengah-setengah di tempat yang nggak tahu",
                    "    konteksnya.",
                    "",
                    "Kata `when` menyaring catch. Catch-nya cuma menangkap kalau syaratnya",
                    "terpenuhi. Kalau syaratnya false, exception itu nggak ditangkap sama",
                    "sekali dan terus naik ke pemanggil:",
                    "  catch (HttpRequestException e)",
                    "      when (e.StatusCode == HttpStatusCode.NotFound)",
                ]
            },
        ],
    },
    {
        "title": "18. Generic: Tipe sebagai Parameter",
        "sections": [
            {
                "body": [
                    "Generic bikin satu class atau method bisa dipakai untuk tipe apa pun,",
                    "tanpa kehilangan pemeriksaan tipe. Tipenya jadi semacam parameter:",
                    "kamu tulis T dulu, lalu tipe aslinya diisi waktu dipakai.",
                    "",
                    "Sebelum ada generic (di C# 1), koleksi menyimpan object:",
                    "  ArrayList daftar = new ArrayList();",
                    "  daftar.Add(\"halo\");",
                    "  daftar.Add(42);              tidak ada yang mencegah",
                    "  int n = (int)daftar[0];      MELEDAK saat program jalan",
                    "",
                    "Ada dua kerugian. Pertama, kesalahannya baru ketahuan waktu program",
                    "jalan. Kedua, tiap int yang masuk harus di-boxing, yaitu dibungkus jadi",
                    "objek di heap (bagian memori tempat objek disimpan).",
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
                    "T di situ disimpulkan compiler dari argumen yang kamu kirim, jadi kamu",
                    "nggak perlu menulisnya sendiri.",
                    "",
                    "Constraint (`where`) ngasih tahu compiler apa yang boleh kamu lakukan",
                    "pada T. Tanpa `where T : IComparable<T>`, compiler nggak tahu bahwa T",
                    "punya CompareTo, jadi dia menolak kodenya.",
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
                    "`default` adalah nilai bawaan T, apa pun T-nya: 0 untuk int, null untuk",
                    "string, false untuk bool. Kata `default` berlaku untuk semua tipe",
                    "sekaligus. Nggak ada cara lain untuk menulis \"nilai kosongnya T\".",
                    "",
                    "`typeof(T).Name` membaca nama tipe waktu program jalan. Makanya",
                    "keluarannya Int32 dan String, yaitu nama .NET untuk int dan string.",
                    "",
                    "Di sini C# beda dari Java. Informasi tipe generic di C# nggak dihapus",
                    "waktu kompilasi (istilahnya, nggak ada type erasure). List<int> dan",
                    "List<string> memang tipe yang berbeda waktu program jalan, dan",
                    "List<int> menyimpan int langsung tanpa boxing. Untuk sejuta angka,",
                    "selisih memorinya bisa puluhan megabyte.",
                ]
            },
        ],
    },
    {
        "title": "19. Delegate, Event & Lambda",
        "sections": [
            {
                "body": [
                    "Delegate itu tipe yang isinya sebuah method. Dengan delegate, method",
                    "bisa disimpan di variabel, dikirim sebagai argumen, dan dikembalikan",
                    "dari method lain, sama seperti angka atau string.",
                    "",
                    "  delegate int Operasi(int a, int b);",
                    "  Operasi f = Tambah;          tanpa tanda kurung!",
                    "  Console.WriteLine(f(3, 4));",
                    "",
                    "Perhatikan, Tambah ditulis tanpa tanda kurung. Kalau pakai kurung,",
                    "methodnya langsung dipanggil. Tanpa kurung, yang disimpan methodnya",
                    "sendiri.",
                    "",
                    "Dalam praktik kamu jarang bikin delegate sendiri. .NET udah",
                    "menyediakan tiga jenis yang cukup untuk hampir semua keperluan:",
                    "",
                    "  Action            tanpa parameter, tanpa kembalian",
                    "  Action<T>         terima T, tanpa kembalian",
                    "  Action<T1,T2>     sampai 16 parameter",
                    "  Func<TResult>     tanpa parameter, kembalikan TResult",
                    "  Func<T,TResult>   terima T, kembalikan TResult",
                    "  Predicate<T>      terima T, kembalikan bool",
                    "",
                    "Cara membaca Func<...>: tipe yang paling akhir itu tipe kembaliannya,",
                    "sisanya parameter. Jadi Func<int, string, bool> artinya menerima int",
                    "dan string, lalu mengembalikan bool.",
                    "",
                    "Lambda itu method tanpa nama yang ditulis langsung di tempat:",
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
                    "Baca x => x * x sebagai \"x jadi x kali x\".",
                    "",
                    "Lambda bisa memakai variabel di sekitarnya. Ini namanya closure.",
                    "Hati-hati, yang ditangkap lambda itu variabelnya, bukan salinan",
                    "nilainya:",
                    "",
                    "  int batas = 10;",
                    "  Func<int, bool> kecil = x => x < batas;",
                    "  batas = 100;",
                    "  kecil(50);        TRUE -- membaca batas yang SEKARANG",
                    "",
                    "Hasil ini sering bikin kaget, dan di dalam perulangan sering jadi",
                    "bug. Untungnya, sejak C# 5 variabel foreach dibuat baru di tiap",
                    "putaran. Jadi `foreach (var x in ...) aksi.Add(() => Console.Write(x))`",
                    "jalan sesuai harapan. Variabel `for` beda: di situ cuma ada satu",
                    "variabel yang sama untuk seluruh perulangan, jadi semua lambda membaca",
                    "nilai terakhirnya.",
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
                    "Lihat apa yang terjadi di Saring. Method itu sama sekali nggak tahu",
                    "syarat apa yang lagi diuji. Dia cuma memanggil `syarat(n)`. Keputusan",
                    "\"mana yang lolos\" sepenuhnya ada di tangan pemanggil. Itu inti",
                    "pemrograman fungsional: yang dikirim ke method nggak cuma data, tapi",
                    "juga perilaku.",
                    "",
                    "Saring dan Ubah di atas melakukan persis hal yang dilakukan LINQ lewat",
                    "Where dan Select. Kalau kamu udah pernah nulis versinya sendiri, LINQ",
                    "jadi gampang dipahami.",
                    "",
                    "Event itu delegate yang dipagari. Dari luar class, event cuma boleh",
                    "ditambah (+=) dan dikurangi (-=). Event nggak boleh diisi ulang pakai",
                    "(=), dan nggak boleh dipanggil dari luar.",
                    "",
                    "  public event Action<string>? Berubah;",
                    "  ...",
                    "  Berubah?.Invoke(\"nilai baru\");   dipanggil dari DALAM",
                    "",
                    "Pagar itu ada untuk mencegah kejadian ini: satu baris",
                    "`obj.Berubah = ...` di tempat lain menghapus semua pendengar yang udah",
                    "terdaftar. Pendengar itu method yang minta dikabari waktu event",
                    "terjadi. Kalau mereka terhapus, notifikasinya berhenti, dan susah",
                    "dicari penyebabnya.",
                    "",
                    "`?.Invoke` juga ada alasannya. Kalau belum ada pendengar sama sekali,",
                    "event bernilai null, dan memanggilnya langsung melempar",
                    "NullReferenceException.",
                ]
            },
        ],
    },
    {
        "title": "20. LINQ: Bertanya pada Data",
        "sections": [
            {
                "body": [
                    "LINQ (Language Integrated Query) itu sekumpulan method untuk",
                    "menyaring, mengubah, mengelompokkan, dan meringkas isi koleksi.",
                    "Sintaksnya sama, apa pun sumbernya: List, array, berkas, atau",
                    "database.",
                    "",
                    "  using System.Linq;    wajib",
                    "",
                    "Ada dua cara nulis, dan hasilnya sama persis:",
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
                    "Method syntax lebih sering dipakai, karena nggak semua method punya",
                    "kata kunci padanannya. Count, Any, dan Sum tetap harus ditulis sebagai",
                    "method.",
                    "",
                    "Operator untuk menyaring dan mengubah:",
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
                    "Operator yang menghasilkan satu nilai:",
                    "  Count() / Sum() / Average() / Min() / Max()",
                    "  Any(p)            adakah yang cocok?",
                    "  All(p)            apakah SEMUA cocok?",
                    "  First(p)          yang pertama; MELEMPAR kalau tidak ada",
                    "  FirstOrDefault(p) yang pertama; null/0 kalau tidak ada",
                    "  Single(p)         tepat satu; melempar kalau 0 atau >1",
                    "  Aggregate(f)      lipat jadi satu nilai",
                    "",
                    "Pasangan First dan FirstOrDefault ada di banyak method, dan kamu yang",
                    "harus memilih. Pakai yang melempar kalau \"nggak ada\" berarti ada bug.",
                    "Pakai versi OrDefault kalau \"nggak ada\" itu hasil yang wajar.",
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
                    "GroupBy menghasilkan deretan IGrouping<TKey, TElement>. Tiap kelompok",
                    "itu koleksi yang juga punya properti .Key. Makanya g bisa di-Count(),",
                    "dan sekaligus bisa ditanya g.Key.",
                    "",
                    "Hal paling penting soal LINQ, dan yang paling sering menjebak:",
                    "deferred execution, artinya query baru dijalankan belakangan.",
                    "",
                    "  var q = data.Where(m => m.Nilai > 80);  BELUM jalan",
                    "  data.Add(new(\"Gita\", \"A\", 99));",
                    "  foreach (var m in q) ...                BARU jalan",
                    "",
                    "Gita ikut muncul di hasil, karena query baru dijalankan waktu",
                    "ditelusuri, bukan waktu ditulis. Kalau kamu mau hasilnya dibekukan",
                    "saat itu juga, panggil .ToList() atau .ToArray().",
                    "",
                    "Akibat keduanya lebih merugikan. Kalau query yang sama ditelusuri dua",
                    "kali, seluruh penyaringannya juga dijalankan dua kali. Kalau",
                    "sumbernya database, berarti dua kali bolak-balik ke server untuk",
                    "pertanyaan yang sama.",
                    "",
                    "Aturan praktisnya: kalau query udah selesai disusun dan hasilnya bakal",
                    "dipakai lebih dari sekali, panggil .ToList().",
                ]
            },
        ],
    },
    {
        "title": "21. Bekerja dengan Berkas",
        "sections": [
            {
                "body": [
                    "Semua yang dibahas di sini ada di namespace System.IO.",
                    "",
                    "Cara paling singkat, untuk berkas yang muat di memori:",
                    "",
                    "  File.WriteAllText(path, isi);",
                    "  File.AppendAllText(path, isi);",
                    "  string isi = File.ReadAllText(path);",
                    "  string[] baris = File.ReadAllLines(path);",
                    "  File.WriteAllLines(path, baris);",
                    "",
                    "path di sini maksudnya alamat berkas, misalnya \"data/murid.txt\".",
                    "",
                    "Untuk berkas besar, jangan pakai ReadAllLines. Method itu menarik",
                    "seluruh isi berkas ke memori sekaligus. Pakai ReadLines, yang membaca",
                    "baris demi baris sambil kamu telusuri:",
                    "",
                    "  foreach (string b in File.ReadLines(path)) ...",
                    "",
                    "Bedanya cuma kata All. Tapi untuk berkas 2 GB, bedanya antara program",
                    "yang jalan dan program yang kehabisan memori.",
                    "",
                    "Untuk ngecek dan mengelola berkas atau folder:",
                    "  File.Exists(path)          bool",
                    "  File.Delete(path)          diam saja kalau tidak ada",
                    "  File.Copy(a, b, true)      true = boleh menimpa",
                    "  File.Move(a, b)",
                    "  Directory.Exists(path)",
                    "  Directory.CreateDirectory(path)   aman kalau sudah ada",
                    "  Directory.GetFiles(path, \"*.txt\")",
                    "",
                    "Jangan pernah menyusun path dengan menyambung garis miring sendiri.",
                    "Pemisah folder beda-beda antar sistem operasi (Windows pakai \\, Linux",
                    "pakai /), dan Path.Combine tahu mana yang benar:",
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
                    "`(Nama: k[0], Kelas: k[1], Nilai: ...)` itu tuple bernama, yaitu",
                    "wadah data sekali pakai yang nggak perlu dibikinin class. Cocok untuk",
                    "situasi seperti ini, waktu bentuk datanya cuma dipakai di dalam satu",
                    "method.",
                    "",
                    "Jebakan: `Split(',')` cuma benar kalau di dalam datanya nggak ada",
                    "koma. CSV sungguhan boleh punya kolom seperti \"Jakarta, DKI\", dan",
                    "Split bakal memecahnya jadi dua. Untuk data sungguhan, pakai pustaka",
                    "CSV. Untuk latihan seperti ini, Split udah cukup, asal kamu tahu",
                    "batasnya.",
                    "",
                    "Operasi berkas selalu bisa gagal karena hal di luar kendalimu: berkas",
                    "lagi dikunci program lain, izinnya ditolak, disk penuh, atau foldernya",
                    "nggak ada. Kode nyata membungkusnya dengan try-catch:",
                    "",
                    "  try { ... }",
                    "  catch (FileNotFoundException) { ... }",
                    "  catch (UnauthorizedAccessException) { ... }",
                    "  catch (IOException e) { ... }",
                    "",
                    "Urutan catch-nya penting. FileNotFoundException itu turunan",
                    "IOException. Kalau IOException ditulis lebih dulu, dia ikut menangkap",
                    "FileNotFoundException, dan catch yang khusus nggak pernah kepakai.",
                ]
            },
        ],
    },
    {
        "title": "22. IDisposable & using",
        "sections": [
            {
                "body": [
                    "Garbage collector cuma mengurus memori. Dia nggak tahu apa-apa soal",
                    "berkas yang masih terbuka, koneksi database yang masih dipegang, atau",
                    "soket jaringan. Sumber daya seperti itu harus kamu lepas sendiri",
                    "secara eksplisit.",
                    "",
                    "Objek yang memegang sumber daya begitu mengimplementasikan",
                    "IDisposable. Interface ini isinya cuma satu method: Dispose(), yang",
                    "tugasnya melepas sumber daya tadi.",
                    "",
                    "Kalau ditulis manual, bentuknya begini:",
                    "",
                    "  StreamReader r = new StreamReader(path);",
                    "  try { ... }",
                    "  finally { r.Dispose(); }",
                    "",
                    "Blok finally selalu dijalankan, entah isi try berhasil atau gagal.",
                    "Pola ini dipakai di mana-mana, jadi C# ngasih kata kunci khusus",
                    "untuknya:",
                    "",
                    "  using (var r = new StreamReader(path))",
                    "  {",
                    "      ...",
                    "  }   // Dispose() dipanggil di sini, GAGAL ATAU TIDAK",
                    "",
                    "Sejak C# 8 ada bentuk tanpa kurawal, namanya using declaration.",
                    "Objeknya dilepas waktu scope-nya selesai, biasanya di akhir method:",
                    "",
                    "  using var r = new StreamReader(path);",
                    "  ... sampai akhir method",
                    "",
                    "Bentuk ini menghemat satu tingkat indentasi. Di method yang membuka",
                    "tiga berkas sekaligus, bedanya kerasa.",
                    "",
                    "Kapan kamu butuh using? Setiap kali sebuah tipe punya method Dispose.",
                    "Analyzer kode bisa ngingetin kamu lewat aturan CA2000. Yang paling",
                    "sering ketemu: StreamReader, StreamWriter, FileStream, HttpClient,",
                    "SqlConnection, Bitmap, CancellationTokenSource.",
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
                    "Ada dua aturan untuk Dispose, dan dua-duanya kelihatan di kode atas:",
                    "",
                    "  1. Dispose wajib aman dipanggil berkali-kali. Itu gunanya penjaga",
                    "     `if (_sudah) return;`. Tanpa penjaga itu, kalau kamu udah",
                    "     memanggil Dispose sendiri lalu `using` memanggilnya lagi,",
                    "     programnya error.",
                    "  2. Method lain harus menolak bekerja sesudah Dispose, dengan",
                    "     melempar ObjectDisposedException. Kalau dibiarkan jalan, yang",
                    "     muncul nanti error dari dalam StreamWriter yang udah tertutup,",
                    "     dan itu jauh lebih membingungkan.",
                    "",
                    "`using` bekerja lewat try/finally, jadi Dispose tetap dipanggil",
                    "walaupun blok di dalamnya melempar exception. Memang itu alasan",
                    "`using` ada. Tanpa `using`, satu exception di tengah jalan bikin",
                    "berkasnya nggak pernah ditutup, dan berkas itu terkunci sampai",
                    "programnya mati.",
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
                    "async dan await dipakai untuk operasi yang kerjanya menunggu: membaca",
                    "berkas besar, memanggil API, atau query ke database. Selama menunggu,",
                    "thread-nya dilepas supaya bisa mengerjakan hal lain, daripada diam",
                    "nungguin jawaban. Thread itu jalur kerja di dalam program; satu thread",
                    "mengerjakan satu hal dalam satu waktu.",
                    "",
                    "Dari awal, luruskan dulu satu salah paham. async nggak bikin sesuatu",
                    "jalan lebih cepat, dan juga nggak bikin thread baru. Gunanya supaya",
                    "thread yang lagi nunggu jawaban dari luar nggak terbuang percuma.",
                    "",
                    "Kata kunci dan tipe yang perlu kamu kenal:",
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
                    "Aturan yang wajib kamu ikuti:",
                    "  1. Method async mengembalikan Task, Task<T>, atau ValueTask.",
                    "     Jangan pakai `async void`, kecuali untuk event handler UI.",
                    "     Exception di dalam async void nggak bisa ditangkap oleh",
                    "     pemanggilnya, dan langsung menjatuhkan seluruh proses.",
                    "  2. Nama method async diakhiri Async. Ini konvensi .NET, dan",
                    "     seluruh pustaka standar mengikutinya.",
                    "  3. Jangan pakai `.Result` atau `.Wait()` pada Task. Dua-duanya",
                    "     memblokir thread. Di aplikasi UI atau ASP.NET lama, ini bikin",
                    "     deadlock, yaitu program macet karena saling tunggu: thread yang",
                    "     sedang menunggu justru thread yang dibutuhkan untuk",
                    "     menyelesaikan tugasnya. Penyebabnya susah sekali dicari.",
                    "  4. async menular ke atas. Kalau sebuah method memanggil method",
                    "     async, method itu sebaiknya ikut async, terus sampai ke Main.",
                    "     Sejak C# 7.1, `static async Task Main()` itu sah.",
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
                    "Ini kesalahan async yang paling sering dan paling mahal: nulis `await`",
                    "di setiap baris, sehingga panggilan yang mestinya bisa jalan",
                    "bareng malah antre satu-satu. Lima panggilan API yang masing-masing",
                    "200 ms jadi makan 1 detik, padahal bisa selesai dalam 200 ms.",
                    "",
                    "Caranya: mulai dulu semua task-nya tanpa await, baru tunggu",
                    "bareng-bareng pakai Task.WhenAll.",
                    "",
                    "Method Task yang sering berguna:",
                    "  Task.Delay(ms)          menunggu tanpa memblokir",
                    "  Task.WhenAll(tasks)     tunggu SEMUA selesai",
                    "  Task.WhenAny(tasks)     tunggu yang PERTAMA selesai",
                    "  Task.Run(() => ...)     jalankan kerja BERAT di thread",
                    "                          pool -- ini yang memindahkan",
                    "                          kerja ke thread lain",
                    "  Task.FromResult(x)      Task yang sudah selesai",
                    "",
                    "Jangan pakai Thread.Sleep di dalam method async. Task.Delay melepas",
                    "thread selama menunggu, sedangkan Thread.Sleep menahannya. Kalau",
                    "Thread.Sleep dipakai di method async, manfaat async-nya hilang.",
                    "",
                    "Untuk membatalkan operasi, pakai CancellationToken:",
                    "  var cts = new CancellationTokenSource(",
                    "      TimeSpan.FromSeconds(5));",
                    "  await KerjaAsync(cts.Token);",
                    "",
                    "Token itu dikirim terus ke method-method di bawahnya, dan dicek",
                    "secara berkala. Operasi yang nggak bisa dibatalkan suatu hari bisa",
                    "bikin aplikasimu menggantung, dan nggak ada cara menghentikannya",
                    "selain mematikan programnya.",
                ]
            },
        ],
    },
    {
        "title": "24. Namespace, Assembly & Struktur Proyek",
        "sections": [
            {
                "body": [
                    "Namespace mengelompokkan tipe supaya namanya nggak bentrok. Misalnya",
                    "dua pustaka sama-sama punya class Produk; namespace yang membedakan",
                    "keduanya. Namespace cuma urusan penamaan, dan nggak berpengaruh apa-apa",
                    "waktu program jalan.",
                    "",
                    "  namespace Toko.Domain;      file-scoped, C# 10",
                    "",
                    "  class Produk { }            jadi Toko.Domain.Produk",
                    "",
                    "Bentuk lama memakai kurawal, dan bikin seluruh isi berkas menjorok",
                    "satu tingkat:",
                    "",
                    "  namespace Toko.Domain",
                    "  {",
                    "      class Produk { }",
                    "  }",
                    "",
                    "Kebiasaannya, namespace mengikuti struktur folder. Berkas",
                    "Toko/Domain/Produk.cs berisi Toko.Domain.Produk.",
                    "",
                    "using dipakai untuk mengimpor namespace, supaya nama di dalamnya bisa",
                    "dipakai tanpa ditulis lengkap:",
                    "  using System.Collections.Generic;",
                    "  using Dict = System.Collections.Generic.Dictionary<string, int>;",
                    "  global using System;           berlaku SEKALI untuk",
                    "                                 seluruh proyek (C# 10)",
                    "  using static System.Math;      pakai Sqrt(x), bukan Math.Sqrt(x)",
                    "",
                    "Setelan ImplicitUsings di berkas .csproj menyalakan sekumpulan global",
                    "using bawaan, misalnya System, System.Linq, System.IO, dan beberapa",
                    "lagi. Makanya proyek baru di .NET 6 ke atas sering nggak punya satu",
                    "pun baris using di bagian atas berkasnya.",
                    "",
                    "Assembly itu hasil kompilasi, berupa satu berkas .dll atau .exe. Satu",
                    "proyek menghasilkan satu assembly. Hati-hati, modifier `internal`",
                    "berlaku di batas assembly, bukan di batas namespace. Dua hal ini",
                    "sering ketuker. Kode yang ditandai internal bisa dipakai di mana aja",
                    "dalam assembly yang sama, apa pun namespace-nya.",
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
                    "Keputusan arsitektur yang paling berpengaruh adalah arah",
                    "ketergantungan, yaitu proyek mana yang boleh memakai proyek mana. Arah",
                    "ini dijaga lewat berkas proyek:",
                    "",
                    "  Toko.App  ->  Toko.Data  ->  Toko.Domain",
                    "",
                    "Domain nggak boleh tahu apa-apa soal database ataupun tampilan. Kalau",
                    "panahnya pernah dibalik, misalnya Domain mereferensi Data, aturan",
                    "bisnisnya jadi nggak bisa dites tanpa database, dan nggak bisa dipakai",
                    "ulang di aplikasi lain. Untungnya, `dotnet add reference` menolak",
                    "membuat lingkaran, jadi pelanggaran yang paling parah ketahuan",
                    "otomatis.",
                    "",
                    "Berkas .csproj modern pendek, biasanya kurang dari sepuluh baris.",
                    "Kalau kamu ketemu berkas proyek sepanjang ratusan baris yang",
                    "mencantumkan setiap berkas .cs satu per satu, itu format .NET",
                    "Framework yang lama.",
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
