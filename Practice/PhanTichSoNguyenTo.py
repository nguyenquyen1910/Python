import math
def testCase():
    n = int(input())
    res="1 * "
    for i in range(2, int(math.sqrt(n))+1):
        cnt=0
        if n%i==0:
            while n%i==0:
                cnt+=1
                n//=i
            res += str(i) + "^" + str(cnt) + " * "
    if n!=1:
        res+=str(n)+"^1"
    else:
        res=res[:-3]
    print(res)

t = int(input())
while t>0:
    testCase()
    t-=1
