def testCase():
    n, p = map(int, input().split())
    cnt = 0
    for i in range(1, n + 1):
        while i % p == 0:
            cnt += 1
            i /= p
    print(cnt)


t = int(input())
while t > 0:
    testCase()
    t -= 1
