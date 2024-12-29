from collections import Counter

s = input()
k = int(input())
res = []
while len(s) > 0:
    x = int(s[:2])
    if len(str(x)) == 2:
        res.append(x)
    s = s[2:]

count = Counter(res)
check = False
for i in sorted(res):
    if count[i] >= k:
        print(i, count[i])
        count[i] = 0
        check = True
if not check:
    print("NOT FOUND")
