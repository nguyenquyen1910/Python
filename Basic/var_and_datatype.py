s=1000 # Python không có giới hạn số nguyên lớn
print(type(s))

# Khai báo số theo hệ cơ số
b=0b1101 # hệ cơ số 2(Binary)
print(b)
o=0o7656 # hệ cơ số 8(octal)
print(o)
h=0x1999 # hệ cơ số 16(hexal)
a=100.345656565 # số thực lưu có giới hạn khoảng 309 chữ số thập phân

# 3 cách in ra các số sau dấu phẩy
print('%.2f' % a)
print(round(a,2)) # co su lam tron(khong nen su dung)
print('{:.2f}'.format(a))


# So phuc
c=3+4j
print(type(c))
print(c.real) # in ra phan thuc
print(c.imag) # in ra phan ao

# string
str='Nguyen Viet Quyen'
print(str)
strl='''Nguyen
Viet
Quyen''' # String co nhieu dong
print(strl)

# Bool
t = True
print(bool(100)) # Cac gia tri khac khong deu la True
print(bool('Quyen')) # Cac xau khac ring deu la True    