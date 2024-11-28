class TheLoai:
    def __init__(self, index, typeName):
        self.id = f"TL{index+1:03d}"
        self.typeName = typeName


class Phim:
    def __init__(self, index, idType, date, filmName, unit):
        self.filmId = f"P{index+1:03d}"
        self.idType = idType
        self.date = date
        self.filmName = filmName
        self.unit = unit
        self.type = next(theloai for theloai in types if theloai.id == idType)
        self.day = int(date[0:2])
        self.month = int(date[3:5])
        self.year = int(date[6:10])

    def __str__(self):
        return f"{self.filmId} {self.type.typeName} {self.date} {self.filmName} {self.unit}"


n, m = map(int, input().split())
types = []
for i in range(n):
    types.append(TheLoai(i, input().strip()))

films = []
for i in range(m):
    idType = input().strip()
    date = input().strip()
    filmName = input().strip()
    unit = int(input().strip())
    films.append(Phim(i, idType, date, filmName, unit))

films.sort(key=lambda x: (x.year, x.month, x.day, x.filmName, -x.unit))

for film in films:
    print(film)
