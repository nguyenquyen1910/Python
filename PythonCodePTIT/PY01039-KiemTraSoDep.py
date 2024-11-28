def check(s):
    for i in range(0, len(s) - 2):
        if s[i] != s[i + 2]:
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
