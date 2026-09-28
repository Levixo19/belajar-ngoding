VB_MATERIALS = [
    {
        "title": "1. Pengenalan Visual Basic .NET",
        "sections": [
            {
                "body": [
                    "SATU HAL YANG HARUS JELAS SEJAK AWAL, karena ia sumber",
                    "kebingungan terbesar: ada TIGA hal berbeda yang",
                    "sama-sama disebut 'Visual Basic'.",
                    "",
                    "  VB6 (1998)      Bahasa lama untuk aplikasi Windows.",
                    "                  SUDAH TIDAK DIDUKUNG. Kode VB6 TIDAK",
                    "                  jalan di VB.NET tanpa ditulis ulang.",
                    "  VBA             Visual Basic for Applications, yang ada",
                    "                  di dalam Excel dan Word. Turunan VB6,",
                    "                  bukan VB.NET.",
                    "  VB.NET (2002)   Bahasa modern di atas platform .NET.",
                    "                  INILAH yang dipelajari di sini.",
                    "",
                    "Kalau sebuah tutorial memakai `Set obj = New ...`,",
                    "`Variant`, atau `On Error Goto`, itu VB6 atau VBA.",
                    "",
                    "VB.NET adalah SAUDARA C#. Keduanya berjalan di runtime",
                    "yang sama, memakai pustaka yang sama, dan menghasilkan",
                    "IL yang hampir identik. Yang berbeda cuma sintaksnya:",
                    "",
                    "  C#              VB.NET",
                    "  int x = 5;      Dim x As Integer = 5",
                    "  { }             Sub ... End Sub",
                    "  //              '",
                    "  ==              =",
                    "  &&  ||          AndAlso  OrElse",
                    "  null            Nothing",
                    "",
                    "Karena keduanya setara, pustaka .NET apa pun bisa",
                    "dipakai dari VB.NET — dan sebaliknya, class VB.NET bisa",
                    "dipakai dari C#.",
                    "",
                    "STATUSNYA HARI INI, dan ini layak diketahui sebelum kamu",
                    "menginvestasikan waktu: Microsoft menyatakan VB.NET",
                    "sebagai bahasa yang STABIL, bukan yang berkembang.",
                    "Fitur bahasa baru diarahkan ke C# dan F#; VB.NET tetap",
                    "didukung penuh tapi tidak lagi menerima fitur besar.",
                    "",
                    "Artinya VB.NET tetap masuk akal untuk:",
                    "  - Merawat aplikasi bisnis yang sudah ada.",
                    "  - Tim yang seluruhnya sudah terbiasa dengannya.",
                    "  - Belajar konsep .NET dengan sintaks yang terbaca.",
                    "",
                    "Dan kurang masuk akal untuk proyek baru yang besar, di",
                    "mana C# akan lebih mudah mencari contoh dan orang.",
                    "",
                    "Instalasi:",
                    "  - Fedora  : sudo dnf install dotnet-sdk-8.0",
                    "  - Windows : Visual Studio, atau .NET SDK saja",
                    "  - Cek     : dotnet --version",
                    "",
                    "Menjalankan:",
                    "  dotnet new console -lang VB -o latihan",
                    "  cd latihan && dotnet run",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """Imports System

Module Program

    Sub Main()
        Console.WriteLine("Halo Dunia!")
        Console.WriteLine("Aku sedang belajar Visual Basic .NET.")

        Dim nama As String = "Andi"
        Dim umur As Integer = 20

        Console.WriteLine($"Halo, {nama}! Umurmu {umur} tahun.")
        Console.WriteLine("Sambung pakai & : " & nama & ", " & umur.ToString())
    End Sub

End Module"""
            },
            {
                "body": [
                    "Penjelasan tiap bagian:",
                    "",
                    "  Imports System",
                    "    Memuat namespace System supaya `Console` bisa ditulis",
                    "    tanpa awalan. Padanan `using` di C#.",
                    "",
                    "  Module Program",
                    "    MODULE adalah wadah untuk kode yang tidak butuh objek.",
                    "    Seluruh isinya otomatis Shared (statis). Padanannya",
                    "    di C# adalah class statis.",
                    "",
                    "  Sub Main()",
                    "    Titik masuk program. SUB adalah prosedur yang TIDAK",
                    "    mengembalikan nilai; yang mengembalikan nilai disebut",
                    "    FUNCTION.",
                    "",
                    "  End Sub / End Module",
                    "    VB menutup blok dengan kata, bukan kurung kurawal.",
                    "",
                    "Aturan penting VB:",
                    "  1. TIDAK ADA titik koma di akhir baris.",
                    "  2. TIDAK MEMBEDAKAN huruf besar-kecil. `Console` dan",
                    "     `CONSOLE` sama. Editor akan merapikannya otomatis",
                    "     ke bentuk baku.",
                    "  3. Satu pernyataan satu baris. Untuk memecah baris",
                    "     panjang, akhiri dengan spasi lalu garis bawah.",
                    "     (Sejak VB 2010, sebagian besar kasus sudah bisa",
                    "     dipecah tanpa garis bawah.)",
                    "  4. Komentar memakai kutip tunggal.",
                    "  5. Nama memakai PascalCase untuk semuanya kecuali",
                    "     variabel lokal dan parameter, yang memakai camelCase.",
                    "",
                    "MENYAMBUNG TEKS memakai `&`, BUKAN `+`. Tanda plus juga",
                    "bekerja untuk string, tapi ia AMBIGU: kalau salah satu",
                    "sisinya angka, VB akan mencoba menjumlahkannya. Selalu",
                    "pakai `&` untuk teks.",
                    "",
                    "String interpolation `$\"...{x}...\"` tersedia sejak",
                    "VB 2015 dan lebih terbaca daripada rantai `&`.",
                ]
            },
        ],
    },
    {
        "title": "2. Option Strict & Tipe Data",
        "sections": [
            {
                "body": [
                    "TIGA SAKLAR di kepala berkas yang menentukan seberapa",
                    "ketat VB memeriksa kodemu. Yang pertama jauh lebih",
                    "penting daripada dua lainnya.",
                    "",
                    "  Option Strict On      TOLAK konversi tipe diam-diam",
                    "  Option Explicit On    WAJIB deklarasikan variabel",
                    "  Option Infer On       boleh simpulkan tipe dari nilai",
                    "",
                    "OPTION STRICT ON WAJIB DINYALAKAN, dan alasannya bisa",
                    "dilihat langsung:",
                    "",
                    "  Dim n As Integer = \"7\"",
                    "",
                    "  Strict Off  -> diterima, n bernilai 7",
                    "  Strict On   -> ERROR kompilasi",
                    "",
                    "Dengan Strict Off, `\"abc\"` juga akan diterima dan baru",
                    "meledak saat program jalan. Seluruh gunanya bahasa",
                    "bertipe hilang.",
                    "",
                    "Di berkas: `Option Strict On` di baris pertama.",
                    "Di proyek: `<OptionStrict>On</OptionStrict>` di .vbproj.",
                    "Yang di berkas menang atas yang di proyek.",
                    "",
                    "Tipe bilangan bulat:",
                    "  SByte    -128 .. 127                1 byte",
                    "  Byte     0 .. 255                   1 byte",
                    "  Short    -32.768 .. 32.767          2 byte",
                    "  Integer  -2,1 miliar .. 2,1 miliar  4 byte  <- bawaan",
                    "  Long     sangat besar               8 byte",
                    "",
                    "PERHATIKAN: `Integer` di VB.NET adalah 32 bit. Di VB6 ia",
                    "16 bit, dan `Long` yang 32 bit — sumber kebingungan bagi",
                    "yang pindah dari VB6.",
                    "",
                    "Tipe pecahan:",
                    "  Single   ~7 digit presisi     ditulis 3.14F",
                    "  Double   ~15 digit presisi    ditulis 3.14   <- bawaan",
                    "  Decimal  ~28 digit presisi    ditulis 3.14D",
                    "",
                    "Aturannya satu kalimat: UANG memakai Decimal, sisanya",
                    "Double. Double menyimpan pecahan dalam basis dua,",
                    "sehingga 0.1 tidak pernah tersimpan persis.",
                    "",
                    "Tipe lain:",
                    "  Boolean  True / False",
                    "  Char     satu karakter, ditulis \"A\"c",
                    "  String   teks",
                    "  Date     tanggal dan waktu, ditulis #2026-09-22#",
                    "  Object   apa pun; hindari kecuali terpaksa",
                    "",
                    "KONVERSI, dan VB punya tiga keluarga:",
                    "  CInt(x)  CDbl(x)  CStr(x)  CDec(x)  CBool(x)",
                    "  CType(x, Integer)",
                    "  Integer.Parse(s)         melempar kalau gagal",
                    "  Integer.TryParse(s, n)   mengembalikan Boolean",
                    "",
                    "Untuk masukan pengguna, TryParse hampir selalu benar.",
                ]
            },
            {
                "heading": "Tipe, batas, dan konversi",
                "code": """Option Strict On

Imports System
Imports System.Globalization

Module Program

    Sub Main()
        Dim umur As Integer = 20
        Dim tinggi As Double = 172.5
        Dim harga As Decimal = 25000D
        Dim aktif As Boolean = True
        Dim huruf As Char = "V"c

        Console.WriteLine($"Integer : {Integer.MinValue} .. {Integer.MaxValue}")
        Console.WriteLine($"Byte    : {Byte.MinValue} .. {Byte.MaxValue}")
        Console.WriteLine($"nilai   : {umur} {tinggi} {harga} {aktif} {huruf}")

        ' Konversi WAJIB ditulis karena Option Strict On
        Dim sebagaiDouble As Double = CDbl(umur)
        Dim sebagaiTeks As String = CStr(umur)
        Console.WriteLine($"konversi: {sebagaiDouble} '{sebagaiTeks}'")

        ' Pembagian: VB punya DUA operator
        Console.WriteLine($"7 / 2   = {7 / 2}")
        Console.WriteLine($"7 \\ 2   = {7 \\ 2}")
        Console.WriteLine($"7 Mod 2 = {7 Mod 2}")
        Console.WriteLine($"2 ^ 10  = {2 ^ 10}")

        ' Decimal tidak kehilangan presisi, Double bisa
        Console.WriteLine($"0.1 + 0.2 = 0.3 (Double) : {0.1 + 0.2 = 0.3}")
        Console.WriteLine($"0.1 + 0.2 = 0.3 (Decimal): {0.1D + 0.2D = 0.3D}")

        ' TryParse: tidak melempar
        For Each teks As String In New String() {"42", "3.5", "abc", ""}
            Dim n As Integer
            Dim berhasil As Boolean = Integer.TryParse(teks, n)
            Console.WriteLine($"TryParse(""{teks}"") = {berhasil}, hasil {n}")
        Next
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Integer : -2147483648 .. 2147483647",
                    "  Byte    : 0 .. 255",
                    "  nilai   : 20 172.5 25000 True V",
                    "  konversi: 20 '20'",
                    "  7 / 2   = 3.5",
                    "  7 \\ 2   = 3",
                    "  7 Mod 2 = 1",
                    "  2 ^ 10  = 1024",
                    "  0.1 + 0.2 = 0.3 (Double) : False",
                    "  0.1 + 0.2 = 0.3 (Decimal): True",
                    "  TryParse(\"42\") = True, hasil 42",
                    "  TryParse(\"3.5\") = False, hasil 0",
                    "  TryParse(\"abc\") = False, hasil 0",
                    "  TryParse(\"\") = False, hasil 0",
                    "",
                    "DUA OPERATOR PEMBAGIAN adalah hal yang tidak ada di C#",
                    "dan sangat berguna:",
                    "",
                    "  /   pembagian PECAHAN, selalu menghasilkan Double",
                    "  \\   pembagian BULAT, sisanya dibuang",
                    "",
                    "Jadi `7 / 2` memberi 3.5 sementara `7 \\ 2` memberi 3.",
                    "Tidak ada kejutan 'kenapa hasilnya bulat' seperti di C,",
                    "Java, atau C# — kamu memilihnya secara eksplisit.",
                    "",
                    "`^` adalah operator PANGKAT, juga tidak ada di C#.",
                    "",
                    "Perhatikan `0.1 + 0.2 = 0.3` memakai SATU tanda sama",
                    "dengan. Di VB, `=` berperan ganda: penugasan di awal",
                    "pernyataan, dan PERBANDINGAN di dalam ekspresi. Tidak ada",
                    "`==` sama sekali.",
                    "",
                    "Ini kebalikan dari jebakan C: di sana `if (x = 5)` adalah",
                    "penugasan yang tidak disengaja. Di VB itu mustahil,",
                    "karena penugasan tidak bisa muncul di dalam ekspresi.",
                ]
            },
        ],
    },
    {
        "title": "3. Operator & Perbandingan",
        "sections": [
            {
                "body": [
                    "Aritmetika:",
                    "  +    tambah",
                    "  -    kurang",
                    "  *    kali",
                    "  /    bagi PECAHAN, hasilnya Double",
                    "  \\    bagi BULAT, sisanya dibuang",
                    "  Mod  sisa bagi",
                    "  ^    pangkat",
                    "",
                    "Penugasan gabungan: += -= *= /= \\= ^= &=",
                    "",
                    "VB TIDAK PUNYA `++` dan `--`. Tulis `i += 1`.",
                    "",
                    "PENYAMBUNG TEKS:",
                    "  &    SELALU menyambung sebagai teks",
                    "  +    ambigu; hindari untuk teks",
                    "",
                    "  \"1\" & 2     -> \"12\"",
                    "  \"1\" + 2     -> dengan Option Strict On: ERROR",
                    "",
                    "Perbandingan:",
                    "  =    sama dengan   (bukan ==)",
                    "  <>   tidak sama    (bukan !=)",
                    "  <  >  <=  >=",
                    "  Is / IsNot         perbandingan REFERENSI",
                    "  Like               pencocokan pola sederhana",
                    "",
                    "`Is` dan `IsNot` dipakai untuk objek dan Nothing:",
                    "  If obj Is Nothing Then",
                    "  If obj IsNot Nothing Then",
                    "",
                    "JANGAN menulis `If obj = Nothing`. Untuk tipe referensi",
                    "itu memanggil operator kesetaraan yang mungkin tidak ada,",
                    "dan untuk tipe nilai artinya berbeda sama sekali.",
                    "",
                    "OPERATOR LOGIKA, dan inilah bagian paling penting di",
                    "materi ini:",
                    "",
                    "  AndAlso   DAN, dengan HUBUNG-SINGKAT",
                    "  OrElse    ATAU, dengan hubung-singkat",
                    "  And       DAN, TANPA hubung-singkat",
                    "  Or        ATAU, tanpa hubung-singkat",
                    "  Not       negasi",
                    "  Xor       salah satu, tapi tidak keduanya",
                    "",
                    "PAKAI AndAlso dan OrElse, HAMPIR SELALU. Tanpa",
                    "hubung-singkat, sisi kanan tetap dievaluasi meski",
                    "hasilnya sudah pasti:",
                    "",
                    "  If nama IsNot Nothing And nama.Length > 0 Then",
                    "      ' MELEDAK kalau nama Nothing: sisi kanan tetap jalan",
                    "",
                    "  If nama IsNot Nothing AndAlso nama.Length > 0 Then",
                    "      ' aman",
                    "",
                    "`And` dan `Or` tetap ada karena keduanya juga berperan",
                    "sebagai operator BIT pada bilangan. Untuk kondisi",
                    "logika, hampir tidak pernah yang kamu maksud.",
                    "",
                    "Operator lain:",
                    "  If(a, b)          pakai a kalau bukan Nothing",
                    "  If(syarat, a, b)  ternary",
                    "  ?.  ?()           null-conditional",
                    "  TypeOf x Is T     periksa tipe",
                    "  AddressOf f       referensi ke prosedur",
                ]
            },
            {
                "heading": "Operator yang khas VB",
                "code": """Option Strict On

Imports System

Module Program

    Sub Main()
        ' --- Dua pembagian ---
        Console.WriteLine($"17 / 5   = {17 / 5}")
        Console.WriteLine($"17 \\ 5   = {17 \\ 5}")
        Console.WriteLine($"17 Mod 5 = {17 Mod 5}")
        Console.WriteLine($"2 ^ 8    = {2 ^ 8}")

        Console.WriteLine("---")

        ' --- Penyambung teks ---
        Dim nama As String = "Andi"
        Dim umur As Integer = 20
        Console.WriteLine("dengan & : " & nama & " (" & umur.ToString() & ")")
        Console.WriteLine($"interpol : {nama} ({umur})")

        Console.WriteLine("---")

        ' --- Is / IsNot untuk objek dan Nothing ---
        Dim kosong As String = Nothing
        Dim isi As String = "ada"
        Console.WriteLine($"kosong Is Nothing    : {kosong Is Nothing}")
        Console.WriteLine($"isi IsNot Nothing    : {isi IsNot Nothing}")

        Console.WriteLine("---")

        ' --- AndAlso menyelamatkan, And tidak ---
        Console.WriteLine($"aman   : {kosong IsNot Nothing AndAlso kosong.Length > 0}")
        Try
            ' Tanpa hubung-singkat, sisi kanan TETAP dievaluasi
            Console.WriteLine(kosong IsNot Nothing And kosong.Length > 0)
        Catch ex As NullReferenceException
            Console.WriteLine("bahaya : And tanpa hubung-singkat -> NullReferenceException")
        End Try

        Console.WriteLine("---")

        ' --- If() sebagai ternary dan sebagai pengganti Nothing ---
        Dim nilai As Integer = 78
        Console.WriteLine($"ternary  : {If(nilai >= 75, "Lulus", "Ulang")}")
        Console.WriteLine($"cadangan : {If(kosong, "(tidak diisi)")}")

        Console.WriteLine("---")

        ' --- Like: pencocokan pola sederhana ---
        For Each teks As String In New String() {"B01", "B123", "X01", "b01"}
            Console.WriteLine($"{teks,-6} Like ""B##"" -> {teks Like "B##"}")
        Next
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  17 / 5   = 3.4",
                    "  17 \\ 5   = 3",
                    "  17 Mod 5 = 2",
                    "  2 ^ 8    = 256",
                    "  ---",
                    "  dengan & : Andi (20)",
                    "  interpol : Andi (20)",
                    "  ---",
                    "  kosong Is Nothing    : True",
                    "  isi IsNot Nothing    : True",
                    "  ---",
                    "  aman   : False",
                    "  bahaya : And tanpa hubung-singkat -> NullReferenceException",
                    "  ---",
                    "  ternary  : Lulus",
                    "  cadangan : (tidak diisi)",
                    "  ---",
                    "  B01    Like \"B##\" -> True",
                    "  B123   Like \"B##\" -> False",
                    "  X01    Like \"B##\" -> False",
                    "  b01    Like \"B##\" -> False",
                    "",
                    "Blok AndAlso versus And adalah pelajaran terpentingnya.",
                    "Keduanya terlihat setara dan berperilaku sama di hampir",
                    "semua kasus — sampai sisi kirinya salah, dan yang satu",
                    "meledak sementara yang lain tidak.",
                    "",
                    "`Like` memakai pola sederhana, bukan regex:",
                    "  ?        satu karakter apa pun",
                    "  *        berapa pun karakter",
                    "  #        satu ANGKA",
                    "  [a-z]    satu karakter dari rentang",
                    "  [!a-z]   satu karakter DI LUAR rentang",
                    "",
                    "Dengan `Option Compare Binary` (bawaan), `Like`",
                    "membedakan huruf besar-kecil — itu sebabnya \"b01\" tidak",
                    "cocok. `Option Compare Text` mengubahnya.",
                    "",
                    "Untuk pola yang lebih rumit, pakai",
                    "`System.Text.RegularExpressions.Regex` yang sama persis",
                    "dengan yang dipakai C#.",
                ]
            },
        ],
    },
    {
        "title": "4. Percabangan: If & Select Case",
        "sections": [
            {
                "body": [
                    "  If nilai >= 75 Then",
                    "      Console.WriteLine(\"Lulus\")",
                    "  ElseIf nilai >= 60 Then",
                    "      Console.WriteLine(\"Mengulang\")",
                    "  Else",
                    "      Console.WriteLine(\"Tidak Lulus\")",
                    "  End If",
                    "",
                    "Perhatikan `ElseIf` SATU KATA. `Else If` dua kata juga",
                    "sah tapi memerlukan `End If` tambahan, dan itu hampir",
                    "selalu bukan yang kamu maksud.",
                    "",
                    "Bentuk SATU BARIS tanpa End If:",
                    "  If nilai >= 75 Then Console.WriteLine(\"Lulus\")",
                    "",
                    "Pakai hemat. Bentuk ini tidak bisa diberi ElseIf dan",
                    "gampang terlewat saat membaca cepat.",
                    "",
                    "SELECT CASE jauh lebih kuat daripada switch di C:",
                    "",
                    "  Select Case nilai",
                    "      Case 90 To 100",
                    "          grade = \"A\"",
                    "      Case 75, 80, 85",
                    "          grade = \"B\"",
                    "      Case Is >= 60",
                    "          grade = \"C\"",
                    "      Case Else",
                    "          grade = \"D\"",
                    "  End Select",
                    "",
                    "Tiga bentuk Case yang tidak ada di C#:",
                    "  Case 90 To 100      RENTANG",
                    "  Case 75, 80, 85     beberapa nilai",
                    "  Case Is >= 60       PERBANDINGAN",
                    "",
                    "TIDAK ADA fall-through sama sekali, jadi tidak ada",
                    "`Break` yang perlu diingat. Begitu satu Case cocok,",
                    "eksekusinya berhenti di situ.",
                    "",
                    "`Select Case True` adalah idiom untuk rantai kondisi:",
                    "",
                    "  Select Case True",
                    "      Case nilai >= 85 : grade = \"A\"",
                    "      Case nilai >= 75 : grade = \"B\"",
                    "      Case Else        : grade = \"C\"",
                    "  End Select",
                    "",
                    "Titik dua memisahkan dua pernyataan di satu baris.",
                    "",
                    "Kondisi di VB memakai Boolean. Tapi dengan Option Strict",
                    "Off, angka juga diterima — nol berarti False. Dengan",
                    "Strict On, kamu harus menulis perbandingannya.",
                ]
            },
            {
                "heading": "Select Case dan semua bentuknya",
                "code": """Option Strict On

Imports System

Module Program

    Function Grade(nilai As Integer) As String
        Select Case nilai
            Case Is >= 85
                Return "A"
            Case 75 To 84
                Return "B"
            Case 60 To 74
                Return "C"
            Case 40 To 59
                Return "D"
            Case Else
                Return "E"
        End Select
    End Function

    Function Jenis(hari As Integer) As String
        Select Case hari
            Case 1, 2, 3, 4, 5
                Return "hari kerja"
            Case 6, 7
                Return "akhir pekan"
            Case Else
                Return "bukan hari yang sah"
        End Select
    End Function

    Function Suhu(derajat As Integer) As String
        ' Select Case True: rantai kondisi bebas
        Select Case True
            Case derajat < 15 : Return "dingin"
            Case derajat < 25 : Return "nyaman"
            Case derajat < 33 : Return "panas"
            Case Else         : Return "sangat panas"
        End Select
    End Function

    Sub Main()
        For Each n As Integer In New Integer() {92, 78, 65, 45, 12}
            Console.WriteLine($"{n,3} -> {Grade(n)}")
        Next

        Console.WriteLine("---")
        For Each h As Integer In New Integer() {1, 6, 9}
            Console.WriteLine($"hari {h} -> {Jenis(h)}")
        Next

        Console.WriteLine("---")
        For Each d As Integer In New Integer() {10, 22, 31, 40}
            Console.WriteLine($"{d,3} derajat -> {Suhu(d)}")
        Next

        Console.WriteLine("---")
        ' If satu baris, dan If() sebagai ekspresi
        Dim nilai As Integer = 78
        If nilai >= 75 Then Console.WriteLine("lulus (If satu baris)")
        Console.WriteLine($"status: {If(nilai >= 75, "Lulus", "Tidak Lulus")}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "   92 -> A",
                    "   78 -> B",
                    "   65 -> C",
                    "   45 -> D",
                    "   12 -> E",
                    "  ---",
                    "  hari 1 -> hari kerja",
                    "  hari 6 -> akhir pekan",
                    "  hari 9 -> bukan hari yang sah",
                    "  ---",
                    "   10 derajat -> dingin",
                    "   22 derajat -> nyaman",
                    "   31 derajat -> panas",
                    "   40 derajat -> sangat panas",
                    "  ---",
                    "  lulus (If satu baris)",
                    "  status: Lulus",
                    "",
                    "`Case 75 To 84` adalah bentuk yang paling sering",
                    "berguna dan tidak ada padanannya di C# sebelum pattern",
                    "matching. Ia membuat tabel penilaian terbaca seperti",
                    "tabel sungguhan.",
                    "",
                    "Perhatikan `Function Grade(...) As String` memakai",
                    "`Return` untuk mengembalikan nilai. VB juga menerima",
                    "bentuk lama `Grade = \"A\"` (menugaskan ke nama fungsinya",
                    "sendiri), tapi itu warisan VB6 yang sebaiknya tidak",
                    "kamu pakai: ia tidak menghentikan fungsinya, sehingga",
                    "kode di bawahnya tetap jalan.",
                    "",
                    "`{n,3}` di dalam interpolasi meratakan ke kanan selebar",
                    "3. Untuk rata kiri, pakai angka negatif: `{n,-3}`.",
                    "Sintaks ini sama persis dengan C#.",
                ]
            },
        ],
    },
    {
        "title": "5. Perulangan",
        "sections": [
            {
                "body": [
                    "Empat bentuk perulangan:",
                    "",
                    "  For i As Integer = 1 To 5",
                    "      ...",
                    "  Next",
                    "",
                    "  For i As Integer = 10 To 1 Step -2",
                    "      ...",
                    "  Next",
                    "",
                    "  For Each x As String In daftar",
                    "      ...",
                    "  Next",
                    "",
                    "  While syarat",
                    "      ...",
                    "  End While",
                    "",
                    "  Do While syarat ... Loop",
                    "  Do Until syarat ... Loop",
                    "  Do ... Loop While syarat      jalan minimal sekali",
                    "  Do ... Loop Until syarat      jalan minimal sekali",
                    "",
                    "PERHATIKAN `For i = 1 To 5` menjalankan LIMA kali:",
                    "1, 2, 3, 4, 5. Batasnya INKLUSIF, berbeda dari",
                    "`for (i = 0; i < 5; i++)` di C yang eksklusif.",
                    "",
                    "Ini sumber kesalahan satu-lebih bagi yang pindah dari",
                    "bahasa berkurung kurawal. Untuk menelusuri array",
                    "berindeks 0, tulis `For i = 0 To a.Length - 1`.",
                    "",
                    "Mengendalikan perulangan:",
                    "  Exit For / Exit While / Exit Do",
                    "  Continue For / Continue While / Continue Do",
                    "  Exit Sub / Exit Function",
                    "",
                    "Berbeda dari C#, kata keluarnya MENYEBUT jenis blok yang",
                    "ditinggalkan. Itu membuat perulangan bersarang lebih",
                    "jelas dibaca, meski tetap tidak bisa keluar dari dua",
                    "tingkat sekaligus.",
                    "",
                    "Untuk keluar dari perulangan bersarang, pindahkan bagian",
                    "dalamnya ke sebuah Function lalu Return — hampir selalu",
                    "lebih terbaca daripada penanda Boolean.",
                    "",
                    "`For Each` TIDAK mengizinkan koleksinya diubah selama",
                    "penelusuran. Menambah atau menghapus melempar",
                    "InvalidOperationException saat program jalan.",
                ]
            },
            {
                "heading": "Semua bentuk perulangan",
                "code": """Option Strict On

Imports System

Module Program

    Sub Main()
        ' --- For dengan batas INKLUSIF ---
        Console.Write("1 To 5      : ")
        For i As Integer = 1 To 5
            Console.Write($"{i} ")
        Next
        Console.WriteLine()

        Console.Write("10 To 1 -2  : ")
        For i As Integer = 10 To 1 Step -2
            Console.Write($"{i} ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Tabel perkalian: For bersarang ---
        For b As Integer = 1 To 3
            For k As Integer = 1 To 5
                Console.Write($"{b * k,4}")
            Next
            Console.WriteLine()
        Next

        Console.WriteLine("---")

        ' --- For Each ---
        Dim nama() As String = {"Andi", "Budi", "Cici"}
        For Each n As String In nama
            Console.Write($"{n} ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Do Until dan Exit Do ---
        Dim sisa As Integer = 27
        Dim langkah As Integer = 0
        Do Until sisa = 1
            sisa = If(sisa Mod 2 = 0, sisa \\ 2, 3 * sisa + 1)
            langkah += 1
            If langkah > 1000 Then Exit Do
        Loop
        Console.WriteLine($"27 sampai 1 dalam {langkah} langkah")

        Console.WriteLine("---")

        ' --- Continue For: melewati sebagian ---
        Console.Write("ganjil 1-10 : ")
        For i As Integer = 1 To 10
            If i Mod 2 = 0 Then Continue For
            Console.Write($"{i} ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Keluar dari dua perulangan lewat Function ---
        Dim hasil = CariFaktor(143)
        Console.WriteLine($"143 = {hasil.Item1} x {hasil.Item2}")
    End Sub

    Function CariFaktor(n As Integer) As Tuple(Of Integer, Integer)
        For i As Integer = 2 To n
            For j As Integer = i To n
                If i * j = n Then Return Tuple.Create(i, j)
            Next
        Next
        Return Tuple.Create(1, n)
    End Function

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  1 To 5      : 1 2 3 4 5",
                    "  10 To 1 -2  : 10 8 6 4 2",
                    "  ---",
                    "     1   2   3   4   5",
                    "     2   4   6   8  10",
                    "     3   6   9  12  15",
                    "  ---",
                    "  Andi Budi Cici",
                    "  ---",
                    "  27 sampai 1 dalam 111 langkah",
                    "  ---",
                    "  ganjil 1-10 : 1 3 5 7 9",
                    "  ---",
                    "  143 = 11 x 13",
                    "",
                    "Fungsi `CariFaktor` menunjukkan pola yang benar untuk",
                    "keluar dari perulangan bersarang di VB: pindahkan ke",
                    "Function lalu `Return`. VB tidak punya label seperti Go",
                    "atau Kotlin, dan penanda Boolean yang diperiksa di dua",
                    "tempat jauh lebih mudah salah.",
                    "",
                    "`Tuple.Create(a, b)` mengembalikan dua nilai sekaligus.",
                    "VB juga mendukung TUPLE BERNAMA sejak VB 15:",
                    "",
                    "  Function Bagi(a As Integer, b As Integer) _",
                    "      As (hasil As Integer, sisa As Integer)",
                    "      Return (a \\ b, a Mod b)",
                    "  End Function",
                    "",
                    "  Dim r = Bagi(17, 5)",
                    "  Console.WriteLine(r.hasil & \" sisa \" & r.sisa)",
                    "",
                    "Bentuk itu jauh lebih terbaca daripada `Item1` dan",
                    "`Item2`, dan layak dipakai untuk kode baru.",
                    "",
                    "Perhatikan juga garis bawah di ujung baris: itulah cara",
                    "memecah satu pernyataan panjang jadi beberapa baris di",
                    "VB. Sejak VB 2010 ia jarang diperlukan, tapi di deklarasi",
                    "seperti di atas ia masih wajib.",
                ]
            },
        ],
    },
    {
        "title": "6. Array & Koleksi",
        "sections": [
            {
                "body": [
                    "ARRAY di VB punya satu kejutan besar yang wajib",
                    "diketahui sejak awal:",
                    "",
                    "  Dim a(4) As Integer",
                    "",
                    "Baris itu membuat array berisi LIMA elemen, berindeks 0",
                    "sampai 4. Angka di dalam kurung adalah BATAS ATAS, bukan",
                    "jumlah elemen — warisan dari VB6.",
                    "",
                    "Ini berbeda dari hampir semua bahasa lain, dan ia sumber",
                    "kesalahan satu-lebih yang sangat sering.",
                    "",
                    "Bentuk lain yang lebih jelas:",
                    "  Dim a() As Integer = {10, 20, 30}",
                    "  Dim a As Integer() = New Integer() {10, 20, 30}",
                    "  Dim a = New Integer(4) {}        lima elemen, semua 0",
                    "",
                    "Mengakses dan mengukur:",
                    "  a(0)                elemen pertama; KURUNG BIASA,",
                    "                      bukan kurung siku",
                    "  a.Length            jumlah elemen",
                    "  UBound(a)           indeks tertinggi",
                    "  a(a.Length - 1)     elemen terakhir",
                    "",
                    "Kurung biasa untuk indeks berarti `a(0)` terlihat sama",
                    "dengan pemanggilan fungsi. Itu disengaja di VB, dan",
                    "kadang membingungkan saat membaca kode orang.",
                    "",
                    "Mengubah ukuran:",
                    "  ReDim a(9)                buat ulang, ISINYA HILANG",
                    "  ReDim Preserve a(9)       pertahankan isinya",
                    "",
                    "`ReDim Preserve` mahal: ia membuat array baru lalu",
                    "menyalin seluruh isinya. Kalau kamu sering menambah,",
                    "yang kamu butuhkan bukan array melainkan List.",
                    "",
                    "KOLEKSI GENERIK, dan inilah yang dipakai sehari-hari:",
                    "",
                    "  Imports System.Collections.Generic",
                    "",
                    "  Dim daftar As New List(Of String)",
                    "  daftar.Add(\"Andi\")",
                    "  daftar.Insert(0, \"Ani\")",
                    "  daftar.Remove(\"Andi\")",
                    "  daftar.RemoveAt(0)",
                    "  daftar.Count",
                    "  daftar.Contains(\"Andi\")",
                    "  daftar.Sort()",
                    "",
                    "  Dim umur As New Dictionary(Of String, Integer)",
                    "  umur(\"Andi\") = 20",
                    "  umur.TryGetValue(\"Andi\", n)",
                    "  umur.ContainsKey(\"Andi\")",
                    "",
                    "  Dim unik As New HashSet(Of Integer)",
                    "  Dim antre As New Queue(Of String)",
                    "  Dim tumpuk As New Stack(Of String)",
                    "",
                    "`(Of T)` adalah cara VB menulis generic; padanannya",
                    "`<T>` di C#.",
                ]
            },
            {
                "heading": "Array, List, dan Dictionary",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Linq

Module Program

    Sub Main()
        ' --- Array: angka dalam kurung adalah BATAS ATAS ---
        Dim kosong(4) As Integer
        Console.WriteLine($"Dim kosong(4) -> {kosong.Length} elemen, indeks 0..{UBound(kosong)}")

        Dim nilai() As Integer = {78, 92, 65, 88, 71, 95, 59, 83}
        Console.WriteLine($"Data      : {String.Join(", ", nilai)}")

        Dim urut() As Integer = CType(nilai.Clone(), Integer())
        Array.Sort(urut)
        Console.WriteLine($"Terurut   : {String.Join(", ", urut)}")

        Dim total As Integer = 0
        For Each n As Integer In nilai
            total += n
        Next
        Console.WriteLine($"Jumlah    : {nilai.Length}")
        Console.WriteLine($"Total     : {total}")
        Console.WriteLine($"Rata-rata : {CDbl(total) / nilai.Length:F2}")
        Console.WriteLine($"Tertinggi : {nilai.Max()}")
        Console.WriteLine($"Terendah  : {nilai.Min()}")

        Console.WriteLine("---")

        ' --- List(Of T) ---
        Dim nama As New List(Of String) From {"Budi", "Andi", "Cici"}
        nama.Add("Dedi")
        nama.Sort()
        Console.WriteLine($"List      : {String.Join(", ", nama)}")
        Console.WriteLine($"Count     : {nama.Count}")
        Console.WriteLine($"Ada Andi? : {nama.Contains("Andi")}")

        Console.WriteLine("---")

        ' --- Dictionary(Of K, V): menghitung frekuensi ---
        Dim kalimat As String = "kucing makan ikan kucing tidur ikan kucing"
        Dim hitung As New Dictionary(Of String, Integer)

        For Each kata As String In kalimat.Split(" "c)
            Dim n As Integer
            hitung.TryGetValue(kata, n)
            hitung(kata) = n + 1
        Next

        For Each pasangan In hitung.OrderByDescending(Function(p) p.Value).
                                     ThenBy(Function(p) p.Key, StringComparer.Ordinal)
            Console.WriteLine($"{pasangan.Key,-7}: {pasangan.Value}")
        Next
        Console.WriteLine($"Kata unik  : {hitung.Count}")

        Console.WriteLine("---")

        ' --- HashSet, Queue, Stack ---
        Dim unik As New HashSet(Of Integer) From {1, 2, 2, 3, 3, 3}
        Console.WriteLine($"HashSet   : {String.Join(",", unik)}")
        Console.WriteLine($"Add 2 lagi: {unik.Add(2)}")

        Dim antre As New Queue(Of String)
        antre.Enqueue("Andi")
        antre.Enqueue("Budi")
        Console.WriteLine($"Dilayani  : {antre.Dequeue()}")

        Dim tumpuk As New Stack(Of String)
        tumpuk.Push("hal-1")
        tumpuk.Push("hal-2")
        Console.WriteLine($"Kembali   : {tumpuk.Pop()}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Dim kosong(4) -> 5 elemen, indeks 0..4",
                    "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
                    "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
                    "  Jumlah    : 8",
                    "  Total     : 631",
                    "  Rata-rata : 78.88",
                    "  Tertinggi : 95",
                    "  Terendah  : 59",
                    "  ---",
                    "  List      : Andi, Budi, Cici, Dedi",
                    "  Count     : 4",
                    "  Ada Andi? : True",
                    "  ---",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "  Kata unik  : 4",
                    "  ---",
                    "  HashSet   : 1,2,3",
                    "  Add 2 lagi: False",
                    "  Dilayani  : Andi",
                    "  Kembali   : hal-2",
                    "",
                    "Baris pertama adalah buktinya: `Dim kosong(4)` memberi",
                    "LIMA elemen. Kalau kamu datang dari bahasa lain dan",
                    "menulis `Dim a(n)` mengira itu n elemen, seluruh",
                    "perhitunganmu akan meleset satu.",
                    "",
                    "`Array.Sort` mengubah array ASLINYA. Itu sebabnya ada",
                    "`nilai.Clone()` sebelum mengurutkan — sama seperti di",
                    "C#, karena memang pustaka yang sama.",
                    "",
                    "Titik di ujung baris (`.OrderByDescending(...).`)",
                    "adalah cara merangkai method di beberapa baris tanpa",
                    "garis bawah. Bentuk itu tersedia sejak VB 2010 dan",
                    "membuat rantai LINQ jauh lebih terbaca.",
                    "",
                    "`\" \"c` dengan akhiran c adalah literal CHAR, bukan",
                    "String. `Split` menerima keduanya, tapi versi Char lebih",
                    "cepat dan lebih jelas maksudnya.",
                ]
            },
        ],
    },
    {
        "title": "7. Sub, Function & Parameter",
        "sections": [
            {
                "body": [
                    "VB membedakan dua jenis prosedur, dan pembedaan itu",
                    "eksplisit di kata kuncinya:",
                    "",
                    "  Sub       TIDAK mengembalikan nilai",
                    "  Function  mengembalikan nilai",
                    "",
                    "  Sub Sapa(nama As String)",
                    "      Console.WriteLine(\"Halo, \" & nama)",
                    "  End Sub",
                    "",
                    "  Function Tambah(a As Integer, b As Integer) As Integer",
                    "      Return a + b",
                    "  End Function",
                    "",
                    "CARA MENGOPER PARAMETER:",
                    "",
                    "  ByVal   salinan nilainya. BAWAAN sejak VB.NET.",
                    "  ByRef   referensi ke variabel aslinya.",
                    "",
                    "Di VB6, bawaannya justru ByRef — sumber bug yang sangat",
                    "sering di kode lama. Di VB.NET bawaannya ByVal, dan itu",
                    "yang benar.",
                    "",
                    "Perhatikan halus: `ByVal` pada TIPE REFERENSI (String,",
                    "array, class) menyalin REFERENSINYA, bukan objeknya.",
                    "Jadi mengubah isi array yang dioper ByVal TETAP terlihat",
                    "di pemanggil; yang tidak terlihat cuma penugasan ulang",
                    "variabelnya.",
                    "",
                    "PARAMETER OPSIONAL:",
                    "  Sub Sapa(nama As String, Optional salam As String = \"Halo\")",
                    "",
                    "Parameter opsional WAJIB punya nilai bawaan dan harus",
                    "berada di akhir.",
                    "",
                    "PARAMETER BEBAS JUMLAHNYA:",
                    "  Function Total(ParamArray angka() As Integer) As Integer",
                    "",
                    "ARGUMEN BERNAMA memakai tanda titik dua sama dengan:",
                    "  Sapa(salam:=\"Hai\", nama:=\"Andi\")",
                    "",
                    "Perhatikan `:=`, bukan `=`. Ini karena `=` sudah dipakai",
                    "untuk perbandingan di dalam ekspresi.",
                    "",
                    "OVERLOAD ditandai kata `Overloads` (opsional):",
                    "  Function Luas(sisi As Double) As Double",
                    "  Function Luas(p As Double, l As Double) As Double",
                    "",
                    "Yang membedakan overload: jumlah dan tipe parameter.",
                    "Tipe kembalian TIDAK membedakan.",
                    "",
                    "Prosedur di dalam MODULE otomatis Shared dan bisa",
                    "dipanggil tanpa nama modulnya — itulah gunanya Module.",
                ]
            },
            {
                "heading": "Semua bentuk parameter",
                "code": """Option Strict On

Imports System

Module Program

    ' ByVal (bawaan): salinan
    Sub NaikkanSalinan(ByVal n As Integer)
        n += 100
    End Sub

    ' ByRef: menyentuh variabel aslinya
    Sub NaikkanAsli(ByRef n As Integer)
        n += 100
    End Sub

    Sub Tukar(ByRef a As Integer, ByRef b As Integer)
        Dim sementara As Integer = a
        a = b
        b = sementara
    End Sub

    ' Optional dan ParamArray
    Function Garis(isi As String,
                   Optional lebar As Integer = 30,
                   Optional pengisi As Char = "-"c) As String
        Dim sisa As Integer = Math.Max(lebar - isi.Length, 0)
        Dim kiri As Integer = sisa \\ 2
        Return New String(pengisi, kiri) & isi & New String(pengisi, sisa - kiri)
    End Function

    Function Total(ParamArray angka() As Integer) As Integer
        Dim jumlah As Integer = 0
        For Each n As Integer In angka
            jumlah += n
        Next
        Return jumlah
    End Function

    ' Overload: satu nama, beberapa bentuk
    Function Luas(sisi As Double) As Double
        Return sisi * sisi
    End Function

    Function Luas(panjang As Double, lebar As Double) As Double
        Return panjang * lebar
    End Function

    ' Tuple bernama: mengembalikan dua nilai
    Function Bagi(a As Integer, b As Integer) As (hasil As Integer, sisa As Integer)
        Return (a \\ b, a Mod b)
    End Function

    Sub Main()
        Dim x As Integer = 5
        NaikkanSalinan(x)
        Console.WriteLine($"sesudah ByVal : {x}")
        NaikkanAsli(x)
        Console.WriteLine($"sesudah ByRef : {x}")

        Dim a As Integer = 3, b As Integer = 8
        Tukar(a, b)
        Console.WriteLine($"sesudah Tukar : a={a} b={b}")

        Console.WriteLine("---")
        Console.WriteLine(Garis(" REKAP "))
        Console.WriteLine(Garis(" KECIL ", 20))
        Console.WriteLine(Garis(" TEBAL ", pengisi:="="c))
        Console.WriteLine(Garis(lebar:=24, isi:=" BERNAMA ", pengisi:="*"c))

        Console.WriteLine("---")
        Console.WriteLine($"Total()       = {Total()}")
        Console.WriteLine($"Total(1,2,3)  = {Total(1, 2, 3)}")

        Console.WriteLine("---")
        Console.WriteLine($"Luas(5)       = {Luas(5)}")
        Console.WriteLine($"Luas(4, 6)    = {Luas(4, 6)}")

        Console.WriteLine("---")
        Dim r = Bagi(17, 5)
        Console.WriteLine($"17 / 5        = {r.hasil} sisa {r.sisa}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  sesudah ByVal : 5",
                    "  sesudah ByRef : 105",
                    "  sesudah Tukar : a=8 b=3",
                    "  ---",
                    "  ----------- REKAP ------------",
                    "  ------ KECIL -------",
                    "  =========== TEBAL ============",
                    "  ******* BERNAMA ********",
                    "  ---",
                    "  Total()       = 0",
                    "  Total(1,2,3)  = 6",
                    "  ---",
                    "  Luas(5)       = 25",
                    "  Luas(4, 6)    = 24",
                    "  ---",
                    "  17 / 5        = 3 sisa 2",
                    "",
                    "Dua baris pertama menunjukkan seluruh perbedaan ByVal",
                    "dan ByRef dalam satu tampilan: yang pertama tidak",
                    "mengubah apa pun di pemanggil, yang kedua mengubah.",
                    "",
                    "`pengisi:=\"=\"c` memakai argumen bernama untuk melewati",
                    "parameter `lebar` yang ada di tengah. Tanpa itu, kamu",
                    "harus menuliskan nilai bawaannya lagi hanya supaya bisa",
                    "sampai ke parameter ketiga.",
                    "",
                    "`New String(pengisi, kiri)` membuat string berisi",
                    "karakter yang sama sebanyak n kali — padanan",
                    "`\"-\".repeat(n)` di bahasa lain.",
                    "",
                    "Tuple bernama `(hasil As Integer, sisa As Integer)`",
                    "membuat dua nilai kembalian bisa dibaca dengan namanya",
                    "sendiri alih-alih `Item1` dan `Item2`. Ini tersedia",
                    "sejak VB 15 dan layak dipakai di kode baru.",
                ]
            },
        ],
    },
    {
        "title": "8. Teks & Format",
        "sections": [
            {
                "body": [
                    "String di VB.NET adalah `System.String` yang sama",
                    "persis dengan C# — termasuk sifatnya yang IMMUTABLE.",
                    "Setiap method mengembalikan string BARU.",
                    "",
                    "  nama.ToUpper()          tidak mengubah nama",
                    "  nama = nama.ToUpper()   ini yang benar",
                    "",
                    "Method yang paling sering dipakai:",
                    "  Length                  PROPERTY, bukan method",
                    "  ToUpper / ToLower",
                    "  Trim / TrimStart / TrimEnd",
                    "  Substring(2, 4)",
                    "  IndexOf(\"abc\")          -1 kalau tidak ada",
                    "  Contains / StartsWith / EndsWith",
                    "  Replace(\"a\", \"b\")",
                    "  Split(\",\"c)",
                    "  String.Join(\", \", arr)",
                    "  PadLeft(10) / PadRight(10)",
                    "  String.IsNullOrEmpty(s)",
                    "  String.IsNullOrWhiteSpace(s)",
                    "",
                    "VB juga punya FUNGSI WARISAN dari VB6 yang masih ada:",
                    "  Len(s)  UCase(s)  LCase(s)  Mid(s, 2, 3)",
                    "  Left(s, 3)  Right(s, 3)  InStr(s, \"x\")  Trim(s)",
                    "",
                    "Fungsi-fungsi itu BUKAN salah, tapi ada dua alasan",
                    "memilih method .NET untuk kode baru:",
                    "  - Ia sama dengan yang dipakai C#, sehingga contoh dan",
                    "    dokumentasi berlimpah.",
                    "  - `Mid` dan `InStr` berindeks MULAI 1, sementara",
                    "    `Substring` dan `IndexOf` mulai 0. Mencampur",
                    "    keduanya di satu berkas adalah undangan bagi",
                    "    kesalahan satu-lebih.",
                    "",
                    "FORMAT ANGKA memakai penentu yang sama dengan C#:",
                    "  {n:C}      mata uang",
                    "  {n:N0}     angka, 0 desimal",
                    "  {n:F2}     dua desimal",
                    "  {n:P1}     persen",
                    "  {n:X}      heksadesimal",
                    "  {t:yyyy-MM-dd}  tanggal",
                    "",
                    "PERATAAN memakai koma di dalam interpolasi:",
                    "  {nama,-15}   rata KIRI selebar 15",
                    "  {harga,10}   rata KANAN selebar 10",
                    "",
                    "Untuk teks multi-baris, VB TIDAK punya raw string",
                    "seperti C#. Yang dipakai: `vbCrLf`, `vbLf`, atau",
                    "`Environment.NewLine`, disambung dengan `&`.",
                    "",
                    "Konstanta bawaan yang sering dipakai: `vbCrLf`, `vbTab`,",
                    "`vbNullString`, dan `ControlChars.Quote` untuk tanda",
                    "kutip.",
                ]
            },
            {
                "heading": "Mengolah teks dan menyusun tabel",
                "code": """Option Strict On

Imports System
Imports System.Globalization
Imports System.Text

Module Program

    Sub Main()
        Dim kalimat As String = "Visual Basic membuat kode bisnis mudah dibaca"

        Console.WriteLine($"asli       : {kalimat}")
        Console.WriteLine($"panjang    : {kalimat.Length}")
        Console.WriteLine($"kata       : {kalimat.Split(" "c).Length}")
        Console.WriteLine($"besar      : {kalimat.ToUpper()}")
        Console.WriteLine($"ganti      : {kalimat.Replace("bisnis", "apa pun")}")
        Console.WriteLine($"mulai?     : {kalimat.StartsWith("Visual")}")
        Console.WriteLine($"posisi     : {kalimat.IndexOf("kode")}")

        Dim terpanjang As String = ""
        For Each kata As String In kalimat.Split(" "c)
            If kata.Length > terpanjang.Length Then terpanjang = kata
        Next
        Console.WriteLine($"terpanjang : {terpanjang}")

        Console.WriteLine("---")

        ' Membangun teks bertahap dengan StringBuilder
        Dim sb As New StringBuilder()
        For i As Integer = 1 To 5
            sb.Append(i).Append(" ")
        Next
        Console.WriteLine($"builder    : {sb.ToString().Trim()}")

        Console.WriteLine("---")

        ' Tabel dengan perataan
        Dim barang() As String = {"Keyboard", "Mouse", "Monitor"}
        Dim jumlah() As Integer = {3, 12, 2}
        Dim harga() As Integer = {350000, 85000, 1750000}

        Console.WriteLine($"{"Barang",-12}{"Qty",5}{"Harga",15}")
        Console.WriteLine(New String("-"c, 32))

        Dim total As Integer = 0
        For i As Integer = 0 To barang.Length - 1
            Dim sub_ As Integer = jumlah(i) * harga(i)
            total += sub_
            Console.WriteLine($"{barang(i),-12}{jumlah(i),5}{sub_,15:N0}")
        Next

        Console.WriteLine(New String("-"c, 32))
        Console.WriteLine($"{"TOTAL",-12}{"",5}{total,15:N0}")

        Console.WriteLine("---")

        ' Teks multi-baris: VB memakai vbCrLf, bukan raw string
        Dim surat As String =
            "Halo Andi," & vbCrLf &
            vbCrLf &
            "Baris ini disambung dengan vbCrLf."
        Console.WriteLine(surat)
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  asli       : Visual Basic membuat kode bisnis mudah dibaca",
                    "  panjang    : 45",
                    "  kata       : 7",
                    "  besar      : VISUAL BASIC MEMBUAT KODE BISNIS MUDAH DIBACA",
                    "  ganti      : Visual Basic membuat kode apa pun mudah dibaca",
                    "  mulai?     : True",
                    "  posisi     : 21",
                    "  terpanjang : membuat",
                    "  ---",
                    "  builder    : 1 2 3 4 5",
                    "  ---",
                    "  Barang        Qty          Harga",
                    "  --------------------------------",
                    "  Keyboard        3      1,050,000",
                    "  Mouse          12      1,020,000",
                    "  Monitor         2      3,500,000",
                    "  --------------------------------",
                    "  TOTAL                  5,570,000",
                    "  ---",
                    "  Halo Andi,",
                    "",
                    "  Baris ini disambung dengan vbCrLf.",
                    "",
                    "Pemisah ribuan yang muncul tergantung setelan wilayah",
                    "mesin. Di aplikasi ini budayanya dipatok INVARIANT",
                    "sehingga pemisahnya koma; di komputer ber-locale",
                    "Indonesia ia akan jadi titik. Untuk keluaran yang harus",
                    "sama di mana pun, oper `CultureInfo.InvariantCulture`",
                    "secara eksplisit.",
                    "",
                    "Variabel bernama `sub_` memakai garis bawah karena `Sub`",
                    "adalah KATA KUNCI di VB. Cara lain: bungkus dengan",
                    "kurung siku — `[Sub]` — yang membuat VB",
                    "memperlakukannya sebagai nama biasa. Itu berguna saat",
                    "kamu memakai pustaka yang punya anggota bernama seperti",
                    "kata kunci VB.",
                    "",
                    "`New String(\"-\"c, 32)` membuat garis pemisah. Ia",
                    "padanan `\"-\".repeat(32)` di bahasa lain, dan bentuknya",
                    "sama persis dengan C#.",
                ]
            },
        ],
    },
    {
        "title": "9. Class, Property & Constructor",
        "sections": [
            {
                "body": [
                    "  Class Murid",
                    "      Private _nilai As Integer",
                    "",
                    "      Public Property Nama As String",
                    "",
                    "      Public Property Nilai As Integer",
                    "          Get",
                    "              Return _nilai",
                    "          End Get",
                    "          Set(value As Integer)",
                    "              If value < 0 OrElse value > 100 Then",
                    "                  Throw New ArgumentOutOfRangeException()",
                    "              End If",
                    "              _nilai = value",
                    "          End Set",
                    "      End Property",
                    "",
                    "      Public Sub New(nama As String, nilai As Integer)",
                    "          Me.Nama = nama",
                    "          Me.Nilai = nilai",
                    "      End Sub",
                    "  End Class",
                    "",
                    "Beberapa hal yang khas VB:",
                    "",
                    "  Public Property Nama As String",
                    "    AUTO-PROPERTY. Satu baris menghasilkan property",
                    "    dengan getter, setter, dan field tersembunyi",
                    "    bernama `_Nama`.",
                    "",
                    "  Public Sub New(...)",
                    "    Constructor. Namanya SELALU `New`, bukan nama",
                    "    class-nya seperti di C# dan Java.",
                    "",
                    "  Me",
                    "    Menunjuk objek yang sedang dikerjakan. Padanan",
                    "    `this` di C#.",
                    "",
                    "  Set(value As Integer)",
                    "    Parameter setter bernama `value` menurut kebiasaan.",
                    "",
                    "Modifier akses:",
                    "  Public      siapa pun",
                    "  Friend      hanya di dalam assembly ini (BAWAAN untuk",
                    "              class); padanan `internal` di C#",
                    "  Protected   class ini dan turunannya",
                    "  Private     hanya class ini (BAWAAN untuk anggota)",
                    "  Protected Friend / Private Protected",
                    "",
                    "Anggota statis memakai kata `Shared`, bukan `static`:",
                    "  Private Shared _urutan As Integer",
                    "  Public Shared Function Buat(...) As Murid",
                    "",
                    "Property hanya-baca:",
                    "  Public ReadOnly Property Grade As String",
                    "      Get",
                    "          Return If(_nilai >= 85, \"A\", \"B\")",
                    "      End Get",
                    "  End Property",
                    "",
                    "Sejak VB 14 ada bentuk singkatnya:",
                    "  Public ReadOnly Property Grade As String =",
                    "      If(_nilai >= 85, \"A\", \"B\")",
                    "",
                    "Tapi hati-hati: bentuk itu dihitung SEKALI saat objek",
                    "dibuat, bukan setiap kali dibaca. Untuk nilai yang",
                    "berubah, pakai bentuk Get.",
                    "",
                    "`Overrides Function ToString()` menentukan bagaimana",
                    "objek dicetak. Tanpa itu, yang muncul cuma nama tipenya.",
                ]
            },
            {
                "heading": "Class lengkap",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic

Class Rekening

    Private Shared _urutan As Integer = 0
    Private _saldo As Long

    Public ReadOnly Property Nomor As String
    Public ReadOnly Property Pemilik As String

    Public ReadOnly Property Saldo As Long
        Get
            Return _saldo
        End Get
    End Property

    Public ReadOnly Property Kosong As Boolean
        Get
            Return _saldo = 0
        End Get
    End Property

    Public Sub New(pemilik As String, Optional saldoAwal As Long = 0)
        If String.IsNullOrWhiteSpace(pemilik) Then
            Throw New ArgumentException("pemilik wajib diisi", NameOf(pemilik))
        End If

        _urutan += 1
        Me.Nomor = $"AC{_urutan:D4}"
        Me.Pemilik = pemilik
        _saldo = saldoAwal
    End Sub

    Public Function Setor(jumlah As Long) As Rekening
        If jumlah <= 0 Then
            Throw New ArgumentOutOfRangeException(NameOf(jumlah))
        End If
        _saldo += jumlah
        Return Me
    End Function

    Public Function Tarik(jumlah As Long) As Boolean
        If jumlah <= 0 OrElse jumlah > _saldo Then Return False
        _saldo -= jumlah
        Return True
    End Function

    Public Shared Function BuatBanyak(ParamArray nama() As String) As List(Of Rekening)
        Dim hasil As New List(Of Rekening)
        For Each n As String In nama
            hasil.Add(New Rekening(n))
        Next
        Return hasil
    End Function

    Public Overrides Function ToString() As String
        Return $"{Nomor} {Pemilik,-8}{_saldo,12}"
    End Function

End Class

Module Program

    Sub Main()
        Dim a As New Rekening("Andi", 500000)
        Dim b As New Rekening("Budi")

        a.Setor(250000)
        Console.WriteLine($"tarik 900rb: {a.Tarik(900000)}")
        Console.WriteLine($"tarik 300rb: {a.Tarik(300000)}")
        b.Setor(100000)

        Console.WriteLine(a.ToString())
        Console.WriteLine(b.ToString())
        Console.WriteLine($"b kosong?  : {b.Kosong}")

        Console.WriteLine("---")
        For Each r As Rekening In Rekening.BuatBanyak("Cici", "Dedi")
            Console.WriteLine(r.ToString())
        Next

        Try
            Dim salah As New Rekening("   ")
        Catch ex As ArgumentException
            Console.WriteLine($"Ditolak: {ex.Message.Split(vbLf)(0)}")
        End Try
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tarik 900rb: False",
                    "  tarik 300rb: True",
                    "  AC0001 Andi          450000",
                    "  AC0002 Budi          100000",
                    "  b kosong?  : False",
                    "  ---",
                    "  AC0003 Cici               0",
                    "  AC0004 Dedi               0",
                    "  Ditolak: pemilik wajib diisi",
                    "",
                    "Empat hal yang layak diperhatikan:",
                    "",
                    "  1. `Public ReadOnly Property Nomor As String` adalah",
                    "     auto-property hanya-baca. Ia BOLEH diisi di dalam",
                    "     constructor, dan terkunci sesudah itu.",
                    "",
                    "  2. `_saldo` private dengan property `Saldo` untuk",
                    "     membaca. Kalau ia Public, seluruh aturan di Setor",
                    "     dan Tarik bisa dilewati dengan satu baris.",
                    "",
                    "  3. `Private Shared _urutan` milik CLASS, bukan objek.",
                    "     Ada satu untuk seluruh program, dan itulah yang",
                    "     membuat penomoran otomatis bekerja.",
                    "",
                    "  4. `Setor` mengembalikan `Me`, sehingga bisa dirantai.",
                    "",
                    "`NameOf(pemilik)` menghasilkan string \"pemilik\" dan",
                    "IKUT BERUBAH kalau nama parameternya diganti. Menulis",
                    "namanya sebagai teks biasa tidak punya sifat itu.",
                    "",
                    "`ex.Message.Split(vbLf)(0)` mengambil baris pertama",
                    "pesannya. ArgumentException menambahkan nama parameter",
                    "di baris kedua, dan untuk contoh ini yang menarik cuma",
                    "kalimat pertamanya.",
                    "",
                    "Perhatikan `Split(...)(0)` memakai kurung biasa untuk",
                    "mengindeks hasilnya — di VB, indeks dan pemanggilan",
                    "fungsi memakai tanda yang sama.",
                ]
            },
        ],
    },
    {
        "title": "10. Pewarisan, Interface & MustInherit",
        "sections": [
            {
                "body": [
                    "PEWARISAN memakai kata `Inherits`, ditulis di baris",
                    "TERSENDIRI sesudah nama class:",
                    "",
                    "  Class Kucing",
                    "      Inherits Hewan",
                    "  End Class",
                    "",
                    "Kata kunci yang mengatur penimpaan:",
                    "  Overridable   di INDUK: boleh ditimpa",
                    "  Overrides     di TURUNAN: aku menimpanya",
                    "  MustOverride  di induk: turunan WAJIB mengisinya",
                    "  NotOverridable di turunan: berhenti di sini",
                    "  MustInherit   class yang tidak bisa di-New (abstract)",
                    "  NotInheritable class yang tidak bisa diturunkan (sealed)",
                    "  Shadows       menyembunyikan, BUKAN menimpa",
                    "",
                    "Sama seperti C#, method TIDAK bisa ditimpa secara bawaan.",
                    "Kamu harus menulis `Overridable` dulu di induknya.",
                    "",
                    "`MyBase` menunjuk induk:",
                    "  MyBase.New(nama)      panggil constructor induk",
                    "  MyBase.Ringkas()      panggil versi induk",
                    "",
                    "`MyClass` menunjuk implementasi di class INI, mengabaikan",
                    "penimpaan oleh turunan. Ia jarang dipakai tapi berguna",
                    "saat sebuah method harus memakai versinya sendiri.",
                    "",
                    "Constructor induk SELALU dijalankan lebih dulu. Kalau",
                    "induknya tidak punya constructor tanpa parameter, kamu",
                    "WAJIB memanggil `MyBase.New(...)` di baris pertama.",
                    "",
                    "INTERFACE dan cara VB mengimplementasinya BERBEDA dari",
                    "C#, dan ini sering mengejutkan:",
                    "",
                    "  Interface IBangun",
                    "      Function Luas() As Double",
                    "      ReadOnly Property Nama As String",
                    "  End Interface",
                    "",
                    "  Class Persegi",
                    "      Implements IBangun",
                    "",
                    "      Public Function Luas() As Double Implements IBangun.Luas",
                    "          ...",
                    "      End Function",
                    "  End Class",
                    "",
                    "Setiap anggota WAJIB menyebut `Implements IBangun.Luas`",
                    "secara eksplisit. Keuntungannya: nama methodmu boleh",
                    "BERBEDA dari nama di interface, dan satu method bisa",
                    "mengimplementasi beberapa anggota sekaligus.",
                    "",
                    "Satu class boleh mengimplementasi banyak interface tapi",
                    "hanya punya satu induk.",
                ]
            },
            {
                "heading": "Abstract, interface, dan polimorfisme",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic

Interface IBangun
    ReadOnly Property Nama As String
    Function Luas() As Double
    Function Keliling() As Double
End Interface

MustInherit Class BangunDasar
    Implements IBangun

    Public ReadOnly Property Nama As String Implements IBangun.Nama

    Protected Sub New(nama As String)
        Me.Nama = nama
    End Sub

    Public MustOverride Function Luas() As Double Implements IBangun.Luas
    Public MustOverride Function Keliling() As Double Implements IBangun.Keliling

    Public Overridable Function Ringkas() As String
        Return $"{Nama,-16}{Luas(),8:F2}{Keliling(),10:F2}"
    End Function
End Class

Class Persegi
    Inherits BangunDasar

    Private ReadOnly _sisi As Double

    Public Sub New(sisi As Double)
        MyBase.New("Persegi")
        _sisi = sisi
    End Sub

    Public Overrides Function Luas() As Double
        Return _sisi * _sisi
    End Function

    Public Overrides Function Keliling() As Double
        Return 4 * _sisi
    End Function
End Class

Class Lingkaran
    Inherits BangunDasar

    Private Const PI As Double = 3.14159
    Private ReadOnly _jari As Double

    Public Sub New(jari As Double)
        MyBase.New("Lingkaran")
        _jari = jari
    End Sub

    Public Overrides Function Luas() As Double
        Return PI * _jari * _jari
    End Function

    Public Overrides Function Keliling() As Double
        Return 2 * PI * _jari
    End Function

    Public Overrides Function Ringkas() As String
        Return MyBase.Ringkas() & $"  (r={_jari})"
    End Function
End Class

Module Program

    Sub Main()
        Dim semua As New List(Of IBangun) From {
            New Persegi(4),
            New Lingkaran(3),
            New Persegi(2.5)
        }

        Dim totalLuas As Double = 0
        For Each b As IBangun In semua
            Dim baris As String = If(TypeOf b Is BangunDasar,
                                     CType(b, BangunDasar).Ringkas(),
                                     b.Nama)
            Console.WriteLine(baris)
            totalLuas += b.Luas()
        Next

        Console.WriteLine($"{"TOTAL",-16}{totalLuas,8:F2}")

        Console.WriteLine("---")
        Console.WriteLine($"semua(0) IBangun?     : {TypeOf semua(0) Is IBangun}")
        Console.WriteLine($"semua(1) Lingkaran?   : {TypeOf semua(1) Is Lingkaran}")
        Console.WriteLine($"semua(1) BangunDasar? : {TypeOf semua(1) Is BangunDasar}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Persegi            16.00     16.00",
                    "  Lingkaran          28.27     18.85  (r=3)",
                    "  Persegi             6.25     10.00",
                    "  TOTAL              50.52",
                    "  ---",
                    "  semua(0) IBangun?     : True",
                    "  semua(1) Lingkaran?   : True",
                    "  semua(1) BangunDasar? : True",
                    "",
                    "Inilah POLIMORFISME: `b.Luas()` di dalam For Each",
                    "memanggil method yang BERBEDA tiap putaran, padahal",
                    "kodenya satu baris dan tipe variabelnya cuma IBangun.",
                    "",
                    "Akibat praktisnya: menambah bangun baru tidak menyentuh",
                    "satu baris pun di Main. Itu ukuran keberhasilan desain",
                    "berorientasi objek — bukan jumlah class-nya, melainkan",
                    "berapa banyak kode lama yang TIDAK perlu disunting.",
                    "",
                    "Perhatikan `Public MustOverride Function Luas() As Double",
                    "Implements IBangun.Luas` menggabungkan dua hal sekaligus:",
                    "ia menyatakan method itu abstrak DAN mengaitkannya ke",
                    "anggota interface. Di C#, keduanya terjadi implisit.",
                    "",
                    "`TypeOf x Is T` memeriksa tipe saat program jalan, dan",
                    "`CType(x, T)` mengonversinya. Ada juga `TryCast(x, T)`",
                    "yang mengembalikan Nothing alih-alih melempar kalau",
                    "tipenya tidak cocok — padanan `as` di C#.",
                    "",
                    "`Protected Sub New(...)` mencegah `New BangunDasar(...)`",
                    "dari luar, tapi tetap memperbolehkan turunannya",
                    "memanggil `MyBase.New`.",
                ]
            },
        ],
    },
    {
        "title": "11. Structure, Enum & Module",
        "sections": [
            {
                "body": [
                    "STRUCTURE adalah tipe NILAI: menyalinnya menyalin",
                    "seluruh isinya, bukan alamatnya.",
                    "",
                    "  Structure Titik",
                    "      Public X As Integer",
                    "      Public Y As Integer",
                    "  End Structure",
                    "",
                    "Kapan memakai Structure alih-alih Class:",
                    "  - Ukurannya kecil, di bawah sekitar 16 byte.",
                    "  - Isinya tidak berubah sesudah dibuat.",
                    "  - Ia berperilaku seperti angka: titik koordinat,",
                    "    rentang tanggal, jumlah uang.",
                    "",
                    "Kalau ragu, pakai Class. Structure yang besar justru",
                    "lebih lambat karena ia disalin setiap kali dioper.",
                    "",
                    "Structure TIDAK BISA:",
                    "  - mewarisi structure lain",
                    "  - punya constructor tanpa parameter sendiri",
                    "  - punya field dengan nilai awal",
                    "",
                    "Tapi ia BISA mengimplementasi interface.",
                    "",
                    "ENUM adalah sekumpulan konstanta bernama:",
                    "",
                    "  Enum Status",
                    "      Draf",
                    "      Ditinjau",
                    "      Terbit",
                    "  End Enum",
                    "",
                    "  Enum Prioritas",
                    "      Rendah = 1",
                    "      Sedang = 5",
                    "      Tinggi = 10",
                    "  End Enum",
                    "",
                    "Operasi yang berguna:",
                    "  CInt(s)                       jadi angka",
                    "  CType(3, Status)              dari angka",
                    "  s.ToString()                  namanya",
                    "  [Enum].GetValues(GetType(Status))",
                    "  [Enum].IsDefined(GetType(Status), n)",
                    "  [Enum].TryParse(Of Status)(teks, hasil)",
                    "",
                    "Perhatikan `[Enum]` dalam kurung siku: `Enum` adalah",
                    "kata kunci VB, jadi untuk memakai CLASS bernama sama",
                    "namanya harus dikurung.",
                    "",
                    "Enum ber-`<Flags>` menyimpan banyak pilihan dalam satu",
                    "angka, memakai bit:",
                    "",
                    "  <Flags>",
                    "  Enum Izin",
                    "      Tidak = 0",
                    "      Baca = 1",
                    "      Tulis = 2",
                    "      Hapus = 4",
                    "  End Enum",
                    "",
                    "MODULE adalah wadah untuk kode tanpa objek. Seluruh",
                    "isinya otomatis Shared, dan bisa dipanggil TANPA menyebut",
                    "nama modulnya dari mana pun di proyek yang sama.",
                    "",
                    "Itu membuat Module tempat yang tepat untuk fungsi bantu,",
                    "konstanta, dan extension method — tapi juga tempat yang",
                    "gampang jadi tong sampah. Kalau sebuah Module sudah",
                    "memuat tiga puluh fungsi yang tidak berhubungan, yang",
                    "kamu butuhkan sebenarnya beberapa class.",
                ]
            },
            {
                "heading": "Structure, Enum, dan Flags",
                "code": """Option Strict On

Imports System

Structure Titik
    Public ReadOnly X As Integer
    Public ReadOnly Y As Integer

    Public Sub New(x As Integer, y As Integer)
        Me.X = x
        Me.Y = y
    End Sub

    Public Function Jarak() As Double
        Return Math.Sqrt(X * X + Y * Y)
    End Function

    Public Overrides Function ToString() As String
        Return $"({X}, {Y})"
    End Function
End Structure

Class TitikKelas
    Public X As Integer
    Public Y As Integer
End Class

Enum Status
    Draf
    Ditinjau
    Disetujui
    Terbit
End Enum

<Flags>
Enum Izin
    Tidak = 0
    Baca = 1
    Tulis = 2
    Hapus = 4
    Jalan = 8
    Penuh = Baca Or Tulis Or Hapus Or Jalan
End Enum

Module Program

    Sub Main()
        ' --- Structure: DISALIN isinya ---
        Dim s1 As New Titik(1, 2)
        Dim s2 As Titik = s1
        Console.WriteLine($"structure : s1={s1} s2={s2} jarak={s1.Jarak():F3}")

        ' --- Class: disalin ALAMATNYA ---
        Dim c1 As New TitikKelas With {.X = 1, .Y = 2}
        Dim c2 As TitikKelas = c1
        c2.X = 99
        Console.WriteLine($"class     : c1.X={c1.X} c2.X={c2.X}  <- ikut berubah")

        Console.WriteLine("---")

        ' --- Enum ---
        Dim st As Status = Status.Ditinjau
        Console.WriteLine($"nama      : {st}")
        Console.WriteLine($"angka     : {CInt(st)}")
        Console.WriteLine($"dari 3    : {CType(3, Status)}")
        Console.WriteLine($"sah 9?    : {[Enum].IsDefined(GetType(Status), 9)}")

        Console.Write("semua     : ")
        For Each nilai As Status In [Enum].GetValues(GetType(Status))
            Console.Write($"{nilai}({CInt(nilai)}) ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Flags: banyak pilihan dalam satu angka ---
        Dim editor As Izin = Izin.Baca Or Izin.Tulis
        Console.WriteLine($"editor    : {editor} = {CInt(editor)}")
        Console.WriteLine($"boleh tulis? {editor.HasFlag(Izin.Tulis)}")
        Console.WriteLine($"boleh hapus? {editor.HasFlag(Izin.Hapus)}")

        editor = editor Or Izin.Hapus
        Console.WriteLine($"+hapus    : {editor}")

        editor = editor And Not Izin.Baca
        Console.WriteLine($"-baca     : {editor}")
        Console.WriteLine($"penuh     : {Izin.Penuh} = {CInt(Izin.Penuh)}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  structure : s1=(1, 2) s2=(1, 2) jarak=2.236",
                    "  class     : c1.X=99 c2.X=99  <- ikut berubah",
                    "  ---",
                    "  nama      : Ditinjau",
                    "  angka     : 1",
                    "  dari 3    : Terbit",
                    "  sah 9?    : False",
                    "  semua     : Draf(0) Ditinjau(1) Disetujui(2) Terbit(3) ",
                    "  ---",
                    "  editor    : Baca, Tulis = 3",
                    "  boleh tulis? True",
                    "  boleh hapus? False",
                    "  +hapus    : Baca, Tulis, Hapus",
                    "  -baca     : Tulis, Hapus",
                    "  penuh     : Penuh = 15",
                    "",
                    "Baris kedua adalah bug yang paling sering ditemui",
                    "pemula: mengubah `c2` ternyata mengubah `c1` juga,",
                    "karena keduanya nama untuk objek yang SAMA. Dengan",
                    "Structure, itu tidak terjadi.",
                    "",
                    "`With {.X = 1, .Y = 2}` adalah OBJECT INITIALIZER di VB",
                    "— padanan `{ X = 1, Y = 2 }` di C#. Perhatikan titik di",
                    "depan nama propertinya.",
                    "",
                    "PERINGATAN tentang enum: `CType(9, Status)` TIDAK",
                    "divalidasi. Ia menghasilkan enum bernilai 9 yang tidak",
                    "punya nama. Kalau nilainya datang dari database atau",
                    "masukan pengguna, periksa dengan `[Enum].IsDefined`.",
                    "",
                    "Atribut `<Flags>` TIDAK mengubah perilaku bitwise —",
                    "operator `Or` dan `And` bekerja pada enum apa pun. Yang",
                    "diubahnya cuma `ToString`: tanpa `<Flags>`, `editor` di",
                    "atas akan dicetak sebagai `3`, bukan `Baca, Tulis`.",
                    "",
                    "`And Not Izin.Baca` membuang satu izin. Di sinilah `And`",
                    "dan `Or` TANPA hubung-singkat memang yang benar: di",
                    "konteks bilangan, keduanya operator BIT, bukan logika.",
                ]
            },
        ],
    },
    {
        "title": "12. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "  Try",
                    "      ... kode yang mungkin gagal",
                    "  Catch ex As FormatException",
                    "      ... tangani yang spesifik dulu",
                    "  Catch ex As Exception",
                    "      ... jaring terakhir",
                    "  Finally",
                    "      ... SELALU dijalankan",
                    "  End Try",
                    "",
                    "Urutan Catch berarti: yang PALING SPESIFIK di atas.",
                    "Menulis `Catch ex As Exception` lebih dulu membuat Catch",
                    "di bawahnya tidak pernah tercapai, dan compiler akan",
                    "memperingatkanmu.",
                    "",
                    "VB punya satu hal yang tidak ada di C# sampai versi 6:",
                    "KLAUSA `When`.",
                    "",
                    "  Catch ex As IOException When ex.HResult = -2147024864",
                    "      ...",
                    "",
                    "Ia menyaring exception TANPA menangkapnya lebih dulu.",
                    "Bedanya dari memeriksa di dalam blok Catch: kalau",
                    "syaratnya tidak terpenuhi, exception-nya melanjutkan",
                    "perjalanan ke atas dengan jejak tumpukan yang UTUH.",
                    "",
                    "Melempar:",
                    "  Throw New ArgumentException(\"pesan\")",
                    "  Throw                             lempar ulang yang sama",
                    "",
                    "`Throw` polos MEMPERTAHANKAN jejak tumpukan aslinya.",
                    "`Throw ex` MENGHAPUSNYA, sehingga yang tercatat di log",
                    "adalah baris Catch-mu, bukan baris yang benar-benar",
                    "gagal. Selalu `Throw` polos.",
                    "",
                    "ON ERROR GOTO adalah warisan VB6 yang masih ada di",
                    "VB.NET, dan sebaiknya TIDAK kamu pakai:",
                    "",
                    "  On Error Resume Next      lanjutkan saja, abaikan galat",
                    "  On Error Goto Penanganan",
                    "",
                    "`On Error Resume Next` khususnya berbahaya: ia menelan",
                    "SETIAP galat dan program berjalan terus dalam keadaan",
                    "rusak. Ia juga tidak bisa dicampur dengan Try/Catch di",
                    "prosedur yang sama.",
                    "",
                    "Exception bawaan yang sering ditemui:",
                    "  NullReferenceException     memakai objek Nothing",
                    "  IndexOutOfRangeException   indeks di luar batas",
                    "  ArgumentException          argumen tidak masuk akal",
                    "  ArgumentNullException      argumen Nothing",
                    "  ArgumentOutOfRangeException",
                    "  InvalidOperationException  objek sedang tidak siap",
                    "  InvalidCastException       konversi tipe gagal",
                    "  FormatException            teks tidak sesuai format",
                    "  OverflowException          hasil melewati batas tipe",
                    "  DivideByZeroException      pembagian BULAT oleh nol",
                    "  IOException / FileNotFoundException",
                    "",
                    "Catatan halus: pembagian Double oleh nol TIDAK melempar.",
                    "Hasilnya Infinity atau NaN. Hanya pembagian BULAT",
                    "dengan `\\` dan `Mod` yang melempar.",
                ]
            },
            {
                "heading": "Exception sendiri, When, dan Finally",
                "code": """Option Strict On

Imports System

Class SaldoKurangException
    Inherits Exception

    Public ReadOnly Property Kurang As Long

    Public Sub New(kurang As Long)
        MyBase.New($"saldo kurang {kurang}")
        Me.Kurang = kurang
    End Sub
End Class

Class Dompet
    Private _saldo As Long

    Public Sub New(saldo As Long)
        _saldo = saldo
    End Sub

    Public ReadOnly Property Saldo As Long
        Get
            Return _saldo
        End Get
    End Property

    Public Sub Bayar(jumlah As Long)
        If jumlah <= 0 Then
            Throw New ArgumentOutOfRangeException(NameOf(jumlah),
                                                  $"jumlah {jumlah} tidak sah")
        End If
        If jumlah > _saldo Then Throw New SaldoKurangException(jumlah - _saldo)
        _saldo -= jumlah
    End Sub
End Class

Module Program

    Function DenganPengukur(nama As String, kerja As Func(Of Integer)) As Integer?
        Console.WriteLine($"mulai {nama}")
        Try
            Dim hasil As Integer = kerja()
            Console.WriteLine($"selesai {nama}")
            Return hasil
        Catch ex As InvalidOperationException
            Console.WriteLine($"galat: {ex.Message}")
            Return Nothing
        Finally
            Console.WriteLine($"(bersih {nama})")
        End Try
    End Function

    Sub Main()
        Dim d As New Dompet(50000)

        For Each tagihan As Long In New Long() {20000, -5, 100000, 30000}
            Try
                d.Bayar(tagihan)
                Console.WriteLine($"bayar {tagihan,7} -> sisa {d.Saldo}")
            Catch ex As SaldoKurangException
                Console.WriteLine($"bayar {tagihan,7} -> GAGAL, kurang {ex.Kurang}")
            Catch ex As ArgumentOutOfRangeException
                Console.WriteLine($"bayar {tagihan,7} -> DITOLAK: jumlah tidak sah")
            End Try
        Next

        Console.WriteLine("---")
        Console.WriteLine($"hasil: {DenganPengukur("hitung", Function() 6 * 7)}")
        Dim gagal As Integer? = DenganPengukur("gagal",
            Function() As Integer
                Throw New InvalidOperationException("rusak")
            End Function)
        Console.WriteLine($"hasil: {If(gagal.HasValue, gagal.ToString(), "Nothing")}")

        Console.WriteLine("---")

        ' Catch ... When: menyaring TANPA menangkap lebih dulu
        For Each teks As String In New String() {"42", "abc"}
            Try
                Console.WriteLine($"{teks} -> {Integer.Parse(teks)}")
            Catch ex As FormatException When teks = ""
                Console.WriteLine("teks kosong")
            Catch ex As FormatException
                Console.WriteLine($"{teks} -> bukan angka")
            End Try
        Next

        Console.WriteLine("---")
        Console.WriteLine($"1.0 / 0 = {1.0 / 0}")
        Dim nol As Integer = 0
        Try
            Console.WriteLine(1 \\ nol)
        Catch ex As DivideByZeroException
            Console.WriteLine("1 \\ 0 -> DivideByZeroException")
        End Try
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  bayar   20000 -> sisa 30000",
                    "  bayar      -5 -> DITOLAK: jumlah tidak sah",
                    "  bayar  100000 -> GAGAL, kurang 70000",
                    "  bayar   30000 -> sisa 0",
                    "  ---",
                    "  mulai hitung",
                    "  selesai hitung",
                    "  (bersih hitung)",
                    "  hasil: 42",
                    "  mulai gagal",
                    "  galat: rusak",
                    "  (bersih gagal)",
                    "  hasil: Nothing",
                    "  ---",
                    "  42 -> 42",
                    "  abc -> bukan angka",
                    "  ---",
                    "  1.0 / 0 = Infinity",
                    "  1 \\ 0 -> DivideByZeroException",
                    "",
                    "Dua baris terakhir menunjukkan hal yang sering",
                    "mengejutkan: pembagian PECAHAN oleh nol tidak melempar",
                    "apa pun — hasilnya Infinity. Hanya pembagian BULAT yang",
                    "melempar. Kalau kamu mengandalkan exception untuk",
                    "menangkap pembagian nol pada Double, ia tidak akan",
                    "pernah datang.",
                    "",
                    "`Finally` dijalankan BAHKAN saat bloknya melempar — di",
                    "kasus kedua, 'selesai gagal' tidak tercetak tapi",
                    "'(bersih gagal)' tetap. Inilah yang membuat pola ini",
                    "bisa menjamin berkas ditutup dan koneksi dilepas.",
                    "",
                    "`Function() As Integer ... End Function` adalah LAMBDA",
                    "MULTI-BARIS. VB memerlukan bentuk panjang ini untuk",
                    "lambda yang isinya lebih dari satu ekspresi — berbeda",
                    "dari C# yang cukup memakai kurung kurawal.",
                    "",
                    "`Integer?` adalah `Nullable(Of Integer)`: Integer yang",
                    "boleh bernilai Nothing. Untuk tipe NILAI, tanda tanya",
                    "itu wajib; tipe referensi sudah boleh Nothing sejak awal.",
                ]
            },
        ],
    },
    {
        "title": "13. LINQ & Lambda",
        "sections": [
            {
                "body": [
                    "LINQ tersedia penuh di VB, dan sintaks QUERY-nya justru",
                    "lebih lengkap daripada di C#.",
                    "",
                    "  Imports System.Linq",
                    "",
                    "DUA BENTUK yang hasilnya identik:",
                    "",
                    "  ' Query syntax",
                    "  Dim lulus = From m In murid",
                    "              Where m.Nilai >= 75",
                    "              Order By m.Nilai Descending",
                    "              Select m.Nama",
                    "",
                    "  ' Method syntax",
                    "  Dim lulus = murid.Where(Function(m) m.Nilai >= 75).",
                    "                    OrderByDescending(Function(m) m.Nilai).",
                    "                    Select(Function(m) m.Nama)",
                    "",
                    "Kata kunci query VB: From, Where, Select, Order By,",
                    "Group By, Join, Let, Distinct, Take, Skip, Aggregate.",
                    "",
                    "`Aggregate` adalah kata kunci yang TIDAK ADA di C#, dan",
                    "ia membuat perhitungan ringkasan bisa ditulis sebagai",
                    "query:",
                    "",
                    "  Dim total = Aggregate m In murid Into Sum(m.Nilai)",
                    "  Dim rata = Aggregate m In murid Into Average(m.Nilai)",
                    "",
                    "LAMBDA di VB ditulis dengan `Function` atau `Sub`:",
                    "",
                    "  Function(x) x * x                satu ekspresi",
                    "  Sub(x) Console.WriteLine(x)      tanpa kembalian",
                    "",
                    "  Function(x As Integer) As Integer",
                    "      Dim h = x * x",
                    "      Return h",
                    "  End Function",
                    "",
                    "Bentuk multi-baris memerlukan `End Function` — lebih",
                    "panjang daripada C#, tapi lebih jelas batasnya.",
                    "",
                    "TIPE DELEGATE:",
                    "  Func(Of Integer, Integer)         (Int) -> Int",
                    "  Func(Of Integer, Integer, Integer)",
                    "  Action(Of String)                 tanpa kembalian",
                    "  Predicate(Of Integer)             -> Boolean",
                    "",
                    "Di `Func(Of ...)`, tipe TERAKHIR adalah kembaliannya.",
                    "",
                    "DEFERRED EXECUTION berlaku sama seperti di C#: query",
                    "baru dijalankan saat ditelusuri, bukan saat ditulis.",
                    "Panggil `.ToList()` untuk membekukan hasilnya.",
                ]
            },
            {
                "heading": "LINQ pada data nyata",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Globalization
Imports System.Linq

Class Murid
    Public Property Nama As String
    Public Property Kelas As String
    Public Property Nilai As Integer

    Public Sub New(nama As String, kelas As String, nilai As Integer)
        Me.Nama = nama
        Me.Kelas = kelas
        Me.Nilai = nilai
    End Sub
End Class

Module Program

    Sub Main()
        Dim data As New List(Of Murid) From {
            New Murid("Andi", "A", 88),
            New Murid("Budi", "B", 72),
            New Murid("Cici", "A", 95),
            New Murid("Dedi", "B", 64),
            New Murid("Euis", "A", 79),
            New Murid("Fajar", "B", 91)
        }

        Console.WriteLine("-- Lulus, nilai tertinggi dulu --")
        Dim lulus = From m In data
                    Where m.Nilai >= 75
                    Order By m.Nilai Descending
                    Select m

        For Each m As Murid In lulus
            Console.WriteLine($"  {m.Nama,-6}{m.Kelas} {m.Nilai}")
        Next

        Console.WriteLine("---")
        Console.WriteLine($"rata-rata : {data.Average(Function(m) m.Nilai):F2}")
        Console.WriteLine($"tertinggi : {data.Max(Function(m) m.Nilai)}")
        ' List(Of T) punya PROPERTY Count, yang MENUTUPI extension Count(...)
        ' dari LINQ. Menulis data.Count(...) membuat VB mengira itu
        ' pengindeksan properti, bukan pemanggilan method.
        Console.WriteLine($"lulus     : {data.Where(Function(m) m.Nilai >= 75).Count}")
        Console.WriteLine($"ada <65?  : {data.Any(Function(m) m.Nilai < 65)}")
        Console.WriteLine($"semua >60?: {data.All(Function(m) m.Nilai > 60)}")

        Console.WriteLine("---")
        Console.WriteLine("-- Per kelas --")
        Dim perKelas = From m In data
                       Group m By kelas = m.Kelas Into Grup = Group
                       Order By kelas
                       Select kelas, Jumlah = Grup.Count,
                              Rata = Grup.Average(Function(x) x.Nilai)

        For Each g In perKelas
            Console.WriteLine($"  Kelas {g.kelas}: {g.Jumlah} murid, rata-rata {g.Rata:F1}")
        Next

        Console.WriteLine("---")
        ' Aggregate: kata kunci yang tidak ada di C#
        Dim total = Aggregate m In data Into Sum(m.Nilai)
        Console.WriteLine($"total nilai : {total}")

        Console.WriteLine("---")
        ' Lambda disimpan di dalam Dictionary
        Dim operasi As New Dictionary(Of String, Func(Of Integer, Integer, Integer)) From {
            {"tambah", Function(a, b) a + b},
            {"kurang", Function(a, b) a - b},
            {"kali", Function(a, b) a * b}
        }

        For Each pasangan In operasi
            Console.WriteLine($"{pasangan.Key,-7}(9, 4) = {pasangan.Value(9, 4)}")
        Next
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  -- Lulus, nilai tertinggi dulu --",
                    "    Cici  A 95",
                    "    Fajar B 91",
                    "    Andi  A 88",
                    "    Euis  A 79",
                    "  ---",
                    "  rata-rata : 81.50",
                    "  tertinggi : 95",
                    "  lulus     : 4",
                    "  ada <65?  : True",
                    "  semua >60?: True",
                    "  ---",
                    "  -- Per kelas --",
                    "    Kelas A: 3 murid, rata-rata 87.3",
                    "    Kelas B: 3 murid, rata-rata 75.7",
                    "  ---",
                    "  total nilai : 489",
                    "  ---",
                    "  tambah (9, 4) = 13",
                    "  kurang (9, 4) = 5",
                    "  kali   (9, 4) = 36",
                    "",
                    "`Group m By kelas = m.Kelas Into Grup = Group` adalah",
                    "bentuk pengelompokan VB. Kata `Group` di ujung adalah",
                    "kata kunci yang berarti 'seluruh anggota kelompok ini'.",
                    "",
                    "Hasil `Select kelas, Jumlah = ..., Rata = ...` adalah",
                    "TIPE ANONIM: sebuah class yang dibuatkan compiler",
                    "dengan properti persis seperti yang kamu sebutkan.",
                    "Itu sebabnya `g.Jumlah` dan `g.Rata` langsung bisa",
                    "dipakai tanpa mendeklarasikan class apa pun.",
                    "",
                    "Perhatikan `Dim perKelas = ...` TANPA `As`. Itu",
                    "inferensi tipe, dan ia WAJIB di sini: tipe anonim tidak",
                    "punya nama yang bisa kamu tulis. Inferensi aktif kalau",
                    "`Option Infer On`, yang merupakan bawaan di proyek baru.",
                    "",
                    "SATU JEBAKAN VB yang tidak ada di C#: `List(Of T)` punya",
                    "PROPERTY bernama `Count`, dan property itu MENUTUPI",
                    "extension method `Count(predikat)` dari LINQ. Menulis",
                    "`data.Count(Function(m) ...)` membuat VB mengira kamu",
                    "sedang MENGINDEKS properti Count, dan pesannya berbunyi",
                    "\"its return type cannot be indexed\" -- yang sama sekali",
                    "tidak menyebut LINQ. Jalan keluarnya: saring dulu, lalu",
                    "baca propertinya: `data.Where(...).Count`.",
                    "",
                    "`pasangan.Value(9, 4)` memanggil delegate yang tersimpan",
                    "di Dictionary. Di VB, memanggil delegate memakai kurung",
                    "biasa — sama seperti mengindeks array, karena keduanya",
                    "memang memakai tanda yang sama.",
                ]
            },
        ],
    },
    {
        "title": "14. Berkas, Data & Using",
        "sections": [
            {
                "body": [
                    "VB memakai pustaka .NET yang sama dengan C#:",
                    "",
                    "  Imports System.IO",
                    "",
                    "  File.WriteAllText(path, isi)",
                    "  File.AppendAllText(path, isi)",
                    "  File.ReadAllText(path)",
                    "  File.ReadAllLines(path)",
                    "  File.WriteAllLines(path, baris)",
                    "  File.ReadLines(path)       baca MALAS, hemat memori",
                    "",
                    "  File.Exists(path)  File.Delete(path)",
                    "  File.Copy(a, b, True)  File.Move(a, b)",
                    "  Directory.CreateDirectory(path)",
                    "  Directory.GetFiles(path, \"*.txt\")",
                    "",
                    "Menyusun path lintas sistem:",
                    "  Path.Combine(folder, \"data\", \"murid.txt\")",
                    "  Path.GetFileName / GetExtension / GetDirectoryName",
                    "  Path.GetTempPath()",
                    "",
                    "JANGAN menyambung path dengan garis miring sendiri.",
                    "Pemisahnya berbeda antar sistem operasi.",
                    "",
                    "USING melepas sumber daya secara otomatis:",
                    "",
                    "  Using penulis As New StreamWriter(path)",
                    "      penulis.WriteLine(\"baris\")",
                    "  End Using          ' ditutup di sini, GAGAL ATAU TIDAK",
                    "",
                    "Ia setara Try/Finally yang memanggil Dispose, dan ia",
                    "wajib dipakai untuk apa pun yang memegang berkas,",
                    "koneksi, atau soket. Satu exception di tengah tanpa",
                    "Using membuat berkasnya tidak pernah tertutup.",
                    "",
                    "Satu `Using` boleh memuat beberapa sumber daya:",
                    "  Using a As New StreamReader(p1),",
                    "        b As New StreamWriter(p2)",
                    "",
                    "NAMESPACE `My` adalah fitur KHAS VB yang tidak ada di",
                    "C#. Ia menyediakan jalan pintas ke hal-hal yang sering",
                    "dipakai:",
                    "",
                    "  My.Computer.FileSystem.ReadAllText(path)",
                    "  My.Computer.FileSystem.WriteAllText(path, isi, False)",
                    "  My.Application.Info.Version",
                    "  My.Settings.NamaSetelan",
                    "",
                    "`My` nyaman untuk skrip kecil dan aplikasi Windows Forms.",
                    "Untuk pustaka dan aplikasi lintas platform, pakai API",
                    ".NET biasa — ia lebih portabel dan lebih mudah dicari",
                    "contohnya, karena sama dengan yang dipakai C#.",
                    "",
                    "Untuk CSV sungguhan, jangan `Split(\",\")`: kolom yang",
                    "dikutip boleh memuat koma. VB menyediakan",
                    "`TextFieldParser` di namespace",
                    "`Microsoft.VisualBasic.FileIO`.",
                ]
            },
            {
                "heading": "Menulis, membaca, dan mengolah berkas",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Globalization
Imports System.IO
Imports System.Linq

Module Program

    Sub Main()
        Dim berkas As String = Path.Combine(Path.GetTempPath(), "belajar-vb.csv")

        ' --- Tulis dengan Using: ditutup apa pun yang terjadi ---
        Using penulis As New StreamWriter(berkas, append:=False)
            penulis.WriteLine("nama,kelas,nilai")
            penulis.WriteLine("Andi,A,88")
            penulis.WriteLine("Budi,B,72")
            penulis.WriteLine("Cici,A,95")
        End Using

        Console.WriteLine($"ditulis   : {Path.GetFileName(berkas)}")

        ' --- Baca kembali dan urai ---
        Dim baris() As String = File.ReadAllLines(berkas)
        Dim data = baris.Skip(1).
                         Select(Function(b) b.Split(","c)).
                         Select(Function(k) New With {
                             .Nama = k(0),
                             .Kelas = k(1),
                             .Nilai = CInt(k(2))
                         }).ToList()

        For Each m In data.OrderByDescending(Function(x) x.Nilai)
            Console.WriteLine($"  {m.Nama,-6}{m.Kelas} {m.Nilai,3}")
        Next

        Console.WriteLine($"rata-rata : {data.Average(Function(x) x.Nilai):F2}")

        Console.WriteLine("---")

        ' --- Baca baris demi baris, hemat memori ---
        Dim nomor As Integer = 0
        For Each b As String In File.ReadLines(berkas)
            nomor += 1
            Console.WriteLine($"{nomor,2}| {b}")
        Next

        Console.WriteLine("---")
        Console.WriteLine($"ukuran    : {New FileInfo(berkas).Length} byte")

        File.Delete(berkas)
        Console.WriteLine($"masih ada?: {File.Exists(berkas)}")

        Console.WriteLine("---")

        ' --- Menangani kegagalan berkas dengan jujur ---
        Try
            File.ReadAllText(Path.Combine(Path.GetTempPath(), "tidak-ada-xyz.txt"))
        Catch ex As FileNotFoundException
            Console.WriteLine("FileNotFoundException tertangkap")
        Catch ex As IOException
            Console.WriteLine($"IOException: {ex.Message}")
        End Try
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  ditulis   : belajar-vb.csv",
                    "    Cici  A  95",
                    "    Andi  A  88",
                    "    Budi  B  72",
                    "  rata-rata : 85.00",
                    "  ---",
                    "   1| nama,kelas,nilai",
                    "   2| Andi,A,88",
                    "   3| Budi,B,72",
                    "   4| Cici,A,95",
                    "  ---",
                    "  ukuran    : 47 byte",
                    "  masih ada?: False",
                    "  ---",
                    "  FileNotFoundException tertangkap",
                    "",
                    "`New With { .Nama = ..., .Kelas = ... }` membuat TIPE",
                    "ANONIM — class sekali pakai yang dibuatkan compiler.",
                    "Berguna persis di situasi seperti ini: bentuk datanya",
                    "cuma hidup di dalam satu prosedur.",
                    "",
                    "Perhatikan urutan Catch: `FileNotFoundException` ditulis",
                    "SEBELUM `IOException`. Yang pertama adalah turunan yang",
                    "kedua, jadi kalau dibalik ia tidak akan pernah tercapai",
                    "— dan compiler VB akan memperingatkanmu.",
                    "",
                    "`append:=False` memakai argumen bernama. Tanpa itu,",
                    "pembaca kode harus mengingat apa arti `False` di posisi",
                    "kedua — dan menebak salah berarti berkasnya ditimpa",
                    "padahal seharusnya ditambahi, atau sebaliknya.",
                    "",
                    "Ukuran 47 byte berlaku kalau berkasnya memakai akhiran",
                    "baris satu karakter. Di Windows, StreamWriter menulis",
                    "dua karakter per baris sehingga ukurannya berbeda —",
                    "salah satu hal yang perlu diingat saat membandingkan",
                    "berkas antar sistem operasi.",
                ]
            },
        ],
    },
    {
        "title": "15. Praktik Baik & Jebakan Umum",
        "sections": [
            {
                "body": [
                    "SAKLAR YANG WAJIB DINYALAKAN, di setiap proyek:",
                    "",
                    "  Option Strict On      tolak konversi diam-diam",
                    "  Option Explicit On    wajib deklarasikan variabel",
                    "  Option Infer On       boleh menyimpulkan tipe",
                    "",
                    "Yang pertama jauh lebih penting daripada dua lainnya.",
                    "Tanpa Option Strict, VB akan menerima hampir apa pun",
                    "dan menggagalkannya saat program jalan.",
                    "",
                    "Di berkas .vbproj:",
                    "  <OptionStrict>On</OptionStrict>",
                    "  <OptionExplicit>On</OptionExplicit>",
                    "  <OptionInfer>On</OptionInfer>",
                    "",
                    "JEBAKAN YANG PALING SERING:",
                    "",
                    "  1. `Dim a(4)` memberi LIMA elemen, bukan empat.",
                    "     Angkanya batas atas, bukan jumlah.",
                    "",
                    "  2. `For i = 1 To 5` menjalankan LIMA kali. Batasnya",
                    "     inklusif, berbeda dari `i < 5` di bahasa lain.",
                    "",
                    "  3. `And` dan `Or` TIDAK hubung-singkat. Pakai",
                    "     `AndAlso` dan `OrElse` untuk kondisi logika.",
                    "",
                    "  4. `= Nothing` bukan cara memeriksa objek kosong.",
                    "     Pakai `Is Nothing` dan `IsNot Nothing`.",
                    "",
                    "  5. `+` pada teks ambigu. Pakai `&` untuk menyambung.",
                    "",
                    "  6. Menugaskan ke NAMA FUNGSI (`Grade = \"A\"`) tidak",
                    "     menghentikan fungsinya. Pakai `Return`.",
                    "",
                    "  7. `On Error Resume Next` menelan setiap galat dan",
                    "     membiarkan program jalan dalam keadaan rusak.",
                    "",
                    "  8. Nama TIDAK membedakan huruf besar-kecil, jadi",
                    "     `nilai` dan `Nilai` adalah variabel yang SAMA.",
                    "     Kalau kamu bermaksud membedakan field dari",
                    "     property, pakai awalan garis bawah.",
                    "",
                    "PENAMAAN menurut kebiasaan .NET:",
                    "  PascalCase  class, method, property, event, konstanta",
                    "  camelCase   parameter dan variabel lokal",
                    "  _camelCase  field privat",
                    "  I di depan  interface",
                    "",
                    "Berbeda dari Java, konstanta memakai PascalCase",
                    "(MaksCoba), bukan huruf besar semua.",
                    "",
                    "Kebiasaan yang membuat kode VB enak dirawat:",
                    "  - Pulang lebih awal alih-alih If bertingkat.",
                    "  - Field `ReadOnly` kalau tidak pernah berubah sesudah",
                    "    constructor.",
                    "  - Kembalikan koleksi kosong, bukan Nothing.",
                    "  - Satu prosedur satu pekerjaan.",
                    "  - Nyalakan analyzer .NET dan naikkan peringatan jadi",
                    "    error di berkas proyek.",
                ]
            },
            {
                "heading": "Melihat jebakannya sendiri",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic

Module Program

    Function GayaLama(nilai As Integer) As String
        ' Gaya VB6: menugaskan ke nama fungsi TIDAK menghentikannya
        GayaLama = "A"
        If nilai < 85 Then GayaLama = "B"
        ' baris di bawah ini TETAP dijalankan
        If nilai < 75 Then GayaLama = "C"
    End Function

    Function GayaBaru(nilai As Integer) As String
        If nilai >= 85 Then Return "A"
        If nilai >= 75 Then Return "B"
        Return "C"
    End Function

    Sub Main()
        ' --- 1. Batas atas array, bukan jumlah ---
        Dim a(4) As Integer
        Console.WriteLine($"Dim a(4)      -> {a.Length} elemen (indeks 0..{UBound(a)})")

        ' --- 2. For inklusif ---
        Dim hitung As Integer = 0
        For i As Integer = 1 To 5
            hitung += 1
        Next
        Console.WriteLine($"For 1 To 5    -> {hitung} kali")

        Console.WriteLine("---")

        ' --- 3. AndAlso versus And ---
        Dim teks As String = Nothing
        Console.WriteLine($"AndAlso aman  : {teks IsNot Nothing AndAlso teks.Length > 0}")
        Try
            Console.WriteLine(teks IsNot Nothing And teks.Length > 0)
        Catch ex As NullReferenceException
            Console.WriteLine("And bahaya    : NullReferenceException")
        End Try

        Console.WriteLine("---")

        ' --- 4. Is Nothing, bukan = Nothing ---
        Console.WriteLine($"Is Nothing    : {teks Is Nothing}")

        ' --- 5. & versus + untuk teks ---
        Console.WriteLine("& selalu teks : " & "1" & 2)

        Console.WriteLine("---")

        ' --- 6. Gaya lama versus Return ---
        For Each n As Integer In New Integer() {92, 80, 70}
            Console.WriteLine($"{n,3}: lama={GayaLama(n)} baru={GayaBaru(n)}")
        Next

        Console.WriteLine("---")

        ' --- 8. Nama tidak membedakan huruf besar-kecil ---
        Dim nilai As Integer = 10
        NILAI = 20                       ' variabel yang SAMA
        Console.WriteLine($"nilai sesudah : {nilai}")

        Console.WriteLine("---")

        ' Kembalikan koleksi KOSONG, bukan Nothing
        Console.WriteLine($"kosong bukan Nothing: {Kosong().Count} elemen")
    End Sub

    Function Kosong() As List(Of String)
        Return New List(Of String)
    End Function

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Dim a(4)      -> 5 elemen (indeks 0..4)",
                    "  For 1 To 5    -> 5 kali",
                    "  ---",
                    "  AndAlso aman  : False",
                    "  And bahaya    : NullReferenceException",
                    "  ---",
                    "  Is Nothing    : True",
                    "  & selalu teks : 12",
                    "  ---",
                    "   92: lama=A baru=A",
                    "   80: lama=B baru=B",
                    "   70: lama=C baru=C",
                    "  ---",
                    "  nilai sesudah : 20",
                    "  ---",
                    "  kosong bukan Nothing: 0 elemen",
                    "",
                    "Fungsi `GayaLama` kebetulan memberi jawaban yang benar",
                    "di sini, dan itu justru yang berbahaya: ia bekerja",
                    "SAMPAI seseorang menambahkan satu baris di bawah tanpa",
                    "menyadari bahwa fungsinya belum berhenti. Bentuk",
                    "`Return` tidak punya masalah itu.",
                    "",
                    "Baris `NILAI = 20` mengubah variabel `nilai` yang sama.",
                    "VB tidak membedakan huruf besar-kecil, dan editor",
                    "biasanya merapikan ejaannya otomatis — tapi di kode",
                    "yang disunting lewat alat lain, dua ejaan yang berbeda",
                    "untuk satu variabel membingungkan pembacanya.",
                    "",
                    "`Kosong()` mengembalikan List kosong, bukan Nothing.",
                    "Pemanggilnya jadi bisa langsung `For Each` tanpa",
                    "memeriksa apa pun. Mengembalikan Nothing untuk koleksi",
                    "memaksa setiap pemanggil menulis pemeriksaan, dan satu",
                    "yang lupa menghasilkan NullReferenceException.",
                    "",
                    "Untuk memeriksa kualitas kode secara otomatis:",
                    "  dotnet build -warnaserror",
                    "  <EnableNETAnalyzers>true</EnableNETAnalyzers>",
                    "  <TreatWarningsAsErrors>true</TreatWarningsAsErrors>",
                ]
            },
        ],
    },
    {
        "title": "16. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan class, property,",
                    "enum, exception, LINQ, dan pemisahan tanggung jawab",
                    "dalam satu program utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang. Yang penting",
                    "bukan fiturnya melainkan CARA bagiannya dipisah.",
                    "",
                    "Tiga lapisan, panah ketergantungan satu arah:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  MODEL     Class Barang, Enum Gerak, dan keluarga",
                    "            exception-nya. Tidak tahu apa-apa tentang",
                    "            layar.",
                    "  LAYANAN   Class Gudang dengan seluruh aturannya. TIDAK",
                    "            PERNAH memanggil Console.",
                    "  ANTARMUKA Module Program: memanggil layanan, mencetak",
                    "            hasilnya. Tidak menghitung apa pun.",
                    "",
                    "Ujinya satu kalimat: kalau program ini diubah jadi",
                    "aplikasi web ASP.NET, berapa banyak kode yang harus",
                    "disentuh? Jawaban yang benar: hanya Module Program.",
                    "",
                    "Kesalahan yang paling sering di program VB pemula",
                    "adalah mencampur ketiganya — menghitung total di tengah",
                    "`Console.WriteLine`. Programnya jalan, dan tetap jalan",
                    "sampai hari ketika ada yang minta totalnya juga muncul",
                    "di laporan lain.",
                ]
            },
            {
                "heading": "Program lengkap",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Linq

' ---------------------------------------------------------------- MODEL
Public Enum Gerak
    Masuk
    Keluar
End Enum

Public Class Barang
    Public ReadOnly Property Kode As String
    Public ReadOnly Property Nama As String
    Public ReadOnly Property Harga As Long
    Public Property Stok As Integer

    Public Sub New(kode As String, nama As String, stok As Integer, harga As Long)
        Me.Kode = kode
        Me.Nama = nama
        Me.Stok = stok
        Me.Harga = harga
    End Sub

    Public ReadOnly Property Subtotal As Long
        Get
            Return Stok * Harga
        End Get
    End Property

    Public Overrides Function ToString() As String
        Return $"{Kode,-5}{Nama,-12}{Stok,2}{Harga,10}{Subtotal,12}"
    End Function
End Class

Public Class GudangException
    Inherits Exception

    Public Sub New(pesan As String)
        MyBase.New(pesan)
    End Sub
End Class

Public Class KodeSudahAdaException
    Inherits GudangException

    Public Sub New(kode As String)
        MyBase.New($"kode {kode} sudah ada")
    End Sub
End Class

Public Class KodeTidakDikenalException
    Inherits GudangException

    Public Sub New(kode As String)
        MyBase.New($"kode {kode} tidak dikenal")
    End Sub
End Class

Public Class JumlahTidakSahException
    Inherits GudangException

    Public Sub New(jumlah As Integer)
        MyBase.New($"jumlah {jumlah} tidak sah")
    End Sub
End Class

Public Class StokTidakCukupException
    Inherits GudangException

    Public Sub New(punya As Integer, diminta As Integer)
        MyBase.New($"stok cuma {punya}, diminta {diminta}")
    End Sub
End Class

' -------------------------------------------------------------- LAYANAN
Public Class Gudang

    Private ReadOnly _isi As New Dictionary(Of String, Barang)

    Public Sub Daftar(b As Barang)
        If _isi.ContainsKey(b.Kode) Then Throw New KodeSudahAdaException(b.Kode)
        _isi(b.Kode) = b
    End Sub

    Public Function Catat(kode As String, gerak As Gerak, jumlah As Integer) As Integer
        Dim b As Barang = Nothing
        If Not _isi.TryGetValue(kode, b) Then Throw New KodeTidakDikenalException(kode)
        If jumlah <= 0 Then Throw New JumlahTidakSahException(jumlah)

        Dim baru As Integer = If(gerak = Gerak.Masuk, b.Stok + jumlah, b.Stok - jumlah)
        If baru < 0 Then Throw New StokTidakCukupException(b.Stok, jumlah)

        b.Stok = baru
        Return baru
    End Function

    Public Function Semua() As List(Of Barang)
        Return _isi.Values.OrderBy(Function(b) b.Kode, StringComparer.Ordinal).ToList()
    End Function

    Public Function NilaiPersediaan() As Long
        Return _isi.Values.Sum(Function(b) b.Subtotal)
    End Function

    Public Function StokMenipis(batas As Integer) As List(Of Barang)
        Return _isi.Values.
            Where(Function(b) b.Stok < batas).
            OrderBy(Function(b) b.Stok).
            ThenBy(Function(b) b.Kode, StringComparer.Ordinal).ToList()
    End Function

End Class

' ------------------------------------------------------------ ANTARMUKA
Module Program

    Sub Main()
        Dim gudang As New Gudang()

        gudang.Daftar(New Barang("B01", "Kabel", 10, 15000))
        gudang.Daftar(New Barang("B02", "Adaptor", 4, 85000))
        gudang.Daftar(New Barang("B03", "Mouse", 25, 120000))

        Dim langkah = {
            Tuple.Create("B01", Gerak.Masuk, 15),
            Tuple.Create("B02", Gerak.Keluar, 10),
            Tuple.Create("B03", Gerak.Keluar, 5),
            Tuple.Create("B09", Gerak.Masuk, 1),
            Tuple.Create("B03", Gerak.Keluar, 0)
        }

        For Each l In langkah
            Dim label As String = $"{l.Item2} {l.Item1} {l.Item3}"
            Try
                Console.WriteLine($"{label} -> stok {gudang.Catat(l.Item1, l.Item2, l.Item3)}")
            Catch ex As GudangException
                Console.WriteLine($"{label} -> DITOLAK: {ex.Message}")
            End Try
        Next

        Console.WriteLine("---")
        For Each b As Barang In gudang.Semua()
            Console.WriteLine(b.ToString())
        Next

        Console.WriteLine("---")
        Console.WriteLine($"nilai persediaan: {gudang.NilaiPersediaan()}")

        Dim menipis = gudang.StokMenipis(10).
            Select(Function(b) $"{b.Kode} {b.Nama} ({b.Stok})")
        Console.WriteLine($"stok menipis (<10): {String.Join(", ", menipis)}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Empat keputusan yang layak ditiru:",
                    "",
                    "  1. Keluarga exception mewarisi satu induk",
                    "     `GudangException`. Antarmuka cukup menulis satu",
                    "     `Catch ex As GudangException` dan tetap mendapat",
                    "     pesan yang tepat untuk tiap kasus — sementara",
                    "     galat lain (bug sungguhan) tetap naik dan terlihat.",
                    "",
                    "  2. `Semua()` dan `StokMenipis()` MENGURUTKAN sebelum",
                    "     mengembalikan. Dictionary tidak menjamin urutan,",
                    "     dan keluaran yang urutannya tidak pasti mustahil",
                    "     diuji.",
                    "",
                    "  3. `Harga` dan `Kode` ReadOnly; hanya `Stok` yang",
                    "     boleh berubah, dan hanya lewat `Catat` yang sudah",
                    "     memvalidasi.",
                    "",
                    "  4. Gudang tidak memanggil Console sama sekali. Itu",
                    "     yang membuat seluruh aturannya bisa diuji tanpa",
                    "     membaca layar.",
                    "",
                    "`If Not _isi.TryGetValue(kode, b) Then` menggabungkan",
                    "pencarian dan pemeriksaan dalam satu langkah. Memeriksa",
                    "`ContainsKey` lalu mengambilnya berarti mencari dua kali",
                    "di tabel hash yang sama.",
                    "",
                    "Langkah berikutnya kalau kamu ingin melanjutkannya:",
                    "  - Simpan ke JSON dengan System.Text.Json.",
                    "  - Pisahkan penyimpanan di balik sebuah Interface,",
                    "    sehingga Gudang tidak tahu datanya di berkas, di",
                    "    database, atau cuma di memori saat tes.",
                    "  - Tambahkan menu interaktif dan penyaringan tanggal.",
                    "  - Tulis tes MSTest atau xUnit untuk Gudang —",
                    "    perhatikan ini langsung bisa dilakukan tanpa",
                    "    mengubah satu baris pun, justru karena keputusan",
                    "    nomor 4.",
                ]
            },
        ],
    },
]
