from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def checkReverse(n):
    s = str(n)
    if s == s[::-1]:
        return False
    return True


def testCase():
    used = []
    n = int(input())
    for i in range(12, n):
        if (
            int(str(i)[::-1]) < n
            and isPrime(i)
            and isPrime(int(str(i)[::-1]))
            and checkReverse(i)
            and str(i) not in used
        ):
            print(i, int(str(i)[::-1]), end=" ")
            used += [str(i), str(i)[::-1]]


t = int(input())
while t > 0:
    testCase()
    print()
    t -= 1
