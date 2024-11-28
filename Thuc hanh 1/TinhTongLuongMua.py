class Position:
    def __init__(self, name):
        self.name = name
        self.totalRain = 0
        self.totalTime = 0

    def solveTime(self, timeStr):
        hh, mm = map(int, timeStr.split(":"))
        return hh * 60 + mm

    def addRain(self, startTime, endTime, rainAmount):
        sMinutes = self.solveTime(startTime)
        eMinutes = self.solveTime(endTime)

        rainTime = eMinutes - sMinutes

        self.totalRain += rainAmount
        self.totalTime += rainTime

    def meanRain(self):
        if self.totalTime == 0:
            return 0
        return self.totalRain / (self.totalTime / 60)


n = int(input())
listPositions = {}
stations = []

for _ in range(n):
    name = input().strip()
    startTime = input().strip()
    endTime = input().strip()
    rain = int(input().strip())

    if name not in listPositions:
        listPositions[name] = Position(name)
        stations.append(name)

    listPositions[name].addRain(startTime, endTime, rain)

for i, name in enumerate(listPositions):
    id = f"T{i+1:02d}"
    position = listPositions[name]
    meanRain = position.meanRain()
    print(f"{id} {name} {meanRain:.2f}")
