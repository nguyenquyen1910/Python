import functools


def cmp(a, b):
    sum1 = 0
    sum2 = 0
    for i in str(a):
        sum1 += int(i)
    for i in str(b):
        sum2 += int(i)
    if sum1 != sum2:
        return sum1 - sum2
    else:
        return a - b


def testCase():
    n = int(input())
    a = list(int(i) for i in input().split())
    sorted_a = sorted(a, key=functools.cmp_to_key(cmp))
    for i in sorted_a:
        print(i, end=" ")

    print()


t = int(input())
while t > 0:
    testCase()
    t -= 1
