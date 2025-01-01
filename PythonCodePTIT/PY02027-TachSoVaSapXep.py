import re

a = []

n = int(input())
for _ in range(n):
    s = input()
    for i in re.split("[a-zA-Z]", s):
        if i != "":
            a.append(int(i))
a.sort()
print(*a, sep="\n")
