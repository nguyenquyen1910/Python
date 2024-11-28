class Student:
    def __init__(self, i, name, OOPscore, CPPscore, CScore):
        self.id = f"SV{i+1:02d}"
        self.name = self.solveName(name)
        self.OOPscore = OOPscore
        self.CPPscore = CPPscore
        self.CScore = CScore
        self.meanScore = round(
            (OOPscore * 3 + CPPscore * 3 + CScore * 2) / 8 + 0.001, 2
        )
        self.rank = None

    def solveName(self, name):
        words = [word.capitalize() for word in name.split()]
        return " ".join(words)

    def __str__(self):
        return f"{self.id} {self.name} {self.meanScore:.2f} {self.rank}"


n = int(input())
listStudents = []
for i in range(n):
    name = input().strip()
    OOPscore = int(input())
    CPPscore = int(input())
    CScore = int(input())
    listStudents.append(Student(i, name, OOPscore, CPPscore, CScore))

listStudents.sort(key=lambda x: (-x.meanScore, x.id))

rank = 1
for i, student in enumerate(listStudents):
    if i > 0 and student.meanScore < listStudents[i - 1].meanScore:
        rank = i + 1
    student.rank = rank

for student in listStudents:
    print(student)
