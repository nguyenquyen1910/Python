def Try(i):
    global n, k, index
    for j in range(index[i-1]+1, n-k+i+1):
        index[i]=j
        if i==k-1:
            print(" ".join(a[index[x]] for x in range(k)))
        else:
            Try(i+1)


n, k = map(int, input().split())
a = input().split()
a = sorted(set(a))
a.insert(0, "a")
n = len(a)
index = [0] * 100
Try(0)