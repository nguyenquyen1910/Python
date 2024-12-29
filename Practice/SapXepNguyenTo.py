import math


def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return num>1

n = int(input())
a = list(int(i) for i in input().split())
primes = list(i for i in a if isPrime(i))
primes.sort()
idx=0
for i in a:
    if isPrime(i):
        print(primes[idx], end=" ")
        idx+=1
    else:
        print(i, end=" ")