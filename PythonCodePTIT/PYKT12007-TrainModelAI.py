def testCase():
    n = int(input())
    u = float(input())
    p = list(map(float, input().split()))
    cnt = {}
    for i in p:
        if cnt.get(i) is None:
            cnt[i]=1
        else:
            cnt[i]+=1
    cnt = [[i, cnt[i]] for i in sorted(cnt)]
    
    

    ans = 1
    for i in p:
        ans*=i
    print(f'{ans:.6f}')

t = int(input())
while t > 0:
    testCase()
    t -= 1