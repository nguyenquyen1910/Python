n = int(input())
a = [[]] * n
for i in range(n):
    a[i] = [int(i) for i in input().split()]

sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i < j:
            sum1 += a[i][j]
        elif i > j:
            sum2 += a[i][j]

k = int(input())
if abs(sum1 - sum2) <= k:
    print("YES")
else:
    print("NO")
print(abs(sum1 - sum2))
