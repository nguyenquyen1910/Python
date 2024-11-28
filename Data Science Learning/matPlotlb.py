import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ve 1 do thi
plt.style.use('dark_background')
plt.plot()
x=[1,2,3,4]
y=[10,8,6,9]


# Pyplot API vs Object-Oriented(OO) API
# Pyplot API - Quickly
# Object-Oriented(OO) API - advanced

# Pyplot API
x=np.linspace(0,10,1000) # Tao ra array
plt.title("sin(x) and cos(x)") # Ten cua do thi
plt.plot(x,np.sin(x),color="blue",linestyle="dashed",label="sin(x)") # Tao do thi hinh sin
plt.plot(x,np.cos(x),label="cos(x)")
plt.xlabel("Bien X") # Them mo ta cho truc x
plt.ylabel("Sin(X)") # Them mo ta cho truc y
#plt.xlim([0,4]) # Gioi han do thi tu 0 - 4 cua X
plt.axis([0,4,-1,1]) # Cach gioi han khac
plt.legend() # Phan biet do thi


# Object-Oriented(OO) API
#1 Prepare Data
x=[1,2,3,4]
y=[11,22,33,44]
#2 Setup plot
fig,ax = plt.subplots(figsize=(5,5)) # Figure size = width $ Height of the plot
# Fig: hinh tong; Ax: hinh nho
#3 Plot the data
ax.plot(x,y)
ax.set(title="A Simple Plot", xlabel="x-axis", ylabel="y-axis") # Set up name, xlable, ylable for plot


# 1 so plot trong matplotlib
# Line
x=np.linspace(0,10,100)
fig,ax = plt.subplots() # Figure size = width $ Height of the plot
ax.plot(x,x**3) # y = x^3

# Scatter (Bieu do phan tan)
plt.scatter(x,np.exp(x)) # y = e^x
# OO API
rng=np.random.RandomState(0) # giong nhu seed(giu nguyen random)
x=rng.randn(100)
y=rng.randn(100)
colors=rng.randn(100) # random mau cho gia tri
sizes=1000*rng.randn(100) # Kich co cua gia tri
fig,ax = plt.subplots()
img1=ax.scatter(x,y,s=sizes,c=colors,cmap="viridis",alpha=0.4) # alpha se giam mo cho diem gia tri

fig.colorbar(img1) # Xem bang gia tri cua cac diem tren bieu do

# Bar (Bieu do cot)
# Vertical(Bieu do dung)
drink_price = {"Coca":10,
               "Pessi":12,
               "Sprite": 15}
fig,ax=plt.subplots()
ax.bar(drink_price.keys(),drink_price.values()) # Truc X la ten, y la gia
ax.set(title="Drink Prices",ylabel="Price ($)")

# Horizontal(Bieu do ngang)
# drink_price = {"Coca":10,
#                "Pessi":12, 
#                "Sprite": 15}
# fig,ax=plt.subplots()
# ax.barh(list(drink_price.keys()),list(drink_price.values())) # Truc X la ten, y la gia(Phai list ra neu dung o dang nay)
# ax.set(title="Drink Prices",ylabel="Price ($)")

# Histogram(Bieu do cot phan phoi tan suat)
# Prepare data
np.random.seed(42) # Tao ra cung 1 loai du lieu
student_height=np.random.normal(170,10,250) # Chieu cao TB 170, do lech chuan 10, 250 hoc sinh
#plt.hist(student_height) # pyplot API
fig,ax=plt.subplots()
ax.hist(student_height,bins=30) # OO API

# Phuong phap OO API tuong ung voi 1 do thi phu deu co 1 axis di kem de de lam viec hon(loi the hon)






plt.show()