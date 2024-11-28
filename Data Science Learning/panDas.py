import pandas as pd
import numpy as np

# Import Dataset
df = pd.read_csv(r"C:\Users\PC\OneDrive\Workspace\CODE\Python\AI Learning\chipotle.tsv", sep="\t")
print(df.head(5))  # Display the first 5 rows

# Dataset Overview (Tong quan du lieu)
df.info() # Doc thong tin cua tung dong
df.describe(include='all') # Lay thong tin cua tat ca cac column

# Select all rows with multiple conditions(Chon hang co nhieu dieu kien)
# Loc
a=df.loc[(df.quantity == 15) | (df.item_name=="Nantucket Nectar"),['order_id','quantity','item_name']] # Lay hang co quantity co gia tri la 15(co the ket hop dieu kien)

# Iloc
df.iloc[3:11] # Lay du lieu tu hang 3 den hang 10
X=df.iloc[3:5,:-1]

# Data Manipulation
# De thuan tien cho viec tinh toan
df.item_price = df.item_price.apply(lambda x : float(x.replace('$',''))) # Xoa ki tu $ o item_price chuyen qua dang so thuc
df["total_price"] = df["quantity"]*df["item_price"] # Them 1 cot total price
print(df.head())

revenue=df["total_price"].sum() # Tong gia thi doanh thu(tong total_price)

# Group By (Nhom cac item_name)
c=df.groupby("item_name")["quantity"].sum() # Tinh tong so luong item duoc order
c=c.sort_values(ascending=False) # Xep theo thu tu giam dan

count=df.item_name.nunique() # Tong so mon hang da duoc ban ra
