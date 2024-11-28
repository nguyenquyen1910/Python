class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Schedule:
    def __init__(self, index, subId, date, time, group):
        self.scheId = f"T{index+1:03d}"
        self.subId = subId
        self.date = date
        self.time = time
        self.group = group
        self.subject = next(subject for subject in subjects if subject.id == self.subId)
        self.day = int(date[0:2])
        self.month = int(date[3:5])
        self.year = int(date[6:10])
        self.hour = int(time[0:2])
        self.minute = int(time[3:5])

    def __str__(self):
        return f"{self.scheId} {self.subId} {self.subject.name} {self.date} {self.time} {self.group}"


n, m = map(int, input().split())
subjects = []
for i in range(n):
    id = input().strip()
    name = input().strip()
    subjects.append(Subject(id, name))

schedules = []
for i in range(m):
    a = list(str(i) for i in input().split())
    subId = a[0].strip()
    date = a[1].strip()
    time = a[2].strip()
    group = a[3].strip()
    schedules.append(Schedule(i, subId, date, time, group))

schedules.sort(key=lambda x: (x.year, x.month, x.day, x.hour, x.minute, x.subId))
for schedule in schedules:
    print(schedule)
