def testCase():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    res = a[0] + a[1] + a[2]
    for i in range(n):
        if i > 0 and a[i] == a[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            sum = a[i] + a[j] + a[k]
            if sum == k:
                print(k)
                return
            if abs(sum - k) < abs(sum - res):
                res = sum
            if sum > k:
                j += 1
            else:
                k -= 1
    print(res)


testCase()
