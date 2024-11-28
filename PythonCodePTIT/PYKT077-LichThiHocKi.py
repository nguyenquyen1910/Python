class Subject:
    def __init__(self, subjectId, subjectName):
        self.subjectId = subjectId
        self.subjectName = subjectName


class Schedule:
    def __init__(self, index, subjectId, date, time, idSche):
        self.id = f"T{index+1:03d}"
        self.subjectId = subjectId
        self.date = date
        self.time = time
        self.idSche = idSche
        self.subject = next(
            subject for subject in subjects if subjectId == subject.subjectId
        )
        self.day = int(date[0:2])
        self.month = int(date[3:5])
        self.year = int(date[6:10])
        self.hour = int(time[0:2])
        self.minute = int(time[3:5])

    def __str__(self):
        return f"{self.id} {self.subjectId} {self.subject.subjectName} {self.date} {self.time} {self.idSche}"


n, m = map(int, input().split())
subjects = []
for i in range(n):
    subjects.append(Subject(input().strip(), input().strip()))

schedules = []
for i in range(m):
    a = list(str(i) for i in input().split())
    subjectId = a[0].strip()
    date = a[1].strip()
    time = a[2].strip()
    idSche = a[3].strip()

    schedules.append(Schedule(i, subjectId, date, time, idSche))

schedules.sort(key=lambda x: (x.year, x.month, x.day, x.hour, x.minute, x.subjectId))

for schedule in schedules:
    print(schedule)
