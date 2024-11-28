def testCase():
    s = input()
    length = 0
    newLine = ""
    words = s.split()
    for i in words:
        if length + len(i) + 1 <= 100:
            newLine += i + " "
            length += len(i) + 1
        else:
            break
    print(newLine)


t = int(input())
while t > 0:
    testCase()
    t -= 1
