import re

s = ""
while True:
    try:
        s += input()
    except EOFError:
        break

s = re.split(r"[.?!]", s)
for line in s:
    line = line.strip().lower()
    if len(line) > 0:
        words = line.split()
        words[0] = words[0].capitalize()
        print(" ".join(words))
