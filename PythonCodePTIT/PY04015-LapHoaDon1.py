class Customer:
    def __init__(self, index, name, oldNum, newNum):
        self.id = f"KH{index+1:02d}"
        self.name = name
        self.oldNum = oldNum
        self.newNum = newNum
        self.price = min(50, self.newNum - self.oldNum) * 100
        self.fee = round(self.price * 0.02)
        if self.newNum - self.oldNum > 50:
            self.price += min(50, self.newNum - self.oldNum - 50) * 150
            self.fee = round(self.price * 0.03)
        if self.newNum - self.oldNum > 100:
            self.price += (self.newNum - self.oldNum - 100) * 200
            self.fee = round(self.price * 0.05)
        self.totalAmount = self.price + self.fee

    def __str__(self):
        return f"{self.id} {self.name} {self.totalAmount}"


n = int(input())
customers = []
for i in range(n):
    name = input()
    oldNum = int(input())
    newNum = int(input())
    customer = Customer(i, name, oldNum, newNum)
    customers.append(customer)

customers.sort(key=lambda x: (-x.totalAmount))
for customer in customers:
    print(customer)
