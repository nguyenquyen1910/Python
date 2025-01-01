class PhongBan:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten


class NhanVien:
    def __init__(self, ma, ten, luong, soNgay):
        self.ma = ma
        self.ten = ten
        self.luong = luong
        self.soNgay = soNgay
        self.phong = next(phong for phong in listPhong if phong.ma == ma[-2:])
        self.heSo = self.tinhHeSo()
        self.tongLuong = self.luong * self.soNgay * self.heSo * 1000

    def tinhHeSo(self):
        if self.ma[0] == "A":
            soNam = int(self.ma[1:3])
            if 1 <= soNam <= 3:
                return 10
            if 4 <= soNam <= 8:
                return 12
            if 9 <= soNam <= 15:
                return 14
            return 20
        if self.ma[0] == "B":
            soNam = int(self.ma[1:3])
            if 1 <= soNam <= 3:
                return 10
            if 4 <= soNam <= 8:
                return 11
            if 9 <= soNam <= 15:
                return 13
            return 16
        if self.ma[0] == "C":
            soNam = int(self.ma[1:3])
            if 1 <= soNam <= 3:
                return 9
            if 4 <= soNam <= 8:
                return 10
            if 9 <= soNam <= 15:
                return 12
            return 14
        if self.ma[0] == "D":
            soNam = int(self.ma[1:3])
            if 1 <= soNam <= 3:
                return 8
            if 4 <= soNam <= 8:
                return 9
            if 9 <= soNam <= 15:
                return 11
            return 13

    def __str__(self):
        return f"{self.ma} {self.ten} {self.phong.ten} {self.tongLuong}"


listPhong = []
n = int(input())
for _ in range(n):
    ma, ten = input().split(" ", 1)
    listPhong.append(PhongBan(ma, ten))

m = int(input())
listNhanVien = []
for _ in range(m):
    ma = input().strip()
    ten = input().strip()
    luong = int(input().strip())
    soNgay = int(input().strip())
    listNhanVien.append(NhanVien(ma, ten, luong, soNgay))

print(*listNhanVien, sep="\n")
