from collections import Counter


def testCase():
    global res
    n = int(input())
    a = list(int(i) for i in input().split())
    count = Counter(a)
    for i in a:
        if count[i] % 2 == 1:
            res = i
    print(res)


t = int(input())
while t > 0:
    testCase()
    t -= 1
