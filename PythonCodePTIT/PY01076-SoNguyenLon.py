from math import gcd


def testCase():
    a = int(input())
    b = int(input())
    print(gcd(a, b))


t = int(input())
while t > 0:
    testCase()
    t -= 1
