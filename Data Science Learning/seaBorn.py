import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Numerical Plots (Do thi phan phoi)
tips_df=sns.load_dataset('tips')
print(tips_df.head())

# Styling(Thay doi theme khac nhau)

sns.set_theme() # Apply the default theme

sns.histplot(data=tips_df["total_bill"])

tips_df["total_bill"].value_counts().sort_values(ascending=False)


# KDE(kernel density estimate) : So do truc quan hoa du lieu

sns.kdeplot(data=tips_df['total_bill'])


# Displot (tich hop giua Histogram va KDE)

sns.displot(data=tips_df,x="total_bill",kde=True,col="time") # Phan ra thoi gian trua va toi


# Bar Plots (Bieu do cot)

sns.barplot(data=tips_df,x="sex",y="tip",estimator=np.mean) # Phan ra theo nam hoac nu

# Count Plot
tips_df["sex"].value_counts()

sns.countplot(data=tips_df,x="sex") # Bieu do the hien so luong nam nu

#Box Plot (Giup ta thay duoc data trai ra nhu the nao)

sns.boxplot(data=tips_df,x="day",y="total_bill",hue="sex") # Bieu do phan bo tong tien bill theo ngay (dinh kem them cot sex)
plt.legend(loc=0)


# Facet Grid (Cho phep ve len den so luong data lon)

tip_fg=sns.FacetGrid(data=tips_df,row="smoker",col="time") # Tao 1 class la Facet Frid class
tip_fg.map(sns.scatterplot,'total_bill','tip') # Se phan du lieu total_bill and tip ra theo 4 truong hop cua smoker and time

kws=dict(s=100,edgecolor='b',alpha=.7) # Bien thay doi kich thuoc, mau, do mo
new_fg=sns.FacetGrid(data=tips_df,col="sex",hue="smoker",
                     col_order=["Female","Male"],
                     palette='Set2',
                     height=4,aspect=1.4)
# col_order : de thay doi thu tu cua Female len truoc Male
# palette : doi mau cua bieu do
# height, aspect : thay doi do dai 2 truc cua bieu do

new_fg.map(sns.scatterplot,'total_bill','tip',**kws) # Dua ta moi tuong quan total_bill va tip theo gioi tinh
new_fg.add_legend()


# Joint Plot (Phan bo giua 2 bien voi nhau)
# Data moi
penguins_df = sns.load_dataset('penguins')
print(penguins_df.head(5))

sns.jointplot(data=penguins_df,x="flipper_length_mm",y="bill_length_mm",hue="species") # Tim su tuong quan giua flipper_length_mm va bill_length_mm(phan bo theo loai(species))

# Ở thực tế rất khó tìm được cột nào tương quan cột nào
# Sử dụng pair plot để ghép giữa 2 cặp bien

# Pair Plot
sns.pairplot(data=penguins_df,hue="species")

# Heatmaps (Muc do tuong quan(Bieu do nhiet))
# Biểu diễn cường độ và mức độ khác nhau của dữ liệu, sự bất thường
# New Data

flights_df=sns.load_dataset('flights')
print(flights_df.head(5))

flights=pd.pivot_table(flights_df,index='month',columns='year',values='passengers') # Thong ke so khach hang theo nam va thang
print(flights)

sns.heatmap(data=flights,cmap='Blues')






plt.show()