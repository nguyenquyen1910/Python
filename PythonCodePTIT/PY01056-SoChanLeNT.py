from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def check(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                return False
        else:
            if int(s[i]) % 2 == 0:
                return False
    if isPrime(sum) == False:
        return False
    return True


def testCase():
    s = input()
    print("YES" if check(s) else "NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
