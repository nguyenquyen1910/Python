import re

dic = {}


for i in range(int(input())):
    s = input().split()
    tmp = ""
    for j in s:
        for k in j.lower():
            if k.isalnum():
                tmp += k
            else:
                if len(tmp) > 0:
                    if tmp in dic:
                        dic[tmp] += 1
                    else:
                        dic[tmp] = 1
                tmp = ""
        if len(tmp) > 0:
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
        tmp = ""

sorted_a = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

for i, cnt in sorted_a:
    print(i, cnt)
