from xmlrpc.client import MAXINT

n = int(input())
a = list(int(i) for i in input().split())
index, minStep = 0, MAXINT
for i in range(n):
    sum=0
    for j in range(n):
        sum+=abs(a[i]-a[j])
    if sum<minStep:
        minStep = sum
        index = i
print(minStep, a[index])