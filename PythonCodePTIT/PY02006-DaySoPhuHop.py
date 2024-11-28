def testCase():
    n = int(input())
    a = list(int(i) for i in input().split())
    b = list(int(i) for i in input().split())
    a = sorted(a)
    b = sorted(b)
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
    print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
