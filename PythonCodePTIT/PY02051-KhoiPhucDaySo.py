n = int(input())
b = list(list(map(int, input().split())) for _ in range(n))
res = [0] * n
if n == 2:
    print(b[0][1] // 2, b[1][0] // 2)
else:
    res[0] = (b[0][1] + b[0][2] - b[1][2]) // 2
    for i in range(1, n):
        res[i] = b[0][i] - res[0]

    print(*res)
