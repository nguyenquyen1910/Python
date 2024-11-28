from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


list = [0, 2]
k = 3
while len(list) <= 1001:
    if isPrime(k):
        list += [k]
    k += 2


n, k = [int(i) for i in input().split()]
for i in range(n + 1):
    k += list[i]
    print(k, end=" ")
