# Toan tu gan
a=100
b=200
a,b=b,a # swap a b
print(a,b)

# Toan tu toan hoc
c=10
print(c+c)
print(c/3) # Chia du
print(c//3) # Chia nguyen
print(c**3) # Luy thua

# Toan tu logic
a=[1,2,3]
b=[1,2,3]
print(a is b) # So sang 2 doi tuong

# Toan tu thanh vien
s='Nguyen Viet Quyen'
print('Quyen' in s) # Kiem tra xem 'Quyen' co thuoc s khong

# Nhap input cho nhieu bien 1 luc
x,y,z=map(int,input().split())
print(x+y+z)