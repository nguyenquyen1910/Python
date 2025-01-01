def Try(i, n, a, used, res):
    for j in range(1, n + 1):
        if not used[j]:
            used[j] = True
            a[i - 1] = j
            if i == n:
                res.append(a[:])
            else:
                Try(i + 1, n, a, used, res)
            used[j] = False


def testCase():
    n = int(input())
    res = []
    a = [0] * n
    used = [False] * (n + 1)
    Try(1, n, a, used, res)
    res.reverse()
    print(len(res))
    for i in res:
        for j in i:
            print(j, end="")
        print(end=" ")
    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
