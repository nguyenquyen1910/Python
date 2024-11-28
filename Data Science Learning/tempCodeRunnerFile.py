ng, tuoi, co mua hang hay khong
data_fr=pd.read_csv('./Python/Data Science Learning/data/Data.csv')
print(data_fr.head())

# Missing Data Replacement
for col in data_fr.columns:
    missing_data=data_fr[col].isna().sum() # Tra lai cac hang co gia tri thieu
    missing_percent=missing_data/len(data_fr)*100
    print(f"Column : {col} has {mis