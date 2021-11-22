# Write a python code to calculate simple intrest and amount payable by inputing the value of principal
# amount and rate from the user for a time period of 5 years.

principal = eval(input("Enter the value of principal : "))
rate = eval(input("Enter the annual rate of intrest : "))
time = 5
simple_intrest = principal * rate * time /100
amount = principal + simple_intrest

print("Simple Intrest = ", simple_intrest)
print("Amount Payable = ", amount)
