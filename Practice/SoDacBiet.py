MOD = int(1e9+7)
def powMod(a, b):
    if b==1:
        return a
    if b%2==0:
        return ((powMod(a, b//2) % MOD) * (powMod(a, b//2) % MOD)) % MOD
    return ((powMod(a, b//2) % MOD) * (powMod(a, b//2) % MOD)) * a % MOD
def solve(n, k):
    if k<=1:
        return k
    tmp = 0
    while k>>tmp!=1:
        tmp+=1
    return powMod(n, tmp) + solve(n, k^(1<<tmp))

def testCase():
    n, k = map(int, input().split())
    print(solve(n, k) % MOD)

t = int(input())
while t>0:
    testCase()
    t-=1