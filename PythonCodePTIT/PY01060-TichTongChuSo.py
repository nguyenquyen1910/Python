def testCase():
    s = input()
    sum = 0
    mul = 1
    for i in range(len(s)):
        if i % 2 == 1:
            sum += int(s[i])
        else:
            if s[i] != "0":
                mul *= int(s[i])
    print(str(mul) + " " + str(sum))


t = int(input())
while t > 0:
    testCase()
    t -= 1
