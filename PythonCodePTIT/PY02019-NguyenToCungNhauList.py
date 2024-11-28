def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
list = [int(i) for i in input().split()]
list.sort()
for i in range(n - 1):
    for j in range(i + 1, n):
        if gcd(list[i], list[j]) == 1:
            print(str(list[i]) + " " + str(list[j]))
