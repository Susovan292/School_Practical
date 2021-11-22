# To illustrate read(x) by reading only the first 10 charcters from the file Program12.txt in res folder

f = open('res/Program12.txt', 'r')
data = f.read(10)
print(data)
f.close()