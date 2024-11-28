s = input()
while len(s) > 1:
    mid = len(s) // 2
    n1 = int(s[:mid])
    n2 = int(s[mid:])
    print(n1 + n2)
    s = str(n1 + n2)
