from .algorithm import bubble_sort

version = "0.0.1"

# constants
INF = float("inf")
NAN = float("nan")
PI = 3.1415926535897932384626433832795
EXP = 2.7182818284590452353602874713527

# functions
def binomial_dist(n_trials,rand_num,p):
    # p -> probability of having success
    # q -> probability of having failure
    # rand_num -> random variable also denoted by 'x'
    # n_trials -> number of times an experment performerd
    if not 0 <= p <= 1:
        raise ValueError("probability is always lies between 0 and 1")
    q = 1 - p
    return combination(n_trials,rand_num) * p ** rand_num * q ** (n_trials - rand_num)

def mean(array):
    return sum(array) / len(array)

def moving_avg(array,window_size):
    if len(array) < window_size:
        return []
    if window_size < 1:
        return []
    if len(array) == window_size:
        return mean(array)
    avgs = []
    for i in range(len(array) - window_size + 1):
        window = array[i:i + window_size]
        avg = summation(window) / window_size
        avgs.append(avg)
    return avgs

def exp_moving_avg(array,alpha):
    if not 0 <= alpha <= 1:
        raise ValueError(f"value of alpha or smoothing factor should lie between 0 and 1")
    avgs = [array[0]]
    for i in range(1,len(array)):
        avgs.append(alpha * array[i] + (1 - alpha) * avgs[-1])
    return avgs

