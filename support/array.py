from .matrix import matrix

version = "0.0.1"

def array(array):
    return Array(array)

def zeros(dimension):
    if len(dimension) == 1:
        return array([0] * dimension[0])
    elif len(dimension) == 2:
        return array([[0 for x in range(dimension[1])] for y in range(dimension[0])])
    else:
        raise ValueError("dimension should be 1D or 2D!")

def ones(dimension):
    if len(dimension) == 1:
        return array([1] * dimension[0])
    elif len(dimension) == 2:
        return array([[1] * dimension[1]] * dimension[0])
    else:
        raise ValueError("dimension should be 1D or 2D!")

def fill(value,dimension):
    if len(dimension) == 1:
        return array([value] * dimension[0])
    elif len(dimension) == 2:
        return array([[value] * dimension[1]] * dimension[0])
    else:
        raise ValueError("dimension should be 1D or 2D!")

class Array:
    def __init__(self,array):
        self.__validate = self.__check_validity(array)
        self.__array = array
        if self.__validate:
            self.dim = self.shape = (len(self.__array),)
        else:
            self.dim = self.shape = (len(self.__array),len(self.__array[0]))
            self.__row = len(self.__array)
            self.__column = len(self.__array[0])

    def __repr__(self):
        digits = self.__count_digits()
        gaps = " " * digits
        representation = "array(["
        if self.__validate:
            if len(self.__array) > 10:
                # Display first five elements
                for x in self.__array[:5]:
                    if len(str(x)) > 8:
                        x = f"{x:.5e}"
                    representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
                # Omitted elements placeholder
                representation += " ..."
                # Display last five elements
                for x in self.__array[-5:]:
                    if len(str(x)) > 8:
                        x = f"{x:.5e}"
                    representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
            else:
                # Display all elements
                for x in self.__array:
                    if len(str(x)) > 8:
                        x = f"{x:.5e}"
                    representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
        else:
            representation += "\n"
            if len(self.__array) > 10:
                # Show only first 5 rows
                for row in self.__array[:5]:
                    representation += "  ["
                    for x in row:
                        if isinstance(x,(int,float)):
                            representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
                        else:
                            raise TypeError(f"type '{type(x).__name__}' isn't supported in matrix")
                    representation += "]\n"
                # Add ellipsis
                representation += "  ...\n" 
                # Show last 5 rows
                for row in self.__array[-5:]:
                    representation += "  ["
                    for x in row:
                        if isinstance(x,(int,float)):
                            representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
                        else:
                            raise ValueError(f"type '{type(x).__name__}' isn't supported in matrix")
                    representation += "]\n"
            else:
                # Show all rows if less than or equal to 10
                for row in self.__array:
                    representation += "  ["
                    for x in row:
                        if isinstance(x,(int,float)):
                            representation += " " + gaps[:digits - len(str(x))] + f"{x}" + " "
                        else:
                            raise ValueError(f"type '{type(x).__name__}' isn't supported in matrix")
                    representation += "]\n" 
        representation += f"],shape = {self.shape})"
        return representation 

    def __check_validity(self,array):
        initial = array[0]
        # check if it's a 2D array or 1D array
        if isinstance(initial,list):
            for index,rows in enumerate(array,start = 1):
                if not isinstance(rows,list):
                    raise TypeError(f"type '{type(rows).__name__}' isn't match with '{type(initial).__name__}' at index '{index}'!")
                if not len(rows) == len(initial):
                    raise ValueError(f"length of entire row of a 2D array must be equal!")
            return False # False if it's a 2D array
        elif isinstance(initial,(int,float)):
            for index,x in enumerate(array,start = 1):
                if not isinstance(x,(int,float)):
                    raise TypeError(f"'{type(x).__name__}' isn't match with '{type(initial).__name__}' at index '{index}'!")
            return True # True if it's a 1D array
        else:
            raise TypeError(f"'{type(initial).__name__}' isn't compatible for array!")
    
    def __len__(self):
        return len(self.__array)

    def __getitem__(self,index):
        return self.__array[index]

    def __setitem__(self,index,value):
        self.__array[index] = value

    def __add__(self,other):
        if self.__validate:
            result = []
            if isinstance(other,(int,float)):
                for i in range(len(self.__array)):
                    result.append(other + self.__array[i])
                return array(result)
            elif isinstance(other,Array):
                if len(self.__array) != len(other.__array):
                    raise ValueError("length of arrays should be equal!")
                for x,y in zip(self.__array,other.__array):
                    result.append(x + y)
                return array(result)
        else:
            result = []
            if isinstance(other,(int,float)):
                for rows in range(self.__row):
                    item = []
                    for columns in range(self.__column):
                        item.append(self.__array[rows][columns] + other)
                    result.append(item) 
                return array(result)
            elif isinstance(other,Array):
                if not (self.__row == other.__row and self.__column == other.__column):
                    raise ValueError("matrices with different dimensions can't be add!")
                result = []
                for rows in range(self.__row):
                    item = []
                    for columns in range(self.__column):
                        item.append(self.__array[rows][columns] + other.__array[rows][columns])
                    result.append(item)
                return array(result)

    def __sub__(self,other):
        if self.__validate:
            result = []
            if isinstance(other,(int,float)):
                for i in range(len(self.__array)):
                    result.append(other - self.__array[i])
                return array(result)
            elif isinstance(other,Array):
                if len(self.__array) != len(other.__array):
                    raise ValueError("length of arrays should be equal!")
                for x,y in zip(self.__array,other.__array):
                    result.append(x - y)
                return array(result)
        else:
            result = []
            if isinstance(other,(int,float)):
                for rows in range(self.__row):
                    item = []
                    for columns in range(self.__column):
                        item.append(self.__array[rows][columns] - other)
                    result.append(item) 
                return array(result)
            elif isinstance(other,Array):
                if not (self.__row == other.__row and self.__column == other.__column):
                    raise ValueError("matrices with different dimensions can't be add!")
                result = []
                for rows in range(self.__row):
                    item = []
                    for columns in range(self.__column):
                        item.append(self.__array[rows][columns] - other.__array[rows][columns])
                    result.append(item)
                return array(result)

    def __mul__(self,other):
        if self.__validate:
            result = []
            if isinstance(other,(int,float)):
                for i in range(len(self.__array)):
                    result.append(other * self.__array[i])
                return array(result)
            elif isinstance(other,Array):
                if len(self.__array) != len(other.__array):
                    raise ValueError("length of arrays must be equal")
                for x,y in zip(self.__array,other.__array):
                    result.append(x * y)
                return result
        else:
            if isinstance(other,(int,float)):
                return Array([[x * other for x in row] for row in self.__array])
            elif isinstance(other,Array):
                if other.__row == 1 and other.__column == self.__column:
                    return Array([[x * y for x, y in zip(row,other.__array[0])] for row in self.__array])
                elif self.__column == other.__row:
                    result = zeros((self.__row,other.__column))
                    for i in range(self.__row):
                        for j in range(other.__column):
                            for k in range(self.__column):
                                result.__array[i][j] += self.__array[i][k] * other.__array[k][j]
                    return result
                else:
                    raise ValueError(f"number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication. {self.__column} != {other.__row}")
            else:
                raise TypeError(f"type 'Array' and '{type(other).__name__}' aren't compatible for each other!")
    
    def head(self,n = 5):
        return array(self.__array[:n])

    def tail(self,n = 5):
        return array(self.__array[-n:])

    def __count_digits(self):
        initial = 1
        if self.__validate:
            for item in self.__array:
                initial = max(initial,len(str(item)))
        else:
            for rows in self.__array:
                for columns in rows:
                    initial = max(initial,len(str(columns)))
        return initial

    def to_matrix(self):
        return matrix(self.__array)

    def transpose(self):
        return array([[x for x in row] for row in zip(*self.__array)])

    def flatten(self):
        if self.__validate:
            return self
        result = []
        for row in range(self.__row):
            for column in range(self.__column):
                result.append(self.__array[row][column])
        return array(result)

    def reduced_sum(self,axis = None,keepdims = False):
        if self.__validate and axis is None and keepdims == False:
            return sum(self.__array)
        if axis is None:
            return sum(self.flatten())
        elif axis == 0:
            result = [sum(row) for row in self.__array]
        elif axis == 1:
            result = []
            for column in range(self.__column):
                total = 0
                for row in range(self.__row):
                    total += self.__array[row][column]
                result.append(total)
        else:
            raise ValueError("axis is out of range or not supported for 2D array")

        if keepdims:
            if axis == 0:
                return array([[value] for value in result])
            elif axis == 1:
                return array([result])
        else:
            return result

