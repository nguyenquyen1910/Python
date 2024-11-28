n = int(input())
list = [float(i) for i in input().split()]
s = 0
maxScore = 0
minScore = 11
for i in list:
    maxScore = max(maxScore, i)
    minScore = min(minScore, i)
for i in list:
    if i == maxScore or i == minScore:
        list.remove(i)

for i in list:
    s += i
print("{:.2f}".format(s / len(list)))
