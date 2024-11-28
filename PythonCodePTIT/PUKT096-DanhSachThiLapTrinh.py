class Team:
    def __init__(self, index, name, univ):
        self.id = f"Team{index+1:02d}"
        self.name = name
        self.univ = univ


class ThiSinh:
    def __init__(self, index, fullname, teamId):
        self.id = f"C{index+1:03d}"
        self.fullname = fullname
        self.teamId = teamId
        self.team = next(team for team in teams if team.id == teamId)

    def __str__(self):
        return f"{self.id} {self.fullname} {self.team.name} {self.team.univ}"


n = int(input())
teams = []
for i in range(n):
    teams.append(Team(i, input().strip(), input().strip()))

m = int(input())
thisinhs = []
for i in range(m):
    fullname = input().strip()
    teamId = input().strip()

    thisinhs.append(ThiSinh(i, fullname, teamId))

thisinhs.sort(key=lambda x: (x.fullname))

for thisinh in thisinhs:
    print(thisinh)
