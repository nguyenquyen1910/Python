def toBaseNumber(n, base):
    if n == 0:
        return "0"
    digit = []
    while n > 0:
        digit.append(str(n % base))
        n //= base

    return "".join(digit[::-1])


def testCase():
    base = int(input())
    s = input()

    decValue = int(s, 2)
    if base == 2:
        return bin(decValue)[2:] 
    elif base == 4:
        return toBaseNumber(decValue, 4)
    elif base == 8:
        return toBaseNumber(decValue, 8)
    elif base == 16:
        return hex(decValue)[2:].upper()


t = int(input())
while t > 0:
    testCase()
    t -= 1
