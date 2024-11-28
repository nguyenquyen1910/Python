n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

max_val = max(max(row) for row in a)
min_val = min(min(row) for row in a)
lucky_value = max_val - min_val

pos = []
for i in range(n):
    for j in range(m):
        if a[i][j] == lucky_value:
            pos.append((i, j))

if pos:
    print(lucky_value)
    for pos in pos:
        print(f"Vi tri [{pos[0]}][{pos[1]}]")
else:
    print("NOT FOUND")
