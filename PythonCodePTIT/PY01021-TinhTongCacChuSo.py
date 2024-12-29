def testCase():
    s = input()
    sum = 0
    res = ""
    for i in s:
        if i.isdigit():
            sum += int(i)
        else:
            res += i
    res = sorted(res)
    res += str(sum)
    for i in res:
        print(i, end="")
    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
