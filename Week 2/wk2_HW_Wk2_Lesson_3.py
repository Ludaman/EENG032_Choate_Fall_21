# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
#Homework for Major Jeff Choate

## Week 2 Lesson 3
from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
## HW
#Why is np.transpose(img, (1, 0, 2)) NOT the same as np.rot90(img)
img = imread("classlogo.png")
print("SHAPE")
print(img.shape)
transposedIMG = np.transpose(img, (1,0,2)).copy()##swaps column 1 and column 0, leave 2 where it is because that is the color part
rotatedIMG = np.rot90(img).copy()
plt.figure("Transposed Image")
plt.imshow(transposedIMG)
plt.figure("Rotated Image")
plt.imshow(rotatedIMG)
plt.figure("ORIGINAL Image")
plt.imshow(img)
plt.show()
plt.close()

#ANSWER to question 1:
#transpose swaps column 1 and 0, which creates a mirror image of the image which is also rotated, but rotate simply rotates the image without seemingly reversing some of it.



##HW

#Use a *for* loop to create the figures in the following code.

#```python
#import matplotlib.pyplot as plt
#from matplotlib.image import imread 
#import numpy as np
#file_nm = "../images/ant_logo.png"
##img = imread(file_nm) ## Note we do not have to close this
#img.shape #(500,300,4) Look an alpha channel
# Lets view it But rotated
#A = np.transpose(img, (1, 0, 2)).copy()
#B = np.rot90(img).copy()  ## We need to copy() here if we want a new object
#plt.figure("A")
#plt.imshow(A) #Make an image plot object
#plt.figure("B")
#plt.imshow(B) #Make an image plot object
#plt.figure("Ant Logo")
##plt.imshow(img)
#plt.show()  # Display it to screen
#plt.close()  # Make sure everything is closed
#```

imageDict = dict()
imageDict["Original_Image"] = img
imageDict["Transposed_Image"] = transposedIMG
imageDict["Rotated_Image"] = rotatedIMG
print(imageDict)
for img_name, img_i in imageDict.items():
    plt.figure(img_name)
    plt.imshow(img_i)
plt.show()
plt.close()


## HW

#When importing the following: numpy and pandas, what is the common alias used.

# numpy is typically np
# pandas is typically pd