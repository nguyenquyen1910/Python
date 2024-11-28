def testCase():
    s = input()
    s1 = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s1[i]) - ord(s1[i - 1])):
            print("NO")
            return
    print("YES")


t = int(input())
while t > 0:
    testCase()
    t -= 1
