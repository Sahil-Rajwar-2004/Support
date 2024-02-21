from .mathx import cos,sqrt

g = 9.8
G = 6.67430e-11
c = 299792458
k = 8.988e9
e = 8.85418e-12
h = 6.626e-34

def force(mass,acceleration):
    return mass * acceleration

def potential_energy(mass,height,gravity = g):
    return mass * gravity * height

def kinetic_energy(mass,velocity):
    return 0.5 * mass * velocity**2

def momentum(mass,velocity):
    return mass * velocity

def gravitational_force(mass1,mass2,distance):
    return G * mass1 * mass2 / distance**2

def speed(distance,time):
    return distance / time

def work(force,displacement,angle = 0):
    return force * displacement * cos(angle)

def coulombs_law(q1,q2,distance):
    return k * q1 * q2 / distance **2

def wave_speed(frequency):
    return h * frequency

def de_broglie_wavelength(mass,velocity):
    return h / (mass * velocity)

def binding_energy(mass,velocity = c):
    return mass * velocity**2

def time_dialation(time,velocity):
    return time / sqrt(1 - velocity**2 / c**2)

def length_contraction(length,velocity):
    return length / sqrt(1 - velocity**2 / c**2)

