def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = a[l + i]
    for i in range(n2):
        R[i] = a[m + 1 + i]
    i = j = 0
    ans = 0
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[l] = L[i]
            i += 1
        else:
            a[l] = R[j]
            j += 1
            ans += len(L) - i
        l += 1
    while i < n1:
        a[l] = L[i]
        i += 1
        l += 1
    while j < n2:
        a[l] = R[j]
        j += 1
        l += 1
    return ans


def mergeCount(a, l, r):
    if l < r:
        m = (l + r) // 2
        return mergeCount(a, l, m) + mergeCount(a, m + 1, r) + merge(a, l, m, r)
    return 0


def testCase():
    n = int(input())
    a = list(int(i) for i in input().split())
    print(mergeCount(a, 0, n - 1))


t = 1
while t > 0:
    testCase()
    t -= 1
