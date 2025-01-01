class Teacher:
    def __init__(self, idx, name, code, itPoint, specPoint):
        self.id = f"GV{idx+1:02d}"
        self.name = name
        self.code = code
        self.itPoint = itPoint
        self.specPoint = specPoint
        self.bonusPoint = self.solveBonusPoint()
        self.subject = self.solveSubject()
        self.score = self.itPoint * 2 + self.specPoint + self.bonusPoint
        self.status = "TRUNG TUYEN" if self.score >= 18 else "LOAI"

    def solveBonusPoint(self):
        if self.code.endswith("1"):
            return 2.0
        if self.code.endswith("2"):
            return 1.5
        if self.code.endswith("3"):
            return 1.0
        return 0.0

    def solveSubject(self):
        if self.code.startswith("A"):
            return "TOAN"
        if self.code.startswith("B"):
            return "LY"
        return "HOA"

    def __str__(self):
        return f"{self.id} {self.name} {self.subject} {self.score:.1f} {self.status}"


n = int(input())
teachers = []
for i in range(n):
    name = input().strip()
    code = input().strip()
    itPoint = float(input().strip())
    specPoint = float(input().strip())
    teachers.append(Teacher(i, name, code, itPoint, specPoint))

teachers.sort(key=lambda x: (-x.score))
print(*teachers, sep="\n")
