class Invoice:
    def __init__(self, id, name, quantity, price, discount):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.totalAmount = self.price * self.quantity - self.discount

    def __str__(self):
        return f"{self.id} {self.name} {self.quantity} {self.price} {self.discount} {self.totalAmount}"


n = int(input())
listInvoices = []

for _ in range(n):
    id = input().strip()
    name = input().strip()
    quantity = int(input().strip())
    price = int(input().strip())
    discount = int(input().strip())
    listInvoices.append(Invoice(id, name, quantity, price, discount))

listInvoices.sort(key=lambda x: (-x.totalAmount))

for invoice in listInvoices:
    print(invoice)
