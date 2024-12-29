def testCase():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(float, input().split())))
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i][0] > a[j][0] and a[i][1] < a[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


t = int(input())
while t > 0:
    testCase()
    t -= 1
