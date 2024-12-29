def getFactor(index):
    if index%5==0:
        return 5
    return index%5*pow(-1, index%5-1)

def testCase():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    m = 5*k
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        index = getFactor(i)
        dp[i][i] = index*a[i]+dp[i-1][i-1]
        for j in range(i+1, n+1):
            dp[i][j] = max(dp[i][j-1], index*a[j]+dp[i-1][j-1])
    print(dp[m][n])

t = int(input())
while t>0:
    testCase()
    t-=1