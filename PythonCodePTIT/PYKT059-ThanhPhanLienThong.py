def DFS(adi, u):
    global vst
    vst[u] = True
    for i in adj[u]:
        if not vst[i]:
            DFS(adj, i)


n, m, x = map(int, input().split())
adj = [[] for _ in range(n + 1)]
vst = [False] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

DFS(adj, x)

res = []
for i in range(1, n + 1):
    if not vst[i]:
        res.append(i)

if res:
    res.sort()
    for i in res:
        print(i)
else:
    print(0)
