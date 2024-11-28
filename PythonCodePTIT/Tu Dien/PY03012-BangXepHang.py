n = int(input())
student = []

for _ in range(n):
    name = input().strip()
    correct, submit = (int(i) for i in input().split())
    student.append([name, correct, submit])

studentSorted = sorted(student, key=lambda x: (-x[1], x[2], x[0]))

for i in studentSorted:
    print(str(i[0]) + " " + str(i[1]) + " " + str(i[2]))
