def testCase():
    n = int(input())
    a = list(int(i) for i in input().split())
    maxEle = max(a)
    minEle = min(a)
    used = [0]*1001
    for i in a:
        used[i]=1
    cnt=0
    for i in range(minEle, maxEle + 1):
        if used[i]==0:
            cnt+=1
    print(cnt)

t = int(input())
while t>0:
    testCase()
    t-=1