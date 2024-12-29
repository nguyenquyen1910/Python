import math

N = 100000
prime = [True] * N
prime[0] = prime[1] = False
for i in range(2, int(math.sqrt(N))+1):
    if prime[i]:
        for j in range(i*i, N, i):
            prime[j] = False
listPrime = []
for i in range(N):
    if prime[i]:
        listPrime.append(i)
listPrime.sort()
N = int(1e9+7)
res = []
for i in listPrime:
    if i**8 <= N:
        res.append(i**8)
    else:
        break
for i in range(len(listPrime)-1):
    for j in range(i+1, len(listPrime)):
        x = listPrime[i]**2 * listPrime[j]**2
        if x<=N:
            res.append(x)
        else:
            break
res.sort()
def up_bou(l, r, x):
    if l==r:
        return l
    m = (l+r)//2
    if res[m] <= x:
        return up_bou(m+1, r, x)
    return up_bou(l, m, x)
n = int(input())
print(up_bou(0, len(res)-1, n))