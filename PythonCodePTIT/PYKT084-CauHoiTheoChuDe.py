n = int(input())
mp = {}
check = True
v = []

for _ in range(n):
    if check:
        s = input().strip()
        v.append(s)
        mp[s] = 0
        check = False

    else:
        s2 = input().strip()
        if s2 == "":
            check = True
        else:
            mp[s] += 1

for i in v:
    print(f"{i}: {mp[i]}")
