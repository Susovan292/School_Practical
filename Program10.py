# Write a function to find factorial of a given number. The function should return
#  the calculated factorial using return statement.


def fact(num):
    result = 1
    while num > 1:
        result = result * num
        num = num-1
    return result

a = fact(int(input("Enter a number to find the factorial : ")))
print("The factorial is",a)
