# Tien xu ly du lieu(Lam sach du lieu, ma hoa thanh dang so hoc)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Dataset
# Gom 4 cot la quoc tich, luong, tuoi, co mua hang hay khong
data_fr=pd.read_csv('./Python/Data Science Learning/data/Data.csv')
print(data_fr.head())

# Missing Data Replacement: Thay the du lieu bi thieu
for col in data_fr.columns:
    missing_data=data_fr[col].isna().sum() # Tra lai cac hang co gia tri thieu
    missing_percent=missing_data/len(data_fr)*100
    print(f'Column : {col}: has {missing_percent}% missing data')
fig,ax=plt.subplots(figsize=(10,8))
sns.heatmap(data_fr.isna(),cmap="Blues")
x=data_fr.iloc[:,:-1].values # Cat cot cuoi cung
y=data_fr.iloc[:,-1].values

# Xu ly cac du lieu bi thieu trong dataset
from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=np.nan,strategy="mean") # Mension cac gia tri Nan 
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3]) # Thay the gia tri Nan bang gia tri mean(trung binh) cua cac gia tri


# Mã hóa các dữ liệu danh mục (Encode Categorical Data)
# Encode Independent variable (Ma hoa doc lap)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# Ma hoa Country thanh dang float
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder="passthrough")
# [0] la column muon transform
# passthrough : 2 column k can lam gi ca
x=ct.fit_transform(x)

# Ma hoa cho y tu Yes><No thanh dang 1><0
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y=le.fit_transform(y)


# Tach dataset thanh Training set va Test set
from sklearn.model_selection import train_test_split
np.random.seed(42) # Xet seed de chac chan random ra cung 1 ket qua
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) # Vì nó sẽ lấy random 20% dòng bất kì để test
# x_train ,x_test,y_train,y_test luon di cung nhau 1 cap


# Feater Scaling(đưa col age và col salary về cùng 1 thang đo, vì sự chênh lệch quá lớn của nó)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:,3:]=sc.fit_transform(x_train[:,3:])
x_test[:,3:]=sc.transform(x_test[:,3:])
print(x_test)