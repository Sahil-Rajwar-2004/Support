from typing import Match
from support.matrix import Matrix, matrix
from support.stats import BinomialDist
import numpy as np


m1 = np.array([[1,2,3],[3,4,5],[5,6,7]])
m2 = matrix([[1,2,3],[3,4,5],[5,6,7]])


print(m1.mean())
print(m1.mean(axis = 0))
print(m1.mean(axis = 1))

print(m2.mean())
print(m2.mean(axis = 0).numpy())
print(m2.mean(axis = 1).numpy())

