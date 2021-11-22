# Program to illustrate 'with' statement.

with open("res/Program14.txt" , 'w') as f:
    f.write("Hello World")
    print("Is file closed : ",f.closed)
print("Is file closed : ",f.closed)
