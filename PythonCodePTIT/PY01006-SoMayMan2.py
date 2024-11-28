def testCase():
    s = list(input())
    for i in s:
        if i != "4" and i != "7":
            print("NO")
            return
    print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
