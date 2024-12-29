import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1

def testCase():
    n = int(input())
    cnt=0
    for i in range(2, n-5):
        if isPrime(i) and isPrime(i+6):
            if isPrime(i+2) or isPrime(i+4):
                cnt+=1
    print(cnt)

t = int(input())
while t>0:
    testCase()
    t-=1