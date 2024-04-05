from .vector import vector
import numpy as np

version = "0.0.1"

def cartesian(points):
    if len(points) == 3:
        return Cartesian(points[0],points[1],points[2])
    raise ValueError(f"length of an array should be equals to 3: {len(points)} != 3")

def spherical(points):
    if len(points) == 3:
        return Spherical(points[0],points[1],points[2])
    raise ValueError(f"length of an array should be equals to 3: {len(points)} != 3")


class Cartesian:
    def __init__(self,x = 0.0,y = 0.0,z = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return f"<Cartesian object at {hex(id(self))}>"
    
    def numpy(self):
        return np.array([self.x,self.y,self.z])

    def to_vector(self):
        return vector([self.x,self.y,self.z])

    def to_list(self):
        return [self.x,self.y,self.z]

    def to_spherical(self):
        r = np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        theta = np.arctan(self.y / self.x)
        phi = np.arccos(self.z / r)
        return Spherical(r,theta,phi)

class Spherical:
    def __init__(self,r = 0.0,theta = 0.0,phi = 0.0):
        self.r = float(r)
        self.theta = float(theta)
        self.phi = float(phi)

    def __repr__(self):
        return f"spherical([{self.r}, {self.theta}, {self.phi}])"

    def to_vector(self):
        return vector([self.r,self.theta,self.phi])

    def to_list(self):
        return [self.r,self.theta,self.phi]

    def to_cartesian(self):
        x = self.r * np.sin(self.phi) * np.cos(self.theta)
        y = self.r * np.sin(self.phi) * np.sin(self.theta)
        z = self.r * np.cos(self.phi)
        return Cartesian(x,y,z)

