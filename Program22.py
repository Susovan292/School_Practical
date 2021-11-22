# Program to write data to file test.txt

f = open('res/test.txt', 'w')
f.write("We are writing \n")
f.write("data to a \n")
f.write("text file \n")
print("Data written to the file Successfully")
f.close()