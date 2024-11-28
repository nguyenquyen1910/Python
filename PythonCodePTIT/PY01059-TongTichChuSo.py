def testCase():
    s = input()
    sum = 0
    mul = 0
    for i in range(len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if s[i] != "0":
                if mul == 0:
                    mul = int(s[i])
                else:
                    mul *= int(s[i])
    print(str(sum) + " " + str(mul))


t = int(input())
while t > 0:
    testCase()
    t -= 1
