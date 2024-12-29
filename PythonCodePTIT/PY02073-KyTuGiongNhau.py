def testCase():
    n = int(input())
    x, y, z = map(int, input().split())
    dp = [10**5] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + x)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + z)
            dp[i] = min(dp[i], dp[i // 2 + 1] + y + z)
        else:
            dp[i] = min(dp[i], dp[(i - 1) // 2] + z + x)
            dp[i] = min(dp[i], dp[(i + 1) // 2] + z + y)
    print(dp[n])


t = int(input())
while t > 0:
    testCase()
    t -= 1
