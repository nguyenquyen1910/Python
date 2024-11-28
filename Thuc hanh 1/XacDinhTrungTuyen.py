class Teacher:
    def __init__(self, i, name, field, ITScore, fieldScore):
        self.id = f"GV{i+1:02d}"
        self.name = name
        self.field = field
        self.ITScore = ITScore
        self.fieldScore = fieldScore
        self.subject = self.solveSubject()
        self.bonusScore = self.solveBonusScore()
        self.totalScore = self.ITScore * 2 + self.fieldScore + self.bonusScore
        self.status = "TRUNG TUYEN" if self.totalScore >= 18 else "LOAI"

    def solveBonusScore(self):
        if self.field[1] == "1":
            return 2
        if self.field[1] == "2":
            return 1.5
        if self.field[1] == "3":
            return 1
        return 0

    def solveSubject(self):
        if self.field[0] == "A":
            return "TOAN"
        if self.field[0] == "B":
            return "LY"
        return "HOA"

    def __str__(self):
        return (
            f"{self.id} {self.name} {self.subject} {self.totalScore:.1f} {self.status}"
        )


n = int(input())
listTeachers = []
for i in range(n):
    name = input().strip()
    field = input().strip()
    ITScore = float(input())
    fieldScore = float(input())
    listTeachers.append(Teacher(i, name, field, ITScore, fieldScore))

listTeachers.sort(key=lambda x: (-x.totalScore, x.id))

for teacher in listTeachers:
    print(teacher)
