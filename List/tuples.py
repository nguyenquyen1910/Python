# Tuples la bat bien va khong the thay doi sau khi khoi tao
# De thuan tien hon nen chuyen ve list

v=('Orange','Apple','Mango','Watermelon','Banana','Cherry')
v=v+('Lemon',)
v1=v*2
v_list=list(v)
v_list.sort()
#print(len(v))
#print(type(v))
cnt=0
for i in v_list:
    if 'water' in i.lower():
        cnt+=1
        #print(i,end=' ')
#print(v[2:5])

# Cong 2 tuples
v1=('Kiwi',)
v+=v1

 
# Remove an item
a=list(v)
a.remove('Apple')


# Gan item cho bien
fruits=('guava','banana','cherry')
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

# Using Asterisk
# Mot tuples khong the chua 2 Asterisk
fruits=('banana','orange','guava','cherry','anavoda')
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red) # Luu lai tat ca cac phan tu con lai cua tuple(*red)


# While in tuple
vehicle_tuple=('motobike','bycle','car','truck')
i=0
while i < len(vehicle_tuple):
    print(vehicle_tuple[i])
    i+=1
print(vehicle_tuple.count())