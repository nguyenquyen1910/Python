from datetime import datetime


class Player:
    def __init__(self, id, name, startTime, endTime):
        self.id = id
        self.name = name
        self.startTime = datetime.strptime(startTime, "%H:%M")
        self.endTime = datetime.strptime(endTime, "%H:%M")
        self.time = int((self.endTime - self.startTime).seconds)
        self.hour = self.time // (60*60)
        self.minute = self.time // 60 % 60

    def __str__(self):
        return f"{self.id} {self.name} {self.hour} gio {self.minute} phut"


n = int(input())
players = []
for _ in range(n):
    id = input()
    name = input()
    startTime = input()
    endTime = input()
    players.append(Player(id, name, startTime, endTime))

players.sort(key = lambda c: (-c.time))
for player in players:
    print(player)

