def testCase():
    n, d = [int(i) for i in input().split()]
    a = list(map(int, input().split()))
    for i in range(d, n):
        print(a[i], end=" ")
    for i in range(0, d):
        print(a[i], end=" ")
    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
