"""
pycmath.pyx
"""

cdef extern from "c_math.h":
    int int_square(int x)

def py_int_square(int x):
    return int_square(x)
