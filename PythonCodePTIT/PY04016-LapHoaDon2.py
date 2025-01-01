import datetime


class Customer:
    def __init__(self, index, name, roomId, checkIn, checkOut, fee):
        self.id = f"KH{index+1:02d}"
        self.name = name
        self.roomId = roomId
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.fee = fee
        self.price = self.solvePrice()
        self.day = self.solveQuantityDay()
        self.totalAmount = self.price * self.day + self.fee

    def solvePrice(self):
        if self.roomId.startswith("1"):
            return 25
        if self.roomId.startswith("2"):
            return 34
        if self.roomId.startswith("3"):
            return 50
        return 80

    def solveQuantityDay(self):
        dayStart = datetime.datetime.strptime(self.checkIn, "%d/%m/%Y")
        dayEnd = datetime.datetime.strptime(self.checkOut, "%d/%m/%Y")
        return max((dayEnd - dayStart).days + 1, 1)

    def __str__(self):
        return f"{self.id} {self.name} {self.roomId} {self.day} {self.totalAmount}"


customers = []
n = int(input())
for i in range(n):
    name = input().strip()
    roomId = input().strip()
    checkIn = input().strip()
    checkOut = input().strip()
    fee = int(input().strip())
    customers.append(Customer(i, name, roomId, checkIn, checkOut, fee))

customers.sort(key=lambda x: (-x.totalAmount))
print(*customers, sep="\n")
