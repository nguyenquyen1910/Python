n = int(input())
a = [2, 3, 5, 7]
ans = set()


def check(num):
    if int(num) % 2 == 0:
        return False
    tmp = set()
    for i in num:
        tmp.add(int(i))
    if len(tmp) != 4:
        return False
    return True


def Try(s):
    if len(s) >= 4 and check(s):
        ans.add(s)
    if len(s) == n:
        return
    for j in a:
        Try(s + str(j))


Try("")
ans = sorted(ans, key=lambda x: (int(x)))
print(*ans, sep="\n")
