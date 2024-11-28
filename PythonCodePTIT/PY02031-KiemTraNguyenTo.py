import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    if n <= 1:
        return 0
    return 1


n, m = map(int, input().split())
for i in range(n):
    list = [isPrime(int(i)) for i in input().split()]
    print(*list)
