def testCase():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        m = min(a[i], a[i + 1])
        M = max(a[i], a[i + 1])
        while M > 2 * m:
            cnt += 1
            m *= 2
    print(cnt)


t = int(input())
while t > 0:
    testCase()
    t -= 1
