class KhachHang:
    def __init__(self, idx, ten, loai, chiSoDau, chiSoCuoi):
        self.id = f"KH{idx+1:02d}"
        self.ten = self.xuLyTen(ten)
        self.loai = loai
        self.chiSoDau = chiSoDau
        self.chiSoCuoi = chiSoCuoi
        self.soDien = self.chiSoCuoi - self.chiSoDau
        if self.loai == "A":
            self.dinhMuc = 100
        elif self.loai == "B":
            self.dinhMuc = 500
        else:
            self.dinhMuc = 200
        self.tienTrongDinhMuc = min(self.soDien, self.dinhMuc) * 450
        self.tienVuotDinhMuc = max(self.soDien - self.dinhMuc, 0) * 1000
        self.vat = self.tienVuotDinhMuc // 20
        self.tongTien = self.tienTrongDinhMuc + self.tienVuotDinhMuc + self.vat

    def xuLyTen(self, name):
        s = [word.capitalize() for word in name.split()]
        return " ".join(s)

    def __str__(self):
        return f"{self.id} {self.ten} {self.tienTrongDinhMuc} {self.tienVuotDinhMuc} {self.vat} {self.tongTien}"


n = int(input())
dskh = []
for i in range(n):
    ten = input()
    loai, chiSoDau, chiSoCuoi = input().split()
    chiSoDau = int(chiSoDau)
    chiSoCuoi = int(chiSoCuoi)
    dskh.append(KhachHang(i, ten, loai, chiSoDau, chiSoCuoi))

dskh.sort(key=lambda x: (-x.tongTien))
print(*dskh, sep="\n")
