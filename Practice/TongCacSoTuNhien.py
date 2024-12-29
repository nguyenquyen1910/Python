res = []
used = set()
def Try(i, current, start):
    if i == 0:
        sortedTuple = tuple(sorted(current, reverse=True))
        if sortedTuple not in used:
            used.add(sortedTuple)
            res.append(sortedTuple)
        return
    for j in range(start, 0, -1):
        if j<=i:
            current.append(j)
            Try(i-j, current, i)
            current.pop()

def testCase():
    n = int(input())
    global res, used
    res.clear()
    used.clear()
    Try(n, [], n)
    print(len(res))
    for it in res:
        tmp="("
        for num in it:
            tmp+=str(num)+" "
        tmp = tmp.strip()+") "
        print(tmp, end="")
    print()

t = int(input())
while t>0:
    testCase()
    t-=1