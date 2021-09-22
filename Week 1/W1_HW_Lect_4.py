# Python for Data Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Student: Jeff Choate
### Week 1: Lecture 4

# Write a function that takes a single argument, prints the value of
#    the argument, and returns the argument as a string.

def my_function(var1, var2="defauiltVar2"):
    print(var1, var2)

my_function("Hello")
my_function(44)
my_function("Goodbye", "John")



# Write a function that takes a variable number of arguments and
#    prints them all.

def my_Variable_Function(*var1):
    for x in var1:
        print("args: ", x)

my_Variable_Function("hello","goodbye"," WOOOT", "Weird")


# Write a function that prints the names and values of keyword
#    arguments passed to it.

def my_Keyword_Function(**var1):
    for key, value in var1.items():
        print(key, " ", value)

my_Keyword_Function(arg1 = "ARG1 HERE", arg4 = "ARG FOURTY FOURTY")
my_Keyword_Function()
# Write a python script (file) that prints your name as all lower case, upper case and proper capitalization.  
#   (Bonus) if you can pass in your name: input()? argparse? etc

firstName = "jeff"
lastName = "choate"
wholeName = " ".join([firstName,lastName])

def NameFunction(myName):
    print("ALL CAPS: ", wholeName.upper())
    print("all lower: ", wholeName.lower())
    print("First capital: ", wholeName.capitalize())
    print("Camel Case: ", wholeName.title())

NameFunction(wholeName)

firstName = input("Type First Name")
lastName = input("Tye Last Name")
wholeName = " ".join([firstName,lastName])

NameFunction(wholeName)