from collections import deque, defaultdict

adj = defaultdict(list)
degree = defaultdict(int)
se = set()


def Kahn(n):
    queue = deque([v for v in se if degree[v] == 0])
    cnt = 0
    while queue:
        top = queue.popleft()
        cnt += 1
        for v in adj[top]:
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v)
    return cnt == n


n = int(input())
for _ in range(n):
    a, b, c = input().split()
    se.add(a)
    se.add(c)
    if b == ">":
        adj[a].append(c)
        degree[c] += 1
    else:
        adj[c].append(a)
        degree[a] += 1

if Kahn(len(se)):
    print("possible")
else:
    print("impossible")
