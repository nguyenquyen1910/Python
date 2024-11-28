from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def testCase():
    s = input()
    for i in range(len(s)):
        if (isPrime(i) and not isPrime(int(s[i]))) or (
            not isPrime(i) and isPrime(int(s[i]))
        ):
            print("NO")
            return
    print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
