def countFrequency(num, end):
    res = 0
    for i in range(0, 10):
        m = 10**i
        if m > end:
            break
        a = end // m
        b = end % m
        z = a % 10
        if z > num:
            res += ((a // 10) + 1) * m
        elif z == num:
            res += (a // 10) * m + (b + 1)
        else:
            res += (a // 10) * m
        if num == 0:
            res -= m
    return res


def countDigit(num, low, high):
    return countFrequency(num, high) - countFrequency(num, low - 1)


def testCase():
    a, b = map(int, input().split())
    for i in range(0, 10):
        print(countDigit(i, a, b), end=" ")
    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
