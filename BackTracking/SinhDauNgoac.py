res = []


def Try(openP, closeP, s, n):
    if openP == closeP and openP + closeP == n * 2:
        res.append(s)
        return
    if openP < n:
        Try(openP + 1, closeP, s + "(", n)
    if closeP < openP:
        Try(openP, closeP + 1, s + ")", n)


n = int(input())
Try(0, 0, "", n)
print(res)
