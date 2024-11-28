# HOUSE PRICE PREDICTION PROJECT
# Problem: Dự đoán giá bán của từng căn nhà
# Import Libraties
import pandas as pd
import numpy as np

data=pd.read_csv('./Python/Data Science Learning/data/train.csv',index_col='Id')
print(data.head())

# Chọn các đặc trưng và biến mục tiêu
features=["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr",
        "TotRmsAbvGrd"]

# Spliting the datasets into x and y
# x : data[features] (Chi lay nhung cot can thiet)
# y : target variable SalePrice(Du doan gia nha)
x=data[features]
y=data["SalePrice"]

# Khong dung toan bo data de train mo hinh may hoc( vi se dan den overfitting)
# Tach x,y thanh x_train,y_train
from sklearn.model_selection import train_test_split
x_train,x_valid,y_train,y_valid=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=0)
# random_state : de chac chan random ra ket qua giong nhau
# x_train,y_train de train mo hinh con x_valid,y_valid de test mo hinh may hoc


# Training Machine Learning model (Huấn luyện mô hình Decision Tree)
from sklearn.tree import DecisionTreeRegressor # DecisionTreeRegressor là cây cơ bản để quyết định
dt_model = DecisionTreeRegressor(random_state=1)
# Dua data vao dt_model
dt_model.fit(x_train,y_train)
y_preds = dt_model.predict(x_valid)

#print(pd.DataFrame({'y' : y_valid.head(), 'y_preds' : y_preds}))


from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
# RandomForestRegressor : Random Forest là một loại mô hình học máy được xây dựng dựa trên các cây
# GradientBoostingRegressor : Gradient Boosting là một thuật toán học máy được sử dụng để xây
# dựng các mô hình dự đoán. Thuật toán này sử dụng một tập hợp các mô hình
# được gọi là các cây quyết định để dự đoán giá trị của một biến mục tiêu.
# Huấn luyện mô hình Random Forest
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(x_train,y_train)
rf_val_preds = rf_model.predict(x_valid)

# Predict with a new inputo
print(rf_model.predict([[6969,2021,1000,800,4,5,8]]))

# Huấn luyện mô hình Gradient Boosting
gb_model = GradientBoostingRegressor(random_state=1)
gb_model.fit(x_train, y_train)
gb_val_preds = gb_model.predict(x_valid.head())
print(pd.DataFrame({'y' : y_valid.head(), 'y_preds' : gb_val_preds}))



# Danh gia 1 mo hinh may hoc
from sklearn.metrics import mean_absolute_error,mean_squared_error
# Ham Đánh giá các mô hình
def evaluate_model(model_name, y_true, y_preds):
    mae = mean_absolute_error(y_true, y_preds) #Chênh lệch tuyệt đối tb
    rmse = np.sqrt(mean_squared_error(y_true, y_preds)) #căn bậc hai của trung bình các độ lệch bình phương giữa giá trị thực tế và giá trị dự đoán
    print(f"{model_name} - MAE: {mae:.2f}, RMSE: {rmse:.2f}")

# Đánh giá mô hình Decision Tree
evaluate_model('Decision Tree', y_valid, y_preds)
# Đánh giá mô hình Random Forest
evaluate_model('Random Forest', y_valid, rf_val_preds)
# Đánh giá mô hình Gradient Boosting
evaluate_model('Gradient Boosting', y_valid, gb_val_preds)