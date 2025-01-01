class Student:
    def __init__(self, id, name, className):
        self.id = id
        self.name = name
        self.className = className
        self.score = 10

    def caculateScore(self, rollCall):
        for i in rollCall:
            if i == "v":
                self.score -= 2
            elif i == "m":
                self.score -= 1
        self.score = max(self.score, 0)
        if self.score == 0:
            self.status = "KDDK"

    def __str__(self):
        if self.score == 0:
            return f"{self.id} {self.name} {self.className} {self.score} {self.status}"
        return f"{self.id} {self.name} {self.className} {self.score}"


n = int(input())
students = []
for _ in range(n):
    id = input()
    name = input()
    className = input()
    students.append(Student(id, name, className))

for _ in range(n):
    id, rollCall = input().strip().split()
    for student in students:
        if student.id == id:
            student.caculateScore(rollCall)
            break

for student in students:
    print(student)
