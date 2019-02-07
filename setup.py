"""
setup.py
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

cmath_extension = Extension(
        name = "ccmath",
        sources = ["pycmath.pyx", "c_math.c"],
        )

setup(
    ext_modules=cythonize([cmath_extension])
    )
