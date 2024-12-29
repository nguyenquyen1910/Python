def solvePoint(point):
    if point>10:
        return point/10
    return point


class Candidate:
    def __init__(self, index, name, theoPoint, practicePoint):
        self.id = "TS0"+str(index+1)
        self.name = name
        self.theoPoint = solvePoint(theoPoint)
        self.practicePoint = solvePoint(practicePoint)
        self.averagePoint = (self.theoPoint + self.practicePoint) / 2
        self.status = self.solveStatus()

    def solveStatus(self):
        if self.averagePoint < 5:
            return "TRUOT"
        if self.averagePoint < 8:
            return "CAN NHAC"
        if self.averagePoint < 9.5:
            return "DAT"
        return "XUAT SAC"

    def __str__(self):
        return f"{self.id} {self.name} {self.averagePoint:.2f} {self.status}"
n = int(input())
candidates = []
for i in range(n):
    name = input()
    theoPoint = float(input())
    practicePoint = float(input())
    candidates.append(Candidate(i, name, theoPoint, practicePoint))

candidates.sort(key = lambda c: (-c.averagePoint))
for c in candidates:
    print(c)