import math


def countOddNumber(n):
    cnt = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 1:
                cnt += 1
            if (n // i) != i and (n // i) % 2 == 1:
                cnt += 1
    return cnt


def testCase():
    n = int(input())
    if n % 2 == 1:
        print(countOddNumber(n) + 1)
    else:
        print(countOddNumber(n))


t = int(input())
while t > 0:
    testCase()
    t -= 1
