from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def countPrime(s):
    cnt = 0
    for i in s:
        if isPrime(int(i)):
            cnt += 1
    return cnt


def testCase():
    s = input()
    if isPrime(len(s)) and countPrime(s) > len(s) - countPrime(s):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
