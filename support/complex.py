import numpy as np

version = "0.0.2"

class Complex:
    def __init__(self,z):
        if isinstance(z,(int,float)):
            z = complex(z)
        if isinstance(z,Complex):
            z = complex(z.z)
        self.z = z
        self.__check_dtype(z)

    def __repr__(self):
        return f"[{self.z.real} {self.z.imag}]"

    def __check_dtype(self,z):
        if not isinstance(z,(int,float,complex,Complex)):
            raise TypeError(f"type '{type(z).__name__}' isn't compatible with 'Complex' type!")

    def __add__(self,other):
        if isinstance(other,(int,float)):
            return Complex(other + self.z)
        elif isinstance(other,complex):
            return Complex(self.z + other)
        elif isinstance(other,Complex):
            return Complex(self.z + other.z)
        else:
            raise TypeError(f"'type {type(other).__name__}' isn't compatible with 'Complex' type!")

    def __sub__(self,other):
        if isinstance(other,(int,float)):
            return Complex(self.z - other)
        elif isinstance(other,complex):
            return Complex(self.z - other)
        elif isinstance(other,Complex):
            return Complex(self.z - other.z)
        else:
            raise TypeError(f"type '{type(other).__name__}' isn't compatible with 'Complex' type!")

    def __mul__(self,other):
        if isinstance(other,(int,float)):
            return Complex(self.z * other)
        elif isinstance(other,complex):
            return Complex(self.z * other)
        elif isinstance(other,Complex):
            return Complex(self.z * other.z)
        else:
            raise TypeError(f"type '{type(other).__name__}' isn't compatible with 'Complex' type!")

    def __truediv__(self,other):
        if isinstance(other,(int,float)):
            return Complex(self.z / other)
        elif isinstance(other,complex):
            return Complex(self.z / other)
        elif isinstance(other,Complex):
            return Complex(self.z / other.z)
        else:
            raise TypeError(f"type '{type(other).__name__}' isn't compatible with 'Complex' type!")

    def __pow__(self,other):
        if isinstance(other,(int,float)):
            return Complex(self.z ** other)
        elif isinstance(other,complex):
            return Complex(self.z ** other)
        elif isinstance(other,Complex):
            return Complex(self.z ** other.z)
        else:
            raise TypeError(f"type '{type(other).__name__}' isn't compatible with 'Complex' type!")

    def __neg__(self):
        return Complex(-self.z)

    def __pos__(self):
        return Complex(self.z)

    def arg(self):
        return np.arctan2(self.z.imag / self.z.real)

    def conj(self):
        return Complex(self.z.real + self.z.imag * 1j)

    def mod(self):
        return np.sqrt(self.z.real ** 2 + self.z.imag ** 2)

