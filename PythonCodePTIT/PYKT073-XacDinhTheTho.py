def lengthString(s):
    s = str(s)
    return len(s.split())


def testCase():
    n = int(input())
    v = []
    for i in range(n):
        s = input()
        v.append(s)

    i = 0
    cnt = 0
    check = True
    res = []
    while i < n:
        if lengthString(v[i]) == 6:
            if check == True:
                cnt += 1
                check = False
                res.append(1)
            i += 2
        else:
            check = True
            cnt += 1
            i += 4
            res.append(2)

    print(len(res))
    for i in res:
        print(i)


testCase()
