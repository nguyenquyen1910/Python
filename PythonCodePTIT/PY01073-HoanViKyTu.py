index = [0] * 100
check = [False] * 100


def Try(v):
    global s
    if len(v) == len(s):
        print(v)
        return
    for i in range(0, len(s)):
        if check[i] == False:
            check[i] = True
            Try(v + s[i])
            check[i] = False


s = input()
Try("")
