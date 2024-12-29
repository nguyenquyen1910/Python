def testCase():
    p, q = input().split()
    s = input().split()
    if len(s) == 1:
        x1 = s[0]
        x2 = input()
    else:
        x1 = s[0]
        x2 = s[1]
    num1 = int(x1.replace(p, q)) + int(x2.replace(p, q))
    num2 = int(x1.replace(q, p)) + int(x2.replace(q, p))
    print(min(num1, num2), max(num1, num2))

t = int(input())
while t>0:
    testCase()
    t-=1