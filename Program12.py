# To read the lines from the file into list.

f = open("res/Program12.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line, end= "")
f.close()