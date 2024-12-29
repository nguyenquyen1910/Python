def testCase():
    s = input()
    tmp=""
    for i in range(0, len(s)):
        if not s[i].isdigit():
            tmp+=s[i]
        else:
            for j in range(0, int(s[i])):
                print(tmp, end="")
            tmp=""
    print()

t = int(input())
while t>0:
    testCase()
    t-=1