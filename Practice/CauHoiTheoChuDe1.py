n = int(input())
dic = {}
count = []
for _ in range(n):
    s = input()
    if s != "":
        count.append(s)
        if len(count) == 1:
            dic[count[0]] = 0
        else:
            dic[count[0]] += 1
    else:
        count.clear()

for k, v in dic.items():
    print(f"{k}: {v}")