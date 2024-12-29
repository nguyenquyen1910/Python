def testCase():
    n, m = map(int, input().split())
    a = list(int(i) for i in input().split())
    maxEle = max(a)
    indexMaxEle = a.index(maxEle)
    a.insert(indexMaxEle, m)

    vecNegative = list(int(i) for i in a if i<0)
    vecNonNegetive = list(int(i) for i in a if i>=0)

    res = vecNegative + vecNonNegetive
    for i in res:
        print(i, end=" ")

    print()

t = int(input())
while t>0:
    testCase()
    t-=1