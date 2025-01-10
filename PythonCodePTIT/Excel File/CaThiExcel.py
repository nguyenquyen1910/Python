import openpyxl
import datetime


class CaThi:
    idx = 1
    def __init__(self, day, time, room):
        self.id = f"C{CaThi.idx:03d}"
        CaThi.idx+=1
        self.day = day
        self.time = time
        self.room = room
        self.times = datetime.datetime.strptime(self.day+" "+self.time, "%d/%m/%Y %H:%M")

    def __str__(self):
        return f"{self.id} {self.day} {self.time} {self.room}"

data = openpyxl.load_workbook("cathi.xlsx")
sheet = data.active 

danh_sach = []
for i in sheet.iter_rows(min_row=2, values_only=True):
    day, time, room = i
    danh_sach.append(CaThi(day, time, room))

danh_sach.sort(key=lambda x: (x.times, x.id))
print(*danh_sach, sep="\n")