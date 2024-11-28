from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def check(n):
    cnt1 = 0
    if isPrime(len(n)) == False:
        return False
    for i in n:
        if isPrime(int(i)):
            cnt1 += 1
    if cnt1 < len(n) - cnt1:
        return False
    return True


def testCase():
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
