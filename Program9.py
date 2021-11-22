# Write a program that fills a list with numbers using randint()

from random import randint

def fill_list(first, limit_num, low, high):
    for i in range(limit_num):
        first.append(randint(low, high))

min = int(input("Enter a min val : "))
max = int(input("Enter a max val : "))
l = int(input("Enter limit : "))
a = []
fill_list(a, l, min, max)
print(a)