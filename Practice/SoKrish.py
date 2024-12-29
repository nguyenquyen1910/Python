def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def check(n):
    tmp=n
    sum=0
    while n>0:
        sum+=factorial(n%10)
        n//=10
    return sum==tmp
def testCase():
    n = int(input())
    print("Yes" if check(n) else "No")
t = int(input())
while t>0:
    testCase()
    t-=1