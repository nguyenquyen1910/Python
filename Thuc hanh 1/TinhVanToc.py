class Information:
    def __init__(self, name, address, time):
        self.name = name
        self.address = address
        self.time = time
        self.id = self.solveId()
        self.speed = self.solveSpeed()

    def solveId(self):
        listWordAddress = list(str(i) for i in self.address.split(" "))
        listWordNames = list(str(i) for i in self.name.split(" "))
        res = ""
        for word in listWordAddress:
            res += word[0].upper()
        for word in listWordNames:
            res += word[0].upper()

        return res

    def solveSpeed(self):
        startTime = 6
        hh, mm = map(int, self.time.split(":"))
        endTime = hh + mm / 60
        return 120 / (endTime - startTime)

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {round(self.speed)} Km/h"


n = int(input())
listRacers = []

for _ in range(n):
    name = input().strip()
    address = input().strip()
    time = input().strip()
    listRacers.append(Information(name, address, time))

listRacers.sort(key=lambda x: (-x.speed))

for racer in listRacers:
    print(racer)
