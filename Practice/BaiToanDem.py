n = int(input())
a = []
while len(a) < n:
    s = input().split()
    a.extend(int(i) for i in s)
a.sort()
check = False
for i in range(1, a[-1]):
    if a.count(i)==0:
        print(i)
        check = True

if not check:
    print("Excellent!")

