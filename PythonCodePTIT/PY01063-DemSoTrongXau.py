def testCase():
    s = input()
    n = input()
    cnt = 0
    pos = s.find(n)
    while pos != -1:
        cnt += 1
        s = s[:pos] + s[pos + len(n) :]
        pos = s.find(n)
    print(cnt)


t = int(input())
while t > 0:
    testCase()
    t -= 1
