n, m = int(input()), int(input())
edge = []
ke = [[0] * (n + 1) for i in range(n + 1)]
par = [-1] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    ke[x][y] = ke[y][x] = 1
    if par[y] == -1:
        p = par[x]
    else:
        p = par[y]
    if p == -1:
        edge.append(set([x, y]))
        par[x] = par[y] = len(edge) - 1
    else:
        edge[p].add(x)
        edge[p].add(y)
        par[x] = par[y] = p


def check():
    for z in edge:
        for x in z:
            for y in z:
                if x != y:
                    if ke[x][y] == 0 or ke[y][x] == 0:
                        return False

    return True


if check():
    print("YES")
else:
    print("NO")
