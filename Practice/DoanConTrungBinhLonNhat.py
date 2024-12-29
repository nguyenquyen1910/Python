n = int(input())
a = list(map(int, input().split()))
maxNum = max(a)
ans, s = 0, 0
for i in range(n):
    if a[i]==maxNum:
        s+=1
    else:
        s=0
    ans = max(ans, s)
print(ans)
