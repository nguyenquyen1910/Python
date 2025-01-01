from collections import Counter


def check(element):
    return element== element[::-1]

f = open("VANBAN.in", "r")
a = f.read().split()
ans = sorted([i for i in a if check(i)], key=lambda x: (-len(x)))
maxLen = len(ans[0])
cnt = Counter(ans)
for it in a:
    if check(it):
        if len(it)==maxLen and cnt[it]>0:
            print(it, cnt[it])
            cnt[it] = 0
