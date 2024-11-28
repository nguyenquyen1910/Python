from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def sumNum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def testCase():
    a, b = map(int, input().split())
    if isPrime(sumNum(gcd(a, b))):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
