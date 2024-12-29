n, m = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))
luckyNum = max(max(row) for row in a) - min(min(row) for row in a)
check = False
for i in range(n):
    for j in range(m):
        if a[i][j] == luckyNum:
            check = True
if check:
    print(luckyNum)
    for i in range(n):
        for j in range(m):
            if a[i][j] == luckyNum:
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
else:
    print("NOT FOUND")
