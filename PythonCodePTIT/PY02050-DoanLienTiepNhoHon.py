def testCase():
    n = int(input())
    list = [int(i) for i in input().split()]
    stack = []
    for i in range(n):
        while len(stack) > 0 and list[stack[-1]] <= list[i]:
            stack.pop()
        if len(stack) == 0:
            print(i + 1, end=" ")
        else:
            print(i - stack[-1], end=" ")
        stack.append(i)
    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
