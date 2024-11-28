from math import sqrt


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def testCase():
    cnt = 0
    n = int(input())
    for i in range(1, n):
        if gcd(i, n) == 1:
            cnt += 1
    if isPrime(cnt):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
