class Candidate:
    def __init__(self, i, name, score, nation, area):
        self.id = f"TS{i+1:02d}"
        self.name = name
        self.score = score
        self.nation = nation
        self.area = area
        self.bonusScore = self.solveBonusScore()
        self.totalScore = self.score + self.bonusScore
        self.status = "Do" if self.totalScore >= 20.5 else "Truot"

    def solveBonusScore(self):
        bonus = 0
        if self.nation != "Kinh":
            bonus = 1.5
        if self.area == 1:
            bonus += 1.5
        if self.area == 2:
            bonus += 1
        if self.area == 3:
            bonus += 0
        return bonus

    def solveName(self):
        tmp = list(str(i) for i in self.name.split())
        res = ""
        for word in tmp:
            res += word[0].upper() + word[1 : len(word)].lower() + " "
        return res.strip()

    def __str__(self):
        return f"{self.id} {self.solveName()} {self.totalScore} {self.status}"


n = int(input())
listCandidates = []
for i in range(n):
    name = input().strip()
    score = float(input())
    nation = input().strip()
    area = int(input())
    listCandidates.append(Candidate(i, name, score, nation, area))

listCandidates.sort(key=lambda x: (-x.totalScore, x.id))

for candidate in listCandidates:
    print(candidate)
