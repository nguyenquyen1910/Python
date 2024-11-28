dic = {}
for _ in range(int(input())):
    s = input().split()
    tmp = ""
    for j in s:
        for k in j.lower():
            if k.isalpha():
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

sort_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

for word, cnt in sort_dic:
    print(word, cnt)
