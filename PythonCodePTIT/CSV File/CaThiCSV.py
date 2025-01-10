import csv
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

with open('cathi.csv', 'r') as file:
    data = csv.DictReader(file)
    dsct = []
    for i in data:
        dsct.append(CaThi(i['ngay'], i['gio'], i['phong']))

dsct.sort(key=lambda x: (x.times, x.id))
print(*dsct, sep="\n")