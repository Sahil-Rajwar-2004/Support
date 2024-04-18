from .mathx import factorial,combination,sqrt,E

class binomial:
    def __init__(self,trials,prob,rand_var) -> None:
        self.trials = trials
        self.prob = prob
        self.rand_var = rand_var

    @property
    def pmf(self):
        comb = combination(self.trials,self.rand_var)
        succ = self.prob ** self.rand_var
        fail = (1 - self.prob) ** (self.trials - self.rand_var)
        return comb * succ * fail

    @property
    def mean(self):
        return self.trials * self.prob

    @property
    def var(self):
        return self.trials * self.prob * (1 - self.prob)

    @property
    def std(self):
        return sqrt(self.var())

class poisson:
    def __init__(self,lambda_:int,k:int):
        self.lambda_ = lambda_
        self.k = k

    @property
    def pmf(self):
        return self.lambda_ * E ** (-self.lambda_) / factorial(self.k)

    @property
    def var(self):
        return self.lambda_

    @property
    def std(self):
        return self.lambda_

