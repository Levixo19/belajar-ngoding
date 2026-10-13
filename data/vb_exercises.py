VB_EXERCISES = [
    {
        "title": "Latihan 1: Perkenalan Diri",
        "difficulty": "Mudah",
        "question": [
            "Buat program VB.NET yang menampilkan tepat tiga baris.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar Visual Basic .NET.",
            "  VB.NET dan C# berjalan di runtime yang sama.",
        ],
        "hints": [
            "Kerangkanya: Module Program / Sub Main() / End Sub / End Module",
            "Console.WriteLine mencetak lalu pindah baris.",
            "Tulis Option Strict On di baris pertama sebagai kebiasaan.",
        ],
        "solution": """Option Strict On

Imports System

Module Program

    Sub Main()
        Console.WriteLine("Halo, namaku Andi!")
        Console.WriteLine("Aku sedang belajar Visual Basic .NET.")
        Console.WriteLine("VB.NET dan C# berjalan di runtime yang sama.")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 2: Kalkulator Dua Bilangan",
        "difficulty": "Mudah",
        "question": [
            "Buat dua variabel a = 17 dan b = 5, lalu tampilkan:",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  17 + 5 = 22",
            "  17 - 5 = 12",
            "  17 * 5 = 85",
            "  17 / 5 = 3.4",
            "  17 \\ 5 = 3",
            "  17 Mod 5 = 2",
            "  17 ^ 2 = 289",
        ],
        "hints": [
            "VB punya DUA pembagian: / menghasilkan pecahan, \\ bilangan bulat.",
            "Mod memberi sisa bagi, ^ memberi pangkat.",
            "Interpolasi: Console.WriteLine($\"{a} + {b} = {a + b}\")",
            "Backslash di dalam string interpolasi tidak perlu diapa-apakan.",
        ],
        "solution": """Option Strict On

Imports System

Module Program

    Sub Main()
        Dim a As Integer = 17
        Dim b As Integer = 5

        Console.WriteLine($"{a} + {b} = {a + b}")
        Console.WriteLine($"{a} - {b} = {a - b}")
        Console.WriteLine($"{a} * {b} = {a * b}")
        Console.WriteLine($"{a} / {b} = {a / b}")
        Console.WriteLine($"{a} \\ {b} = {a \\ b}")
        Console.WriteLine($"{a} Mod {b} = {a Mod b}")
        Console.WriteLine($"{a} ^ 2 = {a ^ 2}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 3: Konversi Suhu",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka suhu Celsius dari input.",
            "Tampilkan konversinya ke Fahrenheit dan Kelvin.",
            "",
            "Rumus:",
            "  F = C * 9 / 5 + 32",
            "  K = C + 273.15",
            "",
            "Untuk input 25, keluaran yang diharapkan:",
            "",
            "  Celsius    : 25.00",
            "  Fahrenheit : 77.00",
            "  Kelvin     : 298.15",
        ],
        "hints": [
            "Console.ReadLine() membaca satu baris sebagai String.",
            "Ubah ke Double dengan CDbl atau Double.Parse.",
            "Karena Option Strict On, konversinya WAJIB ditulis.",
            "Dua desimal: {c:F2} di dalam interpolasi.",
            "Jangan mencetak apa pun sebelum membaca input.",
        ],
        "stdin": "25\n",
        "solution": """Option Strict On

Imports System
Imports System.Globalization

Module Program

    Sub Main()
        Dim baris As String = Console.ReadLine()
        Dim c As Double = Double.Parse(baris.Trim(), CultureInfo.InvariantCulture)

        Dim f As Double = c * 9 / 5 + 32
        Dim k As Double = c + 273.15

        Console.WriteLine($"Celsius    : {c:F2}")
        Console.WriteLine($"Fahrenheit : {f:F2}")
        Console.WriteLine($"Kelvin     : {k:F2}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 4: Grade & Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka nilai (0-100) dari input.",
            "Tampilkan grade memakai Select Case dengan RENTANG:",
            "  >= 85 : A, 75-84 : B, 60-74 : C, 40-59 : D, sisanya E",
            "",
            "Lalu tampilkan status Lulus kalau nilai >= 75.",
            "",
            "Untuk input 78, keluaran yang diharapkan:",
            "",
            "  Grade: B",
            "  Status: Lulus",
        ],
        "hints": [
            "Select Case menerima rentang: Case 75 To 84",
            "Juga menerima perbandingan: Case Is >= 85",
            "Case Else menangkap sisanya.",
            "If(syarat, a, b) adalah operator ternary di VB.",
        ],
        "stdin_list": ["92\n", "78\n", "65\n", "45\n", "12\n"],
        "solution": """Option Strict On

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

    Sub Main()
        Dim nilai As Integer = CInt(Console.ReadLine().Trim())

        Console.WriteLine($"Grade: {Grade(nilai)}")
        Console.WriteLine($"Status: {If(nilai >= 75, "Lulus", "Tidak Lulus")}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 5: Tabel Perkalian",
        "difficulty": "Mudah",
        "question": [
            "Tampilkan tabel perkalian 1 sampai 5.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  1 x 1 =  1   1 x 2 =  2   1 x 3 =  3   1 x 4 =  4   1 x 5 =  5",
            "  2 x 1 =  2   2 x 2 =  4   2 x 3 =  6   2 x 4 =  8   2 x 5 = 10",
            "  3 x 1 =  3   3 x 2 =  6   3 x 3 =  9   3 x 4 = 12   3 x 5 = 15",
            "  4 x 1 =  4   4 x 2 =  8   4 x 3 = 12   4 x 4 = 16   4 x 5 = 20",
            "  5 x 1 =  5   5 x 2 = 10   5 x 3 = 15   5 x 4 = 20   5 x 5 = 25",
            "",
            "Tiap baris diawali dua spasi. Hasil perkaliannya rata kanan",
            "selebar 2 karakter, dan tiap sel dipisah tiga spasi.",
        ],
        "hints": [
            "Dua For bersarang; batas For di VB INKLUSIF.",
            "Console.Write mencetak tanpa pindah baris.",
            "Rata kanan selebar 2: {b * k,2} di dalam interpolasi.",
            "Pemisah ditulis sesudah tiap sel kecuali yang terakhir.",
        ],
        "solution": """Option Strict On

Imports System

Module Program

    Sub Main()
        For b As Integer = 1 To 5
            Console.Write("  ")
            For k As Integer = 1 To 5
                Console.Write($"{b} x {k} = {b * k,2}")
                If k < 5 Then Console.Write("   ")
            Next
            Console.WriteLine()
        Next
    End Sub

End Module""",
    },
    {
        "title": "Latihan 6: Statistik Nilai",
        "difficulty": "Menengah",
        "question": [
            "Diberikan array nilai berikut di dalam kodemu:",
            "  78, 92, 65, 88, 71, 95, 59, 83",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
            "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
            "  Jumlah    : 8",
            "  Total     : 631",
            "  Rata-rata : 78.88",
            "  Tertinggi : 95",
            "  Terendah  : 59",
            "  Di atas rata-rata: 4",
        ],
        "hints": [
            "String.Join(\", \", arr) menggabungkan array jadi teks.",
            "Array.Sort MENGUBAH array aslinya: salin dulu dengan Clone.",
            "CType(nilai.Clone(), Integer()) karena Clone mengembalikan Object.",
            "Rata-rata: CDbl(total) / nilai.Length supaya bukan pembagian bulat.",
        ],
        "solution": """Option Strict On

Imports System

Module Program

    Sub Main()
        Dim nilai() As Integer = {78, 92, 65, 88, 71, 95, 59, 83}

        Dim total As Integer = 0
        Dim tertinggi As Integer = nilai(0)
        Dim terendah As Integer = nilai(0)

        For Each n As Integer In nilai
            total += n
            If n > tertinggi Then tertinggi = n
            If n < terendah Then terendah = n
        Next

        Dim rata As Double = CDbl(total) / nilai.Length

        Dim diAtas As Integer = 0
        For Each n As Integer In nilai
            If n > rata Then diAtas += 1
        Next

        Dim urut() As Integer = CType(nilai.Clone(), Integer())
        Array.Sort(urut)

        Console.WriteLine($"Data      : {String.Join(", ", nilai)}")
        Console.WriteLine($"Terurut   : {String.Join(", ", urut)}")
        Console.WriteLine($"Jumlah    : {nilai.Length}")
        Console.WriteLine($"Total     : {total}")
        Console.WriteLine($"Rata-rata : {rata:F2}")
        Console.WriteLine($"Tertinggi : {tertinggi}")
        Console.WriteLine($"Terendah  : {terendah}")
        Console.WriteLine($"Di atas rata-rata: {diAtas}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 7: Balik Teks & Palindrom",
        "difficulty": "Menengah",
        "question": [
            "Baca satu baris teks dari input, lalu tampilkan:",
            "  Asli    : teks aslinya",
            "  Dibalik : teksnya dibalik",
            "  Huruf   : jumlah huruf tanpa spasi",
            "  Palindrom: ya / bukan (abaikan spasi dan besar-kecil huruf)",
            "",
            "Untuk input 'Kasur ini rusak', keluaran yang diharapkan:",
            "",
            "  Asli    : Kasur ini rusak",
            "  Dibalik : kasur ini rusaK",
            "  Huruf   : 13",
            "  Palindrom: ya",
        ],
        "hints": [
            "Membalik: ubah ke Char(), Array.Reverse, lalu New String(...)",
            "Replace(\" \", \"\") membuang spasi.",
            "ToLowerInvariant() untuk mengabaikan besar-kecil huruf.",
            "Jangan mencetak apa pun sebelum Console.ReadLine() pertama.",
        ],
        "stdin_list": ["Kasur ini rusak\n", "Belajar Visual Basic\n", "Ini\n"],
        "solution": """Option Strict On

Imports System

Module Program

    Function Balik(s As String) As String
        Dim huruf() As Char = s.ToCharArray()
        Array.Reverse(huruf)
        Return New String(huruf)
    End Function

    Sub Main()
        Dim teks As String = Console.ReadLine()

        Dim rapat As String = teks.Replace(" ", "")
        Dim bersih As String = rapat.ToLowerInvariant()
        Dim palindrom As Boolean = (bersih = Balik(bersih))

        Console.WriteLine($"Asli    : {teks}")
        Console.WriteLine($"Dibalik : {Balik(teks)}")
        Console.WriteLine($"Huruf   : {rapat.Length}")
        Console.WriteLine($"Palindrom: {If(palindrom, "ya", "bukan")}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 8: Menghitung Frekuensi Kata",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat berikut di dalam kodemu:",
            "  \"kucing makan ikan kucing tidur ikan kucing\"",
            "",
            "Hitung frekuensi tiap kata memakai Dictionary, lalu tampilkan",
            "terurut dari yang paling sering. Kalau sama, urutkan abjad.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  kucing : 3",
            "  ikan   : 2",
            "  makan  : 1",
            "  tidur  : 1",
            "  ---",
            "  Kata unik  : 4",
            "  Total kata : 7",
            "",
            "Nama kata rata kiri selebar 7 karakter.",
        ],
        "hints": [
            "Split(\" \"c) memecah kalimat; akhiran c membuatnya literal Char.",
            "TryGetValue mengisi 0 untuk kunci yang belum ada.",
            "OrderByDescending lalu ThenBy untuk dua kunci urutan.",
            "Rata kiri: {kata,-7} di dalam interpolasi.",
        ],
        "solution": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Linq

Module Program

    Sub Main()
        Dim kalimat As String = "kucing makan ikan kucing tidur ikan kucing"
        Dim kata() As String = kalimat.Split(" "c)

        Dim hitung As New Dictionary(Of String, Integer)
        For Each k As String In kata
            Dim n As Integer
            hitung.TryGetValue(k, n)
            hitung(k) = n + 1
        Next

        For Each p In hitung.OrderByDescending(Function(x) x.Value).
                             ThenBy(Function(x) x.Key, StringComparer.Ordinal)
            Console.WriteLine($"{p.Key,-7}: {p.Value}")
        Next

        Console.WriteLine("---")
        Console.WriteLine($"Kata unik  : {hitung.Count}")
        Console.WriteLine($"Total kata : {kata.Length}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 9: Class Murid dengan Validasi",
        "difficulty": "Menengah",
        "question": [
            "Buat Class Murid dengan:",
            "  - ReadOnly Property Nama",
            "  - Property Nilai yang MENOLAK di luar 0..100 dengan",
            "    ArgumentOutOfRangeException",
            "  - ReadOnly Property Grade: >=85 A, >=75 B, >=60 C, sisanya D",
            "  - Overrides ToString berbentuk \"Andi     92 A\"",
            "    (nama rata kiri 8, nilai rata kanan 3, spasi, grade)",
            "",
            "Buat tiga murid: Andi 92, Budi 78, Cici 64. Cetak ketiganya,",
            "lalu coba mengisi nilai Andi dengan 150 dan tangkap galatnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Andi     92 A",
            "  Budi     78 B",
            "  Cici     64 C",
            "  Ditolak: nilai di luar 0..100",
        ],
        "hints": [
            "Property dengan validasi butuh bentuk panjang: Get / Set(value).",
            "Di constructor, isi lewat PROPERTY supaya validasinya ikut jalan.",
            "Select Case atau If berantai untuk Grade.",
            "ex.Message.Split(vbLf)(0) mengambil baris pertama pesannya.",
        ],
        "solution": """Option Strict On

Imports System

Class Murid

    Private _nilai As Integer

    Public ReadOnly Property Nama As String

    Public Property Nilai As Integer
        Get
            Return _nilai
        End Get
        Set(value As Integer)
            If value < 0 OrElse value > 100 Then
                Throw New ArgumentOutOfRangeException(NameOf(value),
                                                      "nilai di luar 0..100")
            End If
            _nilai = value
        End Set
    End Property

    Public ReadOnly Property Grade As String
        Get
            Select Case _nilai
                Case Is >= 85 : Return "A"
                Case Is >= 75 : Return "B"
                Case Is >= 60 : Return "C"
                Case Else : Return "D"
            End Select
        End Get
    End Property

    Public Sub New(nama As String, nilai As Integer)
        Me.Nama = nama
        Me.Nilai = nilai
    End Sub

    Public Overrides Function ToString() As String
        Return $"{Nama,-8}{Nilai,3} {Grade}"
    End Function

End Class

Module Program

    Sub Main()
        Dim kelas() As Murid = {
            New Murid("Andi", 92),
            New Murid("Budi", 78),
            New Murid("Cici", 64)
        }

        For Each m As Murid In kelas
            Console.WriteLine(m.ToString())
        Next

        Try
            kelas(0).Nilai = 150
        Catch ex As ArgumentOutOfRangeException
            Console.WriteLine($"Ditolak: {ex.Message.Split(vbLf)(0)}")
        End Try
    End Sub

End Module""",
    },
    {
        "title": "Latihan 10: Interface & Polimorfisme",
        "difficulty": "Lanjut",
        "question": [
            "Buat Interface IBangun dengan ReadOnly Property Nama dan",
            "Function Luas() As Double.",
            "",
            "Buat MustInherit Class BangunDasar yang mengimplementasinya,",
            "menyimpan namanya, dan punya Overridable Function Ringkas()",
            "berformat \"{Nama,-16}{Luas(),8:F2}\".",
            "",
            "Turunkan Persegi(sisi), Lingkaran(jari) dengan PI = 3.14159",
            "yang MENIMPA Ringkas menjadi \"<bawaan>  (r=<jari>)\",",
            "dan PersegiPanjang(p, l).",
            "",
            "Masukkan Persegi(4), Lingkaran(3), PersegiPanjang(6, 3) ke satu",
            "List(Of IBangun), telusuri sekali, lalu cetak totalnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Persegi            16.00",
            "  Lingkaran          28.27  (r=3)",
            "  PersegiPanjang     18.00",
            "  TOTAL              62.27",
        ],
        "hints": [
            "Tiap anggota WAJIB menyebut Implements IBangun.NamaAnggota.",
            "MyBase.New(...) memanggil constructor induk.",
            "MyBase.Ringkas() memanggil versi induk dari method yang ditimpa.",
            "CType(b, BangunDasar).Ringkas() untuk memanggil method turunannya.",
        ],
        "solution": """Option Strict On

Imports System
Imports System.Collections.Generic

Interface IBangun
    ReadOnly Property Nama As String
    Function Luas() As Double
End Interface

MustInherit Class BangunDasar
    Implements IBangun

    Public ReadOnly Property Nama As String Implements IBangun.Nama

    Protected Sub New(nama As String)
        Me.Nama = nama
    End Sub

    Public MustOverride Function Luas() As Double Implements IBangun.Luas

    Public Overridable Function Ringkas() As String
        Return $"{Nama,-16}{Luas(),8:F2}"
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

    Public Overrides Function Ringkas() As String
        Return MyBase.Ringkas() & $"  (r={_jari})"
    End Function
End Class

Class PersegiPanjang
    Inherits BangunDasar

    Private ReadOnly _p As Double
    Private ReadOnly _l As Double

    Public Sub New(p As Double, l As Double)
        MyBase.New("PersegiPanjang")
        _p = p
        _l = l
    End Sub

    Public Overrides Function Luas() As Double
        Return _p * _l
    End Function
End Class

Module Program

    Sub Main()
        Dim semua As New List(Of IBangun) From {
            New Persegi(4),
            New Lingkaran(3),
            New PersegiPanjang(6, 3)
        }

        Dim total As Double = 0
        For Each b As IBangun In semua
            Console.WriteLine(CType(b, BangunDasar).Ringkas())
            total += b.Luas()
        Next

        Console.WriteLine($"{"TOTAL",-16}{total,8:F2}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 11: Enum, Flags & Structure",
        "difficulty": "Lanjut",
        "question": [
            "Buat Structure Titik dengan X dan Y ReadOnly, constructor,",
            "Function Jarak(), dan ToString berbentuk \"(3, 4)\".",
            "",
            "Buat Enum Status { Draf, Ditinjau, Disetujui, Terbit } dan",
            "Enum ber-<Flags> Izin { Tidak=0, Baca=1, Tulis=2, Hapus=4,",
            "Jalan=8, Penuh=gabungan keempatnya }.",
            "",
            "Tunjukkan berurutan:",
            "  1. Structure DISALIN isinya, Class disalin alamatnya",
            "  2. Enum: nama, angka, konversi dari angka, IsDefined",
            "  3. Flags: gabung, HasFlag, tambah, buang",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  structure : s1=(1, 2) s2=(1, 2) jarak=2.236",
            "  class     : c1.X=99 c2.X=99",
            "  ---",
            "  nama      : Ditinjau",
            "  angka     : 1",
            "  dari 3    : Terbit",
            "  sah 9?    : False",
            "  ---",
            "  editor    : Baca, Tulis = 3",
            "  boleh hapus? False",
            "  +hapus    : Baca, Tulis, Hapus",
            "  -baca     : Tulis, Hapus",
            "  penuh     : Penuh = 15",
        ],
        "hints": [
            "Structure tidak bisa punya constructor tanpa parameter.",
            "[Enum].IsDefined(GetType(Status), 9) — kurung siku karena Enum "
            "adalah kata kunci VB.",
            "Gabung izin dengan Or; buang dengan And Not.",
            "Jarak: Math.Sqrt(X * X + Y * Y), cetak dengan format F3.",
        ],
        "solution": """Option Strict On

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
        Dim s1 As New Titik(1, 2)
        Dim s2 As Titik = s1
        Console.WriteLine($"structure : s1={s1} s2={s2} jarak={s1.Jarak():F3}")

        Dim c1 As New TitikKelas With {.X = 1, .Y = 2}
        Dim c2 As TitikKelas = c1
        c2.X = 99
        Console.WriteLine($"class     : c1.X={c1.X} c2.X={c2.X}")

        Console.WriteLine("---")
        Dim st As Status = Status.Ditinjau
        Console.WriteLine($"nama      : {st}")
        Console.WriteLine($"angka     : {CInt(st)}")
        Console.WriteLine($"dari 3    : {CType(3, Status)}")
        Console.WriteLine($"sah 9?    : {[Enum].IsDefined(GetType(Status), 9)}")

        Console.WriteLine("---")
        Dim editor As Izin = Izin.Baca Or Izin.Tulis
        Console.WriteLine($"editor    : {editor} = {CInt(editor)}")
        Console.WriteLine($"boleh hapus? {editor.HasFlag(Izin.Hapus)}")

        editor = editor Or Izin.Hapus
        Console.WriteLine($"+hapus    : {editor}")

        editor = editor And Not Izin.Baca
        Console.WriteLine($"-baca     : {editor}")
        Console.WriteLine($"penuh     : {Izin.Penuh} = {CInt(Izin.Penuh)}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 12: Exception Sendiri",
        "difficulty": "Lanjut",
        "question": [
            "Buat Class SaldoKurangException yang mewarisi Exception,",
            "menyimpan ReadOnly Property Kurang (Long), dengan pesan",
            "\"saldo kurang <n>\".",
            "",
            "Buat Class Dompet dengan saldo awal dan Sub Bayar(jumlah):",
            "  - jumlah <= 0 -> ArgumentOutOfRangeException",
            "  - jumlah > saldo -> SaldoKurangException",
            "  - selain itu saldo berkurang",
            "",
            "Mulai saldo 50000, bayar berurutan 20000, -5, 100000, 30000.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  bayar   20000 -> sisa 30000",
            "  bayar      -5 -> DITOLAK: jumlah tidak sah",
            "  bayar  100000 -> GAGAL, kurang 70000",
            "  bayar   30000 -> sisa 0",
            "",
            "Angka tagihan dicetak rata kanan selebar 7.",
        ],
        "hints": [
            "Exception sendiri: Inherits Exception lalu MyBase.New(pesan).",
            "Tangkap yang PALING SPESIFIK lebih dulu.",
            "Property saldo sebaiknya ReadOnly dari luar.",
            "Rata kanan: {tagihan,7} di dalam interpolasi.",
        ],
        "solution": """Option Strict On

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
            Throw New ArgumentOutOfRangeException(NameOf(jumlah))
        End If
        If jumlah > _saldo Then
            Throw New SaldoKurangException(jumlah - _saldo)
        End If
        _saldo -= jumlah
    End Sub
End Class

Module Program

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
    End Sub

End Module""",
    },
    {
        "title": "Latihan 13: LINQ & Laporan Penjualan",
        "difficulty": "Lanjut",
        "question": [
            "Buat Class Transaksi dengan Barang, Kategori, Jumlah, Harga,",
            "dan ReadOnly Property Subtotal.",
            "",
            "Isi dengan:",
            "  Kopi  Minuman  3  25000",
            "  Teh   Minuman  5  15000",
            "  Roti  Makanan  2  20000",
            "  Nasi  Makanan  4  30000",
            "  Jus   Minuman  1  35000",
            "",
            "Dengan LINQ, tampilkan semua transaksi terurut subtotal",
            "MENURUN; kalau sama, nama barang MENAIK. Lalu total, rekap",
            "per kategori terurut abjad, dan barang termahal.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Nasi       Makanan     4 x  30000 =   120000",
            "  Kopi       Minuman     3 x  25000 =    75000",
            "  Teh        Minuman     5 x  15000 =    75000",
            "  Roti       Makanan     2 x  20000 =    40000",
            "  Jus        Minuman     1 x  35000 =    35000",
            "  ---",
            "  Total     : 345000",
            "  Makanan   : 160000 (2 transaksi)",
            "  Minuman   : 185000 (3 transaksi)",
            "  Termahal  : Nasi",
            "",
            "Kolom: barang rata kiri 11, kategori rata kiri 11, jumlah rata",
            "kanan 2, harga rata kanan 6, subtotal rata kanan 8.",
        ],
        "hints": [
            "OrderByDescending lalu ThenBy untuk dua kunci urutan.",
            "GroupBy(Function(t) t.Kategori) lalu OrderBy kuncinya.",
            "Ingat jebakan: pakai Grup.Count TANPA kurung, bukan Count().",
            "First() sesudah OrderByDescending untuk mencari yang termahal.",
        ],
        "solution": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Linq

Class Transaksi
    Public ReadOnly Property Barang As String
    Public ReadOnly Property Kategori As String
    Public ReadOnly Property Jumlah As Integer
    Public ReadOnly Property Harga As Integer

    Public Sub New(barang As String, kategori As String,
                   jumlah As Integer, harga As Integer)
        Me.Barang = barang
        Me.Kategori = kategori
        Me.Jumlah = jumlah
        Me.Harga = harga
    End Sub

    Public ReadOnly Property Subtotal As Integer
        Get
            Return Jumlah * Harga
        End Get
    End Property
End Class

Module Program

    Sub Main()
        Dim data As New List(Of Transaksi) From {
            New Transaksi("Kopi", "Minuman", 3, 25000),
            New Transaksi("Teh", "Minuman", 5, 15000),
            New Transaksi("Roti", "Makanan", 2, 20000),
            New Transaksi("Nasi", "Makanan", 4, 30000),
            New Transaksi("Jus", "Minuman", 1, 35000)
        }

        For Each t In data.OrderByDescending(Function(x) x.Subtotal).
                           ThenBy(Function(x) x.Barang, StringComparer.Ordinal)
            Console.WriteLine($"{t.Barang,-11}{t.Kategori,-11}{t.Jumlah,2} x " &
                              $"{t.Harga,6} = {t.Subtotal,8}")
        Next

        Console.WriteLine("---")
        Console.WriteLine($"{"Total",-10}: {data.Sum(Function(t) t.Subtotal)}")

        For Each g In data.GroupBy(Function(t) t.Kategori).
                           OrderBy(Function(x) x.Key, StringComparer.Ordinal)
            Console.WriteLine($"{g.Key,-10}: {g.Sum(Function(t) t.Subtotal)} " &
                              $"({g.Count} transaksi)")
        Next

        Dim termahal = data.OrderByDescending(Function(t) t.Subtotal).First()
        Console.WriteLine($"{"Termahal",-10}: {termahal.Barang}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 14: ByVal, ByRef & Parameter",
        "difficulty": "Sulit",
        "question": [
            "Tulis program yang menunjukkan semua bentuk parameter VB:",
            "",
            "  Sub NaikkanSalinan(ByVal n As Integer)",
            "  Sub NaikkanAsli(ByRef n As Integer)",
            "  Sub Tukar(ByRef a, ByRef b)",
            "  Function Garis(isi, Optional lebar = 30, Optional pengisi = \"-\"c)",
            "  Function Total(ParamArray angka() As Integer)",
            "  Function Luas(sisi) dan Luas(panjang, lebar)   ' overload",
            "  Function Bagi(a, b) As (hasil, sisa)           ' tuple bernama",
            "",
            "Tunjukkan juga argumen bernama dengan := untuk melewati",
            "parameter di tengah.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  sesudah ByVal : 5",
            "  sesudah ByRef : 105",
            "  sesudah Tukar : a=8 b=3",
            "  ---",
            "  Total()       = 0",
            "  Total(1,2,3)  = 6",
            "  ---",
            "  Luas(5)       = 25",
            "  Luas(4, 6)    = 24",
            "  ---",
            "  17 / 5        = 3 sisa 2",
            "  ---",
            "  bernama       : **** BERNAMA ****",
        ],
        "hints": [
            "ByVal adalah BAWAAN di VB.NET; ByRef harus ditulis eksplisit.",
            "Argumen bernama memakai := bukan =",
            "Tuple bernama: As (hasil As Integer, sisa As Integer)",
            "New String(pengisi, n) membuat teks berulang.",
            "Untuk baris terakhir, panggil Garis dengan lebar 17 dan pengisi *.",
        ],
        "solution": """Option Strict On

Imports System

Module Program

    Sub NaikkanSalinan(ByVal n As Integer)
        n += 100
    End Sub

    Sub NaikkanAsli(ByRef n As Integer)
        n += 100
    End Sub

    Sub Tukar(ByRef a As Integer, ByRef b As Integer)
        Dim sementara As Integer = a
        a = b
        b = sementara
    End Sub

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

    Function Luas(sisi As Double) As Double
        Return sisi * sisi
    End Function

    Function Luas(panjang As Double, lebar As Double) As Double
        Return panjang * lebar
    End Function

    Function Bagi(a As Integer, b As Integer) As (hasil As Integer, sisa As Integer)
        Return (a \\ b, a Mod b)
    End Function

    Sub Main()
        Dim x As Integer = 5
        NaikkanSalinan(x)
        Console.WriteLine($"sesudah ByVal : {x}")
        NaikkanAsli(x)
        Console.WriteLine($"sesudah ByRef : {x}")

        Dim a As Integer = 3
        Dim b As Integer = 8
        Tukar(a, b)
        Console.WriteLine($"sesudah Tukar : a={a} b={b}")

        Console.WriteLine("---")
        Console.WriteLine($"Total()       = {Total()}")
        Console.WriteLine($"Total(1,2,3)  = {Total(1, 2, 3)}")

        Console.WriteLine("---")
        Console.WriteLine($"Luas(5)       = {Luas(5)}")
        Console.WriteLine($"Luas(4, 6)    = {Luas(4, 6)}")

        Console.WriteLine("---")
        Dim r = Bagi(17, 5)
        Console.WriteLine($"17 / 5        = {r.hasil} sisa {r.sisa}")

        Console.WriteLine("---")
        Console.WriteLine($"bernama       : {Garis(lebar:=17, isi:=" BERNAMA ", pengisi:="*"c)}")
    End Sub

End Module""",
    },
    {
        "title": "Latihan 15: Berkas & Using",
        "difficulty": "Sulit",
        "question": [
            "Tulis berkas CSV sementara berisi judul dan tiga baris data",
            "(Andi A 88, Budi B 72, Cici A 95) memakai blok Using dengan",
            "StreamWriter.",
            "",
            "Baca kembali, urai jadi tipe anonim, lalu tampilkan terurut",
            "nilai MENURUN beserta rata-ratanya.",
            "",
            "Lalu cetak isi berkasnya baris demi baris dengan nomor,",
            "hapus berkasnya, dan buktikan ia sudah tidak ada.",
            "",
            "Terakhir, tangkap FileNotFoundException dari membaca berkas",
            "yang memang tidak ada.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  ditulis   : belajar-vb-latihan.csv",
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
            "  masih ada?: False",
            "  FileNotFoundException tertangkap",
        ],
        "hints": [
            "Path.Combine(Path.GetTempPath(), \"nama.csv\") menyusun path.",
            "Using penulis As New StreamWriter(berkas, append:=False)",
            "Skip(1) melewati baris judul.",
            "New With { .Nama = ..., .Nilai = ... } membuat tipe anonim.",
            "Tangkap FileNotFoundException SEBELUM IOException.",
        ],
        "solution": """Option Strict On

Imports System
Imports System.IO
Imports System.Linq

Module Program

    Sub Main()
        Dim berkas As String = Path.Combine(Path.GetTempPath(),
                                            "belajar-vb-latihan.csv")

        Using penulis As New StreamWriter(berkas, append:=False)
            penulis.WriteLine("nama,kelas,nilai")
            penulis.WriteLine("Andi,A,88")
            penulis.WriteLine("Budi,B,72")
            penulis.WriteLine("Cici,A,95")
        End Using

        Console.WriteLine($"ditulis   : {Path.GetFileName(berkas)}")

        Dim data = File.ReadAllLines(berkas).
                        Skip(1).
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
        Dim nomor As Integer = 0
        For Each baris As String In File.ReadLines(berkas)
            nomor += 1
            Console.WriteLine($"{nomor,2}| {baris}")
        Next

        Console.WriteLine("---")
        File.Delete(berkas)
        Console.WriteLine($"masih ada?: {File.Exists(berkas)}")

        Try
            File.ReadAllText(Path.Combine(Path.GetTempPath(), "tidak-ada-xyz.txt"))
        Catch ex As FileNotFoundException
            Console.WriteLine("FileNotFoundException tertangkap")
        Catch ex As IOException
            Console.WriteLine($"IOException: {ex.Message}")
        End Try
    End Sub

End Module""",
    },
    {
        "title": "Latihan 16: Proyek Akhir - Inventaris Gudang",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Bangun sistem inventaris yang MEMISAHKAN tiga lapisan:",
            "model (data), layanan (aturan), dan antarmuka (cetak).",
            "",
            "MODEL",
            "  Enum Gerak { Masuk, Keluar }",
            "  Class Barang: Kode, Nama, Harga ReadOnly; Stok bisa berubah;",
            "  ReadOnly Property Subtotal; Overrides ToString berformat",
            "  \"{Kode,-5}{Nama,-12}{Stok,2}{Harga,10}{Subtotal,12}\".",
            "  Class GudangException sebagai INDUK, dengan empat turunan:",
            "    KodeSudahAdaException      -> \"kode B01 sudah ada\"",
            "    KodeTidakDikenalException  -> \"kode B09 tidak dikenal\"",
            "    JumlahTidakSahException    -> \"jumlah 0 tidak sah\"",
            "    StokTidakCukupException    -> \"stok cuma 4, diminta 10\"",
            "",
            "LAYANAN  Class Gudang berisi Dictionary(Of String, Barang)",
            "  - Daftar(Barang)  -> tolak kode kembar",
            "  - Catat(kode, Gerak, jumlah) As Integer",
            "    urutan periksa: kode dulu, lalu jumlah, baru kecukupan stok",
            "  - Semua() terurut kode",
            "  - NilaiPersediaan()",
            "  - StokMenipis(batas) terurut stok naik lalu kode",
            "  Gudang TIDAK BOLEH memanggil Console sama sekali.",
            "",
            "ANTARMUKA",
            "  Daftarkan B01 Kabel 10 15000, B02 Adaptor 4 85000,",
            "            B03 Mouse 25 120000",
            "  Jalankan: Masuk B01 15, Keluar B02 10, Keluar B03 5,",
            "            Masuk B09 1, Keluar B03 0",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Masuk B01 15 -> stok 25",
            "  Keluar B02 10 -> DITOLAK: stok cuma 4, diminta 10",
            "  Keluar B03 5 -> stok 20",
            "  Masuk B09 1 -> DITOLAK: kode B09 tidak dikenal",
            "  Keluar B03 0 -> DITOLAK: jumlah 0 tidak sah",
            "  ---",
            "  B01  Kabel       25     15000      375000",
            "  B02  Adaptor      4     85000      340000",
            "  B03  Mouse       20    120000     2400000",
            "  ---",
            "  nilai persediaan: 3115000",
            "  stok menipis (<10): B02 Adaptor (4)",
        ],
        "hints": [
            "Satu Catch As GudangException di antarmuka cukup menangani "
            "keempat galat, sementara bug sungguhan tetap naik dan terlihat.",
            "TryGetValue menggabungkan pencarian dan pemeriksaan sekaligus.",
            "Dictionary tidak menjamin urutan: Semua() WAJIB mengurutkan.",
            "Tuple.Create menyimpan tiga nilai langkah dalam satu array.",
            "Gudang yang tidak pernah mencetak bisa diuji tanpa membaca layar.",
        ],
        "solution": """Option Strict On

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
        If Not _isi.TryGetValue(kode, b) Then
            Throw New KodeTidakDikenalException(kode)
        End If
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

End Module""",
    },
]
