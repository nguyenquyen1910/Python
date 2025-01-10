import math


def testCase():
    n, k = map(int, input().split())
    s, a = "0" + input(), [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = a[i - 1] + (1 if s[i] == "1" else 0)
    res = 0
    for i in range(1, n + 1):
        if s[i] == "1":
            if i <= k:
                res += 1 + 2 * (a[i] - 1)
            else:
                res += 1 + 2 * (a[i] - a[i - k - 1] - 1)
    m = n * n
    if res == 0:
        print("0/1")
    else:
        print(f"{res//math.gcd(res, m)}/{m//math.gcd(res, m)}")


t = int(input())
while t > 0:
    testCase()
    t -= 1
