# To illustrate read(n) by reading only the first 10 characters from the file program11.txt in res folder

f = open("res/Program11.txt", 'r')
data = f.read(10)
print(data)
f.close()