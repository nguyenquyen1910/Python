def testCase():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    tmp = []
    res = []
    for i in a:
        if i < 0:
            res.append(i)
    index = a.index(max(a))
    for i in range(0, index):
        tmp.append(a[i])
    tmp.append(m)
    for i in range(index, n):
        tmp.append(a[i])
    for i in tmp:
        if i >= 0:
            res.append(i)

    print(" ".join(map(str, res)))


t = int(input())
while t > 0:
    testCase()
    t -= 1
