n = int(input())
a =list(int(i) for i in input().split())
stack = []
for i in a:
    if stack and (stack[-1]+i)%2==0:
        stack.pop()
    else:
        stack.append(i)

print(len(stack))