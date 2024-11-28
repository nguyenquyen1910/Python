class ThiSinh:
    def __init__(self, i, name, score, national, area):
        self.id = f"TS{i+1:02d}"
        self.name = name
        self.score = score
        self.national = national
        self.area = area
        self.bonusScore = self.solveScoreBonus()
        self.totalScore = self.score + self.bonusScore
        self.status = self.solveStatus()

    def solveScoreBonus(self):
        bonus = 0
        if self.area == 1:
            bonus = 1.5
        elif self.area == 2:
            bonus = 1

        if self.national != "Kinh":
            bonus += 1.5

        return bonus

    def solveStatus(self):
        if self.totalScore >= 20.5:
            return "Do"
        return "Truot"

    def __str__(self):
        return f"{self.id} {self.name} {self.totalScore:.1f} {self.status}"


def solveName(name):
    words = name.strip().split()
    words = [word.capitalize() for word in words]
    return " ".join(words)


n = int(input())
thiSinh = []
for i in range(n):
    name = input().strip()
    score = float(input().strip())
    national = input().strip()
    area = int(input().strip())

    thiSinh.append(ThiSinh(i, solveName(name), score, national, area))

thiSinh.sort(key=lambda x: (-x.totalScore, x.id))

for ts in thiSinh:
    print(ts)
