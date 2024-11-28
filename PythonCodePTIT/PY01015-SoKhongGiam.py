def testCase():
    n = input()
    for i in range(0, len(n) - 1):
        if int(n[i]) > int(n[i + 1]):
            print("NO")
            return
    print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
