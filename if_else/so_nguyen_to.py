from math import *
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
n=int(input())
a=[None]*n
for i in range(n):
    a[i]=int(input())
print(a)
for i in range(n):
    if(isPrime(a[i])):
        print(a[i],end=' ')