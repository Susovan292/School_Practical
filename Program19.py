# To illustrate read() by reading the entire data from a file Program12.txt from res folder

f = open('res/Program12.txt', 'r')
data = f.read()
print(data)
f.close()