n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
for i in range(n):
    res.append([a[i], b[i]])

res.sort(key=lambda x: x[0] - x[1])
ans = 0
for i in range(k):
    ans += res[i][0]
i = k
while i < n and res[i][0] < res[i][1]:
    ans += res[i][0]
    i += 1
for j in range(i, n):
    ans+=res[j][1]
print(ans)
