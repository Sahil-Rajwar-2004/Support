from .__init__ import Matrix,zeros
import numpy as np

def cos(matrix: Matrix) -> Matrix:
    if not isinstance(matrix,Matrix):
        raise TypeError(f"`{type(matrix).__mame__}` isn't compatible for `Matrix`")
    return Matrix(np.cos(matrix.numpy()))

def sin(matrix: Matrix) -> Matrix:
    return Matrix(np.sin(matrix.numpy()))


