def testCase():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    res = 0
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            res += a[i] - a[i - 1] - 1
    print(res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
