def testCase():
    s = input()
    res = 1
    for i in s:
        if i != "0":
            res *= int(i)
    print(res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
