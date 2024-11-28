from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def testCase():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
