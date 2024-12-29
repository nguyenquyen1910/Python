def testCase():
    n, k = map(int, input().split())
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        res = digits[n % k] + res
        n //= k
    print(res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
