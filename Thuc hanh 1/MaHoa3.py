def rotate_string(s, rotation):
    rotated = []
    for char in s:
        newChar = chr((ord(char) - ord("A") + rotation) % 26 + ord("A"))
        rotated.append(newChar)
    return "".join(rotated)


def merge_strings(s1, s2):
    merged = []
    for char1, char2 in zip(s1, s2):
        newChar = chr((ord(char1) - ord("A") + (ord(char2) - ord("A"))) % 26 + ord("A"))
        merged.append(newChar)
    return "".join(merged)


def drm_encoding(s):

    mid = len(s) // 2
    firstHaft = s[:mid]
    secondHaft = s[mid:]

    rotateFirst = sum(ord(char) - ord("A") for char in firstHaft)
    rotateSecond = sum(ord(char) - ord("A") for char in secondHaft)

    rotated_firstHaft = rotate_string(firstHaft, rotateFirst)
    rotated_secondHaft = rotate_string(secondHaft, rotateSecond)

    result = merge_strings(rotated_firstHaft, rotated_secondHaft)

    return result


T = int(input())

for _ in range(T):
    test_string = input().strip()
    print(drm_encoding(test_string))
