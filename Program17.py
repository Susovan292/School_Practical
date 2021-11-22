# To read data line by line using readline.

f = open('res/Program12.txt', 'r')
L1 = f.readline()
print(L1, end="")
L2 = f.readline()
print(L2, end="")
L3 = f.readline()
print(L3, end="")
f.close()