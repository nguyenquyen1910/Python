from xmlrpc.client import MAXINT

t = int(input())

while t>0:
    s = input()+" "
    i=0
    minNum = MAXINT
    while i<len(s):
        num=0
        tmp=""
        if s[i].isdigit():
            while s[i].isdigit() and i<len(s):
                tmp+=s[i]
                i+=1
        else:
            i+=1
        if tmp!="":
            num = int(tmp)
        if num!=0:
            minNum=min(minNum,num)
    print(minNum)
    t-=1