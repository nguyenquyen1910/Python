def testCase():
    n, m, k = map(int, input().split())
    a = list(int(i) for i in input().split())
    b = list(int(i) for i in input().split())
    c = list(int(i) for i in input().split())

    i = j = 0
    tmp = []
    while i < n and j < m:
        if a[i] == b[j]:
            tmp.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    i = j = 0
    res = []
    while i < len(tmp) and j < k:
        if tmp[i] == c[j]:
            res.append(tmp[i])
            i += 1
            j += 1
        elif tmp[i] < c[j]:
            i += 1
        else:
            j += 1
    if len(res) == 0:
        print("NO")
    else:
        print(*res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
