import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
cereal_df=pd.read_csv('./Python/Data Science Learning/data/cereal.csv')
# Data (thong ke data cua ngu coc)
# name : ten cua loai ngu coc
# mfr : ten nha san xuat
# fiber : chat xo
# carbo : carbohydrates
# sodium : natri
# potass : kali
# shelf : ke dung cac loai ngu coc nay
# cups : so coc dung trong 1 lan uong
# rating : xep hang danh gia
print(cereal_df.head())

# Mình focus vào những column đề cập đến dinh dưỡng
# Bỏ qua những column không có ý nghĩa dinh dưỡng(shelf, cup,rating)
fields=['name','mfr','type','shelf','weight','cups','rating']
cereal_df_new=cereal_df.drop(fields,axis=1)
print(cereal_df_new.head())


# Corr() : Tính toán ma trận tương quan giữa các cột số học
cereal_corr=cereal_df_new.corr() # Get correlation data(Tim su tuong quan du lieu)
adjusted_cereal_corr=cereal_corr.iloc[1:,:-1]
print(cereal_corr)

ones_corr=np.ones_like(cereal_corr,dtype=bool) # Danh gia su tuong quan qua boolean
# np's triu : tra ve 1 nua True, 1 nua False (Vi 2 nua tren va nua duoi doi xung nhau nen chi ve nua duoi)
mask=np.triu(ones_corr)
adjusted_mask=mask[1:,:-1] # Khong lay hang dau tien va cot cuoi cung 
fig,ax=plt.subplots(figsize=(10,8)) # Phong to bieu do
sns.heatmap(data=adjusted_cereal_corr,mask=adjusted_mask,
            annot=True,fmt=".2f",
            cmap="Blues",linecolor="white",
            linewidths=0.5) # ve bang heatmap de thay su phan bo
# Annot de viet gia tri cu the len tung hinh
yticks=[i.upper() for i in adjusted_cereal_corr.index] # Them ten cua tung hang tung cot
xticks=[i.upper() for i in adjusted_cereal_corr.columns]
plt.show()