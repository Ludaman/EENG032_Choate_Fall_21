# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
##SUBMISSION For Major Jeff Choate

## Week 2 Lesson 2

## Problems
### 1

#Write a script that
#* generates an array of numbers from 16-100,000 with a stride of 4.
##* reshape it to a 2083 rows by 12 columns
#* print out the first 3 and last 3 rows

import numpy as np
import pandas as pd
newArray = np.arange(16, 100000, 4)

print("Verify new array by inspecting it")
print("First ten items")
print(newArray[:10])
print("Last ten items")
print(newArray[-1:-10:-1])
print("shape")
print(newArray.shape)
print("size")
print(newArray.size)

reshapeArray = newArray.reshape(2083,12)
print("First ten items RESHAPED ARRAY")
print(reshapeArray[:10])
print("Last ten items")
print(reshapeArray[-1:-10:-1])
print("shape")
print(reshapeArray.shape)
print("size")
print(reshapeArray.size)

print("checking by reference or value")
reshapeArray[0] = 44
reshapeArray[0][3] = 55

print("First ten items RESHAPED ARRAY")
print(reshapeArray[:10])
print("First ten items ORIGINAL ARRAY")
print(newArray[:100])

print("!!!!RESHAPED ARRAY IS REALLY PASSED BY REFERENCE AND NOT BY VALUE!!!!!")


### 2
#Build an numpy array WITH named types
namedTypeArray = np.array([[3, 4, 5.6],[1, 2.2, 3]])
print(namedTypeArray)
print(namedTypeArray.dtype)
newNamedArary = namedTypeArray.astype([('col1', 'int8'),('col2','int8'),('col3','float')])
print(namedTypeArray)
print(namedTypeArray.dtype)
print(newNamedArary)
print(newNamedArary.dtype)
print(newNamedArary['col1'])
print(newNamedArary['col2'])
print(newNamedArary['col3'])
newNamedArary = namedTypeArray.astype([('col1', 'int8')])
print(namedTypeArray)
print(namedTypeArray.dtype)
print(newNamedArary)
print(newNamedArary.dtype)
print(newNamedArary['col1'])

### 3
#Build a numpy array of ones called "A"
#* take a slice out and call that slice by variable "B".
#* multiply B by 5 or a slice of B by 5
#* print(A)
#* repeat above WITHOUT or WITH changing the value of "A"
A = np.ones([10,10])
print(A)
B = A[:5,5:]
B[:,:] = 5
print(B)
print(A)
##BUT THIS OPERATION DOES NOT WORK BECAUSE OF HOW IT COPIES THE ARRAY!
B = B+1#this copies it?  SHOULD use A.copy()
print(B)
print(A)


### 4
#Take the mode of the data in the last example
df_A =  pd.DataFrame(A)
print("A is:")
print(df_A)

print("MODE of A")
print(df_A.mode(1))
##INTERESTING that two rows or columns are returned (pending 1 or 0 as parameter) this is due to the fact there are TWO MODEs for the dataset!

### 5
#Read in a csv file but use dtype 'U5' for the header

fileLoc = "../../Data/Hawaii.csv"
someData  = np.genfromtxt(fileLoc, delimiter=",")
print("READ IN DATA SET FROM " ,  fileLoc)
print(someData)
header = np.genfromtxt(fileLoc, delimiter = ",", max_rows=1, dtype='U5')
print("HEADER")
print(header)
dataSet = np.genfromtxt(fileLoc, delimiter = ",", skip_header=1, names=header.tolist())
print("dataset")
print(dataSet)
