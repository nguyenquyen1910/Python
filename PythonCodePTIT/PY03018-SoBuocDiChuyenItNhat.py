from sys import stdin
from collections import deque

input = stdin.readline
a = [[]] * 1000


def testCase():
    n, m = map(int, input().split())
    dp = [[0] * m for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    queue = deque()
    queue.append((0, 0))
    while len(queue):
        i, j = queue.popleft()
        if i + 1 < n:
            tmp = abs(a[i + 1][j] - a[i][j])
            if tmp and i + tmp < n and dp[i + tmp][j] == 0:
                dp[i + tmp][j] = dp[i][j] + 1
                queue.append((i + tmp, j))
        if j + 1 < m:
            tmp = abs(a[i][j + 1] - a[i][j])
            if tmp and j + tmp < m and dp[i][j + tmp] == 0:
                dp[i][j + tmp] = dp[i][j] + 1
                queue.append((i, j + tmp))
        if i + 1 < n and j + 1 < m:
            tmp = abs(a[i + 1][j + 1] - a[i][j])
            if tmp and i + tmp < n and j + tmp < m and dp[i + tmp][j + tmp] == 0:
                dp[i + tmp][j + tmp] = dp[i][j] + 1
                queue.append((i + tmp, j + tmp))
    if dp[n - 1][m - 1]:
        print(dp[n - 1][m - 1])
    else:
        print(-1)


t = int(input())
while t > 0:
    testCase()
    t -= 1
