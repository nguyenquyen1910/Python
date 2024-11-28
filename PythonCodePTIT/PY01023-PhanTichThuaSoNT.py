from math import sqrt


def testCase():
    n = int(input())
    res = "1"
    for i in range(2, int(sqrt(n)) + 1):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n //= i
        if cnt != 0:
            res += " * " + str(i) + "^" + str(cnt)
        if n == 1:
            break
    if n != 1:
        res += " * " + str(int(n)) + "^1"
    print(res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
