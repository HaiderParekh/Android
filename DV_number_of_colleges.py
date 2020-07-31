import pandas as pd 
from matplotlib import pyplot as plt 
import os
from matplotlib import style



Pune = 0
Nashik = 0
Aurangabad = 0 

df = pd.read_csv('scraped_final.csv', index_col=1)

for data in df["region"].values:
    if data =="Pune":
        Pune+=1
    if data =="Nashik":
        Nashik+=1
    if data =="Aurangabad":
        Aurangabad+=1

print(Pune, Nashik, Aurangabad)

plt.bar([1],[Pune], label="Pune")
plt.bar([2],[Nashik], label="Nashik", color='g')
plt.bar([3],[Aurangabad], label="Aurangabad", color='y')


plt.title('Number of universities in each city')
plt.legend()
plt.ylabel('Number Of Colleges')
plt.xlabel('City')

plt.grid(True)

plt.show()