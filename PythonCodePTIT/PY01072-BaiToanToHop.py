def Try(i,v):
    global n,k
    if len(v)==k:
        print(*v)
        return
    for j in range(i,n):
        Try(j+1,v+[a[j]])


n, k = map(int, input().split())
a = sorted(list({int(i) for i in input().split()}))
n=len(a)

Try(0,[])