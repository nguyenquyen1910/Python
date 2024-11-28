def check(n):
    for i in n:
        if i != "0" and i != "1" and i != "2":
            return False
    return True


def testCase():
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
