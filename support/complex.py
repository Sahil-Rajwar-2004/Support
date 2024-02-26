r"""
Complex:
=======

A minimal Python library for working with complex numbers, which are used in engineering and solving equations that involve the square root of negative numbers.

Version: 0.0.2

Author: Sahil Rajwar

Attributes:
-----------
- Re (float): The real part of the complex number.
- Imag (float): The imaginary part of the complex number.

Methods:
--------
- __init__(Re=0.0, Imag=0.0): Initializes a complex number with the given real and imaginary parts.
- __repr__(): Returns a string representation of the complex number.
- __add__(other): Adds the complex number to another complex number or a scalar.
- __sub__(other): Subtracts another complex number or a scalar from the complex number.
- __mul__(other): Multiplies the complex number by another complex number or a scalar.
- __truediv__(other): Divides the complex number by another complex number or a scalar.
- __pow__(other): Raises the complex number to the power of another complex number or a scalar.
- __neg__(): Returns the negation of the complex number.
- __pos__(): Returns the complex number itself.
- conj(): Returns the complex conjugate of the complex number.
- arg(): Returns the argument of the complex number in radians.
- polar(): Returns the complex number in polar form.
- mod(): Returns the modulus (absolute value) of the complex number.

Usage:
------
# Create a complex number  
z1 = Complex(3, 4)  

# Perform arithmetic operations  
z2 = z1 + 2  
z3 = z1 * (1 + 2j)  

# Calculate the argument and modulus  
arg_z1 = z1.arg()  
mod_z1 = z1.mod()  

# Print the complex number  
print(z1)  # Output: [3.0,4.0]   


#NOTE that the output is in the square bracket where the number at first position is real and on the other hand second number is an imaginary number `[real,imag]` => `real +/- imag*j`
"""

import numpy as np

version = "0.0.2"

def euler(x):
    return Complex(np.cos(x),np.sin(x))

class Complex:
    def __init__(self,Re = 0.0,Imag = 0.0):
        self.Re = round(Re,16)
        self.Imag = round(Imag,16)
        
    def __repr__(self):
        if self.Imag < 0:
            return f"[{self.Re},{self.Imag}]"
        else:
            return f"[{self.Re},{self.Imag}]"

    def __add__(self,other):
        if isinstance(other,(int,float)):
            new_real = self.Re + other
            return Complex(new_real,self.Imag)
        elif isinstance(other,complex):
            new_real = self.Re + other.real
            new_imag = self.Imag + other.imag
            return Complex(new_real,new_imag)
        elif isinstance(other,Complex):
            new_real = self.Re + other.Re
            new_imag = self.Imag + other.Imag
            return Complex(new_real,new_imag)
        else:
            raise TypeError(f"'{type(other).__name__}' isn't compatible with 'Complex'!")

    def __sub__(self,other):
        if isinstance(other,(int,float)):
            new_real = self.Re - other
            return Complex(new_real,self.Imag)
        elif isinstance(other,complex):
            new_real = self.Re - other.real
            new_imag = self.Imag - other.imag
            return Complex(new_real,new_imag)
        elif isinstance(other,Complex):
            new_real = self.Re - other.Re
            new_imag = self.Imag - other.Imag
            return Complex(new_real,new_imag)
        else:
            raise TypeError(f"'{type(other).__name__}' isn't compatible with 'Complex'!")

    def __mul__(self,other):
        if isinstance(other,(int,float)):
            new_real = self.Re * other
            new_imag = self.Imag * other
            return Complex(new_real,new_imag)
        elif isinstance(other,complex):
            new_real = self.Re * other.real - self.Imag * other.imag
            new_imag = self.Re * other.imag + self.Imag * other.real
            return Complex(new_real,new_imag)
        elif isinstance(other,Complex):
            new_real = self.Re * other.Re - self.Imag * other.Imag
            new_imag = self.Re * other.Imag + self.Imag * other.Re
            return Complex(new_real,new_imag)
        else:
            raise TypeError(f"'{type(other).__name__}' isn't compatible with 'Complex'!")

    def __truediv__(self,other):
        if isinstance(other,(int,float)):
            if other == 0:
                raise ZeroDivisionError("division by zero is undefined!")
            new_real = self.Re / other
            new_imag = self.Imag / other
            return Complex(new_real,new_imag)
        elif isinstance(other,complex):
            other = Complex(other.real,other.imag)
            conj_denominator = other.conj()
            denominator = other.Re**2 + other.Imag**2
            numerator_real = self.Re * conj_denominator.Re - self.Imag * conj_denominator.Imag
            numerator_imag = self.Re * conj_denominator.Imag + self.Imag * conj_denominator.Re
            new_real = numerator_real / denominator
            new_imag = numerator_imag / denominator
            return Complex(new_real,new_imag)
        elif isinstance(other,Complex):
            return self * other.conj() / (other.Re**2 + other.Imag**2)
        else:
            raise TypeError(f"'{type(other).__name__}' isn't compatible with 'Complex'!")

    def __pow__(self,other):
        if isinstance(other,(int,float)):
            mod = self.mod() ** other
            arg = self.arg() * other
            real_part = mod * np.cos(arg)
            imag_part = mod * np.sin(arg)
            return Complex(real_part,imag_part)
        elif isinstance(other,complex) or isinstance(other,Complex):
            raise TypeError(f"to find the complex raise to the power complex isn't available/supported for version-0.0.2 of or below in complex.py module, try to install newer version or wait for update!")
        else:
            raise TypeError(f"'{type(other).__name__}' isn't compatible with 'Complex'!")

    def __neg__(self):
        new_real = -self.Re
        new_imag = -self.Imag
        return Complex(new_real,new_imag)

    def __pos__(self):
        return Complex(self.Re,self.Imag)

    def conj(self):
        return Complex(self.Re,-self.Imag)

    def arg(self):
        if self.Re == 0 and self.Imag != 0:
            if self.Imag > 0:
                return round(np.pi / 2,16)
            else:
                return round((-np.pi / 2) + np.pi,16)
        elif self.Re == 0 and self.Imag == 0:
            raise ValueError("undefined!")
        else:
            return round(np.arctan(self.Imag / self.Re),16)

    def polar(self):
        arg = self.arg()
        mod = self.mod()
        new_real = mod * np.cos(arg)
        new_imag = mod * np.sin(arg)
        return Complex(new_real,new_imag)

    def mod(self):
        return round(np.sqrt(self.Re**2 + self.Imag**2),16)
