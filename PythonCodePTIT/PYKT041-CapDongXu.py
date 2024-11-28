n = int(input())
matrix = [input().strip() for _ in range(n)]
res = 0
for i in matrix:
    cInRow = i.count("C")
    if cInRow > 1:
        res += (cInRow) * (cInRow - 1) // 2

for col in range(n):
    cInCol = sum(1 for i in range(n) if matrix[i][col] == "C")
    if cInCol > 1:
        res += (cInCol) * (cInCol - 1) // 2

print(res)
