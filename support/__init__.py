# Support (v-0.2.1)

version = "0.2.1"


from .algorithm import linear_search
from .algorithm import binary_search
from .algorithm import bubble_sort
from .algorithm import quick_sort
from .algorithm import insertion_sort
from .algorithm import selection_sort

from .boolean_algebra import AND
from .boolean_algebra import NAND
from .boolean_algebra import OR
from .boolean_algebra import NOR
from .boolean_algebra import XOR
from .boolean_algebra import XNOR
from .boolean_algebra import NOT
from .boolean_algebra import Buffer

from .file import SearchFile
from .file import FileFilter

from .iter import RandomNumberGenerator
from .iter import RangeGenerator
from .iter import PrimeGenerator

from .mapping import Mapping

from .mathx import INF
from .mathx import NAN
from .mathx import PI
from .mathx import EXP
from .mathx import mean
from .mathx import median
from .mathx import standard_deviation
from .mathx import variance
from .mathx import variance
from .mathx import Range
from .mathx import skewness
from .mathx import kurtosis
from .mathx import gaussian_distribution
from .mathx import percentile
from .mathx import quartile
from .mathx import iqr
from .mathx import cv
from .mathx import cc
from .mathx import mean_squared_error
from .mathx import mean_absolute_error
from .mathx import root_mean_squared_error
from .mathx import mean_absolute_deviation
from .mathx import covariance
from .mathx import zscore
from .mathx import compare
from .mathx import definite_integral
from .mathx import cos
from .mathx import sin
from .mathx import tan
from .mathx import cot
from .mathx import sec
from .mathx import cosec
from .mathx import cosh
from .mathx import sinh
from .mathx import tanh
from .mathx import coth
from .mathx import sech
from .mathx import cosech
from .mathx import deg2rad
from .mathx import rad2deg
from .mathx import fibonacci
from .mathx import factorial
from .mathx import palindrome
from .mathx import gcd
from .mathx import lcm
from .mathx import quadratic_roots
from .mathx import permutation
from .mathx import combination
from .mathx import precentage
from .mathx import precentage_change
from .mathx import floor
from .mathx import ceil
from .mathx import absolute
from .mathx import exp
from .mathx import sqrt
from .mathx import cbrt
from .mathx import is_prime
from .mathx import is_even
from .mathx import is_odd
from .mathx import primes
from .mathx import odds
from .mathx import evens
from .mathx import find_max
from .mathx import find_min
from .mathx import signum
from .mathx import summation
from .mathx import product
from .mathx import is_nan
from .mathx import is_inf

from .matrix import matrix
from .matrix import ones
from .matrix import zeros
from .matrix import identity
from .matrix import fill
from .matrix import Matrix

from .physics import g
from .physics import G
from .physics import c
from .physics import k
from .physics import e
from .physics import h
from .physics import force
from .physics import potential_energy
from .physics import kinetic_energy
from .physics import momentum
from .physics import gravitational_force
from .physics import speed
from .physics import work
from .physics import coulombs_law
from .physics import wave_speed
from .physics import de_broglie_wavelength
from .physics import binding_energy
from .physics import time_dialation
from .physics import length_contraction

from .transforms import DFT
from .transforms import DTFT

from .vector import vector
from .vector import Vector

__all__ = [
    "INF",
    "NAN",
    "PI",
    "EXP",
    "mean",
    "median",
    "standard_deviation",
    "variance",
    "Range",
    "skewness",
    "kurtosis",
    "gaussian_distribution",
    "percentile",
    "quartile",
    "iqr",
    "cv",
    "cc",
    "mean_squared_error",
    "mean_absolute_error",
    "root_mean_squared_error",
    "mean_absolute_deviation",
    "covariance",
    "zscore",
    "compare",
    "definite_integral",
    "cos",
    "sin",
    "tan",
    "cot",
    "sec",
    "cosec",
    "cosh",
    "sinh",
    "tanh",
    "coth",
    "sech",
    "cosech",
    "deg2rad",
    "rad2deg",
    "fibonacci",
    "factorial",
    "palindrome",
    "gcd",
    "lcm",
    "quadratic_roots",
    "permutation",
    "combination",
    "precentage",
    "precentage_change",
    "floor",
    "ceil",
    "absolute",
    "exp",
    "sqrt",
    "cbrt",
    "prime",
    "is_prime",
    "is_even",
    "is_odd",
    "primes",
    "odds",
    "evens",
    "find_max",
    "find_min",
    "signum",
    "summation",
    "product",
    "is_nan",
    "is_inf",
    "matrix",
    "ones",
    "zeros",
    "identity",
    "fill",
    "Matrix",
    "linear_search",
    "binary_search",
    "bubble_sort",
    "quick_sort",
    "insertion_sort",
    "selection_sort",
    "AND",
    "NAND",
    "OR",
    "NOR",
    "XOR",
    "XNOR",
    "NOT",
    "Buffer",
    "SearchFile",
    "FileFilter",
    "RandomNumberGenerator",
    "RangeGenerator",
    "PrimeGenerator",
    "Mapping",
    "g",
    "G",
    "c",
    "k",
    "e",
    "h",
    "force",
    "potential_energy",
    "kinetic_energy",
    "momentum",
    "gravitational_force",
    "speed",
    "work",
    "coulombs_law",
    "wave_speed",
    "de_broglie_wavelength",
    "binding_energy",
    "time_dialation",
    "length_contraction",
    "DFT",
    "DTFT",
    "vector",
    "Vector"
]
