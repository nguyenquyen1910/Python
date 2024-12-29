def testCase():
    n = input()
    num = input()
    cnt = i = 0
    while i<len(n):
        if n[i:i+len(num)] == num:
            cnt+=1
            i+=len(num)
        else:
            i+=1
    print(cnt)

t = int(input())
while t>0:
    testCase()
    t-=1