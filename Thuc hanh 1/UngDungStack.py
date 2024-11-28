def solve(i, cnt, d):
    if cnt > k:
        return 0
    if dp[i][cnt][d] != -1:
        return dp[i][cnt][d]
    dp[i][cnt][d] = 0
    if i == n:
        if cnt == 0 and d == k:
            dp[i][cnt][d] = 1
        return dp[i][cnt][d]
    if s[i] == "?":
        dp[i][cnt][d] += solve(i + 1, cnt + 1, max(d, cnt + 1))
        if cnt:
            dp[i][cnt][d] += solve(i + 1, cnt - 1, d)
    elif s[i] == "(":
        dp[i][cnt][d] += solve(i + 1, cnt + 1, max(d, cnt + 1))
    elif cnt:
        dp[i][cnt][d] += solve(i + 1, cnt - 1, d)
    return dp[i][cnt][d]


k = int(input())
s = input()
n = len(s)
dp = [[[-1] * (n + 1) for j in range(k + 1)] for i in range(n + 1)]
print(solve(0, 0, 0))
