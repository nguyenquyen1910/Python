n, m = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))
if n>m:
    cnt = n-m
    tmp = 0
    for i in range(n):
        if tmp!=cnt and i%2==0:
            tmp+=1
            continue
        for j in range(m):
            print(a[i][j], end=" ")
        print()
else:
    cnt = m - n
    tmp = 0
    res = []
    col = []
    for j in range(m):
        if tmp!=cnt and j%2==1:
            tmp+=1
            continue
        col.append(j)
    for i in range(n):
        for j in col:
            print(a[i][j], end=" ")
        print()