import functools


def cmp(a, b):
    mul1 = 1
    mul2 = 1
    for i in str(a):
        mul1 *= int(i)
    for i in str(b):
        mul2 *= int(i)
    if mul1 != mul2:
        return mul1 - mul2
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
