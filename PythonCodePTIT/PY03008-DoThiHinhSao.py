n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

degree = [len(adj[i]) for i in range(1, n + 1)]
cnt1 = degree.count(1)
cntN = degree.count(n - 1)
if cnt1 == n - 1 and cntN == 1:
    print("Yes")
else:
    print("No")
