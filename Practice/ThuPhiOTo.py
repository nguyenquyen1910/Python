class Vehicle:
    def __init__(self, id, name, seat, status, day):
        self.id = id
        self.name = name
        self.seat = seat
        self.status = status
        self.day = day
        if self.name == "Xe_con":
            if self.seat == 5:
                self.price = 10000
            else:
                self.price = 15000
        if self.name == "Xe_tai":
            self.price = 20000
        if self.name == "Xe_khach":
            if self.seat == 29:
                self.price = 50000
            else:
                self.price = 70000

n = int(input())
listVehicle = []
for _ in range(n):
    id, name, seat, status, day = map(str, input().split())
    seat = int(seat)
    listVehicle.append(Vehicle(id, name, seat, status, day))

map = {}
for vehicle in listVehicle:
    if vehicle.status == "IN":
        if vehicle.day not in map:
            map[vehicle.day] = 0
        map[vehicle.day] += vehicle.price

for key, value in map.items():
    print(f"{key}: {value}")