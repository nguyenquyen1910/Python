class Student:
    def __init__(self, idx, name, oop, cpp, c):
        self.id = f"SV{idx+1:02d}"
        self.name = self.solveName(name)
        self.oop = oop
        self.cpp = cpp
        self.c = c
        self.meanScore = round((oop * 3 + cpp * 3 + c * 2) / 8 + 0.001, 2)
        self.rank = None

    def solveName(self, name):
        s = [word.capitalize() for word in name.split()]
        return " ".join(s)

    def __str__(self):
        return f"{self.id} {self.name} {self.meanScore:.2f} {self.rank}"


n = int(input())
students = []
for i in range(n):
    name = input().strip()
    oop = int(input().strip())
    cpp = int(input().strip())
    c = int(input().strip())
    students.append(Student(i, name, oop, cpp, c))

students.sort(key=lambda x: (-x.meanScore, x.id))

rank = 1
for i in range(n):
    if i > 0 and students[i].meanScore < students[i - 1].meanScore:
        rank = i + 1
    students[i].rank = rank

print(*students, sep="\n")
