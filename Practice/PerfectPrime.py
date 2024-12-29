import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
def check(n):
    if not isPrime(n):
        return False
    if not isPrime(int(str(n)[::-1])):
        return False
    for i in str(n):
        if not isPrime(int(i)):
            return False
    sumNum=0
    for i in str(n):
        sumNum+=int(i)
    return isPrime(sumNum)
def testCase():
    n = int(input())
    if check(n):
        print("Yes")
    else:
        print("No")

t = int(input())
while t>0:
    testCase()
    t-=1