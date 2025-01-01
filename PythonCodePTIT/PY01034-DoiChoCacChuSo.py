def findIndex(s, i):
    ans = -1
    for j in range(i + 1, len(s)):
        if s[j] < s[i]:
            if ans == -1 or s[j] > s[ans]:
                ans = j
    return ans


def testCase():
    s = input()
    s = list(s)
    ans = ""
    for i in range(len(s) - 1, -1, -1):
        index = findIndex(s, i)
        if index > -1:
            s[index], s[i] = s[i], s[index]
            ans = "".join(s)
            if ans[0] != "0":
                print(ans)
                return
            else:
                break

    print(-1)


t = int(input())
while t > 0:
    testCase()
    t -= 1
