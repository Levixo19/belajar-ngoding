"""Kumpulan konten kurikulum per bahasa.

Setiap bahasa punya tiga file: materi, kuis, dan latihan.
Menambah bahasa baru = tambah tiga file di sini, ekspor di bawah,
lalu daftarkan satu entri di LANGUAGES pada main.py.
"""

from data.normalisasi import seimbangkan_kuis

from data.java_materials import JAVA_MATERIALS
from data.java_quizzes import JAVA_QUIZZES as _JAVA_QUIZZES
from data.java_exercises import JAVA_EXERCISES

from data.sql_materials import SQL_MATERIALS
from data.sql_quizzes import SQL_QUIZZES as _SQL_QUIZZES
from data.sql_exercises import SQL_EXERCISES

from data.python_materials import PYTHON_MATERIALS
from data.python_quizzes import PYTHON_QUIZZES as _PYTHON_QUIZZES
from data.python_exercises import PYTHON_EXERCISES

from data.javascript_materials import JAVASCRIPT_MATERIALS
from data.javascript_quizzes import JAVASCRIPT_QUIZZES as _JAVASCRIPT_QUIZZES
from data.javascript_exercises import JAVASCRIPT_EXERCISES

from data.c_materials import C_MATERIALS
from data.c_quizzes import C_QUIZZES as _C_QUIZZES
from data.c_exercises import C_EXERCISES

from data.cpp_materials import CPP_MATERIALS
from data.cpp_quizzes import CPP_QUIZZES as _CPP_QUIZZES
from data.cpp_exercises import CPP_EXERCISES

from data.bash_materials import BASH_MATERIALS
from data.bash_quizzes import BASH_QUIZZES as _BASH_QUIZZES
from data.bash_exercises import BASH_EXERCISES

from data.go_materials import GO_MATERIALS
from data.go_quizzes import GO_QUIZZES as _GO_QUIZZES
from data.go_exercises import GO_EXERCISES

# Posisi jawaban diratakan supaya kuis tidak bisa ditebak dari polanya.
# Lihat data/normalisasi.py untuk alasan lengkapnya.
JAVA_QUIZZES = seimbangkan_kuis(_JAVA_QUIZZES)
SQL_QUIZZES = seimbangkan_kuis(_SQL_QUIZZES)
PYTHON_QUIZZES = seimbangkan_kuis(_PYTHON_QUIZZES)
JAVASCRIPT_QUIZZES = seimbangkan_kuis(_JAVASCRIPT_QUIZZES)
C_QUIZZES = seimbangkan_kuis(_C_QUIZZES)
CPP_QUIZZES = seimbangkan_kuis(_CPP_QUIZZES)
BASH_QUIZZES = seimbangkan_kuis(_BASH_QUIZZES)
GO_QUIZZES = seimbangkan_kuis(_GO_QUIZZES)

__all__ = [
    "JAVA_MATERIALS", "JAVA_QUIZZES", "JAVA_EXERCISES",
    "SQL_MATERIALS", "SQL_QUIZZES", "SQL_EXERCISES",
    "PYTHON_MATERIALS", "PYTHON_QUIZZES", "PYTHON_EXERCISES",
    "JAVASCRIPT_MATERIALS", "JAVASCRIPT_QUIZZES", "JAVASCRIPT_EXERCISES",
    "C_MATERIALS", "C_QUIZZES", "C_EXERCISES",
    "CPP_MATERIALS", "CPP_QUIZZES", "CPP_EXERCISES",
    "BASH_MATERIALS", "BASH_QUIZZES", "BASH_EXERCISES",
    "GO_MATERIALS", "GO_QUIZZES", "GO_EXERCISES",
]
