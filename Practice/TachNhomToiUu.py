n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
gr, i = 0, 0
def up_bound(l, r, x):
    if l>=r:
        return l
    m = (l+r)//2
    if a[m]<=x:
        return up_bound(m+1, r, x)
    return up_bound(l, m, x)

while i<n:
    while True:
        if i>=n: break
        next = up_bound(i+1, n, a[i]+k)
        if next==i+1: break
        else: i = next-1
    i+=1
    gr+=1
print(gr)