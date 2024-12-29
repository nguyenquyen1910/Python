binary = input()
while len(binary)%3 != 0:
    binary = '0' + binary

res=""
for i in range(0, len(binary), 3):
    group = binary[i:i+3]
    res += str(int(group, 2))

print(res)