# Program to implement standard streams

import sys

f = open("res/Program12.txt", 'r')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stdout.write(line3)
