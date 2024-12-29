def check(n):
    cnt2 = 0
    for i in n:
        if i == "2":
            cnt2 += 1
    return cnt2 > len(n) // 2


def testCase():
    n = int(input())
    res = []
    queue = ["1", "2"]
    while len(res) < n:
        top = queue.pop(0)
        if check(top):
            res.append(top)
        queue.append(top + "0")
        queue.append(top + "1")
        queue.append(top + "2")
    print(" ".join(res))


t = int(input())
while t > 0:
    testCase()
    t -= 1
