def testCase():
    n=int(input())
    a=list(map(int,input().split()))
    sum=0
    Min=1e9
    for i in range(0,n-1):
        sum+=a[i]
        Min=min(Min,a[i])
    print(Min)
t=int(input())
while t>0:
    testCase()
    t-=1
        