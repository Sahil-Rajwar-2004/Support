import numpy as np
from matrix import Matrix

version = "0.0.1"

def sin(matrix: Matrix):
    return Matrix(np.sin(matrix.numpy()))

def cos(matrix: Matrix):
    return Matrix(np.cos(matrix.numpy()))

def tan(matrix: Matrix):
    return Matrix(np.tan(matrix.numpy()))

def cosec(matrix: Matrix):
    return Matrix(1 / np.sin(matrix.numpy()))

def sec(matrix: Matrix):
    return Matrix(1 / np.cos(matrix.numpy()))

def cot(matrix: Matrix):
    return Matrix(1 / np.tan(matrix.numpy()))

def log(matrix: Matrix,base: None|int|float = None):
    if base is None:
        return Matrix(np.log(matrix.numpy()))
    else:
        return Matrix(np.log(matrix.numpy()) / np.log(base))

def pow(matrix: Matrix,exponent: int|float):
    return Matrix(matrix.numpy() ** exponent)

def exp(matrix: Matrix):
    return Matrix(np.exp(matrix.numpy()))

