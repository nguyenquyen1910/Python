from collections import Counter

s = input()
res = []
tmp = set()
while len(s) > 0:
    x = int(s[:2])
    if len(str(x)) == 2:
        res.append(x)
    s = s[2:]

count = Counter(res)
for i in res:
    if count[i] != 0:
        print(i, count[i])
        count[i] = 0
