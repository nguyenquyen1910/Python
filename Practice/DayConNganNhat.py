def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def testCase():
    n, k = map(int, input().split())
    a = list(int(i) for i in input().split())


t = int(input())
while t>0:
    testCase()
    t-=1