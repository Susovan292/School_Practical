# The data of winner of four rounds of a competitive programing competition is gives as:

# ['Name', 'Points', 'Rank']
# ['Susovan', 1000, 100]
# ['Binod', 2000, 200]


# Write a program to save the above data in results.csv file in res folder

import csv

fh = open("res/Results.csv", 'w')
writer = csv.writer(fh)
compdata = [
    ['Name', 'Points', 'Rank'],
    ['Susovan', 1000, 100],
    ['Binod', 2000, 200]
]
writer.writerows(compdata)
fh.close()
print("Data imported")