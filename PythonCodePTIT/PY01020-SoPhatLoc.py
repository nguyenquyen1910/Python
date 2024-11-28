def testCase():
    s = input()
    if (s[len(s) - 2]) + s[len(s) - 1] != "86":
        print("NO")
    else:
        print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
