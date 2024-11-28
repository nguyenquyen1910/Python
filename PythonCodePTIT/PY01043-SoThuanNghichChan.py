def check(n):
    if n != n[::-1]:
        return False
    for i in n:
        if int(i) % 2 != 0:
            return False
    if len(n) % 2 != 0:
        return False
    return True


def testCase():
    n = int(input())
    for i in range(22, n):
        if check(str(i)):
            print(i, end=" ")
    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
