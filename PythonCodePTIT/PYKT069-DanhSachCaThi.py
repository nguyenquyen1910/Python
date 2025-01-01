from datetime import datetime


class CaThi:
    def __init__(self, idx, day, time, room):
        self.id = f"C{idx+1:03d}"
        self.day = day
        self.time = time
        self.room = room
        self.times = datetime.strptime(self.day + " " + self.time, "%d/%m/%Y %H:%M")

    def __str__(self):
        return f"{self.id} {self.day} {self.time} {self.room}"


with open("CATHI.in", "r") as f:
    lines = f.readlines()

n = int(lines[0].strip())
sessions = []
lineIndex = 1
for i in range(n):
    day = lines[lineIndex].strip()
    time = lines[lineIndex + 1].strip()
    room = lines[lineIndex + 2].strip()
    sessions.append(CaThi(i, day, time, room))
    lineIndex += 3

sessions.sort(key=lambda x: (x.times, x.id))
print(*sessions, sep="\n")
