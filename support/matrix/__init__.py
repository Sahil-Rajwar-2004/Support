"""
Matrix Module:
=============

this module provides functionality to handle various operations related to matrices,
including determinant calculation, cofactor, determination, transpositions, adjoint calculation, and more.
it also includes support for special matrices such as identity matrices, zero matrices, one matrices, and fill matrices.

for more detailed information on the methods and functions provided, please refer to the documentation below.

contributor: Sahil Rajwar
author: Sahil Rajwar
module-homepage: https://github.com/Sahil-Rajwar-2004/support/blob/master/support/matrix.py
"""

import numpy as np

version = "0.0.3"

def matrix(array):
    if isinstance(array,Matrix):
        return array
    return Matrix(array)

def zeros(dimension:tuple):
    return Matrix([[0 for _ in range(dimension[1])] for _ in range(dimension[0])])

def ones(dimension:tuple):
    return Matrix([[1 for _ in range(dimension[1])] for _ in range(dimension[0])])

def fill(value,dimension:tuple):
    return Matrix([[value for _ in range(dimension[1])] for _ in range(dimension[0])])

def eye(N):
    result = zeros((N,N))
    for i in range(N):
        result[i][i] = 1
    return result

def scaler(values):
    length = len(values)
    mat = zeros((length,length))
    for i in range(length):
        mat[i][i] = values[i]
    return mat

