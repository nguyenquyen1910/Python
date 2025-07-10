# Tìm các cặp 3 số có tổng bằng 0 trong dãy
n = int(input())
a = sorted(list(map(int, input().split())))
res = []
for i in range(n):
    if i>0 and a[i]==a[i-1]:
        continue
    j = i+1
    k = n-1
    while j<k:
        sum = a[i]+a[j]+a[k]
        if sum>0:
            k-=1
        elif sum<0:
            j+=1
        else:
            res.append([a[i], a[j], a[k]])
            j+=1

            while a[j]==a[j-1] and j<k:
                j+=1

for i in res:
    print(*i)