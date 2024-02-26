"""
Matrix Module:
=============

this module provides functionality to handle various operations related to matrices, 
including determinant calculation, cofactor, determination, transpositions, adjoint calculation, and more. 
it also includes support for special matrices such as identity matrices, zero matrices, one matrices, and fill matrices.

for more detailed information on the methods and functions provided, please refer to the documentation below.

contributor: Sahil Rajwar
author: Sahil Rajwar
homepage: https://github.com/Sahil-Rajwar-2004/support

implementation:
    >>> from support.matrix import matrix       # importing essential library
    >>> x = matrix([[1,2,3],[4,5,6],[7,8,9]])   # call the function matrix() to create matrix from nested list
    >>> print(x)
    >>> matrix([
              [ 1  2  3 ]
              [ 4  5  6 ]
              [ 7  8  9 ]
            ],shape = (3, 3))
"""

version = "0.0.2"

def matrix(array):
    """
        this function will simply convert an array to matrix format instead using class
        NOTE: this function will accept only `2D` arrays

        parameters:
            array: 2D list only as an input

        implementations:
            >>> from support.matrix import matrix
            >>> x = matrix([[1,2,3],[4,5,6],[6,7,8]])
            >>> print(x)
            >>> matrix([
                  [ 1  2  3 ]
                  [ 4  5  6 ]
                  [ 7  8  9 ]
                ],shape = (3, 3))
    """
    return Matrix(array)

def zeros(dimension):
    """
        this function take dimension (rows,columns) and return the matrix of shape (rows,columns)
        and fill each element with zero values

        parameters:
            dimension: tuple of int datatype row and column (row,column)

        implementations:
            >>> from support.matrix import zeros
            >>> x = zeros((2,3))
            >>> print(x)
            >>> matrix([
                  [ 0  0  0 ]
                  [ 0  0  0 ]
                ],shape = (2, 3))
    """
    return Matrix([[0 for x in range(dimension[1])] for y in range(dimension[0])])

def ones(dimension):
    """
        this function will create matrix where each element filled with value 1
        of dimension given by the user

        parameters:
            dimension: tuple of int datatype row and column (row,column)

        implementations:
            >>> from support.matrix import ones
            >>> x = ones((2,3))
            >>> print(x)
            >>> matrix([
                  [ 1  1  1 ]
                  [ 1  1  1 ]
                ],shape = (2, 3))
    """
    return Matrix([[1 for x in range(dimension[1])] for y in range(dimension[0])])


def fill(value,dimension):
    """
        this function will create matrix where each element filled with value and 
        dimension which will be given by the user!
       
        parameters:
            value: any datatype
            dimension: tuple of int datatype row and column (row,column)
        
        implementations:
            >>> from support.matrix import fill
            >>> x = fill((2,3),float("nan"))
            >>> print(x)
            >>> matrix([
                  [ nan  nan  nan ]
                  [ nan  nan  nan ]
                ],shape = (2, 3))
    """
    return Matrix([[value for x in range(dimension[1])] for y in range(dimension[0])])

def identity(row_col):
    """
        this function will create square matrix, a square matrix have same number of rows and columns
        rows = columns. And fill the diagonal from top left to bottom right with value 1

        parameters:
            dimensions:
        
        implementations:
            >>> from support.matrix import identity
            >>> x = identity(row_col)
            >>> print(x)
            >>> matrix([
                  [ 1  0  0 ]
                  [ 0  1  0 ]
                  [ 0  0  1 ]
                ],shape = (3, 3))
    """
    result = zeros((row_col,row_col))
    for i in range(row_col):
        for j in range(row_col):
            if i == j:
                result[i][j] = 1
    return result

