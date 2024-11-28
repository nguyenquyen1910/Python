import functools

n = int(input())
res = []


def Try(s, cntA, cntB, cntC):
    if len(s) <= n:
        if cntA and cntB and cntC and cntA <= cntB and cntB <= cntC:
            res.append(s)
        if len(s) == n:
            return
        Try(s + "A", cntA + 1, cntB, cntC)
        Try(s + "B", cntA, cntB + 1, cntC)
        Try(s + "C", cntA, cntB, cntC + 1)


def cmp(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    return (a > b) - (a < b)


Try("", 0, 0, 0)
sorted_res = sorted(res, key=functools.cmp_to_key(cmp))
for i in sorted_res:
    print(i)
