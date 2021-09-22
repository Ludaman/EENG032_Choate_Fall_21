
# Python for Data Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Student: Jeff Choate
### Week 1: Lecture 3


## HW

# Write a conditional expression statement with, "if, elif and else." to check if my_string = "Hello World" is a string

my_string = "Hello World"
if type(my_string) == type(""):
    print("It is a String!")
elif  my_string == "Hello World":
    print("HELLO WORLD")
else:
    print("Else statemnet that doesnt get reached")


#   Write a list comprehension that returns all the keys in a dictionary
#    whose associated values are greater than zero.
#    -   The dictionary: `{'aa': 11, 'cc': 33, 'LESS Than': -55, 'bb': 22}`
#    - Output should be a list

d1 = {'aa': 11, 'cc': 33, 'LESS Than': -55, 'bb': 22}
newList = [x for x,y in d1.items() if y>0]
print(newList)

#   Write a list comprehension that produces even integers from 0 to 10.
#        Use a `for` statement to iterate over those values and print results to screen.

intsOneToTen = list(range(0,11,2))
print(intsOneToTen)
# with list comprehension
intsOneToTen = [x for x in range(11) if x%2==0]
print(intsOneToTen)

#   Write a list comprehension that iterates over two lists and produces
#            all the combinations of items from the lists.
listOne = ["one", "two", "three", "four"]
listTwo = ["11", "22", "33", "44"]
listThree = [x+y for x in listOne for y in listTwo]
print(listThree)


#   Using `break`, write a `while` statement that
#                prints integers from zero to 5.
x = 0
while True:
    print(x)
    x+=1
    if x>5:
        break


#   Using `continue` , write a `while` statement
#      that processes only even integers from 0 to 10. Note: `%` is the
#      modulo operator. 

x=0
while x<11:

    if x%2 ==0:
        x+=1
        continue
    else:
        x+=1
        print("processing ", x )