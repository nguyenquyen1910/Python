fibo = [0] * 100


def init():
    fibo[0] = 0
    fibo[1] = 1
    fibo[2] = 1
    for i in range(3, 100):
        fibo[i] = fibo[i - 1] + fibo[i - 2]


def testCase():
    a, b = [int(i) for i in input().split()]
    for i in range(a, b + 1):
        print(fibo[i], end=" ")
    print()


t = int(input())
init()
while t > 0:
    testCase()
    t -= 1
