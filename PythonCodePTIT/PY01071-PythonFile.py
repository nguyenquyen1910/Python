def testCase():
    s = str(input().lower())
    if ".py" in s:
        print("yes")
    else:
        print("no")


t = 1
while t > 0:
    testCase()
    t -= 1
