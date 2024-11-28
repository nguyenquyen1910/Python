class Station:
    def __init__(self, name):
        self.name = name
        self.totalRain = 0
        self.totalTime = 0

    def solveTime(self, timeStr):
        hh, mm = map(int, timeStr.split(":"))
        return hh * 60 + mm

    def addRain(self, startTime, endTime, rainAmount):
        sMinu = self.solveTime(startTime)
        eMinu = self.solveTime(endTime)

        rainTime = eMinu - sMinu

        self.totalRain += rainAmount
        self.totalTime += rainTime

    def meanRain(self):
        if self.totalTime == 0:
            return 0
        return self.totalRain / (self.totalTime / 60)


n = int(input())
listStation = {}
stations = []

for _ in range(n):
    name = input().strip()
    startTime = input().strip()
    endTime = input().strip()
    rain = float(input().strip())

    if name not in listStation:
        listStation[name] = Station(name)
        stations.append(name)

    listStation[name].addRain(startTime, endTime, rain)

for i, name in enumerate(stations):
    idStation = f"T{i+1:02d}"
    station = listStation[name]
    meanRain = station.meanRain()
    print(f"{idStation} {name} {meanRain:.2f}")
