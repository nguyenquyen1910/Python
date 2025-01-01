def check(adj, u, v, e, n):
    queue = [u]
    vst = [False] * (n + 1)
    vst[u] = True
    while queue:
        top = queue.pop()
        if top == v:
            return False
        for it in adj[top]:
            if it != e and not vst[it]:
                queue.append(it)
                vst[it] = True
    return True


def testCase():
    n, m, u, v = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
    cnt = 0
    for i in range(1, n + 1):
        if i != u and i != v:
            if check(adj, u, v, i, n):
                cnt += 1
    print(cnt)


t = int(input())
while t > 0:
    testCase()
    t -= 1
