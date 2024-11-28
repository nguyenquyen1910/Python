def testCase():
    cnt = {}
    maxCntNum = 0
    n = int(input())
    for i in range(n):
        x = int(input())
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1
        maxCntNum = max(maxCntNum, cnt[x])
    ans = 10000
    for i in cnt:
        if cnt[i] == maxCntNum:
            ans = min(ans, i)
    print(ans)


t = int(input())
while t > 0:
    testCase()
    t -= 1
