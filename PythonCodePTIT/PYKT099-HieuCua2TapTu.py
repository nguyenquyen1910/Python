with open("DATA1.in", "r") as f1:
    data1 = f1.readlines()
with open("DATA2.in", "r") as f2:
    data2 = f2.readlines()

words1 = set(word for line in data1 for word in line.lower().split())
words2 = set(word for line in data2 for word in line.lower().split())
inData1 = sorted(words1 - words2)
inData2 = sorted(words2 - words1)
print(*inData1, sep=" ")
print(*inData2, sep=" ")