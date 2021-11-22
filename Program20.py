# Program to copy the content of a file to another file.

def filecopy(file1, file2):
    f1 = open("res/"+file1, 'r')
    f2 = open("res/"+file2, 'w')
    line = f1.readline()
    while line != '':
        f2.write(line)
        line = f1.readline()
    f1.close()
    f2.close()

def main():
    File_name_1 = input("Enter the source file name : ")
    File_name_2 = input("Enter the destination file name : ")

    filecopy(File_name_1, File_name_2)

if __name__ == "__main__":
    main()