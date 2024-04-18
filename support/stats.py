from .algorithm import bubble_sort
from .mathx import combination
import numpy as np


class BinomialDist:
    def __init__(self,n_trials,prob_success,random_var):
        self.__trials = n_trials
        self.__prob = prob_success
        self.__rand_var = random_var

    def __repr__(self):
        return f"<trials = {self.__trials}, prob_success = {self.__prob}, random_var = {self.__rand_var}>"

    def pmf(self):
        return combination(self.__trials,self.__rand_var) * (self.__prob ** self.__rand_var) * (1 - self.__prob) ** (self.__trials - self.__rand_var)

    def cdf(self):
        values = sum(self.pmf() for k in range(self.__rand_var + 1))
        return values
    
    def mean(self):
        return self.__trials * self.__prob

    def var(self):
        return self.__trials * self.__prob * (1 - self.__prob)

    def std(self):
        return self.var() ** 0.5

def mean(array):
    return sum(array) / len(array)

def median(array):
    array = bubble_sort(array)
    n = len(array)
    mid = n // 2
    if n % 2 == 0:
       return (array[n - 1] + array[n - 2]) / 2
    else:
        return array[mid]

def mode(array):
    counts = {}
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = max(counts.values())
    modes = [num for (num, count) in counts.items() if count == max_count]
    return modes if len(modes) > 1 else modes[0]

def std(array,sample = False):
    N = len(array)
    if sample:
        N -= 1
    m = mean(array)
    diff = [(x - m)**2 for x in array]
    return np.sqrt(summation(diff)/N)

def var(array,sample = False):
    return std(array,sample)**2

def quartile(array):
    sorted_data = sorted(array)
    n = len(sorted_data)
    q2_index = n // 2
    q2 = sorted_data[q2_index]
    if n % 2 == 0:
        q2 = (sorted_data[q2_index - 1] + sorted_data[q2_index]) / 2
    q1_index = n // 4
    q3_index = 3 * n // 4
    q1 = sorted_data[q1_index]
    q3 = sorted_data[q3_index]
    if n % 4 != 0:
        q1_weight = (n / 4) - q1_index
        q3_weight = (3 * n / 4) - q3_index
        q1 = sorted_data[q1_index] * (1 - q1_weight) + sorted_data[q1_index + 1] * q1_weight
        q3 = sorted_data[q3_index] * (1 - q3_weight) + sorted_data[q3_index + 1] * q3_weight
    return q1,q2,q3,q3 - q1

def max_value(array):
    value = -float("inf")
    for x in array:
        if value < x:
            value = x
    return value

def min_value(array):
    value = float("inf")
    for x in array:
        if value > x:
            value = x
    return value

def summation(array):
    answer = 0
    for x in array:
        answer += x
    return answer

def product(array):
    answer = 1
    for x in array:
        answer *= x
    return answer

def Range(array):
    return max_value(array) - min_value(array)

def corr(X,Y):
    meanX = mean(X)
    meanY = mean(Y)
    numerator = summation([(xi - meanX)*(yi - meanY) for xi,yi in zip(X,Y)])
    denominatorX = summation([(xi - meanX)**2 for xi in X])
    denominatorY = summation([(yi - meanY)**2 for yi in Y])
    denominator = (denominatorX * denominatorY)**0.5
    return numerator / denominator

def cov(X,Y,sample = False):
    if not len(X) == len(Y):
        raise ValueError(f"`X` and `Y` size must be the same {len(X)} != {len(Y)}")
    N = len(X)
    if  sample:
        N -= 1
    meanX = mean(X)
    meanY = mean(Y)
    numerator = summation([(xi - meanX)*(yi - meanY) for xi,yi in zip(X,Y)])
    return numerator / N

def mse(Y,predY):
    if not len(Y) == len(predY):
        raise ValueError(f"`Y` and `predY` size must be equal!{len(Y)} != {len(predY)}")
    return summation([(yi - pred_yi)**2 for yi,pred_yi in zip(Y,predY)]) / len(Y)

def mae(Y,predY):
    if not len(Y) == len(predY):
        raise ValueError(f"`Y` and `perdY` size must be equal! {len(Y)} != {len(predY)}")
    return summation([abs(yi - pred_yi) for yi,pred_yi in zip(Y,predY)]) / len(Y)

def discrete_expectation(x,px):
    if not len(x) == len(px):
        raise ValueError

