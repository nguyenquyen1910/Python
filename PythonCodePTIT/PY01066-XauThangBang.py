def check(s):
    s1 = s[::-1]
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s1[i]) - ord(s1[i + 1])):
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
