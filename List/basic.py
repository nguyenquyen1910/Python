# List
# Gioi han boi cap ngoac vuong
# Cac phan tu cach nhau boi dau ,
# List co kha nang chua moi doi tuong cua python (bao gom ca no)
s='nguyen'
# Constructer list
a=list(s) # Tach cac chu trong list roi them vao list a
for i in a:
    if(i!='n'):
        print(i,end=' ')
print()
a=[1,2,3,4,5]


a.append(100) # Them 100 vao cuoi list
print(a)
a.insert(2,1000) # Them 1000 vao chi so 2
print(a)


a.pop(3) # Xoa phan tu o chi so 3
print(a)
a.pop() # Xoa phan tu cuoi cung
print(a)
del a[1] # Xoa phan tu co chi so 1 
print(a)
a.remove(1000) # Xoa phan tu co gia tri la 1000 dau tien ra khoi mang(Neu trong list khong co 1000 thi se bi loi)
#a.clear() # Xoa het tat ca phan tu
print(a)
a[2:4]=[] # Xoa cac phan tu tu chi so 2 den 3
print(a)


# Sao chep list
b=[0]*1000 # Tao mang co 1000 phan tu 0


a.reverse() # De lat nguoc 1 list(O(n))
print(a)


a.sort() # Sap xep(O(nlogn))
print(a)


b=sorted(a) # Tra ve mang b da duoc sap xep tu mang a
print(b)
print(min(a))
print(max(a))
print(sum(a))

# Khai bao list theo for
a=[i for i in range(30)] # Tao ra 0->30
print(a)

a=[[n,n*2,n*3] for n in range(1,4)]
print(a)

# List Slicing
#a[start : stop : step]
a=[10,20,30,40,50]
b=a[2 : 5]
print(b)

a=[10,20,30,'Quyen','Viet']
b=a[::-1] # Lat nguoc list
print(b)

# Chen nhanh vao dau,cuoi
a=['a','b','c']
a[:0]=[10,20,30] # Chen vao dau
print(a)
a[len(a):] = [40,50,60]
print(a)
b=a[:] # Copy a thanh b
print(b)


# Function(tuong tu void)
def my_function():
    print('Hello!')

my_function()

# Function truyen tham so
def order_water(topping='dammit'):
    print('Have a ' + topping + ' lemon water!')
order_water()
order_water('jelly')