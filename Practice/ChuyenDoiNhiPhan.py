from math import log2


def toS(i):
    if i<=9:
        return str(i)
    return chr(ord('A') + i-10)

def convert(s):
    r=0
    for i in s:
        r = r << 1 | int(i)
    return toS(r)
with open("DATA.in", "r") as f:
    t = int(f.readline())
    while t>0:
        n = int(log2(int(f.readline())))
        s = f.readline().strip()
        res = ""
        while s!='':
            res = convert(s[-n:])+res
            s = s[:-n]
        print(res)
        t-=1