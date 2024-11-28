import numpy as np
import pandas as pd

# Numpy array co ban
np.array([1,2,3,4]) # Chuyen sang numpy array
np.array([3.14,4,3,2]) # Se chuyen tu integet->float(kieu du lieu cao hon)
np.array([1,2,3,4], dtype='float32') # Chuyen qua kieu du lieu float 32 bit
a1=np.array([[1,2,3],[2,3,4]])
a1.shape # Lay ra so dong va so cot array
a1.ndim # Tim so chieu cua mang array
a1.dtype # Tim kieu du lieu ben trong array
a1.size # Kich thuoc cua array

# Ham Build in co san
np.zeros([2,4],dtype=int) # Build 1 array co 2 dong 4 cot toan so 0
np.ones([3,5],dtype=int) # Build 1 array co 3 dong 5 cot toan so 1
np.arange(0,20,2) # Build 1 array cac so chan tu 0 den 19
np.full((3,5),6.9) # Build 1 array toan so 6.9
np.linspace(0,1,5) # Build 1 array chia deu cac so tu 0 den 1 ([0.   0.25 0.5  0.75 1.  ] day la output)

# Ham random
np.random.random((4,4)) # Random 1 array chay tu 0->1
np.random.rand(4,4) # Random 1 array chay tu 0->1
np.random.randint(0,100,(4,5)) # Random 1 array chay tu 0->100

#Array indexing
x1=np.random.randint(20,size=(3,4))
x1[1,2] = 6 # Truy cap vao x1[1][2]

#Slicing
x2=np.random.randint(20,size=10)
# print(x2)
# print(x2[2:5]) # Cat tu 2 den 5
# print(x2[::2]) # Lay ra cac phan tu cach nhau 2 chi so
# print(x1[::2,::1])

# Reshape of Array & Transpose
x3=np.arange(1,10)
x3=x3.reshape((3,3)) # Dat lai shape cho array

# Transpose(chuyen hang thanh cot va nguoc lai)
x4=np.array([[1,2,3],[3,4,5]])
x4=x4.T # Chuyen vi ma tran


# Array Concatenation and Splitting
x=np.array([1,2,3])
y=np.array([3,2,1])
np.concatenate((x,y)) # Noi 2 array theo hang

grid = np.array([[1,2,3],[4,5,6]])
np.concatenate((grid,grid), axis=1) # Noi theo hang theo cot
# Vstack
x=np.array([1,2,3])
grid = np.array([[1,2,3],[6,5,4]])
np.vstack((x,grid)) # Noi array voi grid theo cot(yeu cau cung so cot)
# Horizontally stack(hstack)
y=np.array([[99],
            [99]])
np.hstack((y,grid)) # Noi theo cot

# Splitting of Array
x=np.array([1,2,3,99,69,3,2,1])
x1,x2,x3=np.split(x,[3,5]) # Tach array theo khoang
# array x1 se bat dau tu 0 den 3...
# array x2 se bat dau tu 3 den 5...
# array x3 se bat dau tu 5 den cuoi


# Broadcasting and Vectorized 
a=np.arange(3)
a+5 # Broadcasting(cong moi thanh phan cho 5)
# No se tu dong them hang va cot de cung shape cho viec cong
b=np.ones((3,3))
a+b # No se tu dong them hang cot de cong(tru, nhan tuong tu)

# Manipulating & Comparing Arrays
list_num=[1,2,3]
ll=np.array(list_num)
sum(ll) # Ham cu python
np.sum(ll) # Ham cu numpy

#Tao 1 numpy array cuc ki lon
massive_array=np.random.random(10000)
sum(massive_array)
np.sum(massive_array) # Tinh nhanh hon nhieu lan voi so luong lon
np.mean(massive_array) # Tinh trung binh cua array
np.min(massive_array) # Tim min(tuong tu voi max)


# Statstics(Xac suat thong ke)
# Standard Deviation and Variance(Do lech chuan va phuong sai)
# Vi du ve du lieu chieu cao cac con cho
dog_height = [600,470,170,430,300]
dog_height = np.array(dog_height)
np.std(dog_height) # Do lech chuan (co the tinh bang can bac 2 cua phuong sai)
np.var(dog_height) # Phuong sai


# Sorting Arrays (dua tren thuat toan quick sort)
x=np.array([2,1,4,5,7,6,3])
np.sort(x)
np.argsort(x) # Sort theo chi so

#Sort theo rows or columns
np.random.seed(42) # De co the random giong nhau
MatA=np.random.randint(0,10,size=(4,6))
np.sort(MatA,axis=0) # Sort theo column
np.sort(MatA,axis=1) # Sort theo row


# Linear Algebra (Dai so tuyen tinh)
A=np.array([[1,2,3],
           [4,5,6],
           [6,7,8]])
B=np.array([[6,5],
            [4,3],
            [2,1]])
A.dot(B) # Hoac A @ B(Tinh tich vo huong A*B)


# Dot Product Example (Tinh huu dung cua tich vo huong)
np.random.seed(0)
sale_amounts=np.random.randint(20,size=(5,3))

# Tao 1 Dataframe(theo du lieu cua sale_amouts)
weekly_sales=pd.DataFrame(sale_amounts,index=["Mon","Tue","Wed","Thurs","Fri"],
                          columns=["Orange","Apple","Mango"])
print(weekly_sales)

# Create a price array
prices=np.array([10,8,12]) # Bang gia cua tung loai hoa qua
fruits_prices=pd.DataFrame(prices.reshape(1,3),index=["Prices"],
                           columns=["Orange","Apple","Mango"])
print(fruits_prices)
#Tinh tong gia tri da ban ra cua tung ngay
total_prices=weekly_sales @ prices.T

weekly_sales["Total Price"]=total_prices # don cot total price vao bang gia
print(weekly_sales)