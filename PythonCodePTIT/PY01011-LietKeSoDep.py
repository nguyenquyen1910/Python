def check(s):
    if len(s) % 2 == 1 or s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 == 1:
            return False
    return True


def testCase():
    n = input()
    for i in range(22, int(n), 2):
        if check(str(i)):
            print(i, end=" ")


t = int(input())
while t > 0:
    testCase()
    print()
    t -= 1
