class Student:
    def __init__(self, name, correct, submit):
        self.name = name
        self.correct = correct
        self.submit = submit

    def __str__(self):
        return f"{self.name} {self.correct} {self.submit}"


n = int(input())
students = []
for _ in range(n):
    name = input()
    correct, submit = map(int, input().strip().split())
    students.append(Student(name, correct, submit))

students.sort(key=lambda s: (-s.correct, s.submit, s.name))
for student in students:
    print(student)
