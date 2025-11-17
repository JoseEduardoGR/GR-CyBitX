# compile_grgates.py
import os
import sys
import shutil
from setuptools import setup
from Cython.Build import cythonize

# Detectar sistema operativo y carpeta de destino
if sys.platform.startswith("darwin"):
    target_dir = os.path.abspath("../cybitx/Mac")
elif sys.platform.startswith("win"):
    target_dir = os.path.abspath("../cybitx/Windows")
elif sys.platform.startswith("linux"):
    target_dir = os.path.abspath("../cybitx/Linux")
else:
    target_dir = os.path.abspath("../cybitx/Other")

os.makedirs(target_dir, exist_ok=True)

# Compilar el .pyx directamente en target_dir
setup(
    name="GRgates",
    ext_modules=cythonize(
        "grgates.pyx",
        compiler_directives={'language_level': "3"},
    ),
    script_args=["build_ext", f"--build-lib={target_dir}", "--inplace"]
)

# Limpiar archivos temporales que crea Cython
temp_dirs = ["build", "grgates.c", "grgates.html","grgates.cpython-313-darwin.so"]
for d in temp_dirs:
    path = os.path.join(os.getcwd(), d)
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

print(f"GRgates compilado correctamente en {target_dir}")
