def testCase():
    n = int(input())
    a = list(int(i) for i in input().split())
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if len(stack)==0:
            print(i+1, end=" ")
        else:
            print(i-stack[-1], end=" ")
        stack.append(i)

    print()

t = int(input())
while t>0:
    testCase()
    t-=1