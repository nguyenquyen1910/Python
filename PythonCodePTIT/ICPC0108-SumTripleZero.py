def testCase():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            x = a[i] + a[l] + a[r]
            if x == 0:
                cnt += 1
                l += 1
            elif x < 0:
                l += 1
            else:
                r -= 1
    print(cnt)


t = int(input())
while t > 0:
    testCase()
    t -= 1
