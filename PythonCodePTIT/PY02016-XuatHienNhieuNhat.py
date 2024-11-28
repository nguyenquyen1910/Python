def testCase():
    n = int(input())
    list = [int(i) for i in input().split()]
    cnt = {}
    res = 0
    for i in list:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
        res = max(res, cnt[i])
    if res * 2 <= n:
        print("NO")
    else:
        for i in list:
            if cnt[i] == res:
                print(i)
                break


t = int(input())
while t > 0:
    testCase()
    t -= 1
