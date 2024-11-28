from math import *
n=int(input())
a=[int(i) for i in input().split()]

def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return n>1

def is_revnum(n):
    return n==(int)(str(n)[::-1])

def sumdigit(n):
    s=0
    while n!=0:
        s+=n%10
        n//=10
    return s
def is_square(n):
    return n==sqrt(n)**2

for i in range(n):
    if is_prime(a[i]):
        print(a[i],end=' ')
print()
for i in range(n):
    if is_revnum(a[i]):
        print(a[i],end=' ')
print()
for i in range(n):
    if is_square(a[i]):
        print(a[i],end=' ')
print()
for i in range(n):
    if is_prime(sumdigit(a[i])):
        print(a[i],end=' ')