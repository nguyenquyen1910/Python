class DanhBa:
    def __init__(self, name="", phone="", date=""):
        self.name = name
        self.phone = phone
        self.date = date

    def __lt__(self, other):
        s_lastName = self.name.split()[-1]
        o_lastName = other.name.split()[-1]
        s_firstName = " ".join(self.name.split()[::-1])
        o_firstName = " ".join(other.name.split()[::-1])
        if s_lastName != o_lastName:
            return s_lastName < o_lastName
        else:
            return s_firstName < o_firstName

    def __str__(self):
        return f"{self.name}: {self.phone} {self.date}"


def checkDay(s):
    return "Ngay" in s


def checkPhone(s):
    return s.isdigit()


danhba = []
with open("SOTAY.txt", "r", encoding="utf-8") as file:
    preDate = ""
    prePhone = ""
    preName = ""
    for line in file:
        s = line.strip()
        if checkDay(s):
            preDate = s.split(" ")[1]
        elif checkPhone(s):
            prePhone = s
            db = DanhBa(preName, prePhone, preDate)
            danhba.append(db)
        else:
            preName = s

danhba.sort()

with open("DIENTHOAI.txt", "w", encoding="utf-8") as output_file:
    for db in danhba:
        output_file.write(str(db) + "\n")
