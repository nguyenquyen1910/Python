import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cities=pd.read_csv(r"C:\Users\PC\OneDrive\Workspace\CODE\Python\Data Science Learning\data\california_cities.csv")
print(cities.head(5))

# Extract Latd (Vi do) ; Longd (Kinh do)
lat,lon=cities['latd'],cities['longd']
population,area=cities['population_total'],cities['area_total_km2'].sort_values(ascending=False)

# Su dung bieu do roi rac 
plt.figure(figsize=(8,6))
plt.scatter(lon,lat,
            c=np.log10(population),cmap='viridis',
            s=area,linewidths=0,alpha=0.5)
plt.axis('equal') # Sua truc x va truc y bang nhau
plt.xlabel('longtatitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)') # Cong thuc cua log10
plt.clim(3,7) # Gioi han lai cua bieu do

# Tao khoang size cua area
area_range=[50,100,300,500]
for area in area_range:
    plt.scatter([],[],s=area,c='k',alpha=0.4,
                label=str(area)+'km$^2$')
plt.legend(labelspacing=0.7,title='City Area')


plt.title('California Cities: Population and Area Distribution') # Ten cua bieu do



plt.show()