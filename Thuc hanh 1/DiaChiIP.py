def check(s):
    item = str(s).split(".")
    if len(item) != 4:
        return False
    for i in item:
        if not i.isdigit():
            return False
        num = int(i)
        if num < 0 or num > 255:
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
