"""Kurikulum "Bikin Aplikasi".

Jembatan antara "sudah paham sintaks Java" dan "bisa membangun aplikasi web
sendiri". Studi kasusnya B-iFAMS - aplikasi inventori Gudang Fire & Safety
PT Badak NGL - termasuk beberapa bug nyata yang pernah ditemukan di sana,
karena kesalahan sungguhan lebih mengajar daripada contoh yang selalu benar.

Latihan modul ini memakai runner Java biasa: seluruh konsep dilatih dalam
Java murni tanpa framework, supaya yang dipelajari adalah CARA BERPIKIRNYA,
bukan hafalan anotasi.
"""

APLIKASI_MATERIALS = [
    {
        "title": "1. Dari Skrip ke Aplikasi",
        "sections": [
            {
                "body": [
                    "Kamu sudah bisa menulis program Java yang jalan. Lalu kenapa",
                    "membangun aplikasi terasa jauh lebih sulit?",
                    "",
                    "Karena keduanya memang beda jenis.",
                    "",
                    "SKRIP",
                    "  - Dijalankan sekali, selesai, mati.",
                    "  - Satu orang yang memakai: kamu sendiri.",
                    "  - Datanya hilang setelah program berhenti.",
                    "  - Kalau error, kamu yang lihat dan kamu yang benahi.",
                    "",
                    "APLIKASI",
                    "  - Hidup terus, menunggu permintaan datang.",
                    "  - Banyak orang memakai bersamaan, dengan hak berbeda-beda.",
                    "  - Datanya harus selamat walau aplikasi dimatikan.",
                    "  - Kalau error, orang lain yang kena, dan kamu belum tentu tahu.",
                    "",
                    "Empat perbedaan itu melahirkan hampir semua kerumitan yang akan",
                    "kamu temui. Database ada karena data harus selamat. Login ada",
                    "karena penggunanya banyak dan tidak sederajat. Log ada karena",
                    "error terjadi saat kamu tidak menonton.",
                ]
            },
            {
                "heading": "Skrip: hitung stok sekali jalan",
                "code": """public class HitungStok {
    public static void main(String[] args) {
        int stok = 20;
        stok = stok - 5;
        System.out.println("Sisa stok: " + stok);
    }
}"""
            },
            {
                "body": [
                    "Program di atas benar. Tapi coba tanya:",
                    "",
                    "  - Kalau program dimatikan, angka 15 itu ke mana?",
                    "  - Kalau dua petugas mengurangi stok bersamaan, siapa yang menang?",
                    "  - Siapa yang mengurangi? Kapan? Kenapa?",
                    "  - Bagaimana kalau seseorang mengurangi 999 padahal stok cuma 20?",
                    "",
                    "Empat pertanyaan itu yang mengubah skrip 5 baris menjadi aplikasi",
                    "puluhan berkas. Bukan karena Java-nya makin rumit, tapi karena",
                    "kenyataannya memang rumit.",
                    "",
                    "PATOKAN UNTUK MODUL INI",
                    "",
                    "Aplikasi yang kita bedah bernama B-iFAMS. Isinya kira-kira:",
                    "",
                    "  - 8 jenis benda yang disimpan (item, kategori, mutasi, dst.)",
                    "  - 6 controller",
                    "  - sekitar 15 halaman",
                    "",
                    "Skalanya menengah-kecil. Untuk developer Java berpengalaman:",
                    "3-6 minggu. Untuk yang baru belajar: 6-12 bulan, dan hasil",
                    "pertamanya kemungkinan besar dibongkar ulang. Itu normal dan",
                    "bukan tanda kamu gagal.",
                ]
            },
        ],
    },
    {
        "title": "2. Lapisan-lapisan Aplikasi Web",
        "sections": [
            {
                "body": [
                    "Ini konsep terpenting di seluruh modul ini. Kalau cuma satu hal",
                    "yang nempel dari sini, semoga yang ini.",
                    "",
                    "Aplikasi web disusun berlapis. Tiap lapisan punya satu tugas, dan",
                    "hanya boleh bicara ke lapisan tepat di bawahnya.",
                    "",
                    "  Browser",
                    "     |  permintaan HTTP: GET /items/61",
                    "     v",
                    "  CONTROLLER    menerjemahkan HTTP <-> Java. Tidak tahu SQL.",
                    "     |",
                    "     v",
                    "  SERVICE       tempat ATURAN BISNIS hidup. Tidak tahu HTTP.",
                    "     |",
                    "     v",
                    "  DAO           satu-satunya yang bicara ke database.",
                    "     |",
                    "     v",
                    "  DATABASE      menyimpan data secara permanen.",
                    "",
                    "Perhatikan kalimat 'tidak tahu' di tiap lapisan. Itu bukan",
                    "kekurangan, itu justru intinya.",
                ]
            },
            {
                "body": [
                    "KENAPA REPOT-REPOT DIPISAH?",
                    "",
                    "Bayangkan aturan 'stok tidak boleh negatif'. Aturan ini harus",
                    "berlaku di mana pun stok berkurang:",
                    "",
                    "  - saat petugas mencatat barang keluar",
                    "  - saat permintaan peminjaman disetujui",
                    "  - saat barang ditandai rusak",
                    "",
                    "Kalau aturannya ditulis di controller, kamu menulisnya TIGA KALI.",
                    "Suatu hari salah satunya lupa diperbarui, dan stok jadi negatif",
                    "lewat jalur yang terlupakan itu.",
                    "",
                    "Kalau aturannya ditulis sekali di service, ketiga jalur memanggil",
                    "service yang sama. Mustahil ada jalur yang lolos.",
                    "",
                    "ATURAN PRAKTIS",
                    "",
                    "  Controller  tipis. Ambil input, panggil service, pilih halaman.",
                    "              Kalau ada 'if' rumit di sini, biasanya salah tempat.",
                    "",
                    "  Service     tebal. Semua keputusan ada di sini.",
                    "",
                    "  DAO         bodoh. Cuma simpan dan ambil. Tidak boleh memutuskan.",
                ]
            },
            {
                "heading": "Contoh nyata dari B-iFAMS",
                "code": """// CONTROLLER - tipis, cuma menghubungkan
@RequestMapping(value = "/{id}/stock", method = RequestMethod.POST)
public String sesuaikanStok(@PathVariable Long id,
                            @RequestParam MovementType type,
                            @RequestParam int qty,
                            RedirectAttributes ra) {
    try {
        stockService.catatMutasi(id, type, qty);   // keputusan bukan di sini
        ra.addFlashAttribute("success", "Mutasi tersimpan.");
    } catch (StokTidakCukupException e) {
        ra.addFlashAttribute("error", e.getMessage());
    }
    return "redirect:/items/" + id;
}"""
            },
            {
                "body": [
                    "Lihat controller di atas: tidak ada satu pun aturan bisnis.",
                    "Ia cuma menerima, memanggil, dan menentukan halaman berikutnya.",
                    "Keputusan 'boleh atau tidak' ada di dalam catatMutasi().",
                    "",
                    "Kalau besok ada halaman baru yang juga mengurangi stok, halaman",
                    "itu tinggal memanggil catatMutasi() dan otomatis ikut terlindungi.",
                ]
            },
        ],
    },
    {
        "title": "3. Model Data: dari Benda Nyata ke Tabel",
        "sections": [
            {
                "body": [
                    "Sebelum menulis kode, gambar dulu di kertas: BENDA APA SAJA yang",
                    "disimpan sistem ini, dan bagaimana hubungannya.",
                    "",
                    "Bagian ini paling sering diremehkan dan paling mahal kalau salah.",
                    "Mengubah model data setelah aplikasi berisi data asli itu berat -",
                    "seperti mengganti pondasi rumah yang sudah ditinggali.",
                    "",
                    "CARA MENEMUKAN BENDANYA",
                    "",
                    "Baca dokumen kebutuhan, lalu lingkari semua KATA BENDA-nya.",
                    "",
                    "  'Petugas mencatat item baru beserta kategorinya, lalu setiap",
                    "   perubahan stok dicatat sebagai mutasi. Pekerja dari seksi lain",
                    "   mengajukan permintaan peminjaman barang.'",
                    "",
                    "Kata benda: petugas, item, kategori, stok, mutasi, pekerja,",
                    "permintaan, barang.",
                    "",
                    "Beberapa ternyata sama (petugas & pekerja = pengguna; barang &",
                    "item = item). Beberapa bukan benda tapi sifat (stok = angka milik",
                    "item, bukan benda tersendiri).",
                    "",
                    "Sisanya jadi tabel.",
                ]
            },
            {
                "heading": "Model data B-iFAMS",
                "code": """Kategori ---punya banyak---> Item ---punya banyak---> MutasiStok
                              |
                              +---muncul di---> BarisPermintaan
                                                     ^
                                                     | berisi banyak
                                                Permintaan
                                                     ^
                                                     | mengajukan
                                                 Pengguna"""
            },
            {
                "body": [
                    "TIGA JENIS HUBUNGAN",
                    "",
                    "  Satu ke banyak (paling sering)",
                    "    Satu kategori punya banyak item.",
                    "    Satu item punya banyak baris mutasi.",
                    "    Caranya: tabel 'banyak' menyimpan id si 'satu'.",
                    "    Tabel item punya kolom category_id.",
                    "",
                    "  Banyak ke banyak",
                    "    Satu permintaan berisi banyak item,",
                    "    satu item muncul di banyak permintaan.",
                    "    Caranya: bikin tabel penghubung di tengah.",
                    "    Di B-iFAMS namanya request_item.",
                    "",
                    "  Satu ke satu (jarang)",
                    "    Biasanya tanda dua tabel itu sebenarnya satu.",
                    "",
                    "SATU PERTANYAAN YANG MENYELAMATKAN",
                    "",
                    "Untuk tiap kolom, tanya: 'kalau ini berubah, apa yang harus",
                    "ikut berubah?' Kalau jawabannya banyak, model datamu belum benar.",
                    "",
                    "Contoh: kalau nama item disimpan juga di tabel mutasi, maka",
                    "mengganti nama item harus memperbarui ratusan baris mutasi. Itu",
                    "tanda seharusnya mutasi cukup menyimpan item_id saja.",
                ]
            },
        ],
    },
    {
        "title": "4. Entitas: Benda Menjadi Kelas",
        "sections": [
            {
                "body": [
                    "Tiap benda di model data jadi satu kelas Java. Kelas semacam ini",
                    "disebut ENTITAS, dan bentuknya sangat sederhana: field privat,",
                    "getter, setter. Tidak ada logika rumit di dalamnya.",
                    "",
                    "Kelas seperti ini sering dijuluki POJO - Plain Old Java Object.",
                    "Namanya terdengar merendahkan, padahal justru pujian: artinya",
                    "kelas biasa yang tidak terikat framework apa pun.",
                    "",
                    "KENAPA FIELD-NYA PRIVAT?",
                    "",
                    "Supaya nilainya cuma bisa diubah lewat pintu yang kamu kendalikan.",
                    "Kalau field publik, siapa pun bisa menulis item.stok = -5 dari mana",
                    "saja, dan kamu tidak punya tempat untuk mencegahnya.",
                ]
            },
            {
                "heading": "Entitas Item yang disederhanakan",
                "code": """public class Item {
    private Long id;
    private String kode;
    private String nama;
    private String satuan;
    private int stok;
    private int stokMinimum;

    public Item(String kode, String nama, String satuan, int stokMinimum) {
        this.kode = kode;
        this.nama = nama;
        this.satuan = satuan;
        this.stokMinimum = stokMinimum;
        this.stok = 0;
    }

    public String getKode()  { return kode; }
    public String getNama()  { return nama; }
    public int getStok()     { return stok; }
    public void setStok(int stok) { this.stok = stok; }

    public boolean stokMenipis() {
        return stok <= stokMinimum;
    }

    @Override
    public String toString() {
        return kode + " - " + nama + " (" + stok + " " + satuan + ")";
    }
}"""
            },
            {
                "body": [
                    "Perhatikan method stokMenipis(). Ini contoh logika yang PANTAS",
                    "ada di entitas: ia cuma menjawab pertanyaan tentang dirinya",
                    "sendiri, tidak butuh data lain, tidak menyentuh database.",
                    "",
                    "Bandingkan dengan 'apakah item ini boleh dipinjam?' - itu butuh",
                    "tahu status junk, tanggal kedaluwarsa, dan jumlah yang diminta.",
                    "Pertanyaan seperti itu tempatnya di service, bukan di entitas.",
                    "",
                    "GARIS PEMISAHNYA",
                    "",
                    "  Di entitas   : pertanyaan yang bisa dijawab dari field sendiri.",
                    "  Di service   : keputusan yang butuh data lain atau efek samping.",
                ]
            },
        ],
    },
    {
        "title": "5. DAO: Satu-satunya Pintu ke Database",
        "sections": [
            {
                "body": [
                    "DAO singkatan dari Data Access Object. Tugasnya satu: menerjemahkan",
                    "antara objek Java dan baris tabel. Tidak lebih.",
                    "",
                    "Aturannya keras: SELURUH SQL di aplikasimu harus ada di dalam DAO.",
                    "Kalau ada SQL bocor ke controller atau service, kamu kehilangan",
                    "kemampuan menjawab pertanyaan 'siapa saja yang menyentuh tabel ini?'",
                    "",
                    "BENTUK BAKUNYA",
                    "",
                    "  simpan(objek)        -> INSERT atau UPDATE",
                    "  cariById(id)         -> SELECT satu baris",
                    "  cariSemua()          -> SELECT banyak baris",
                    "  hapus(id)            -> DELETE",
                    "",
                    "Plus pencarian khusus sesuai kebutuhan, misalnya:",
                    "",
                    "  cariStokMenipis()",
                    "  cariAkanKedaluwarsa(int hari)",
                ]
            },
            {
                "heading": "DAO sebagai antarmuka",
                "code": """public interface ItemDao {
    Item cariById(Long id);
    List<Item> cariSemua();
    List<Item> cariStokMenipis();
    void simpan(Item item);
    void hapus(Long id);
}"""
            },
            {
                "body": [
                    "Kenapa dibuat interface dulu, bukan langsung kelas?",
                    "",
                    "Karena service cukup tahu APA yang bisa dilakukan, tidak perlu tahu",
                    "CARANYA. Hari ini implementasinya pakai Hibernate ke Oracle; besok",
                    "bisa diganti ke PostgreSQL atau bahkan ke daftar di memori untuk",
                    "keperluan pengujian - dan service tidak perlu diubah sebaris pun.",
                    "",
                    "Ini bukan teori. Latihan di modul ini memakai DAO versi memori,",
                    "sehingga kamu bisa melatih logika service tanpa memasang database",
                    "apa pun.",
                    "",
                    "HIBERNATE MENGERJAKAN BAGIAN MEMBOSANKANNYA",
                    "",
                    "Menulis SQL manual untuk tiap tabel itu melelahkan dan rawan salah",
                    "ketik. Hibernate membacanya dari anotasi di entitas lalu membuatkan",
                    "SQL-nya sendiri. Kamu cukup menandai:",
                    "",
                    "  @Entity              kelas ini mewakili sebuah tabel",
                    "  @Table(name=\"item\")  nama tabelnya",
                    "  @Id                  kolom kunci utama",
                    "  @Column              pengaturan kolom",
                    "  @ManyToOne           hubungan ke tabel lain",
                    "",
                    "Tapi hati-hati: Hibernate menyembunyikan SQL, bukan menghapusnya.",
                    "Saat aplikasi melambat, kamu tetap harus bisa membaca SQL yang",
                    "dihasilkannya. Karena itu belajar SQL tidak bisa dilewati.",
                ]
            },
        ],
    },
    {
        "title": "6. Service: Tempat Aturan Bisnis Hidup",
        "sections": [
            {
                "body": [
                    "Kalau aplikasimu punya 'otak', letaknya di sini.",
                    "",
                    "Service menjawab pertanyaan yang tidak bisa dijawab satu entitas",
                    "sendirian, dan mengatur urutan langkah yang harus terjadi bersamaan.",
                    "",
                    "CONTOH: MENYETUJUI PEMINJAMAN",
                    "",
                    "Satu tombol 'Setujui' di layar sebenarnya memicu rantai keputusan:",
                    "",
                    "  1. Apakah permintaannya masih berstatus PENDING?",
                    "  2. Apakah itemnya masih aktif, bukan junk?",
                    "  3. Apakah itemnya belum kedaluwarsa?",
                    "  4. Apakah stoknya mencukupi?",
                    "  5. Kurangi stok item.",
                    "  6. Catat mutasi keluar, sebutkan nomor permintaannya.",
                    "  7. Ubah status jadi APPROVED.",
                    "  8. Catat siapa yang menyetujui dan kapan.",
                    "",
                    "Delapan langkah, dan tidak boleh setengah jalan.",
                ]
            },
            {
                "heading": "Bentuk service-nya",
                "code": """public class RequestService {

    private final ItemDao itemDao;
    private final RequestDao requestDao;

    public void setujui(Long requestId, String namaPetugas) {
        Permintaan p = requestDao.cariById(requestId);

        if (p.getStatus() != Status.PENDING)
            throw new AturanDilanggar("Permintaan sudah diproses.");

        for (BarisPermintaan baris : p.getBaris()) {
            Item item = baris.getItem();

            if (item.isJunk())
                throw new AturanDilanggar(item.getNama() + " berstatus junk.");

            if (item.getStok() < baris.getJumlah())
                throw new AturanDilanggar("Stok tidak mencukupi untuk "
                        + item.getNama() + " (tersedia " + item.getStok()
                        + ", diminta " + baris.getJumlah() + ").");
        }

        for (BarisPermintaan baris : p.getBaris()) {
            Item item = baris.getItem();
            item.setStok(item.getStok() - baris.getJumlah());
            itemDao.simpan(item);
            catatMutasi(item, MovementType.OUT, baris.getJumlah(),
                        "Dipinjam - permintaan " + p.getKode(), namaPetugas);
        }

        p.setStatus(Status.APPROVED);
        p.setDiprosesOleh(namaPetugas);
        requestDao.simpan(p);
    }
}"""
            },
            {
                "body": [
                    "Perhatikan susunannya: SEMUA pemeriksaan dilakukan lebih dulu di",
                    "perulangan pertama, baru perubahan dilakukan di perulangan kedua.",
                    "",
                    "Kenapa tidak digabung saja jadi satu perulangan?",
                    "",
                    "Karena kalau permintaan berisi 5 item dan item kelima ternyata",
                    "stoknya kurang, dengan satu perulangan stok item 1-4 sudah terlanjur",
                    "berkurang saat error dilempar. Data jadi rusak separuh jalan.",
                    "",
                    "Pola 'periksa semua dulu, ubah belakangan' ini nama akademisnya",
                    "atomicity - dan ini salah satu kebiasaan yang membedakan kode",
                    "pemula dari kode yang layak dipakai orang.",
                    "",
                    "TRANSAKSI",
                    "",
                    "Untuk perlindungan yang lebih kuat, database punya TRANSAKSI:",
                    "sekumpulan perubahan yang dianggap satu kesatuan. Kalau ada yang",
                    "gagal di tengah, semuanya dibatalkan otomatis.",
                    "",
                    "Di Spring caranya cukup menempelkan @Transactional di method.",
                    "Tapi anotasi itu baru berguna kalau kamu paham kenapa dibutuhkan -",
                    "dan alasannya persis yang barusan dijelaskan.",
                ]
            },
        ],
    },
    {
        "title": "7. Controller: Menerjemahkan HTTP",
        "sections": [
            {
                "body": [
                    "Browser tidak mengenal objek Java. Ia cuma tahu mengirim teks",
                    "lewat HTTP dan menerima HTML. Controller adalah penerjemahnya.",
                    "",
                    "ISI SEBUAH PERMINTAAN HTTP",
                    "",
                    "  METHOD   GET (ambil) atau POST (kirim/ubah)",
                    "  PATH     /items/61",
                    "  PARAM    ?cari=apar   atau data formulir",
                    "  HEADER   keterangan tambahan, termasuk cookie sesi",
                    "",
                    "GET DAN POST TIDAK BOLEH TERTUKAR",
                    "",
                    "GET harus AMAN: memanggilnya berkali-kali tidak mengubah apa pun.",
                    "POST boleh mengubah data.",
                    "",
                    "Kenapa penting? Karena browser dan mesin pencari bebas memanggil",
                    "GET kapan saja - saat pengguna menekan tombol kembali, saat",
                    "halaman di-refresh, saat tautan di-preview. Kalau menghapus data",
                    "dibuat sebagai GET, satu kali refresh bisa menghapus dua kali.",
                ]
            },
            {
                "heading": "Peta rute B-iFAMS",
                "code": """GET   /items                 daftar semua item
GET   /items/new             formulir tambah item
POST  /items                 simpan item baru
GET   /items/{id}            detail satu item
GET   /items/{id}/edit       formulir ubah item
POST  /items/{id}            simpan perubahan
POST  /items/{id}/stock      catat mutasi stok
POST  /items/{id}/junk       tandai rusak
POST  /requests/{id}/approve setujui permintaan"""
            },
            {
                "body": [
                    "Pola penamaan ini namanya REST. Perhatikan keteraturannya: kata",
                    "benda jamak untuk kumpulan, id untuk satu benda, kata kerja hanya",
                    "muncul untuk aksi yang tidak sekadar simpan/ambil.",
                    "",
                    "Keteraturan ini bukan gaya-gayaan. Dengan pola yang konsisten,",
                    "orang bisa menebak alamat halaman yang belum pernah dilihatnya -",
                    "termasuk kamu sendiri enam bulan lagi.",
                    "",
                    "POLA POST-REDIRECT-GET",
                    "",
                    "Setelah POST berhasil, JANGAN langsung menampilkan halaman.",
                    "Balas dengan perintah pindah alamat (redirect), lalu biarkan",
                    "browser meminta halamannya lewat GET.",
                    "",
                    "Tanpa ini, pengguna yang menekan refresh setelah menyimpan akan",
                    "mengirim formulir yang sama dua kali. Di B-iFAMS itu berarti",
                    "stok berkurang dua kali dari satu pencatatan.",
                    "",
                    "Di kode tadi kamu sudah melihatnya:",
                    "",
                    "  return \"redirect:/items/\" + id;",
                ]
            },
        ],
    },
    {
        "title": "8. Tampilan: JSP, Tiles, dan Kenapa Dipisah",
        "sections": [
            {
                "body": [
                    "Controller sudah menyiapkan data. Sekarang data itu harus jadi",
                    "HTML yang bisa dibaca manusia.",
                    "",
                    "JSP adalah HTML yang boleh disisipi data. Bentuknya HTML biasa,",
                    "dengan lubang-lubang kecil tempat nilai dari Java dimasukkan.",
                ]
            },
            {
                "heading": "Potongan JSP",
                "code": """<h1>${item.nama}</h1>
<p>Stok saat ini: ${item.stok} ${item.satuan}</p>

<table>
  <tr><th>Waktu</th><th>Jenis</th><th>Qty</th><th>Sisa</th></tr>
  <c:forEach var="m" items="${history}">
    <tr>
      <td>${m.waktu}</td>
      <td>${m.jenis}</td>
      <td>${m.qty}</td>
      <td>${m.sisaStok}</td>
    </tr>
  </c:forEach>
</table>"""
            },
            {
                "body": [
                    "  ${item.nama}   diganti nilai dari objek yang dikirim controller",
                    "  <c:forEach>    mengulang blok untuk tiap baris daftar",
                    "",
                    "APACHE TILES: MENGHINDARI SALIN-TEMPEL",
                    "",
                    "Lima belas halaman B-iFAMS punya bagian yang sama persis: header,",
                    "menu samping, footer. Kalau ditulis ulang di tiap halaman, mengganti",
                    "satu menu berarti menyunting lima belas berkas.",
                    "",
                    "Tiles memisahkan rangka dari isi:",
                    "",
                    "  layout.jsp   rangka: header + menu + <lubang isi> + footer",
                    "  detail.jsp   cuma bagian isinya saja",
                    "",
                    "Ganti menu sekali di layout, lima belas halaman ikut berubah.",
                    "",
                    "SATU ATURAN YANG TIDAK BOLEH DILANGGAR",
                    "",
                    "JANGAN menaruh keputusan bisnis di JSP.",
                    "",
                    "  Boleh    : <c:if test=\"${item.stokMenipis}\"> tampilkan lencana",
                    "  Terlarang: <c:if test=\"${item.stok <= item.stokMin}\">",
                    "",
                    "Yang pertama bertanya pada objek. Yang kedua MEMUTUSKAN di tampilan -",
                    "dan keputusan itu akan berbeda dengan yang di service begitu",
                    "aturannya berubah.",
                    "",
                    "Contoh paling mahal dari pelanggaran ini ada di materi berikutnya:",
                    "menyembunyikan tombol di tampilan disangka sama dengan melarang",
                    "aksinya. Ternyata tidak.",
                ]
            },
        ],
    },
    {
        "title": "9. Maven dan Struktur Proyek",
        "sections": [
            {
                "body": [
                    "Aplikasi Java butuh puluhan pustaka buatan orang lain. Spring",
                    "sendiri terdiri dari belasan berkas jar, dan tiap jar butuh jar",
                    "lain lagi. Mengunduhnya satu per satu mustahil dikerjakan tangan.",
                    "",
                    "Maven mengurus itu. Kamu cukup menulis APA yang dibutuhkan di satu",
                    "berkas bernama pom.xml, Maven mengunduh semuanya beserta rantai",
                    "kebutuhannya, lalu merakit aplikasimu jadi satu berkas siap deploy.",
                ]
            },
            {
                "heading": "Sepotong pom.xml",
                "code": """<dependencies>
  <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>4.1.0.RELEASE</version>
  </dependency>
  <dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-core</artifactId>
    <version>4.1.12.Final</version>
  </dependency>
</dependencies>"""
            },
            {
                "body": [
                    "Tiga baris itu menarik puluhan jar sekaligus.",
                    "",
                    "STRUKTUR FOLDER YANG WAJIB DIIKUTI",
                    "",
                    "Maven tidak bertanya di mana kodemu - ia sudah menetapkannya.",
                    "",
                    "  pom.xml",
                    "  src/main/java/          kode Java",
                    "  src/main/resources/     konfigurasi (jdbc.properties)",
                    "  src/main/webapp/        halaman & aset",
                    "      WEB-INF/views/      JSP",
                    "      WEB-INF/spring/     konfigurasi Spring",
                    "      WEB-INF/web.xml     titik masuk aplikasi",
                    "  src/test/java/          kode pengujian",
                    "  target/                 hasil rakitan (jangan disimpan di Git)",
                    "",
                    "Awalnya terasa kaku. Manfaatnya baru terasa saat kamu membuka",
                    "proyek Java orang lain dan langsung tahu harus mencari di mana.",
                    "",
                    "PERINTAH YANG DIPAKAI SEHARI-HARI",
                    "",
                    "  mvn clean          hapus hasil rakitan lama",
                    "  mvn compile        kompilasi saja",
                    "  mvn test           jalankan pengujian",
                    "  mvn package        rakit jadi .war atau .jar",
                    "",
                    "Biasanya digabung: mvn clean package",
                    "",
                    "Hasilnya muncul di target/. Berkas .war itulah yang disalin ke",
                    "server. Untuk B-iFAMS, ukurannya sekitar 25 MB.",
                ]
            },
        ],
    },
    {
        "title": "10. Keamanan: Autentikasi vs Otorisasi",
        "sections": [
            {
                "body": [
                    "Dua kata yang mirip, sering tertukar, dan akibat tertukarnya fatal.",
                    "",
                    "  AUTENTIKASI  Siapa kamu?        -> proses login",
                    "  OTORISASI    Kamu boleh apa?    -> pemeriksaan hak akses",
                    "",
                    "Login yang benar tidak ada gunanya kalau setelah masuk semua orang",
                    "bisa melakukan segalanya.",
                    "",
                    "B-iFAMS punya dua peran:",
                    "",
                    "  ADMIN      petugas Fire & Safety. Kelola item, setujui permintaan.",
                    "  REQUESTER  pekerja seksi lain. Mengajukan dan melihat saja.",
                    "",
                    "DUA LAPIS PEMERIKSAAN",
                    "",
                    "  Lapis URL     'siapa pun bukan ADMIN, tolak /items/new'",
                    "  Lapis method  'method ini hanya boleh dipanggil ADMIN'",
                    "",
                    "Dan satu hal yang BUKAN pemeriksaan sama sekali: menyembunyikan",
                    "tombol di tampilan.",
                ]
            },
            {
                "body": [
                    "KISAH NYATA: BUG YANG MEMBUKA SEMUA PINTU",
                    "",
                    "Di B-iFAMS pernah ditemukan hal ini. Semua controller sudah diberi",
                    "penanda hak akses dengan benar:",
                    "",
                    "  @PreAuthorize(\"hasRole('ADMIN')\")",
                    "  public String hapus(...)",
                    "",
                    "Sembilan penanda di ItemController, lima di RequestController, dua",
                    "di CategoryController. Ditulis rapi, tidak ada yang salah ketik.",
                    "",
                    "Tapi seluruhnya TIDAK PERNAH AKTIF.",
                    "",
                    "Penyebabnya letak satu baris konfigurasi. Spring punya dua wadah",
                    "objek: satu untuk aplikasi umum, satu untuk bagian web. Perintah",
                    "yang MENGHIDUPKAN penanda itu ditaruh di wadah pertama, sementara",
                    "controller-nya tinggal di wadah kedua. Mekanisme penghidupnya",
                    "hanya bekerja pada penghuni wadah yang sama.",
                    "",
                    "Akibatnya: setiap orang yang berhasil login - peran apa pun - bisa",
                    "memanggil semua endpoint admin. Tombolnya memang disembunyikan di",
                    "layar, tapi mengetik alamatnya langsung tetap berhasil.",
                    "",
                    "PELAJARANNYA ADA TIGA, DAN KETIGANYA MAHAL",
                    "",
                    "1. Kode yang KELIHATAN benar belum tentu BERJALAN benar.",
                    "   Tidak ada error, tidak ada peringatan, semuanya tampak beres.",
                    "",
                    "2. Menguji sebagai admin tidak membuktikan apa pun tentang hak akses.",
                    "   Admin memang boleh segalanya. Bug ini hanya bisa terlihat kalau",
                    "   diuji dari akun berperan rendah.",
                    "",
                    "3. Jangan bergantung pada satu mekanisme saja.",
                    "   Perbaikannya bukan cuma memindahkan baris itu, tapi juga",
                    "   menambahkan aturan di lapis URL - supaya kalau penanda method",
                    "   mati lagi suatu hari, masih ada yang menahan.",
                ]
            },
            {
                "heading": "Cara membuktikannya - ini yang benar-benar dilakukan",
                "code": """Login sebagai akun berperan REQUESTER, lalu panggil langsung:

  GET  /items/new              -> 403   (ditolak)
  POST /items                  -> 403
  POST /items/1/stock          -> 403
  POST /categories             -> 403
  POST /requests/1/approve     -> 403

Sekaligus pastikan yang boleh TIDAK ikut terkunci:

  GET  /items                  -> 200   (boleh melihat)
  GET  /requests/new           -> 200   (boleh mengajukan)
  POST /requests               -> 400   (ditolak karena data kosong,
                                         BUKAN karena hak akses)"""
            },
            {
                "body": [
                    "Baris terakhir itu penting dan sering dilupakan. Kalau seluruh",
                    "pengujianmu cuma memastikan 'yang dilarang ditolak', kamu bisa",
                    "salah kunci sampai pengguna sah pun tidak bisa bekerja - dan itu",
                    "tetap lolos pengujian.",
                    "",
                    "Uji dua arah: yang dilarang harus ditolak, yang diizinkan harus",
                    "lewat.",
                ]
            },
        ],
    },
    {
        "title": "11. Database di Produksi",
        "sections": [
            {
                "body": [
                    "Database di laptopmu boleh diperlakukan seenaknya. Database",
                    "produksi tidak - isinya pekerjaan orang sungguhan.",
                    "",
                    "SATU PENGATURAN YANG BISA MENGHANCURKAN DIAM-DIAM",
                    "",
                    "Hibernate punya pengaturan bernama hbm2ddl.auto. Nilainya",
                    "menentukan apa yang terjadi pada struktur tabel saat aplikasi start:",
                    "",
                    "  none      jangan sentuh apa pun          <- aman",
                    "  validate  periksa cocok, tolak jalan     <- aman, disarankan",
                    "  update    ubah tabel agar cocok kode     <- BERBAHAYA di produksi",
                    "  create    hapus semua, bikin ulang       <- data lenyap seketika",
                    "",
                    "B-iFAMS dan B-Guest keduanya memakai 'update' di produksi.",
                    "",
                    "Artinya kalau seseorang mengganti nama field di kode Java, Hibernate",
                    "akan menambah kolom baru di tabel Oracle saat aplikasi di-restart,",
                    "dan meninggalkan kolom lama berisi data - tanpa memberi tahu siapa pun.",
                    "",
                    "Yang benar: pakai 'validate', dan setiap perubahan struktur tabel",
                    "ditulis sebagai skrip SQL yang ditinjau, dijalankan sadar-sadar,",
                    "dan disimpan di Git bersama kodenya. Itu namanya migrasi.",
                ]
            },
            {
                "body": [
                    "SATU HAL LAGI: JANGAN SAMPAI SALAH DATABASE",
                    "",
                    "Ini kejadian sungguhan saat audit B-iFAMS.",
                    "",
                    "Di server aplikasi ada kontainer Docker bernama bifams-pg, berisi",
                    "database dengan nama tabel yang sama persis: app_user, item,",
                    "item_request. Sekilas itulah database aplikasinya.",
                    "",
                    "Ternyata bukan. Itu sisa versi lama yang belum dimatikan, dan",
                    "isinya kosong. Database yang sesungguhnya dipakai ada di MESIN LAIN,",
                    "memakai Oracle, bukan PostgreSQL.",
                    "",
                    "Akun uji yang dibuat ke sana tidak pernah bisa dipakai login, dan",
                    "butuh waktu cukup lama untuk sadar penyebabnya.",
                    "",
                    "CARA MENGHINDARINYA",
                    "",
                    "Jangan menebak dari nama. Baca konfigurasi aplikasi yang SEDANG",
                    "BERJALAN:",
                    "",
                    "  jdbc.url=jdbc:oracle:thin:@//10.10.1.187:1521/XE",
                    "  jdbc.username=BIFAMS_FS",
                    "",
                    "Baris itu sumber kebenarannya. Bukan nama kontainer, bukan ingatan,",
                    "bukan dokumentasi - karena dokumentasinya waktu itu juga salah.",
                    "",
                    "Dan sebelum mengubah data, buktikan dulu kamu di tempat yang benar:",
                    "cari satu baris yang kamu tahu pasti ada. Kalau tidak ketemu,",
                    "berarti kamu salah database.",
                ]
            },
        ],
    },
    {
        "title": "12. Deploy, Cadangan, dan Cara Mundur",
        "sections": [
            {
                "body": [
                    "Deploy artinya memindahkan aplikasi dari laptopmu ke server tempat",
                    "orang lain memakainya.",
                    "",
                    "URUTAN YANG DIPAKAI DI B-iFAMS",
                    "",
                    "  1. Rakit          mvn clean package  -> target/aplikasi.war",
                    "  2. CADANGKAN      salin .war lama yang sedang jalan",
                    "  3. Hentikan       shutdown.sh",
                    "  4. Tukar          .war baru menggantikan yang lama",
                    "  5. Nyalakan       startup.sh",
                    "  6. Verifikasi     buka halamannya, baca log",
                    "",
                    "LANGKAH 2 TIDAK BOLEH DILEWATI",
                    "",
                    "Sebelum menyentuh apa pun, simpan dulu versi yang sedang berjalan.",
                    "Kalau versi baru bermasalah, kamu bisa kembali dalam hitungan detik",
                    "alih-alih memperbaikinya dalam panik sementara pengguna menunggu.",
                    "",
                    "  cp webapps/ROOT.war ~/ROOT.war.sebelum-20260826",
                    "",
                    "Beri nama bertanggal. Enam bulan lagi kamu tidak akan ingat",
                    "'ROOT.war.backup2' itu versi yang mana.",
                ]
            },
            {
                "body": [
                    "LANGKAH 6 BUKAN SEKADAR 'APLIKASINYA NYALA'",
                    "",
                    "Halaman login muncul bukan bukti aplikasi sehat. Yang harus dicek:",
                    "",
                    "  - Log start-up bersih, tidak ada exception",
                    "  - Halaman yang kamu ubah benar-benar berubah",
                    "  - Halaman yang TIDAK kamu ubah masih normal",
                    "",
                    "Yang ketiga sering dilupakan, padahal justru di situ kerusakan",
                    "tak sengaja muncul.",
                    "",
                    "JEBAKAN: MENYUNTING LANGSUNG DI SERVER",
                    "",
                    "Aplikasi yang sudah di-deploy biasanya terhampar sebagai folder di",
                    "server. Menyunting berkas di situ terasa praktis - perubahannya",
                    "langsung terasa, tidak perlu build ulang.",
                    "",
                    "Masalahnya, perubahan itu ada DI SERVER SAJA. Begitu aplikasi",
                    "di-deploy ulang dari .war, perubahanmu hilang tanpa jejak - dan",
                    "biasanya kamu baru sadar berbulan-bulan kemudian saat bug lama",
                    "muncul lagi entah dari mana.",
                    "",
                    "Kalau terpaksa melakukannya, catat, dan segera lipat perubahan itu",
                    "ke source aslinya.",
                ]
            },
        ],
    },
    {
        "title": "13. Menguji Seperti Pengguna Sungguhan",
        "sections": [
            {
                "body": [
                    "Pengujian yang bermanfaat bukan 'coba klik-klik sebentar', tapi",
                    "menjalankan tiap alur sampai tuntas dengan hasil yang bisa diperiksa.",
                    "",
                    "TIGA TINGKAT",
                    "",
                    "  Unit         satu method diuji sendirian, tanpa database.",
                    "               Cepat, dijalankan tiap kali kode berubah.",
                    "",
                    "  Integrasi    beberapa lapisan bersama, dengan database.",
                    "               Lebih lambat, menangkap salah sambung antar lapisan.",
                    "",
                    "  Manual       manusia memakainya seperti pengguna asli.",
                    "               Paling lambat, tapi menangkap hal yang tak terpikirkan.",
                    "",
                    "SATU KEBIASAAN YANG PALING BERGUNA",
                    "",
                    "Untuk tiap aturan bisnis, uji DUA sisinya:",
                    "",
                    "  - kasus yang seharusnya BERHASIL",
                    "  - kasus yang seharusnya DITOLAK",
                    "",
                    "Menguji sisi berhasil saja meloloskan aplikasi yang tidak punya",
                    "pemeriksaan sama sekali. Menguji sisi ditolak saja meloloskan",
                    "aplikasi yang menolak segalanya.",
                ]
            },
            {
                "heading": "Contoh daftar uji untuk satu aturan",
                "code": """Aturan: stok tidak boleh negatif

  stok 20, keluar  5  -> berhasil, sisa 15
  stok 20, keluar 20  -> berhasil, sisa 0      (batas tepat)
  stok 20, keluar 21  -> DITOLAK               (lewat satu langkah)
  stok 20, keluar  0  -> ditolak, tidak masuk akal
  stok 20, keluar -5  -> ditolak, jangan sampai malah menambah

Perhatikan tiga baris tengah. Kesalahan hampir selalu bersembunyi
di BATAS, bukan di tengah-tengah."""
            },
            {
                "body": [
                    "PERIKSA DATANYA, JANGAN CUMA LAYARNYA",
                    "",
                    "Saat menguji B-iFAMS, penghapusan sebuah item terlihat berhasil:",
                    "pesan sukses muncul, daftar item kosong, seluruh penghitung di",
                    "beranda kembali nol. Semua tampak beres.",
                    "",
                    "Ternyata dua permintaan yang mengacu item itu masih tertinggal di",
                    "database - kini menggantung tanpa item sama sekali. Layar tidak",
                    "menunjukkannya karena halaman yang menampilkannya memang tidak",
                    "dibuka.",
                    "",
                    "Karena itu belajar SQL bukan pelengkap. Tanpa kemampuan membuka",
                    "database sendiri, kamu cuma bisa mempercayai apa yang aplikasi",
                    "mau tunjukkan padamu.",
                    "",
                    "PENUTUP MODUL",
                    "",
                    "Materi ini sengaja tidak mengajarkan cara menempelkan anotasi",
                    "Spring satu per satu. Anotasi bisa dicari kapan saja; yang tidak",
                    "bisa dicari adalah pertimbangan di baliknya - kenapa aturan bisnis",
                    "ditaruh di service, kenapa periksa dulu baru ubah, kenapa hak akses",
                    "harus diuji dari akun yang tidak berhak.",
                    "",
                    "Latihan modul ini melatih semua itu dalam Java murni, tanpa",
                    "framework apa pun. Kalau kamu bisa menyelesaikannya, membaca kode",
                    "B-iFAMS tidak akan terasa seperti sihir lagi.",
                ]
            },
        ],
    },
]
