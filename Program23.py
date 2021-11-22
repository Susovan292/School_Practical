# Write a program to create a csv file to store data (Rollno, Name, Marks). Obtain data from user and write % records into the file.

import csv


fh = open('res/Students.csv', 'w')
writer = csv.writer(fh)
writer.writerow(['Rollno', "Name", "Marks"])

for i in range(5):
    print("Student record ", i+1)
    rollno = int(input("Enter rollNo : "))
    name = input("Enter name : ")
    marks = float(input("Enter marks : "))
    rec = [rollno, name, marks]
    writer.writerow(rec)

fh.close()
print("Data saved")