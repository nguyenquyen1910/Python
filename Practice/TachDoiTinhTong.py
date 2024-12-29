s = input()
while len(s)!=1:
    num1 = s[0:len(s)//2]
    num2 = s[len(s)//2:]
    newNum = int(num1) + int(num2)
    print(newNum)
    s = str(newNum)