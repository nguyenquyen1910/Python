def testCase():
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
