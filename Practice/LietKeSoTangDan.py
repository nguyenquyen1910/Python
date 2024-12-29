s = input()
tmp = set()
res = []
while len(s)>0:
    x = int(s[:2])
    if len(str(x)) == 2:
        if x not in tmp:
            tmp.add(x)
            res.append(x)
    s = s[2:]
print(*res)