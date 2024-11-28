from math import log2

BASE = "0123456789ABCDEF"


def testCase():
    n = int(log2(int(input())))
    x = input()
    while len(x) % n:
        x = "0" + x
    pow = [1]
    for i in range(1, n):
        pow = [pow[0] * 2] + pow
    res = ""
    for i in range(0, len(x), n):
        e = 0
        for j in range(i, i + n):
            e += int(x[j]) * pow[j - i]
        res += BASE[e]
    print(res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
