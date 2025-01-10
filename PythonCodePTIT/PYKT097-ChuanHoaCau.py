data = ""
while True:
    try:
        data += input()
        if data[-1] not in ".!?":
            data += " ."
        else:
            if data[-2] != " ":
                data = f"{data[:-1]} {data[-1]}"
        data += " "
    except Exception as e:
        break

words = data.split()
i = 0
while i < len(words):
    res = ""
    while i < len(words) and words[i] not in ".!?":
        res += words[i] + " "
        i += 1
    if words[i] in ".!?":
        res = res.strip() + words[i]
    i += 1
    print(res[0].upper() + res[1:].lower())
