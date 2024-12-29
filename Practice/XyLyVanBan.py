import re

s=""
while True:
    try:
        s+=input()
    except EOFError:
        break

s = re.split(r"[.?!]+", s)
for line in s:
    line = line.strip().lower()
    if len(line) > 0:
        word = line.split()
        word[0] = word[0].capitalize()
        print(" ".join(word))