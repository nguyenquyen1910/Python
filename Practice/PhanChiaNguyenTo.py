import math


def isPrime(num):
    for index in range(2, int(math.sqrt(num)) + 1):
        if num%index==0:
            return False
    return num>1

def testCase():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    cnt = set()
    for i in a:
        if i not in cnt:
            cnt.add(i)
            b.append(i)

    m = len(b)
    sumArray = sum(b)
    sum1=0
    for i in range(m):
        sum1+=b[i]
        if isPrime(sum1) and isPrime(sumArray-sum1):
            print(i)
            return

    print("NOT FOUND")

testCase()

