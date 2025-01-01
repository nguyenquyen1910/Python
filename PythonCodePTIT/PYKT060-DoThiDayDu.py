n = int(input())
m = int(input())
adj = [[0] * (n + 1) for _ in range(n + 1)]
par = [-1] * (n + 1)
res = []

for i in range(m):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1
    p = par[x] if par[y] == -1 else par[y]
    if p == -1:
        res.append(set([x, y]))
        par[x] = par[y] = len(res) - 1
    else:
        res[p].add(x)
        res[p].add(y)
        par[x] = par[y] = p


def check():
    for it in res:
        for x in it:
            for y in it:
                if x != y:
                    if adj[x][y] == 0 or adj[y][x] == 0:
                        return False
    return True


if check():
    print("YES")
else:
    print("NO")
