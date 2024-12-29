n = int(input())
str = input().split()
a = [int(i) for i in str]
while len(a)<n:
    k = input().split()
    for num in k:
        a.append(int(num))

even = list(i for i in a if i%2==0)
odd = list(i for i in a if i%2!=0)
even.sort()
odd.sort(key = lambda x: (-x))
res = []
cntE=0
cntO=0
for i in range(n):
    if a[i]%2==0:
       res.insert(i, even[cntE])
       cntE+=1
    else:
        res.insert(i, odd[cntO])
        cntO+=1

print(*res)