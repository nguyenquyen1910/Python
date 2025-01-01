from datetime import datetime


class Player:
    def __init__(self, name, address, endTime):
        self.name = name
        self.address = address
        self.endTime = endTime
        self.id = self.solveId()
        self.time = self.solveTime()
        self.speed = round(120 / (self.time / (60 * 60)))

    def solveId(self):
        res = ""
        for i in self.address.upper().split():
            res += i[0]
        for i in self.name.upper().split():
            res += i[0]
        return res

    def solveTime(self):
        timeStart = datetime.strptime("6:00", "%H:%M")
        timeEnd = datetime.strptime(self.endTime, "%H:%M")
        return (timeEnd - timeStart).total_seconds()

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {self.speed} Km/h"


n = int(input())
players = []
for _ in range(n):
    name = input().strip()
    address = input().strip()
    endTime = input().strip()
    players.append(Player(name, address, endTime))

players.sort(key=lambda x: (x.time))
print(*players, sep="\n")
