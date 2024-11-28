def testCase():
    n = int(input())
    a = list(int(i) for i in input().split())
    cnt = 0
    for i in range(0, n - 1):
        if a[i] != a[i + 1]:
            cnt += 1
    print(cnt)


t = 1
while t > 0:
    testCase()
    t -= 1
