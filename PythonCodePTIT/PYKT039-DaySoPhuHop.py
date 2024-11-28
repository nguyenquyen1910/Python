def testCase():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    for i in range(n):
        if b[i] < a[i]:
            print("NO")
            return
    print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
