class ThiSinh:
    def __init__(self, tenTS, nsTS, score1, score2, score3):
        self.tenTS = tenTS
        self.nsTS = nsTS
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def __str__(self) -> str:
        return f"{self.tenTS} {self.nsTS} {(self.score1+self.score2+self.score3):.1f}"


tenTS = input()
nsTS = input()
score1 = float(input())
score2 = float(input())
score3 = float(input())

print(ThiSinh(tenTS, nsTS, score1, score2, score3))
