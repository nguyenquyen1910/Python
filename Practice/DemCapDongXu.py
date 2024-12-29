n = int(input())
a = list(input().strip() for _ in range(n))
cnt=0
for i in a:
    cInRow = i.count("C")
    if cInRow>1:
        cnt+=(cInRow)*(cInRow-1)//2

for i in range(n):
    cInCol=0
    for j in range(n):
        if a[j][i]=="C":
            cInCol+=1
    if cInCol>1:
        cnt+=(cInCol)*(cInCol-1)//2

print(cnt)