class Matrix:
    # initialization
    def __init__(self,array):
        self.__check_validity(array)
        self.__matrix = array
        self.__row = len(array)
        self.__column = len(array[0])
        self.dim = self.shape = (self.__row,self.__column)
        self.size = tuple([self.__row * self.__column])

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

    def __getitem__(self,row,column = None):
        # get item using index

        """
            >>> from support.matrix import matrix
            >>> x = matrix([[1,2,3],[4,5,6],[7,8,9]])
            >>> print(x[0])
            >>> [1, 2, 3]
            >>> print(x[0][0])
            >>> 1
        """

        if row is not None and column is None:
            return self.__matrix[row]
        elif row is not None and column is not None:
            return self.__matrix[row][column]

    def __setitem__(self,row,value,column = None):
        """
            >>> from support.matrix import matrix
            >>> x = matrix([[1,2,3],[4,5,6],[7,8,9]])
            >>> x[0] = [12,13,14]
            >>> print(x)
            >>> matrix([
                  [ 12  13  14 ]
                  [  4   5   6 ]
                  [  7   8   9 ]
                ])
            >>> x[0][0] = 100
            >>> print(x)
            >>> matrix([
                  [ 100   13   14 ]
                  [   4    5    6 ]
                  [   7    8    9 ]
                ])
        """
        if row != None and column == None:
            if len(self.__matrix[row]) == len(value):
                self.__matrix[row] = value
        if row != None and column != None:
            self.__matrix[row][column] = value

    def __eq__(self,other):
        if isinstance(other,Matrix):
            if self.dim == other.dim:
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

    def __count_digits(self):
        initial = 1
        for row in self.__matrix:
            for item in row:
                initial = max(initial, len(str(item)))
        return initial
    
    def __check_validity(self,array):
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

    def __add__(self,other):
        if isinstance(other,(int,float)):
            return matrix([[x + other for x in row] for row in self.__matrix])
        elif isinstance(other,Matrix):
            if other.__row == 1 and other.__column == self.__column:
                return matrix([[x + y for x,y in zip(row,other.__matrix[0])] for row in self.__matrix])
            elif other.dim == self.dim:
                result = zeros(self.dim)
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
            elif other.dim == self.dim:
                result = zeros(self.dim)
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
            det += ((-1) ** j) * self.__matrix[0][j] * self.__minor(0, j).determinant()
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
        return self.__row == 1

    def is_row(self):
        return self.__column == 1
    
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
            raise ValueError(f"Can't reshape the matrix with dimension {self.dim} to {dimension}!")

    def flatten(self):
        result = []
        for row in range(self.__row):
            for column in range(self.__column):
                result.append(self.__matrix[row][column])
        return result
    
    def head(self,index = 5):
        #zero_matrix = zeros((self.__row,self.__column))
        return matrix(self.__matrix[:index])
    
    def tail(self,index = 5):
        return matrix(self.__matrix[index:])

    def remove_row(self,index):
        """
            remove row at a given index

            Args:
                index (int): specific row to delete

            Returns:
                Matrix: the same matrix with removed row at an index

            Example:
                >>> x = Matrix([[1, 2, 3],[4, 5, 6]])
                >>> x.remove_row(index = 1)
                matrix([
                  [  1  2  3 ]
                  [  7  8  9 ]
                ],shape = (2, 3))

        """
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
        """
        adds a new row to the matrix.

        Args:
            row (list): the row to be added.
            index (int or None): the index at which to add the row. If None, the row is added at the end.

        Returns:
            Matrix: a new matrix with the added row.

        Example:
            >>> x = Matrix([[1, 2, 3], [4, 5, 6]])
            >>> x.add_row([7, 8, 9])
            matrix([
              [ 1  2  3 ]
              [ 4  5  6 ]
              [ 7  8  9 ]
            ],shape = (3, 3))
            >>> x.add_row([10, 11, 12], index=1)
            matrix([
              [  1  2  3 ]
              [ 10 11 12 ]
              [  4  5  6 ]
              [  7  8  9 ]
            ],shape = (4, 3))
        """
        if len(row) != self.__column:
            raise ValueError("The length of the row must match the number of columns in the matrix.")
        if index is None:
            new_matrix = self.__matrix + [row]
        else:
            new_matrix = self.__matrix[:index] + [row] + self.__matrix[index:]
        return Matrix(new_matrix)

    def add_column(self,column,index = None):
        """
        adds a new column to the matrix.

        Args:
            column (list): the column to be added.
            index (int or None): the index at which to add the column. If None, the column is added at the end.

        Returns:
            matrix: a new matrix with the added column.

        Example:
            >>> x = Matrix([[1, 2], [3, 4]])
            >>> x.add_column([5, 6])
            matrix([
              [ 1  2  5 ]
              [ 3  4  6 ]
            ], shape = (2, 3))
            >>> x.add_column([7, 8], index=1)
            matrix([
              [ 1  7  2  ]
              [ 3  8  4  ]
            ], shape = (2, 3))
        """
        if len(column) != self.__row:
            raise ValueError("The length of the column must match the number of rows in the matrix.")
        if index is None:
            new_matrix = [self.__matrix[i] + [column[i]] for i in range(self.__row)]
        else:
            new_matrix = [self.__matrix[i][:index] + [column[i]] + self.__matrix[i][index:] for i in range(self.__row)]
        return Matrix(new_matrix)


