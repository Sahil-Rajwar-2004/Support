import random

class RandomNumberGenerator:
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
        self.generated_numbers = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_numbers < self.count:
            result = random.randint(self.start, self.end)
            self.generated_numbers += 1
            return result
        else:
            raise StopIteration

class RangeGenerator:
    def __init__(self,start,end,step = 1):
        self.start = start
        self.end = end
        self.step = step
        self.current_value = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current_value < self.end) or (self.step < 0 and self.current_value > self.end):
            result = self.current_value
            self.current_value += self.step
            return result
        else:
            raise StopIteration
        
class PrimeGenerator:
    def __init__(self,lower_limit = 2,upper_limit = 10):
        self.current = max(lower_limit, 1)
        self.upper_limit = upper_limit

    def __iter__(self):
        return self

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __next__(self):
        while self.current <= self.upper_limit:
            if self.is_prime(self.current):
                result = self.current
                self.current += 1
                return result
            else:
                self.current += 1
        raise StopIteration("No more prime numbers in the specified range.")

