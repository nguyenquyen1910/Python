def handleReadingAndListening(score):
    if 3 <= score <= 4:
        return 2.5
    if 5 <= score <= 6:
        return 3.0
    if 7 <= score <= 9:
        return 3.5
    if 10 <= score <= 12:
        return 4.0
    if 13 <= score <= 15:
        return 4.5
    if 16 <= score <= 19:
        return 5.0
    if 20 <= score <= 22:
        return 5.5
    if 23 <= score <= 26:
        return 6.0
    if 27 <= score <= 29:
        return 6.5
    if 30 <= score <= 32:
        return 7.0
    if 33 <= score <= 34:
        return 7.5
    if 35 <= score <= 36:
        return 8.0
    if 37 <= score <= 38:
        return 8.5
    if 39 <= score <= 40:
        return 9.0


t = int(input())
while t > 0:
    reading, listening, speaking, writing = (float(i) for i in input().split())
    reading = handleReadingAndListening(reading)
    listening = handleReadingAndListening(listening)
    meanScore = (reading + listening + speaking + writing) / 4
    if meanScore - int(meanScore) >= 0.75:
        meanScore = int(meanScore) + 1.0
    if meanScore - int(meanScore) >= 0.25:
        meanScore = int(meanScore) + 0.5
    if meanScore - int(meanScore) < 0.25:
        meanScore = float(int(meanScore))
    print(meanScore)
    t -= 1
