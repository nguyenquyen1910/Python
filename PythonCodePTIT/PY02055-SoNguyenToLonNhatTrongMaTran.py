import math


def isPrime(num):
    for idx in range(2, int(math.sqrt(num)) + 1):
        if num % idx == 0:
            return False
    return num > 1


n, m = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))
maxPrime = 0
check = False
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]):
            maxPrime = max(maxPrime, a[i][j])
            check = True
if check:
    print(maxPrime)
    res = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxPrime:
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
if not check:
    print("NOT FOUND")
