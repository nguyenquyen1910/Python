import math


def testCase():
    n, x, m = map(float, input().split())
    t = math.ceil(math.log(m / n) / math.log(1 + x / 100))
    print(t)


t = int(input())
while t > 0:
    testCase()
    t -= 1
