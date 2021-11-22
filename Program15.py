# Program to write structured list in the cinary file.

import pickle

def func():
    lst = [10, 20, 30, 40]
    with open("res/Program15.bin",'wb') as f:
        pickle.dump(lst, f)
        print("List added to binary file !")


func()