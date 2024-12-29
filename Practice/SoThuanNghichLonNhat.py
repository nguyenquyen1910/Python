def checkRev(num):
    return int(str(num))==int(str(num)[::-1])

n, m = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))
check = False
maxRevNum = 0
for i in range(n):
    for j in range(m):
        if checkRev(a[i][j]) and a[i][j]>=10:
            maxRevNum = max(maxRevNum, a[i][j])
            check = True
if check:
    print(maxRevNum)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxRevNum:
                print("Vi tri ["+str(i)+"]["+str(j)+"]")
else:
    print("NOT FOUND")