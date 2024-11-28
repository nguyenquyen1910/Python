class Student:
    def __init__(self, index, name, scores):
        self.id = f"HS{index+1:02d}"
        self.name = name
        self.scores = scores
        self.totalScore = self.solveTotalScore(scores)
        self.status = self.solveStatus()

    def solveTotalScore(self, scores):
        totalScore = 0
        totalScore += scores[0] * 2 + scores[1] * 2
        for i in range(2, 10):
            totalScore += scores[i]
        return round(totalScore / 12 + 0.01, 1)

    def solveStatus(self):
        if self.totalScore >= 9:
            return "XUAT SAC"
        elif 8 <= self.totalScore < 9:
            return "GIOI"
        elif 7 <= self.totalScore < 8:
            return "KHA"
        elif 5 <= self.totalScore < 7:
            return "TB"
        else:
            return "YEU"

    def __str__(self):
        return f"{self.id} {self.name} {self.totalScore:.1f} {self.status}"


n = int(input())
students = []

for i in range(n):
    name = input().strip()
    scores = list(map(float, input().split()))
    students.append(Student(i, name, scores))

students.sort(key=lambda x: (-x.totalScore, x.id))

for student in students:
    print(student)
