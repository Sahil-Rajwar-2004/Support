from .mathx import combination,sqrt
import numpy as np

version = "0.0.1"

class Binomial:
    def __init__(self,n_trials,prob_success,n_successes):
        self.n_trials = n_trials
        self.prob_success = prob_success
        self.n_successes = n_successes

    def __pmf(self,n_successes = None):
        n_successes = n_successes if n_successes is not None else self.n_successes
        return combination(self.n_trials,n_successes) * self.prob_success ** n_successes * (1 - self.prob_success) ** (self.n_trials - n_successes)

    def pmf(self):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("probability must be in between 0 and 1 inclusive")
        if isinstance(self.n_successes,int):
            if self.n_trials < self.n_successes:
                raise ValueError("number successes shouldn't exceed the number trials")
            return self.__pmf()
        elif isinstance(self.n_successes,list):
            result = []
            for x in self.n_successes:
                if self.n_trials < x:
                    raise ValueError("number successes shouldn't exceed the number trials")
                result.append(self.__pmf(n_successes = x))
            return np.array(result)
        else:
            raise TypeError("check the data types of each parameters:: n_trials:int, prob_success:float and n_successes:int|list[int]")

    def logpmf(self):
        return np.log(self.pmf())

    def cdf(self,max_limit):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("probability must be in between 0 and 1 inclusive")
        if max_limit <= self.n_trials or max_limit >= 0:
            cdf_value = 0
            cdf_values = []
            for i in range(max_limit + 1):
                cdf_value += self.__pmf(i)
                cdf_values.append(cdf_value)
            return cdf_values
        else:
            raise TypeError("number of successes should be int|list of integers")

    def isf(self, alpha):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("Probability must be between 0 and 1 inclusive")
        if not 0 <= alpha <= 1:
            raise ValueError("Alpha must be between 0 and 1 inclusive")
        cumulative_prob = 0
        for i in range(self.n_trials + 1):
            cumulative_prob += self.__pmf(i)
            if cumulative_prob >= 1 - alpha:
                return i

    def sf(self, x):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("Probability must be between 0 and 1 inclusive")
        return 1 - self.cdf(x)
    
    def ppf(self,probability):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("probability must be between 0 and 1 inclusive")
        if not 0 <= probability <= 1:
            raise ValueError("probability must be between 0 and 1 inclusive")
        cumulative_prob = 0
        for i in range(self.n_trials + 1):
            cumulative_prob += self.__pmf(i)
            if cumulative_prob >= probability:
                return i

    def mean(self):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("probability must be in between 0 and 1 inclusive")
        return self.n_trials * self.prob_success

    def var(self):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("probability must be in between 0 and 1 inclusive")
        return self.n_trials * self.prob_success * (1 - self.prob_success)

    def std(self):
        return sqrt(self.var())

    def skewness(self):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("probability must be in between 0 and 1 inclusive")
        return (1 - 2 * self.prob_success) / self.std()

    def kurtosis(self):
        if not 0 <= self.prob_success <= 1:
            raise ValueError("probability must be in between 0 and 1 inclusive")
        return (1 - 6 * self.prob_success) * (1 - self.prob_success) / self.var()
