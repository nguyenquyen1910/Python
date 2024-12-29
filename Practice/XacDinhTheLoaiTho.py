def lenLine(s):
    return len(str(s).split())
n = int(input())
list = []
for i in range(n):
    s = input()
    list.append(s)

i=0
check=True
res = []
while i<n:
    if lenLine(list[i])==6:
        if check:
            check=False
            res.append(1)
        i+=2
    else:
        check=True
        i+=4
        res.append(2)

print(len(res))
for i in res:
    print(i)