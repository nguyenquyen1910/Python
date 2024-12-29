import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
def testCase():
    k = int(input())
    used = []
    for i in range(12, k):
        if (
                int(str(i)[::-1])<k
                and isPrime(i)
                and isPrime(int(str(i)[::-1]))
                and i!=int(str(i)[::-1])
                and str(i) not in used
        ):
            used += [str(i), str(i)[::-1]]
            print(i, int(str(i)[::-1]), end=" ")

t = int(input())
while t>0:
    testCase()
    print()
    t-=1