class Matrix:
    # initialization
    def __init__(self,array:list[list]|np.ndarray):
        self.__check_validity(array)
        self.__matrix = array
        self.__row = len(array)
        self.__column = len(array[0])
        self.__ndim = self.__shape = (self.__row,self.__column)
        self.__size = tuple([self.__row * self.__column])

    @property
    def length(self):
        return len(self.__matrix)

    @property
    def ndim(self):
        return self.__ndim

    @property
    def shape(self):
        return self.__shape

    @property
    def size(self):
        return self.__size

    def __repr__(self):
        return f"<Matrix object at {hex(id(self))}, shape = ({self.__row},{self.__column}), size = {self.__size}>"

    """
    def __repr__(self):
        digits = self.__count_digits()
        gaps = " " * (digits)
        representation = "matrix([\n"

        if len(self.__matrix) > 10:
            # show only first 5 rows
            for row in self.__matrix[:5]:
                representation += "  ["
                for x in row:
                    if isinstance(x,(int,float)):
                        representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
                    else:
                        raise TypeError(f"type '{type(x).__name__}' isn't supported in matrix")
                representation += "]\n"
            # add ellipsis
            representation += "  ...\n"
            # show last 5 rows
            for row in self.__matrix[-5:]:
                representation += "  ["
                for x in row:
                    if isinstance(x,(int,float)):
                        representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
                    else:
                        raise ValueError(f"type '{type(x).__name__}' isn't supported in matrix")
                representation += "]\n"
        else:
            # show all rows if less than or equal to 10
            for row in self.__matrix:
                representation += "  ["
                for x in row:
                    if isinstance(x,(int,float)):
                        representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
                    else:
                        raise ValueError(f"type '{type(x).__name__}' isn't supported in matrix")
                representation += "]\n"
        representation += f"],shape = {self.shape})"
        return representation
    """

    def numpy(self):
        return np.array(self.__matrix)

    def __getitem__(self,row,column = None):
        if row is not None and column is None:
            return self.__matrix[row]
        elif row is not None and column is not None:
            return self.__matrix[row][column]

    def __setitem__(self,row,value,column = None):
        if row is not None and column is None:
            if len(self.__matrix[row]) == len(value):
                self.__matrix[row] = value
            return
        if row is not None and column is not None:
            self.__matrix[row][column] = value
            return

    def __eq__(self,other):
        if isinstance(other,Matrix):
            if self.ndim == other.ndim:
                for row in range(self.__row):
                    for column in range(self.__column):
                        if self[row][column] != other[row][column]:
                            return False
                return True
            else:
                return False
        else:
            raise TypeError(f"type 'Matrix' and '{type(other).__name__}' aren't compatible for each other!")

    def __iter__(self):
        for row in self.__matrix:
            yield row

    def __check_validity(self,array):
        if isinstance(array,np.ndarray):
            if array.ndim == 2:
                buff = []
                for i in range(array.shape[0]):
                    buff.append(list(array[i]))
                return buff
            else:
                raise ValueError(f"array should be 2 dimension")
        for rows in array:
            if not isinstance(rows,list):
                raise TypeError(f"rows should be 'list' datatype not '{type(rows).__name__}'!")
            for columns in rows:
                if not isinstance(columns,(int,float)):
                    raise ValueError(f"each element in the matrix should have int/float only!")
        column = array[0]
        for x in array:
            if len(x) != len(column):
                raise ValueError(f"columns of the matrix must be equal")
        return True

    def __neg__(self):
        new_mat = [[-self.__matrix[row][col] for col in range(self.__column)] for row in range(self.__row)]
        return matrix(new_mat)

    def __pos__(self):
        return Matrix(self.__matrix)

    def __add__(self,other):
        if isinstance(other,(int,float)):
            return matrix([[x + other for x in row] for row in self.__matrix])
        elif isinstance(other,Matrix):
            if other.__row == 1 and other.__column == self.__column:
                return matrix([[x + y for x,y in zip(row,other.__matrix[0])] for row in self.__matrix])
            elif other.ndim == self.ndim:
                result = zeros(self.ndim)
                for row in range(self.__row):
                    for column in range(self.__column):
                        result[row][column] = self[row][column] + other[row][column]
                return result
        else:
            raise TypeError(f"type 'Matrix' and '{type(other).__name__}' aren't compatible for each other!")

    def __sub__(self,other):
        if isinstance(other,(int,float)):
            return matrix([[x - other for x in row] for row in self.__matrix])
        elif isinstance(other,Matrix):
            if other.__row == 1 and other.__column == self.__column:
                return matrix([[x - y for x,y in zip(row,other.__matrix[0])] for row in self.__matrix])
            elif other.ndim == self.ndim:
                result = zeros(self.ndim)
                for row in range(self.__row):
                    for column in range(self.__column):
                        result[row][column] = self[row][column] - other[row][column]
                return result
        else:
            raise TypeError(f"type 'Matrix' and '{type(other).__name__}' aren't compatible for each other!")

    def __mul__(self,other):
        if isinstance(other,(int,float)):
            return Matrix([[x * other for x in row] for row in self.__matrix])
        elif isinstance(other,Matrix):
            if other.__row == 1 and other.__column == self.__column:
                return Matrix([[x * y for x, y in zip(row,other.__matrix[0])] for row in self.__matrix])
            elif self.__column == other.__row:
                result = zeros((self.__row,other.__column))
                for i in range(self.__row):
                    for j in range(other.__column):
                        for k in range(self.__column):
                            result.__matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
                return result
            else:
                raise ValueError(f"number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication. {self.__column} != {other.__row}")
        else:
            raise TypeError(f"type 'Matrix' and '{type(other).__name__}' aren't compatible for each other!")

    def __pow__(self,other):
        if isinstance(other,(int,float)):
            return Matrix([[x ** other for x in row] for row in self.__matrix])
        return TypeError(f"Type 'Matrix' and '{type(other).__name__}' aren't compatible for each other!")

    def reduce_sum(self,axis = None,keepdims = False):
        if axis is None:
            return sum(self.flatten())
        elif axis == 0:
            result = [sum(row) for row in self.__matrix]
        elif axis == 1:
            result = []
            for column in range(self.__column):
                total = 0
                for row in range(self.__row):
                    total += self.__matrix[row][column]
                result.append(total)
        else:
            raise ValueError("axis out of range or not supported for 2D matrix!")

        if keepdims:
            if axis == 0:
                return Matrix([[value] for value in result])
            elif axis == 1:
                return Matrix([result])
        else:
            return result

    def mean(self,axis = None):
        if axis is None:
            return sum(self.flatten()) / self.size[0]
        elif axis == 1:
            return Matrix([[sum(row)/self.shape[1] for row in self.__matrix]])
        elif axis == 0:
            result = []
            for column in range(self.__column):
                total = 0
                for row in range(self.__row):
                    total += self.__matrix[row][column]
                result.append(total / self.__row)
            return Matrix([result])
        else:
            raise ValueError("axis out of range or not supported for > 2D array")

    def std(self,axis = None):
        if axis is None:
            mean = self.mean()
            variance = sum((x - mean) ** 2 for row in self.__matrix for x in row) / len(self.__matrix)
            return variance ** 0.5
        elif axis == 1:
            mean_cols = self.mean(axis = 0)
            std_devs = []
            for col in range(self.shape[1]):
                col_sum = sum((self.__matrix[row][col] - mean_cols[0][col]) ** 2 for row in range(self.shape[0]))
                std_dev = (col_sum / self.shape[0]) ** 0.5
                std_devs.append(std_dev)
            return Matrix(std_devs)
        elif axis == 0:
            mean_rows = self.mean(axis = 1)
            std_devs = []
            for row in range(self.shape[0]):
                row_sum = sum((self.__matrix[row][col] - mean_rows[row][0]) ** 2 for col in range(self.shape[1]))
                std_dev = (row_sum / self.shape[1]) ** 0.5
                std_devs.append([std_dev])
            return Matrix(std_devs)
        else:
            raise ValueError("axis out of range or not supported for > 2D array")

    def var(self,axis = None):
        if axis is None:
            mean = self.mean()
            variance = sum((element - mean) ** 2 for row in self.__matrix for element in row) / len(self.__matrix)
            return variance
        elif axis == 0:
            mean_cols = self.mean(axis=0)
            variances = []
            for col in range(self.shape[1]):
                column_sum = sum((self.__matrix[row][col] - mean_cols[0][col]) ** 2 for row in range(self.shape[0]))
                variance = column_sum / self.shape[0]
                variances.append(variance)
            return Matrix([variances])
        elif axis == 1:
            mean_rows = self.mean(axis=1)
            variances = []
            for row in range(self.shape[0]):
                row_sum = sum((self.__matrix[row][col] - mean_rows[row][0]) ** 2 for col in range(self.shape[1]))
                variance = row_sum / self.shape[1]
                variances.append([variance])
            return Matrix(variances)
        else:
            raise ValueError("axis out of range or not supported for > 2D array")

    def cofactor(self,row,column):
        minor_matrix = [row[:column] + row[column+1:] for row in (self.__matrix[:row] + self.__matrix[row+1:])]
        determinant = Matrix(minor_matrix).determinant()
        sign = (-1) ** (row + column)
        return determinant * sign

    def determinant(self):
        if self.__row != self.__column:
            raise ValueError("determinant is only defined for square matrices!")
        if self.__row == 1:
            return self.__matrix[0][0]
        if self.__row == 2:
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[0][1] * self.__matrix[1][0]
        det = 0
        for j in range(self.__column):
            det += ((-1) ** j) * self.__matrix[0][j] * self.__minor(0,j).determinant()
        return det

    def __minor(self, row, column):
        minor_matrix = [row[:column] + row[column + 1:] for row in (self.__matrix[:row] + self.__matrix[row + 1:])]
        return Matrix(minor_matrix)

    def transpose(self):
        return matrix([[x for x in row] for row in zip(*self.__matrix)])

    def adjoint(self):
        if self.__row != self.__column:
            raise ValueError("adjoint is only defined for square matrices!")
        cofactor_matrix = [[self.cofactor(i, j) for j in range(self.__column)] for i in range(self.__row)]
        cofactor_matrix_transpose = [[cofactor_matrix[j][i] for j in range(self.__column)] for i in range(self.__row)]
        return Matrix(cofactor_matrix_transpose)

    def is_square(self):
        return self.__row == self.__column

    def is_column(self):
        return self.__column == 1

    def is_row(self):
        return self.__row == 1

    def trace(self):
        if not self.is_square():
            raise ValueError(f"given matrix should have equal number of rows and columns: {self.__row} != {self.__column}")
        return sum(self.__matrix[i][i] for i in range(self.__row))

    def is_symetric(self):
        if not self.is_square():
            raise ValueError(f"given matrix should have equal number of rows and columns: {self.__row} != {self.__column}")
        return self == self.transpose()

    def is_skew_symmetric(self):
        if not self.is_square():
            raise ValueError(f"given matrix should have equal number of rows and columns: {self.__row} != {self.__column}")
        return self.scale(-1) == self.transpose()

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ZeroDivisionError(f"inverse of a matrix with 'zero' determinant doesn't exist!")
        return self.adjoint().scale(1 / det)

    def scale(self,scaler):
        return matrix([[x * scaler for x in row] for row in self.__matrix])

    def reshape(self,dimension):
        size = self.size[0]
        if dimension[0] * dimension[1] == size:
            result = zeros(dimension)
            for i in range(size):
                result.__matrix[i // dimension[1]][i % dimension[1]] = self.__matrix[i // self.__column][i % self.__column]
            return result
        else:
            raise ValueError(f"Can't reshape the matrix with dimension {self.ndim} to {dimension}!")

    def flatten(self):
        result = []
        for row in range(self.__row):
            for column in range(self.__column):
                result.append(self.__matrix[row][column])
        return result

    def head(self,index = 5):
        return matrix(self.__matrix[:index])

    def tail(self,index = 5):
        return matrix(self.__matrix[index:])

    def remove_row(self,index):
        if index < 0 or index >= self.__row:
            raise IndexError("index out of range!")
        self.__matrix = [row for i,row in enumerate(self.__matrix) if i != index]
        return matrix(self.__matrix)

    def remove_column(self,index):
        if index < 0 or index >= self.__column:
            raise IndexError("index out of range!")
        self.__matrix = [[row[i] for i in range(self.__column) if i != index] for row in self.__matrix]
        return matrix(self.__matrix)

    def add_row(self,row,index = None):
        if len(row) != self.__column:
            raise ValueError("The length of the row must match the number of columns in the matrix.")
        if index is None:
            new_matrix = self.__matrix + [row]
        else:
            new_matrix = self.__matrix[:index] + [row] + self.__matrix[index:]
        return Matrix(new_matrix)

    def add_column(self,column,index = None):
        if len(column) != self.__row:
            raise ValueError("The length of the column must match the number of rows in the matrix.")
        if index is None:
            new_matrix = [self.__matrix[i] + [column[i]] for i in range(self.__row)]
        else:
            new_matrix = [self.__matrix[i][:index] + [column[i]] + self.__matrix[i][index:] for i in range(self.__row)]
        return Matrix(new_matrix)

    def to_list(self):
        return self.__matrix

