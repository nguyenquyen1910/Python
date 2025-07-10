n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
res = []
for i in range(n - 3):
    if i > 0 and a[i] == a[i - 1]:
        continue
    for j in range(i + 1, n - 2):
        if j > i + 1 and a[j] == a[j - 1]:
            continue
        l = j + 1
        r = n - 1
        while l < r:
            sum = a[i] + a[j] + a[l] + a[r]
            if sum == k:
                res.append([a[i], a[j], a[l], a[r]])
                l += 1
                r -= 1
                while l < r and a[l] == a[l - 1]:
                    l += 1
                while l < r and a[r] == a[r + 1]:
                    r -= 1
            elif sum > k:
                r -= 1
            else:
                l += 1
for i in res:
    print(*i)
