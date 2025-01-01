def testCase():
    s = input()
    stack = []
    cnt = 1
    for i in s:
        if i == "(":
            stack.append(cnt)
            print(cnt, end=" ")
            cnt += 1
        elif i == ")":
            print(stack[-1], end=" ")
            stack.pop()
    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
