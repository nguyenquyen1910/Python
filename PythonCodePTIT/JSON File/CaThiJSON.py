import json
from datetime import datetime


class CaThi:
    idx = 1
    def __init__(self, day, time, room):
        self.id = f"C{CaThi.idx:03d}"
        CaThi.idx+=1
        self.day = day
        self.time = time
        self.room = room
        self.times = datetime.strptime(self.day+" "+self.time, "%d/%m/%Y %H:%M")

    def __str__(self):
        return f"{self.id} {self.day} {self.time} {self.room}"

with open("cathi.json", "r") as file:
    data = json.load(file)

dsct = []
for i in data['cathi']:
    dsct.append(CaThi(i['ngay'], i['gio'], i['phong']))

dsct = sorted(dsct, key=lambda d: (d.times, d.id))
print(*dsct, sep="\n")