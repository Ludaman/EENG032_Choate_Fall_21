# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
## Week 2 Lesson 4
#Homework for Major Jeff Choate

#Go to www.data.gov or any a data source of your choice.

#* download a dataset, and examine that data.
#* Do this for a json file and a csv file. 
### Downloaded data set on expense actuals from New york city, Here is description:
# This dataset contains agency summary level data for total and city funded expense actuals. The dollar amount fields are rounded to thousands. Data are from FY 2002 and updated once a year after annual expense numbers are final. Usually, they are updated along with the first quarter financial plan between October and December each year. 

import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd
import json
import matplotlib.pyplot as plt


dataset_CSV = pd.read_csv("Expense_Actuals.csv")
plt.scatter(x=dataset_CSV["FISCAL YEAR"], y=dataset_CSV["ALL FUNDS"])

#dataset_CSV.plot(x="FISCAL YEAR", y="ALL FUNDS")
#plt.show()
#print(dataset_CSV)

mean_All_Funds_Column = dataset_CSV["ALL FUNDS"].mean()
mode_All_Funds_Column = dataset_CSV["ALL FUNDS"].mode()
median_All_Funds_Column = dataset_CSV["ALL FUNDS"].median()

print("MEAN ", mean_All_Funds_Column)
print("MODE ", mode_All_Funds_Column)
print("MEDIAN ", median_All_Funds_Column)
print()
print(dataset_CSV["ALL FUNDS"])
print()

rawJSON = json.load(open("Expense_Actuals.json"))
dataset_JSON = pd.DataFrame(rawJSON["data"])
#print(dataset_JSON.iloc[12] )
#print(dataset_CSV['ALL_FUNDS'].keys() )
print(dataset_JSON[12])##BUT IT is an object not an int!!
print(dataset_JSON.dtypes)
dataset_JSON = dataset_JSON.astype({12:'int64'})
mean_All_Funds_Column = dataset_JSON[12].mean()
mode_All_Funds_Column = dataset_JSON[12].mode()
median_All_Funds_Column = dataset_JSON[12].median()
print(dataset_JSON.dtypes)#changed the data type of the column so now I can get mean mode and median of it

print("MEAN ", mean_All_Funds_Column)
print("MODE ", mode_All_Funds_Column)
print("MEDIAN ", median_All_Funds_Column)
#Example:
#    * Find the mean, median mode of a data attribution or 
#    * Plot the data  

 
  
  
#My go to is pandas to read in new data.  But, you can use any package(s) that you like.