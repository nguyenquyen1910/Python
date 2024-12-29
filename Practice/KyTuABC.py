n = int(input())
res=[]
def Try(str, a, b, c):
    if len(str)<=n:
        if a and b and c and a <= b <= c:
            res.append(str)
        if len(str)==n:
            return
        Try(str+"A", a+1, b, c)
        Try(str+"B", a, b+1, c)
        Try(str+"C", a, b, c+1)

Try("", 0, 0, 0)
res.sort(key = lambda x: (len(x), x))
for i in res:
    print(i)


