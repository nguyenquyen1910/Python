def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def testCase():
    n = int(input())
    s = str(n)
    if gcd(int(n), int(s[::-1])) == 1:
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
