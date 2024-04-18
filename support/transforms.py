version = "0.0.1"

class DFT: # Discrete Fourier Transform
    def __init__(self,function,k,n_samples):
        self.function = function
        self.k = k
        self.n_samples = n_samples
        self.__e = 2.7182818284590452353602874713527
        self.__pi = 3.1415926535897932384626433832795

    def exp(self,number):
        return self.__e ** number

    def transform(self):
        if 0 <= self.k < self.n_samples:
            return sum(self.function(n) * self.exp(-2j * self.__pi * self.k * n / self.n_samples) for n in range(self.n_samples))
        return f"value of 'k' = [{0},{self.n_samples - 1}] for n_samples = {self.n_samples}"

class DTFT: # Discrete Time Fourier Transform
    def __init__(self,function,n_samples,omega):
        self.function = function
        self.n_samples = n_samples
        self.omega = omega
        self.__e = 2.7182818284590452353602874713527

    def exp(self,number):
        return self.__e ** number

    def transform(self):
        return sum(self.function(n) * self.exp(-1j * self.omega * n) for n in range(self.n_samples))

class ZT: # Z-Transform
    def __init__(self,sequence):
        self.__sequence = sequence

    def transform(self,z):
        result = 0
        for k in range(len(self.__sequence)):
            result += self.__sequence[k] * (z ** -k)
        return result

