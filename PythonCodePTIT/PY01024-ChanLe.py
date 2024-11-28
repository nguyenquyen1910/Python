def check(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 10 != 0:
        return False
    for i in range(0, len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            return False
    return True


def testCase():
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")


t = int(input())
while t > 0:
    testCase()
    t -= 1
