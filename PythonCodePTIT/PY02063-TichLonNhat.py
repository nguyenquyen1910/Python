n = int(input())
a = sorted(list(map(int, input().split())))
maxValue = max(a[-2] * a[-1], a[0] * a[1])
maxValue2 = max(a[-2] * a[-1] * a[-3], a[0] * a[1] * a[-1])
print(max(maxValue, maxValue2))
