import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical10\dalys-rate-from-all-causes.csv")

#some attemption
'''
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
print(dalys_data.iloc[0,3])
print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:5])
print(dalys_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])
print(dalys_data.loc[2:4,"Year"])
'''

print(dalys_data.iloc[0:10,2]) #the 10th year is 1999

#show DALYs for all countries in 1990
row = []
for x in range(len(dalys_data)):
    if dalys_data.loc[x,"Year"] == 1990: #use Boolean
        row.append(x) 
print(dalys_data.loc[row,"DALYs"])

uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
France = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]
sum1 = 0
sum2 = 0
for num in uk.DALYs:
    sum1 += float(num)
for num in France.DALYs:
    sum2 += float(num)
mean_uk = sum1/len(uk.DALYs)
mean_France = sum2/len(France.DALYs)
print(f"mean DALYs for the UK is {mean_uk}")
print(f"mean DALYs for the France is {mean_France}")
#It turned out that mean DALYs in the UK is greater than France.

plt.figure(figsize=(10, 6))
plt.plot(uk.Year, uk.DALYs, 'b+', label='UK')
plt.plot(France.Year, France.DALYs, 'r+', label='France')
plt.xticks(uk.Year,rotation=-90)
plt.title("Mean DALYs in the UK and France")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.legend() #show the label
plt.show()

#the coding of the question
list = []
for num in row: #based on the formal coding to search the countries in 1990
    list.append(dalys_data.loc[num,"DALYs"]) #use DALYs to sort
list.sort()
name = dalys_data.loc[dalys_data.DALYs == list[-1], ["Entity"]] #use dalys_data function to search the target Entity and put into name list
print(f"{name["Entity"].values[0]} has the highest DALYs: {list[-1]}.") #name is an object in Pandas, we can use a label to search the elecment
#Here, ["Entity"] refers to the colume that labeled "Entity", and value refers to all its values in list. So use [0] to pick out the content.