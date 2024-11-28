def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def testCase():
    n = int(input())
    s = str(n)
    sum = 0
    for i in s:
        sum += factorial(int(i))
    if sum == n:
        print("Yes")
    else:
        print("No")


t = int(input())
while t > 0:
    testCase()
    t -= 1
