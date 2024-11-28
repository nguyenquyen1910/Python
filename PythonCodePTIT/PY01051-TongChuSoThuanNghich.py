def testCase():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if len(str(sum)) < 2:
        print("NO")
        return
    if sum == int(str(sum)[::-1]):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1