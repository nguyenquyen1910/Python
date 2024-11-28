def testCase():
    s = input()
    res = ""
    for i in range(0, len(s), 2):
        res += s[i] * int(s[i + 1])
    print(res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
