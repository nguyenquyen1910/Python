def testCase():
    n = input()
    if (n[0] + n[1]) == (n[-2] + n[-1]):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
