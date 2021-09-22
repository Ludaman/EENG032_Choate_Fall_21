# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Week 2 Lesson 1

## Pr 1

#Create a python script ***file*** (example: Pr1_WK2.py), that when executed prints to screen.
print("Hello")
#```bash
#Hello problem 1 from Week 2 Lesson 1.
#```

## Pr 2

#Explain why you should ALWAYS have a .gitignore file in your repo.
#You should always have a Git ignore file in your repo to prevent sensitive data from being uploaded to GitHub or other insecure services.  
#Additionally, you should use GIT ignore to avoid large data sets or items that benefit from being colocated with your code but do not benefit from version control; i.e. unchanging files.


## Pr 3

#Using `open` , create a new file that records user input 
#(min 1, max 4 inputs) and then opens that files and APPENDS the following
#"Received User Input"

import sys
f = open("test.txt", 'a')
i=0
print("PLease enter some text, if you type EXIT then text entries will stop, max of 4 entries")

for line in sys.stdin:
    if line.upper() == "EXIT" or i>=3:
        break
    i+=1
    f.write(line)
f.write("Received User Input")
print("All text entered, writing to file and continueing execution")
f.close()

## Pr 4

#repeat # 3 with a `with`

with open("test.txt", 'a') as f2:
    i=0
    print("PLease enter some text, if you type EXIT then text entries will stop, max of 4 entries")

    for line in sys.stdin:
        if line.upper() == "EXIT" or i>=3:
            break
        i+=1
        f2.write(line)
    f2.write("Received User Input")
    print("All text entered, writing to file and continueing execution")

## Pr 5

#* Create a new git repo in github.
#* Populate it with typical files and directories (.gitignore and README.md)
#* Commit your changes.
#* Push it to your repository

#<br>

## Sidebar

### Why have a github account?

#* Industry and some government jobs check your github account to see if you
#  really do know that software language.
#* It free and a nice place to store software you used and like.
#* You can help contribute to open data!