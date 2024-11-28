def testCase():
    s = input() + "z"
    i = 0
    ans = 10**20
    while i < len(s):
        tmp = 0
        if s[i].isdigit():
            while i < len(s) and s[i].isdigit():
                tmp = tmp * 10 + int(s[i])
                i += 1
        else:
            i += 1
            tmp = 0
        if tmp != 0:
            ans = min(ans, tmp)
    print(ans)


t = int(input())
while t > 0:
    testCase()
    t -= 1
