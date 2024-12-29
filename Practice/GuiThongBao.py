n = int(input())
while n>0:
    s = input()
    length = 0
    newLine = ""
    words = s.split()
    for word in words:
        if length + len(word) + 1 <= 100:
            newLine += word + " "
            length += len(word) + 1
        else:
            break
    print(newLine)
    n-=1