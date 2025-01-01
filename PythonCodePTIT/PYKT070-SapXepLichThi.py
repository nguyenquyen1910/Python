from datetime import datetime

class MonThi:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

class CaThi:
    def __init__(self, idx, day, time, room):
        self.id = f"C{idx+1:03d}"
        self.day = day
        self.time = time
        self.room = room

class LichThi:
    def __init__(self, sesId, subId, group, quantity):
        self.sesId = sesId
        self.subId = subId
        self.group = group
        self.quantity = quantity
        self.subject = next(
            subject for subject in subjects if subject.id == self.subId
        )
        self.session = next(
            ses for ses in sessions if ses.id == self.sesId
        )
        self.times = datetime.strptime(self.session.day+" "+self.session.time, "%d/%m/%Y %H:%M")


    def __str__(self):
        return f"{self.session.day} {self.session.time} {self.session.room} {self.subject.name} {self.group} {self.quantity}"

with open("MONTHI.in", "r") as f1:
    data1 = f1.readlines()
n = int(data1[0].strip())
idx1 = 1
subjects = []
for _ in range(n):
    id = data1[idx1].strip()
    name = data1[idx1+1].strip()
    type = data1[idx1+2].strip()
    subjects.append(MonThi(id, name, type))
    idx1 += 3

sessions = []
with open("CATHI.in", "r") as f2:
    data2 = f2.readlines()
m = int(data2[0].strip())
idx2 = 1
for i in range(m):
    day = data2[idx2].strip()
    time = data2[idx2+1].strip()
    room = data2[idx2+2].strip()
    sessions.append(CaThi(i, day, time, room))
    idx2 += 3
schedule = []
with open("LICHTHI.in", "r") as f3:
    data3 = f3.readlines()
o = int(data3[0].strip())
idx3 = 1
for _ in range(o):
    sesId, subId, group, quantity = data3[idx3].split()
    schedule.append(LichThi(sesId, subId, group, quantity))
    idx3 += 1

schedule.sort(key=lambda s: (s.times, s.sesId))
print(*schedule, sep="\n")