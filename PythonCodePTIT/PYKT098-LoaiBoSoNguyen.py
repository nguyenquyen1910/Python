from xmlrpc.client import MAXINT

f = open("DATA.in", "r")
a = f.read().split()
res = []
for i in a:
    try:
        num = int(i)
        if num>MAXINT:
            res.append(i)
    except:
        res.append(i)
res.sort()
print(*res)