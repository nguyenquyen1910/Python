def check(adj, u, v, e, n):
    queue = [u]
    vst = [False] * (n + 1)
    vst[u] = True
    while len(queue) > 0:
        top = queue.pop()
        if top == v:
            return False
        for i in adj[top]:
            if not vst[i] and i != e:
                queue.append(i)
                vst[i] = True
    return True


def testCase():
    n, m, u, v = map(int, input().split())
    adj = {x: [] for x in range(1, n + 1)}
    for _ in range(m):
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
