def testCase():
    n = input()
    if len(n) < 3:
        print("NO")
        return
    a = list(int(i) for i in n)
    ok = True
    for i in range(1, len(a)):
        if ok and a[i] <= a[i - 1]:
            ok = False
        elif not ok and a[i] >= a[i - 1]:
            print("NO")
            return
    print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
