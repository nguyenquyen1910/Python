import math


def isPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return number > 1


primes = []
for i in range(2, 10001):
    if isPrime(i):
        primes.append(i)

n = int(input())
a = list(int(i) for i in input().split())
res = 0
for i in a:
    m = primes[-1]
    for j in primes:
        m = min(m, abs(j - i))
    res = max(res, m)
print(res)
