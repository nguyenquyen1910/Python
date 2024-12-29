def sumNum(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum
def testCase():
    n = int(input())
    a = list(int(i) for i in input().split())
    a.sort(key=lambda x:(sumNum(x), x))
    for i in a:
        print(i, end=" ")
    print()

t = int(input())
while t>0:
    testCase()
    t-=1