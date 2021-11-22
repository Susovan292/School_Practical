# Program to display the contents of the file starting from 2nd charcter into the list.

f = open("res/Program12.txt", 'r')
print(f.read(2))
print(f.readlines())
print(f.read(3))
print("Reading data")
print(f.read())
f.close()