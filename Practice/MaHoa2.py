p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    str = input()
    if str=='0':
        break
    k, s = str.split()
    encode = ""
    for i in s:
        index = p.index(i)
        encode += p[(index+int(k))%28]
    print(encode[::-1])
