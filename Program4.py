# Write a program to calculate and display the difference of two inputed numbers 

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if n1>n2:
    diff = n1-n2
else:
    diff = n2-n1

print("The difference of {0} and {1} is {2}".format(n1, n2, diff)) 
