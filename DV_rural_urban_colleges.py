import pandas as pd 
from matplotlib import pyplot as plt 
import os
from matplotlib import style

Rural = 0
Urban = 0

df = pd.read_csv('scraped_final.csv', index_col=1)

for data in df["region_type"].values:
    if data =="Rural":
        Rural+=1
    if data =="Urban":
        Urban+=1

print(Rural, Urban) 

plt.bar([1],[Rural], label="Rural")
plt.bar([2],[Urban], label="Urban", color='g')

plt.title('Number of universities in rural and urban areas')
plt.legend()
plt.ylabel('Number Of Colleges')
plt.xlabel('Region Type')

plt.grid(True)

plt.show()