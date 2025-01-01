class Subject:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def __str__(self):
        return f"{self.id} {self.name} {self.type}"


n = int(input())
subjects = []
for _ in range(n):
    id = input().strip()
    name = input().strip()
    type = input().strip()
    subjects.append(Subject(id, name, type))

subjects.sort(key=lambda x: (x.id))
print(*subjects, sep="\n")
