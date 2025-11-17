# compile_grgates.py
import os
import sys
import shutil
from setuptools import setup
from Cython.Build import cythonize

# Detectar sistema operativo y carpeta de destino
if sys.platform.startswith("darwin"):
    target_dir = os.path.abspath("../cybitx/Mac")
    so_ext = ".so"
elif sys.platform.startswith("win"):
    target_dir = os.path.abspath("../cybitx/Windows")
    so_ext = ".pyd"
elif sys.platform.startswith("linux"):
    target_dir = os.path.abspath("../cybitx/Linux")
    so_ext = ".so"
else:
    target_dir = os.path.abspath("../cybitx/Other")
    so_ext = ".so"

os.makedirs(target_dir, exist_ok=True)

# Compilar módulos
for module in ["full_adder.pyx", "grgates.pyx"]:
    setup(
        name=os.path.splitext(module)[0],
        ext_modules=cythonize(module, compiler_directives={'language_level': "3"}),
        script_args=["build_ext", f"--build-lib={target_dir}", "--inplace"]
    )

# Limpiar archivos temporales generados por Cython
for file in os.listdir(os.getcwd()):
    if file.endswith((".c", ".html", so_ext)):
        os.remove(file)

if os.path.exists("build"):
    shutil.rmtree("build")

print(f"GRgates compilado correctamente en {target_dir}")
