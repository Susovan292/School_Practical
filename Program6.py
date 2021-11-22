# Write a python module to display square root using sqrt() function of math library.

import math

def cal_sqrt():
    num = float(input("Enter an number :"))
    sq_root = math.sqrt(num)
    print("The square root of", num, "is", sq_root)

cal_sqrt()