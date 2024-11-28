s = input()
lower = 0
for x in s:
    if x.islower():
        lower += 1
if lower >= len(s) - lower:
    print(s.lower())
else:
    print(s.upper())
