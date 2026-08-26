"""Penyeimbang posisi jawaban kuis.

Konten kuis ditulis manual dan punya bias kuat: penulis hampir selalu
menaruh jawaban benar di opsi kedua. Pada C++ misalnya, 55 dari 56 jawaban
ada di index 1. Kuis seperti itu bisa ditebak tanpa memahami materi.

Daripada menyunting ratusan soal di source (berisiko merusak escaping dan
format), posisi jawaban diseimbangkan di sini saat data dimuat.

Cara kerjanya: opsi DIPUTAR, bukan diacak. Memutar menjaga urutan relatif
antar opsi sehingga daftar tetap terbaca wajar, sekaligus memindahkan
jawaban benar ke posisi yang ditargetkan.

Hasilnya deterministik: menjalankan aplikasi dua kali memberi susunan yang
sama persis, sehingga penjelasan yang menyebut opsi tertentu tetap konsisten.
"""


def _putar(opsi, jawaban, target):
    """Putar daftar opsi supaya jawaban benar pindah ke index `target`."""
    n = len(opsi)
    if n == 0:
        return opsi, jawaban
    target %= n
    geser = (jawaban - target) % n
    if geser == 0:
        return opsi, jawaban
    return opsi[geser:] + opsi[:geser], target


def seimbangkan_kuis(quizzes):
    """Ratakan posisi jawaban benar di seluruh set kuis sebuah bahasa.

    Mengembalikan struktur BARU; data aslinya tidak disentuh.
    """
    hasil = []
    penghitung = 0

    for kuis in quizzes:
        soal_baru = []
        for soal in kuis["questions"]:
            opsi = list(soal["options"])
            jawaban = soal["answer"]

            # Target berputar 0,1,2,3,0,1,... sepanjang seluruh bahasa
            # sehingga sebarannya rata walau tiap kuis pendek.
            opsi, jawaban = _putar(opsi, jawaban, penghitung)
            penghitung += 1

            salinan = dict(soal)
            salinan["options"] = opsi
            salinan["answer"] = jawaban
            soal_baru.append(salinan)

        kuis_baru = dict(kuis)
        kuis_baru["questions"] = soal_baru
        hasil.append(kuis_baru)

    return hasil
