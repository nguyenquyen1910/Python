from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def check(n):
    s = str(n)
    s1 = s[::-1]
    sum = 0
    if isPrime(n) == False:
        return False
    for i in s:
        if i != "2" and i != "3" and i != "5" and i != "7":
            return False
        sum += int(i)
    if isPrime(sum) == False:
        return False
    if isPrime(int(s1)) == False:
        return False
    return True


def testCase():
    n = int(input())
    if check(n):
        print("Yes")
    else:
        print("No")


t = int(input())
while t > 0:
    testCase()
    t -= 1
