from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


n = int(input())
list = [int(i) for i in input().split()]
cnt = {}
for i in list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in list:
    if cnt[i] != 0:
        if isPrime(i):
            print(str(i) + " " + str(cnt[i]))
        cnt[i] = 0
