def findChar(n, k):
    x = (1<<(n-1))
    if k==x:
        return chr(n-1+ord('A'))
    if k>x:
        return findChar(n-1, x-(k-x))
    return findChar(n-1, k)

def testCase():
    n, k = map(int, input().split())
    print(findChar(n, k))
t = int(input())
while t>0:
    testCase()
    t-=1