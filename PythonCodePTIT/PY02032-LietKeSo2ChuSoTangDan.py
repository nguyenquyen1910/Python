s = input()
res = set()
while len(s) > 0:
    x = int(s[:2])
    if len(str(x)) == 2:
        res.add(x)
    s = s[2:]
res = sorted(list(res))
print(*res)
