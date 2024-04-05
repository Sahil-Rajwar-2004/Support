"""
Vector:
======

a minimal python module to solve vectors related problems
keep in mind that this whole module is written for cartesian plane only
"""


from .mathx import sqrt,find_min
import numpy as np

version = "0.0.2"

def vector(array):
    if len(array) == 3:
        return Vector(float(array[0]),float(array[1]),float(array[2]))
    raise ValueError(f"length of an array should be equals to 3: {len(array)} != 3")

class Vector:
    def __init__(self,i = 0.0,j = 0.0,k = 0.0):
        self.i = i
        self.j = j
        self.k = k
        self.__components = [self.i,self.j,self.k]

    def __repr__(self):
        return repr([self.i,self.j,self.k])

    def __add__(self,vector):
        return Vector(self.i + vector.i,self.j + vector.j,self.k + vector.k)

    def __sub__(self,vector):
        return Vector(self.i - vector.i,self.j - vector.j,self.k - vector.k)

    def __mul__(self,vector):
        return self.i * vector.i + self.j * vector.j + self.k * vector.k

    def __matmul__(self,vector):
        I = self.j * vector.k - self.k * vector.j
        J = self.k * vector.i - self.i * vector.k
        K = self.i * vector.j - self.j * vector.i
        return Vector(I,J,K)

    def __truediv__(self,vector):
        return Vector(self.i / vector.i,self.j / vector.j,self.k / vector.k)

    def __floordiv__(self,vector):
        return Vector(self.i // vector.i,self.j // vector.j,self.k // vector.k)

    def __pow__(self,value):
        return Vector(self.i ** value,self.j ** value,self.k ** value)

    def __getitem__(self,component):
        if component.lower() == "i":
            return self.i
        elif component.lower() == "j":
            return self.j
        elif component.lower() == "k":
            return self.k
        else:
            raise ValueError(f"unidentified component: expected i,I,j,J,k or K but got {component}!")
        
    def __setitem__(self,component,value):
        if component.lower() == "i":
            self.i = value
        elif component.lower() == "j":
            self.j = value
        elif component.lower() == "k":
            self.k = value
        else:
            raise ValueError(f"unidentified component: expected i,I,j,J,k or K but got {component}!")

    def __eq__(self,vector):
        if self.i == vector.i and self.j == vector.j and self.k == vector.k:
            return True
        return False

    def __neg__(self):
        return Vector(-self.i,-self.j,-self.k)

    def __pos__(self):
        return Vector(self.i,self.j,self.k)

    def __ne__(self,vector):
        if not self == vector:
            return True
        return False
    
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index < len(self.__components):
            result = self.__components[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration

    def is_orthogonal(self,vector):
        return self * vector == 0
    
    def is_zero(self):
        if self.i == 0.0 and self.j == 0.0 and self.k == 0.0:
            return True
        return False

    def is_one(self):
        if self.i == 1 and self.j == 1 and self.k == 1:
            return True
        return False

    def scaling(self,scaler):
        return Vector(self.i * scaler,self.j * scaler,self.k * scaler)

    def cross(self,vector):
        return self @ vector

    def dot(self,vector):
        return self * vector

    def magnitude(self):
        return sqrt(self * self)
    
    def distance(self,vector):
        return sqrt((self.i - vector.i)**2 + (self.j - vector.j)**2 + (self.k- vector.k)**2)
    
    def unit(self):
        mag = self.magnitude()
        return Vector(self.i / mag,self.j / mag,self.k / mag)
    
    def angle(self,vector):
        dot = self * vector
        mag = self.magnitude() * vector.magnitude()
        if mag == 0:
            return -1
        cosine = dot / mag
        angle = find_min([1.0,max([-1,cosine])])
        return np.arccos(angle)

    def get(self,index):
        if not 0 <= index <= 2:
            raise IndexError("index out of bound, ranges lie between 0 to 2!")
        if index == 0:
            return self.i
        elif index == 1:
            return self.j
        elif index == 2:
            return self.k
        else:
            raise TypeError(f"expected integer value but got {type(index).__name__}!")

    def gradient(self,delta=1.0):
        """
        computes the gradient of the vector.

        parameters:
        - delta (float): the spacing between points for finite differences.

        returns:
        - Vector: the gradient vector.
        """
        # Compute the gradient using finite differences
        dx = (self + Vector(delta,0,0) - self) / delta
        dy = (self + Vector(0,delta,0) - self) / delta
        dz = (self + Vector(0,0,delta) - self) / delta
        return Vector(dx,dy,dz)

    def to_list(self):
        return [self.i,self.j,self.k]

    def octant(self):
        if self.i == 0 and self.j == 0 and self.k == 0:
            return 0
        elif self.i > 0 and self.j > 0 and self.k > 0:
            return 1
        elif self.i < 0 and self.j > 0 and self.k > 0:
            return 2
        elif self.i < 0 and self.j < 0 and self.k > 0:
            return 3
        elif self.i  > 0 and self.j < 0 and self.k > 0:
            return 4
        elif self.i > 0 and self.j > 0 and self.k < 0:
            return 5
        elif self.i < 0 and self.j > 0 and self.k < 0:
            return 6
        elif self.i < 0 and self.j < 0 and self.k < 0:
            return 7
        elif self.i > 0 and self.j < 0 and self.k < 0:
            return 8
        else:
            raise ValueError("an error occurred!")

