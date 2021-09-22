print("WEEK 1: Lection 2 - Jeff Choate")


#list practice
# 
print("1.2 DICTIONARY PRACTICE")

a = list()
b = ["test", "test2", "test3","test4"]
#print(type(a))
#print(type(b))
#print(dir(a))
a.append("hello")
a.append(" ")
a.append("World")
a.append(" I WIN")
print(a)

#dictionary practice
print("1.3 DICTIONARY PRACTICE")

d = dict(zip(a, b))
print(d)

d["HW2"] = "Done"

print(d)

first = "firstName"
second = "secondName"

d2 = {first : second, "newName":"newSEcondsName"}
print(d2)


print("1.4 3 Strings")

stringOne = "helo'Bob"
stringTwo = 'GoodBye"Bob'
stringThree = "NOT \"NOW\" 'BOB'" #note both of these work
stringThree = 'NOT "NOW" \'BOB\''

print(stringOne, stringTwo, stringThree)


print("1.5  4 Strings Multi Line")

print("this is a \n multiline string \
    hear me roar")

print("1.6 5 Join")

aString="Hello"
bString="Goodbye"
listStrings = []
listStrings.append(aString)
listStrings.append(bString)

print(":".join(listStrings))

print("1.7  6 String Format")
lastName = "Choate"
firstName = "Jeff"
print("{}, {}".format(firstName, lastName))
full = '%s, %s' % (firstName, lastName)
print(full)