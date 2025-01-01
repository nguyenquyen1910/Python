res = set()
with open("CONTACT.in", "r") as f:
    for line in f:
        line = line.lower().strip()
        if len(line)>0:
            res.add(line)

res = sorted(res)
for it in res:
    print(it)