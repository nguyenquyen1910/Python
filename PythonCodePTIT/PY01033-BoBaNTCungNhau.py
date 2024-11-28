def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def testCase():
    l, r = [int(i) for i in input().split()]
    for i in range(l, r - 1):
        for j in range(i + 1, r):
            for k in range(j + 1, r + 1):
                if gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(i, k) == 1:
                    print("(", i, ", ", j, ", ", k, ")", sep="")


testCase()
