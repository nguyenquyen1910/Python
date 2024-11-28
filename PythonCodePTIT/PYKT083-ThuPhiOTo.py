from collections import defaultdict


class PhuongTien:
    def __init__(self, idNum="", typeVehicle="", quantity=0, status="", date=""):
        self.idNum = idNum
        self.typeVehicle = typeVehicle
        self.quantity = quantity
        self.status = status
        self.date = date
        self.fee = self.feeSolve()

    def feeSolve(self):
        if self.status == "IN":
            if self.typeVehicle == "Xe_con":
                return 10000 if self.quantity == 5 else 15000
            elif self.typeVehicle == "Xe_tai":
                return 20000
            else:
                return 50000 if self.quantity == 29 else 70000
        return 0


class QuanLyThuPhi:
    def __init__(self):
        self.totalFee = defaultdict(int)

    def solveNumberOfMoves(self, vehicle):
        if vehicle.status == "IN":
            self.totalFee[vehicle.date] += vehicle.fee

    def printTotalFee(self):
        for date, totalFee in self.totalFee.items():
            print(f"{date}: {totalFee}")


n = int(input())
quanly = QuanLyThuPhi()
for _ in range(n):
    idNum, typeVehicle, quantity, status, date = input().split()
    quantity = int(quantity)
    vehicle = PhuongTien(idNum, typeVehicle, quantity, status, date)
    quanly.solveNumberOfMoves(vehicle)

quanly.printTotalFee()