def median(array):
    if len(array) % 2 == 0:
        return (array[len(array)//2 - 1] + array[len(array)//2]) / 2
    return array[len(array)//2]

def standard_deviation(array,sample = False):
    l = len(array)
    if sample:
        l = l - 1
    return sqrt(summation([(x - mean(array))**2 for x in array]) / l)

def variance(array,sample = False):
    return standard_deviation(array,sample)**2

def Range(array):
    return find_max(array) - find_min(array)

def softmax(array,index = None):
    exp_array = [EXP**x for x in array]
    sum_array = sum(exp_array)
    softmax_array = [x / sum_array for x in exp_array]
    if index is None:
        return softmax_array
    else:
        if 0 <= index < len(softmax_array):
            return softmax_array[index]
        else:
            raise IndexError(f"index out of range! length of an array: {len(array)}")

def skewness(array):
    m = mean(array)
    std_dev = standard_deviation(array)
    diff = [(x - m)**3 for x in array]
    return summation(diff) / (len(array) * std_dev**3)

def kurtosis(array):
    m = mean(array)
    std_dev = standard_deviation(array)
    diff = [(x - m)**4 for x in array]
    return summation(diff) / (len(array) * std_dev**4) - 3

def gaussian_distribution(x,mean,standard_deviation):
    return 1 / (standard_deviation * sqrt(2 * PI)) * exp(-0.5 * ((x - mean) / standard_deviation)**2)

def percentile(array,percentile):
    array = bubble_sort(array)
    length = len(array)
    index = (percentile / 100) * (length - 1)
    if index.is_integer():
        return array[int(index)]
    lower_index = int(index // 1)
    upper_index = lower_index + 1
    lower_value = array[lower_index]
    upper_value = array[upper_index]
    interpolation = index % 1
    interpolated_value = (1 - interpolation) * lower_value + interpolation * upper_value
    return interpolated_value

def quartile(array):
    array = bubble_sort(array)
    length = len(array)
    Q1_index = int(0.25 * (length + 1))
    Q2_index = int(0.5 * (length + 1))
    Q3_index = int(0.75 * (length + 1))
    Q1 = array[Q1_index - 1] + 0.25 * (array[Q1_index] - array[Q1_index - 1])
    Q2 = array[Q2_index - 1] + 0.5 * (array[Q2_index] - array[Q2_index - 1])
    Q3 = array[Q3_index - 1] + 0.75 * (array[Q2_index] - array[Q2_index - 1])
    return Q1,Q2,Q3

def iqr(array):
    Q = quartile(array)
    return Q[2] - Q[0]

def cv(array):
    return (standard_deviation(array) / mean(array)) * 100

def cc(X,Y):
    return covariance(X,Y) / (standard_deviation(X) * standard_deviation(Y)) 

def mean_squared_error(actual,predicted):
    if len(actual) != len(predicted):
        return -1
    return summation([(actual[i] - predicted[i])**2 for i in range(len(actual))]) / len(actual)

def mean_absolute_error(actual,predicted):
    if len(actual) != len(predicted):
        return -1
    return summation([absolute(actual[i] - predicted[i]) for i in range(len(actual))]) / len(actual)

def root_mean_squared_error(actual,predicted):
    if len(actual) != len(predicted):
        return -1
    return sqrt(mean_squared_error(actual,predicted))

def mean_absolute_deviation(array):
    m = mean(array)
    return summation([absolute(x - m) for x in array]) / len(array)

def covariance(X,Y,sample = False):
    if len(X) != len(Y):
        return -1
    N = len(X)
    if sample:
        N = N - 1
    meanX = mean(X)
    meanY = mean(Y)
    return summation([(x - meanX)*(y - meanY) for x,y in zip(X,Y)]) / N

def zscore(array):
    m = mean(array)
    std_dev = standard_deviation(array)
    return [(x - m) / std_dev for x in array]

def compare(X,Y,largest = True):
    if X > Y:
        if largest:
            return X
        return Y
    elif X < Y:
        if largest:
            return Y
        return X
    else:
        X

def definite_integral(function,lower_limit,upper_limit,max_iterations = 1000):
    h = (upper_limit - lower_limit) / max_iterations
    integral_sum = function(lower_limit) + function(upper_limit)
    for i in range(1,max_iterations,2):
        integral_sum += 4 * function(lower_limit + i * h)
    for i in range(2,max_iterations - 1,2):
        integral_sum += 2 * function(lower_limit + i * h)
    result = h / 3 * integral_sum
    return result

def cos(x):
    return ((EXP**(1j*x) + EXP**(-1j*x)) / 2).real

def sin(x):
    return ((EXP**(1j*x) - EXP**(-1j*x)) / 2j).real

def tan(x):
    return sin(x) / cos(x)

def cot(x):
    return cos(x) / sin(x)

def sec(x):
    return 1 / cos(x)

def cosec(x):
    return 1 / sin(x)

def cosh(x):
    return (EXP**x + EXP**-x) / 2

def sinh(x):
    return (EXP**x - EXP**-x) / 2

def tanh(x):
    return sinh(x) / cosh(x)

def coth(x):
    return cosh(x) / sinh(x)

def sech(x):
    return 1 / cosh(x)

def cosech(x):
    return 1 / sinh(x)

def deg2rad(degree):
    return degree * PI / 180

def rad2deg(radian):
    return radian * 180 / PI

def fibonacci(number):
    if number <= 0:
        return -1
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def factorial(number):
    if not isinstance(number,int):
        return -1
    if number == 0:
        return 1
    return number * factorial(number - 1)

def collatz_conjecture(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

def palindrome(number):
    org = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    return org == reverse

def gcd(x,y):
    while y != 0:
        x,y = y,x % y
    return absolute(x)

def lcm(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // gcd(lcm, numbers[i])
    return lcm

def quadratic_roots(a,b,c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return -1
    elif discriminant == 0:
        return [ -b / (2*a)]
    else:
        return [(-b + sqrt(discriminant)) / (2*a),(-b - sqrt(discriminant)) / (2*a)]

def permutation(n,r):
    if n < r:
        return None
    return factorial(n) / factorial(n - r)

def combination(n,r):
    if n < r:
        return None
    return factorial(n) / (factorial(r) * factorial(n - r))

def precentage(part,whole):
    if part > whole:
        return f"whole is always greater than the part: part({part}) > whole({whole})"
    return (part / whole) * 100

def precentage_change(initial_value,final_value):
    return ((final_value - initial_value) / initial_value) * 100

def floor(number):
    if number < 0:
        if number != int(number):
            return int(number) - 1
    return int(number)

def ceil(number):
    if number == int(number):
        return int(number)
    return int(number) + 1

def absolute(number):
    if number < 0:
        return -number
    return number

def exp(number):
    return EXP**number

def sqrt(number,tolerance = 1e-10,max_iterations = 1000):
    if number < 0:
        return -1
    guess = number / 2
    for _ in range(max_iterations):
        new_guess = 0.5 * (guess + number / guess)
        if absolute(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
    return guess

def cbrt(number,tolerance = 1e-10,max_iterations = 1000):
    guess = number / 2
    for _ in range(max_iterations):
        new_guess = (2 * guess + number / (guess * guess)) / 3
        if absolute(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
    return guess

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def is_even(number):
    if number % 2 == 0:
        return True
    return False

def is_odd(number):
    return not is_even(number)

def primes(lower_limit,upper_limit):
    if lower_limit > upper_limit:
        return -1
    answer = []
    for number in range(lower_limit,upper_limit + 1):
        if is_prime(number):
            answer.append(number)
    return answer

def odds(lower_limit,upper_limit):
    if lower_limit > upper_limit:
        return -1
    answer = []
    for number in range(lower_limit,upper_limit + 1):
        if is_odd(number):
            answer.append(number)
    return answer

def evens(lower_limit,upper_limit):
    if lower_limit > upper_limit:
        return -1
    answer = []
    for number in range(lower_limit,upper_limit + 1):
        if is_even(number):
            answer.append(number)
    return answer

def linear_space(start,end,n_samples):
    results = []
    for x in range(n_samples):
        value = start + x * (end - start)/(n_samples - 1)
        results.append(round(value,8))
    return results

def arange(start,end,step):
    result = [start]
    while start < end:
        start += step
        result.append(start)
    return result

def notation(number):
    return f"{number:.8e}"

def find_max(array):
    value = -INF
    for x in array:
        if value < x:
            value = x
    return value

def find_min(array):
    value = INF
    for x in array:
        if value > x:
            value = x
    return value

def signum(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    return 0

def summation(array):
    total = 0
    for x in array:
        total += x
    return total

def product(array):
    answer = 1
    for x in array:
        answer *= x
    return x

def is_nan(array):
    for x in array:
        if x != x:
            return True
    return False

def is_inf(array):
    for x in array:
        if x == INF or x == -INF:
            return True

