from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def testCase():
    s = input()
    if isPrime(int(s[0:3])) and isPrime(int(s[-3 : len(s)])):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
