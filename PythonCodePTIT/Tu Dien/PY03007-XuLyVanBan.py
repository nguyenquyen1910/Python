import re

s = ""
while True:
    try:
        s += input()
    except EOFError:
        break

s = re.split(r"[.!?]+", s)

for i in s:
    x = i.strip().lower()
    if len(x) > 0:
        word = x.split()
        word[0] = word[0].capitalize()
        print(" ".join(word))
