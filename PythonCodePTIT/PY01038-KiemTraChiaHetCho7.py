def testCase(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        revn = int(str(n)[::-1])
        n += revn
    return -1


t = int(input())
for i in range(t):
    n = int(input())
    print(testCase(n))
