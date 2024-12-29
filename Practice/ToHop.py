def Try(list, i):
    global n,k
    if len(list) == k:
        print(*list)
        return
    for j in range(i, n):
        Try(list+[a[j]], j+1)

n, k=map(int, input().split())
a = sorted(list({int(i) for i in input().split()}))
n=len(a)
Try([], 0)