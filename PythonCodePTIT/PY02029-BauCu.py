from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
count = Counter(a)
a.sort(key=lambda x: (count[x], x))
cnt = count[a[-1]]
i = len(a) - 1
while i >= 0 and count[a[i]] == cnt:
    i -= 1
if i == -1:
    print("NONE")
else:
    print(a[i])
