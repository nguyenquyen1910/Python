m, n = map(int, input().split())
a = list(list(int(i) for i in input().split()) for _ in range(m))
cnt=0
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            for k in range(8):
                newI = i + dx[k]
                newJ = j + dy[k]
                if 0 <= newI < m and 0 <= newJ < n and not visited[newI][newJ]:
                    cnt+=a[newI][newJ]
                    visited[newI][newJ] = True

print(cnt)
